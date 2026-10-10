# Instance: huggingface__transformers-21768

- Final resolved (evaluator, logs/huggingface__transformers-21768_result.json): True
- Run state: DONE
- One attempt. Duration 68.4 s, turns 8, actor cost $0.30163819999999997, container commands 4
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/huggingface__transformers-21768/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/huggingface__transformers-21768/repo. Consider the following issue description:

<issue_description>
Make schedulers picklable
### Feature request

Change lambda functions passed to `LambdaLR` in `get_constant_schedule`, `get_constant_schedule_with_warmup`, `get_linear_schedule_with_warmup`, `get_cosine_schedule_with_warmup`, `get_cosine_with_hard_restarts_schedule_with_warmup` and `get_polynomial_decay_schedule_with_warmup` to callable objects.

### Motivation

Python cannot serialize lambda and local functions. Torch created a workaround around this in their `state_dict` method of `LambdaLR` by not returning any non-picklable functions:
```python
        ...
        for idx, fn in enumerate(self.lr_lambdas):
            if not isinstance(fn, types.FunctionType):
                state_dict['lr_lambdas'][idx] = fn.__dict__.copy()

        return state_dict
```
While this approach is fine when LR schedule is constant and deterministic, it makes it impossible to change the schedule mid training dynamically using lambda functions since any changes will not be saved to checkpoints.

In my particular case I wanted to implement a dynamic LR schedule based on evaluation metrics. I've implemented a wrapper around `LambdaLR` that applies transformation `fn: float -> float` to existing LR schedule:
```python
class LambdaWrapper:

    def __init__(self, lr_lamda: Callable[[Union[float, int]], float], wrapper_function: Callable[[float], float]):
        self._wrapper_function = wrapper_function
        self._lr_lambda = lr_lamda

    def __call__(self, x: Union[float, int]):
        return self._wrapper_function(self._lr_lambda(x))


class DynamicScheduler:

    def __init__(self, lr_scheduler: LambdaLR):
        self._scheduler = lr_scheduler

    def __getattr__(self, item):
        # Calling the super class to avoid recursion
        return getattr(super(DynamicScheduler, self).__getattribute__('_scheduler'), item)

    def wrap_schedule(self, fn: Callable[[float], float]):
        """If you want this object to be picklable, pass only picklable callable objects as `fn`!"""
        wrappers_builder = partial(LambdaWrapper, wrapper_function=fn)  # wrap in callable object to preserve picklability
        self._scheduler.lr_lambdas = list(map(wrappers_builder, self._scheduler.lr_lambdas))
```
I've taken special care to preserve picklability, however, since `LambdaLR` instances created by `transformers` library hold lambda and local functions in them, pickling of `DynamicScheduler` (as well as it's state, which is the same as the wrapped `LambdaLR` state) fails.

While reimplementing dynamic scheduling with lambda functions will allow the `torch` workaround that handles lambda functions in scheduler, the whole point of dynamic scheduling will be lost since the complex dynamically constructed lambdas: `f_n(f_n-1(...f_1(schedule(x))...))` will fall back to their default state: `schedule(x)`.

