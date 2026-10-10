# Instance: mui__material-ui-12406

- Final resolved (evaluator, logs/mui__material-ui-12406_result.json): True
- Run state: DONE
- One attempt. Duration 55.4 s, turns 12, actor cost $0.21420979999999998, container commands 4
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/mui__material-ui-12406/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-12406/repo. Consider the following issue description:

<issue_description>
1.4.1 Texfield multiline jest snapshot tests broken
When upgrading to 1.4.1 all our snapshot tests including a `<TextField multiline />` are broken due to `Error: Uncaught [TypeError: Cannot read property 'scrollHeight' of null]`.
We had similar issues in the past which were related to refs + react-test-renderer, but I couldn't spot any change in 1.4.1 yet which changed the ref logic.

- related #5531
<!-- Checked checkbox should look like this: [x] -->
- [x] This is a v1.x issue. <!-- (v0.x is no longer maintained) -->
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Expected Behavior
minor version jump shouldn't break testing setup

## Current Behavior
testing setup is broken

## Steps to Reproduce
Snapshot `<TextField multiline {...props} />` via jest.

## Context
We render snapshots of all our pages to spot changes on component updates.

## Your Environment
| Tech         | Version |
|--------------|---------|
| Material-UI  | v1.4.1  |
| React        |   latest      |


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-12406/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-12406/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-12406/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-12406/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cat packages/material-ui/src/Input/Textarea.js
```

tool result:

```
import React from 'react';
import PropTypes from 'prop-types';
import classnames from 'classnames';
import debounce from 'debounce'; // < 1kb payload overhead when lodash/debounce is > 3kb.
import EventListener from 'react-event-listener';
import withStyles from '../styles/withStyles';

const ROWS_HEIGHT = 19;

export const styles = {
  /* Styles applied to the root element. */
  root: {
    position: 'relative', // because the shadow has position: 'absolute',
    width: '100%',
  },
  textarea: {
    width: '100%',
    height: '100%',
    resize: 'none',
    font: 'inherit',
    padding: 0,
    cursor: 'inherit',
    boxSizing: 'border-box',
    lineHeight: 'inherit',
    border: 'none',
    outline: 'none',
    background: 'transparent',
  },
  shadow: {
    // Overflow also needed to here to remove the extra row
    // added to textareas in Firefox.
    overflow: 'hidden',
    // Visibility needed to hide the extra text area on ipads
    visibility: 'hidden',
    position: 'absolute',
    height: 'auto',
    whiteSpace: 'pre-wrap',
  },
};

/**
 * @ignore - internal component.
 */
class Textarea extends React.Component {
  isControlled = this.props.value != null;

  shadowRef = null;

  singlelineShadowRef = null;

  inputRef = null;

  value = null;

  handleResize = debounce(() => {
    this.syncHeightWithShadow();
  }, 166); // Corresponds to 10 frames at 60 Hz.

  constructor(props) {
    super(props);

    // <Input> expects the components it renders to respond to 'value'
    // so that it can check whether they are filled.
    this.value = props.value || props.defaultValue || '';
    this.state = {
      height: Number(props.rows) * ROWS_HEIGHT,
    };
  }

  state = {
    height: null,
  };

  componentDidMount() {
    this.syncHeightWithShadow();
  }

  componentDidUpdate() {
    this.syncHeightWithShadow();
  }

  componentWillUnmount() {
    this.handleResize.clear();
  }

  handleRefInput = ref => {
    this.inputRef = ref;

    const { textareaRef } = this.props;
    if (textareaRef) {
      if (typeof textareaRef === 'function') {
        textareaRef(ref);
      } else {
        textareaRef.current = ref;
      }
    }
  };

  handleRefSinglelineShadow = ref => {
    this.singlelineShadowRef = ref;
  };

  handleRefShadow = ref => {
    this.shadowRef = ref;
  };

