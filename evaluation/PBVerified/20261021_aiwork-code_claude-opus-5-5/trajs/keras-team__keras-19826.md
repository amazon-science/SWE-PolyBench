# Instance: keras-team__keras-19826
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: False

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
 `keras.ops.repeat` cannot return an exptected shape when `x` is a `KerasTensor` and the `axis` is `None`
Hello. Thank you for your contributions and maintenance for the best Keras.

I'm following the instructions of [Conditional GAN (code samples, uses Keras 3)](https://keras.io/examples/generative/conditional_gan/), and focusing on the `keras.ops.repeat` function that is used in it.

I have found, maybe, if the input tensor of  `keras.ops.repeat`  is a symbolic tensor, i.e., the `keras.KerasTensor`, and the arg `axis` is `None`, the returned one will not be my expected one.

As the following：
```python
batch_size = 64
class_num = 10
a = keras.KerasTensor(shape=(batch_size, class_num), dtype=tf.float32)
a = a[:, :, None, None] # [B,10,1,1]
b = keras.ops.repeat(a, repeats=[28 * 28])
print(b.shape)# (784,)
# expected output: (501760,)
```

If assign `axis`, it works as expected:
```python
a = keras.KerasTensor(shape=(batch_size, class_num), dtype=tf.float32)
a = a[:, :, None, None] # [B,10,1,1]
b = keras.ops.repeat(a, repeats=[28 * 28],axis=0)
print(b.shape)# (784, 10, 1, 1)
# expected output: (784, 10, 1, 1)
```

If not use the symbolic tensor, it also works as expected:
```python
a = keras.random.normal(shape=(batch_size, class_num), dtype=tf.float32)
a = a[:, :, None, None] # [B,10,1,1]
b = keras.ops.repeat(a, repeats=[28 * 28])
print(b.shape)# (501760,)
# expected output: (501760,)
```

So, is the above a bug? 

And my environment is:
- Keras: Version: 3.3.3
- Numpy: Version: 1.26.4
- TensorFlow: Version: 2.16.1

Thanks in advance.
````

## Operational trajectory

### Turn 1 — tool call call_0001 (rg)

````json
{
 "pattern": "class Repeat\\(",
 "path": "keras/src/ops/numpy.py",
 "context_after": 45
}
````

Result:

````text
{
 "output_mode": "content",
 "pattern": "class Repeat\\(",
 "search_path": "/testbed/keras/src/ops/numpy.py",
 "matches": [],
 "stats": {
  "files_searched": 1,
  "files_with_matches": 0,
  "matches_found": 0,
  "matches_returned": 0,
  "denied_skips": 0,
  "duration_ms": 3,
  "timing": {
   "walk_ms": 0,
   "search_ms": 2,
   "collect_ms": 0,
   "total_ms": 3
  }
 },
 "truncated": false
}
````

### Turn 2 — tool call call_0002 (rg)

````json
{
 "context_after": 45,
 "path": "keras",
 "pattern": "class Repeat\\(Operation"
}
````

Result:

````text
{
 "output_mode": "content",
 "pattern": "class Repeat\\(Operation",
 "search_path": "/testbed/keras",
 "matches": [],
 "stats": {
  "files_searched": 715,
  "files_with_matches": 0,
  "matches_found": 0,
  "matches_returned": 0,
  "denied_skips": 0,
  "duration_ms": 342,
  "timing": {
   "walk_ms": 0,
   "search_ms": 342,
   "collect_ms": 0,
   "total_ms": 342
  }
 },
 "truncated": false
}
````

### Turn 3 — tool call call_0003 (rg)

````json
{
 "context_after": 45,
 "path": "keras",
 "pattern": "class Repeat\\("
}
````

Result:

````text
{
 "output_mode": "content",
 "pattern": "class Repeat\\(",
 "search_path": "/testbed/keras",
 "matches": [],
 "stats": {
  "files_searched": 715,
  "files_with_matches": 0,
  "matches_found": 0,
  "matches_returned": 0,
  "denied_skips": 0,
  "duration_ms": 322,
  "timing": {
   "walk_ms": 0,
   "search_ms": 322,
   "collect_ms": 0,
   "total_ms": 322
  }
 },
 "truncated": false
}
````

### Turn 4 — tool call call_0004 (rg)