Here is the callback I use to track evaluation metrics for anyone interested:
```python
def get_warmup_steps(args: TrainingArguments, state: TrainerState) -> int:
    return (
        args.warmup_steps
        if args.warmup_steps > 0
        else math.ceil(state.max_steps * args.warmup_ratio)
    )


class DecreaseLRTransformer:
    def __init__(self, decrease_ratio: float):
        if decrease_ratio < 0.0 or decrease_ratio > 1.0:
            raise ValueError('Decrease ratio should be within [1.0, 0.0]')
        self._decrease_ratio = decrease_ratio

    def __call__(self, lr: float):
        return self._decrease_ratio * lr


# Developer notice (may change in the future versions of transformers):
# All kwargs have the following fields set: model, tokenizer, optimizer, lr_scheduler, train_dataloader, eval_dataloader

class LRDecreaseCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that handles learning rate decrease based on evaluation metrics.
    """

    def __init__(self, decrease_ratio: float, patience: int, *, decrease_on_warmup: bool = False, decrease_threshold: float = 0.0):
        self._transformer = DecreaseLRTransformer(decrease_ratio)
        self._patience = patience
        self._decrease_on_warmup = decrease_on_warmup
        self._decrease_threshold = decrease_threshold

        self._failed_checks = 0

    def _metric_improved(self, new_metric: float, old_metric: float, *, greater_is_better: bool = True) -> bool:
        operator = np.greater if greater_is_better else np.less
        return operator(new_metric, old_metric) and abs(new_metric - old_metric) > self._decrease_threshold

    def check_metric_value(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, metric_value: float):
        # best_metric is set by code for load_best_model
        no_metric = (state.best_metric is None)

        warmup_steps = get_warmup_steps(args, state)
        skip_warmup = (self._decrease_on_warmup and warmup_steps >= state.global_step)

        if skip_warmup:
            return

        if no_metric or self._metric_improved(metric_value, state.best_metric, greater_is_better=args.greater_is_better):
            self._failed_checks = 0
            control.should_save = True
        else:
            self._failed_checks += 1

    def on_train_begin(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs):
        if args.metric_for_best_model is None:
            raise ValueError(f"{self.__class__.__name__} requires metric_for_best_model to be defined defined")

        if args.evaluation_strategy == IntervalStrategy.NO:
            raise ValueError(f"{self.__class__.__name__} requires IntervalStrategy of steps or epoch")

    def on_evaluate(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs):
        metrics: Dict[str, float] = kwargs['metrics']
        lr_scheduler = kwargs['lr_scheduler']
        if not isinstance(lr_scheduler, DynamicScheduler):
            logger.warning(f'{self.__class__.__name__} is not compatible with {lr_scheduler.__class__.__name__} scheduler! '
                           f'Wrap your scheduler with {DynamicScheduler.__class__.__name__} to change LR dynamically. '
                           f'{self.__class__.__name__} is disabled!')
            return

        metric_to_check = args.metric_for_best_model
        if not metric_to_check.startswith("eval_"):
            metric_to_check = f"eval_{metric_to_check}"
        metric_value = metrics.get(metric_to_check)

        if metric_value is None:
            logger.warning(f"{self.__class__.__name__} required metric_for_best_model, "
                           f"but did not find {metric_to_check} in evaluation metrics. {self.__class__.__name__} is disabled!")
            return

        self.check_metric_value(args, state, control, metric_value)
        if self._failed_checks >= self._patience:
            lr_scheduler.wrap_schedule(self._transformer)
            self._failed_checks = 0

    def on_log(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs):
        logs: Dict[str, float] = kwargs['logs']
        logs['lr_decrease_patience'] = (self._patience - self._failed_checks) / self._patience
``` 

### Your contribution

The simplest and the cleanest workaround would be to make the local functions global:

Intead of:
```python
def get_linear_schedule_with_warmup(optimizer, num_warmup_steps, num_training_steps, last_epoch=-1):
    def lr_lambda(current_step: int):
        if current_step < num_warmup_steps:
            return float(current_step) / float(max(1, num_warmup_steps))
        return max(
            0.0, float(num_training_steps - current_step) / float(max(1, num_training_steps - num_warmup_steps))
        )

    return LambdaLR(optimizer, lr_lambda, last_epoch)
```

Do this:
```python
def _linear_schedule_with_warmup_step(current_step: int, *, num_warmup_steps: int, num_training_steps: int) -> float:
      if current_step < num_warmup_steps:
          return float(current_step) / float(max(1, num_warmup_steps))
      return max(
          0.0, float(num_training_steps - current_step) / float(max(1, num_training_steps - num_warmup_steps))
      )

def get_linear_schedule_with_warmup(optimizer, num_warmup_steps, num_training_steps, last_epoch=-1):
    schedule = partial(_linear_schedule_with_warmup_step, num_warmup_steps=num_warmup_steps, num_training_steps=num_training_steps)
    return LambdaLR(optimizer, schedule, last_epoch)
```
When created with global functions, partial function are picklable:
```python
>>>from functools import partial

>>>import pickle

>>>def f(x):
...    print(x)
    
>>>with open('f.pkl', 'wb') as file:
...    pickle.dump(partial(f, x='Dog'), file)
    
>>>with open('f.pkl', 'rb') as file:
...    unpickled_f = pickle.load(file)
    
>>>unpickled_f()
Dog
```