  handleChange = event => {
    this.value = event.target.value;

    if (!this.isControlled) {
      // The component is not controlled, we need to update the shallow value.
      this.shadowRef.value = this.value;
      this.syncHeightWithShadow();
    }

    if (this.props.onChange) {
      this.props.onChange(event);
    }
  };

  syncHeightWithShadow() {
    const props = this.props;

    if (this.isControlled) {
      // The component is controlled, we need to update the shallow value.
      this.shadowRef.value = props.value == null ? '' : String(props.value);
    }

    const lineHeight = this.singlelineShadowRef.scrollHeight;
    let newHeight = this.shadowRef.scrollHeight;

    // Guarding for jsdom, where scrollHeight isn't present.
    // See https://github.com/tmpvar/jsdom/issues/1013
    if (newHeight === undefined) {
      return;
    }

    if (Number(props.rowsMax) >= Number(props.rows)) {
      newHeight = Math.min(Number(props.rowsMax) * lineHeight, newHeight);
    }

    newHeight = Math.max(newHeight, lineHeight);

    // Need a large enough different to update the height.
    // This prevents infinite rendering loop.
    if (Math.abs(this.state.height - newHeight) > 1) {
      this.setState({
        height: newHeight,
      });
    }
  }

  render() {
    const {
      classes,
      className,
      defaultValue,
      onChange,
      rows,
      rowsMax,
      textareaRef,
      value,
      ...other
    } = this.props;

    return (
      <div className={classes.root} style={{ height: this.state.height }}>
        <EventListener target="window" onResize={this.handleResize} />
        <textarea
          aria-hidden="true"
          className={classnames(classes.textarea, classes.shadow)}
          readOnly
          ref={this.handleRefSinglelineShadow}
          rows="1"
          tabIndex={-1}
          value=""
        />
        <textarea
          aria-hidden="true"
          className={classnames(classes.textarea, classes.shadow)}
          defaultValue={defaultValue}
          readOnly
          ref={this.handleRefShadow}
          rows={rows}
          tabIndex={-1}
          value={value}
        />
        <textarea
          rows={rows}
          className={classnames(classes.textarea, className)}
          defaultValue={defaultValue}
          value={value}
          onChange={this.handleChange}
          ref={this.handleRefInput}
          {...other}
        />
      </div>
    );
  }
}

Textarea.propTypes = {
  /**
   * Override or extend the styles applied to the component.
   * See [CSS API](#css-api) below for more details.
   */
  classes: PropTypes.object.isRequired,
  /**
   * @ignore
   */
  className: PropTypes.string,
  /**
   * @ignore
   */
  defaultValue: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  /**
   * @ignore
   */
  disabled: PropTypes.bool,
  /**
   * @ignore
   */
  onChange: PropTypes.func,
  /**
   * Number of rows to display when multiline option is set to true.
   */
  rows: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  /**
   * Maximum number of rows to display when multiline option is set to true.
   */
  rowsMax: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  /**
   * Use that property to pass a ref callback to the native textarea element.
   */
  textareaRef: PropTypes.oneOfType([PropTypes.func, PropTypes.object]),
  /**
   * @ignore
   */
  value: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
};

Textarea.defaultProps = {
  rows: 1,
};