````json
{
 "path": "keras",
 "pattern": "class Repeat"
}
````

Result:

````text
{
 "output_mode": "content",
 "pattern": "class Repeat",
 "search_path": "/testbed/keras",
 "matches": [
  {
   "path": "src/layers/reshaping/repeat_vector.py",
   "line_number": 8,
   "line": "class RepeatVector(Layer):"
  },
  {
   "path": "src/ops/numpy.py",
   "line_number": 4337,
   "line": "class Repeat(Operation):"
  }
 ],
 "stats": {
  "files_searched": 715,
  "files_with_matches": 2,
  "matches_found": 2,
  "matches_returned": 2,
  "denied_skips": 0,
  "duration_ms": 286,
  "timing": {
   "walk_ms": 0,
   "search_ms": 285,
   "collect_ms": 0,
   "total_ms": 286
  }
 },
 "truncated": false
}
````

### Turn 5 — tool call call_0005 (read)

````json
{
 "file_path": "keras/src/ops/numpy.py",
 "offset": 4337,
 "limit": 50
}
````

Result:

````text
{
 "type": "file",
 "path": "keras/src/ops/numpy.py",
 "full_read": false,
 "output": "keras/src/ops/numpy.py\n\n4337: class Repeat(Operation):\n4338:     def __init__(self, repeats, axis=None):\n4339:         super().__init__()\n4340:         self.axis = axis\n4341:         self.repeats = repeats\n4342: \n4343:     def call(self, x):\n4344:         return backend.numpy.repeat(x, self.repeats, axis=self.axis)\n4345: \n4346:     def compute_output_spec(self, x):\n4347:         x_shape = list(x.shape)\n4348:         if self.axis is None:\n4349:             if None in x_shape:\n4350:                 return KerasTensor([None], dtype=x.dtype)\n4351: \n4352:             x_flatten_size = int(np.prod(x_shape))\n4353:             if isinstance(self.repeats, int):\n4354:                 output_shape = [x_flatten_size * self.repeats]\n4355:             else:\n4356:                 output_shape = [int(np.sum(self.repeats))]\n4357:             return KerasTensor(output_shape, dtype=x.dtype)\n4358: \n4359:         size_on_ax = x_shape[self.axis]\n4360:         output_shape = x_shape\n4361:         if isinstance(self.repeats, int):\n4362:             if size_on_ax is None:\n4363:                 output_shape[self.axis] = None\n4364:             else:\n4365:                 output_shape[self.axis] = size_on_ax * self.repeats\n4366:         else:\n4367:             output_shape[self.axis] = int(np.sum(self.repeats))\n4368:         return KerasTensor(output_shape, dtype=x.dtype)\n4369: \n4370: \n4371: @keras_export([\"keras.ops.repeat\", \"keras.ops.numpy.repeat\"])\n4372: def repeat(x, repeats, axis=None):\n4373:     \"\"\"Repeat each element of a tensor after themselves.\n4374: \n4375:     Args:\n4376:         x: Input tensor.\n4377:         repeats: The number of repetitions for each element.\n4378:         axis: The axis along which to repeat values. By default, use\n4379:             the flattened input array, and return a flat output array.\n4380: \n4381:     Returns:\n4382:         Output tensor.\n4383:     \"\"\"\n4384:     if any_symbolic_tensors((x,)):\n4385:         return Repeat(repeats, axis=axis).symbolic_call(x)\n4386:     return backend.numpy.repeat(x, repeats, axis=axis)\n\n(Returned 50 lines starting at 4337; observed at least 4387 total lines; output truncated at the 102400 byte read window — continue with offset=4387)",
 "offset": 4337,
 "limit": 50,
 "lines_returned": 50,
 "total_lines": null,
 "observed_lines": 4387,
 "total_lines_lower_bound": 4387,
 "total_lines_exact": false,
 "truncated": true,
 "next_offset": 4387,
 "window_bytes_limit": 102400,
 "size_bytes": 196951
}
````

### Turn 6 — thinking

````text
I'm reasoning through the repeats-length-1 broadcasting case, similar to the axis scenario — treating a single-element repeats list as equivalent to passing an int so the behavior matches expectations across both axis and non-axis calls.
````

### Turn 6 — tool call call_0006 (apply_patch)