The fix is straightforward and I can create a PR. Nonetheless, it would be my first contribution so I might need some help along the way.

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/huggingface__transformers-21768/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/huggingface__transformers-21768/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/huggingface__transformers-21768/bin/envrun 'git status --short && ls'
Edits you make under /work/huggingface__transformers-21768/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

Follow these steps to resolve the issue:
1. As a first step, explore the repo to find and read the code relevant to the <issue_description>.
2. Create a script or a small test to reproduce the error and execute it with envrun, to confirm the error.
3. Edit the source code of the repo to resolve the issue.
4. Rerun your reproduction and confirm that the error is fixed.
5. Think about edge cases and make sure your fix handles them as well; run the existing tests closest to the code you changed.
6. Delete any scripts or files you created only for reproduction or checking, so that only the fix remains in the repository.

````

## Trajectory

_session start: model claude-opus-5-5, tools ['Bash', 'Edit', 'Glob', 'Grep', 'Read', 'Write'], MCP servers []_

**tool call: Bash**

```bash
sed -n 1,260p src/transformers/optimization.py
```

tool result:

```
# coding=utf-8
# Copyright 2018 The Google AI Language Team Authors and The HuggingFace Inc. team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""PyTorch optimization for BERT model."""

import math
import warnings
from typing import Callable, Iterable, Optional, Tuple, Union

import torch
from torch import nn
from torch.optim import Optimizer
from torch.optim.lr_scheduler import LambdaLR

from .trainer_utils import SchedulerType
from .utils import logging
from .utils.versions import require_version


logger = logging.get_logger(__name__)


def get_constant_schedule(optimizer: Optimizer, last_epoch: int = -1):
    """
    Create a schedule with a constant learning rate, using the learning rate set in optimizer.

    Args:
        optimizer ([`~torch.optim.Optimizer`]):
            The optimizer for which to schedule the learning rate.
        last_epoch (`int`, *optional*, defaults to -1):
            The index of the last epoch when resuming training.

    Return:
        `torch.optim.lr_scheduler.LambdaLR` with the appropriate schedule.
    """
    return LambdaLR(optimizer, lambda _: 1, last_epoch=last_epoch)


def get_constant_schedule_with_warmup(optimizer: Optimizer, num_warmup_steps: int, last_epoch: int = -1):
    """
    Create a schedule with a constant learning rate preceded by a warmup period during which the learning rate
    increases linearly between 0 and the initial lr set in the optimizer.

    Args:
        optimizer ([`~torch.optim.Optimizer`]):
            The optimizer for which to schedule the learning rate.
        num_warmup_steps (`int`):
            The number of steps for the warmup phase.
        last_epoch (`int`, *optional*, defaults to -1):
            The index of the last epoch when resuming training.

    Return:
        `torch.optim.lr_scheduler.LambdaLR` with the appropriate schedule.
    """

    def lr_lambda(current_step: int):
        if current_step < num_warmup_steps:
            return float(current_step) / float(max(1.0, num_warmup_steps))
        return 1.0

    return LambdaLR(optimizer, lr_lambda, last_epoch=last_epoch)


def get_linear_schedule_with_warmup(optimizer, num_warmup_steps, num_training_steps, last_epoch=-1):
    """
    Create a schedule with a learning rate that decreases linearly from the initial lr set in the optimizer to 0, after
    a warmup period during which it increases linearly from 0 to the initial lr set in the optimizer.

    Args:
        optimizer ([`~torch.optim.Optimizer`]):
            The optimizer for which to schedule the learning rate.
        num_warmup_steps (`int`):
            The number of steps for the warmup phase.
        num_training_steps (`int`):
            The total number of training steps.
        last_epoch (`int`, *optional*, defaults to -1):
            The index of the last epoch when resuming training.

    Return:
        `torch.optim.lr_scheduler.LambdaLR` with the appropriate schedule.
    """

    def lr_lambda(current_step: int):
        if current_step < num_warmup_steps:
            return float(current_step) / float(max(1, num_warmup_steps))
        return max(
            0.0, float(num_training_steps - current_step) / float(max(1, num_training_steps - num_warmup_steps))
        )

    return LambdaLR(optimizer, lr_lambda, last_epoch)


def get_cosine_schedule_with_warmup(
    optimizer: Optimizer, num_warmup_steps: int, num_training_steps: int, num_cycles: float = 0.5, last_epoch: int = -1
):
    """
    Create a schedule with a learning rate that decreases following the values of the cosine function between the
    initial lr set in the optimizer to 0, after a warmup period during which it increases linearly between 0 and the
    initial lr set in the optimizer.

    Args:
        optimizer ([`~torch.optim.Optimizer`]):
            The optimizer for which to schedule the learning rate.
        num_warmup_steps (`int`):
            The number of steps for the warmup phase.
        num_training_steps (`int`):
            The total number of training steps.
        num_cycles (`float`, *optional*, defaults to 0.5):
            The number of waves in the cosine schedule (the defaults is to just decrease from the max value to 0
            following a half-cosine).
        last_epoch (`int`, *optional*, defaults to -1):
            The index of the last epoch when resuming training.

    Return:
        `torch.optim.lr_scheduler.LambdaLR` with the appropriate schedule.
    """

    def lr_lambda(current_step):
        if current_step < num_warmup_steps:
            return float(current_step) / float(max(1, num_warmup_steps))
        progress = float(current_step - num_warmup_steps) / float(max(1, num_training_steps - num_warmup_steps))
        return max(0.0, 0.5 * (1.0 + math.cos(math.pi * float(num_cycles) * 2.0 * progress)))

    return LambdaLR(optimizer, lr_lambda, last_epoch)


def get_cosine_with_hard_restarts_schedule_with_warmup(
    optimizer: Optimizer, num_warmup_steps: int, num_training_steps: int, num_cycles: int = 1, last_epoch: int = -1
):
    """
    Create a schedule with a learning rate that decreases following the values of the cosine function between the
    initial lr set in the optimizer to 0, with several hard restarts, after a warmup period during which it increases
    linearly between 0 and the initial lr set in the optimizer.

    Args:
        optimizer ([`~torch.optim.Optimizer`]):
            The optimizer for which to schedule the learning rate.
        num
[... 4663 more characters not shown]
```

