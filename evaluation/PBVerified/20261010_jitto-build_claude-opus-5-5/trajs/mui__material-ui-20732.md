# Instance: mui__material-ui-20732

- Final resolved (evaluator, logs/mui__material-ui-20732_result.json): True
- Run state: DONE
- One attempt. Duration 771.7 s, turns 16, actor cost $0.22806760000000006, container commands 5
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/mui__material-ui-20732/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-20732/repo. Consider the following issue description:

<issue_description>
Single-select autocomplete doesn't open on click after selecting option
<!-- Provide a general summary of the issue in the Title above -->

<!--
  Thank you very much for contributing to Material-UI by creating an issue! ❤️
  To avoid duplicate issues we ask you to check off the following list.
-->

<!-- Checked checkbox should look like this: [x] -->

- [x] The issue is present in the latest release.
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Current Behavior 😯

I am using `Autocomplete` component with single-choice that closes on option select. When an option has been selected, it closes, but stays in focus which prevents it from opening when the user clicks on the input again.

## Expected Behavior 🤔

After an option has been selected, autocomplete closes but reacts on click by showing the list of options again.

## Steps to Reproduce 🕹

Can be reproduced on all examples of single-choice autocomplete without `disableCloseOnSelect` set to `true`. See https://material-ui.com/components/autocomplete/. 

Steps:

1. Open an autocomplete by clicking on it
2. Select an option (autocomplete closes)
3. Click on the input field of the autocomplete
4. The list of options doesn't appear

## Context 🔦

I have tried setting my own `open` state and trying to control it myself, but got issues with input focus and the component getting open and closed multiple times in a row.

## Your Environment 🌎

<!--
  Include as many relevant details about the environment with which you experienced the bug.
  If you encounter issues with typescript please include version and tsconfig.
-->

| Tech        | Version |
| ----------- | ------- |
| Material-UI | v4.9.3  |
| Material-UI lab | v4.0.0-alpha.47  |
| React       |    v16.9.0     |
| Browser     |   all      |
| etc.        |         |