````json
{
 "patch_text": "*** Begin Patch\n*** Update File: keras/src/ops/numpy.py\n@@\n     def compute_output_spec(self, x):\n         x_shape = list(x.shape)\n+        repeats = self.repeats\n+        if isinstance(repeats, np.ndarray):\n+            repeats = repeats.tolist()\n+        if not isinstance(repeats, int) and len(repeats) == 1:\n+            # A single-element `repeats` is broadcast to every element.\n+            repeats = int(repeats[0])\n         if self.axis is None:\n             if None in x_shape:\n                 return KerasTensor([None], dtype=x.dtype)\n \n             x_flatten_size = int(np.prod(x_shape))\n-            if isinstance(self.repeats, int):\n-                output_shape = [x_flatten_size * self.repeats]\n+            if isinstance(repeats, int):\n+                output_shape = [x_flatten_size * repeats]\n             else:\n-                output_shape = [int(np.sum(self.repeats))]\n+                output_shape = [int(np.sum(repeats))]\n             return KerasTensor(output_shape, dtype=x.dtype)\n \n         size_on_ax = x_shape[self.axis]\n         output_shape = x_shape\n-        if isinstance(self.repeats, int):\n+        if isinstance(repeats, int):\n             if size_on_ax is None:\n                 output_shape[self.axis] = None\n             else:\n-                output_shape[self.axis] = size_on_ax * self.repeats\n+                output_shape[self.axis] = size_on_ax * repeats\n         else:\n-            output_shape[self.axis] = int(np.sum(self.repeats))\n+            output_shape[self.axis] = int(np.sum(repeats))\n         return KerasTensor(output_shape, dtype=x.dtype)\n*** End Patch"
}
````

Result:

````text
{
 "plan_id": "5626fd2c0e5e43c5b88612da9300663ab29288e934fbd9dd257c704bd005b366",
 "applied": true,
 "files_modified": [
  "keras/src/ops/numpy.py"
 ],
 "conflicts": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "apply_patch",
    "paths": [
     "keras/src/ops/numpy.py"
    ]
   }
  ]
 }
}
````

### Turn 7 — tool call call_0007 (exec)

````json
{
 "command": "cd /testbed && python -c \"\nimport keras, numpy as np\na = keras.KerasTensor(shape=(64,10,1,1))\nprint(keras.ops.repeat(a,[784]).shape, keras.ops.repeat(a,[784],axis=0).shape, keras.ops.repeat(a,2).shape, keras.ops.repeat(a,[1,2,3,4,5,6,7,8,9,10],axis=1).shape)\nprint(np.repeat(np.zeros((64,10,1,1)),[784]).shape, np.repeat(np.zeros((64,10,1,1)),[784],axis=0).shape)\n\" 2>&1 | tail -3; python -m pytest -q keras/src/ops/numpy_test.py -k \"repeat or Repeat\" 2>&1 | tail -3",
 "timeout_secs": 300
}
````

Result:

````text
{
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "backgrounded",
  "retryability": "retry_after_wait",
  "open_work_at_failure": false
 },
 "background_exec": {
  "tool_action": "run",
  "task": {
   "task_id": "bg_1_5e6d6cd6d69a42219bdd37190da2d1ac",
   "session_id": "cli:default:s7c3b48d7",
   "root_session_id": "cli:default:s7c3b48d7",
   "origin_session_id": "cli:default:s7c3b48d7",
   "status": "running",
   "controls": {
    "list": {
     "method": "background_exec.list",
     "params": {
      "sessionId": "cli:default:s7c3b48d7"
     }
    },
    "logs": {
     "method": "background_exec.logs",
     "params": {
      "sessionId": "cli:default:s7c3b48d7",
      "task_id": "bg_1_5e6d6cd6d69a42219bdd37190da2d1ac"
     }
    },
    "wait": {
     "method": "background_exec.wait",
     "params": {
      "sessionId": "cli:default:s7c3b48d7",
      "task_id": "bg_1_5e6d6cd6d69a42219bdd37190da2d1ac"
     }
    },
    "stop": {
     "method": "background_exec.stop",
     "params": {
      "sessionId": "cli:default:s7c3b48d7",
      "task_id": "bg_1_5e6d6cd6d69a42219bdd37190da2d1ac"
     }
    }
   },
   "title": null,
   "cwd": "/testbed",
   "pid": 694,
   "pgid": 694,
   "runtime_identity_kind": "process",
   "lifecycle_intent": "session_bound",
   "operation_descriptor": {
    "schema_id": "agent.background-exec.operation.v1",
    "requested_type": "auto",
    "session_effective_type": "native",
    "operation_family": "native",
    "isolation_tier": "none",
    "lifecycle_mode": "host-process-group",
    "policy": "transitional-native",
    "reason": {
     "code": "session-native-fallback"
    }
   },
   "process_start_time_ticks": 34685888,
   "started_at_unix_secs": 1792205856,
   "updated_at_unix_secs": 1792205856,
   "finished_at_unix_secs": null,
   "duration_ms": 1,
   "exit_code": null,
   "requested_foreground_timeout_secs": 300,
   "effective_background_timeout_secs": 14400,
   "lease_mode": "renewable",
   "lease_source": "daemon_default",
   "timeout_secs": 14400,
   "output_bytes": 0,
   "last_output_at_unix_secs": null
  },
  "work_id": "bg_1_5e6d6cd6d69a42219bdd37190da2d1ac",
  "work_terminal_revision": 1792205856,
  "controls": {
   "list": {
    "method": "background_exec.list",
    "params": {
     "sessionId": "cli:default:s7c3b48d7"
    }
   },
   "logs": {
    "method": "background_exec.logs",
    "params": {
     "sessionId": "cli:default:s7c3b48d7",
     "task_id": "bg_1_5e6d6cd6d69a42219bdd37190da2d1ac"
    }
   },
   "wait": {
    "method": "background_exec.wait",
    "params": {
     "sessionId": "cli:default:s7c3b48d7",
     "task_id": "bg_1_5e6d6cd6d69a42219bdd37190da2d1ac"
    }
   },
   "stop": {
    "method": "background_exec.stop",
    "params": {
     "sessionId": "cli:default:s7c3b48d7",
     "task_id": "bg_1_5e6d6cd6d69a42219bdd37190da2d1ac"
    }
   }
  },
  "_meta": {
   "agent": {
    "background_exec_v1": {
     "controls": {
      "list": {
       "method": "background_exec.list",
       "params": {
        "sessionId": "cli:default:s7c3b48d7"
       }
      },
      "logs": {
       "method": "background_exec.logs",
       "params": {
        "sessionId": "cli:default:s7c3b48d7",
        "task_id": "bg_1_5e6d6cd6d69a42219bdd37190da2d1ac"
       }
      },
      "wait": {
       "method": "background_exec.wait",
       "params": {
        "sessionId": "cli:default:s7c3b48d7",
        "task_id": "bg_1_5e6d6cd6d69a42219bdd37190da2d1ac"
       }
      },
      "stop": {
       "method": "background_exec.stop",
       "params": {
        "sessionId": "cli:default:s7c3b48d7",
        "task_id": "bg_1_5e6d6cd6d69a42219bdd37190da2d1ac"
       }
      }
     },
     "task": {
      "task_id": "bg_1_5e6d6cd6d69a42219bdd37190da2d1ac",
      "session_id": "cli:default:s7c3b48d7",
      "root_session_id": "cli:default:s7c3b48d7",
      "origin_session_id": "cli:default:s7c3b48d7",
      "status": "running",
      "controls": {
       "list": {
        "method": "background_exec.list",
        "params": {
         "sessionId": "cli:default:s7c3b48d7"
        }
       },
       "logs": {
        "method": "background_exec.logs",
        "params": {
         "sessionId": "cli:default:s7c3b48d7",
         "task_id": "bg_1_5e6d6cd6d69a42219bdd37190da2d1ac"
        }
       },
       "wait": {
        "method": "background_exec.wait",
        "params": {
         "sessionId": "cli:default:s7c3b48d7",
         "task_id": "bg_1_5e6d6cd6d69a42219bdd37190da2d1ac"
        }
       },
       "stop": {
        "method": "background_exec.stop",
        "params": {
         "sessionId": "cli:default:s7c3b48d7",
         "task_id": "bg_1_5e6d6cd6d69a42219bdd37190da2d1ac"
        }
       }
      },
      "title": null,
      "cwd": "/testbed",
      "pid": 694,
      "pgid": 694,
      "runtime_identity_kind": "process",
      "lifecycle_intent": "session_bound",
      "operation_descriptor": {
       "schema_id": "agent.background-exec.operation.v1",
       "requested_type": "auto",
       "session_effective_type": "native",
       "operation_family": "native",
       "isolation_tier": "none",
       "lifecycle_mode": "host-process-group",
       "policy": "transitional-native",
       "reason": {
        "code": "session-native-fallback"
       }
      },
      "process_start_time_ticks": 34685888,
      "started_at_unix_secs": 1792205856,
      "updated_at_unix_secs": 1792205856,
      "finished_at_unix_secs": null,
      "duration_ms": 1,
      "exit_code": null,
      "requested_foreground_timeout_secs": 300,
      "effective_background_timeout_secs": 14400,
      "lease_mode": "renewable",
      "lease_source": "daemon_default",
      "timeout_secs": 14400,
      "output_bytes": 0,
      "last_output_at_unix_secs": null
     },
     "status": "running",
     "terminal": false
    }
   }
  },
  "tool_outcome": {
   "schema_version": 1,
   "tool_name": "background_exec",
   "status": "backgrounded",
   "retryability": "retry_after_wait",
   "open_work_at_failure": false
  }
 },
 "_agent_context_projection": {
  "schema_version": "agent.exec_tool_result_receipt_preview.v1",
  "content_status": "partial_preview",
  "context_view_limit_bytes": 16384,
  "receipt": {
   "result_id": "tr_8a0d3d24d05b4f9eadb35c46949d0028",
   "total_bytes": 5982,
   "total_lines": 0,
   "omitted_bytes": 0,
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "artifact": {
   "result_id": "tr_8a0d3d24d05b4f9eadb35c46949d0028",
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "content_preview": "{\"backgrounded\":true,\"background_exec\":{\"tool_action\":\"run\",\"task\":{\"task_id\":\"bg_1_5e6d6cd6d\n...[agent-cli tool_result context preview: tool_result_delivery_status=delivered; content_status=partial_preview_not_failure; compatibility_marker=tool_result truncated; omitted_bytes=4752; total_bytes=4938; context_view_limit=512 bytes; context_view_strategy=head_tail_compact; guidance=preview_not_failure_outcome_neutral]...\nait timeouts do not kill the task; background_exec.stop is the explicit termination action.\"}"
 }
}
````

### Turn 8 — tool call call_0008 (background_exec)

````json
{
 "action": "wait",
 "task_id": "bg_1_5e6d6cd6d69a42219bdd37190da2d1ac",
 "until": "terminal"
}
````

Result:

````text
{
 "tool_action": "wait",
 "task_id": "bg_1_5e6d6cd6d69a42219bdd37190da2d1ac",
 "work_id": "bg_1_5e6d6cd6d69a42219bdd37190da2d1ac",
 "work_terminal_revision": 1792205873,
 "status": "completed",
 "terminal": true,
 "lease_mode": "renewable",
 "last_output_at_unix_secs": 1792205873,
 "duration_ms": 16905,
 "stdout_delta": "To enable the following instructions: AVX2 AVX512F AVX512_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.\n(501760,) (50176, 10, 1, 1) (1280,) (64, 55, 1, 1)\n(501760,) (50176, 10, 1, 1)\nkeras/src/ops/numpy_test.py::NumpyDtypeTest::test_repeat_uint8 PASSED    [100%]\n\n===================== 16 passed, 5479 deselected in 4.20s ======================\n",
 "stderr_delta": "",
 "from_cursor": {
  "stdout": 0,
  "stderr": 0
 },
 "next_cursor": {
  "stdout": 386,
  "stderr": 0
 },
 "truncated": false,
 "omitted_bytes": 0,
 "has_more": false,
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "background_exec",
  "status": "success",
  "exit_code": 0,
  "retryability": "not_needed",
  "open_work_at_failure": false
 },
 "wait_timed_out": false,
 "progress_state": "terminal"
}
````