**tool call: Bash**

```bash
grep -n "pickle\|reload\|lambda\|class \|def " tests/optimization/test_optimization.py | head -60
```

tool result:

```
42:def unwrap_schedule(scheduler, num_steps=10):
50:def unwrap_and_save_reload_schedule(scheduler, num_steps=10):
66:class OptimizationTest(unittest.TestCase):
67:    def assertListAlmostEqual(self, list1, list2, tol):
72:    def test_adam_w(self):
86:    def test_adafactor(self):
113:class ScheduleInitTest(unittest.TestCase):
118:    def assertListAlmostEqual(self, list1, list2, tol, msg=None):
123:    def test_schedulers(self):
169:            lrs_2 = unwrap_and_save_reload_schedule(scheduler, self.num_steps)
170:            self.assertListEqual(lrs_1, lrs_2, msg=f"failed for {scheduler_func} in save and reload")
```

**tool call: Bash**

```bash
cat > /tmp/repro.py <<'EOF'
import pickle, torch
from transformers import optimization as o
m = torch.nn.Linear(2,2)
opt = torch.optim.AdamW(m.parameters(), lr=10.)
for f, kw in [(o.get_constant_schedule,{}),(o.get_constant_schedule_with_warmup,dict(num_warmup_steps=2)),
              (o.get_linear_schedule_with_warmup,dict(num_warmup_steps=2,num_training_steps=10)),
              (o.get_cosine_schedule_with_warmup,dict(num_warmup_steps=2,num_training_steps=10)),
              (o.get_cosine_with_hard_restarts_schedule_with_warmup,dict(num_warmup_steps=2,num_training_steps=10,num_cycles=2)),
              (o.get_polynomial_decay_schedule_with_warmup,dict(num_warmup_steps=2,num_training_steps=10,lr_end=1e-7,power=2.0)),
              (o.get_inverse_sqrt_schedule,dict(num_warmup_steps=2))]:
    s = f(opt, **kw)
    try:
        pickle.loads(pickle.dumps(s.lr_lambdas)); print("ok", f.__name__)
    except Exception as e: print("FAIL", f.__name__, e)
EOF
cp /tmp/repro.py ./repro_tmp.py; ../bin/envrun 'python repro_tmp.py'
```