The autocomplete component is perfect for our application at work, unfortunately this issue is considered to be rather crucial, so I really appreciate any help on this! 
Thanks in advance! 🙂 


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-20732/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-20732/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-20732/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-20732/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
grep -n "handleMouseDown\|handleInputMouseDown\|handleClick\|onMouseDown\|onClick\|handleOpen\|const handleFocus\|handleInputChange = " packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js
```

tool result:

```
459:  const handleOpen = (event) => {
577:  const handleFocusTag = (event, direction) => {
644:        handleOpen(event);
650:        handleOpen(event);
656:        handleOpen(event);
662:        handleOpen(event);
735:  const handleFocus = (event) => {
739:      handleOpen(event);
772:  const handleInputChange = (event) => {
788:      handleOpen(event);
801:  const handleOptionClick = (event) => {
836:      handleOpen(event);
841:  const handleMouseDown = (event) => {
848:  const handleClick = () => {
862:  const handleInputMouseDown = (event) => {
913:      onMouseDown: handleMouseDown,
914:      onClick: handleClick,
926:      onMouseDown: handleInputMouseDown,
941:      onClick: handleClear,
945:      onClick: handlePopupIndicator,
958:      onMouseDown: (event) => {
975:        onClick: handleOptionClick,
```

**tool call: Bash**

```bash
sed -n 730,880p packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js; git log --oneline -1
```

tool result:

```
    if (other.onKeyDown) {
      other.onKeyDown(event);
    }
  };

  const handleFocus = (event) => {
    setFocused(true);

    if (openOnFocus && !ignoreFocus.current) {
      handleOpen(event);
    }
  };

  const handleBlur = (event) => {
    // Ignore the event when using the scrollbar with IE 11
    if (
      listboxRef.current !== null &&
      document.activeElement === listboxRef.current.parentElement
    ) {
      inputRef.current.focus();
      return;
    }

    setFocused(false);
    firstFocus.current = true;
    ignoreFocus.current = false;

    if (debug && inputValue !== '') {
      return;
    }

    if (autoSelect && highlightedIndexRef.current !== -1 && popupOpen) {
      selectNewValue(event, filteredOptions[highlightedIndexRef.current], 'blur');
    } else if (autoSelect && freeSolo && inputValue !== '') {
      selectNewValue(event, inputValue, 'blur', 'freeSolo');
    } else if (clearOnBlur) {
      resetInputValue(event, value);
    }

    handleClose(event, 'blur');
  };

  const handleInputChange = (event) => {
    const newValue = event.target.value;

    if (inputValue !== newValue) {
      setInputValue(newValue);

      if (onInputChange) {
        onInputChange(event, newValue, 'input');
      }
    }

    if (newValue === '') {
      if (!disableClearable && !multiple) {
        handleValue(event, null, 'clear');
      }
    } else {
      handleOpen(event);
    }
  };

  const handleOptionMouseOver = (event) => {
    const index = Number(event.currentTarget.getAttribute('data-option-index'));
    setHighlightedIndex(index, 'mouse', event);
  };

  const handleOptionTouchStart = () => {
    isTouch.current = true;
  };

  const handleOptionClick = (event) => {
    const index = Number(event.currentTarget.getAttribute('data-option-index'));
    selectNewValue(event, filteredOptions[index], 'select-option');

    isTouch.current = false;
  };

  const handleTagDelete = (index) => (event) => {
    const newValue = [...value];
    newValue.splice(index, 1);
    handleValue(event, newValue, 'remove-option', {
      option: value[index],
    });
  };

  const handleListboxRef = useEventCallback((node) => {
    setRef(listboxRef, node);

    if (!node) {
      return;
    }

    // Automatically select the first option as the listbox become visible.
    if (highlightedIndexRef.current === -1 && autoHighlight) {
      changeHighlightedIndex('reset', 'next');
    } else {
      // Restore the focus to the correct option.
      setHighlightedIndex(highlightedIndexRef.current);
    }
  });

  const handlePopupIndicator = (event) => {
    if (open) {
      handleClose(event, 'toggleInput');
    } else {
      handleOpen(event);
    }
  };

  // Prevent input blur when interacting with the combobox
  const handleMouseDown = (event) => {
    if (event.target.getAttribute('id') !== id) {
      event.preventDefault();
    }
  };

  // Focus the input when interacting with the combobox
  const handleClick = () => {
    inputRef.current.focus();

    if (
      selectOnFocus &&
      firstFocus.current &&
      inputRef.current.selectionEnd - inputRef.current.selectionStart === 0
    ) {
      inputRef.current.select();
    }

    firstFocus.current = false;
  };

  const handleInputMouseDown = (event) => {
    if (inputValue === '') {
      handlePopupIndicator(event);
    }
  };

  let dirty = freeSolo && inputValue.length > 0;
  dirty = dirty || (multiple ? value.length > 0 : value !== null);

  let groupedOptions = filteredOptions;
  if (groupBy) {
    // used to keep track of key and indexes in the result array
    const indexBy = new Map();
    let warn = false;

    groupedOptions = filteredOptions.reduce((acc, option, index) => {
      const group = groupBy(option);

      if (acc.length > 0 && acc[acc.length - 1].group === group) {
2231349c3 [Autocomplete] Remove startAfter props (#20729)
```

**tool call: Bash**

```bash
grep -n "mouse\|click" -i packages/material-ui-lab/src/Autocomplete/Autocomplete.test.js | head -50
```

tool result:

```
285:      fireEvent.click(container.querySelectorAll('svg[data-mui-test="CancelIcon"]')[1]);
483:      fireEvent.click(clear);
621:      fireEvent.mouseDown(textbox);
622:      fireEvent.click(textbox);
629:      fireEvent.mouseDown(textbox);
630:      fireEvent.click(textbox);
634:      fireEvent.mouseDown(textbox);
635:      fireEvent.click(textbox);
997:      fireEvent.click(input);
1001:      fireEvent.click(firstOption);
1071:  describe('click input', () => {
1083:      fireEvent.mouseDown(textbox);
1085:      fireEvent.mouseDown(textbox);
1099:      fireEvent.click(textbox);
1104:    it('should focus the input when clicking on the open action', () => {
1115:      fireEvent.click(textbox);
1119:      fireEvent.click(queryByTitle('Open'));
1385:      fireEvent.click(button);
1433:    it('[blurOnSelect=true] should blur the input when clicking or touching options', () => {
1447:      fireEvent.click(firstOption);
1450:      fireEvent.click(queryByTitle('Open'));
1454:      fireEvent.click(firstOption);
1471:      fireEvent.click(firstOption);
1474:      fireEvent.click(queryByTitle('Open'));
1477:      fireEvent.click(firstOption);
1481:    it('[blurOnSelect="mouse"] should only blur the input when an option is clicked', () => {
1489:          blurOnSelect="mouse"
1495:      fireEvent.click(firstOption);
1498:      fireEvent.click(queryByTitle('Open'));
1500:      fireEvent.click(firstOption);
1595:    it('should support mouse event', () => {
1607:      fireEvent.mouseOver(firstOption);
1611:      expect(handleChange.args[1][2]).to.equal('mouse');
```

**tool call: Bash**

```bash
sed -n 1068,1125p packages/material-ui-lab/src/Autocomplete/Autocomplete.test.js
```

tool result:

```
    });
  });

  describe('click input', () => {
    it('toggles if empty', () => {
      const { getByRole } = render(
        <Autocomplete
          {...defaultProps}
          options={['one', 'two']}
          renderInput={(params) => <TextField {...params} />}
        />,
      );
      const textbox = getByRole('textbox');
      const combobox = getByRole('combobox');
      expect(combobox).to.have.attribute('aria-expanded', 'false');
      fireEvent.mouseDown(textbox);
      expect(combobox).to.have.attribute('aria-expanded', 'true');
      fireEvent.mouseDown(textbox);
      expect(combobox).to.have.attribute('aria-expanded', 'false');
    });

    it('selects all the first time', () => {
      const { getByRole } = render(
        <Autocomplete
          {...defaultProps}
          value="one"
          options={['one', 'two']}
          renderInput={(params) => <TextField {...params} />}
        />,
      );
      const textbox = getByRole('textbox');
      fireEvent.click(textbox);
      expect(textbox.selectionStart).to.equal(0);
      expect(textbox.selectionEnd).to.equal(3);
    });

    it('should focus the input when clicking on the open action', () => {
      const { getByRole, queryByTitle } = render(
        <Autocomplete
          {...defaultProps}
          value="one"
          options={['one', 'two']}
          renderInput={(params) => <TextField {...params} />}
        />,
      );

      const textbox = getByRole('textbox');
      fireEvent.click(textbox);
      expect(textbox).toHaveFocus();
      textbox.blur();

      fireEvent.click(queryByTitle('Open'));
      expect(textbox).toHaveFocus();
    });
  });

  describe('controlled', () => {
    it('controls the input value', () => {
```

**assistant:** Let me reproduce with a temporary test.

**tool call: Bash**

```bash
mkdir -p /tmp && cat > packages/material-ui-lab/src/Autocomplete/Repro.test.js <<'EOF'
import * as React from 'react';
import { expect } from 'chai';
import { createClientRender, fireEvent } from 'test/utils/createClientRender';
import TextField from '@material-ui/core/TextField';
import Autocomplete from './Autocomplete';

describe('repro', () => {
  const render = createClientRender();
  it('opens on mousedown when value set', () => {
    const { getByRole } = render(
      <Autocomplete value="one" options={['one', 'two']} renderInput={(p) => <TextField {...p} />} />,
    );
    const textbox = getByRole('textbox');
    const combobox = getByRole('combobox');
    textbox.focus();
    expect(combobox).to.have.attribute('aria-expanded', 'false');
    fireEvent.mouseDown(textbox);
    expect(combobox).to.have.attribute('aria-expanded', 'true');
    fireEvent.mouseDown(textbox);
    expect(combobox).to.have.attribute('aria-expanded', 'true');
  });
});
EOF
cat package.json | grep '"test:unit'
```

tool result:

```
    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/*.test.js' 'docs/**/*.test.js' 'scripts/**/*.test.js' --exclude '**/node_modules/**'",
```

**tool call: Bash**

```bash
../bin/envrun 'yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/Autocomplete/Repro.test.js 2>&1 | tail -20'
```

tool result:

```
Command did not complete within its 120s timeout and was moved to the background (ID: bfkc62pv8). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/fe242f1b-bcae-494b-82da-65b758d383d9/tasks/bfkc62pv8.output. You will be notified when it completes. To check interim output, use Read on that file path.
```

**tool call: Bash**

```bash
sleep 90; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/fe242f1b-bcae-494b-82da-65b758d383d9/tasks/bfkc62pv8.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
sleep 120; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/fe242f1b-bcae-494b-82da-65b758d383d9/tasks/bfkc62pv8.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
cat .mocharc.js; sleep 150; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/fe242f1b-bcae-494b-82da-65b758d383d9/tasks/bfkc62pv8.output
```

tool result:

```
module.exports = {
  recursive: true,
  reporter: 'dot',
  require: [require.resolve('@babel/register'), require.resolve('./test/utils/setup')],
};
```

**tool call: Bash**

```bash
sleep 240; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/fe242f1b-bcae-494b-82da-65b758d383d9/tasks/bfkc62pv8.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
../bin/envrun 'ps aux | grep -v grep | grep -i mocha | head'
```

tool result:

```
root         7  0.0  0.0 289612  6092 ?        Ss   08:04   0:00 bash -lc yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/Autocomplete/Repro.test.js 2>&1 | tail -20
root        15  0.1  1.1 1151780 92264 ?       Sl   08:04   0:01 node --no-opt -r /proc/.reset /usr/local/nvm/versions/node/v16.20.2/bin/yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/Autocomplete/Repro.test.js
root        27  0.0  0.0 287856  3212 ?        S    08:04   0:00 /bin/sh -c /testbed/node_modules/.bin/cross-env NODE_ENV=test mocha packages/material-ui-lab/src/Autocomplete/Repro.test.js
root        28  0.0  0.6 815036 50504 ?        Sl   08:04   0:00 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/.bin/cross-env NODE_ENV=test mocha packages/material-ui-lab/src/Autocomplete/Repro.test.js
root        35  1.2  2.6 996212 216132 ?       Sl   08:04   0:09 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/.bin/mocha packages/material-ui-lab/src/Autocomplete/Repro.test.js
```

**assistant:** The mocha run is hung with almost no CPU use, so it's probably not exiting on its own. I'll kill it and rerun with `--exit`.

**tool call: Bash**

```bash
../bin/envrun 'pkill -f mocha; pkill -f "yarn -s"; true'; ../bin/envrun 'timeout 300 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui-lab/src/Autocomplete/Repro.test.js 2>&1 | tail -30'
```

tool result:

```
Browserslist: caniuse-lite is outdated. Please run:
npx browserslist@latest --update-db
including inaccessible elements by default


  !

  0 passing (275ms)
  1 failing

  1) repro
       opens on mousedown when value set:

      AssertionError: expected div.MuiAutocomplete-root.Mui-focused.MuiAutocomplete-hasClearIcon.MuiAutocomplete-hasPopupIcon[role="combobox"][aria-expanded="false"] to have an attribute 'aria-expanded' with the value 'true', but the value was 'false'
      + expected - actual

      -false
      +true
      
      at Context.<anonymous> (packages/material-ui-lab/src/Autocomplete/Repro.test.js:18:30)
      at processImmediate (node:internal/timers:466:21)
```

**thinking:**

```
I've confirmed the bug: mousedown on an input with existing text fails to open the popup. Now I'll fix it so mousedown opens the popup whenever it's closed, regardless of input content.


```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/mui__material-ui-20732/repo/packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js",
 "old_string": "    if (inputValue === '') {\n      handlePopupIndicator(event);",
 "new_string": "    if (inputValue === '' || !open) {\n      handlePopupIndicator(event);"
}
```

tool result:

```
The file /work/mui__material-ui-20732/repo/packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
../bin/envrun 'timeout 300 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui-lab/src/Autocomplete/Repro.test.js packages/material-ui-lab/src/Autocomplete/Autocomplete.test.js packages/material-ui-lab/src/useAutocomplete/*.test.js 2>&1 | tail -30'
```

tool result:

```
Browserslist: caniuse-lite is outdated. Please run:
npx browserslist@latest --update-db
including inaccessible elements by default


  ․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․
  ․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․

  89 passing (4s)
```

**assistant:** The repro passes now, along with all existing Autocomplete and useAutocomplete tests. Removing the repro file:

**tool call: Bash**

```bash
rm packages/material-ui-lab/src/Autocomplete/Repro.test.js && git status --short && git diff
```

tool result:

```
<persisted-output>
Output too large (30.1KB). Full output saved to: <actor-session-dir>

Preview (first 2KB):
 M package.json
 M packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
diff --git a/package.json b/package.json
index b8075a2b6..05d47bec3 100644
--- a/package.json
+++ b/package.json
@@ -58,17 +58,20 @@
     "@testing-library/dom": "^7.0.3",
     "@testing-library/react": "^10.0.1",
     "@testing-library/react-hooks": "3.2.1",
-    "@types/chai": "^4.2.3",
-    "@types/chai-dom": "^0.0.9",
+    "@types/chai": "^5.2.2",
+    "@types/chai-dom": "^1.11.3",
     "@types/enzyme": "^3.10.3",
+    "@types/format-util": "^1.0.4",
     "@types/fs-extra": "^8.0.0",
     "@types/glob": "^7.1.1",
     "@types/jsdom": "^16.1.0",
     "@types/lodash": "^4.14.138",
     "@types/mocha": "^7.0.1",
     "@types/prettier": "^2.0.0",
+    "@types/prop-types": "^15.7.15",
     "@types/react": "^16.9.3",
-    "@types/sinon": "^9.0.0",
+    "@types/react-dom": "^19.1.8",
+    "@types/sinon": "^17.0.4",
     "argos-cli": "^0.1.2",
     "babel-core": "^7.0.0-bridge.0",
     "babel-eslint": "^10.0.3",
@@ -144,7 +147,6 @@
     "typescript": "^3.8.2",
     "typescript-to-proptypes": "^1.5.0",
     "unist-util-visit": "^2.0.2",
-    "vrtest-mui": "^0.3.3",
     "webpack": "^4.41.0",
     "webpack-cli": "^3.3.9",
     "yargs": "^15.2.0",
diff --git a/packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js b/packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js
index 76a1fb32d..fdd530a79 100644
--- a/packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js
+++ b/packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js
@@ -860,7 +860,7 @@ export default function useAutocomplete(props) {
   };
 
   const handleInputMouseDown = (event) => {
-    if (inputValue === '') {
+    if (inputValue === '' || !open) {
       handlePopupIndicator(event);
     }
   };
diff --git a/yarn.lock b/yarn.lock
index e553e33d1..7063e3959 100644
--- a/yarn.lock
+++ b/yarn.lock
@@ -2347,18 +2347,25 @@
...
</persisted-output>
```

**assistant:** I fixed the bug with a one-line change in `packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js:863`. Clicking the input of a single-select Autocomplete now reopens the options list after you've picked one.

**Cause:** Pressing the mouse on the input only opened or closed the list when the input was empty (`inputValue === ''`). Once you select an option, its label fills the input, so clicking it did nothing. Opening when the field gets focus doesn't help either, because the input is still focused after the selection.

**Fix:**
```js
const handleInputMouseDown = (event) => {
  if (inputValue === '' || !open) {
    handlePopupIndicator(event);
  }
};
```
How a click on the input behaves now:
- **Empty input:** it opens and closes the list on alternate clicks, as before.
- **Input has text and the list is closed:** it opens the list.
- **Input has text and the list is open:** it leaves the list open. This means clicking to place the cursor or select text while typing doesn't unexpectedly close it.

**Checks:**
- I wrote a temporary test: focus an Autocomplete that has a value, then press the mouse on the input. It failed before the change (`aria-expanded` stayed `"false"`) and passes after it.
- The existing Autocomplete and useAutocomplete tests all pass (89 passing).
- I deleted the temporary test, so the only change left is the one line above.

Two things about the environment:
- Plain `mocha` hung after the tests finished, so I ran it with `--exit`.
- `git status` also shows changes to `package.json` and `yarn.lock`, plus untracked `Dockerfile` and `custom-reporter.js` files. I didn't make any of these; they appear to come from the test environment setup, so I left them alone.

_session end: success, turns 16, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.14 s: ps aux | grep -v grep | grep -i mocha | head
- `rc=143` 734.73 s: yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/Autocomplete/Repro.test.js 2>&1 | tail -20
- `rc=143` 0.15 s: pkill -f mocha; pkill -f "yarn -s"; true
- `rc=0` 2.45 s: timeout 300 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui-lab/src/Autocomplete/Repro.test.js 2>&1 | tail -30
- `rc=0` 7.59 s: timeout 300 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui-lab/src/Autocomplete/Repro.test.js packages/material-ui-lab/src/Autocomplete/Autocomplete.test.js packages/material-ui-lab/src/useAutocomplete/*.test.js 2>&1 | tail -30
