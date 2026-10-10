# Instance: mui__material-ui-14496

- Final resolved (evaluator, logs/mui__material-ui-14496_result.json): True
- Run state: DONE
- One attempt. Duration 478.1 s, turns 19, actor cost $0.3437438, container commands 10
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/mui__material-ui-14496/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-14496/repo. Consider the following issue description:

<issue_description>
[Tooltip] Tooltips aren't displayed on focus on TextFields
- [x] This is not a v0.x issue. <!-- (v0.x is no longer maintained) -->
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Expected Behavior 🤔
Using a `Tooltip` component with `disableHoverListener` around a `TextField` component should display the tooltip on focus

## Current Behavior 😯
No tooltip is displayed

## Steps to Reproduce 🕹
Link: https://codesandbox.io/s/ooywx0xlq9

1. Click on the TextField, nothing is displayed.

Testing anywhere the following code sample is enough to reproduce :
```js
<Tooltip title="TestTooltip" disableHoverListener>
  <TextField label="TestTooltip" />
</Tooltip>
```

## Context 🔦
Display hints for user entering their data.

This used to work, and, after trying a few versions, appears to be broken starting v3.1.1

## Your Environment 🌎

| Tech         | Version |
|--------------|---------|
| Material-UI  | v3.9.2  |
| React        | 16.6.3 |
| Browser      | Firefox 66b, Chromium 71 |

As always, thanks for the great project :slightly_smiling_face: 

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-14496/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-14496/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-14496/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-14496/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cat packages/material-ui/src/Tooltip/Tooltip.js | sed -n 1,260p
```

tool result:

```
import React from 'react';
import PropTypes from 'prop-types';
import warning from 'warning';
import classNames from 'classnames';
import { componentPropType } from '@material-ui/utils';
import RootRef from '../RootRef';
import withStyles from '../styles/withStyles';
import { capitalize } from '../utils/helpers';
import Grow from '../Grow';
import Popper from '../Popper';

export const styles = theme => ({
  /* Styles applied to the Popper component. */
  popper: {
    zIndex: theme.zIndex.tooltip,
    opacity: 0.9,
    pointerEvents: 'none',
  },
  /* Styles applied to the Popper component if `interactive={true}`. */
  popperInteractive: {
    pointerEvents: 'auto',
  },
  /* Styles applied to the tooltip (label wrapper) element. */
  tooltip: {
    backgroundColor: theme.palette.grey[700],
    borderRadius: theme.shape.borderRadius,
    color: theme.palette.common.white,
    fontFamily: theme.typography.fontFamily,
    padding: '4px 8px',
    fontSize: theme.typography.pxToRem(10),
    lineHeight: `${theme.typography.round(14 / 10)}em`,
    maxWidth: 300,
  },
  /* Styles applied to the tooltip (label wrapper) element if the tooltip is opened by touch. */
  touch: {
    padding: '8px 16px',
    fontSize: theme.typography.pxToRem(14),
    lineHeight: `${theme.typography.round(16 / 14)}em`,
  },
  /* Styles applied to the tooltip (label wrapper) element if `placement` contains "left". */
  tooltipPlacementLeft: {
    transformOrigin: 'right center',
    margin: '0 24px ',
    [theme.breakpoints.up('sm')]: {
      margin: '0 14px',
    },
  },
  /* Styles applied to the tooltip (label wrapper) element if `placement` contains "right". */
  tooltipPlacementRight: {
    transformOrigin: 'left center',
    margin: '0 24px',
    [theme.breakpoints.up('sm')]: {
      margin: '0 14px',
    },
  },
  /* Styles applied to the tooltip (label wrapper) element if `placement` contains "top". */
  tooltipPlacementTop: {
    transformOrigin: 'center bottom',
    margin: '24px 0',
    [theme.breakpoints.up('sm')]: {
      margin: '14px 0',
    },
  },
  /* Styles applied to the tooltip (label wrapper) element if `placement` contains "bottom". */
  tooltipPlacementBottom: {
    transformOrigin: 'center top',
    margin: '24px 0',
    [theme.breakpoints.up('sm')]: {
      margin: '14px 0',
    },
  },
});