tool result:

```
Exit code 2
(eval):1: operation not permitted: /tmp/repro.py
cp: /tmp/repro.py: No such file or directory
python: can't open file '/testbed/repro_tmp.py': [Errno 2] No such file or directory
```

**tool call: Bash**

```bash
cat > repro_tmp.py <<'EOF'
import pickle, torch
from transformers import optimization as o
m = torch.nn.Linear(2,2)
opt = torch.optim.AdamW(m.parameters(), lr=10.)
for f, kw in [(o.get_constant_schedule,{}),(o.get_constant_schedule_with_warmup,dict(num_warmup_steps=2)),
              (o.get_linear_schedule_with_warmup,dict(num_warmup_steps=2,num_training_steps=10)),
              (o.get_cosine_schedule_with_warmup,dict(num_warmup_steps=2,num_training_steps=10)),
              (o.get_cosine_with_hard_restarts_schedule_with_warmup,dict(num_warmup_steps=2,num_training_steps=10,num_cycles=2)),
              (o.get_polynomial_decay_schedule_with_warmup,dict(num_warmup_steps=2,num_training_steps=10,lr_end=1e-7,power=2.0)),
              (o.get_inverse_sqrt_schedule,dict(num_warmup_steps=2))]:
    s = f(opt, **kw)
    try:
        pickle.loads(pickle.dumps(s.lr_lambdas)); print("ok", f.__name__, [s.lr_lambdas[0](i) for i in range(12)])
    except Exception as e: print("FAIL", f.__name__, e)
EOF
../bin/envrun 'python repro_tmp.py'
```

tool result:

```
FAIL get_constant_schedule Can't pickle local object 'get_constant_schedule.<locals>.<lambda>'
FAIL get_constant_schedule_with_warmup Can't pickle local object 'get_constant_schedule_with_warmup.<locals>.lr_lambda'
FAIL get_linear_schedule_with_warmup Can't pickle local object 'get_linear_schedule_with_warmup.<locals>.lr_lambda'
FAIL get_cosine_schedule_with_warmup Can't pickle local object 'get_cosine_schedule_with_warmup.<locals>.lr_lambda'
FAIL get_cosine_with_hard_restarts_schedule_with_warmup Can't pickle local object 'get_cosine_with_hard_restarts_schedule_with_warmup.<locals>.lr_lambda'
FAIL get_polynomial_decay_schedule_with_warmup Can't pickle local object 'get_polynomial_decay_schedule_with_warmup.<locals>.lr_lambda'
FAIL get_inverse_sqrt_schedule Can't pickle local object 'get_inverse_sqrt_schedule.<locals>.lr_lambda'
```

**assistant:** Confirmed. Now I'll refactor each local function into a module-level function bound via `functools.partial`.

**tool call: Bash**

