# Instance: mui__material-ui-34158

- Final resolved (evaluator, logs/mui__material-ui-34158_result.json): True
- Run state: DONE
- One attempt. Duration 415.6 s, turns 31, actor cost $1.1051198, container commands 8
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/mui__material-ui-34158/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-34158/repo. Consider the following issue description:

<issue_description>
[SelectUnstyled] Event is not passed to the onChange handler
The SelectUnstyled's (and MultiSelectUnstyled's) onChange handler is called with the selected value as the first parameter. This is not in line with other components (and native elements) that have an event associated with the change as the first parameter.

Add the event as the first parameter. The current value can be passed in as the second parameter.

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-34158/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-34158/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-34158/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-34158/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

Follow these steps to resolve the issue:
1. As a first step, explore the repo to find and read the code relevant to the <issue_description>.
2. Create a script or a small test to reproduce the error and execute it with envrun, to confirm the error.
3. Edit the source code of the repo to resolve the issue.
4. Rerun your reproduction and confirm that the error is fixed.
5. Think about edge cases and make sure your fix handles them as well; run the existing tests closest to the code you changed.
6. Delete any scripts or files you created only for reproduction or checking, so that only the fix remains in the repository.

```

## Trajectory

_session start: model claude-opus-5-5, tools ['Bash', 'Edit', 'Glob', 'Grep', 'Read', 'Write'], MCP servers []_

**tool call: Bash**

```bash
grep -rn "onChange" packages/mui-base/src/SelectUnstyled packages/mui-base/src/MultiSelectUnstyled packages/mui-base/src/ListboxUnstyled --include=*.ts --include=*.tsx | grep -v test; grep -rln "onChange" packages/mui-joy/src/Select | grep -v test
```

tool result:

```
(eval):1: no matches found: --include=*.ts
packages/mui-joy/src/Select/Select.spec.tsx
packages/mui-joy/src/Select/SelectProps.ts
packages/mui-joy/src/Select/Select.tsx
```

**tool call: Bash**

```bash
grep -rn "onChange\|onChangeUnstyled\|handleChange\|ChangeEvent" packages/mui-base/src/SelectUnstyled packages/mui-base/src/MultiSelectUnstyled packages/mui-base/src/ListboxUnstyled | grep -v "test\.\|spec"; grep -n "onChange" packages/mui-joy/src/Select/Select.tsx packages/mui-joy/src/Select/SelectProps.ts
```

tool result:

```
packages/mui-base/src/SelectUnstyled/useSelect.types.ts:44:  onChange?: (value: TValue | null) => void;
packages/mui-base/src/SelectUnstyled/useSelect.types.ts:51:  onChange?: (value: TValue[]) => void;
packages/mui-base/src/SelectUnstyled/SelectUnstyled.types.ts:100:  onChange?: (value: TValue | null) => void;
packages/mui-base/src/SelectUnstyled/SelectUnstyled.tsx:87:    onChange,
packages/mui-base/src/SelectUnstyled/SelectUnstyled.tsx:150:    onChange,
packages/mui-base/src/SelectUnstyled/SelectUnstyled.tsx:311:  onChange: PropTypes.func,
packages/mui-base/src/SelectUnstyled/useSelect.ts:38:    onChange,
packages/mui-base/src/SelectUnstyled/useSelect.ts:217:      onChange: (newOptions) => {
packages/mui-base/src/SelectUnstyled/useSelect.ts:220:        (onChange as (value: TValue[]) => void)?.(newValues);
packages/mui-base/src/SelectUnstyled/useSelect.ts:233:      onChange: (option: SelectOption<TValue> | null) => {
packages/mui-base/src/SelectUnstyled/useSelect.ts:235:        (onChange as (value: TValue | null) => void)?.(option?.value ?? null);
packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.tsx:95:    onChange,
packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.tsx:157:    onChange,
packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.tsx:322:  onChange: PropTypes.func,
packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.types.ts:62:  onChange?: (value: TValue[]) => void;
packages/mui-base/src/ListboxUnstyled/useListbox.types.ts:181:  onChange?: (value: TOption) => void;
packages/mui-base/src/ListboxUnstyled/useListbox.types.ts:201:  onChange?: (value: TOption[]) => void;
packages/mui-base/src/ListboxUnstyled/useControllableReducer.ts:64:      const onChange = propsRef.current.onChange as ((value: TOption[]) => void) | undefined;
packages/mui-base/src/ListboxUnstyled/useControllableReducer.ts:67:        onChange?.(nextSelectedValues);
packages/mui-base/src/ListboxUnstyled/useControllableReducer.ts:72:      const onChange = propsRef.current.onChange as ((value: TOption | null) => void) | undefined;
packages/mui-base/src/ListboxUnstyled/useControllableReducer.ts:75:        onChange?.(nextSelectedValue);
packages/mui-joy/src/Select/Select.tsx:272:    onChange,
packages/mui-joy/src/Select/Select.tsx:382:    onChange,
packages/mui-joy/src/Select/Select.tsx:633:  onChange: PropTypes.func,
packages/mui-joy/src/Select/SelectProps.ts:107:  onChange?: (value: TValue | null) => void;
```

**tool call: Bash**

```bash
cat packages/mui-base/src/ListboxUnstyled/useControllableReducer.ts; cat packages/mui-base/src/ListboxUnstyled/useListbox.ts; sed -n 1,210p packages/mui-base/src/ListboxUnstyled/useListbox.types.ts
```

tool result:

```
import * as React from 'react';
import {
  ListboxAction,
  ListboxReducer,
  ListboxState,
  UseListboxPropsWithDefaults,
} from './useListbox.types';
import areArraysEqual from '../utils/areArraysEqual';

/**
 * Gets the current state. If the selectedValue is controlled,
 * the `value` prop is the source of truth instead of the internal state.
 */
function getControlledState<TOption>(
  internalState: ListboxState<TOption>,
  props: UseListboxPropsWithDefaults<TOption>,
) {
  if (props.value !== undefined) {
    return { ...internalState, selectedValue: props.value };
  }

  return internalState;
}

function areOptionsEqual<TOption>(
  option1: TOption | null,
  option2: TOption | null,
  optionComparer: (optionA: TOption, optionB: TOption) => boolean,
) {
  if (option1 === option2) {
    return true;
  }

  if (option1 === null || option2 === null) {
    return false;
  }

  return optionComparer(option1, option2);
}

/**
 * Triggers change event handlers when reducer returns changed state.
 */
function useStateChangeDetection<TOption>(
  nextState: ListboxState<TOption>,
  internalPreviousState: ListboxState<TOption>,
  propsRef: React.RefObject<UseListboxPropsWithDefaults<TOption>>,
  hasDispatchedActionRef: React.MutableRefObject<boolean>,
) {
  React.useEffect(() => {
    if (!propsRef.current || !hasDispatchedActionRef.current) {
      // Detect changes only if an action has been dispatched.
      return;
    }

    hasDispatchedActionRef.current = false;

    const previousState = getControlledState(internalPreviousState, propsRef.current);
    const { multiple, optionComparer } = propsRef.current;

    if (multiple) {
      const previousSelectedValues = (previousState?.selectedValue ?? []) as TOption[];
      const nextSelectedValues = nextState.selectedValue as TOption[];
      const onChange = propsRef.current.onChange as ((value: TOption[]) => void) | undefined;

      if (!areArraysEqual(nextSelectedValues, previousSelectedValues, optionComparer)) {
        onChange?.(nextSelectedValues);
      }
    } else {
      const previousSelectedValue = previousState?.selectedValue as TOption | null;
      const nextSelectedValue = nextState.selectedValue as TOption | null;
      const onChange = propsRef.current.onChange as ((value: TOption | null) => void) | undefined;

      if (!areOptionsEqual(nextSelectedValue, previousSelectedValue, optionComparer)) {
        onChange?.(nextSelectedValue);
      }
    }
  }, [nextState.selectedValue, internalPreviousState, propsRef, hasDispatchedActionRef]);

  React.useEffect(() => {
    if (!propsRef.current) {
      return;
    }

    // Fires the highlightChange event when reducer returns changed `highlightedValue`.
    if (
      !areOptionsEqual(
        internalPreviousState.highlightedValue,
        nextState.highlightedValue,
        propsRef.current.optionComparer,
      )
    ) {
      propsRef.current?.onHighlightChange?.(nextState.highlightedValue);
    }
  }, [nextState.highlightedValue, internalPreviousState.highlightedValue, propsRef]);
}

export default function useControllableReducer<TOption>(
  internalReducer: ListboxReducer<TOption>,
  externalReducer: ListboxReducer<TOption> | undefined,
  props: UseListboxPropsWithDefaults<TOption>,
): [ListboxState<TOption>, (action: ListboxAction<TOption>) => void] {
  const { value, defaultValue } = props;

  const propsRef = React.useRef(props);
  propsRef.current = props;

  const hasDispatchedActionRef = React.useRef(false);

  const initialSelectedValue =
    (value === undefined ? defaultValue : value) ?? (props.multiple ? [] : null);

  const initalState = {
    highlightedValue: null,
    selectedValue: initialSelectedValue,
  };

  const combinedReducer = React.useCallback(
    (state: ListboxState<TOption>, action: ListboxAction<TOption>) => {
      hasDispatchedActionRef.current = true;

      if (externalReducer) {
        return externalReducer(getControlledState(state, propsRef.current), action);
      }

      return internalReducer(getControlledState(state, propsRef.current), action);
    },
    [externalReducer, internalReducer, propsRef],
  );

  const [nextState, dispatch] = React.useReducer(combinedReducer, initalState);

  const previousState = React.useRef<ListboxState<TOption>>(initalState);
  React.useEffect(() => {
    previousState.current = nextState;
  }, [previousState, nextState]);

  useStateChangeDetection<TOption>(
    nextState,
    previousState.current,
    propsRef,
    hasDispatchedActionRef,
  );
  return [getControlledState(nextState, propsRef.current), dispatch];
}
import * as React from 'react';
import { unstable_useForkRef as useForkRef, unstable_useId as useId } from '@mui/utils';
import {
  UseListboxParameters,
  UseListboxPropsWithDefaults,
  ActionTypes,
  OptionState,
  UseListboxOptionSlotProps,
  UseListboxRootSlotProps,
} from './useListbox.types';
import defaultReducer from './defaultListboxReducer';
import useControllableReducer from './useControllableReducer';
import areArraysEqual from '../utils/areArraysEqual';
import { EventHandlers } from '../utils/types';

const TEXT_NAVIGATION_RESET_TIMEOUT = 500; // milliseconds

const defaultOptionComparer = <TOption>(optionA: TOption, optionB: TOption) => optionA === optionB;
const defaultIsOptionDisabled = () => false;
const defaultOptionStringifier = <TOption>(option: TOption) =>
  typeof option === 'string' ? option : String(option);

export default function useListbox<TOption>(props: UseListboxParameters<TOption>) {
  const {
    disabledItemsFocusable = false,
    disableListWrap = false,
    focusManagement = 'activeDescendant',
    id: idProp,
    isOptionDisabled = defaultIsOptionDisabled,
    listboxRef: externalListboxRef,
    multiple = false,
    optionComparer = defaultOptionComparer,
    optionStringifier = defaultOptionStringifier,
    options,
    stateReducer: externalReducer,
  } = props;

  const id = useId(idProp);

  function defaultIdGenerator(_: TOption, index: num
[... 13259 more characters not shown]
```

**tool call: Bash**

```bash
git log --oneline -1; ls packages/mui-base/src/ListboxUnstyled packages/mui-base/src/SelectUnstyled packages/mui-base/src/MultiSelectUnstyled; grep -rn "onChange\|changeEvent\|event" packages/mui-base/src/ListboxUnstyled/*.test.* packages/mui-base/src/SelectUnstyled/*.test.* packages/mui-base/src/MultiSelectUnstyled/*.test.* | head -50
```

tool result:

```
d88ab9ebdc [docs] Add notification for MUI Base announcement post (#34295)
packages/mui-base/src/ListboxUnstyled:
defaultListboxReducer.test.ts
defaultListboxReducer.ts
index.ts
useControllableReducer.test.tsx
useControllableReducer.ts
useListbox.test.tsx
useListbox.ts
useListbox.types.ts

packages/mui-base/src/MultiSelectUnstyled:
MultiSelectUnstyled.spec.tsx
MultiSelectUnstyled.test.tsx
MultiSelectUnstyled.tsx
MultiSelectUnstyled.types.ts
index.ts

packages/mui-base/src/SelectUnstyled:
SelectUnstyled.spec.tsx
SelectUnstyled.test.tsx
SelectUnstyled.tsx
SelectUnstyled.types.ts
SelectUnstyledContext.ts
defaultOptionStringifier.ts
index.ts
selectUnstyledClasses.ts
useSelect.ts
useSelect.types.ts
utils.tsx
packages/mui-base/src/ListboxUnstyled/defaultListboxReducer.test.ts:31:        event: {} as any, // not relevant
packages/mui-base/src/ListboxUnstyled/defaultListboxReducer.test.ts:57:        event: {} as any, // not relevant
packages/mui-base/src/ListboxUnstyled/defaultListboxReducer.test.ts:82:        event: {} as any, // not relevant
packages/mui-base/src/ListboxUnstyled/defaultListboxReducer.test.ts:107:        event: {} as any, // not relevant
packages/mui-base/src/ListboxUnstyled/defaultListboxReducer.test.ts:135:          event: {
packages/mui-base/src/ListboxUnstyled/defaultListboxReducer.test.ts:163:          event: {
packages/mui-base/src/ListboxUnstyled/defaultListboxReducer.test.ts:191:          event: {
packages/mui-base/src/ListboxUnstyled/defaultListboxReducer.test.ts:219:          event: {
packages/mui-base/src/ListboxUnstyled/defaultListboxReducer.test.ts:245:          event: {
packages/mui-base/src/ListboxUnstyled/defaultListboxReducer.test.ts:273:          event: {
packages/mui-base/src/ListboxUnstyled/defaultListboxReducer.test.ts:299:          event: {
packages/mui-base/src/ListboxUnstyled/useControllableReducer.test.tsx:77:    it('calls onChange when the reducer returns a modified selected value', () => {
packages/mui-base/src/ListboxUnstyled/useControllableReducer.test.tsx:99:          onChange: handleChange,
packages/mui-base/src/ListboxUnstyled/useControllableReducer.test.tsx:134:          onChange: handleChange,
packages/mui-base/src/ListboxUnstyled/useListbox.test.tsx:61:  describe('preventing default behavior on keyDown', () => {
packages/mui-base/src/ListboxUnstyled/useListbox.test.tsx:63:      it(`prevents default behavior when ${key} is pressed in activeDescendant focus management mode`, () => {
packages/mui-base/src/ListboxUnstyled/useListbox.test.tsx:73:        const event = createEvent.keyDown(listbox, {
packages/mui-base/src/ListboxUnstyled/useListbox.test.tsx:77:        event.preventDefault = spy();
packages/mui-base/src/ListboxUnstyled/useListbox.test.tsx:78:        fireEvent(listbox, event);
packages/mui-base/src/ListboxUnstyled/useListbox.test.tsx:80:        expect((event.preventDefault as SinonSpy).calledOnce).to.equal(true);
packages/mui-base/src/ListboxUnstyled/useListbox.test.tsx:85:      it(`prevents default behavior when ${key} is pressed in DOM focus management mode`, () => {
packages/mui-base/src/ListboxUnstyled/useListbox.test.tsx:95:        const event = createEvent.keyDown(listbox, {
packages/mui-base/src/ListboxUnstyled/useListbox.test.tsx:99:        event.preventDefault = spy();
packages/mui-base/src/ListboxUnstyled/useListbox.test.tsx:100:        fireEvent(listbox, event);
packages/mui-base/src/ListboxUnstyled/useListbox.test.tsx:102:        expect((event.preventDefault as SinonSpy).calledOnce).to.equal(true);
packages/mui-base/src/ListboxUnstyled/useListbox.test.tsx:107:      it(`does not prevent default behavior when ${key} is pressed in DOM focus management mode`, () => {
packages/mui-base/src/ListboxUnstyled/useListbox.test.tsx:117:        const event = createEvent.keyDown(listbox, {
packages/mui-base/src/ListboxUnstyled/useListbox.test.tsx:121:        event.preventDefault = spy();
packages/mui-base/src/ListboxUnstyled/useListbox.test.tsx:122:        fireEvent(listbox, event);
packages/mui-base/src/ListboxUnstyled/useListbox.test.tsx:124:        expect((event.preventDefault as SinonSpy).notCalled).to.equal(true);
packages/mui-base/src/SelectUnstyled/SelectUnstyled.test.tsx:343:      const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
packages/mui-base/src/SelectUnstyled/SelectUnstyled.test.tsx:344:        event.preventDefault();
packages/mui-base/src/SelectUnstyled/SelectUnstyled.test.tsx:345:        const formData = new FormData(event.currentTarget);
packages/mui-base/src/SelectUnstyled/SelectUnstyled.test.tsx:376:      const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
packages/mui-base/src/SelectUnstyled/SelectUnstyled.test.tsx:377:        event.preventDefault();
packages/mui-base/src/SelectUnstyled/SelectUnstyled.test.tsx:378:        const formData = new FormData(event.currentTarget);
packages/mui-base/src/SelectUnstyled/SelectUnstyled.test.tsx:416:      const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
packages/mui-base/src/SelectUnstyled/SelectUnstyled.test.tsx:417:        event.preventDefault();
packages/mui-base/src/SelectUnstyled/SelectUnstyled.test.tsx:418:        const formData = new FormData(event.currentTarget);
packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.test.tsx:139:      const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.test.tsx:140:        event.preventDefault();
packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.test.tsx:141:        const formData = new FormData(event.currentTarget);
packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.test.tsx:168:      const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.test.tsx:169:        event.preventDefault();
packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.test.tsx:170:        const formData = new FormData(event.curren
[... 707 more characters not shown]
```

**tool call: Bash**

```bash
sed -n 70,160p packages/mui-base/src/ListboxUnstyled/useControllableReducer.test.tsx; sed -n 225,290p packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.test.tsx; grep -n "onChange\|handleChange" -A3 packages/mui-base/src/SelectUnstyled/SelectUnstyled.test.tsx packages/mui-joy/src/Select/Select.test.tsx | head -80
```

tool result:

```
      };

      render(<TestComponent />);
      expect(internalReducer.notCalled).to.equal(true);
      expect(externalReducer.getCalls()[0].args[1]).to.equal(actionToDispatch);
    });

    it('calls onChange when the reducer returns a modified selected value', () => {
      const reducer = spy((state: ListboxState<string>) => {
        return {
          ...state,
          selectedValue: 'b',
        };
      });

      const actionToDispatch = { type: ActionTypes.setValue as const, value: 'b' };
      const handleChange = spy();
      const handleHighlightChange = spy();

      const TestComponent = () => {
        const props: UseListboxPropsWithDefaults<string> = {
          options: ['a', 'b', 'c'],
          defaultValue: 'a',
          isOptionDisabled: () => false,
          disableListWrap: false,
          disabledItemsFocusable: false,
          optionComparer: (a, b) => a === b,
          optionStringifier: (option) => option,
          multiple: false,
          onChange: handleChange,
          onHighlightChange: handleHighlightChange,
        };
        const [, dispatch] = useControllableReducer(reducer, undefined, props);
        React.useEffect(() => dispatch(actionToDispatch), [dispatch]);
        return null;
      };

      render(<TestComponent />);
      expect(handleChange.getCalls()[0].args[0]).to.equal('b');
      expect(handleHighlightChange.notCalled).to.equal(true);
    });

    it('calls onHighlightChange when the reducer returns a modified highlighted value', () => {
      const reducer = spy((state: ListboxState<string>) => {
        return {
          ...state,
          highlightedValue: 'b',
        };
      });

      const actionToDispatch = { type: ActionTypes.setHighlight as const, highlight: 'b' };
      const handleChange = spy();
      const handleHighlightChange = spy();

      const TestComponent = () => {
        const props: UseListboxPropsWithDefaults<string> = {
          options: ['a', 'b', 'c'],
          defaultValue: 'a',
          isOptionDisabled: () => false,
          disableListWrap: false,
          disabledItemsFocusable: false,
          optionComparer: (a, b) => a === b,
          optionStringifier: (option) => option,
          multiple: false,
          onChange: handleChange,
          onHighlightChange: handleHighlightChange,
        };
        const [, dispatch] = useControllableReducer(reducer, undefined, props);
        React.useEffect(() => dispatch(actionToDispatch), [dispatch]);
        return null;
      };

      render(<TestComponent />);
      expect(handleHighlightChange.getCalls()[0].args[0]).to.equal('b');
      expect(handleChange.notCalled).to.equal(true);
    });
  });
});
        </form>,
      );

      const button = getByText('Submit');
      act(() => {
        button.click();
      });
    });
  });

  it('does not call onChange if `value` is modified externally', () => {
    function TestComponent({ onChange }: { onChange: (value: number[]) => void }) {
      const [value, setValue] = React.useState([1]);
      const handleChange = (newValue: number[]) => {
        setValue(newValue);
        onChange(newValue);
      };

      return (
        <div>
          <button onClick={() => setValue([1, 2])}>Update value</button>
          <MultiSelectUnstyled value={value} onChange={handleChange}>
            <OptionUnstyled value={1}>1</OptionUnstyled>
            <OptionUnstyled value={2}>2</OptionUnstyled>
          </MultiSelectUnstyled>
        </div>
      );
    }

    const onChange = sinon.spy();
    const { getByText } = render(<TestComponent onChange={onChange} />);

    const button = getByText('Update value');
    act(() => button.click());
    expect(onChange.notCalled).to.equal(true);
  });

  it('sets a value correctly when interacted by a user and external code', () => {
    function TestComponent() {
      const [value, setValue] = React.useState<number[]>([]);

      return (
        <div>
          <button data-testid="update-externally" onClick={() => setValue([1])}>
            Update value
          </button>
          <MultiSelectUnstyled
            value={value}
            onChange={setValue}
            componentsProps={{
              root: {
                'data-testid': 'select',
              } as any,
            }}
          >
            <OptionUnstyled value={1}>1</OptionUnstyled>
            <OptionUnstyled value={2}>2</OptionUnstyled>
          </MultiSelectUnstyled>
        </div>
      );
    }

    const { getByTestId, getByText } = render(<TestComponent />);
    const updateButton = getByTestId('update-externally');
    const selectButton = getByTestId('select');

packages/mui-joy/src/Select/Select.test.tsx:89:    const handleChange = spy();
packages/mui-joy/src/Select/Select.test.tsx-90-    const handleClose = spy();
packages/mui-joy/src/Select/Select.test.tsx-91-    render(
packages/mui-joy/src/Select/Select.test.tsx:92:      <Select defaultListboxOpen onChange={handleChange} onClose={handleClose} value="second">
packages/mui-joy/src/Select/Select.test.tsx-93-        <Option value="first" />
packages/mui-joy/src/Select/Select.test.tsx-94-        <Option value="second" />
packages/mui-joy/src/Select/Select.test.tsx-95-      </Select>,
--
packages/mui-joy/src/Select/Select.test.tsx:102:    expect(handleChange.callCount).to.equal(0);
packages/mui-joy/src/Select/Select.test.tsx-103-    expect(handleClose.callCount).to.equal(1);
packages/mui-joy/src/Select/Select.test.tsx-104-  });
packages/mui-joy/src/Select/Select.test.tsx-105-
--
packages/mui-joy/src/Select/Select.test.tsx:114:  describe('prop: onChange', () => {
packages/mui-joy/src/Select/Select.test.tsx-115-    it('should get selected value from the 1st argument', () => {
packages/mui-joy/src/Select/Select.test.tsx:116:      const onChangeHandler = spy();
packages/mui-joy/src/Select/Select.test.tsx-117-      const { getAllByRole, getByRole } = render(
packages/mui-joy/src/Select/Select.test.tsx:118:        <Se
[... 3415 more characters not shown]
```

**tool call: Bash**

```bash
cat packages/mui-base/src/SelectUnstyled/useSelect.ts; sed -n 30,60p packages/mui-base/src/SelectUnstyled/useSelect.types.ts; cat packages/mui-base/src/ListboxUnstyled/defaultListboxReducer.ts | grep -n "action\.\|case"
```

tool result:

```
import * as React from 'react';
import {
  unstable_useControlled as useControlled,
  unstable_useForkRef as useForkRef,
} from '@mui/utils';
import { useButton } from '../ButtonUnstyled';
import {
  SelectOption,
  UseSelectButtonSlotProps,
  UseSelectListboxSlotProps,
  UseSelectMultiParameters,
  UseSelectMultiResult,
  UseSelectOptionSlotProps,
  UseSelectParameters,
  UseSelectSingleParameters,
  UseSelectSingleResult,
} from './useSelect.types';
import {
  ListboxReducer,
  useListbox,
  defaultListboxReducer,
  ActionTypes,
  UseListboxParameters,
} from '../ListboxUnstyled';
import { EventHandlers } from '../utils/types';
import defaultOptionStringifier from './defaultOptionStringifier';

function useSelect<TValue>(props: UseSelectSingleParameters<TValue>): UseSelectSingleResult<TValue>;
function useSelect<TValue>(props: UseSelectMultiParameters<TValue>): UseSelectMultiResult<TValue>;
function useSelect<TValue>(props: UseSelectParameters<TValue>) {
  const {
    buttonRef: buttonRefProp,
    defaultValue,
    disabled = false,
    listboxId,
    listboxRef: listboxRefProp,
    multiple = false,
    onChange,
    onOpenChange,
    open = false,
    options,
    optionStringifier = defaultOptionStringifier,
    value: valueProp,
  } = props;

  const buttonRef = React.useRef<HTMLElement>(null);
  const handleButtonRef = useForkRef(buttonRefProp, buttonRef);

  const listboxRef = React.useRef<HTMLElement | null>(null);

  const [value, setValue] = useControlled({
    controlled: valueProp,
    default: defaultValue,
    name: 'SelectUnstyled',
    state: 'value',
  });

  // prevents closing the listbox on keyUp right after opening it
  const ignoreEnterKeyUp = React.useRef(false);

  // prevents reopening the listbox when button is clicked
  // (listbox closes on lost focus, then immediately reopens on click)
  const ignoreClick = React.useRef(false);

  // Ensure the listbox is focused after opening
  const [listboxFocusRequested, requestListboxFocus] = React.useState(false);

  const focusListboxIfRequested = React.useCallback(() => {
    if (listboxFocusRequested && listboxRef.current != null) {
      listboxRef.current.focus();
      requestListboxFocus(false);
    }
  }, [listboxFocusRequested]);

  const updateListboxRef = (listboxElement: HTMLUListElement | null) => {
    listboxRef.current = listboxElement;
    focusListboxIfRequested();
  };

  const handleListboxRef = useForkRef(useForkRef(listboxRefProp, listboxRef), updateListboxRef);

  React.useEffect(() => {
    focusListboxIfRequested();
  }, [focusListboxIfRequested]);

  React.useEffect(() => {
    requestListboxFocus(open);
  }, [open]);

  const createHandleMouseDown =
    (otherHandlers?: Record<string, React.EventHandler<any>>) =>
    (event: React.MouseEvent<HTMLElement>) => {
      otherHandlers?.onMouseDown?.(event);
      if (!event.defaultPrevented && open) {
        ignoreClick.current = true;
      }
    };

  const createHandleButtonClick =
    (otherHandlers?: Record<string, React.EventHandler<any>>) => (event: React.MouseEvent) => {
      otherHandlers?.onClick?.(event);
      if (!event.defaultPrevented && !ignoreClick.current) {
        onOpenChange?.(!open);
      }

      ignoreClick.current = false;
    };

  const createHandleButtonKeyDown =
    (otherHandlers?: Record<string, React.EventHandler<any>>) => (event: React.KeyboardEvent) => {
      otherHandlers?.onKeyDown?.(event);
      if (event.defaultPrevented) {
        return;
      }

      if (event.key === 'Enter') {
        ignoreEnterKeyUp.current = true;
      }

      if (event.key === 'ArrowDown' || event.key === 'ArrowUp') {
        event.preventDefault();
        onOpenChange?.(true);
      }
    };

  const createHandleListboxKeyUp =
    (otherHandlers?: Record<string, React.EventHandler<any>>) => (event: React.KeyboardEvent) => {
      otherHandlers?.onKeyUp?.(event);
      if (event.defaultPrevented) {
        return;
      }

      const closingKeys = multiple ? ['Escape'] : ['Escape', 'Enter', ' '];

      if (open && !ignoreEnterKeyUp.current && closingKeys.includes(event.key)) {
        buttonRef?.current?.focus();
      }

      ignoreEnterKeyUp.current = false;
    };

  const createHandleListboxItemClick =
    (otherHandlers?: Record<string, React.EventHandler<any>>) => (event: React.MouseEvent) => {
      otherHandlers?.onClick?.(event);
      if (event.defaultPrevented) {
        return;
      }

      if (!multiple) {
        onOpenChange?.(false);
      }
    };

  const createHandleListboxBlur =
    (otherHandlers?: Record<string, React.EventHandler<any>>) => (event: React.FocusEvent) => {
      otherHandlers?.onBlur?.(event);
      if (!event.defaultPrevented) {
        onOpenChange?.(false);
      }
    };

  const listboxReducer: ListboxReducer<SelectOption<TValue>> = (state, action) => {
    const newState = defaultListboxReducer(state, action);

    // change selection when listbox is closed
    if (
      action.type === ActionTypes.keyDown &&
      !open &&
      (action.event.key === 'ArrowUp' || action.event.key === 'ArrowDown')
    ) {
      return {
        ...newState,
        selectedValue: newState.highlightedValue,
      };
    }

    if (
      action.type === ActionTypes.blur ||
      action.type === ActionTypes.setValue ||
      action.type === ActionTypes.optionsChange
    ) {
      return {
        ...newState,
        highlightedValue: newState.selectedValue as SelectOption<TValue>,
      };
    }

    return newState;
  };

  const {
    getRootProps: getButtonRootProps,
    active: buttonActive,
    focusVisible: buttonFocusVisible,
  } = useButton({
    disabled,
    ref: handleButtonRef,
  });

  const selectedOption = React.useMemo(
    () =>
      props.multiple
        ? props.options.filter((o) => (value as TValue[]).includes(o.value))
        : props.options.find((o) => o.value === value) ?? null,
    [props.multiple, props.options, value],
  );

  let useListboxParameters: UseListboxPar
[... 4546 more characters not shown]
```

**thinking:**

```
I'll have every listbox action carry its event (or null), store the last dispatched action in a ref, and pass its event to onChange. Now checking what other code relies on these APIs.


```

**tool call: Bash**

```bash
grep -rn "setSelectedValue\|setHighlightedValue\|onHighlightChange\|ActionTypes\.\(setValue\|setHighlight\|optionsChange\|textNavigation\)" packages docs/data --include=*.ts --include=*.tsx --include=*.js | grep -v "\.test\."
```

tool result:

```
(eval):1: no matches found: --include=*.ts
```

**tool call: Bash**

```bash
grep -rn "setSelectedValue\|setHighlightedValue\|onHighlightChange\|ActionTypes\.\(setValue\|setHighlight\|optionsChange\|textNavigation\)" packages docs/data docs/pages/base | grep -v "\.test\.\|node_modules\|/build/"
```

tool result:

```
packages/mui-base/src/SelectUnstyled/useSelect.ts:179:      action.type === ActionTypes.setValue ||
packages/mui-base/src/SelectUnstyled/useSelect.ts:180:      action.type === ActionTypes.optionsChange
packages/mui-base/src/ListboxUnstyled/useListbox.ts:88:      type: ActionTypes.optionsChange,
packages/mui-base/src/ListboxUnstyled/useListbox.ts:100:  const setSelectedValue = React.useCallback(
packages/mui-base/src/ListboxUnstyled/useListbox.ts:103:        type: ActionTypes.setValue,
packages/mui-base/src/ListboxUnstyled/useListbox.ts:110:  const setHighlightedValue = React.useCallback(
packages/mui-base/src/ListboxUnstyled/useListbox.ts:113:        type: ActionTypes.setHighlight,
packages/mui-base/src/ListboxUnstyled/useListbox.ts:205:          type: ActionTypes.textNavigation,
packages/mui-base/src/ListboxUnstyled/useListbox.ts:316:    setSelectedValue,
packages/mui-base/src/ListboxUnstyled/useListbox.ts:317:    setHighlightedValue,
packages/mui-base/src/ListboxUnstyled/defaultListboxReducer.ts:352:    case ActionTypes.setValue:
packages/mui-base/src/ListboxUnstyled/defaultListboxReducer.ts:357:    case ActionTypes.setHighlight:
packages/mui-base/src/ListboxUnstyled/defaultListboxReducer.ts:362:    case ActionTypes.textNavigation:
packages/mui-base/src/ListboxUnstyled/defaultListboxReducer.ts:364:    case ActionTypes.optionsChange:
packages/mui-base/src/ListboxUnstyled/useListbox.types.ts:67:  type: ActionTypes.setValue;
packages/mui-base/src/ListboxUnstyled/useListbox.types.ts:72:  type: ActionTypes.setHighlight;
packages/mui-base/src/ListboxUnstyled/useListbox.types.ts:77:  type: ActionTypes.textNavigation;
packages/mui-base/src/ListboxUnstyled/useListbox.types.ts:83:  type: ActionTypes.optionsChange;
packages/mui-base/src/ListboxUnstyled/useListbox.types.ts:138:  onHighlightChange?: (option: TOption | null) => void;
packages/mui-base/src/ListboxUnstyled/useControllableReducer.ts:93:      propsRef.current?.onHighlightChange?.(nextState.highlightedValue);
packages/mui-base/src/MenuUnstyled/useMenu.ts:25:    action.type === ActionTypes.setValue
packages/mui-base/src/MenuUnstyled/useMenu.ts:33:    action.type !== ActionTypes.setHighlight &&
packages/mui-base/src/MenuUnstyled/useMenu.ts:75:    setHighlightedValue: setListboxHighlight,
packages/mui-base/src/AutocompleteUnstyled/useAutocomplete.js:98:    onHighlightChange,
packages/mui-base/src/AutocompleteUnstyled/useAutocomplete.js:321:    if (onHighlightChange) {
packages/mui-base/src/AutocompleteUnstyled/useAutocomplete.js:322:      onHighlightChange(event, index === -1 ? null : filteredOptions[index], reason);
packages/mui-base/src/AutocompleteUnstyled/useAutocomplete.d.ts:229:  onHighlightChange?: (
packages/mui-material/src/Autocomplete/Autocomplete.js:410:    onHighlightChange,
packages/mui-material/src/Autocomplete/Autocomplete.js:955:  onHighlightChange: PropTypes.func,
docs/data/joy/components/radio/RadioButtons.js:6:  const [selectedValue, setSelectedValue] = React.useState('a');
docs/data/joy/components/radio/RadioButtons.js:9:    setSelectedValue(event.target.value);
docs/data/material/components/dialogs/SimpleDialog.js:65:  const [selectedValue, setSelectedValue] = React.useState(emails[1]);
docs/data/material/components/dialogs/SimpleDialog.js:73:    setSelectedValue(value);
docs/data/material/components/dialogs/SimpleDialog.tsx:63:  const [selectedValue, setSelectedValue] = React.useState(emails[1]);
docs/data/material/components/dialogs/SimpleDialog.tsx:71:    setSelectedValue(value);
docs/data/material/components/radio-buttons/RadioButtons.tsx:5:  const [selectedValue, setSelectedValue] = React.useState('a');
docs/data/material/components/radio-buttons/RadioButtons.tsx:8:    setSelectedValue(event.target.value);
docs/data/material/components/radio-buttons/SizeRadioButtons.tsx:5:  const [selectedValue, setSelectedValue] = React.useState('a');
docs/data/material/components/radio-buttons/SizeRadioButtons.tsx:7:    setSelectedValue(event.target.value);
docs/data/material/components/radio-buttons/ColorRadioButtons.tsx:6:  const [selectedValue, setSelectedValue] = React.useState('a');
docs/data/material/components/radio-buttons/ColorRadioButtons.tsx:9:    setSelectedValue(event.target.value);
docs/data/material/components/radio-buttons/SizeRadioButtons.js:5:  const [selectedValue, setSelectedValue] = React.useState('a');
docs/data/material/components/radio-buttons/SizeRadioButtons.js:7:    setSelectedValue(event.target.value);
docs/data/material/components/radio-buttons/ColorRadioButtons.js:6:  const [selectedValue, setSelectedValue] = React.useState('a');
docs/data/material/components/radio-buttons/ColorRadioButtons.js:9:    setSelectedValue(event.target.value);
docs/data/material/components/radio-buttons/RadioButtons.js:5:  const [selectedValue, setSelectedValue] = React.useState('a');
docs/data/material/components/radio-buttons/RadioButtons.js:8:    setSelectedValue(event.target.value);
```

**assistant:** Now the type changes in `useListbox.types.ts`:

**tool call: Bash**

```bash
cd packages/mui-base/src/ListboxUnstyled && python3 - <<'EOF'
p='useListbox.types.ts'
s=open(p).read()
s=s.replace("""interface SetValueAction<TOption> {
  type: ActionTypes.setValue;
  value""","""interface SetValueAction<TOption> {
  type: ActionTypes.setValue;
  event: null;
  value""")
s=s.replace("""interface SetHighlightAction<TOption> {
  type: ActionTypes.setHighlight;
  highlight""","""interface SetHighlightAction<TOption> {
  type: ActionTypes.setHighlight;
  event: null;
  highlight""")
s=s.replace("""interface TextNavigationAction<TOption> {
  type: ActionTypes.textNavigation;
""","""interface TextNavigationAction<TOption> {
  type: ActionTypes.textNavigation;
  event: React.KeyboardEvent;
""")
s=s.replace("""interface OptionsChangeAction<TOption> {
  type: ActionTypes.optionsChange;
""","""interface OptionsChangeAction<TOption> {
  type: ActionTypes.optionsChange;
  event: null;
""")
s=s.replace("""  onHighlightChange?: (option: TOption | null) => void;""","""  onHighlightChange?: (
    e: React.MouseEvent | React.KeyboardEvent | React.FocusEvent | null,
    option: TOption | null,
  ) => void;""")
s=s.replace("""  onChange?: (value: TOption) => void;""","""  onChange?: (
    e: React.MouseEvent | React.KeyboardEvent | React.FocusEvent | null,
    value: TOption,
  ) => void;""")
s=s.replace("""  onChange?: (value: TOption[]) => void;""","""  onChange?: (
    e: React.MouseEvent | React.KeyboardEvent | React.FocusEvent | null,
    value: TOption[],
  ) => void;""")
open(p,'w').write(s)
EOF
git diff --stat
```

tool result:

```
 package.json                                       |     9 +-
 .../src/ListboxUnstyled/useListbox.types.ts        |    19 +-
 yarn.lock                                          | 28724 ++++++++++---------
 3 files changed, 14953 insertions(+), 13799 deletions(-)
```

**thinking:**

```
`package.json` and `yarn.lock` were already modified by the environment setup, so I'll leave them as is. Now I'll rewrite the change detection logic in `useControllableReducer.ts`.


```

**tool call: Bash**

```bash
python3 - <<'EOF'
p='useControllableReducer.ts'
s=open(p).read()
old_start=s.index("/**\n * Triggers change event handlers")
old_end=s.index("export default function")
s=s[:old_start]+'''/**
 * Triggers change event handlers when reducer returns changed state.
 */
function useStateChangeDetection<TOption>(
  nextState: ListboxState<TOption>,
  internalPreviousState: ListboxState<TOption>,
  propsRef: React.RefObject<UseListboxPropsWithDefaults<TOption>>,
  lastActionRef: React.MutableRefObject<ListboxAction<TOption> | null>,
) {
  React.useEffect(() => {
    if (!propsRef.current || lastActionRef.current === null) {
      // Detect changes only if an action has been dispatched.
      return;
    }

    const previousState = getControlledState(internalPreviousState, propsRef.current);
    const { multiple, optionComparer } = propsRef.current;

    if (multiple) {
      const previousSelectedValues = (previousState?.selectedValue ?? []) as TOption[];
      const nextSelectedValues = nextState.selectedValue as TOption[];
      const onChange = propsRef.current.onChange as
        | ((
            e: React.MouseEvent | React.KeyboardEvent | React.FocusEvent | null,
            value: TOption[],
          ) => void)
        | undefined;

      if (!areArraysEqual(nextSelectedValues, previousSelectedValues, optionComparer)) {
        onChange?.(lastActionRef.current.event, nextSelectedValues);
      }
    } else {
      const previousSelectedValue = previousState?.selectedValue as TOption | null;
      const nextSelectedValue = nextState.selectedValue as TOption | null;
      const onChange = propsRef.current.onChange as
        | ((
            e: React.MouseEvent | React.KeyboardEvent | React.FocusEvent | null,
            value: TOption | null,
          ) => void)
        | undefined;

      if (!areOptionsEqual(nextSelectedValue, previousSelectedValue, optionComparer)) {
        onChange?.(lastActionRef.current.event, nextSelectedValue);
      }
    }

    // Fires the highlightChange event when reducer returns changed `highlightedValue`.
    if (
      !areOptionsEqual(
        internalPreviousState.highlightedValue,
        nextState.highlightedValue,
        propsRef.current.optionComparer,
      )
    ) {
      propsRef.current?.onHighlightChange?.(
        lastActionRef.current.event,
        nextState.highlightedValue,
      );
    }

    lastActionRef.current = null;
  }, [
    nextState.selectedValue,
    nextState.highlightedValue,
    internalPreviousState,
    propsRef,
    lastActionRef,
  ]);
}

'''+s[old_end:]
s=s.replace("""  const hasDispatchedActionRef = React.useRef(false);""","""  const lastActionRef = React.useRef<ListboxAction<TOption> | null>(null);""")
s=s.replace("""      hasDispatchedActionRef.current = true;
""","""      lastActionRef.current = action;
""")
s=s.replace("""    propsRef,
    hasDispatchedActionRef,
  );""","""    propsRef,
    lastActionRef,
  );""")
open(p,'w').write(s)
EOF
git diff useControllableReducer.ts | tail -30
```

tool result:

```
 }
 
 export default function useControllableReducer<TOption>(
@@ -105,7 +118,7 @@ export default function useControllableReducer<TOption>(
   const propsRef = React.useRef(props);
   propsRef.current = props;
 
-  const hasDispatchedActionRef = React.useRef(false);
+  const lastActionRef = React.useRef<ListboxAction<TOption> | null>(null);
 
   const initialSelectedValue =
     (value === undefined ? defaultValue : value) ?? (props.multiple ? [] : null);
@@ -117,7 +130,7 @@ export default function useControllableReducer<TOption>(
 
   const combinedReducer = React.useCallback(
     (state: ListboxState<TOption>, action: ListboxAction<TOption>) => {
-      hasDispatchedActionRef.current = true;
+      lastActionRef.current = action;
 
       if (externalReducer) {
         return externalReducer(getControlledState(state, propsRef.current), action);
@@ -139,7 +152,7 @@ export default function useControllableReducer<TOption>(
     nextState,
     previousState.current,
     propsRef,
-    hasDispatchedActionRef,
+    lastActionRef,
   );
   return [getControlledState(nextState, propsRef.current), dispatch];
 }
```

**assistant:** Now passing events in the `useListbox.ts` dispatches:

**tool call: Bash**

```bash
python3 - <<'EOF'
p='useListbox.ts'
s=open(p).read()
s=s.replace("""      type: ActionTypes.optionsChange,
""","""      type: ActionTypes.optionsChange,
      event: null,
""")
s=s.replace("""        type: ActionTypes.setValue,
""","""        type: ActionTypes.setValue,
        event: null,
""")
s=s.replace("""        type: ActionTypes.setHighlight,
""","""        type: ActionTypes.setHighlight,
        event: null,
""")
s=s.replace("""          type: ActionTypes.textNavigation,
""","""          type: ActionTypes.textNavigation,
          event,
""")
open(p,'w').write(s)
EOF
git diff --stat .
```

tool result:

```
 .../src/ListboxUnstyled/useControllableReducer.ts  | 51 ++++++++++++++--------
 .../mui-base/src/ListboxUnstyled/useListbox.ts     |  4 ++
 .../src/ListboxUnstyled/useListbox.types.ts        | 19 ++++++--
 3 files changed, 52 insertions(+), 22 deletions(-)
```

**assistant:** Now the Select layer: `useSelect` and its types.

**tool call: Bash**

```bash
cd ../SelectUnstyled && python3 - <<'EOF'
p='useSelect.ts'
s=open(p).read()
s=s.replace("""      onChange: (newOptions) => {
        const newValues = newOptions.map((o) => o.value);
        setValue(newValues);
        (onChange as (value: TValue[]) => void)?.(newValues);
      },""","""      onChange: (e, newOptions) => {
        const newValues = newOptions.map((o) => o.value);
        setValue(newValues);
        (onChange as UseSelectMultiParameters<TValue>['onChange'])?.(e, newValues);
      },""")
s=s.replace("""      onChange: (option: SelectOption<TValue> | null) => {
        setValue(option?.value ?? null);
        (onChange as (value: TValue | null) => void)?.(option?.value ?? null);
      },""","""      onChange: (e, option: SelectOption<TValue> | null) => {
        setValue(option?.value ?? null);
        (onChange as UseSelectSingleParameters<TValue>['onChange'])?.(e, option?.value ?? null);
      },""")
open(p,'w').write(s)
p='useSelect.types.ts'
s=open(p).read()
s=s.replace("""  onChange?: (value: TValue | null) => void;""","""  onChange?: (
    e: React.MouseEvent | React.KeyboardEvent | React.FocusEvent | null,
    value: TValue | null,
  ) => void;""")
s=s.replace("""  onChange?: (value: TValue[]) => void;""","""  onChange?: (
    e: React.MouseEvent | React.KeyboardEvent | React.FocusEvent | null,
    value: TValue[],
  ) => void;""")
open(p,'w').write(s)
EOF
head -5 useSelect.types.ts; sed -n 90,105p SelectUnstyled.types.ts; sed -n 55,66p ../MultiSelectUnstyled/MultiSelectUnstyled.types.ts; sed -n 100,110p ../../../mui-joy/src/Select/SelectProps.ts
```

tool result:

```
import React from 'react';
import { UseButtonRootSlotProps } from '../ButtonUnstyled';
import {
  OptionState,
  UseListboxOptionSlotProps,
   * A function to convert the currently selected value to a string.
   * Used to set a value of a hidden input associated with the select,
   * so that the selected value can be posted with a form.
   */
  getSerializedValue?: (
    option: SelectOption<TValue> | null,
  ) => React.InputHTMLAttributes<HTMLInputElement>['value'];
  /**
   * Callback fired when an option is selected.
   */
  onChange?: (value: TValue | null) => void;
  /**
   * A function used to convert the option label to a string.
   * It's useful when labels are elements and need to be converted to plain text
   * to enable navigation using character keys on a keyboard.
   *
   */
  getSerializedValue?: (
    option: SelectOption<TValue>[],
  ) => React.InputHTMLAttributes<HTMLInputElement>['value'];
  /**
   * Callback fired when an option is selected.
   */
  onChange?: (value: TValue[]) => void;
  /**
   * A function used to convert the option label to a string.
   * It's useful when labels are elements and need to be converted to plain text
   * to enable navigation using character keys on a keyboard.
   * The default selected value. Use when the component is not controlled.
   */
  defaultValue?: TValue | null;

  /**
   * Callback fired when an option is selected.
   */
  onChange?: (value: TValue | null) => void;
  /**
   * Function that customizes the rendering of the selected value.
   */
```

**assistant:** Now the public component prop types (SelectUnstyled, MultiSelectUnstyled, Joy Select):

**tool call: Bash**

```bash
cd /work/mui__material-ui-34158/repo && python3 - <<'EOF'
for p,v in [('packages/mui-base/src/SelectUnstyled/SelectUnstyled.types.ts','TValue | null'),
            ('packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.types.ts','TValue[]'),
            ('packages/mui-joy/src/Select/SelectProps.ts','TValue | null')]:
    s=open(p).read()
    old="  onChange?: (value: %s) => void;" % v
    assert old in s, p
    s=s.replace(old,"""  onChange?: (
    e: React.MouseEvent | React.KeyboardEvent | React.FocusEvent | null,
    value: %s,
  ) => void;""" % v)
    open(p,'w').write(s)
EOF
grep -n "^import" packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.types.ts packages/mui-joy/src/Select/SelectProps.ts packages/mui-base/src/SelectUnstyled/SelectUnstyled.types.ts
```

tool result:

```
packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.types.ts:1:import * as React from 'react';
packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.types.ts:2:import { DefaultComponentProps, OverrideProps, Simplify } from '@mui/types';
packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.types.ts:3:import PopperUnstyled, { PopperUnstyledProps } from '../PopperUnstyled';
packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.types.ts:4:import {
packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.types.ts:10:import { SlotComponentProps } from '../utils';
packages/mui-joy/src/Select/SelectProps.ts:1:import React from 'react';
packages/mui-joy/src/Select/SelectProps.ts:2:import { OverridableStringUnion, OverrideProps } from '@mui/types';
packages/mui-joy/src/Select/SelectProps.ts:3:import { SelectUnstyledCommonProps, SelectOption } from '@mui/base/SelectUnstyled';
packages/mui-joy/src/Select/SelectProps.ts:4:import { PopperUnstyledOwnProps } from '@mui/base/PopperUnstyled';
packages/mui-joy/src/Select/SelectProps.ts:5:import { SlotComponentProps } from '@mui/base/utils';
packages/mui-joy/src/Select/SelectProps.ts:6:import { ColorPaletteProp, VariantProp, SxProps } from '../styles/types';
packages/mui-base/src/SelectUnstyled/SelectUnstyled.types.ts:1:import * as React from 'react';
packages/mui-base/src/SelectUnstyled/SelectUnstyled.types.ts:2:import { DefaultComponentProps, OverrideProps, Simplify } from '@mui/types';
packages/mui-base/src/SelectUnstyled/SelectUnstyled.types.ts:3:import {
packages/mui-base/src/SelectUnstyled/SelectUnstyled.types.ts:8:import PopperUnstyled, { PopperUnstyledProps } from '../PopperUnstyled';
packages/mui-base/src/SelectUnstyled/SelectUnstyled.types.ts:9:import { SlotComponentProps } from '../utils';
```

**assistant:** Next, finding docs demos and other code that pass `onChange` to these components:

**tool call: Bash**

```bash
grep -rlE "SelectUnstyled|MultiSelectUnstyled|from '@mui/joy/Select'|useSelect\b" docs/data docs/src packages --include='*.js' --include='*.tsx' --include='*.ts' 2>/dev/null | grep -v "node_modules\|/build/\|\.test\.\|\.spec\." | xargs grep -ln "onChange" 
```

tool result:

```
docs/data/joy/customization/approaches/ButtonThemes.js
docs/data/joy/components/select/SelectFieldDemo.js
docs/data/joy/components/select/SelectUsage.js
docs/data/joy/components/select/SelectClearable.js
docs/data/joy/main-features/automatic-adjustment/ListThemes.js
docs/data/base/components/select/UnstyledSelectControlled.js
docs/data/base/components/select/UnstyledSelectIntroduction.js
docs/data/base/components/select/UnstyledSelectControlled.tsx
docs/data/base/components/select/UnstyledSelectObjectValuesForm.js
docs/data/base/components/select/UnstyledSelectObjectValues.tsx
docs/data/base/components/select/UnstyledSelectObjectValuesForm.tsx
docs/data/base/components/select/UnstyledSelectObjectValues.js
docs/src/modules/components/JoyUsageDemo.tsx
packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.tsx
packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.types.ts
packages/mui-base/src/SelectUnstyled/SelectUnstyled.types.ts
packages/mui-base/src/SelectUnstyled/SelectUnstyled.tsx
packages/mui-base/src/SelectUnstyled/useSelect.ts
packages/mui-joy/src/Select/SelectProps.ts
packages/mui-joy/src/Select/Select.tsx
```

**tool call: Bash**

```bash
for f in $(grep -rlE "SelectUnstyled|MultiSelectUnstyled|from '@mui/joy/Select'" docs/data docs/src docs/pages --include='*.js' --include='*.tsx' --include='*.md' | xargs grep -ln "onChange"); do echo "== $f"; grep -n "onChange\|setValue\|handleChange\|newValue" $f; done
```

tool result:

```
== docs/data/joy/customization/approaches/ButtonThemes.js
563:              onChange={setDesign}
== docs/data/joy/components/select/SelectFieldDemo.js
9:  const [value, setValue] = React.useState('dog');
18:      <Select defaultValue="dog" value={value} onChange={setValue}>
== docs/data/joy/components/select/SelectUsage.js
9:  const [value, setValue] = React.useState(null);
52:          onChange={setValue}
64:                  setValue(null);
== docs/data/joy/components/select/SelectClearable.js
8:  const [value, setValue] = React.useState('dog');
15:      onChange={setValue}
29:              setValue(null);
== docs/data/joy/main-features/automatic-adjustment/ListThemes.js
118:            onChange={setPreset}
== docs/data/base/components/select/UnstyledSelectControlled.js
165:  const [value, setValue] = React.useState(10);
168:      <CustomSelect value={value} onChange={setValue}>
== docs/data/base/components/select/UnstyledSelectIntroduction.js
66:    onChange: PropTypes.func,
== docs/data/base/components/select/UnstyledSelectControlled.tsx
154:  const [value, setValue] = React.useState<number | null>(10);
157:      <CustomSelect value={value} onChange={setValue}>
== docs/data/base/components/select/UnstyledSelectObjectValuesForm.js
207:        <CustomSelect value={character} onChange={setCharacter} name="character">
222:          onChange={setCharacter}
== docs/data/base/components/select/UnstyledSelectObjectValues.tsx
184:      <CustomSelect value={character} onChange={setCharacter}>
== docs/data/base/components/select/UnstyledSelectObjectValuesForm.tsx
202:        <CustomSelect value={character} onChange={setCharacter} name="character">
217:          onChange={setCharacter}
== docs/data/base/components/select/UnstyledSelectObjectValues.js
190:      <CustomSelect value={character} onChange={setCharacter}>
== docs/src/modules/components/JoyUsageDemo.tsx
278:                    onChange={(event) =>
316:                    onChange={(event) =>
358:                    onChange={(event) =>
441:                    onChange={(val) =>
482:                  onChange={(event) =>
509:                  onChange={(event) =>
```

**assistant:** Several demos pass a state setter straight to `onChange`, so they'd break with the new signature. Checking each one's context:

**tool call: Bash**

```bash
sed -n 555,570p docs/data/joy/customization/approaches/ButtonThemes.js; sed -n 112,122p docs/data/joy/main-features/automatic-adjustment/ListThemes.js; sed -n 435,450p docs/src/modules/components/JoyUsageDemo.tsx; sed -n 215,226p docs/data/base/components/select/UnstyledSelectObjectValuesForm.tsx; ls docs/data/joy/components/select/ docs/data/base/components/select/
```

tool result:

```
            <Select
              componentsProps={{
                button: {
                  id: 'button-theme',
                },
              }}
              size="sm"
              value={design}
              onChange={setDesign}
              sx={{ minWidth: 160 }}
            >
              <Option value="github">GitHub</Option>
              <Option value="fluent">Fluent</Option>
              <Option value="chakra">Chakra</Option>
              <Option value="mantine">Mantine</Option>
            </Select>
            componentsProps={{
              button: {
                id: 'list-theme',
              },
            }}
            value={preset}
            onChange={setPreset}
            sx={{ minWidth: 160 }}
          >
            <Option value="">Default</Option>
            <Option value="dense">Dense</Option>
                        sx: {
                          '--List-decorator-size': '24px',
                        },
                      },
                    }}
                    value={(resolvedValue || 'none') as string}
                    onChange={(val) =>
                      setProps((latestProps) => ({
                        ...latestProps,
                        [propName]: val,
                      }))
                    }
                  >
                    {options.map((value) => (
                      <Option
                        key={value}
        <CustomSelect
          value={character}
          onChange={setCharacter}
          getSerializedValue={getSerializedValue}
          name="character"
        >
          {characters.map((c) => (
            <StyledOption key={c.name} value={c}>
              {c.name}
            </StyledOption>
          ))}
        </CustomSelect>
docs/data/base/components/select/:
UnstyledSelectControlled.js
UnstyledSelectControlled.tsx
UnstyledSelectControlled.tsx.preview
UnstyledSelectCustomRenderValue.js
UnstyledSelectCustomRenderValue.tsx
UnstyledSelectCustomRenderValue.tsx.preview
UnstyledSelectGrouping.js
UnstyledSelectGrouping.tsx
UnstyledSelectGrouping.tsx.preview
UnstyledSelectIntroduction.js
UnstyledSelectIntroduction.tsx
UnstyledSelectIntroduction.tsx.preview
UnstyledSelectMultiple.js
UnstyledSelectMultiple.tsx
UnstyledSelectMultiple.tsx.preview
UnstyledSelectObjectValues.js
UnstyledSelectObjectValues.tsx
UnstyledSelectObjectValues.tsx.preview
UnstyledSelectObjectValuesForm.js
UnstyledSelectObjectValuesForm.tsx
UnstyledSelectRichOptions.js
UnstyledSelectRichOptions.tsx
UnstyledSelectRichOptions.tsx.preview
UnstyledSelectSimple.js
UnstyledSelectSimple.tsx
UnstyledSelectSimple.tsx.preview
UseSelect.js
UseSelect.tsx
UseSelect.tsx.preview
select-pt.md
select-zh.md
select.md

docs/data/joy/components/select/:
SelectBasic.js
SelectClearable.js
SelectCustomOption.js
SelectCustomValueAppearance.js
SelectDecorators.js
SelectFieldDemo.js
SelectGroupedOptions.js
SelectIndicator.js
SelectUsage.js
select-pt.md
select-zh.md
select.md
```

**assistant:** I'll update these demos to use the `(event, newValue)` form:

**tool call: Bash**

```bash
files="docs/data/joy/customization/approaches/ButtonThemes.js docs/data/joy/components/select/SelectFieldDemo.js docs/data/joy/components/select/SelectUsage.js docs/data/joy/components/select/SelectClearable.js docs/data/joy/main-features/automatic-adjustment/ListThemes.js docs/data/base/components/select/UnstyledSelectControlled.js docs/data/base/components/select/UnstyledSelectControlled.tsx docs/data/base/components/select/UnstyledSelectObjectValuesForm.js docs/data/base/components/select/UnstyledSelectObjectValuesForm.tsx docs/data/base/components/select/UnstyledSelectObjectValues.js docs/data/base/components/select/UnstyledSelectObjectValues.tsx"
perl -pi -e 's/onChange=\{(set[A-Za-z]+)\}/onChange={(e, newValue) => $1(newValue)}/g' $files
perl -0pi -e 's/onChange=\{\(val\) =>\n/onChange={(e, val) =>\n/' docs/src/modules/components/JoyUsageDemo.tsx
grep -n "onChange" $files docs/src/modules/components/JoyUsageDemo.tsx | grep -v "event) =>"; cat docs/data/base/components/select/UnstyledSelectControlled.tsx.preview docs/data/base/components/select/UnstyledSelectObjectValues.tsx.preview
```

tool result:

```
Can't open docs/data/joy/customization/approaches/ButtonThemes.js docs/data/joy/components/select/SelectFieldDemo.js docs/data/joy/components/select/SelectUsage.js docs/data/joy/components/select/SelectClearable.js docs/data/joy/main-features/automatic-adjustment/ListThemes.js docs/data/base/components/select/UnstyledSelectControlled.js docs/data/base/components/select/UnstyledSelectControlled.tsx docs/data/base/components/select/UnstyledSelectObjectValuesForm.js docs/data/base/components/select/UnstyledSelectObjectValuesForm.tsx docs/data/base/components/select/UnstyledSelectObjectValues.js docs/data/base/components/select/UnstyledSelectObjectValues.tsx: No such file or directory.
grep: docs/data/joy/customization/approaches/ButtonThemes.js docs/data/joy/components/select/SelectFieldDemo.js docs/data/joy/components/select/SelectUsage.js docs/data/joy/components/select/SelectClearable.js docs/data/joy/main-features/automatic-adjustment/ListThemes.js docs/data/base/components/select/UnstyledSelectControlled.js docs/data/base/components/select/UnstyledSelectControlled.tsx docs/data/base/components/select/UnstyledSelectObjectValuesForm.js docs/data/base/components/select/UnstyledSelectObjectValuesForm.tsx docs/data/base/components/select/UnstyledSelectObjectValues.js docs/data/base/components/select/UnstyledSelectObjectValues.tsx: No such file or directory
docs/src/modules/components/JoyUsageDemo.tsx:441:                    onChange={(e, val) =>
<CustomSelect value={value} onChange={setValue}>
  <StyledOption value={10}>Ten</StyledOption>
  <StyledOption value={20}>Twenty</StyledOption>
  <StyledOption value={30}>Thirty</StyledOption>
</CustomSelect>

<Paragraph>Selected value: {value}</Paragraph><CustomSelect value={character} onChange={setCharacter}>
  {characters.map((c) => (
    <StyledOption key={c.name} value={c}>
      {c.name}
    </StyledOption>
  ))}
</CustomSelect>

<Paragraph>Selected character:</Paragraph>
<Pre>{JSON.stringify(character, null, 2)}</Pre>
```

**assistant:** zsh doesn't word-split the variable, so the first command failed. Running it again with an explicit list, this time including the `.preview` files:

**tool call: Bash**

```bash
files=(docs/data/joy/customization/approaches/ButtonThemes.js docs/data/joy/components/select/SelectFieldDemo.js docs/data/joy/components/select/SelectUsage.js docs/data/joy/components/select/SelectClearable.js docs/data/joy/main-features/automatic-adjustment/ListThemes.js docs/data/base/components/select/UnstyledSelectControlled.js docs/data/base/components/select/UnstyledSelectControlled.tsx docs/data/base/components/select/UnstyledSelectControlled.tsx.preview docs/data/base/components/select/UnstyledSelectObjectValuesForm.js docs/data/base/components/select/UnstyledSelectObjectValuesForm.tsx docs/data/base/components/select/UnstyledSelectObjectValues.js docs/data/base/components/select/UnstyledSelectObjectValues.tsx docs/data/base/components/select/UnstyledSelectObjectValues.tsx.preview)
perl -pi -e 's/onChange=\{(set[A-Za-z]+)\}/onChange={(e, newValue) => $1(newValue)}/g' $files
grep -n "onChange" $files
```

tool result:

```
docs/data/joy/customization/approaches/ButtonThemes.js:563:              onChange={(e, newValue) => setDesign(newValue)}
docs/data/joy/components/select/SelectFieldDemo.js:18:      <Select defaultValue="dog" value={value} onChange={(e, newValue) => setValue(newValue)}>
docs/data/joy/components/select/SelectUsage.js:52:          onChange={(e, newValue) => setValue(newValue)}
docs/data/joy/components/select/SelectClearable.js:15:      onChange={(e, newValue) => setValue(newValue)}
docs/data/joy/main-features/automatic-adjustment/ListThemes.js:118:            onChange={(e, newValue) => setPreset(newValue)}
docs/data/base/components/select/UnstyledSelectControlled.js:168:      <CustomSelect value={value} onChange={(e, newValue) => setValue(newValue)}>
docs/data/base/components/select/UnstyledSelectControlled.tsx:157:      <CustomSelect value={value} onChange={(e, newValue) => setValue(newValue)}>
docs/data/base/components/select/UnstyledSelectControlled.tsx.preview:1:<CustomSelect value={value} onChange={(e, newValue) => setValue(newValue)}>
docs/data/base/components/select/UnstyledSelectObjectValuesForm.js:207:        <CustomSelect value={character} onChange={(e, newValue) => setCharacter(newValue)} name="character">
docs/data/base/components/select/UnstyledSelectObjectValuesForm.js:222:          onChange={(e, newValue) => setCharacter(newValue)}
docs/data/base/components/select/UnstyledSelectObjectValuesForm.tsx:202:        <CustomSelect value={character} onChange={(e, newValue) => setCharacter(newValue)} name="character">
docs/data/base/components/select/UnstyledSelectObjectValuesForm.tsx:217:          onChange={(e, newValue) => setCharacter(newValue)}
docs/data/base/components/select/UnstyledSelectObjectValues.js:190:      <CustomSelect value={character} onChange={(e, newValue) => setCharacter(newValue)}>
docs/data/base/components/select/UnstyledSelectObjectValues.tsx:184:      <CustomSelect value={character} onChange={(e, newValue) => setCharacter(newValue)}>
docs/data/base/components/select/UnstyledSelectObjectValues.tsx.preview:1:<CustomSelect value={character} onChange={(e, newValue) => setCharacter(newValue)}>
```

**assistant:** Checking the markdown docs for `onChange` examples, then running prettier and TypeScript in the container:

**tool call: Bash**

```bash
grep -n "onChange" docs/data/base/components/select/select.md docs/data/joy/components/select/select.md; /work/mui__material-ui-34158/bin/envrun 'npx prettier --write $(git diff --name-only | grep -v "package.json\|yarn.lock") >/dev/null && git diff --stat'
```

tool result:

```
Exit code 2
[error] No parser could be inferred for file: docs/data/base/components/select/UnstyledSelectControlled.tsx.preview
[error] No parser could be inferred for file: docs/data/base/components/select/UnstyledSelectObjectValues.tsx.preview
```

**tool call: Bash**

```bash
git diff --stat; git diff docs/data/base/components/select/UnstyledSelectObjectValuesForm.tsx
```

tool result:

```
 .../components/select/UnstyledSelectControlled.js  |     2 +-
 .../components/select/UnstyledSelectControlled.tsx |     2 +-
 .../select/UnstyledSelectControlled.tsx.preview    |     2 +-
 .../select/UnstyledSelectObjectValues.js           |     5 +-
 .../select/UnstyledSelectObjectValues.tsx          |     5 +-
 .../select/UnstyledSelectObjectValues.tsx.preview  |     2 +-
 .../select/UnstyledSelectObjectValuesForm.js       |     8 +-
 .../select/UnstyledSelectObjectValuesForm.tsx      |     8 +-
 docs/data/joy/components/select/SelectClearable.js |     2 +-
 docs/data/joy/components/select/SelectFieldDemo.js |     6 +-
 docs/data/joy/components/select/SelectUsage.js     |     2 +-
 .../joy/customization/approaches/ButtonThemes.js   |     2 +-
 .../automatic-adjustment/ListThemes.js             |     2 +-
 docs/src/modules/components/JoyUsageDemo.tsx       |     2 +-
 package.json                                       |     9 +-
 .../src/ListboxUnstyled/useControllableReducer.ts  |    56 +-
 .../mui-base/src/ListboxUnstyled/useListbox.ts     |     4 +
 .../src/ListboxUnstyled/useListbox.types.ts        |    19 +-
 .../MultiSelectUnstyled.types.ts                   |     5 +-
 .../src/SelectUnstyled/SelectUnstyled.types.ts     |     5 +-
 packages/mui-base/src/SelectUnstyled/useSelect.ts  |     8 +-
 .../mui-base/src/SelectUnstyled/useSelect.types.ts |    10 +-
 packages/mui-joy/src/Select/SelectProps.ts         |     5 +-
 yarn.lock                                          | 28724 ++++++++++---------
 24 files changed, 15047 insertions(+), 13848 deletions(-)
diff --git a/docs/data/base/components/select/UnstyledSelectObjectValuesForm.tsx b/docs/data/base/components/select/UnstyledSelectObjectValuesForm.tsx
index 7b063743d8..f75634bc65 100644
--- a/docs/data/base/components/select/UnstyledSelectObjectValuesForm.tsx
+++ b/docs/data/base/components/select/UnstyledSelectObjectValuesForm.tsx
@@ -199,7 +199,11 @@ export default function UnstyledSelectObjectValues() {
     <div>
       <Header>Default behavior</Header>
       <form onSubmit={handleSubmit}>
-        <CustomSelect value={character} onChange={setCharacter} name="character">
+        <CustomSelect
+          value={character}
+          onChange={(e, newValue) => setCharacter(newValue)}
+          name="character"
+        >
           {characters.map((c) => (
             <StyledOption key={c.name} value={c}>
               {c.name}
@@ -214,7 +218,7 @@ export default function UnstyledSelectObjectValues() {
       <form onSubmit={handleSubmit}>
         <CustomSelect
           value={character}
-          onChange={setCharacter}
+          onChange={(e, newValue) => setCharacter(newValue)}
           getSerializedValue={getSerializedValue}
           name="character"
         >
```

**tool call: Bash**

```bash
git diff docs/data/base/components/select/UnstyledSelectObjectValues.tsx; cat docs/data/base/components/select/UnstyledSelectObjectValues.tsx.preview
```

tool result:

```
diff --git a/docs/data/base/components/select/UnstyledSelectObjectValues.tsx b/docs/data/base/components/select/UnstyledSelectObjectValues.tsx
index d50392f5bd..18b1091e30 100644
--- a/docs/data/base/components/select/UnstyledSelectObjectValues.tsx
+++ b/docs/data/base/components/select/UnstyledSelectObjectValues.tsx
@@ -181,7 +181,10 @@ export default function UnstyledSelectObjectValues() {
   const [character, setCharacter] = React.useState<Character | null>(characters[0]);
   return (
     <div>
-      <CustomSelect value={character} onChange={setCharacter}>
+      <CustomSelect
+        value={character}
+        onChange={(e, newValue) => setCharacter(newValue)}
+      >
         {characters.map((c) => (
           <StyledOption key={c.name} value={c}>
             {c.name}
<CustomSelect value={character} onChange={(e, newValue) => setCharacter(newValue)}>
  {characters.map((c) => (
    <StyledOption key={c.name} value={c}>
      {c.name}
    </StyledOption>
  ))}
</CustomSelect>

<Paragraph>Selected character:</Paragraph>
<Pre>{JSON.stringify(character, null, 2)}</Pre>
```

**assistant:** Syncing that preview with the formatted source, then type-checking:

**tool call: Bash**

```bash
python3 - <<'EOF'
p='docs/data/base/components/select/UnstyledSelectObjectValues.tsx.preview'
s=open(p).read()
s=s.replace("""<CustomSelect value={character} onChange={(e, newValue) => setCharacter(newValue)}>""","""<CustomSelect
  value={character}
  onChange={(e, newValue) => setCharacter(newValue)}
>""")
open(p,'w').write(s)
EOF
/work/mui__material-ui-34158/bin/envrun 'cd packages/mui-base && npx tsc -p tsconfig.build.json --noEmit 2>&1 | tail -20; cd ../mui-joy && npx tsc -p tsconfig.json --noEmit 2>&1 | tail -20' 
```

tool result:

```
tsconfig.build.json(8,5): error TS5053: Option 'emitDeclarationOnly' cannot be specified with option 'noEmit'.
tsconfig.build.json(9,5): error TS5053: Option 'emitDeclarationOnly' cannot be specified with option 'noEmit'.
../../node_modules/@types/react-dom/test-utils/index.d.ts(6,9): error TS2305: Module '"react"' has no exported member 'act'.
src/Select/Select.spec.tsx(9,43): error TS2345: Argument of type 'FocusEvent<Element, Element> | KeyboardEvent<Element> | MouseEvent<Element, MouseEvent> | null' is not assignable to parameter of type 'never'.
  Type 'null' is not assignable to type 'never'.
src/Select/Select.spec.tsx(15,43): error TS2345: Argument of type 'FocusEvent<Element, Element> | KeyboardEvent<Element> | MouseEvent<Element, MouseEvent> | null' is not assignable to parameter of type 'never'.
src/Select/Select.spec.tsx(22,53): error TS2345: Argument of type 'FocusEvent<Element, Element> | KeyboardEvent<Element> | MouseEvent<Element, MouseEvent> | null' is not assignable to parameter of type 'never'.
src/Select/Select.spec.tsx(34,42): error TS2345: Argument of type 'FocusEvent<Element, Element> | KeyboardEvent<Element> | MouseEvent<Element, MouseEvent> | null' is not assignable to parameter of type 'never'.
```

**assistant:** The Joy `Select.spec.tsx` type test fails. Let me see what it expects:

**tool call: Bash**

```bash
sed -n 1,40p packages/mui-joy/src/Select/Select.spec.tsx; grep -n "onChange" -B2 -A6 packages/mui-base/src/SelectUnstyled/SelectUnstyled.spec.tsx packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.spec.tsx
```

tool result:

```
import * as React from 'react';
import { expectType } from '@mui/types';
import Select from '@mui/joy/Select';

<Select defaultListboxOpen />;
<Select
  value=""
  onChange={(val) => {
    expectType<string | null, typeof val>(val);
  }}
/>;
<Select
  value={2}
  onChange={(val) => {
    expectType<number | null, typeof val>(val);
  }}
/>;
// any object
<Select
  value={{ name: '' }}
  onChange={(val) => {
    expectType<{ name: string } | null, typeof val>(val);
  }}
/>;

interface Value {
  key: string;
  name: { id: string };
}
<Select<Value>
  // @ts-expect-error the provided value type does not match the Value
  value={{ name: '' }}
  onChange={(val) => {
    expectType<Value | null, typeof val>(val);
  }}
/>;
<Select sx={{ bgcolor: (theme) => theme.vars.palette.background.body }} />;
<Select
  componentsProps={{
    button: {
```

**thinking:**

```
The old `(val)` callback signature in Joy's `Select.spec.tsx` type test breaks typecheck with this change, so I'll update those callback signatures to fix `tsc` while leaving the rest of the file untouched.


```

**tool call: Bash**

```bash
perl -pi -e 's/onChange=\{\(val\) => \{/onChange={(e, val) => {/' packages/mui-joy/src/Select/Select.spec.tsx
/work/mui__material-ui-34158/bin/envrun 'cd packages/mui-base && npx tsc -p tsconfig.json --noEmit 2>&1 | grep -v test-utils | tail -20; cd ../mui-joy && npx tsc -p tsconfig.json --noEmit 2>&1 | grep -v test-utils| tail; cd ../../docs && npx tsc -p tsconfig.json --noEmit 2>&1 | grep -v test-utils | tail'
```

tool result:

```
Command did not complete within its 120s timeout and was moved to the background (ID: b7tzxctro). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/472f68fa-22e9-4d0d-9fa7-da8ca79da0bb/tasks/b7tzxctro.output. You will be notified when it completes. To check interim output, use Read on that file path.
```

**assistant:** While that runs, I'll write a reproduction test that checks the event is passed:

**tool call: Bash**

```bash
cat > packages/mui-base/src/SelectUnstyled/repro.test.tsx <<'EOF'
import * as React from 'react';
import { expect } from 'chai';
import { spy } from 'sinon';
import { createRenderer, fireEvent } from 'test/utils';
import SelectUnstyled from '@mui/base/SelectUnstyled';
import MultiSelectUnstyled from '@mui/base/MultiSelectUnstyled';
import OptionUnstyled from '@mui/base/OptionUnstyled';

describe('repro onChange event', () => {
  const { render } = createRenderer();

  it('single: click', () => {
    const handleChange = spy();
    const { getAllByRole } = render(
      <SelectUnstyled defaultListboxOpen onChange={handleChange} defaultValue={1}>
        <OptionUnstyled value={1}>1</OptionUnstyled>
        <OptionUnstyled value={2}>2</OptionUnstyled>
      </SelectUnstyled>,
    );
    fireEvent.click(getAllByRole('option')[1]);
    expect(handleChange.callCount).to.equal(1);
    expect(handleChange.args[0][0]).to.haveOwnProperty('type', 'click');
    expect(handleChange.args[0][0].target).to.equal(getAllByRole('option')[1]);
    expect(handleChange.args[0][1]).to.equal(2);
  });

  it('single: keyboard', () => {
    const handleChange = spy();
    const { getByRole } = render(
      <SelectUnstyled defaultListboxOpen onChange={handleChange} defaultValue={1}>
        <OptionUnstyled value={1}>1</OptionUnstyled>
        <OptionUnstyled value={2}>2</OptionUnstyled>
      </SelectUnstyled>,
    );
    const listbox = getByRole('listbox');
    fireEvent.keyDown(listbox, { key: 'ArrowDown' });
    fireEvent.keyDown(listbox, { key: 'Enter' });
    expect(handleChange.callCount).to.equal(1);
    expect(handleChange.args[0][0]).to.haveOwnProperty('type', 'keydown');
    expect(handleChange.args[0][1]).to.equal(2);
  });

  it('multi: click', () => {
    const handleChange = spy();
    const { getAllByRole } = render(
      <MultiSelectUnstyled defaultListboxOpen onChange={handleChange} defaultValue={[1]}>
        <OptionUnstyled value={1}>1</OptionUnstyled>
        <OptionUnstyled value={2}>2</OptionUnstyled>
      </MultiSelectUnstyled>,
    );
    fireEvent.click(getAllByRole('option')[1]);
    expect(handleChange.callCount).to.equal(1);
    expect(handleChange.args[0][0]).to.haveOwnProperty('type', 'click');
    expect(handleChange.args[0][1]).to.deep.equal([1, 2]);
  });
});
EOF
git stash push -q -- packages/mui-base/src packages/mui-joy/src docs && /work/mui__material-ui-34158/bin/envrun 'yarn cross-env NODE_ENV=test mocha packages/mui-base/src/SelectUnstyled/repro.test.tsx 2>&1 | tail -25'; git stash pop -q && git diff --stat | tail -1
```

tool result:

```
  0 passing (607ms)
  3 failing

  1) repro onChange event
       single: click:
     AssertionError: expected 2 to have own property 'type'
      at Context.<anonymous> (packages/mui-base/src/SelectUnstyled/repro.test.tsx:22:40)
      at processImmediate (node:internal/timers:466:21)

  2) repro onChange event
       single: keyboard:
     AssertionError: expected 2 to have own property 'type'
      at Context.<anonymous> (packages/mui-base/src/SelectUnstyled/repro.test.tsx:39:40)
      at processImmediate (node:internal/timers:466:21)

  3) repro onChange event
       multi: click:
     AssertionError: expected [ 1, 2 ] to have own property 'type'
      at Context.<anonymous> (packages/mui-base/src/SelectUnstyled/repro.test.tsx:53:40)
      at processImmediate (node:internal/timers:466:21)



error Command failed with exit code 3.
info Visit https://yarnpkg.com/en/docs/cli/run for documentation about this command.

 25 files changed, 15054 insertions(+), 13852 deletions(-)
```

**assistant:** With the original code (my changes stashed), the bug reproduces: the value arrives as the first argument. Now with the fix applied:

**tool call: Bash**

```bash
/work/mui__material-ui-34158/bin/envrun 'yarn cross-env NODE_ENV=test mocha packages/mui-base/src/SelectUnstyled/repro.test.tsx 2>&1 | tail -12'
```

tool result:

```
  [36m</div>[39m
[36m</body>[39m
      at Object.getElementError (node_modules/@testing-library/dom/dist/config.js:40:19)
      at /testbed/node_modules/@testing-library/dom/dist/query-helpers.js:90:38
      at getAllByRole (node_modules/@testing-library/dom/dist/query-helpers.js:130:15)
      at Context.<anonymous> (packages/mui-base/src/SelectUnstyled/repro.test.tsx:23:53)
      at processImmediate (node:internal/timers:466:21)



error Command failed with exit code 1.
info Visit https://yarnpkg.com/en/docs/cli/run for documentation about this command.
```

**assistant:** The first test failed for a reason in my test: the listbox closes after the click, so re-querying the options fails. I'll keep a reference to the option before clicking:

**tool call: Bash**

```bash
python3 - <<'EOF'
p='packages/mui-base/src/SelectUnstyled/repro.test.tsx'
s=open(p).read()
s=s.replace("""    fireEvent.click(getAllByRole('option')[1]);
    expect(handleChange.callCount).to.equal(1);
    expect(handleChange.args[0][0]).to.haveOwnProperty('type', 'click');
    expect(handleChange.args[0][0].target).to.equal(getAllByRole('option')[1]);""","""    const option = getAllByRole('option')[1];
    fireEvent.click(option);
    expect(handleChange.callCount).to.equal(1);
    expect(handleChange.args[0][0]).to.haveOwnProperty('type', 'click');
    expect(handleChange.args[0][0].target).to.equal(option);""")
open(p,'w').write(s)
EOF
/work/mui__material-ui-34158/bin/envrun 'yarn cross-env NODE_ENV=test mocha packages/mui-base/src/SelectUnstyled/repro.test.tsx 2>&1 | tail -12'
```

tool result:

```
$ /testbed/node_modules/.bin/cross-env NODE_ENV=test mocha packages/mui-base/src/SelectUnstyled/repro.test.tsx
Browserslist: caniuse-lite is outdated. Please run:
  npx update-browserslist-db@latest
  Why you should do it regularly: https://github.com/browserslist/update-db#readme
including inaccessible elements by default


  ...

  3 passing (560ms)

Done in 3.44s.
```

**assistant:** The reproduction passes now. Next I'll run the existing tests for Listbox, Select, MultiSelect, Menu and Joy Select, and check the typecheck output:

**tool call: Bash**

```bash
/work/mui__material-ui-34158/bin/envrun "yarn cross-env NODE_ENV=test mocha 'packages/mui-base/src/{ListboxUnstyled,SelectUnstyled,MultiSelectUnstyled,MenuUnstyled,MenuItemUnstyled,OptionUnstyled}/**/*.test.{ts,tsx}' 'packages/mui-joy/src/{Select,Menu,MenuItem,Option}/**/*.test.tsx' 2>&1 | tail -40"; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/472f68fa-22e9-4d0d-9fa7-da8ca79da0bb/tasks/b7tzxctro.output
```

tool result:

```
    at TestComponent (/testbed/packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.test.tsx:312:39)
    at Wrapper (/testbed/test/utils/createRenderer.tsx:399:7)

Consider adding an error boundary to your tree to customize error handling behavior.
Visit https://reactjs.org/link/error-boundaries to learn more about error boundaries.

Stack:
    at logCapturedError (/testbed/node_modules/react-dom/cjs/react-dom.development.js:18687:23)
    at update.callback (/testbed/node_modules/react-dom/cjs/react-dom.development.js:18720:5)
    at callCallback (/testbed/node_modules/react-dom/cjs/react-dom.development.js:13923:12)
    at commitUpdateQueue (/testbed/node_modules/react-dom/cjs/react-dom.development.js:13944:9)
    at commitLayoutEffectOnFiber (/testbed/node_modules/react-dom/cjs/react-dom.development.js:23391:13)
    at commitLayoutMountEffects_complete (/testbed/node_modules/react-dom/cjs/react-dom.development.js:24688:9)
    at commitLayoutEffects_begin (/testbed/node_modules/react-dom/cjs/react-dom.development.js:24674:7)
    at commitLayoutEffects (/testbed/node_modules/react-dom/cjs/react-dom.development.js:24612:3)
    at commitRootImpl (/testbed/node_modules/react-dom/cjs/react-dom.development.js:26823:5)
    at commitRoot (/testbed/node_modules/react-dom/cjs/react-dom.development.js:26682:5)
    at finishConcurrentRender (/testbed/node_modules/react-dom/cjs/react-dom.development.js:25892:9)
    at performConcurrentWorkOnRoot (/testbed/node_modules/react-dom/cjs/react-dom.development.js:25809:7)
    at flushActQueue (/testbed/node_modules/react/cjs/react.development.js:2667:24)
    at act (/testbed/node_modules/react/cjs/react.development.js:2582:11)
    at /testbed/node_modules/@testing-library/react/dist/act-compat.js:63:25
    at callback (/testbed/test/utils/createRenderer.tsx:719:39)
    at traceSync (/testbed/test/utils/createRenderer.tsx:29:10)
    at act (/testbed/test/utils/createRenderer.tsx:719:10)
    at Context.<anonymous> (/testbed/packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.test.tsx:295:8)
    at processImmediate (node:internal/timers:466:21)
  

  5) Joy <Select />
       prop: onChange
         should get selected value from the 1st argument:
     AssertionError: expected SyntheticBaseEvent{ …(32) } to equal '1'
      at Context.<anonymous> (packages/mui-joy/src/Select/Select.test.tsx:130:45)
      at processImmediate (node:internal/timers:466:21)



error Command failed with exit code 5.
info Visit https://yarnpkg.com/en/docs/cli/run for documentation about this command.

src/ListboxUnstyled/useControllableReducer.test.tsx(103,40): error TS2345: Argument of type '{ type: ActionTypes.setValue; value: string; }' is not assignable to parameter of type 'ListboxAction<string>'.
  Property 'event' is missing in type '{ type: ActionTypes.setValue; value: string; }' but required in type 'SetValueAction<string>'.
src/ListboxUnstyled/useControllableReducer.test.tsx(138,40): error TS2345: Argument of type '{ type: ActionTypes.setHighlight; highlight: string; }' is not assignable to parameter of type 'ListboxAction<string>'.
  Property 'event' is missing in type '{ type: ActionTypes.setHighlight; highlight: string; }' but required in type 'SetHighlightAction<string>'.
src/MultiSelectUnstyled/MultiSelectUnstyled.test.tsx(246,46): error TS2769: No overload matches this call.
  Overload 1 of 2, '(props: { component: ElementType<any>; } & MultiSelectUnstyledOwnProps<number> & Omit<any, keyof MultiSelectUnstyledOwnProps<TValue>>): Element | null', gave the following error.
    Type '(newValue: number[]) => void' is not assignable to type '(e: FocusEvent<Element, Element> | KeyboardEvent<Element> | MouseEvent<Element, MouseEvent> | null, value: number[]) => void'.
      Types of parameters 'newValue' and 'e' are incompatible.
        Type 'FocusEvent<Element, Element> | KeyboardEvent<Element> | MouseEvent<Element, MouseEvent> | null' is not assignable to type 'number[]'.
          Type 'null' is not assignable to type 'number[]'.
  Overload 2 of 2, '(props: DefaultComponentProps<MultiSelectUnstyledTypeMap<number, {}, "button">>): Element | null', gave the following error.
    Type '(newValue: number[]) => void' is not assignable to type '(e: FocusEvent<Element, Element> | KeyboardEvent<Element> | MouseEvent<Element, MouseEvent> | null, value: number[]) => void'.
src/MultiSelectUnstyled/MultiSelectUnstyled.test.tsx(273,13): error TS2769: No overload matches this call.
  Overload 1 of 2, '(props: { component: ElementType<any>; } & MultiSelectUnstyledOwnProps<number> & Omit<any, keyof MultiSelectUnstyledOwnProps<TValue>>): Element | null', gave the following error.
    Type 'Dispatch<SetStateAction<number[]>>' is not assignable to type '(e: FocusEvent<Element, Element> | KeyboardEvent<Element> | MouseEvent<Element, MouseEvent> | null, value: number[]) => void'.
      Types of parameters 'value' and 'e' are incompatible.
        Type 'FocusEvent<Element, Element> | KeyboardEvent<Element> | MouseEvent<Element, MouseEvent> | null' is not assignable to type 'SetStateAction<number[]>'.
          Type 'null' is not assignable to type 'SetStateAction<number[]>'.
  Overload 2 of 2, '(props: DefaultComponentProps<MultiSelectUnstyledTypeMap<number, {}, "button">>): Element | null', gave the following error.
    Type 'Dispatch<SetStateAction<number[]>>' is not assignable to type '(e: FocusEvent<Element, Element> | KeyboardEvent<Element> | MouseEvent<Element, MouseEvent> | null, value: number[]) => void'.
../packages/typescript-to-proptypes/src/injector.ts(128,35): error TS2345: Argument of type 'object | null | undefined' is not assignable to parameter of type 'Node | null | undefined'.
  Type 'object' is not assignable to type 'Node | null | undefined'.
../packages/typescript-to-proptypes/src/injector.ts(380,48): error TS2345: Argument of type 'object | null | undefined' is not assignable to parameter of type 'Node | null | undefined'.
../packages/typescript-to-prop
[... 364 more characters not shown]
```

**thinking:**

```
Typecheck shows only expected errors in test files still using the old `onChange(value)` signature, with docs typecheck clean and other errors unrelated. Now pulling up the full list of runtime test failures.


```

**tool call: Bash**

```bash
/work/mui__material-ui-34158/bin/envrun "yarn cross-env NODE_ENV=test mocha 'packages/mui-base/src/{ListboxUnstyled,SelectUnstyled,MultiSelectUnstyled,MenuUnstyled,MenuItemUnstyled,OptionUnstyled}/**/*.test.{ts,tsx}' 'packages/mui-joy/src/{Select,Menu,MenuItem,Option}/**/*.test.tsx' 2>&1 | grep -E 'passing|failing|^  [0-9]+\) |^       [a-zA-Z]|AssertionError|TypeError' | head -40"
```

tool result:

```
  195 passing (9s)
  5 failing
  1) useControllableReducer
       dispatch
     AssertionError: expected undefined to equal 'b'
  2) useControllableReducer
       dispatch
     AssertionError: expected undefined to equal 'b'
  3) MultiSelectUnstyled
       sets a value correctly when interacted by a user and external code:
     TypeError: value.includes is not a function
  4) MultiSelectUnstyled
       sets a value correctly when interacted by a user and external code:
  Error: Uncaught [TypeError: value.includes is not a function]
    at processImmediate (node:internal/timers:466:21) TypeError: value.includes is not a function
  Error: Uncaught [TypeError: value.includes is not a function]
    at processImmediate (node:internal/timers:466:21) TypeError: value.includes is not a function
  5) Joy <Select />
       prop: onChange
     AssertionError: expected SyntheticBaseEvent{ …(32) } to equal '1'
```

**thinking:**

```
The 195 other tests pass; the 5 failures are existing tests that assert the old signature, which the issue intentionally changes. Since you've said tests are handled, I'll leave all test files untouched—reverting my `Select.spec.tsx` edit and deleting the reproduction test.


```

**tool call: Bash**

```bash
git checkout packages/mui-joy/src/Select/Select.spec.tsx && rm packages/mui-base/src/SelectUnstyled/repro.test.tsx && git status --short
```

tool result:

```
Updated 1 path from the index
 M docs/data/base/components/select/UnstyledSelectControlled.js
 M docs/data/base/components/select/UnstyledSelectControlled.tsx
 M docs/data/base/components/select/UnstyledSelectControlled.tsx.preview
 M docs/data/base/components/select/UnstyledSelectObjectValues.js
 M docs/data/base/components/select/UnstyledSelectObjectValues.tsx
 M docs/data/base/components/select/UnstyledSelectObjectValues.tsx.preview
 M docs/data/base/components/select/UnstyledSelectObjectValuesForm.js
 M docs/data/base/components/select/UnstyledSelectObjectValuesForm.tsx
 M docs/data/joy/components/select/SelectClearable.js
 M docs/data/joy/components/select/SelectFieldDemo.js
 M docs/data/joy/components/select/SelectUsage.js
 M docs/data/joy/customization/approaches/ButtonThemes.js
 M docs/data/joy/main-features/automatic-adjustment/ListThemes.js
 M docs/src/modules/components/JoyUsageDemo.tsx
 M package.json
 M packages/mui-base/src/ListboxUnstyled/useControllableReducer.ts
 M packages/mui-base/src/ListboxUnstyled/useListbox.ts
 M packages/mui-base/src/ListboxUnstyled/useListbox.types.ts
 M packages/mui-base/src/MultiSelectUnstyled/MultiSelectUnstyled.types.ts
 M packages/mui-base/src/SelectUnstyled/SelectUnstyled.types.ts
 M packages/mui-base/src/SelectUnstyled/useSelect.ts
 M packages/mui-base/src/SelectUnstyled/useSelect.types.ts
 M packages/mui-joy/src/Select/SelectProps.ts
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
```

**assistant:** `SelectUnstyled`, `MultiSelectUnstyled` and the Joy UI `Select` now call `onChange(event, value)`: the event that caused the change comes first and the new value second. This is a breaking change for anyone using these components.

**How it works** (in `packages/mui-base/src/ListboxUnstyled/`):
- Every listbox action now carries an `event`. Clicks, hovers, key presses, typing to jump to an option, and blur pass the real event. Changes made from code (`setSelectedValue`, `setHighlightedValue`, and updates when the option list changes) pass `null`.
- `useControllableReducer.ts` keeps the last action it handled. When the selected value changes, it calls `onChange(lastAction.event, newValue)`. The event type is `React.MouseEvent | React.KeyboardEvent | React.FocusEvent | null`.
- I gave `onHighlightChange` the same `(event, option)` signature so the two stay consistent. It's only used inside the listbox hook, not by any public component prop.

**Types and docs:** the `onChange` types in `useSelect`, `SelectUnstyled`, `MultiSelectUnstyled` and Joy `SelectProps` are updated. Demos that passed a state setter straight in (`onChange={setValue}`) would have broken, so they now use `(e, newValue) => setValue(newValue)`. That covers the Base and Joy select demos, their `.tsx.preview` files, `ButtonThemes.js`, `ListThemes.js` and `JoyUsageDemo.tsx`.

**Checks:**
- **Reproduction:** I wrote a test covering a click and a keyboard selection on `SelectUnstyled` and a click on `MultiSelectUnstyled`. Before the fix all 3 cases failed because the value was the first argument; after it, all 3 pass. I deleted the test afterwards.
- **Existing tests:** I ran the tests for Listbox, Select, MultiSelect, Menu, MenuItem and Option in Base, and Select, Menu, MenuItem and Option in Joy. 195 pass and 5 fail. All 5 failures are tests that still expect the old signature:
  - `useControllableReducer.test.tsx` (2 failures) reads the value from the first argument.
  - `MultiSelectUnstyled.test.tsx` (2 failures from one test) passes `onChange={setValue}` directly, so the event gets stored as the value.
  - Joy `Select.test.tsx`, "should get selected value from the 1st argument" (1 failure).
- **Typecheck:** In `mui-base` and `mui-joy` the only errors come from those same out-of-date test files, plus the Joy type test `Select.spec.tsx`, which still uses `onChange={(val) => …}`. The remaining errors are pre-existing ones in `packages/typescript-to-proptypes` and an `act` export error from `@types/react-dom`. The docs typecheck shows nothing beyond that same `act` error.

Since you said the tests are handled, I didn't change any test files. These failures should go away once the updated tests are in. `package.json`, `yarn.lock`, `Dockerfile` and `custom-reporter.js` were already modified or untracked before I started, and I didn't touch them.

_session end: success, turns 31, is_error False_

## Container commands (task container, no network; broker log)

- `rc=2` 20.0 s: npx prettier --write $(git diff --name-only | grep -v "package.json\|yarn.lock") >/dev/null && git diff --stat
- `rc=0` 42.96 s: cd packages/mui-base && npx tsc -p tsconfig.build.json --noEmit 2>&1 | tail -20; cd ../mui-joy && npx tsc -p tsconfig.json --noEmit 2>&1 | tail -20
- `rc=0` 12.43 s: yarn cross-env NODE_ENV=test mocha packages/mui-base/src/SelectUnstyled/repro.test.tsx 2>&1 | tail -25
- `rc=0` 4.64 s: yarn cross-env NODE_ENV=test mocha packages/mui-base/src/SelectUnstyled/repro.test.tsx 2>&1 | tail -12
- `rc=0` 4.31 s: yarn cross-env NODE_ENV=test mocha packages/mui-base/src/SelectUnstyled/repro.test.tsx 2>&1 | tail -12
- `rc=0` 163.36 s: cd packages/mui-base && npx tsc -p tsconfig.json --noEmit 2>&1 | grep -v test-utils | tail -20; cd ../mui-joy && npx tsc -p tsconfig.json --noEmit 2>&1 | grep -v test-utils| tail; cd ../../docs && npx tsc -p tsconfig.json --noEmit 2>&1 | grep -v test-utils | tail
- `rc=0` 15.77 s: yarn cross-env NODE_ENV=test mocha 'packages/mui-base/src/{ListboxUnstyled,SelectUnstyled,MultiSelectUnstyled,MenuUnstyled,MenuItemUnstyled,OptionUnstyled}/**/*.test.{ts,tsx}' 'packages/mui-joy/src/{Select,Menu,MenuItem,Option}/**/*.test.tsx' 2>&1 | tail -40
- `rc=0` 14.23 s: yarn cross-env NODE_ENV=test mocha 'packages/mui-base/src/{ListboxUnstyled,SelectUnstyled,MultiSelectUnstyled,MenuUnstyled,MenuItemUnstyled,OptionUnstyled}/**/*.test.{ts,tsx}' 'packages/mui-joy/src/{Select,Menu,MenuItem,Option}/**/*.test.tsx' 2>&1 | grep -E 'passing|failing|^  [0-9]+\) |^       [a-zA-Z]|AssertionError|TypeError' | head -40
