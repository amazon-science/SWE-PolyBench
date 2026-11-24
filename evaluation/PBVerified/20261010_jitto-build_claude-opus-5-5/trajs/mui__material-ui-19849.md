# Instance: mui__material-ui-19849

- Final resolved (evaluator, logs/mui__material-ui-19849_result.json): True
- Run state: DONE
- One attempt. Duration 578.4 s, turns 17, actor cost $0.3477002, container commands 8
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/mui__material-ui-19849/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-19849/repo. Consider the following issue description:

<issue_description>
[TreeItem] No conditional rendering support
<!-- Provide a general summary of the issue in the Title above -->

<!--
  Thank you very much for contributing to Material-UI by creating an issue! ❤️
  To avoid duplicate issues we ask you to check off the following list.
-->

<!-- Checked checkbox should look like this: [x] -->

- [x] The issue is present in the latest release.
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Current Behavior 😯

`TreeView` and `TreeItem` throw an error when attempting to conditionally render a `TreeItem`.

## Expected Behavior 🤔

Any `TreeItem` which is excluded from rendering by a condition (i.e. replaced with `null`) should not be rendered, remove itself from the tree structure, and no error is thrown.

## Steps to Reproduce 🕹

https://codesandbox.io/s/zen-breeze-fh11u

Steps:

1. Render a `<TreeView>` with child `<TreeItem>` components
2. Wrap a `<TreeItem>` in a conditional rendering expression (`{!!condition && <TreeItem />}`)
3. Toggle off the condition. The parent of the `TreeItem` throws an error (it could be another `TreeItem` or the top `TreeView`): `Cannot read property 'props' of null`

## Context 🔦

I'm using TreeView to render a navigation structure in a mobile nav. Depending on the roles and permissions of the user, certain pages are not available in the navigation structure. I therefore have to conditionally render certain tree items based on user information.

From the code it looks like the tree components are assuming that `React.Children.map` iterables will all be defined, but for conditionally rendered elements the values in the Children list will be null.

## Workaround

A workaround is present, but because of the way TreeView works at the moment it's slightly ugly.

You can define a simple wrapper component to handle conditional rendering:

```ts
function ConditionalWrapper({
  show,
  children
}: {
  show: boolean;
  children: ReactElement;
  // required due to TreeView idiosyncrasies
  nodeId: string;
}) {
  if (!show) return null;
  return children;
}
```

You can then use it instead of traditional conditional rendering to avoid the error:

```ts
<ConditionalWrapper show={showTreeItem} nodeId="foo">
  <TreeItem nodeId="foo" label="Foo" />
</ConditionalWrapper>
```

However, as shown above, **`nodeId` is required for both the wrapper and the TreeItem**, because TreeView/TreeItem iterates using `React.Children` naively, assuming all children will be `TreeItem` components with `nodeId` props.

That problem is not necessarily related to this issue, though. If there's interest I would open another issue with thoughts about the use of `React.Children` for this kind of thing (in short, I think children registering via Context is always a more flexible and stable option than reading data from children).

## Your Environment 🌎

<!--
  Include as many relevant details about the environment with which you experienced the bug.
  If you encounter issues with typescript please include version and tsconfig.
-->