```bash
cat > edit_tmp.py <<'EOF'
import re
p = "src/transformers/optimization.py"
s = open(p).read()
def rep(old, new):
    global s
    assert s.count(old) == 1, old
    s = s.replace(old, new)

rep("import math\nimport warnings\n", "import math\nimport warnings\nfrom functools import partial\n")

rep('''def get_constant_schedule(optimizer''', '''def _get_constant_lambda(_=None):
    return 1


def get_constant_schedule(optimizer''')
rep("return LambdaLR(optimizer, lambda _: 1, last_epoch=last_epoch)", "return LambdaLR(optimizer, _get_constant_lambda, last_epoch=last_epoch)")

rep('''def get_constant_schedule_with_warmup(''', '''def _get_constant_schedule_with_warmup_lr_lambda(current_step: int, *, num_warmup_steps: int):
    if current_step < num_warmup_steps:
        return float(current_step) / float(max(1.0, num_warmup_steps))
    return 1.0


def get_constant_schedule_with_warmup(''')
rep('''
    def lr_lambda(current_step: int):
        if current_step < num_warmup_steps:
            return float(current_step) / float(max(1.0, num_warmup_steps))
        return 1.0

    return LambdaLR(optimizer, lr_lambda, last_epoch=last_epoch)''', '''
    lr_lambda = partial(_get_constant_schedule_with_warmup_lr_lambda, num_warmup_steps=num_warmup_steps)
    return LambdaLR(optimizer, lr_lambda, last_epoch=last_epoch)''')

rep('''def get_linear_schedule_with_warmup(''', '''def _get_linear_schedule_with_warmup_lr_lambda(current_step: int, *, num_warmup_steps: int, num_training_steps: int):
    if current_step < num_warmup_steps:
        return float(current_step) / float(max(1, num_warmup_steps))
    return max(0.0, float(num_training_steps - current_step) / float(max(1, num_training_steps - num_warmup_steps)))


def get_linear_schedule_with_warmup(''')
rep('''
    def lr_lambda(current_step: int):
        if current_step < num_warmup_steps:
            return float(current_step) / float(max(1, num_warmup_steps))
        return max(
            0.0, float(num_training_steps - current_step) / float(max(1, num_training_steps - num_warmup_steps))
        )

    return LambdaLR''', '''
    lr_lambda = partial(
        _get_linear_schedule_with_warmup_lr_lambda,
        num_warmup_steps=num_warmup_steps,
        num_training_steps=num_training_steps,
    )
    return LambdaLR''')

rep('''def get_cosine_schedule_with_warmup(''', '''def _get_cosine_schedule_with_warmup_lr_lambda(
    current_step: int, *, num_warmup_steps: int, num_training_steps: int, num_cycles: float
):
    if current_step < num_warmup_steps:
        return float(current_step) / float(max(1, num_warmup_steps))
    progress = float(current_step - num_warmup_steps) / float(max(1, num_training_steps - num_warmup_steps))
    return max(0.0, 0.5 * (1.0 + math.cos(math.pi * float(num_cycles) * 2.0 * progress)))


def get_cosine_schedule_with_warmup(''')
rep('''
    def lr_lambda(current_step):
        if current_step < num_warmup_steps:
            return float(current_step) / float(max(1, num_warmup_steps))
        progress = float(current_step - num_warmup_steps) / float(max(1, num_training_steps - num_warmup_steps))
        return max(0.0, 0.5 * (1.0 + math.cos(math.pi * float(num_cycles) * 2.0 * progress)))

    return LambdaLR''', '''
    lr_lambda = partial(
        _get_cosine_schedule_with_warmup_lr_lambda,
        num_warmup_steps=num_warmup_steps,
        num_training_steps=num_training_steps,
        num_cycles=num_cycles,
    )
    return LambdaLR''')

rep('''def get_cosine_with_hard_restarts_schedule_with_warmup(''', '''def _get_cosine_with_hard_restarts_schedule_with_warmup_lr_lambda(
    current_step: int, *, num_warmup_steps: int, num_training_steps: int, num_cycles: int
):
    if current_step < num_warmup_steps:
        return float(current_step) / float(max(1, num_warmup_steps))
    progress = float(current_step - num_warmup_steps) / float(max(1, num_training_steps - num_warmup_steps))
    if progress >= 1.0:
        return 0.0
    return max(0.0, 0.5 * (1.0 + math.cos(math.pi * ((float(num_cycles) * progress) % 1.0))))


def get_cosine_with_hard_restarts_schedule_with_warmup(''')
rep('''
    def lr_lambda(current_step):
        if current_step < num_warmup_steps:
            return float(current_step) / float(max(1, num_warmup_steps))
        progress = float(current_step - num_warmup_steps) / float(max(1, num_training_steps - num_warmup_steps))
        if progress >= 1.0:
            return 0.0
        return max(0.0, 0.5 * (1.0 + math.cos(math.pi * ((float(num_cycles) * progress) % 1.0))))

    return LambdaLR''', '''
    lr_lambda = partial(
        _get_cosine_with_hard_restarts_schedule_with_warmup_lr_lambda,
        num_warmup_steps=num_warmup_steps,
        num_training_steps=num_training_steps,
        num_cycles=num_cycles,
    )
    return LambdaLR''')

rep('''def get_polynomial_decay_schedule_with_warmup(''', '''def _get_polynomial_decay_schedule_with_warmup_lr_lambda(
    current_step: int,
    *,
    num_warmup_steps: int,
    num_training_steps: int,
    lr_end: float,
    power: float,
    lr_init: int,
):
    if current_step < num_warmup_steps:
        return float(current_step) / float(max(1, num_warmup_steps))
    elif current_step > num_training_steps:
        return lr_end / lr_init  # as LambdaLR multiplies by lr_init
    else:
        lr_range = lr_init - lr_end
        decay_steps = num_training_steps - num_warmup_steps
        pct_remaining = 1 - (current_step - num_warmup_steps) / decay_steps
        decay = lr_range * pct_remaining**power + lr_end
        return decay / lr_init  # as LambdaLR multiplies by lr_init


def get_polynomial_decay_schedule_with_warmup(''')
rep('''
    def lr_lambda(current_step: int):
        if current_step < num_warmup_steps:
            return float(current_step) / float(max(1, num_warmup_steps))
        elif current_step > num_training_steps:
            return lr_end / lr_init  # as LambdaLR multiplies by lr_init
        else:
            lr_range = lr_init - lr_end
            decay_steps = num_training_steps - num_warmup_steps
            pct_remaining = 1 - (current_step - num_warmup_steps) / decay_steps
            decay = lr_range * pct_remaining**power + lr_end
            return decay / lr_init  # as LambdaLR multiplies by lr_init

    return LambdaLR''', '''
    lr_lambda = partial(
        _get_polynomial_decay_schedule_with_warmup_lr_lambda,
        num_warmup_steps=num_warmup_steps,
        num_training_steps=num_training_steps,
        lr_end=lr_end,
        power=power,
        lr_init=lr_init,
    )
    return LambdaLR''')

rep('''def get_inverse_sqrt_schedule(''', '''def _get_inverse_sqrt_schedule_lr_lambda(current_step: int, *, num_warmup_steps: int, timescale: int = None):
    if current_step < num_warmup_steps:
        return float(current_step) / float(max(1, num_warmup_steps))
    shift = timescale - num_warmup_steps
    decay = 1.0 / math.sqrt((current_step + shift) / timescale)
    return decay


def get_inverse_sqrt_schedule(''')
rep('''
    def lr_lambda(current_step: int):
        if current_step < num_warmup_steps:
            return float(current_step) / float(max(1, num_warmup_steps))
        shift = timescale - num_warmup_steps
        decay = 1.0 / math.sqrt((current_step + shift) / timescale)
        return decay

    return LambdaLR''', '''
    lr_lambda = partial(_get_inverse_sqrt_schedule_lr_lambda, num_warmup_steps=num_warmup_steps, timescale=timescale)
    return LambdaLR''')
open(p, "w").write(s)
EOF
../bin/envrun 'python edit_tmp.py && python repro_tmp.py && python -m pytest -q tests/optimization tests/trainer/test_trainer.py -k "schedul or Optimization or resume" 2>&1 | tail -5; black --check src/transformers/optimization.py; ruff src/transformers/optimization.py'
```

