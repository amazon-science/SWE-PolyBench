# Instance: mui__material-ui-15359

- Final resolved (evaluator, logs/mui__material-ui-15359_result.json): True
- Run state: DONE
- One attempt. Duration 1197.2 s, turns 11, actor cost $0.23189559999999998, container commands 2
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/mui__material-ui-15359/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-15359/repo. Consider the following issue description:

<issue_description>
[Popper] onUpdate / onCreate not handled
`onUpdate` and `onCreate` options are overridden in the Popper component, making it difficult to access internal data about the popout / get lifecycle callbacks.

<!--
    Thank you very much for contributing to Material-UI by creating an issue! ❤️
    To avoid duplicate issues we ask you to check off the following list.
-->

<!-- Checked checkbox should look like this: [x] -->
- [x] This is not a v0.x issue. <!-- (v0.x is no longer maintained) -->
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Expected Behavior 🤔
The `popperOptions` should support `onUpdate` and `onCreate` as per docs (https://github.com/FezVrasta/popper.js#callbacks). i.e. Popper callbacks should be fired when PopperJS creates or "updates" a popup.

## Current Behavior 😯
The callbacks do not fire, as they are overridden in the wrapping MUI Popper component.

## Steps to Reproduce 🕹
<!---
    Provide a link to a live example (you can use codesandbox.io) and an unambiguous set of steps to reproduce this bug.
    Include code to reproduce, if relevant (which it most likely is).

    This codesandbox.io template _may_ be a good starting point:
    https://codesandbox.io/s/github/mui-org/material-ui/tree/next/examples/create-react-app

    If you're using typescript a better starting point would be
    https://codesandbox.io/s/github/mui-org/material-ui/tree/next/examples/create-react-app-with-typescript

    If YOU DO NOT take time to provide a codesandbox.io reproduction, should the COMMUNITY take time to help you?

-->
Try to use `onUpdate` or `onCreate` options: i.e. `<Popper popperOptions={{ onUpdate: data => console.log(data) }} />`

Link:

1. https://codesandbox.io/s/822z0prqz2

## Context 🔦
I am trying to get a callback when the popup is created and get the dimensions of the rendered component.

## Your Environment 🌎
<!---
    Include as many relevant details about the environment with which you experienced the bug.
    If you encounter issues with typescript please include version and tsconfig.
-->

| Tech         | Version |
|--------------|---------|
| Material-UI  | v3.6.0  |
| React        |   v16.8.1      |
| Browser      |    Chrome     |
| TypeScript   |     No    |


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-15359/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-15359/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-15359/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-15359/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cat packages/material-ui/src/Popper/Popper.js | sed -n 1,140p
```

tool result:

```
import React from 'react';
import PropTypes from 'prop-types';
import PopperJS from 'popper.js';
import { chainPropTypes } from '@material-ui/utils';
import Portal from '../Portal';
import { setRef, withForwardedRef } from '../utils';

function flipPlacement(placement) {
  const direction = (typeof window !== 'undefined' && document.body.getAttribute('dir')) || 'ltr';

  if (direction !== 'rtl') {
    return placement;
  }

  switch (placement) {
    case 'bottom-end':
      return 'bottom-start';
    case 'bottom-start':
      return 'bottom-end';
    case 'top-end':
      return 'top-start';
    case 'top-start':
      return 'top-end';
    default:
      return placement;
  }
}

function getAnchorEl(anchorEl) {
  return typeof anchorEl === 'function' ? anchorEl() : anchorEl;
}

/**
 * Poppers rely on the 3rd party library [Popper.js](https://github.com/FezVrasta/popper.js) for positioning.
 */
class Popper extends React.Component {
  tooltipRef = React.createRef();

  constructor(props) {
    super();
    this.state = {
      exited: !props.open,
    };
  }

  componentDidUpdate(prevProps) {
    if (prevProps.open !== this.props.open && !this.props.open && !this.props.transition) {
      // Otherwise handleExited will call this.
      this.handleClose();
    }

    // Let's update the popper position.
    if (
      prevProps.open !== this.props.open ||
      prevProps.anchorEl !== this.props.anchorEl ||
      prevProps.popperOptions !== this.props.popperOptions ||
      prevProps.modifiers !== this.props.modifiers ||
      prevProps.disablePortal !== this.props.disablePortal ||
      prevProps.placement !== this.props.placement
    ) {
      this.handleOpen();
    }
  }

  componentWillUnmount() {
    this.handleClose();
  }

  handleOpen = () => {
    const { anchorEl, modifiers, open, placement, popperOptions = {}, disablePortal } = this.props;
    const popperNode = this.tooltipRef.current;

    if (!popperNode || !anchorEl || !open) {
      return;
    }

    if (this.popper) {
      this.popper.destroy();
      this.popper = null;
    }

    this.popper = new PopperJS(getAnchorEl(anchorEl), popperNode, {
      placement: flipPlacement(placement),
      ...popperOptions,
      modifiers: {
        ...(disablePortal
          ? {}
          : {
              // It's using scrollParent by default, we can use the viewport when using a portal.
              preventOverflow: {
                boundariesElement: 'window',
              },
            }),
        ...modifiers,
        ...popperOptions.modifiers,
      },
      // We could have been using a custom modifier like react-popper is doing.
      // But it seems this is the best public API for this use case.
      onCreate: this.handlePopperUpdate,
      onUpdate: this.handlePopperUpdate,
    });
  };

  handlePopperUpdate = data => {
    if (data.placement !== this.state.placement) {
      this.setState({
        placement: data.placement,
      });
    }
  };

  handleEnter = () => {
    this.setState({ exited: false });
  };

  handleExited = () => {
    this.setState({ exited: true });
    this.handleClose();
  };

  handleClose = () => {
    if (!this.popper) {
      return;
    }

    this.popper.destroy();
    this.popper = null;
  };

  handleRef = ref => {
    setRef(this.props.innerRef, ref);
    setRef(this.tooltipRef, ref);
  };

  render() {
    const {
      anchorEl,
      children,
      container,
      disablePortal,
```

**tool call: Bash**

```bash
grep -rn "createChainedFunction" packages/material-ui/src/utils/*.js | head -3; grep -n "onCreate\|onUpdate" -A15 packages/material-ui/src/Popper/Popper.test.js | head -50
```

tool result:

```
packages/material-ui/src/utils/helpers.js:28:export function createChainedFunction(...funcs) {
```

**tool call: Bash**

```bash
python3 - <<'EOF'
p='packages/material-ui/src/Popper/Popper.js'
s=open(p).read()
s=s.replace("""      onCreate: this.handlePopperUpdate,
      onUpdate: this.handlePopperUpdate,
""","""      onCreate: createChainedFunction(this.handlePopperUpdate, popperOptions.onCreate),
      onUpdate: createChainedFunction(this.handlePopperUpdate, popperOptions.onUpdate),
""")
s=s.replace("import { setRef, withForwardedRef } from '../utils';","import { setRef, withForwardedRef } from '../utils';\nimport { createChainedFunction } from '../utils/helpers';")
open(p,'w').write(s)
EOF
sed -n 20,40p packages/material-ui/src/utils/helpers.js; git diff
```

tool result:

```
 * Safe chained function
 *
 * Will only create a new function if needed,
 * otherwise will pass back existing functions or null.
 *
 * @param {function} functions to chain
 * @returns {function|null}
 */
export function createChainedFunction(...funcs) {
  return funcs.reduce(
    (acc, func) => {
      if (func == null) {
        return acc;
      }

      warning(
        typeof func === 'function',
        'Material-UI: invalid Argument Type, must only provide functions, undefined, or null.',
      );

      return function chainedFunction(...args) {
diff --git a/package.json b/package.json
index 0fc9b8282..678e089a5 100644
--- a/package.json
+++ b/package.json
@@ -76,14 +76,19 @@
     "@emotion/core": "^10.0.0",
     "@emotion/styled": "^10.0.0",
     "@trendmicro/react-interpolate": "0.5.5",
+    "@types/chai": "^5.2.2",
+    "@types/chai-dom": "^1.11.3",
     "@types/enzyme": "^3.1.4",
+    "@types/format-util": "^1.0.4",
+    "@types/prop-types": "^15.7.15",
     "@types/react": "^16.8.10",
-    "@types/react-dom": "^16.0.9",
+    "@types/react-dom": "^19.1.8",
     "@types/react-router-dom": "^4.3.1",
     "@types/react-select": "^2.0.14",
     "@types/react-swipeable-views": "^0.13.0",
     "@types/react-text-mask": "^5.4.2",
     "@types/react-window": "^1.7.0",
+    "@types/sinon": "^17.0.4",
     "@types/styled-components": "^4.1.11",
     "@zeit/next-typescript": "^1.1.1",
     "address": "^1.0.3",
diff --git a/packages/material-ui/src/Popper/Popper.js b/packages/material-ui/src/Popper/Popper.js
index ce37362db..003013cef 100644
--- a/packages/material-ui/src/Popper/Popper.js
+++ b/packages/material-ui/src/Popper/Popper.js
@@ -4,6 +4,7 @@ import PopperJS from 'popper.js';
 import { chainPropTypes } from '@material-ui/utils';
 import Portal from '../Portal';
 import { setRef, withForwardedRef } from '../utils';
+import { createChainedFunction } from '../utils/helpers';
 
 function flipPlacement(placement) {
   const direction = (typeof window !== 'undefined' && document.body.getAttribute('dir')) || 'ltr';
@@ -96,8 +97,8 @@ class Popper extends React.Component {
       },
       // We could have been using a custom modifier like react-popper is doing.
       // But it seems this is the best public API for this use case.
-      onCreate: this.handlePopperUpdate,
-      onUpdate: this.handlePopperUpdate,
+      onCreate: createChainedFunction(this.handlePopperUpdate, popperOptions.onCreate),
+      onUpdate: createChainedFunction(this.handlePopperUpdate, popperOptions.onUpdate),
     });
   };
 
diff --git a/yarn.lock b/yarn.lock
index 72cb28731..a41945fe4 100644
--- a/yarn.lock
+++ b/yarn.lock
@@ -1806,6 +1806,20 @@
     lodash.omit "^4.5.0"
     prop-types "^15.5.8"
 
+"@types/chai-dom@^1.11.3":
+  version "1.11.3"
+  resolved "https://registry.yarnpkg.com/@types/chai-dom/-/chai-dom-1.11.3.tgz#1659ace2698cdcd9ed8b2c007876f53e37d9cc89"
+  integrity sha512-EUEZI7uID4ewzxnU7DJXtyvykhQuwe+etJ1wwOiJyQRTH/ifMWKX+ghiXkxCUvNJ6IQDodf0JXhuP6zZcy2qXQ==
+  dependencies:
+    "@types/chai" "*"
+
+"@types/chai@*", "@types/chai@^5.2.2":
+  version "5.2.2"
+  resolved "https://registry.yarnpkg.com/@types/chai/-/chai-5.2.2.tgz#6f14cea18180ffc4416bc0fd12be05fdd73bdd6b"
+  integrity sha512-8kB30R7Hwqf40JPiKhVzodJs2Qc1ZJ5zuT3uzw5Hq/dhNCl3G3l83jfpdI1e20BP348+fV7VIL/+FxaXkqBmWg==
+  dependencies:
+    "@types/deep-eql" "*"
+
 "@types/cheerio@*":
   version "0.22.11"
   resolved "https://registry.yarnpkg.com/@types/cheerio/-/cheerio-0.22.11.tgz#61c0facf9636d14ba5f77fc65ed8913aa845d717"
@@ -1813,6 +1827,11 @@
   dependencies:
     "@types/node" "*"
 
+"@types/deep-eql@*":
+  version "4.0.2"
+  resolved "https://registry.yarnpkg.com/@types/deep-eql/-/deep-eql-4.0.2.tgz#334311971d3a07121e7eb91b684a605e7eea9cbd"
+  integrity sha512-c9h9dVVMigMPc4bwTvC5dxqtqJZwQPePsWjPlpSOnojbor6pGqdk541lfA7AqFQr5pB1BRdq0juY9db81BwyFw==
+
 "@types/enzyme@^3.1.4":
   version "3.9.1"
   resolved "https://registry.yarnpkg.com/@types/enzyme/-/enzyme-3.9.1.tgz#3a0ce07e30066dbc26cd3474c8e680af2d249e26"
@@ -1831,6 +1850,11 @@
   resolved "https://registry.yarnpkg.com/@types/events/-/events-3.0.0.tgz#2862f3f58a9a7f7c3e78d79f130dd4d71c25c2a7"
   integrity sha512-EaObqwIvayI5a8dCzhFrjKzVwKLxjoG9T6Ppd5CEo07LRKfQ8Yokw54r5+Wq7FaBQ+yXRvQAYPrHwya1/UFt9g==
 
+"@types/format-util@^1.0.4":
+  version "1.0.4"
+  resolved "https://registry.yarnpkg.com/@types/format-util/-/format-util-1.0.4.tgz#c4e3b556735149fdf047898a5b9c04650491509b"
+  integrity sha512-xrCYOdHh5zA3LUrn6CvspYwlzSWxPso11Lx32WnAG6KvLCRecKZ/Rh21PLXUkzUFsQmrGcx/traJAFjR6dVS5Q==
+
 "@types/glob@*":
   version "7.1.1"
   resolved "https://registry.yarnpkg.com/@types/glob/-/glob-7.1.1.tgz#aa59a1c6e3fbc421e07ccd31a944c30eba521575"
@@ -1865,18 +1889,28 @@
   resolved "https://registry.yarnpkg.com/@types/prop-types/-/prop-types-15.7.0.tgz#4c48fed958d6dcf9487195a0ef6456d5f6e0163a"
   integrity sha512-eItQyV43bj4rR3JPV0Skpl1SncRCdziTEK9/v8VwXmV6d/qOUO8/EuWeHBbCZcsfSHfzI5UyMJLCSXtxxznyZg==
 
+"@types/prop-types@^15.7.15":
+  version "15.7.15"
+  resolved "https://registry.yarnpkg.com/@types/prop-types/-/prop-types-15.7.15.tgz#e6e5a86d602beaca71ce5163fadf5f95d70931c7"
+  integrity sha512-F6bEyamV9jKGAFBEmlQnesRPGOQqS2+Uwi0Em15xenOxHaf2hv6L8YCVn3rPdPJOiJfPiCnLIRyvwVaqMY3MIw==
+
 "@types/q@^1.5.1":
   version "1.5.2"
   resolved "https://registry.yarnpkg.com/@types/q/-/q-1.5.2.tgz#690a1475b84f2a884fd07cd797c00f5f31356ea8"
   integrity sha512-ce5d3q03Ex0sy4R14722Rmt6MT07Ua+k4FwDfdcToYJcMKNtRVQvJ6JCAPdAmAnbRb6CsX6aYb9m96NGod9uTw==
 
-"@types/react-dom@*", "@types/react-dom@^16.0.9":
+"@types/react-dom@*":
   version "16.8.3"
   resolved "https://registry.yarnpkg.com/@types/react-dom/-/react-dom-16.8.3.tgz#6131b7b6158bc7ed1925a3374b88b7c00481f0cb"
   integrity sha512-HF5hD5YR3z9Mn6kXcW1VKe4AQ04ZlZj1EdLBae61hzQ3eEWWxMgNLUbIxeZp40BnSxqY1eAYLsH9QopQcxzScA==
   dependencies:
     "@types/react" "*"
 
+"@types/react-dom@^19.1.8":
+  version "19.1.8"
+  resolved "https://registry.yarnpkg.com/@type
[... 1275 more characters not shown]
```

**assistant:** The `package.json`/`yarn.lock` changes were already there before I started. I'm leaving them alone. Next I'll write a quick repro test:

**tool call: Bash**

```bash
cat > packages/material-ui/src/Popper/repro.test.js <<'EOF'
import React from 'react';
import { assert } from 'chai';
import { spy } from 'sinon';
import { createMount } from '@material-ui/core/test-utils';
import Popper from './Popper';

describe('repro', () => {
  it('calls user onCreate/onUpdate', done => {
    const mount = createMount();
    const onCreate = spy();
    const onUpdate = spy();
    const wrapper = mount(
      <Popper open anchorEl={document.createElement('div')} popperOptions={{ onCreate, onUpdate }}>
        <div />
      </Popper>,
    );
    setTimeout(() => {
      assert.strictEqual(onCreate.callCount, 1);
      wrapper.instance().popper.update();
      setTimeout(() => {
        assert.strictEqual(onUpdate.callCount, 1);
        mount.cleanUp();
        done();
      }, 50);
    }, 50);
  });
});
EOF
../bin/envrun 'grep -n "\"test:unit\"" package.json; NODE_ENV=test yarn -s mocha packages/material-ui/src/Popper/*.test.js 2>&1 | tail -30'
```

tool result:

```
Command did not complete within its 300s timeout and was moved to the background (ID: bdcc5j6c6). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/c946f34f-11ff-45d7-9da1-5e51bb016b8f/tasks/bdcc5j6c6.output. You will be notified when it completes. To check interim output, use Read on that file path.
```

**tool call: Bash**

```bash
cat /tmp/cell-scratch/claude-502/<actor-session-slug>/c946f34f-11ff-45d7-9da1-5e51bb016b8f/tasks/bdcc5j6c6.output; grep -n "test:unit\|mocha" package.json; cat .mocharc* test/mocha.opts 2>/dev/null
```

tool result:

```
Exit code 1
55:    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/50:    "test:coverage": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha 'packages/**/*.test.js' 'docs/**/*.test.js' --exclude '**/node_modules/**' && nyc report -r lcovonly",
51:    "test:coverage:html": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha 'packages/**/**/*.test.js' --exclude '**/node_modules/**' && nyc report --reporter=html",
55:    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/*.test.js' 'docs/**/*.test.js' --exclude '**/node_modules/**'",
56:    "test:watch": "yarn test:unit --watch",
133:    "eslint-plugin-mocha": "^5.0.0",
151:    "karma-mocha": "^1.3.0",
152:    "karma-mocha-reporter": "^2.2.5",
161:    "mocha": "^5.0.0",
(eval):1: no matches found: .mocharc*
```

**tool call: Bash**

```bash
../bin/envrun 'NODE_ENV=test timeout 250 node_modules/.bin/mocha packages/material-ui/src/Popper/*.test.js 2>&1 | tail -30'
```

tool result:

```
Browserslist: caniuse-lite is outdated. Please run next command `yarn upgrade`


  ․․․․․․․․․․․․․․․․․!

  17 passing (387ms)
  1 failing

  1) repro
       calls user onCreate/onUpdate:
     Uncaught TypeError: Cannot read properties of null (reading 'popper')
      at Timeout._onTimeout (packages/material-ui/src/Popper/repro.test.js:19:7)
      at listOnTimeout (node:internal/timers:559:17)
      at processTimers (node:internal/timers:502:7)
```

**assistant:** onCreate passed. `instance()` returned null because of the `withForwardedRef` wrapper, so I'll reach the inner component a different way:

**tool call: Bash**

```bash
sed -i '' "s/wrapper.instance().popper.update()/wrapper.find('Popper').filterWhere(n => n.instance()).first().instance().popper.update()/" packages/material-ui/src/Popper/repro.test.js
../bin/envrun 'NODE_ENV=test timeout 250 node_modules/.bin/mocha packages/material-ui/src/Popper/*.test.js 2>&1 | tail -15; git stash -q -- packages/material-ui/src/Popper/Popper.js; NODE_ENV=test timeout 250 node_modules/.bin/mocha packages/material-ui/src/Popper/repro.test.js 2>&1 | tail -8; git stash pop -q; git diff --stat packages'
```

tool result:

```
Command did not complete within its 300s timeout and was moved to the background (ID: b6962m0zx). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/c946f34f-11ff-45d7-9da1-5e51bb016b8f/tasks/b6962m0zx.output. You will be notified when it completes. To check interim output, use Read on that file path.
```

**tool call: Bash**

```bash
sleep 60; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/c946f34f-11ff-45d7-9da1-5e51bb016b8f/tasks/b6962m0zx.output; git -C . diff --stat packages; git stash list
```

tool result:

```
Browserslist: caniuse-lite is outdated. Please run next command `yarn upgrade`


  ․․․․�stash@{0}: WIP on main: 13ac4ce92 [List] Update to match the specification (#15339)
```

**assistant:** The first run seems to have hung until the timeout killed it, and the stash step has run. I'll wait for the rest:

**tool call: Bash**

```bash
sleep 200; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/c946f34f-11ff-45d7-9da1-5e51bb016b8f/tasks/b6962m0zx.output; git diff --stat packages; git stash list
```

tool result:

```
Browserslist: caniuse-lite is outdated. Please run next command `yarn upgrade`


  ․․․․․․․․․․․․․․․․․․

  18 passing (446ms)

      +1
      
      at Timeout.strictEqual [as _onTimeout] (packages/material-ui/src/Popper/repro.test.js:18:14)
      at listOnTimeout (node:internal/timers:559:17)
      at processTimers (node:internal/timers:502:7)



 packages/material-ui/src/Popper/Popper.js | 5 +++--
 1 file changed, 3 insertions(+), 2 deletions(-)


[exited with code 0]
 packages/material-ui/src/Popper/Popper.js | 5 +++--
 1 file changed, 3 insertions(+), 2 deletions(-)
```

**thinking:**

```
All 18 tests pass with the fix restored, confirming the repro correctly reproduced the original bug. Now I'll remove the repro file.


```

**tool call: Bash**

```bash
rm packages/material-ui/src/Popper/repro.test.js; git status --short
```

tool result:

```
 M package.json
 M packages/material-ui/src/Popper/Popper.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
```

**assistant:** `onCreate` and `onUpdate` in `popperOptions` now fire. Before, Popper always replaced them with its own internal handler.

**The fix** (`packages/material-ui/src/Popper/Popper.js`): Popper still runs its internal `handlePopperUpdate`, which keeps track of the placement. It then calls your callback with the same Popper.js data object. This uses the repo's existing `createChainedFunction` helper from `../utils/helpers`:

```js
onCreate: createChainedFunction(this.handlePopperUpdate, popperOptions.onCreate),
onUpdate: createChainedFunction(this.handlePopperUpdate, popperOptions.onUpdate),
```

If you don't pass a callback, the helper skips it, so behaviour is unchanged when `popperOptions` is omitted or has no callbacks.

**Testing:** I wrote a temporary test that mounts an open Popper with spy `onCreate`/`onUpdate` options and triggers `popper.update()`.
- **Without the fix:** it fails because `onCreate` is called 0 times.
- **With the fix:** it passes, along with all 17 existing tests in `Popper.test.js` (18 passing).
- One quirk: when run directly, mocha doesn't exit after the tests finish because it's run without `--exit`. The results are complete before that point.

I deleted the temporary test, so the only change I made is in `Popper.js`. The working tree also has changes I didn't make and left alone: modified `package.json` and `yarn.lock` (added `@types/*` packages), and untracked `Dockerfile` and `custom-reporter.js`.

_session end: success, turns 11, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 250.14 s: NODE_ENV=test timeout 250 node_modules/.bin/mocha packages/material-ui/src/Popper/*.test.js 2>&1 | tail -30
- `rc=0` 503.86 s: NODE_ENV=test timeout 250 node_modules/.bin/mocha packages/material-ui/src/Popper/*.test.js 2>&1 | tail -15; git stash -q -- packages/material-ui/src/Popper/Popper.js; NODE_ENV=test timeout 250 node_modules/.bin/mocha packages/material-ui/src/Popper/repro.test.js 2>&1 | tail -8; git stash pop -q; git diff --stat packages