class Tooltip extends React.Component {
  ignoreNonTouchEvents = false;

  constructor(props) {
    super();
    this.isControlled = props.open != null;
    this.state = {
      open: null,
    };

    if (!this.isControlled) {
      // not controlled, use internal state
      this.state.open = false;
    }
  }

  componentDidMount() {
    warning(
      !this.childrenRef.disabled ||
        (this.childrenRef.disabled && this.props.title === '') ||
        this.childrenRef.tagName.toLowerCase() !== 'button',
      [
        'Material-UI: you are providing a disabled `button` child to the Tooltip component.',
        'A disabled element does not fire events.',
        "Tooltip needs to listen to the child element's events to display the title.",
        '',
        'Place a `div` container on top of the element.',
      ].join('\n'),
    );

    // Fallback to this default id when possible.
    // Use the random value for client side rendering only.
    // We can't use it server-side.
    this.defaultId = `mui-tooltip-${Math.round(Math.random() * 1e5)}`;

    // Rerender with this.defaultId and this.childrenRef.
    if (this.props.open) {
      this.forceUpdate();
    }
  }

  componentWillUnmount() {
    clearTimeout(this.closeTimer);
    clearTimeout(this.enterTimer);
    clearTimeout(this.focusTimer);
    clearTimeout(this.leaveTimer);
    clearTimeout(this.touchTimer);
  }

  onRootRef = ref => {
    this.childrenRef = ref;
  };

  handleFocus = event => {
    event.persist();
    // The autoFocus of React might trigger the event before the componentDidMount.
    // We need to account for this eventuality.
    this.focusTimer = setTimeout(() => {
      // We need to make sure the focus hasn't moved since the event was triggered.
      if (this.childrenRef === document.activeElement) {
        this.handleEnter(event);
      }
    });

    const childrenProps = this.props.children.props;
    if (childrenProps.onFocus) {
      childrenProps.onFocus(event);
    }
  };

  handleEnter = event => {
    const { children, enterDelay } = this.props;
    const childrenProps = children.props;

    if (event.type === 'mouseover' && childrenProps.onMouseOver) {
      childrenProps.onMouseOver(event);
    }

    if (this.ignoreNonTouchEvents && event.type !== 'touchstart') {
      return;
    }

    // Remove the title ahead of time.
    // We don't want to wait for the next render commit.
    // We would risk displaying two tooltips at the same time (native + this one).
    this.childrenRef.setAttribute('title', '');

    clearTimeout(this.enterTimer);
    clearTimeout(this.leaveTimer);
    if (enterDelay) {
      event.persist();
      this.enterTimer = setTimeout(() => {
        this.handleOpen(event);
      }, enterDelay);
    } else {
      this.handleOpen(event);
    }
  };

  handleOpen = event => {
    // The mouseover event will trigger for every nested element in the tooltip.
    // We can skip rerendering when the tooltip is already open.
    // We are using the mouseover event instead of the mouseenter event to fix a hide/show issue.
    if (!this.isControlled && !this.state.open) {
      this.setState({ open: true });
    }

    if (this.props.onOpen) {
      this.props.onOpen(event);
    }
  };