tool result:

```
Exit code 127
ok get_constant_schedule [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
ok get_constant_schedule_with_warmup [0.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
ok get_linear_schedule_with_warmup [0.0, 0.5, 1.0, 0.875, 0.75, 0.625, 0.5, 0.375, 0.25, 0.125, 0.0, 0.0]
ok get_cosine_schedule_with_warmup [0.0, 0.5, 1.0, 0.9619397662556434, 0.8535533905932737, 0.6913417161825449, 0.5, 0.30865828381745514, 0.14644660940672627, 0.03806023374435663, 0.0, 0.038060233744356575]
ok get_cosine_with_hard_restarts_schedule_with_warmup [0.0, 0.5, 1.0, 0.8535533905932737, 0.5, 0.14644660940672627, 1.0, 0.8535533905932737, 0.5, 0.14644660940672627, 0.0, 0.0]
ok get_polynomial_decay_schedule_with_warmup [0.0, 0.5, 1.0, 0.7656250023437501, 0.5625000043750001, 0.39062500609375, 0.2500000075, 0.14062500859375002, 0.062500009375, 0.015625009843750003, 1e-08, 1e-08]
ok get_inverse_sqrt_schedule [0.0, 0.5, 1.0, 0.8164965809277261, 0.7071067811865475, 0.6324555320336759, 0.5773502691896258, 0.5345224838248488, 0.5, 0.47140452079103173, 0.4472135954999579, 0.42640143271122083]
-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
ERROR tests/trainer/test_trainer.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 warning, 1 error in 0.65s
All done! ✨ 🍰 ✨
1 file would be left unchanged.
bash: line 1: ruff: command not found
```