export default withStyles(styles)(Textarea);
```

**tool call: Bash**

```bash
cd packages/material-ui/src/Input; git log --oneline -3; grep -n "renderer\|null\|shadowRef" Textarea.test.js | head -30
```

tool result:

```
cbc6828c9 [MobileStepper] Add a LinearProgressProps property (#12404)
81c8d84e4 [docs] Add Tomahawk boilerplate to the related projects (#12393)
f6036ed61 [palette] Better defensive logic (#12402)
13:  wrapper.instance().shadowRef = textareaShadowRef;
78:      instance.shadowRef = { scrollHeight: 19 };
81:      instance.shadowRef = { scrollHeight: 48 };
91:      instance.shadowRef = { scrollHeight: lineHeight * 5 };
```

**assistant:** Let me reproduce with react-test-renderer.

**tool call: Bash**

```bash
cd /work/mui__material-ui-12406/repo; cat > packages/material-ui/src/Input/repro.test.js <<'EOF'
import React from 'react';
import { assert } from 'chai';
import TestRenderer from 'react-test-renderer';
import Textarea from './Textarea';

describe('repro', () => {
  it('uncontrolled', () => {
    const r = TestRenderer.create(<Textarea />);
    assert.ok(r.toJSON());
  });
  it('controlled', () => {
    const r = TestRenderer.create(<Textarea value="a" onChange={() => {}} />);
    r.update(<Textarea value="ab" onChange={() => {}} />);
    assert.ok(r.toJSON());
  });
});
EOF
../bin/envrun 'ls node_modules | grep react-test; cat package.json | grep "\"test:unit"'
```

tool result:

```
react-test-renderer
    "test:unit": "cross-env NODE_ENV=test mocha packages/material-ui/test/**/*.test.js packages/material-ui/src/{,**/}*.test.js docs/src/**/*.test.js",
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-12406/repo; ../bin/envrun 'NODE_ENV=test npx mocha packages/material-ui/src/Input/repro.test.js 2>&1 | tail -30'
```

tool result:

```
      at reportException (node_modules/jsdom/lib/jsdom/living/helpers/runtime-script-errors.js:70:28)
      at invokeEventListeners (node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:209:9)
      at HTMLUnknownElementImpl._dispatch (node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:119:9)
      at HTMLUnknownElementImpl.dispatchEvent (node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:82:17)
      at HTMLUnknownElementImpl.dispatchEvent (node_modules/jsdom/lib/jsdom/living/nodes/HTMLElement-impl.js:30:27)
      at HTMLUnknownElement.dispatchEvent (node_modules/jsdom/lib/jsdom/living/generated/EventTarget.js:157:21)
      at Object.invokeGuardedCallbackDev (node_modules/react-test-renderer/cjs/react-test-renderer.development.js:1937:16)
      at invokeGuardedCallback (node_modules/react-test-renderer/cjs/react-test-renderer.development.js:1986:29)
      at commitRoot (node_modules/react-test-renderer/cjs/react-test-renderer.development.js:7681:7)
      at completeRoot (node_modules/react-test-renderer/cjs/react-test-renderer.development.js:8650:34)
      at performWorkOnRoot (node_modules/react-test-renderer/cjs/react-test-renderer.development.js:8595:9)
      at performWork (node_modules/react-test-renderer/cjs/react-test-renderer.development.js:8527:7)
      at performSyncWork (node_modules/react-test-renderer/cjs/react-test-renderer.development.js:8499:3)
      at requestWork (node_modules/react-test-renderer/cjs/react-test-renderer.development.js:8399:5)
      at scheduleWork (node_modules/react-test-renderer/cjs/react-test-renderer.development.js:8274:11)
      at scheduleRootUpdate (node_modules/react-test-renderer/cjs/react-test-renderer.development.js:8739:3)
      at updateContainerAtExpirationTime (node_modules/react-test-renderer/cjs/react-test-renderer.development.js:8766:10)
      at updateContainer (node_modules/react-test-renderer/cjs/react-test-renderer.development.js:8777:10)
      at Object.create (node_modules/react-test-renderer/cjs/react-test-renderer.development.js:9260:5)
      at Context.<anonymous> (packages/material-ui/src/Input/repro.test.js:8:28)
      at processImmediate (node:internal/timers:466:21)

  2) repro
       controlled:
     AssertionError: expected null to be truthy
      at Context.<anonymous> (packages/material-ui/src/Input/repro.test.js:14:12)
      at processImmediate (node:internal/timers:466:21)
```

**assistant:** Reproduced. Now I'll fix it by making `syncHeightWithShadow` do nothing when the shadow refs are missing, which is what happens under react-test-renderer:

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/mui__material-ui-12406/repo/packages/material-ui/src/Input/Textarea.js",
 "old_string": "    const props = this.props;\n\n    if (this.isControlled) {",
 "new_string": "    const props = this.props;\n\n    // Guarding for **broken** shallow rendering method that call componentDidMount\n    // but doesn't handle refs correctly.\n    // To remove once the shallow rendering has been fixed.\n    if (!this.shadowRef) {\n      return;\n    }\n\n    if (this.isControlled) {"
}
```

tool result:

```
The file /work/mui__material-ui-12406/repo/packages/material-ui/src/Input/Textarea.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/mui__material-ui-12406/repo/packages/material-ui/src/Input/Textarea.js",
 "old_string": "      this.shadowRef.value = this.value;\n      this.syncHeightWithShadow();",
 "new_string": "      if (this.shadowRef) {\n        this.shadowRef.value = this.value;\n      }\n      this.syncHeightWithShadow();"
}
```

tool result:

```
The file /work/mui__material-ui-12406/repo/packages/material-ui/src/Input/Textarea.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-12406/repo; sed -n 1,110p packages/material-ui/src/Input/Textarea.test.js
```

tool result:

```
import React from 'react';
import { assert } from 'chai';
import { spy, useFakeTimers } from 'sinon';
import { createShallow, createMount, unwrap } from '../test-utils';
import Textarea from './Textarea';

function assignRefs(wrapper) {
  // refs don't work with shallow renders in enzyme so here we directly define
  // 'this.input', 'this.shadow', etc. for this Textarea via wrapper.instance()
  const inputRef = wrapper.find('textarea').last();
  wrapper.instance().inputRef = inputRef;
  const textareaShadowRef = wrapper.find('textarea').at(2);
  wrapper.instance().shadowRef = textareaShadowRef;
  const singlelineShadowRef = wrapper.find('textarea').first();
  wrapper.instance().singlelineShadowRef = singlelineShadowRef;

  return {
    inputRef,
    singlelineShadowRef,
    textareaShadowRef,
  };
}

const TextareaNaked = unwrap(Textarea);

describe('<Textarea />', () => {
  let shallow;
  let mount;

  before(() => {
    shallow = createShallow({ disableLifecycleMethods: true });
    mount = createMount();
  });

  after(() => {
    mount.cleanUp();
  });

  it('should render 3 textareas', () => {
    const wrapper = shallow(<TextareaNaked classes={{}} />);
    assert.strictEqual(wrapper.find('textarea').length, 3);
  });

  it('should change its height when the height of its shadows changes', () => {
    const wrapper = shallow(<TextareaNaked classes={{}} />);
    assert.strictEqual(wrapper.state().height, 19);

    const refs = assignRefs(wrapper);

    // jsdom doesn't support scroll height so we have to simulate it changing
    // which makes this not so great of a test :(
    refs.textareaShadowRef.scrollHeight = 43;
    refs.singlelineShadowRef.scrollHeight = 43;
    // this is needed to trigger the resize
    refs.inputRef.simulate('change', { target: { value: 'x' } });
    assert.strictEqual(wrapper.state().height, 43);

    refs.textareaShadowRef.scrollHeight = 19;
    refs.singlelineShadowRef.scrollHeight = 19;
    refs.inputRef.simulate('change', { target: { value: '' } });
    assert.strictEqual(wrapper.state().height, 19);
  });

  describe('height behavior', () => {
    let wrapper;

    beforeEach(() => {
      wrapper = mount(<TextareaNaked classes={{}} value="f" />);
    });

    afterEach(() => {
      wrapper.unmount();
    });

    it('should update the height when the value change', () => {
      const instance = wrapper.instance();
      instance.singlelineShadowRef = { scrollHeight: 19 };
      instance.shadowRef = { scrollHeight: 19 };
      wrapper.setProps({ value: 'fo' });
      assert.strictEqual(wrapper.state().height, 19);
      instance.shadowRef = { scrollHeight: 48 };
      wrapper.setProps({ value: 'foooooo' });
      assert.strictEqual(wrapper.state().height, 48);
    });

    it('should respect the rowsMax property', () => {
      const instance = wrapper.instance();
      const rowsMax = 4;
      const lineHeight = 19;
      instance.singlelineShadowRef = { scrollHeight: lineHeight };
      instance.shadowRef = { scrollHeight: lineHeight * 5 };
      wrapper.setProps({ rowsMax });
      assert.strictEqual(wrapper.state().height, lineHeight * rowsMax);
    });
  });

  it('should set filled', () => {
    const wrapper = shallow(<TextareaNaked classes={{}} />);
    assert.strictEqual(wrapper.find('textarea').length, 3);

    const refs = assignRefs(wrapper);
    // this is needed to trigger the resize
    refs.inputRef.simulate('change', { target: { value: 'x' } });
    assert.strictEqual(wrapper.instance().value, 'x');
    // this is needed to trigger the resize
    refs.inputRef.simulate('change', { target: { value: '' } });
    assert.strictEqual(wrapper.instance().value, '');
  });

  describe('prop: textareaRef', () => {
```

**assistant:** Tests always assign both refs together, so a `shadowRef` guard covers the missing-ref case. Now I'll rerun the reproduction and the existing Input tests:

**tool call: Bash**

```bash
cd /work/mui__material-ui-12406/repo; ../bin/envrun 'NODE_ENV=test npx mocha packages/material-ui/src/Input/repro.test.js packages/material-ui/src/Input/*.test.js packages/material-ui/src/TextField/*.test.js 2>&1 | tail -15'
```

tool result:

```
      at Object.install (node_modules/lolex/src/lolex-src.js:808:21)
      at exports.useFakeTimers (node_modules/sinon/lib/sinon/util/fake_timers.js:26:21)
      at useFakeTimers (node_modules/sinon/lib/sinon/sandbox.js:331:46)
      at Context.<anonymous> (packages/material-ui/src/Input/Textarea.test.js:137:15)
      at processImmediate (node:internal/timers:466:21)

  2) <Textarea />
       resize
         "after all" hook:
     TypeError: Cannot read properties of undefined (reading 'restore')
      at Context.<anonymous> (packages/material-ui/src/Input/Textarea.test.js:141:13)
      at processImmediate (node:internal/timers:466:21)
```

**assistant:** Two tests fail. I'll check the full summary and whether these failures already happen without my change:

**tool call: Bash**

```bash
cd /work/mui__material-ui-12406/repo; ../bin/envrun 'NODE_ENV=test npx mocha packages/material-ui/src/Input/repro.test.js packages/material-ui/src/Input/*.test.js packages/material-ui/src/TextField/*.test.js 2>&1 | grep -E "passing|failing|^  [0-9]\)" -A3 | head -30; git stash -q; NODE_ENV=test npx mocha packages/material-ui/src/Input/Textarea.test.js 2>&1 | grep -E "passing|failing"; git stash pop -q; git status --short'
```

tool result:

```
  84 passing (393ms)
  2 failing

  1) <Textarea />
       resize
         "before all" hook:
     TypeError: Cannot assign to read only property 'now' of object '#<Performance>'
--
  2) <Textarea />
       resize
         "after all" hook:
     TypeError: Cannot read properties of undefined (reading 'restore')
  8 passing (235ms)
  2 failing
 M package.json
 M packages/material-ui/src/Input/Textarea.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
?? packages/material-ui/src/Input/repro.test.js
```

**thinking:**

```
These two failures are pre-existing and unrelated to my fix—they're caused by sinon's fake timers conflicting with the container's Node version. My reproduction tests and all other Input/TextField tests pass, so I'll clean up now.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-12406/repo; rm packages/material-ui/src/Input/repro.test.js; git diff packages/material-ui/src/Input/Textarea.js
```

tool result:

```
diff --git a/packages/material-ui/src/Input/Textarea.js b/packages/material-ui/src/Input/Textarea.js
index 8dfa1a7ae..cc34203af 100644
--- a/packages/material-ui/src/Input/Textarea.js
+++ b/packages/material-ui/src/Input/Textarea.js
@@ -109,7 +109,9 @@ class Textarea extends React.Component {
 
     if (!this.isControlled) {
       // The component is not controlled, we need to update the shallow value.
-      this.shadowRef.value = this.value;
+      if (this.shadowRef) {
+        this.shadowRef.value = this.value;
+      }
       this.syncHeightWithShadow();
     }
 
@@ -121,6 +123,13 @@ class Textarea extends React.Component {
   syncHeightWithShadow() {
     const props = this.props;
 
+    // Guarding for **broken** shallow rendering method that call componentDidMount
+    // but doesn't handle refs correctly.
+    // To remove once the shallow rendering has been fixed.
+    if (!this.shadowRef) {
+      return;
+    }
+
     if (this.isControlled) {
       // The component is controlled, we need to update the shallow value.
       this.shadowRef.value = props.value == null ? '' : String(props.value);
```

**assistant:** Let me make the comment accurate about the cause:

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/mui__material-ui-12406/repo/packages/material-ui/src/Input/Textarea.js",
 "old_string": "    // Guarding for **broken** shallow rendering method that call componentDidMount\n    // but doesn't handle refs correctly.\n    // To remove once the shallow rendering has been fixed.",
 "new_string": "    // Guarding for renderers that call componentDidMount but don't attach refs,\n    // e.g. react-test-renderer used for jest snapshots."
}
```

tool result:

```
The file /work/mui__material-ui-12406/repo/packages/material-ui/src/Input/Textarea.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**assistant:** I fixed the crash: snapshotting a `<TextField multiline />` with react-test-renderer no longer throws `Cannot read property 'scrollHeight' of null`.

**Cause:** react-test-renderer doesn't create real DOM elements, so the ref callbacks get `null`. `Textarea` still measures its hidden "shadow" textareas when it mounts and updates (`componentDidMount` / `componentDidUpdate` call `syncHeightWithShadow`), so it read `scrollHeight` from a missing element.

**Fix** (only `packages/material-ui/src/Input/Textarea.js` changed):
- `syncHeightWithShadow()` now returns early if `this.shadowRef` isn't set. It keeps the starting height from the `rows` prop instead of measuring.
- `handleChange` only copies the value into the shadow textarea if the ref exists.

**Testing:** I wrote a temporary test that rendered `Textarea` with react-test-renderer, both uncontrolled and controlled with a value update.
- Before the fix, the uncontrolled case crashed with the error from the issue, and the controlled render came back empty (`toJSON()` returned `null`).
- After the fix, both pass, and so do the existing Input and TextField tests except two.
- Those two are in `Textarea.test.js`, in the setup and teardown hooks of the `resize` group: `Cannot assign to read only property 'now' of object '#<Performance>'`. They fail the same way with my change removed. sinon's fake timers can't replace `performance.now` on the container's Node version, so the tests inside that group didn't run in this environment.

I deleted the temporary test. `git status` also shows changes I didn't make, which look like test-environment setup: `package.json` and `yarn.lock` modified, plus untracked `Dockerfile` and `custom-reporter.js`. I left those alone.

_session end: success, turns 12, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.16 s: ls node_modules | grep react-test; cat package.json | grep "\"test:unit"
- `rc=0` 3.32 s: NODE_ENV=test npx mocha packages/material-ui/src/Input/repro.test.js 2>&1 | tail -30
- `rc=0` 5.75 s: NODE_ENV=test npx mocha packages/material-ui/src/Input/repro.test.js packages/material-ui/src/Input/*.test.js packages/material-ui/src/TextField/*.test.js 2>&1 | tail -15
- `rc=0` 8.43 s: NODE_ENV=test npx mocha packages/material-ui/src/Input/repro.test.js packages/material-ui/src/Input/*.test.js packages/material-ui/src/TextField/*.test.js 2>&1 | grep -E "passing|failing|^  [0-9]\)" -A3 | head -30; git stash -q; NODE_ENV=test npx mocha packages/material-ui/src/Input/Textarea.test.js 2>&1 | grep -E "passing|failing"; git stash pop -q; git status --short