  handleLeave = event => {
    const { children, leaveDelay } = this.props;
    const childrenProps = children.props;

    if (event.type === 'blur' && childrenProps.onBlur) {
      childrenProps.onBlur(event);
    }

    if (event.type === 'mouseleave' && childrenProps.onMouseLeave) {
      childrenProps.onMouseLeave(event);
    }

    clearTimeout(this.enterTimer);
    clearTimeout(this.leaveTimer);
    if (l
[... 1401 more characters not shown]
```

**tool call: Bash**

```bash
grep -n "focus\|activeElement" -i packages/material-ui/src/Tooltip/Tooltip.test.js | head -40
```

tool result:

```
127:    childrenRef.focus();
128:    children.simulate('focus', { type: 'focus', persist });
146:      childrenRef.focus();
147:      children.simulate('focus', { type: 'focus', persist });
158:      childrenRef.focus();
159:      children.simulate('focus', { type: 'focus', persist });
180:      childrenRef.focus();
181:      assert.strictEqual(document.activeElement, childrenRef);
191:      childrenRef.focus();
192:      assert.strictEqual(document.activeElement, childrenRef);
209:      'onFocus',
```

**tool call: Bash**

```bash
sed -n 1,60p packages/material-ui/src/Tooltip/Tooltip.test.js; sed -n 170,200p packages/material-ui/src/Tooltip/Tooltip.test.js; cat package.json | grep '"test'
```

tool result:

```
import React from 'react';
import { assert } from 'chai';
import { spy, useFakeTimers } from 'sinon';
import consoleErrorMock from 'test/utils/consoleErrorMock';
import { createShallow, createMount, getClasses, unwrap } from '@material-ui/core/test-utils';
import Popper from '../Popper';
import Tooltip from './Tooltip';
import createMuiTheme from '../styles/createMuiTheme';

function persist() {}

const TooltipNaked = unwrap(Tooltip);
const theme = createMuiTheme();

describe('<Tooltip />', () => {
  let shallow;
  let mount;
  let classes;
  let clock;
  const defaultProps = {
    children: <span>Hello World</span>,
    theme,
    title: 'Hello World',
  };

  before(() => {
    shallow = createShallow({ dive: true, disableLifecycleMethods: true });
    mount = createMount();
    classes = getClasses(<Tooltip {...defaultProps} />);
    clock = useFakeTimers();
  });

  after(() => {
    clock.restore();
    mount.cleanUp();
  });

  it('should render the correct structure', () => {
    const wrapper = shallow(<Tooltip {...defaultProps} />);
    assert.strictEqual(wrapper.type(), React.Fragment);
    assert.strictEqual(wrapper.childAt(0).name(), 'RootRef');
    assert.strictEqual(wrapper.childAt(1).name(), 'Popper');
    assert.strictEqual(wrapper.childAt(1).hasClass(classes.popper), true);
  });

  describe('prop: disableHoverListener', () => {
    it('should hide the native title', () => {
      const wrapper = shallow(
        <Tooltip {...defaultProps} title="Hello World" disableHoverListener>
          <button type="submit">Hello World</button>
        </Tooltip>,
      );

      const children = wrapper.find('button');
      assert.strictEqual(children.props().title, null);
    });
  });

  describe('prop: title', () => {
    it('should display if the title is present', () => {
    it('should mount without any issue', () => {
      mount(<Tooltip {...defaultProps} open />);
    });
  });

  describe('prop: delay', () => {
    it('should take the enterDelay into account', () => {
      const wrapper = mount(<TooltipNaked classes={{}} enterDelay={111} {...defaultProps} />);
      const childrenRef = wrapper.instance().childrenRef;
      childrenRef.tabIndex = 0;
      childrenRef.focus();
      assert.strictEqual(document.activeElement, childrenRef);
      assert.strictEqual(wrapper.state().open, false);
      clock.tick(111);
      assert.strictEqual(wrapper.state().open, true);
    });

    it('should take the leaveDelay into account', () => {
      const wrapper = mount(<TooltipNaked classes={{}} leaveDelay={111} {...defaultProps} />);
      const childrenRef = wrapper.instance().childrenRef;
      childrenRef.tabIndex = 0;
      childrenRef.focus();
      assert.strictEqual(document.activeElement, childrenRef);
      clock.tick(0);
      assert.strictEqual(wrapper.state().open, true);
      childrenRef.blur();
      assert.strictEqual(wrapper.state().open, true);
      clock.tick(111);
      assert.strictEqual(wrapper.state().open, false);
    });
  });
    "test": "yarn lint && yarn typescript && yarn test:coverage",
    "test:coverage": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha 'packages/material-ui/**/*.test.js' 'packages/material-ui-utils/**/*.test.js' 'packages/material-ui-styles/**/*.test.js' --exclude '**/node_modules/**' && nyc report -r lcovonly",
    "test:coverage:html": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha 'packages/material-ui/**/*.test.js' 'packages/material-ui-utils/**/*.test.js' 'packages/material-ui-styles/**/*.test.js' --exclude '**/node_modules/**' && nyc report --reporter=html",
    "test:karma": "cross-env NODE_ENV=test karma start test/karma.conf.js --single-run",
    "test:regressions": "webpack --config test/regressions/webpack.config.js && rimraf test/regressions/screenshots/chrome/* && vrtest run --config test/vrtest.config.js --record",
    "test:umd": "yarn babel-node packages/material-ui/test/umd/run.js",
    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/*.test.js' 'docs/**/*.test.js' --exclude '**/node_modules/**'",
    "test:watch": "yarn test:unit --watch",
```

**assistant:** Now a reproduction test with a wrapper element containing a focusable input:

**tool call: Bash**

```bash
cat > packages/material-ui/src/Tooltip/Repro.test.js <<'EOF'
import React from 'react';
import { assert } from 'chai';
import { useFakeTimers } from 'sinon';
import { createMount, unwrap } from '@material-ui/core/test-utils';
import Tooltip from './Tooltip';
import TextField from '../TextField';
import createMuiTheme from '../styles/createMuiTheme';

const TooltipNaked = unwrap(Tooltip);

describe('repro', () => {
  it('opens on focus of nested input', () => {
    const clock = useFakeTimers();
    const mount = createMount();
    const wrapper = mount(
      <TooltipNaked classes={{}} theme={createMuiTheme()} title="Hi" disableHoverListener>
        <TextField label="x" />
      </TooltipNaked>,
    );
    const input = wrapper.find('input');
    input.instance().focus();
    input.simulate('focus');
    clock.tick(0);
    assert.strictEqual(wrapper.state().open, true);
    clock.restore();
    mount.cleanUp();
  });
});
EOF
../bin/envrun 'NODE_ENV=test npx mocha packages/material-ui/src/Tooltip/Repro.test.js 2>&1 | tail -20'
```

tool result:

```
Command did not complete within its 120s timeout and was moved to the background (ID: bxwpl5i0q). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/adc84b68-18e5-43b0-9bc3-e1efbcd93681/tasks/bxwpl5i0q.output. You will be notified when it completes. To check interim output, use Read on that file path.
```

**tool call: Bash**

```bash
sleep 60; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/adc84b68-18e5-43b0-9bc3-e1efbcd93681/tasks/bxwpl5i0q.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
sleep 90; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/adc84b68-18e5-43b0-9bc3-e1efbcd93681/tasks/bxwpl5i0q.output; cat test/mocha.opts 2>/dev/null
```

tool result:

```
--require @babel/register
--reporter dot
--recursive
test/utils/setup.js
```

**tool call: Bash**

```bash
sleep 180; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/adc84b68-18e5-43b0-9bc3-e1efbcd93681/tasks/bxwpl5i0q.output
```

tool result:

```
Exit code 143
Command timed out after 2m 0s
```

**tool call: Bash**

```bash
cat /tmp/cell-scratch/claude-502/<actor-session-slug>/adc84b68-18e5-43b0-9bc3-e1efbcd93681/tasks/bxwpl5i0q.output; ../bin/envrun 'ps aux | grep -c mocha; ls node_modules/.bin/mocha'
```

tool result:

```
7
node_modules/.bin/mocha
```

**tool call: Bash**

```bash
../bin/envrun 'pkill -f mocha; NODE_ENV=test timeout 300 node_modules/.bin/mocha --exit packages/material-ui/src/Tooltip/Repro.test.js 2>&1 | tail -20'
```

tool result:

```
Exit code 143
```

**assistant:** The `pkill -f mocha` probably matched and killed its own shell. I'll run it again without that.

**tool call: Bash**

```bash
../bin/envrun 'NODE_ENV=test timeout 500 node_modules/.bin/mocha --exit packages/material-ui/src/Tooltip/Repro.test.js 2>&1 | tail -20'
```

tool result:

```
      at scheduleRootUpdate (node_modules/react-dom/cjs/react-dom.development.js:19391:3)
      at updateContainerAtExpirationTime (node_modules/react-dom/cjs/react-dom.development.js:19419:10)
      at updateContainer (node_modules/react-dom/cjs/react-dom.development.js:19476:10)
      at ReactRoot.render (node_modules/react-dom/cjs/react-dom.development.js:19771:3)
      at /testbed/node_modules/react-dom/cjs/react-dom.development.js:19911:14
      at unbatchedUpdates (node_modules/react-dom/cjs/react-dom.development.js:19274:10)
      at legacyRenderSubtreeIntoContainer (node_modules/react-dom/cjs/react-dom.development.js:19907:5)
      at Object.render (node_modules/react-dom/cjs/react-dom.development.js:19968:12)
      at getFiber (node_modules/enzyme-adapter-react-16/build/detectFiberTags.js:49:25)
      at detectFiberTags (node_modules/enzyme-adapter-react-16/build/detectFiberTags.js:101:17)
      at ReactSixteenAdapter.createMountRenderer (node_modules/enzyme-adapter-react-16/build/ReactSixteenAdapter.js:329:56)
      at ReactSixteenAdapter.createRenderer (node_modules/enzyme-adapter-react-16/build/ReactSixteenAdapter.js:588:25)
      at new ReactWrapper (node_modules/enzyme/build/ReactWrapper.js:132:30)
      at mount (node_modules/enzyme/build/mount.js:21:10)
      at mount (packages/material-ui/src/test-utils/createMount.js:14:12)
      at Context.mount (packages/material-ui/src/Tooltip/Repro.test.js:15:21)
      at processImmediate (node:internal/timers:466:21)
```

**tool call: Bash**

```bash
../bin/envrun 'NODE_ENV=test timeout 500 node_modules/.bin/mocha --exit packages/material-ui/src/Tooltip/Repro.test.js 2>&1 | grep -v "^      at" | head -30'
```

tool result:

```
Browserslist: caniuse-lite is outdated. Please run next command `yarn upgrade caniuse-lite browserslist`


  !

  0 passing (50ms)
  1 failing

  1) repro
       opens on focus of nested input:
     TypeError: performance.mark is not a function
```

**tool call: Bash**

```bash
sed -i '' "s/useFakeTimers()/useFakeTimers({ toFake: ['setTimeout', 'clearTimeout'] })/" packages/material-ui/src/Tooltip/Repro.test.js && ../bin/envrun 'NODE_ENV=test timeout 500 node_modules/.bin/mocha --exit packages/material-ui/src/Tooltip/Repro.test.js 2>&1 | grep -v "^      at" | head -30'
```

tool result:

```
Browserslist: caniuse-lite is outdated. Please run next command `yarn upgrade caniuse-lite browserslist`


  !

  0 passing (165ms)
  1 failing

  1) repro
       opens on focus of nested input:

      AssertionError: expected false to equal true
      + expected - actual

      -false
      +true
```

**thinking:**

```
Confirmed the bug: `handleFocus` in Tooltip.js only triggers when the ref element itself is focused, but for TextField the ref is the wrapper div while focus actually lands on the inner input. I'll fix this by checking whether focus is contained within the child element instead of requiring an exact match.


```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/mui__material-ui-14496/repo/packages/material-ui/src/Tooltip/Tooltip.js",
 "old_string": "      // We need to make sure the focus hasn't moved since the event was triggered.\n      if (this.childrenRef === document.activeElement) {",
 "new_string": "      // We need to make sure the focus hasn't moved since the event was triggered.\n      // The focus can be on a descendant of the children, e.g. the input of a TextField.\n      if (this.childrenRef && this.childrenRef.contains(document.activeElement)) {"
}
```

tool result:

```
The file /work/mui__material-ui-14496/repo/packages/material-ui/src/Tooltip/Tooltip.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
../bin/envrun 'NODE_ENV=test timeout 500 node_modules/.bin/mocha --exit packages/material-ui/src/Tooltip/Repro.test.js packages/material-ui/src/Tooltip/Tooltip.test.js 2>&1 | grep -v "^      at" | tail -30'
```

tool result:

```
     TypeError: performance.mark is not a function

  2) <Tooltip />
       prop: delay
         should take the enterDelay into account:
     Error: Method “instance” is meant to be run on 1 node. 0 found instead.

  3) <Tooltip />
       prop: delay
         should take the leaveDelay into account:
     Error: Method “instance” is meant to be run on 1 node. 0 found instead.

  4) <Tooltip />
       disabled button warning
         should raise a warning when we can listen to events:

      should call console.error
      + expected - actual

      -0
      +1
      

  5) <Tooltip />
       prop: interactive
         should keep the overlay open if the popper element is hovered:
     Error: Method “childAt” is meant to be run on 1 node. 0 found instead.
```

**assistant:** Running both files together interferes with the fake timers, so I'll run them separately and also check the existing tests without my fix (via `git stash`):

**tool call: Bash**

```bash
../bin/envrun 'for f in Repro Tooltip; do NODE_ENV=test timeout 500 node_modules/.bin/mocha --exit packages/material-ui/src/Tooltip/$f.test.js 2>&1 | grep -E "passing|failing"; done; git stash -q; NODE_ENV=test timeout 500 node_modules/.bin/mocha --exit packages/material-ui/src/Tooltip/Tooltip.test.js 2>&1 | grep -E "passing|failing"; git stash pop -q; git status --short'
```

tool result:

```
  1 passing (266ms)
  20 passing (179ms)
  6 failing
  20 passing (192ms)
  6 failing
 M package.json
 M packages/material-ui/src/Tooltip/Tooltip.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
?? packages/material-ui/src/Tooltip/Repro.test.js
```

**assistant:** My repro test passes now. `Tooltip.test.js` has the same 20 passing and 6 failing with and without my change. Checking what those failures are, and the unexpected `package.json`/`yarn.lock` changes:

**tool call: Bash**

```bash
../bin/envrun 'NODE_ENV=test timeout 500 node_modules/.bin/mocha --exit packages/material-ui/src/Tooltip/Tooltip.test.js 2>&1 | grep -E "^  [0-9]\)|^     [A-Z]" -A2 | head -40'; git diff --stat package.json yarn.lock
```

tool result:

```
  1) <Tooltip />
       mount
         should mount without any issue:
     TypeError: performance.mark is not a function
      at beginMark (node_modules/react-dom/cjs/react-dom.development.js:9019:15)
      at startWorkLoopTimer (node_modules/react-dom/cjs/react-dom.development.js:9277:5)
--
  2) <Tooltip />
       prop: delay
         should take the enterDelay into account:
     TypeError: Cannot read properties of null (reading '_reactInternalFiber')
      at getFiber (node_modules/enzyme-adapter-react-16/build/detectFiberTags.js:50:15)
      at detectFiberTags (node_modules/enzyme-adapter-react-16/build/detectFiberTags.js:101:17)
--
  3) <Tooltip />
       prop: delay
         should take the leaveDelay into account:
     TypeError: Cannot read properties of null (reading '_reactInternalFiber')
      at getFiber (node_modules/enzyme-adapter-react-16/build/detectFiberTags.js:50:15)
      at detectFiberTags (node_modules/enzyme-adapter-react-16/build/detectFiberTags.js:101:17)
--
  4) <Tooltip />
       disabled button warning
         should not raise a warning if title is empty:
     TypeError: Cannot read properties of null (reading '_reactInternalFiber')
      at getFiber (node_modules/enzyme-adapter-react-16/build/detectFiberTags.js:50:15)
      at detectFiberTags (node_modules/enzyme-adapter-react-16/build/detectFiberTags.js:101:17)
--
  5) <Tooltip />
       disabled button warning
         should raise a warning when we can listen to events:
     TypeError: Cannot read properties of null (reading '_reactInternalFiber')
      at getFiber (node_modules/enzyme-adapter-react-16/build/detectFiberTags.js:50:15)
      at detectFiberTags (node_modules/enzyme-adapter-react-16/build/detectFiberTags.js:101:17)
--
  6) <Tooltip />
       prop: interactive
         should keep the overlay open if the popper element is hovered:
     TypeError: Cannot read properties of null (reading '_reactInternalFiber')
      at getFiber (node_modules/enzyme-adapter-react-16/build/detectFiberTags.js:50:15)

 package.json |  7 ++++++-
 yarn.lock    | 51 +++++++++++++++++++++++++++++++++++++++++++++------
 2 files changed, 51 insertions(+), 7 deletions(-)
```

**thinking:**

```
Those 6 failures are unrelated to my fix—they stem from sinon's `useFakeTimers()` also faking `performance`, which breaks React's `performance.mark`. I'll leave the existing package.json/yarn.lock changes as-is and instead run a temporary test copy that only fakes `setTimeout`/`clearTimeout` to properly exercise the focus/delay tests.


```

**tool call: Bash**

```bash
sed "s/useFakeTimers()/useFakeTimers({ toFake: ['setTimeout', 'clearTimeout'] })/" packages/material-ui/src/Tooltip/Tooltip.test.js > packages/material-ui/src/Tooltip/TmpCopy.test.js && ../bin/envrun 'NODE_ENV=test timeout 500 node_modules/.bin/mocha --exit packages/material-ui/src/Tooltip/TmpCopy.test.js 2>&1 | grep -E "passing|failing" -A6; NODE_ENV=test timeout 500 node_modules/.bin/eslint packages/material-ui/src/Tooltip/Tooltip.js && echo LINT_OK'
```

tool result:

```
  26 passing (414ms)

LINT_OK
```

**assistant:** All 26 Tooltip tests pass. Cleaning up the temporary files:

**tool call: Bash**

```bash
rm packages/material-ui/src/Tooltip/TmpCopy.test.js packages/material-ui/src/Tooltip/Repro.test.js; git status --short; git diff packages/material-ui/src
```

tool result:

```
 M package.json
 M packages/material-ui/src/Tooltip/Tooltip.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
diff --git a/packages/material-ui/src/Tooltip/Tooltip.js b/packages/material-ui/src/Tooltip/Tooltip.js
index 5d1ceb604..48af5255c 100644
--- a/packages/material-ui/src/Tooltip/Tooltip.js
+++ b/packages/material-ui/src/Tooltip/Tooltip.js
@@ -130,7 +130,8 @@ class Tooltip extends React.Component {
     // We need to account for this eventuality.
     this.focusTimer = setTimeout(() => {
       // We need to make sure the focus hasn't moved since the event was triggered.
-      if (this.childrenRef === document.activeElement) {
+      // The focus can be on a descendant of the children, e.g. the input of a TextField.
+      if (this.childrenRef && this.childrenRef.contains(document.activeElement)) {
         this.handleEnter(event);
       }
     });
```

**assistant:** Focusing a `TextField` inside a `Tooltip` now opens the tooltip. The fix is one line in `packages/material-ui/src/Tooltip/Tooltip.js:134`.

**Cause:** When the child gets focus, the Tooltip waits one tick and then opens only if the focused element (`document.activeElement`) is exactly its child's root element (`this.childrenRef`). For a `TextField`, the root is a wrapper `<div>`, but the focus goes to the `<input>` inside it, so the check always failed and the tooltip never opened.

**Fix:** The check now asks whether focus is anywhere inside the child, not only on its root:
```js
if (this.childrenRef && this.childrenRef.contains(document.activeElement)) {
```
`contains()` also returns true for the root element itself, so children that take focus directly (like a plain `<button>`) behave as before. It still doesn't open if focus has moved away before the timer runs. The extra `this.childrenRef &&` stops it from crashing if there's no element to check yet.

**Verification:**
- **Reproduction:** I mounted a `Tooltip` with `disableHoverListener` around a `TextField` and focused the inner `<input>`. Before the fix the tooltip stayed closed; after it, it opens.
- **Existing tests:** As written, `Tooltip.test.js` gives 20 passing and 6 failing here, and the result is the same without my change. The failures come from the environment: sinon's fake timers also replace `performance`, which breaks React's `performance.mark` on this Node version. I ran a temporary copy that only fakes `setTimeout`/`clearTimeout`, and all 26 tests passed, including the focus and delay tests.
- ESLint passes on the changed file.

I deleted the reproduction test and the temporary copy. `package.json` and `yarn.lock` were already modified, and `Dockerfile` and `custom-reporter.js` were already untracked, when I first checked `git status`; I didn't make those changes, so I left them as they were.

_session end: success, turns 19, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.14 s: ps aux | grep -c mocha; ls node_modules/.bin/mocha
- `rc=143` 0.15 s: pkill -f mocha; NODE_ENV=test timeout 300 node_modules/.bin/mocha --exit packages/material-ui/src/Tooltip/Repro.test.js 2>&1 | tail -20
- `rc=143` 400.97 s: NODE_ENV=test npx mocha packages/material-ui/src/Tooltip/Repro.test.js 2>&1 | tail -20
- `rc=0` 1.73 s: NODE_ENV=test timeout 500 node_modules/.bin/mocha --exit packages/material-ui/src/Tooltip/Repro.test.js 2>&1 | tail -20
- `rc=0` 1.73 s: NODE_ENV=test timeout 500 node_modules/.bin/mocha --exit packages/material-ui/src/Tooltip/Repro.test.js 2>&1 | grep -v "^      at" | head -30
- `rc=0` 1.95 s: NODE_ENV=test timeout 500 node_modules/.bin/mocha --exit packages/material-ui/src/Tooltip/Repro.test.js 2>&1 | grep -v "^      at" | head -30
- `rc=0` 2.71 s: NODE_ENV=test timeout 500 node_modules/.bin/mocha --exit packages/material-ui/src/Tooltip/Repro.test.js packages/material-ui/src/Tooltip/Tooltip.test.js 2>&1 | grep -v "^      at" | tail -30
- `rc=0` 8.08 s: for f in Repro Tooltip; do NODE_ENV=test timeout 500 node_modules/.bin/mocha --exit packages/material-ui/src/Tooltip/$f.test.js 2>&1 | grep -E "passing|failing"; done; git stash -q; NODE_ENV=test timeout 500 node_modules/.bin/mocha --exit packages/material-ui/src/Tooltip/Tooltip.test.js 2>&1 | grep -E "passing|failing"; git stash pop -q; git status --short
- `rc=0` 2.27 s: NODE_ENV=test timeout 500 node_modules/.bin/mocha --exit packages/material-ui/src/Tooltip/Tooltip.test.js 2>&1 | grep -E "^  [0-9]\)|^     [A-Z]" -A2 | head -40
- `rc=0` 4.02 s: NODE_ENV=test timeout 500 node_modules/.bin/mocha --exit packages/material-ui/src/Tooltip/TmpCopy.test.js 2>&1 | grep -E "passing|failing" -A6; NODE_ENV=test timeout 500 node_modules/.bin/eslint packages/material-ui/src/Tooltip/Tooltip.js && echo LINT_OK
