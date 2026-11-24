# Instance: mui__material-ui-19794

- Final resolved (evaluator, logs/mui__material-ui-19794_result.json): True
- Run state: DONE
- One attempt. Duration 1396.8 s, turns 15, actor cost $0.36186699999999994, container commands 5
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/mui__material-ui-19794/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-19794/repo. Consider the following issue description:

<issue_description>
[Autocomplete] Drop list no close outline mouse

| Tech        | Version |
| ----------- | ------- |
| Material-UI | v4.9.3  |
| React       |   v16.12.0      |
| Browser     |     Chrome   |
| TypeScript  |         |
| etc.        |         |

Hi, please, look at the gif with the problem
![1](https://user-images.githubusercontent.com/11176223/74817353-cef40400-530d-11ea-83b8-2fc6bdfa0cc8.gif)



</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-19794/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-19794/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-19794/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-19794/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/mui__material-ui-19794/repo/packages/material-ui-lab/src/useAutocomplete; grep -n "handleBlur\|handleMouseDown\|handleClick\|handleOptionClick\|onMouseDown\|onClick\|onBlur\|onFocus\|handleFocus\|firstFocus\|inputRef.current.focus\|selectionStart" useAutocomplete.js
```

tool result:

```
127:  const firstFocus = React.useRef(true);
280:      inputRef.current.focus();
506:  const handleFocusTag = (event, direction) => {
594:        handleFocusTag(event, 'previous');
597:        handleFocusTag(event, 'next');
655:  const handleFocus = event => {
663:  const handleBlur = event => {
665:    firstFocus.current = true;
718:  const handleOptionClick = event => {
764:  const handleMouseDown = event => {
771:  const handleClick = () => {
773:      firstFocus.current &&
774:      inputRef.current.selectionEnd - inputRef.current.selectionStart === 0
776:      inputRef.current.focus();
783:    firstFocus.current = false;
833:      onMouseDown: handleMouseDown,
834:      onClick: handleClick,
843:      onBlur: handleBlur,
844:      onFocus: handleFocus,
846:      onMouseDown: handleInputMouseDown,
861:      onClick: handleClear,
865:      onClick: handlePopupIndicator,
878:      onMouseDown: event => {
895:        onClick: handleOptionClick,
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-19794/repo/packages/material-ui-lab/src/useAutocomplete; sed -n 650,900p useAutocomplete.js
```

tool result:

```
    if (other.onKeyDown) {
      other.onKeyDown(event);
    }
  };

  const handleFocus = event => {
    setFocused(true);

    if (!disableOpenOnFocus && !ignoreFocus.current) {
      handleOpen(event);
    }
  };

  const handleBlur = event => {
    setFocused(false);
    firstFocus.current = true;
    ignoreFocus.current = false;

    if (debug && inputValue !== '') {
      return;
    }

    if (autoSelect && highlightedIndexRef.current !== -1 && popupOpen) {
      selectNewValue(event, filteredOptions[highlightedIndexRef.current]);
    } else if (autoSelect && freeSolo && inputValue !== '') {
      selectNewValue(event, inputValue, 'freeSolo');
    } else if (!freeSolo) {
      resetInputValue(event, value);
    }

    handleClose(event);
  };

  const handleInputChange = event => {
    const newValue = event.target.value;

    if (inputValue !== newValue) {
      setInputValue(newValue);

      if (onInputChange) {
        onInputChange(event, newValue, 'input');
      }
    }

    if (newValue === '') {
      if (disableOpenOnFocus) {
        handleClose(event);
      }

      if (!disableClearable && !multiple) {
        handleValue(event, null);
      }
    } else {
      handleOpen(event);
    }
  };

  const handleOptionMouseOver = event => {
    const index = Number(event.currentTarget.getAttribute('data-option-index'));
    setHighlightedIndex(index, 'mouse');
  };

  const isTouch = React.useRef(false);

  const handleOptionTouchStart = () => {
    isTouch.current = true;
  };

  const handleOptionClick = event => {
    const index = Number(event.currentTarget.getAttribute('data-option-index'));
    selectNewValue(event, filteredOptions[index]);

    if (
      blurOnSelect === true ||
      (blurOnSelect === 'touch' && isTouch.current) ||
      (blurOnSelect === 'mouse' && !isTouch.current)
    ) {
      inputRef.current.blur();
    }

    isTouch.current = false;
  };

  const handleTagDelete = index => event => {
    const newValue = [...value];
    newValue.splice(index, 1);
    handleValue(event, newValue);
  };

  const handleListboxRef = useEventCallback(node => {
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

  const handlePopupIndicator = event => {
    if (open) {
      handleClose(event);
    } else {
      handleOpen(event);
    }
  };

  // Prevent input blur when interacting with the combobox
  const handleMouseDown = event => {
    if (event.target.getAttribute('id') !== id) {
      event.preventDefault();
    }
  };

  // Focus the input when first interacting with the combobox
  const handleClick = () => {
    if (
      firstFocus.current &&
      inputRef.current.selectionEnd - inputRef.current.selectionStart === 0
    ) {
      inputRef.current.focus();

      if (selectOnFocus) {
        inputRef.current.select();
      }
    }

    firstFocus.current = false;
  };

  const handleInputMouseDown = event => {
    if (inputValue === '' && (!disableOpenOnFocus || inputRef.current === document.activeElement)) {
      handlePopupIndicator(event);
    }
  };

  let dirty = freeSolo && inputValue.length > 0;
  dirty = dirty || (multiple ? value.length > 0 : value !== null);

  let groupedOptions = filteredOptions;
  if (groupBy) {
    const result = [];

    // used to keep track of key and indexes in the result array
    const indexByKey = new Map();
    let currentResultIndex = 0;

    filteredOptions.forEach(option => {
      const key = groupBy(option);
      if (indexByKey.get(key) === undefined) {
        indexByKey.set(key, currentResultIndex);
        result.push({
          key,
          options: [],
        });
        currentResultIndex += 1;
      }
      result[indexByKey.get(key)].options.push(option);
    });

    // now we can add the `index` property based on the options length
    let indexCounter = 0;
    result.forEach(option => {
      option.index = indexCounter;
      indexCounter += option.options.length;
    });

    groupedOptions = result;
  }

  return {
    getRootProps: (other = {}) => ({
      'aria-owns': popupOpen ? `${id}-popup` : null,
      role: 'combobox',
      'aria-expanded': popupOpen,
      ...other,
      onKeyDown: handleKeyDown(other),
      onMouseDown: handleMouseDown,
      onClick: handleClick,
    }),
    getInputLabelProps: () => ({
      id: `${id}-label`,
      htmlFor: id,
    }),
    getInputProps: () => ({
      id,
      value: inputValue,
      onBlur: handleBlur,
      onFocus: handleFocus,
      onChange: handleInputChange,
      onMouseDown: handleInputMouseDown,
      // if open then this is handled imperativeley so don't let react override
      // only have an opinion about this when closed
      'aria-activedescendant': popupOpen ? '' : null,
      'aria-autocomplete': autoComplete ? 'both' : 'list',
      'aria-controls': popupOpen ? `${id}-popup` : null,
      // Disable browser's suggestion that might overlap with the popup.
      // Handle autocomplete but not autofill.
      autoComplete: 'off',
      ref: inputRef,
      autoCapitalize: 'none',
      spellCheck: 'false',
    }),
    getClearProps: () => ({
      tabIndex: -1,
      onClick: handleClear,
    }),
    getPopupIndicatorProps: () => ({
      tabIndex: -1,
      onClick: handlePopupIndicator,
    }),
    getTagProps: ({ index }) => ({
      key: index,
      'data-tag-index': index,
      tabIndex: -1,
      onDelete: handleTagDelete(index),
    }),
    getListboxProps: () => ({
      role: 'listbox',
      id: `${id}-popup`,
      'aria-labelledby': `${id}-label`,
      ref: handleListboxRef,
      onMouseDown: event => {
        // Prevent blur
        event.preventDefault();
      },
    }),
[... 621 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-19794/repo; git log --oneline -2; grep -n "focus\b\|firstFocus\|selectOnFocus\|activeElement" packages/material-ui-lab/src/Autocomplete/Autocomplete.test.js | head -50
```

tool result:

```
eec5b6086 [Framer] Release v1.1.0 (#19800)
670b858d3 [Tooltip] Add enterNextDelay prop (#19766)
40:      input.focus();
41:      fireEvent.change(document.activeElement, { target: { value: 'a' } });
43:      document.activeElement.blur();
57:    it('should set the focus on the first item', () => {
70:        expect(getByRole('listbox').querySelector('li[data-focus]')).to.have.text(expected);
74:      fireEvent.change(document.activeElement, { target: { value: 'oo' } });
75:      fireEvent.change(document.activeElement, { target: { value: 'o' } });
95:      fireEvent.change(document.activeElement, { target: { value: 'o' } });
96:      fireEvent.keyDown(document.activeElement, { key: 'ArrowDown' });
97:      fireEvent.change(document.activeElement, { target: { value: 'oo' } });
98:      document.activeElement.blur();
117:      fireEvent.change(document.activeElement, { target: { value: 't' } });
118:      fireEvent.keyDown(document.activeElement, { key: 'ArrowDown' });
119:      document.activeElement.blur();
136:      fireEvent.change(document.activeElement, { target: { value: 'a' } });
137:      document.activeElement.blur();
153:      input.focus();
154:      document.activeElement.blur();
155:      input.focus();
189:      fireEvent.keyDown(document.activeElement, { key: 'ArrowLeft' });
190:      expect(document.activeElement).to.have.text('two');
191:      fireEvent.keyDown(document.activeElement, { key: 'ArrowLeft' });
192:      expect(document.activeElement).to.have.text('one');
193:      fireEvent.keyDown(document.activeElement, { key: 'Backspace' });
196:      expect(document.activeElement).to.equal(getByRole('textbox'));
214:    fireEvent.keyDown(document.activeElement, { key: 'Enter' });
217:    fireEvent.change(document.activeElement, { target: { value: 'o' } });
218:    fireEvent.keyDown(document.activeElement, { key: 'ArrowDown' });
219:    fireEvent.keyDown(document.activeElement, { key: 'Enter' });
221:    fireEvent.keyDown(document.activeElement, { key: 'Enter' });
225:    fireEvent.change(document.activeElement, { target: { value: 'o' } });
226:    fireEvent.keyDown(document.activeElement, { key: 'Enter' });
228:    fireEvent.keyDown(document.activeElement, { key: 'Enter' });
232:    fireEvent.change(document.activeElement, { target: { value: 'o' } });
233:    fireEvent.keyDown(document.activeElement, { key: 'Enter' });
328:      fireEvent.keyDown(document.activeElement, { key: 'ArrowDown' });
376:      it(`opens on ${key} when focus is on the textbox without moving focus`, () => {
387:        fireEvent.keyDown(document.activeElement, { key });
389:        // first from focus
408:      fireEvent.keyDown(document.activeElement, { key: 'Escape' });
427:      fireEvent.keyDown(document.activeElement, { key: 'Escape' });
432:    it('moves focus to the first option on ArrowDown', () => {
441:      fireEvent.keyDown(document.activeElement, { key: 'ArrowDown' });
449:    it('moves focus to the last option on ArrowUp', () => {
458:      fireEvent.keyDown(document.activeElement, { key: 'ArrowUp' });
469:    it('disables open on input focus', () => {
482:      expect(textbox).to.have.focus;
488:      document.activeElement.blur();
490:      expect(textbox).to.not.have.focus;
495:      expect(textbox).to.have.focus;
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-19794/repo; cat > packages/material-ui-lab/src/Autocomplete/repro.test.js <<'EOF'
import React from 'react';
import { expect } from 'chai';
import { createClientRender, fireEvent } from 'test/utils/createClientRender';
import TextField from '@material-ui/core/TextField';
import Autocomplete from './Autocomplete';

describe('repro', () => {
  const render = createClientRender();
  it('focuses input when clicking popup indicator after blur with a selection', () => {
    const { getByRole, getByTitle, queryByRole } = render(
      <Autocomplete
        options={['one', 'two']}
        defaultValue="one"
        renderInput={params => <TextField {...params} />}
      />,
    );
    const textbox = getByRole('textbox');
    fireEvent.click(textbox);
    textbox.select();
    textbox.blur();
    expect(queryByRole('listbox')).to.equal(null);
    const button = getByTitle('Open');
    fireEvent.mouseDown(button);
    fireEvent.click(button);
    expect(textbox).to.have.focus;
    textbox.blur();
    expect(queryByRole('listbox')).to.equal(null);
  });
});
EOF
/work/mui__material-ui-19794/bin/envrun 'yarn -s mocha packages/material-ui-lab/src/Autocomplete/repro.test.js 2>&1 | tail -20'
```

tool result:

```
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
    at node:internal/main/run_main_module:22:47 {
  code: 'MODULE_NOT_FOUND',
  requireStack: [
    '/testbed/packages/material-ui-lab/src/Autocomplete/repro.test.js',
    '/testbed/node_modules/mocha/lib/mocha.js',
    '/testbed/node_modules/mocha/lib/cli/one-and-dones.js',
    '/testbed/node_modules/mocha/lib/cli/options.js',
    '/testbed/node_modules/mocha/bin/mocha'
  ]
}
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-19794/repo; head -8 packages/material-ui-lab/src/Autocomplete/Autocomplete.test.js
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
import { createFilterOptions } from '../useAutocomplete/useAutocomplete';
```

**assistant:** The imports are the same as the existing test's, so the failure is probably about how mocha is invoked. I'll use the repo's own test script.

**tool call: Bash**

```bash
cd /work/mui__material-ui-19794/repo; grep -n '"test' package.json; /work/mui__material-ui-19794/bin/envrun 'yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/Autocomplete/repro.test.js 2>&1 | tail -20'
```

tool result:

```
Command did not complete within its 120s timeout and was moved to the background (ID: bc9vnl61l). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/b8763740-4743-4f98-9972-2020553ceb84/tasks/bc9vnl61l.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /work/mui__material-ui-19794/repo; directory changes made by the backgrounded command do not apply to subsequent commands.
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-19794/repo; grep -n '"test' package.json; cat .mocharc.js 2>/dev/null | head -20
```

tool result:

```
33:    "test": "yarn lint && yarn typescript && yarn test:coverage",
34:    "test:coverage": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha 'packages/**/*.test.js' 'docs/**/*.test.js' --exclude '**/node_modules/**' && nyc report -r lcovonly",
35:    "test:coverage:html": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha 'packages/**/**/*.test.js' --exclude '**/node_modules/**' && nyc report --reporter=html",
36:    "test:karma": "cross-env NODE_ENV=test karma start test/karma.conf.js",
37:    "test:regressions": "webpack --config test/regressions/webpack.config.js && rimraf test/regressions/screenshots/chrome/* && vrtest run --config test/vrtest.config.js --record",
38:    "test:umd": "node packages/material-ui/test/umd/run.js",
39:    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/*.test.js' 'docs/**/*.test.js' 'scripts/**/*.test.js' --exclude '**/node_modules/**'",
40:    "test:watch": "yarn test:unit --watch",
module.exports = {
  recursive: true,
  reporter: 'dot',
  require: [require.resolve('@babel/register'), require.resolve('./test/utils/setup')],
};
```

**tool call: Bash**

```bash
sleep 90; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/b8763740-4743-4f98-9972-2020553ceb84/tasks/bc9vnl61l.output | tail -30
```

tool result:

```
33:    "test": "yarn lint && yarn typescript && yarn test:coverage",
34:    "test:coverage": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha 'packages/**/*.test.js' 'docs/**/*.test.js' --exclude '**/node_modules/**' && nyc report -r lcovonly",
35:    "test:coverage:html": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha 'packages/**/**/*.test.js' --exclude '**/node_modules/**' && nyc report --reporter=html",
36:    "test:karma": "cross-env NODE_ENV=test karma start test/karma.conf.js",
37:    "test:regressions": "webpack --config test/regressions/webpack.config.js && rimraf test/regressions/screenshots/chrome/* && vrtest run --config test/vrtest.config.js --record",
38:    "test:umd": "node packages/material-ui/test/umd/run.js",
39:    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/*.test.js' 'docs/**/*.test.js' 'scripts/**/*.test.js' --exclude '**/node_modules/**'",
40:    "test:watch": "yarn test:unit --watch",
```

**tool call: Bash**

```bash
sleep 120; tail -30 /tmp/cell-scratch/claude-502/<actor-session-slug>/b8763740-4743-4f98-9972-2020553ceb84/tasks/bc9vnl61l.output
```

tool result:

```
Exit code 143
Command timed out after 2m 0s
```

**tool call: Bash**

```bash
/work/mui__material-ui-19794/bin/envrun 'NODE_ENV=test timeout 500 node_modules/.bin/mocha packages/material-ui-lab/src/Autocomplete/repro.test.js 2>&1 | tail -30'
```

tool result:

```
      -          [33mclass[39m=[32m"MuiAutocomplete-option"[39m
      -          [33mdata-option-index[39m=[32m"1"[39m
      -          [33mid[39m=[32m"mui-autocomplete-34704-option-1"[39m
      -          [33mrole[39m=[32m"option"[39m
      -          [33mtabindex[39m=[32m"-1"[39m
      -        [36m>[39m
      -          [0mtwo[0m
      -        [36m</li>[39m
      -      [36m</ul>[39m
      -    [36m</div>[39m
      -  [36m</div>[39m
      -[36m</body>[39m
      +[36m<input[39m
      +  [33maria-autocomplete[39m=[32m"list"[39m
      +  [33maria-controls[39m=[32m"mui-autocomplete-34704-popup"[39m
      +  [33maria-invalid[39m=[32m"false"[39m
      +  [33mautocapitalize[39m=[32m"none"[39m
      +  [33mautocomplete[39m=[32m"off"[39m
      +  [33mclass[39m=[32m"MuiInputBase-input MuiInput-input MuiAutocomplete-input MuiAutocomplete-inputFocused MuiInputBase-inputAdornedEnd"[39m
      +  [33mid[39m=[32m"mui-autocomplete-34704"[39m
      +  [33mspellcheck[39m=[32m"false"[39m
      +  [33mtype[39m=[32m"text"[39m
      +  [33mvalue[39m=[32m"one"[39m
      +[36m/>[39m
      
      at Context.<anonymous> (packages/material-ui-lab/src/Autocomplete/repro.test.js:25:5)
      at processImmediate (node:internal/timers:466:21)
```

**thinking:**

```
Found the bug: when the input retains a text selection on blur (from `selectOnFocus`), clicking the popup arrow opens the list but never focuses the input, so there's no blur event to close it on outside clicks. Fix: always focus the input on click, and only keep the select-on-first-click behavior conditional.


```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/mui__material-ui-19794/repo/packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js",
 "old_string": "  // Focus the input when first interacting with the combobox\n  const handleClick = () => {\n    if (\n      firstFocus.current &&\n      inputRef.current.selectionEnd - inputRef.current.selectionStart === 0\n    ) {\n      inputRef.current.focus();\n\n      if (selectOnFocus) {\n        inputRef.current.select();\n      }\n    }",
 "new_string": "  // Focus the input when interacting with the combobox\n  const handleClick = () => {\n    inputRef.current.focus();\n\n    if (\n      selectOnFocus &&\n      firstFocus.current &&\n      inputRef.current.selectionEnd - inputRef.current.selectionStart === 0\n    ) {\n      inputRef.current.select();\n    }"
}
```

tool result:

```
The file /work/mui__material-ui-19794/repo/packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
/work/mui__material-ui-19794/bin/envrun 'NODE_ENV=test timeout 500 node_modules/.bin/mocha packages/material-ui-lab/src/Autocomplete/repro.test.js packages/material-ui-lab/src/Autocomplete/Autocomplete.test.js packages/material-ui-lab/src/useAutocomplete/*.test.js 2>&1 | tail -30'
```

tool result:

```
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
```

**assistant:** I've applied the fix. My test command pointed at a file that doesn't exist, so I'm rerunning it with just the repro and the existing Autocomplete tests.

**tool call: Bash**

```bash
/work/mui__material-ui-19794/bin/envrun 'NODE_ENV=test timeout 500 node_modules/.bin/mocha packages/material-ui-lab/src/Autocomplete/repro.test.js packages/material-ui-lab/src/Autocomplete/Autocomplete.test.js 2>&1 | tail -30'
```

tool result:

```
Browserslist: caniuse-lite is outdated. Please run the following command: `yarn upgrade`
including inaccessible elements by default


  ․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․
  ․․․․․․․․․․

  66 passing (3s)
```

**assistant:** All pass (the background failure is just the earlier hung `yarn` invocation timing out). Cleaning up the repro file:

**tool call: Bash**

```bash
cd /work/mui__material-ui-19794/repo; rm packages/material-ui-lab/src/Autocomplete/repro.test.js; git status --short; git diff
```

tool result:

```
 M package.json
 M packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
diff --git a/package.json b/package.json
index 2678596db..8b4e1ca08 100644
--- a/package.json
+++ b/package.json
@@ -55,17 +55,20 @@
     "@testing-library/dom": "^6.8.1",
     "@testing-library/react": "^9.3.2",
     "@testing-library/react-hooks": "3.2.1",
-    "@types/chai": "^4.2.3",
-    "@types/chai-dom": "^0.0.8",
+    "@types/chai": "^5.2.2",
+    "@types/chai-dom": "^1.11.3",
     "@types/enzyme": "^3.10.3",
+    "@types/format-util": "^1.0.4",
     "@types/fs-extra": "^8.0.0",
     "@types/glob": "^7.1.1",
     "@types/jsdom": "^16.1.0",
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
@@ -104,7 +107,6 @@
     "fs-extra": "^8.1.0",
     "glob": "^7.1.2",
     "glob-gitignore": "^1.0.11",
-    "lodash": "^4.17.15",
     "jsdom": "^16.0.0",
     "karma": "^4.3.0",
     "karma-browserstack-launcher": "~1.4.0",
@@ -114,6 +116,7 @@
     "karma-sourcemap-loader": "^0.3.7",
     "karma-webpack": "^4.0.2",
     "lerna": "^3.16.4",
+    "lodash": "^4.17.15",
     "mocha": "^7.0.0",
     "node-fetch": "^ 2.6.0",
     "nyc": "^15.0.0",
diff --git a/packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js b/packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js
index 9957ed76d..a3a0f0052 100644
--- a/packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js
+++ b/packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js
@@ -767,17 +767,16 @@ export default function useAutocomplete(props) {
     }
   };
 
-  // Focus the input when first interacting with the combobox
+  // Focus the input when interacting with the combobox
   const handleClick = () => {
+    inputRef.current.focus();
+
     if (
+      selectOnFocus &&
       firstFocus.current &&
       inputRef.current.selectionEnd - inputRef.current.selectionStart === 0
     ) {
-      inputRef.current.focus();
-
-      if (selectOnFocus) {
-        inputRef.current.select();
-      }
+      inputRef.current.select();
     }
 
     firstFocus.current = false;
diff --git a/yarn.lock b/yarn.lock
index b08c4eac9..8ad2c845d 100644
--- a/yarn.lock
+++ b/yarn.lock
@@ -2085,18 +2085,25 @@
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
   version "4.2.9"
   resolved "https://registry.yarnpkg.com/@types/chai/-/chai-4.2.9.tgz#194332625ed2ae914aef00b8d5ca3b77e7924cc6"
   integrity sha512-NeXgZj+MFL4izGqA4sapdYzkzQG+MtGra9vhQ58dnmDY++VgJaRUws+aLVV5zRJCYJl/8s9IjMmhiUw1WsKSmw==
 
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
@@ -2114,6 +2121,11 @@
   resolved "https://registry.yarnpkg.com/@types/css-mediaquery/-/css-mediaquery-0.1.0.tgz#61d439d8163880e90b61d19aba24f7b778c4e77d"
   integrity sha512-jzZ9bRw8fTgCEllDvE7GHR1zTP5LsDHJbAX6BCwD9qdxIOq/Le5TTsdteoCIdEQaFpDMvudLHU/hLo1Lmfcy0Q==
 
+"@types/deep-eql@*":
+  version "4.0.2"
+  resolved "https://registry.yarnpkg.com/@types/deep-eql/-/deep-eql-4.0.2.tgz#334311971d3a07121e7eb91b684a605e7eea9cbd"
+  integrity sha512-c9h9dVVMigMPc4bwTvC5dxqtqJZwQPePsWjPlpSOnojbor6pGqdk541lfA7AqFQr5pB1BRdq0juY9db81BwyFw==
+
 "@types/enzyme@^3.10.3":
   version "3.10.5"
   resolved "https://registry.yarnpkg.com/@types/enzyme/-/enzyme-3.10.5.tgz#fe7eeba3550369eed20e7fb565bfb74eec44f1f0"
@@ -2132,6 +2144,11 @@
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
@@ -2240,6 +2257,11 @@
   resolved "https://registry.yarnpkg.com/@types/prop-types/-/prop-types-15.7.1.tgz#f1a11e7babb0c3cad68100be381d1e064c68f1f6"
   integrity sha512-CFzn9idOEpHrgdw8JsoTkaDDyRWk1jrzIV8djzcgpq0y9tG4B4lFT+Nxh52DVpDXV+n4+NPNv7M1Dj5uMp6XFg==
 
+"@types/prop-types@^15.7.15":
+  version "15.7.15"
+  resolved "https://registry.yarnpkg.com/@types/prop-types/-/prop-types-15.7.15.tgz#e6e5a86d602beaca7
[... 1834 more characters not shown]
```

**assistant:** I fixed it: the Autocomplete list now closes when you click outside it.

**Cause:** In `packages/material-ui-lab/src/useAutocomplete/useAutocomplete.js`, `handleClick` only focused the input if it had no text selected. But an input keeps its old selection after it loses focus, and with `selectOnFocus` the whole value is selected on focus. So this sequence breaks it:

1. Click into the input, so its text gets selected.
2. Click elsewhere to blur it.
3. Click the open arrow.

The arrow's mousedown is deliberately blocked so the input doesn't blur, the list opens, and `handleClick` skips focusing because the old selection is still there. The list is then open with nothing focused. It only closes when the input blurs, and a click outside never triggers that blur.

**Fix:** `handleClick` now always focuses the input. Only the select-all on first focus still depends on `selectOnFocus`, first focus, and there being no existing selection:

```js
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
```

**Verification:** I wrote a temporary test for the sequence above (select text, blur, click the arrow, check the input has focus, blur, check the list closed). It failed before the change and passed after. All 66 tests in `Autocomplete.test.js` plus that repro pass. I've deleted the repro file, so the only change is the one in `useAutocomplete.js`.

`git status` also shows changes to `package.json` and `yarn.lock`, and untracked `Dockerfile` and `custom-reporter.js`. I didn't make those (they look like the test environment's setup) and left them as they were.

_session end: success, turns 15, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 2.16 s: yarn -s mocha packages/material-ui-lab/src/Autocomplete/repro.test.js 2>&1 | tail -20
- `rc=0` 500.14 s: NODE_ENV=test timeout 500 node_modules/.bin/mocha packages/material-ui-lab/src/Autocomplete/repro.test.js 2>&1 | tail -30
- `rc=0` 1.53 s: NODE_ENV=test timeout 500 node_modules/.bin/mocha packages/material-ui-lab/src/Autocomplete/repro.test.js packages/material-ui-lab/src/Autocomplete/Autocomplete.test.js packages/material-ui-lab/src/useAutocomplete/*.test.js 2>&1 | tail -30
- `rc=124` 1200.01 s: yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/Autocomplete/repro.test.js 2>&1 | tail -20
- `rc=0` 500.14 s: NODE_ENV=test timeout 500 node_modules/.bin/mocha packages/material-ui-lab/src/Autocomplete/repro.test.js packages/material-ui-lab/src/Autocomplete/Autocomplete.test.js 2>&1 | tail -30