### Turn 9 — thinking

````text
I should flag that the user's stated expected shape for axis=0 (784,10,1,1) doesn't match what numpy actually produces, which is (50176,...).
````

### Turn 10 — thinking

````text
The fix checks out. I should flag that the user's expected shape of (784,10,1,1) for axis=0 doesn't actually match what numpy produces -- numpy gives (50176,...), which is what my output matches, so I'll note that discrepancy to the user.
````

### Turn 10 — assistant text

I fixed the bug. `keras.ops.repeat` on a `KerasTensor` now gives the same shape as NumPy and eager tensors when `repeats` is a single-element list. The change is in `Repeat.compute_output_spec` in `keras/src/ops/numpy.py`.

**Cause:** NumPy and eager mode apply a one-item `repeats` list such as `[784]` to every element, the same as `repeats=784`. The symbolic shape code only did that for a plain `int`. For a list, it just added up the list, so `axis=None` returned `(784,)`.

**Fix:** A one-item list (or NumPy array) is now treated as an integer before the output shape is worked out. This applies whether or not `axis` is given. Longer lists that give one count per element work as before.

**Checks run** (the input is a `KerasTensor` of shape `(64, 10, 1, 1)`, matching the issue):
- `repeat(a, [784])` now gives `(501760,)`, the same as `np.repeat`.
- `repeat(a, [784], axis=0)` now gives `(50176, 10, 1, 1)`, which also matches `np.repeat`. The issue said `(784, 10, 1, 1)` was right here, but it wasn't: 64 × 784 = 50176 along axis 0.
- `repeat(a, 2)` gives `(1280,)`, and a 10-item list on `axis=1` gives `(64, 55, 1, 1)`. Both are as expected.
- The existing repeat tests in `keras/src/ops/numpy_test.py` pass (16 passed).

