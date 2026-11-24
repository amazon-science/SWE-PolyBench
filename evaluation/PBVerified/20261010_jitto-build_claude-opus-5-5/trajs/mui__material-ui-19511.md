# Instance: mui__material-ui-19511

- Final resolved (evaluator, logs/mui__material-ui-19511_result.json): False
- Run state: DONE
- One attempt. Duration 959.9 s, turns 19, actor cost $0.3854963999999999, container commands 8
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/mui__material-ui-19511/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-19511/repo. Consider the following issue description:

<issue_description>
[Autocomplete] Input cleared unexpectedly with freeSolo, autoHighlight and autoSelect
<!-- Provide a general summary of the issue in the Title above -->

An `Autocomplete` with `freeSolo`, `autoHighlight` and `autoSelect` props set to `true` clears its input when it loses focus and the input value is not an exact or partial match for any of the  provided options.

<!--
  Thank you very much for contributing to Material-UI by creating an issue! ❤️
  To avoid duplicate issues we ask you to check off the following list.
-->

<!-- Checked checkbox should look like this: [x] -->

- [x] The issue is present in the latest release.
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Current Behavior 😯

<!-- Describe what happens instead of the expected behavior. -->
See above. This only occurs once; going back and entering the same free string causes it to persist until the input is cleared again (either manually or by clicking the clear button), which seems to put it back into the problematic state. Note that the string must contain letters that appear in any of the option labels for this to occur.

## Expected Behavior 🤔

The input value should not be cleared on blur as long as `freeSolo` is `true`.

## Steps to Reproduce 🕹

<!--
  Provide a link to a live example (you can use codesandbox.io) and an unambiguous set of steps to reproduce this bug.
  Include code to reproduce, if relevant (which it most likely is).

  This codesandbox.io template _may_ be a good starting point:
  https://codesandbox.io/s/github/mui-org/material-ui/tree/master/examples/create-react-app

  If you're using typescript a better starting point would be
  https://codesandbox.io/s/github/mui-org/material-ui/tree/master/examples/create-react-app-with-typescript

  If YOU DO NOT take time to provide a codesandbox.io reproduction, should the COMMUNITY take time to help you?
-->

Codesandbox: https://codesandbox.io/s/create-react-app-76xd5

Steps:

1. Enter a string into the Autocomplete input which is *not a substring of any of the option labels, but contains letters that appear in at least one of them* (e.g. "aaa").
2. Tab to the next field.
3. Tab back to the Autocomplete and enter the same string.
4. Tab to the next field.

To reset, click the clear button or backspace over the input field.

## Context 🔦

<!--
  What are you trying to accomplish? How has this issue affected you?
  Providing context helps us come up with a solution that is most useful in the real world.
-->
I am trying to build a simple autocomplete field which permits free values but optimizes entry of provided options first (hence this combination of props).

## Your Environment 🌎

<!--
  Include as many relevant details about the environment with which you experienced the bug.
  If you encounter issues with typescript please include version and tsconfig.
-->

| Tech        | Version |
| ----------- | ------- |
| Material-UI | latest |
| Material-UI Lab | 4.0.0-alpha.34 |
| React       | latest |
| Browser     | Firefox 70.0.1, Chrome 78.0.3904.108 |