**assistant:** All schedules now pickle and give correct values. Next I'll run the optimization tests on their own and check why `test_trainer.py` failed to collect.

**tool call: Bash**

```bash
../bin/envrun 'python -m pytest -q tests/optimization 2>&1 | tail -3; python -m pytest -q tests/trainer/test_trainer.py 2>&1 | grep -m3 Error; git stash -q; python -m pytest -q tests/trainer/test_trainer.py 2>&1 | tail -1; git stash pop -q; git status --short'
```

tool result:

```
-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
3 passed, 2 skipped, 5 warnings in 0.65s
ImportError while importing test module '/testbed/tests/trainer/test_trainer.py'.
E   ImportError: cannot import name 'set_access_token' from 'huggingface_hub' (/usr/local/lib/python3.10/site-packages/huggingface_hub/__init__.py)
1 error in 0.14s
 M src/transformers/optimization.py
?? Dockerfile
?? edit_tmp.py
?? repro_tmp.py
```

**assistant:** The `test_trainer.py` import error also happens without my change. It's caused by the installed `huggingface_hub` version, not by this fix. Removing the temporary scripts:

**tool call: Bash**

```bash
rm edit_tmp.py repro_tmp.py; git diff --stat
```

tool result:

```
 src/transformers/optimization.py | 140 ++++++++++++++++++++++++++-------------
 1 file changed, 94 insertions(+), 46 deletions(-)
```

**assistant:** The learning-rate schedulers in `src/transformers/optimization.py` can now be pickled. Before the change, all seven schedule factories failed with `Can't pickle local object ...`; after it, all seven pickle and unpickle without errors.

**What changed:** each lambda or nested `lr_lambda` is now a module-level function. The factory binds its arguments to that function with `functools.partial` and passes the result to `LambdaLR`, which is the approach the issue suggested.
- `get_constant_schedule` now uses a module-level `_get_constant_lambda` instead of `lambda _: 1`.
- The other five functions named in the issue (constant/linear/cosine/hard-restart cosine/polynomial with warmup) each got a matching `_get_..._lr_lambda` function.
- I also changed `get_inverse_sqrt_schedule` the same way. The issue didn't list it, but it had the same problem.

The math is unchanged; I only moved it. The function signatures, defaults and the `lr_end` check in the polynomial schedule are as before.

**Checks:**
- A small script built every scheduler, pickled and unpickled its `lr_lambdas`, and printed 12 steps of values. The values are as expected for each schedule, e.g. linear warmup then decay to 0, and polynomial ending at `lr_end / lr_init`.
- `tests/optimization` passes (3 passed, 2 skipped). That includes the existing save-and-reload check on every scheduler.
- `black --check` passes on the file. `ruff` isn't installed in the container, so I didn't run it.
- `tests/trainer/test_trainer.py` won't load in this environment, with or without my change: the installed `huggingface_hub` no longer has `set_access_token`. So the trainer tests didn't run.

I deleted my temporary scripts, so the only change in the repo is `optimization.py`. There's also an untracked `Dockerfile` in the repo root that I didn't create; I left it alone.

_session end: success, turns 8, is_error False_

## Container commands (task container, no network; broker log)

- `rc=2` 0.18 s: python repro_tmp.py
- `rc=0` 2.84 s: python repro_tmp.py
- `rc=127` 6.11 s: python edit_tmp.py && python repro_tmp.py && python -m pytest -q tests/optimization tests/trainer/test_trainer.py -k "schedul or Optimization or resume" 2>&1 | tail -5; black --check src/transformers/optimization.py; ruff src/transformers/optimization.py
- `rc=0` 8.78 s: python -m pytest -q tests/optimization 2>&1 | tail -3; python -m pytest -q tests/trainer/test_trainer.py 2>&1 | grep -m3 Error; git stash -q; python -m pytest -q tests/trainer/test_trainer.py 2>&1 | tail -1; git stash pop -q; git status --short