| Tech        | Version |
| ----------- | ------- |
| Material-UI | v4.9.0  |
| Material-UI/labs | 4.0.0-alpha.40 |
| React       | v16.9.19        |
| Browser     | Chrome 79.0.3945.88        |
| TypeScript  | 3.8.0        |


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-19849/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-19849/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-19849/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-19849/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/mui__material-ui-19849/repo/packages/material-ui-lab/src; grep -n "Children\|props.nodeId\|child" TreeView/TreeView.js TreeItem/TreeItem.js
```

tool result:

```
TreeView/TreeView.js:41:    children,
TreeView/TreeView.js:212:      diff = parent.children.filter(child => !isExpanded(child));
TreeView/TreeView.js:214:      const topLevelNodes = nodeMap.current[-1].children;
TreeView/TreeView.js:388:  const addNodeToNodeMap = (id, childrenIds) => {
TreeView/TreeView.js:390:    nodeMap.current[id] = { ...currentMap, children: childrenIds, id };
TreeView/TreeView.js:392:    childrenIds.forEach(childId => {
TreeView/TreeView.js:393:      const currentChildMap = nodeMap.current[childId];
TreeView/TreeView.js:394:      nodeMap.current[childId] = { ...currentChildMap, parent: id, id: childId };
TreeView/TreeView.js:403:        if (parentMap && parentMap.children) {
TreeView/TreeView.js:404:          const parentChildren = parentMap.children.filter(c => c !== id);
TreeView/TreeView.js:405:          nodeMap.current[map.parent] = { ...parentMap, children: parentChildren };
TreeView/TreeView.js:418:  const [childrenCalculated, setChildrenCalculated] = React.useState(false);
TreeView/TreeView.js:420:    const childIds = React.Children.map(children, child => child.props.nodeId) || [];
TreeView/TreeView.js:421:    if (arrayDiff(prevChildIds.current, childIds)) {
TreeView/TreeView.js:422:      nodeMap.current[-1] = { parent: null, children: childIds };
TreeView/TreeView.js:424:      childIds.forEach((id, index) => {
TreeView/TreeView.js:430:      visibleNodes.current = nodeMap.current[-1].children;
TreeView/TreeView.js:431:      prevChildIds.current = childIds;
TreeView/TreeView.js:432:      setChildrenCalculated(true);
TreeView/TreeView.js:434:  }, [children]);
TreeView/TreeView.js:442:        const childs = nodeMap.current[item].children;
TreeView/TreeView.js:443:        if (isExpanded(item) && childs) {
TreeView/TreeView.js:444:          list = list.concat(buildVisible(childs));
TreeView/TreeView.js:450:    if (childrenCalculated) {
TreeView/TreeView.js:451:      visibleNodes.current = buildVisible(nodeMap.current[-1].children);
TreeView/TreeView.js:453:  }, [expanded, childrenCalculated, isExpanded]);
TreeView/TreeView.js:493:        {children}
TreeView/TreeView.js:507:  children: PropTypes.node,
TreeItem/TreeItem.js:85:    children,
TreeItem/TreeItem.js:138:  const expandable = Boolean(Array.isArray(children) ? children.length : children);
TreeItem/TreeItem.js:341:    const childIds = React.Children.map(children, child => child.props.nodeId) || [];
TreeItem/TreeItem.js:343:      addNodeToNodeMap(nodeId, childIds);
TreeItem/TreeItem.js:345:  }, [children, nodeId, addNodeToNodeMap]);
TreeItem/TreeItem.js:394:      {children && (
TreeItem/TreeItem.js:403:          {children}
TreeItem/TreeItem.js:418:  children: PropTypes.node,
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-19849/repo/packages/material-ui-lab/src; grep -n -i "condition\|null" TreeView/TreeView.test.js TreeItem/TreeItem.test.js | head -30; sed -n 130,145p TreeItem/TreeItem.js; sed -n 335,346p TreeItem/TreeItem.js
```

tool result:

```
TreeView/TreeView.test.js:95:      const [selectedState, setSelectedState] = React.useState(null);
  } = React.useContext(TreeViewContext);

  const nodeRef = React.useRef(null);
  const contentRef = React.useRef(null);
  const handleRef = useForkRef(nodeRef, ref);

  let icon = iconProp;

  const expandable = Boolean(Array.isArray(children) ? children.length : children);
  const expanded = isExpanded ? isExpanded(nodeId) : false;
  const focused = isFocused ? isFocused(nodeId) : false;
  const tabbable = isTabbable ? isTabbable(nodeId) : false;
  const selected = isSelected ? isSelected(nodeId) : false;
  const icons = contextIcons || {};
  const theme = useTheme();

    if (onFocus) {
      onFocus(event);
    }
  };

  React.useEffect(() => {
    const childIds = React.Children.map(children, child => child.props.nodeId) || [];
    if (addNodeToNodeMap) {
      addNodeToNodeMap(nodeId, childIds);
    }
  }, [children, nodeId, addNodeToNodeMap]);
```

**assistant:** Let me reproduce first with a temporary test.

**tool call: Bash**

```bash
cd /work/mui__material-ui-19849/repo/packages/material-ui-lab/src; head -20 TreeView/TreeView.test.js; cat > TreeView/Repro.test.js <<'EOF'
import * as React from 'react';
import { expect } from 'chai';
import { createClientRender } from 'test/utils/createClientRender';
import TreeView from './TreeView';
import TreeItem from '../TreeItem';

describe('repro conditional', () => {
  const render = createClientRender();
  it('should not crash', () => {
    function MyComponent() {
      const [hide, setHide] = React.useState(false);
      return (
        <React.Fragment>
          <button type="button" onClick={() => setHide(true)}>Hide</button>
          <TreeView defaultExpanded={['1']}>
            {!hide && <TreeItem nodeId="test" label="test" />}
            <TreeItem nodeId="1" label="one">
              {!hide && <TreeItem nodeId="2" label="two" />}
            </TreeItem>
            {null}
          </TreeView>
        </React.Fragment>
      );
    }
    const { getByText, queryByText } = render(<MyComponent />);
    getByText('Hide').click();
    expect(queryByText('test')).to.equal(null);
    expect(queryByText('two')).to.equal(null);
  });
});
EOF
cd ../../..; ../bin/envrun 'yarn -s mocha packages/material-ui-lab/src/TreeView/Repro.test.js 2>&1 | tail -30'
```

tool result:

```
import * as React from 'react';
import { expect } from 'chai';
import { spy } from 'sinon';
import { createClientRender, fireEvent } from 'test/utils/createClientRender';
import describeConformance from '@material-ui/core/test-utils/describeConformance';
import { createMount, getClasses } from '@material-ui/core/test-utils';
import consoleErrorMock from 'test/utils/consoleErrorMock';
import TreeView from './TreeView';
import TreeItem from '../TreeItem';

describe('<TreeView />', () => {
  let classes;
  let mount;
  // StrictModeViolation: test uses TreeItem
  const render = createClientRender({ strict: false });

  before(() => {
    mount = createMount({ strict: true });
    classes = getClasses(<TreeView />);
  });
    at Function.Module._load (node:internal/modules/cjs/loader:911:12)
    at Module.require (node:internal/modules/cjs/loader:1100:19)
    at require (node:internal/modules/cjs/helpers:119:18)
    at /testbed/node_modules/mocha/lib/mocha.js:311:36
    at Array.forEach (<anonymous>)
    at Mocha.loadFiles (/testbed/node_modules/mocha/lib/mocha.js:308:14)
    at Mocha.run (/testbed/node_modules/mocha/lib/mocha.js:849:10)
    at Object.exports.singleRun (/testbed/node_modules/mocha/lib/cli/run-helpers.js:108:16)
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
    at node:internal/main/run_main_module:22:47 {
  code: 'MODULE_NOT_FOUND',
  requireStack: [
    '/testbed/packages/material-ui-lab/src/TreeView/Repro.test.js',
    '/testbed/node_modules/mocha/lib/mocha.js',
    '/testbed/node_modules/mocha/lib/cli/one-and-dones.js',
    '/testbed/node_modules/mocha/lib/cli/options.js',
    '/testbed/node_modules/mocha/bin/mocha'
  ]
}
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-19849/repo; grep '"test:unit"' package.json; cat .mocharc.js 2>/dev/null | head -20
```

tool result:

```
    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/*.test.js' 'docs/**/*.test.js' 'scripts/**/*.test.js' --exclude '**/node_modules/**'",
module.exports = {
  recursive: true,
  reporter: 'dot',
  require: [require.resolve('@babel/register'), require.resolve('./test/utils/setup')],
};
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-19849/repo; ../bin/envrun 'NODE_ENV=test yarn -s mocha packages/material-ui-lab/src/TreeView/Repro.test.js 2>&1 | grep -v "^    at" | tail -30'
```

tool result:

```
Command did not complete within its 120s timeout and was moved to the background (ID: bkt94axak). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/2943734b-9e87-448a-8e0a-654b96b76971/tasks/bkt94axak.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /work/mui__material-ui-19849/repo; directory changes made by the backgrounded command do not apply to subsequent commands.
```

**tool call: Bash**

```bash
sleep 90; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/2943734b-9e87-448a-8e0a-654b96b76971/tasks/bkt94axak.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
sleep 120; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/2943734b-9e87-448a-8e0a-654b96b76971/tasks/bkt94axak.output
```

tool result:

```
Exit code 143
Command timed out after 2m 0s
```

**tool call: Bash**

```bash
sleep 60; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/2943734b-9e87-448a-8e0a-654b96b76971/tasks/bkt94axak.output
```

tool result:

```
(Bash completed with no output)
```

**assistant:** The first mocha run is still going (likely a slow cold Babel compile), so I'm waiting for it to finish.

**tool call: Bash**

```bash
sleep 120; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/2943734b-9e87-448a-8e0a-654b96b76971/tasks/bkt94axak.output
```

tool result:

```
(Bash completed with no output)
```

**assistant:** Still no output after ~7 minutes, so I'm checking whether the process is hung.

**tool call: Bash**

```bash
cd /work/mui__material-ui-19849/repo; ../bin/envrun 'ps aux | grep -v grep | grep -i mocha | head'
```

tool result:

```
root        43  0.1  0.9 1139032 79408 ?       Sl   08:20   0:00 node --no-opt -r /proc/.reset /usr/local/nvm/versions/node/v16.20.2/bin/yarn -s mocha packages/material-ui-lab/src/TreeView/Repro.test.js
root        56  0.0  0.0 287852  3336 ?        S    08:20   0:00 /bin/sh -c /testbed/node_modules/.bin/mocha packages/material-ui-lab/src/TreeView/Repro.test.js
root        57  0.9  2.3 985060 184576 ?       Sl   08:20   0:04 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/.bin/mocha packages/material-ui-lab/src/TreeView/Repro.test.js
```

**assistant:** It's idle (4s CPU total), so mocha probably finished but isn't exiting, and my `tail` pipe was hiding the output. I'll kill it and rerun with `--exit`.

**tool call: Bash**

```bash
cd /work/mui__material-ui-19849/repo; ../bin/envrun 'pkill -f mocha; NODE_ENV=test timeout 100 node_modules/.bin/mocha --exit packages/material-ui-lab/src/TreeView/Repro.test.js 2>&1 | grep -v "^    at" | tail -30'
```

tool result:

```
Exit code 143
```

**assistant:** `pkill -f mocha` matched its own shell command. Running the two steps separately:

**tool call: Bash**

```bash
cd /work/mui__material-ui-19849/repo; ../bin/envrun 'kill 43 56 57; true'; ../bin/envrun 'NODE_ENV=test timeout 100 node_modules/.bin/mocha --exit packages/material-ui-lab/src/TreeView/Repro.test.js > /tmp/out.txt 2>&1; echo rc=$?; grep -v "^    at" /tmp/out.txt | tail -30'
```

tool result:

```
rc=2
      at invokeGuardedCallback (node_modules/react-dom/cjs/react-dom.development.js:440:31)
      at flushPassiveEffectsImpl (node_modules/react-dom/cjs/react-dom.development.js:25392:7)
      at unstable_runWithPriority (node_modules/scheduler/cjs/scheduler.development.js:697:12)
      at runWithPriority$2 (node_modules/react-dom/cjs/react-dom.development.js:12149:10)
      at flushPassiveEffects (node_modules/react-dom/cjs/react-dom.development.js:25361:12)
      at flushWork (node_modules/react-dom/cjs/react-dom-test-utils.development.js:1041:10)
      at act (node_modules/react-dom/cjs/react-dom-test-utils.development.js:1155:9)
      at render (node_modules/@testing-library/react/dist/pure.js:82:26)
      at clientRender (test/utils/createClientRender.js:52:18)
      at render (test/utils/createClientRender.js:90:12)
      at Context.<anonymous> (packages/material-ui-lab/src/TreeView/Repro.test.js:25:40)
      at processImmediate (node:internal/timers:466:21)

  2) repro conditional
       "after each" hook in "repro conditional":
     Uncaught Error: Should not already be working. (and Mocha's done() called multiple times)
      at performSyncWorkOnRoot (node_modules/react-dom/cjs/react-dom.development.js:24247:15)
      at /testbed/node_modules/react-dom/cjs/react-dom.development.js:12199:24
      at unstable_runWithPriority (node_modules/scheduler/cjs/scheduler.development.js:697:12)
      at runWithPriority$2 (node_modules/react-dom/cjs/react-dom.development.js:12149:10)
      at flushSyncCallbackQueueImpl (node_modules/react-dom/cjs/react-dom.development.js:12194:7)
      at workLoop (node_modules/scheduler/cjs/scheduler.development.js:641:34)
      at flushWork (node_modules/scheduler/cjs/scheduler.development.js:596:16)
      at MessagePort.performWorkUntilDeadline (node_modules/scheduler/cjs/scheduler.development.js:203:27)
      at MessagePort.eventHandler (node:internal/event_target:1021:12)
      at MessagePort.[nodejs.internal.kHybridDispatch] (node:internal/event_target:736:20)
      at MessagePort.exports.emitMessage (node:internal/per_context/messageport:23:28)
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-19849/repo; ../bin/envrun 'grep -n -m3 -A3 "Error" /tmp/out.txt'
```

tool result:

```
4:Error: Uncaught [TypeError: Cannot read properties of null (reading 'props')]
5-    at reportException (/testbed/node_modules/jsdom/lib/jsdom/living/helpers/runtime-script-errors.js:62:24)
6-    at innerInvokeEventListeners (/testbed/node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:346:9)
7-    at invokeEventListeners (/testbed/node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:281:3)
--
31:    at processImmediate (node:internal/timers:466:21) TypeError: Cannot read properties of null (reading 'props')
32-    at /testbed/packages/material-ui-lab/src/TreeView/TreeView.js:420:66
33-    at mapSingleChildIntoContext (/testbed/node_modules/react/cjs/react.development.js:1283:26)
34-    at traverseAllChildrenImpl (/testbed/node_modules/react/cjs/react.development.js:1145:5)
--
77:     Error: Uncaught [TypeError: Cannot read properties of null (reading 'props')]
78-    at reportException (/testbed/node_modules/jsdom/lib/jsdom/living/helpers/runtime-script-errors.js:62:24)
79-    at innerInvokeEventListeners (/testbed/node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:346:9)
80-    at invokeEventListeners (/testbed/node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:281:3)
```

**thinking:**

```
I reproduced the error: `React.Children.map` passes `null` to the callback for `false`/`null` children, causing a crash at `TreeView.js:420`. I'll fix this by collecting node IDs only from valid elements in both `TreeView` and `TreeItem`.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-19849/repo/packages/material-ui-lab/src; python3 - <<'EOF'
for f, ind in [('TreeView/TreeView.js', '    '), ('TreeItem/TreeItem.js', '    ')]:
    s = open(f).read()
    old = ind + "const childIds = React.Children.map(children, child => child.props.nodeId) || [];\n"
    new = (ind + "const childIds = [];\n"
           + ind + "React.Children.forEach(children, child => {\n"
           + ind + "  if (React.isValidElement(child) && child.props.nodeId) {\n"
           + ind + "    childIds.push(child.props.nodeId);\n"
           + ind + "  }\n"
           + ind + "});\n")
    assert s.count(old) == 1
    open(f, 'w').write(s.replace(old, new))
EOF
git diff
```

tool result:

```
diff --git a/package.json b/package.json
index 13a574dde..7a88f2e54 100644
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
diff --git a/packages/material-ui-lab/src/TreeItem/TreeItem.js b/packages/material-ui-lab/src/TreeItem/TreeItem.js
index 1b3c568b7..7e9e79717 100644
--- a/packages/material-ui-lab/src/TreeItem/TreeItem.js
+++ b/packages/material-ui-lab/src/TreeItem/TreeItem.js
@@ -338,7 +338,12 @@ const TreeItem = React.forwardRef(function TreeItem(props, ref) {
   };
 
   React.useEffect(() => {
-    const childIds = React.Children.map(children, child => child.props.nodeId) || [];
+    const childIds = [];
+    React.Children.forEach(children, child => {
+      if (React.isValidElement(child) && child.props.nodeId) {
+        childIds.push(child.props.nodeId);
+      }
+    });
     if (addNodeToNodeMap) {
       addNodeToNodeMap(nodeId, childIds);
     }
diff --git a/packages/material-ui-lab/src/TreeView/TreeView.js b/packages/material-ui-lab/src/TreeView/TreeView.js
index ef214967d..6f522a1bb 100644
--- a/packages/material-ui-lab/src/TreeView/TreeView.js
+++ b/packages/material-ui-lab/src/TreeView/TreeView.js
@@ -417,7 +417,12 @@ const TreeView = React.forwardRef(function TreeView(props, ref) {
   const prevChildIds = React.useRef([]);
   const [childrenCalculated, setChildrenCalculated] = React.useState(false);
   React.useEffect(() => {
-    const childIds = React.Children.map(children, child => child.props.nodeId) || [];
+    const childIds = [];
+    React.Children.forEach(children, child => {
+      if (React.isValidElement(child) && child.props.nodeId) {
+        childIds.push(child.props.nodeId);
+      }
+    });
     if (arrayDiff(prevChildIds.current, childIds)) {
       nodeMap.current[-1] = { parent: null, children: childIds };
 
diff --git a/yarn.lock b/yarn.lock
index 6bda298a6..d60be46d6 100644
--- a/yarn.lock
+++ b/yarn.lock
@@ -2093,18 +2093,25 @@
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
@@ -2122,6 +2129,11 @@
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
@@ -2140,6 +2152,11 @@
   resolved "https://registry.yarnpkg.com/@types/events/-/events-3.0.0.tgz#2862f3f58a9a7f7c3e78d79f130dd4d71c25c2a7"
   integrity sha512-EaObqwIvayI5a8dCzhFrjKzVwKLxjoG9T6Ppd5CEo07LRKfQ8Yokw54r5+Wq7FaBQ+yXRvQAYPrHwya1/UFt9g==
 
+"@types/format-util@^1.0.4":
+  version "1.0.4"
+  resolved "https://registry.yarnpkg.com/@types/format-util/-/format-util-1.0.4.tgz#c4e3b556735149fdf047898a5b9c04650491509b"
+  integrity sha512-xrCYOdHh5zA3LUrn6CvspYwlzSWxPso11Lx32WnAG6KvLCRecKZ/Rh21PLXUkzUFsQmr
[... 2438 more characters not shown]
```

**thinking:**

```
The fix is applied—those package.json/yarn.lock changes were pre-existing setup, not something I modified. Now I'll rerun the repro case along with the existing TreeView/TreeItem tests.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-19849/repo; ../bin/envrun 'NODE_ENV=test timeout 200 node_modules/.bin/mocha --exit --reporter spec packages/material-ui-lab/src/TreeView/*.test.js packages/material-ui-lab/src/TreeItem/*.test.js > /tmp/out.txt 2>&1; echo rc=$?; grep -E "passing|failing|pending|repro|should not crash|^\s+[0-9]+\)" /tmp/out.txt'
```

tool result:

```
rc=0
  repro conditional
    ✓ should not crash (157ms)
  71 passing (905ms)
```

**assistant:** The repro passes now, and so do all 70 existing TreeView/TreeItem tests. Removing the repro file:

**tool call: Bash**

```bash
cd /work/mui__material-ui-19849/repo; rm packages/material-ui-lab/src/TreeView/Repro.test.js; git status --short
```

tool result:

```
 M package.json
 M packages/material-ui-lab/src/TreeItem/TreeItem.js
 M packages/material-ui-lab/src/TreeView/TreeView.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
```

**assistant:** Conditionally rendered `TreeItem`s now work: hiding one removes it from the tree without an error.

**Cause:** `TreeView.js` and `TreeItem.js` both built their list of child node IDs with `React.Children.map(children, child => child.props.nodeId)`. React calls that callback with `null` for children like `{false}`, `{null}` or `{cond && <TreeItem/>}`, so reading `child.props` crashed with `Cannot read property 'props' of null`.

**Fix:** in both files I replaced that line with:

```js
const childIds = [];
React.Children.forEach(children, child => {
  if (React.isValidElement(child) && child.props.nodeId) {
    childIds.push(child.props.nodeId);
  }
});
```

Hidden items are left out of the node map, so keyboard navigation and expand/collapse ignore them. Children without a `nodeId` are also skipped instead of adding `undefined` to the map.

**Verification:** I wrote a temporary test that toggles off a top-level `TreeItem` and a nested `TreeItem`, with a literal `{null}` child too. Before the fix it failed with the error from the issue; after the fix it passed. All 70 existing TreeView/TreeItem tests also pass. I deleted the temporary test afterwards.

- **Something I left alone:** if every child of a `TreeItem` is hidden but they're still passed as an array (e.g. `[false, false]`), the item still shows an expand icon. That comes from a separate `expandable` check in `TreeItem.js` and is outside the crash described in the issue. I can fix it too if you want.
- **Other changes in the working tree:** the edits to `package.json` and `yarn.lock`, and the untracked `Dockerfile` and `custom-reporter.js`, were there before I started and aren't mine. My only changes are in `TreeView.js` and `TreeItem.js`.

_session end: success, turns 17, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 2.29 s: yarn -s mocha packages/material-ui-lab/src/TreeView/Repro.test.js 2>&1 | tail -30
- `rc=0` 0.14 s: ps aux | grep -v grep | grep -i mocha | head
- `rc=143` 0.13 s: pkill -f mocha; NODE_ENV=test timeout 100 node_modules/.bin/mocha --exit packages/material-ui-lab/src/TreeView/Repro.test.js 2>&1 | grep -v "^    at" | tail -30
- `rc=143` 523.86 s: NODE_ENV=test yarn -s mocha packages/material-ui-lab/src/TreeView/Repro.test.js 2>&1 | grep -v "^    at" | tail -30
- `rc=0` 0.1 s: kill 43 56 57; true
- `rc=0` 1.74 s: NODE_ENV=test timeout 100 node_modules/.bin/mocha --exit packages/material-ui-lab/src/TreeView/Repro.test.js > /tmp/out.txt 2>&1; echo rc=$?; grep -v "^    at" /tmp/out.txt | tail -30
- `rc=0` 0.12 s: grep -n -m3 -A3 "Error" /tmp/out.txt
- `rc=0` 4.05 s: NODE_ENV=test timeout 200 node_modules/.bin/mocha --exit --reporter spec packages/material-ui-lab/src/TreeView/*.test.js packages/material-ui-lab/src/TreeItem/*.test.js > /tmp/out.txt 2>&1; echo rc=$?; grep -E "passing|failing|pending|repro|should not crash|^\s+[0-9]+\)" /tmp/out.txt