### Turn 11 — assistant text

I fixed the bug in `keras/src/ops/numpy.py`. A symbolic `keras.ops.repeat` now returns the same shape as NumPy and eager mode. In your example it gives `(501760,)` instead of `(784,)`.

**Cause:** `Repeat.compute_output_spec` treated any list for `repeats` as one count per element and just added them up. But a one-element list like `[784]` should be applied to every element, the same as the plain integer `784`.

**Fix:** I made `compute_output_spec` turn a one-element `repeats` list (or NumPy array) into a plain integer before working out the shape. This applies both with and without `axis`.

**Checks:** I compared symbolic results to `np.repeat` on an input of shape `(64, 10, 1, 1)`:
- `repeats=[784]` with no axis: `(501760,)`, same as NumPy.
- `repeats=[784], axis=0`: `(50176, 10, 1, 1)`, same as NumPy.
- `repeats=2` gives `(1280,)`, and per-element repeats `[1..10]` on `axis=1` give `(64, 55, 1, 1)`.
- The existing repeat tests in `keras/src/ops/numpy_test.py` all pass (16 tests).

**One difference from the issue:** for `axis=0`, the issue expects `(784, 10, 1, 1)`. NumPy and eager mode actually give `64 × 784 = 50176` along that axis, because every one of the 64 rows is repeated 784 times. The symbolic shape now matches that, so it no longer shows the `(784, 10, 1, 1)` the issue expected.

## Final answer

I fixed the bug in `keras/src/ops/numpy.py`. A symbolic `keras.ops.repeat` now returns the same shape as NumPy and eager mode. In your example it gives `(501760,)` instead of `(784,)`.

**Cause:** `Repeat.compute_output_spec` treated any list for `repeats` as one count per element and just added them up. But a one-element list like `[784]` should be applied to every element, the same as the plain integer `784`.

**Fix:** I made `compute_output_spec` turn a one-element `repeats` list (or NumPy array) into a plain integer before working out the shape. This applies both with and without `axis`.

**Checks:** I compared symbolic results to `np.repeat` on an input of shape `(64, 10, 1, 1)`:
- `repeats=[784]` with no axis: `(501760,)`, same as NumPy.
- `repeats=[784], axis=0`: `(50176, 10, 1, 1)`, same as NumPy.
- `repeats=2` gives `(1280,)`, and per-element repeats `[1..10]` on `axis=1` give `(64, 55, 1, 1)`.
- The existing repeat tests in `keras/src/ops/numpy_test.py` all pass (16 tests).

**One difference from the issue:** for `axis=0`, the issue expects `(784, 10, 1, 1)`. NumPy and eager mode actually give `64 × 784 = 50176` along that axis, because every one of the 64 rows is repeated 784 times. The symbolic shape now matches that, so it no longer shows the `(784, 10, 1, 1)` the issue expected.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 153236 | 3004 | 131980 | 21232 | 156240 |