</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-19511/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-19511/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-19511/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-19511/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/mui__material-ui-19511/repo/packages/material-ui-lab/src/useAutocomplete; grep -n "highlightedIndexRef\|autoSelect\|handleBlur\|changeHighlightedIndex = \|syncHighlightedIndex\|filteredOptions\b" useAutocomplete.js | head -80
```

tool result:

```
84:    autoSelect = false,
132:  const highlightedIndexRef = React.useRef(defaultHighlighted);
136:    highlightedIndexRef.current = index;
256:  const filteredOptions = popupOpen
275:  popupOpen = freeSolo && filteredOptions.length === 0 ? false : popupOpen;
303:        (direction === 'next' && nextFocus === filteredOptions.length) ||
325:  const changeHighlightedIndex = (diff, direction) => {
331:      const maxIndex = filteredOptions.length - 1;
345:      const newIndex = highlightedIndexRef.current + diff;
352:        if ((disableListWrap && highlightedIndexRef.current !== -1) || Math.abs(diff) > 1) {
382:        const option = getOptionLabel(filteredOptions[nextIndex]);
591:        if (highlightedIndexRef.current !== -1 && popupOpen) {
594:          selectNewValue(event, filteredOptions[highlightedIndexRef.current]);
650:  const handleBlur = event => {
659:    if (autoSelect && selectedIndexRef.current !== -1) {
660:      selectNewValue(event, filteredOptions[selectedIndexRef.current]);
661:    } else if (autoSelect && freeSolo && inputValue !== '') {
707:    selectNewValue(event, filteredOptions[index]);
734:    setHighlightedIndex(highlightedIndexRef.current);
777:  let groupedOptions = filteredOptions;
785:    filteredOptions.forEach(option => {
825:      onBlur: handleBlur,
913:  autoSelect: PropTypes.bool,
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-19511/repo/packages/material-ui-lab/src/useAutocomplete; sed -n 120,160p useAutocomplete.js; sed -n 250,460p useAutocomplete.js; sed -n 640,680p useAutocomplete.js
```

tool result:

```
    // We can't use it server-side.
    setDefaultId(`mui-autocomplete-${Math.round(Math.random() * 1e5)}`);
  }, []);

  const ignoreFocus = React.useRef(false);
  const firstFocus = React.useRef(true);
  const inputRef = React.useRef(null);
  const listboxRef = React.useRef(null);
  const [anchorEl, setAnchorEl] = React.useState(null);

  const [focusedTag, setFocusedTag] = React.useState(-1);
  const defaultHighlighted = autoHighlight ? 0 : -1;
  const highlightedIndexRef = React.useRef(defaultHighlighted);
  const selectedIndexRef = React.useRef(-1);

  function setHighlightedIndex(index, mouse = false) {
    highlightedIndexRef.current = index;
    // does the index exist?
    if (index === -1) {
      inputRef.current.removeAttribute('aria-activedescendant');
    } else {
      inputRef.current.setAttribute('aria-activedescendant', `${id}-option-${index}`);
    }

    if (!listboxRef.current) {
      return;
    }

    const prev = listboxRef.current.querySelector('[data-focus]');
    if (prev) {
      prev.removeAttribute('data-focus');
    }

    const listboxNode = listboxRef.current.parentElement.querySelector('[role="listbox"]');

    // "No results"
    if (!listboxNode) {
      return;
    }

    if (index === -1) {

  const inputValueIsSelectedValue =
    !multiple && value != null && inputValue === getOptionLabel(value);

  let popupOpen = open;

  const filteredOptions = popupOpen
    ? filterOptions(
        options.filter(option => {
          if (
            filterSelectedOptions &&
            (multiple ? value : [value]).some(
              value2 => value2 !== null && getOptionSelected(option, value2),
            )
          ) {
            return false;
          }
          return true;
        }),
        // we use the empty string to manipulate `filterOptions` to not filter any options
        // i.e. the filter predicate always returns true
        { inputValue: inputValueIsSelectedValue ? '' : inputValue },
      )
    : [];

  popupOpen = freeSolo && filteredOptions.length === 0 ? false : popupOpen;

  const focusTag = useEventCallback(tagToFocus => {
    if (tagToFocus === -1) {
      inputRef.current.focus();
    } else {
      anchorEl.querySelector(`[data-tag-index="${tagToFocus}"]`).focus();
    }
  });

  // Ensure the focusedTag is never inconsistent
  React.useEffect(() => {
    if (multiple && focusedTag > value.length - 1) {
      setFocusedTag(-1);
      focusTag(-1);
    }
  }, [value, multiple, focusedTag, focusTag]);

  function validOptionIndex(index, direction) {
    if (!listboxRef.current || index === -1) {
      return -1;
    }

    let nextFocus = index;

    while (true) {
      // Out of range
      if (
        (direction === 'next' && nextFocus === filteredOptions.length) ||
        (direction === 'previous' && nextFocus === -1)
      ) {
        return -1;
      }

      const option = listboxRef.current.querySelector(`[data-option-index="${nextFocus}"]`);

      // Same logic as MenuList.js
      if (
        option &&
        (!option.hasAttribute('tabindex') ||
          option.disabled ||
          option.getAttribute('aria-disabled') === 'true')
      ) {
        nextFocus += direction === 'next' ? 1 : -1;
      } else {
        return nextFocus;
      }
    }
  }

  const changeHighlightedIndex = (diff, direction) => {
    if (!popupOpen) {
      return;
    }

    const getNextIndex = () => {
      const maxIndex = filteredOptions.length - 1;

      if (diff === 'reset') {
        return defaultHighlighted;
      }

      if (diff === 'start') {
        return 0;
      }

      if (diff === 'end') {
        return maxIndex;
      }

      const newIndex = highlightedIndexRef.current + diff;

      if (newIndex < 0) {
        if (newIndex === -1 && includeInputInList) {
          return -1;
        }

        if ((disableListWrap && highlightedIndexRef.current !== -1) || Math.abs(diff) > 1) {
          return 0;
        }

        return maxIndex;
      }

      if (newIndex > maxIndex) {
        if (newIndex === maxIndex + 1 && includeInputInList) {
          return -1;
        }

        if (disableListWrap || Math.abs(diff) > 1) {
          return maxIndex;
        }

        return 0;
      }

      return newIndex;
    };

    const nextIndex = validOptionIndex(getNextIndex(), direction);
    setHighlightedIndex(nextIndex);
    selectedIndexRef.current = nextIndex;

    if (autoComplete && diff !== 'reset') {
      if (nextIndex === -1) {
        inputRef.current.value = inputValue;
      } else {
        const option = getOptionLabel(filteredOptions[nextIndex]);
        inputRef.current.value = option;

        // The portion of the selected suggestion that has not been typed by the user,
        // a completion string, appears inline after the input cursor in the textbox.
        const index = option.toLowerCase().indexOf(inputValue.toLowerCase());
        if (index === 0 && inputValue.length > 0) {
          inputRef.current.setSelectionRange(inputValue.length, option.length);
        }
      }
    }
  };

  React.useEffect(() => {
    changeHighlightedIndex('reset', 'next');
  }, [inputValue]); // eslint-disable-line react-hooks/exhaustive-deps

  const handleOpen = event => {
    if (open) {
      return;
    }

    if (onOpen) {
      onOpen(event);
    }
    if (!isOpenControlled) {
      setOpenState(true);
    }
  };

  const handleClose = event => {
    if (!open) {
      return;
    }

    if (onClose) {
      onClose(event);
    }
    if (!isOpenControlled) {
      setOpenState(false);
    }
  };

  const handleValue = (event, newValue) => {
    if (value === newValue) {
      return;
    }

    if (onChange) {
      onChange(event, newValue);
    }

    setValue(newValue);
  };

  const selectNewValue = (event, newValue, origin = 'option') => {
    if (multiple) {
      const item = newValue;
      newValue = Array.isArray(value) ? [...value] : [];

      const itemIndex = findIndex(newValue, valueItem => ge
[... 1287 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-19511/repo/packages/material-ui-lab/src; grep -n "autoSelect" -A30 Autocomplete/Autocomplete.test.js | head -120
```

tool result:

```
52:  describe('prop: autoSelect', () => {
53:    it('should add new value when autoSelect & multiple on blur', () => {
54-      const handleChange = spy();
55-      const options = ['one', 'two'];
56-      render(
57-        <Autocomplete
58:          autoSelect
59-          multiple
60-          value={[options[0]]}
61-          options={options}
62-          onChange={handleChange}
63-          renderInput={params => <TextField autoFocus {...params} />}
64-        />,
65-      );
66-      fireEvent.change(document.activeElement, { target: { value: 't' } });
67-      fireEvent.keyDown(document.activeElement, { key: 'ArrowDown' });
68-      document.activeElement.blur();
69-      expect(handleChange.callCount).to.equal(1);
70-      expect(handleChange.args[0][1]).to.deep.equal(options);
71-    });
72-
73:    it('should add new value when autoSelect & multiple & freeSolo on blur', () => {
74-      const handleChange = spy();
75-      render(
76-        <Autocomplete
77:          autoSelect
78-          freeSolo
79-          multiple
80-          onChange={handleChange}
81-          renderInput={params => <TextField autoFocus {...params} />}
82-        />,
83-      );
84-      fireEvent.change(document.activeElement, { target: { value: 'a' } });
85-      document.activeElement.blur();
86-      expect(handleChange.callCount).to.equal(1);
87-      expect(handleChange.args[0][1]).to.deep.equal(['a']);
88-    });
89-  });
90-
91-  describe('prop: multiple', () => {
92-    it('should not crash', () => {
93-      const { getByRole } = render(
94-        <Autocomplete renderInput={params => <TextField {...params} />} multiple />,
95-      );
96-      const input = getByRole('textbox');
97-      input.focus();
98-      document.activeElement.blur();
99-      input.focus();
100-    });
101-
102-    it('should remove the last option', () => {
103-      const handleChange = spy();
104-      const options = ['one', 'two'];
105-      const { container } = render(
106-        <Autocomplete
107-          defaultValue={options}
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-19511/repo/packages/material-ui-lab/src; sed -n 1,20p Autocomplete/Autocomplete.test.js; cat > Autocomplete/Repro.test.js <<'EOF'
import React from 'react';
import { expect } from 'chai';
import { createClientRender, fireEvent } from 'test/utils/createClientRender';
import { spy } from 'sinon';
import TextField from '@material-ui/core/TextField';
import Autocomplete from './Autocomplete';

describe('repro', () => {
  const render = createClientRender({ strict: true });
  it('keeps freeSolo value on blur with autoHighlight', () => {
    const handleChange = spy();
    const { getByRole } = render(
      <Autocomplete
        freeSolo autoSelect autoHighlight
        options={['one', 'two']}
        onChange={handleChange}
        renderInput={params => <TextField autoFocus {...params} />}
      />,
    );
    fireEvent.change(document.activeElement, { target: { value: 'oo' } });
    document.activeElement.blur();
    expect(handleChange.callCount).to.equal(1);
    expect(handleChange.args[0][1]).to.equal('oo');
    expect(getByRole('textbox').value).to.equal('oo');
  });
});
EOF
```

tool result:

```
import React from 'react';
import { expect } from 'chai';
import { createMount, getClasses } from '@material-ui/core/test-utils';
import describeConformance from '@material-ui/core/test-utils/describeConformance';
import consoleErrorMock from 'test/utils/consoleErrorMock';
import { spy } from 'sinon';
import { createClientRender, fireEvent } from 'test/utils/createClientRender';
import Autocomplete from './Autocomplete';
import TextField from '@material-ui/core/TextField';

describe('<Autocomplete />', () => {
  let mount;
  let classes;
  const render = createClientRender();

  before(() => {
    classes = getClasses(<Autocomplete renderInput={() => null} />);
    mount = createMount({ strict: true });
  });
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-19511/; bin/envrun 'grep "\"test:unit\"" package.json; yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/Autocomplete/Repro.test.js 2>&1 | tail -30'
```

tool result:

```
Command did not complete within its 120s timeout and was moved to the background (ID: bj7cgn18k). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/d6e7d7f0-5067-4b0f-abdd-d217a236d757/tasks/bj7cgn18k.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /work/mui__material-ui-19511/repo/packages/material-ui-lab/src; directory changes made by the backgrounded command do not apply to subsequent commands.
```

**thinking:**

```
Found the bug: when input stops matching any option, `filteredOptions` empties out and the popup closes before the highlight reset runs, leaving `selectedIndexRef` stuck at `0`—so on blur `filteredOptions[0]` is undefined and the field clears. I'm now waiting on a reproduction test to confirm.


```

**tool call: Bash**

```bash
sleep 90; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/d6e7d7f0-5067-4b0f-abdd-d217a236d757/tasks/bj7cgn18k.output
```

tool result:

```
    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/*.test.js' 'docs/**/*.t
```

**tool call: Bash**

```bash
sleep 120; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/d6e7d7f0-5067-4b0f-abdd-d217a236d757/tasks/bj7cgn18k.output
```

tool result:

```
    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/*.test.js' 'docs/**/*.t
```

**tool call: Bash**

```bash
sleep 240; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/d6e7d7f0-5067-4b0f-abdd-d217a236d757/tasks/bj7cgn18k.output
```

tool result:

```
    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/*.test.js' 'docs/**/*.t
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-19511/; bin/envrun 'cat .mocharc.js; ps aux | grep -c mocha'
```

tool result:

```
module.exports = {
  recursive: true,
  reporter: 'dot',
  require: [require.resolve('@babel/register'), require.resolve('./test/utils/setup')],
};
7
Shell cwd was reset to /work/mui__material-ui-19511/repo
```

**tool call: Bash**

```bash
sleep 300; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/d6e7d7f0-5067-4b0f-abdd-d217a236d757/tasks/bj7cgn18k.output
```

tool result:

```
    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/*.test.js' 'docs/**/*.t
```

**assistant:** The test run has been stuck for more than 10 minutes, so I'm checking whether mocha is hung.

**tool call: Bash**

```bash
cd /work/mui__material-ui-19511/; bin/envrun 'ps aux | grep -v grep | grep -i "mocha\|node" | cut -c1-200'
```

tool result:

```
root        15  0.1  0.5 1281448 94044 ?       Sl   11:27   0:01 node --no-opt -r /proc/.reset /usr/local/nvm/versions/node/v16.20.2/bin/yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/
root        27  0.0  0.0 418028  3348 ?        S    11:27   0:00 /bin/sh -c /testbed/node_modules/.bin/cross-env NODE_ENV=test mocha packages/material-ui-lab/src/Autocomplete/Repro.test.js
root        28  0.0  0.3 945208 50772 ?        Sl   11:27   0:00 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/.bin/cross-env NODE_ENV=test mocha packag
root        35  0.9  1.3 1128152 222840 ?      Sl   11:27   0:08 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/.bin/mocha packages/material-ui-lab/src/A
Shell cwd was reset to /work/mui__material-ui-19511/repo
```

**assistant:** Mocha has barely used any CPU, so it's probably idle and not exiting rather than still working. I'll stop it and rerun with `--exit`.

**tool call: Bash**

```bash
cd /work/mui__material-ui-19511/; bin/envrun 'pkill -f mocha; timeout 300 yarn -s cross-env NODE_ENV=test mocha --exit packages/material-ui-lab/src/Autocomplete/Repro.test.js 2>&1 | tail -30'
```

tool result:

```
Exit code 143
```

**assistant:** That `pkill -f mocha` also matched its own shell command, so the run killed itself. Running again without it:

**tool call: Bash**

```bash
cd /work/mui__material-ui-19511/; bin/envrun 'timeout 300 yarn -s cross-env NODE_ENV=test mocha --exit packages/material-ui-lab/src/Autocomplete/Repro.test.js 2>&1 | tail -30'
```

tool result:

```
warning You don't appear to have an internet connection. Try the --offline flag to use the cache for registry queries.
Browserslist: caniuse-lite is outdated. Please run the following command: `yarn upgrade`
including inaccessible elements by default


  ․

  1 passing (422ms)
Shell cwd was reset to /work/mui__material-ui-19511/repo
```

**assistant:** The test passed, so the bug didn't show up. Typing "oo" in one step never sets `selectedIndexRef` to 0. I'll type "o" first so an option gets highlighted, then "oo".

**tool call: Bash**

```bash
cd /work/mui__material-ui-19511/; sed -i '' "s/    fireEvent.change(document.activeElement, { target: { value: 'oo' } });/    fireEvent.change(document.activeElement, { target: { value: 'o' } });\n&/" testbed/packages/material-ui-lab/src/Autocomplete/Repro.test.js; grep -n change testbed/packages/material-ui-lab/src/Autocomplete/Repro.test.js; bin/envrun 'timeout 300 yarn -s cross-env NODE_ENV=test mocha --exit packages/material-ui-lab/src/Autocomplete/Repro.test.js 2>&1 | tail -30'
```

tool result:

```
20:    fireEvent.change(document.activeElement, { target: { value: 'o' } });
21:    fireEvent.change(document.activeElement, { target: { value: 'oo' } });
warning You don't appear to have an internet connection. Try the --offline flag to use the cache for registry queries.
Browserslist: caniuse-lite is outdated. Please run the following command: `yarn upgrade`
including inaccessible elements by default


  !

  0 passing (475ms)
  1 failing

  1) repro
       keeps freeSolo value on blur with autoHighlight:
     AssertionError: expected undefined to equal 'oo'
      at Context.<anonymous> (packages/material-ui-lab/src/Autocomplete/Repro.test.js:24:40)
      at processImmediate (node:internal/timers:466:21)
Shell cwd was reset to /work/mui__material-ui-19511/repo
```

**thinking:**

```
I've confirmed the bug: `onChange` returns `undefined` instead of `'oo'`. I'll fix it by auto-selecting the highlighted option on blur only while the popup is open, so it's still present in `filteredOptions`.


```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/mui__material-ui-19511/repo/packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js",
 "old_string": "    if (autoSelect && selectedIndexRef.current !== -1) {",
 "new_string": "    if (autoSelect && selectedIndexRef.current !== -1 && popupOpen) {"
}
```

tool result:

```
The file /work/mui__material-ui-19511/repo/packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-19511/; bin/envrun 'timeout 500 yarn -s cross-env NODE_ENV=test mocha --exit packages/material-ui-lab/src/Autocomplete/Repro.test.js "packages/material-ui-lab/src/Autocomplete/*.test.js" "packages/material-ui-lab/src/useAutocomplete/*.test.js" 2>&1 | tail -30'
```

tool result:

```
warning You don't appear to have an internet connection. Try the --offline flag to use the cache for registry queries.
Browserslist: caniuse-lite is outdated. Please run the following command: `yarn upgrade`
including inaccessible elements by default
[33mWarning: Cannot find any files matching pattern "packages/material-ui-lab/src/useAutocomplete/*.test.js"[39m
/testbed/node_modules/mocha/node_modules/yargs/yargs.js:1163
      else throw err
           ^

Error: [33mWarning: Cannot find any files matching pattern "packages/material-ui-lab/src/useAutocomplete/*.test.js"[39m
    at _construct (/testbed/node_modules/@babel/runtime/helpers/construct.js:30:21)
    at console.warn (/testbed/test/utils/consoleError.js:13:5)
    at /testbed/node_modules/mocha/lib/cli/collect-files.js:80:15
    at Array.forEach (<anonymous>)
    at module.exports (/testbed/node_modules/mocha/lib/cli/collect-files.js:79:15)
    at Object.exports.singleRun (/testbed/node_modules/mocha/lib/cli/run-helpers.js:105:17)
    at exports.runMocha (/testbed/node_modules/mocha/lib/cli/run-helpers.js:143:13)
    at Object.exports.handler (/testbed/node_modules/mocha/lib/cli/run.js:305:3)
    at Object.runCommand (/testbed/node_modules/mocha/node_modules/yargs/lib/command.js:242:26)
    at Object.parseArgs [as _parseArgs] (/testbed/node_modules/mocha/node_modules/yargs/yargs.js:1087:28)
    at Object.parse (/testbed/node_modules/mocha/node_modules/yargs/yargs.js:566:25)
    at Object.exports.main (/testbed/node_modules/mocha/lib/cli/cli.js:68:6)
    at Object.<anonymous> (/testbed/node_modules/mocha/bin/mocha:133:29)
    at Module._compile (node:internal/modules/cjs/loader:1198:14)
    at Object.Module._extensions..js (node:internal/modules/cjs/loader:1252:10)
    at Module.load (node:internal/modules/cjs/loader:1076:32)
    at Function.Module._load (node:internal/modules/cjs/loader:911:12)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:81:12)
    at node:internal/main/run_main_module:22:47
Shell cwd was reset to /work/mui__material-ui-19511/repo
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-19511/; bin/envrun 'timeout 500 yarn -s cross-env NODE_ENV=test mocha --exit "packages/material-ui-lab/src/Autocomplete/*.test.js" 2>&1 | tail -30'
```

tool result:

```
warning You don't appear to have an internet connection. Try the --offline flag to use the cache for registry queries.
Browserslist: caniuse-lite is outdated. Please run the following command: `yarn upgrade`
including inaccessible elements by default


  ․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․
  ․․․․․

  61 passing (3s)
Shell cwd was reset to /work/mui__material-ui-19511/repo
```

**assistant:** All 61 Autocomplete tests pass. Now I'll delete the reproduction file and check the final diff.

**tool call: Bash**

```bash
cd /work/mui__material-ui-19511/repo; rm packages/material-ui-lab/src/Autocomplete/Repro.test.js; git status --short; git diff
```

tool result:

```
 M package.json
 M packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
diff --git a/package.json b/package.json
index 59a0a0420..177ce4504 100644
--- a/package.json
+++ b/package.json
@@ -53,17 +53,20 @@
     "@babel/register": "^7.7.4",
     "@testing-library/dom": "^6.8.1",
     "@testing-library/react": "^9.3.2",
-    "@types/chai": "^4.2.3",
-    "@types/chai-dom": "^0.0.8",
+    "@types/chai": "^5.2.2",
+    "@types/chai-dom": "^1.11.3",
     "@types/enzyme": "^3.10.3",
+    "@types/format-util": "^1.0.4",
     "@types/fs-extra": "^8.0.0",
     "@types/glob": "^7.1.1",
     "@types/jsdom": "^12.2.4",
     "@types/lodash": "^4.14.138",
     "@types/mocha": "^7.0.1",
     "@types/prettier": "^1.18.0",
+    "@types/prop-types": "^15.7.15",
     "@types/react": "^16.9.3",
-    "@types/sinon": "^7.0.13",
+    "@types/react-dom": "^19.1.8",
+    "@types/sinon": "^17.0.4",
     "argos-cli": "^0.1.2",
     "babel-core": "^7.0.0-bridge.0",
     "babel-eslint": "^10.0.3",
diff --git a/packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js b/packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js
index 632fb2bf4..1f9713e0a 100644
--- a/packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js
+++ b/packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js
@@ -656,7 +656,7 @@ export default function useAutocomplete(props) {
       return;
     }
 
-    if (autoSelect && selectedIndexRef.current !== -1) {
+    if (autoSelect && selectedIndexRef.current !== -1 && popupOpen) {
       selectNewValue(event, filteredOptions[selectedIndexRef.current]);
     } else if (autoSelect && freeSolo && inputValue !== '') {
       selectNewValue(event, inputValue, 'freeSolo');
diff --git a/yarn.lock b/yarn.lock
index 94ed528f4..c90a4d6f5 100644
--- a/yarn.lock
+++ b/yarn.lock
@@ -2052,18 +2052,25 @@
   resolved "https://registry.yarnpkg.com/@types/autosuggest-highlight/-/autosuggest-highlight-3.1.0.tgz#62045417c2f6d841f9f12e715336218e4db0fcb1"
   integrity sha512-rJWvrDFKf2NkB3CkeJPcnX3oD0XAQriJOhYC5DUwiK6X/KTM96e1rW+1/PgI0U4tL6GQ2K7dvoiYFhMnAaNLUw==
 
-"@types/chai-dom@^0.0.8":
-  version "0.0.8"
-  resolved "https://registry.yarnpkg.com/@types/chai-dom/-/chai-dom-0.0.8.tgz#832b68d78390c80030e64d8fd4990e514484e91d"
-  integrity sha512-F5vAuz2hp7VY+0UmkFLgTwyeHDddIw1c/JbAQZp2lgpZOd3ujlHFijWO4sHdo7sun9HrzwnSJlZfINdKrUwI+w==
+"@types/chai-dom@^1.11.3":
+  version "1.11.3"
+  resolved "https://registry.yarnpkg.com/@types/chai-dom/-/chai-dom-1.11.3.tgz#1659ace2698cdcd9ed8b2c007876f53e37d9cc89"
+  integrity sha512-EUEZI7uID4ewzxnU7DJXtyvykhQuwe+etJ1wwOiJyQRTH/ifMWKX+ghiXkxCUvNJ6IQDodf0JXhuP6zZcy2qXQ==
   dependencies:
     "@types/chai" "*"
 
-"@types/chai@*", "@types/chai@^4.2.3":
+"@types/chai@*":
   version "4.2.7"
   resolved "https://registry.yarnpkg.com/@types/chai/-/chai-4.2.7.tgz#1c8c25cbf6e59ffa7d6b9652c78e547d9a41692d"
   integrity sha512-luq8meHGYwvky0O7u0eQZdA7B4Wd9owUCqvbw2m3XCrCU8mplYOujMBbvyS547AxJkC+pGnd0Cm15eNxEUNU8g==
 
+"@types/chai@^5.2.2":
+  version "5.2.2"
+  resolved "https://registry.yarnpkg.com/@types/chai/-/chai-5.2.2.tgz#6f14cea18180ffc4416bc0fd12be05fdd73bdd6b"
+  integrity sha512-8kB30R7Hwqf40JPiKhVzodJs2Qc1ZJ5zuT3uzw5Hq/dhNCl3G3l83jfpdI1e20BP348+fV7VIL/+FxaXkqBmWg==
+  dependencies:
+    "@types/deep-eql" "*"
+
 "@types/cheerio@*":
   version "0.22.11"
   resolved "https://registry.yarnpkg.com/@types/cheerio/-/cheerio-0.22.11.tgz#61c0facf9636d14ba5f77fc65ed8913aa845d717"
@@ -2081,6 +2088,11 @@
   resolved "https://registry.yarnpkg.com/@types/css-mediaquery/-/css-mediaquery-0.1.0.tgz#61d439d8163880e90b61d19aba24f7b778c4e77d"
   integrity sha512-jzZ9bRw8fTgCEllDvE7GHR1zTP5LsDHJbAX6BCwD9qdxIOq/Le5TTsdteoCIdEQaFpDMvudLHU/hLo1Lmfcy0Q==
 
+"@types/deep-eql@*":
+  version "4.0.2"
+  resolved "https://registry.yarnpkg.com/@types/deep-eql/-/deep-eql-4.0.2.tgz#334311971d3a07121e7eb91b684a605e7eea9cbd"
+  integrity sha512-c9h9dVVMigMPc4bwTvC5dxqtqJZwQPePsWjPlpSOnojbor6pGqdk541lfA7AqFQr5pB1BRdq0juY9db81BwyFw==
+
 "@types/enzyme@^3.10.3":
   version "3.10.4"
   resolved "https://registry.yarnpkg.com/@types/enzyme/-/enzyme-3.10.4.tgz#dd4961042381a7c0f6637ce25fec3f773ce489dd"
@@ -2099,6 +2111,11 @@
   resolved "https://registry.yarnpkg.com/@types/events/-/events-3.0.0.tgz#2862f3f58a9a7f7c3e78d79f130dd4d71c25c2a7"
   integrity sha512-EaObqwIvayI5a8dCzhFrjKzVwKLxjoG9T6Ppd5CEo07LRKfQ8Yokw54r5+Wq7FaBQ+yXRvQAYPrHwya1/UFt9g==
 
+"@types/format-util@^1.0.4":
+  version "1.0.4"
+  resolved "https://registry.yarnpkg.com/@types/format-util/-/format-util-1.0.4.tgz#c4e3b556735149fdf047898a5b9c04650491509b"
+  integrity sha512-xrCYOdHh5zA3LUrn6CvspYwlzSWxPso11Lx32WnAG6KvLCRecKZ/Rh21PLXUkzUFsQmrGcx/traJAFjR6dVS5Q==
+
 "@types/fs-extra@^8.0.0":
   version "8.0.1"
   resolved "https://registry.yarnpkg.com/@types/fs-extra/-/fs-extra-8.0.1.tgz#a2378d6e7e8afea1564e44aafa2e207dadf77686"
@@ -2197,6 +2214,11 @@
   resolved "https://registry.yarnpkg.com/@types/prop-types/-/prop-types-15.7.1.tgz#f1a11e7babb0c3cad68100be381d1e064c68f1f6"
   integrity sha512-CFzn9idOEpHrgdw8JsoTkaDDyRWk1jrzIV8djzcgpq0y9tG4B4lFT+Nxh52DVpDXV+n4+NPNv7M1Dj5uMp6XFg==
 
+"@types/prop-types@^15.7.15":
+  version "15.7.15"
+  resolved "https://registry.yarnpkg.com/@types/prop-types/-/prop-types-15.7.15.tgz#e6e5a86d602beaca71ce5163fadf5f95d70931c7"
+  integrity sha512-F6bEyamV9jKGAFBEmlQnesRPGOQqS2+Uwi0Em15xenOxHaf2hv6L8YCVn3rPdPJOiJfPiCnLIRyvwVaqMY3MIw==
+
 "@types/q@^1.5.1":
   version "1.5.2"
   resolved "https://registry.yarnpkg.com/@types/q/-/q-1.5.2.tgz#690a1475b84f2a884fd07cd797c00f5f31356ea8"
@@ -2209,6 +2231,11 @@
   dependencies:
     "@types/react" "*"
 
+"@types/react-dom@^19.1.8":
+  version "19.1.8"
+  resolved "https://registry.yarnpkg.com/@types/react-dom/-/react-dom-19.1.8.tgz#6cad88ec938beb2626df7c4cb97b15d9f66a05a9"
+  integrity sha512-xG7xaBMJCpcK0RpN8jDbAACQo54ycO6h4dSSmgv8+fu6ZIAdANkx/WsawASUjVXYfy+J9AbUpRMNNEsXCDfDBQ==
+
 "@types/react-nati
[... 1183 more characters not shown]
```

**assistant:** I fixed it: with `freeSolo`, `autoHighlight` and `autoSelect`, typing a value that matches no option and then leaving the field now keeps the value.

**Cause:** With `autoHighlight`, typing text that matches an option (e.g. "o") highlights option 0 and stores that index. When the text stops matching anything (e.g. "oo"), the option list becomes empty and the `freeSolo` popup closes. The code that resets the stored index only runs while the popup is open, so the old index 0 stayed. On blur, `handleBlur` tried to select `filteredOptions[0]`, which no longer existed. That passed `undefined` as the new value and cleared the input. This is why it only happened after the text had first matched something, and only the first time.

**Fix** (one line in `packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js`): on blur, the highlighted option is auto-selected only if the popup is open.

```js
if (autoSelect && selectedIndexRef.current !== -1 && popupOpen) {
```

Otherwise blur goes to the existing `freeSolo` branch, which commits the typed text.

**Verification:**
- **Reproduction:** I wrote a temporary test that types "o", then "oo", then blurs. Before the fix, `onChange` received `undefined`. After the fix, it receives `'oo'` and the input keeps its text. I deleted the test afterwards.
- **Existing tests:** All 61 Autocomplete tests pass.

**Side effects:**
- **Escape before blur:** Without `freeSolo`, if someone closes the popup with Escape and then leaves the field, the highlighted option is no longer auto-selected. The input resets to the current value instead.
- **No matches without `freeSolo`:** I didn't change this case. The popup stays open showing "No options", and the stored index may still point past the empty list. It's outside this issue, so I left it alone.

`git status` also shows changes to `package.json` and `yarn.lock`, plus untracked `Dockerfile` and `custom-reporter.js`. I didn't make any of those; they look like part of the container setup, so I left them as they are.

_session end: success, turns 19, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.15 s: cat .mocharc.js; ps aux | grep -c mocha
- `rc=0` 0.14 s: ps aux | grep -v grep | grep -i "mocha\|node" | cut -c1-200
- `rc=143` 893.27 s: grep "\"test:unit\"" package.json; yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/Autocomplete/Repro.test.js 2>&1 | tail -30
- `rc=143` 0.15 s: pkill -f mocha; timeout 300 yarn -s cross-env NODE_ENV=test mocha --exit packages/material-ui-lab/src/Autocomplete/Repro.test.js 2>&1 | tail -30
- `rc=0` 2.65 s: timeout 300 yarn -s cross-env NODE_ENV=test mocha --exit packages/material-ui-lab/src/Autocomplete/Repro.test.js 2>&1 | tail -30
- `rc=0` 2.91 s: timeout 300 yarn -s cross-env NODE_ENV=test mocha --exit packages/material-ui-lab/src/Autocomplete/Repro.test.js 2>&1 | tail -30
- `rc=0` 2.02 s: timeout 500 yarn -s cross-env NODE_ENV=test mocha --exit packages/material-ui-lab/src/Autocomplete/Repro.test.js "packages/material-ui-lab/src/Autocomplete/*.test.js" "packages/material-ui-lab/src/useAutocomplete/*.test.js" 2>&1 | tail -30
- `rc=0` 6.47 s: timeout 500 yarn -s cross-env NODE_ENV=test mocha --exit "packages/material-ui-lab/src/Autocomplete/*.test.js" 2>&1 | tail -30
