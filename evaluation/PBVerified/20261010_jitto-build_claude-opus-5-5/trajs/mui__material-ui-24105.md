# Instance: mui__material-ui-24105

- Final resolved (evaluator, logs/mui__material-ui-24105_result.json): True
- Run state: DONE
- One attempt. Duration 511.3 s, turns 18, actor cost $0.28947419999999996, container commands 8
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/mui__material-ui-24105/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-24105/repo. Consider the following issue description:

<issue_description>
[TreeView] Scroll jump bug
When Tree View has a larger height than the window height, clicking Tree Items first jumps the position of the item to the top and then on the second click toggles. See the video, please. 

A similar thing happens in the last items too - it just positions the element to the bottom and it is really hard to click it then.

Items in the middle seem fine. 

Official doc examples have the same problem.

https://user-images.githubusercontent.com/7082560/102820418-84cc2b00-43d5-11eb-94fb-f7019d355366.mov

### Versions

v5.0.0-alpha.20

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-24105/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-24105/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-24105/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-24105/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/mui__material-ui-24105/repo/packages/material-ui-lab/src; grep -n "focus\|Focus" TreeItem/TreeItem.js TreeView/TreeView.js | head -80
```

tool result:

```
TreeItem/TreeItem.js:45:    '&$focused': {
TreeItem/TreeItem.js:46:      backgroundColor: theme.palette.action.focus,
TreeItem/TreeItem.js:60:      '&$focused': {
TreeItem/TreeItem.js:63:          theme.palette.action.selectedOpacity + theme.palette.action.focusOpacity,
TreeItem/TreeItem.js:72:  /* Pseudo-class applied to the content element when focused. */
TreeItem/TreeItem.js:73:  focused: {},
TreeItem/TreeItem.js:120:    focus,
TreeItem/TreeItem.js:122:    isFocused,
TreeItem/TreeItem.js:126:    disabledItemsFocusable,
TreeItem/TreeItem.js:158:  const focused = isFocused ? isFocused(nodeId) : false;
TreeItem/TreeItem.js:223:  function handleFocus(event) {
TreeItem/TreeItem.js:224:    // DOM focus stays on the tree which manages focus with aria-activedescendant
TreeItem/TreeItem.js:226:      ownerDocument(event.target).getElementById(treeId).focus();
TreeItem/TreeItem.js:229:    const unfocusable = !disabledItemsFocusable && disabled;
TreeItem/TreeItem.js:230:    if (!focused && event.currentTarget === event.target && !unfocusable) {
TreeItem/TreeItem.js:231:      focus(event, nodeId);
TreeItem/TreeItem.js:246:      onFocus={handleFocus}
TreeItem/TreeItem.js:254:          focused: classes.focused,
TreeItem/TreeItem.js:350:   * Use the `onNodeFocus` callback on the tree if you need to monitor a node's focus.
TreeItem/TreeItem.js:352:  onFocus: unsupportedProp,
TreeView/TreeView.js:55:    disabledItemsFocusable = false,
TreeView/TreeView.js:61:    onFocus,
TreeView/TreeView.js:63:    onNodeFocus,
TreeView/TreeView.js:75:  const [focusedNodeId, setFocusedNodeId] = React.useState(null);
TreeView/TreeView.js:137:  const isFocused = (id) => focusedNodeId === id;
TreeView/TreeView.js:156:    if (!disabledItemsFocusable) {
TreeView/TreeView.js:303:   * Focus Helpers
TreeView/TreeView.js:306:  const focus = (event, id) => {
TreeView/TreeView.js:308:      setFocusedNodeId(id);
TreeView/TreeView.js:310:      if (onNodeFocus) {
TreeView/TreeView.js:311:        onNodeFocus(event, id);
TreeView/TreeView.js:316:  const focusNextNode = (event, id) => focus(event, getNextNode(id));
TreeView/TreeView.js:317:  const focusPreviousNode = (event, id) => focus(event, getPreviousNode(id));
TreeView/TreeView.js:318:  const focusFirstNode = (event) => focus(event, getFirstNode());
TreeView/TreeView.js:319:  const focusLastNode = (event) => focus(event, getLastNode());
TreeView/TreeView.js:321:  const focusByFirstCharacter = (event, id, char) => {
TreeView/TreeView.js:333:      const shouldBeSkipped = disabledItemsFocusable ? false : isDisabled(nodeId);
TreeView/TreeView.js:357:      focus(event, firstCharIds[index]);
TreeView/TreeView.js:365:  const toggleExpansion = (event, value = focusedNodeId) => {
TreeView/TreeView.js:582:    setFocusedNodeId((oldFocusedNodeId) => {
TreeView/TreeView.js:584:        oldFocusedNodeId === id &&
TreeView/TreeView.js:589:      return oldFocusedNodeId;
TreeView/TreeView.js:608:    if (isExpandable(focusedNodeId)) {
TreeView/TreeView.js:609:      if (isExpanded(focusedNodeId)) {
TreeView/TreeView.js:610:        focusNextNode(event, focusedNodeId);
TreeView/TreeView.js:611:      } else if (!isDisabled(focusedNodeId)) {
TreeView/TreeView.js:619:    if (isExpanded(focusedNodeId) && !isDisabled(focusedNodeId)) {
TreeView/TreeView.js:620:      toggleExpansion(event, focusedNodeId);
TreeView/TreeView.js:624:    const parent = getParent(focusedNodeId);
TreeView/TreeView.js:626:      focus(event, parent);
TreeView/TreeView.js:636:    // If the tree is empty there will be no focused node
TreeView/TreeView.js:637:    if (event.altKey || event.currentTarget !== event.target || !focusedNodeId) {
TreeView/TreeView.js:644:        if (!disableSelection && !isDisabled(focusedNodeId)) {
TreeView/TreeView.js:646:            selectRange(event, { end: focusedNodeId });
TreeView/TreeView.js:649:            flag = selectNode(event, focusedNodeId, true);
TreeView/TreeView.js:651:            flag = selectNode(event, focusedNodeId);
TreeView/TreeView.js:657:        if (!isDisabled(focusedNodeId)) {
TreeView/TreeView.js:658:          if (isExpandable(focusedNodeId)) {
TreeView/TreeView.js:667:          selectNextNode(event, focusedNodeId);
TreeView/TreeView.js:669:        focusNextNode(event, focusedNodeId);
TreeView/TreeView.js:674:          selectPreviousNode(event, focusedNodeId);
TreeView/TreeView.js:676:        focusPreviousNode(event, focusedNodeId);
TreeView/TreeView.js:699:          !isDisabled(focusedNodeId)
TreeView/TreeView.js:701:          rangeSelectToFirst(event, focusedNodeId);
TreeView/TreeView.js:703:        focusFirstNode(event);
TreeView/TreeView.js:712:          !isDisabled(focusedNodeId)
TreeView/TreeView.js:714:          rangeSelectToLast(event, focusedNodeId);
TreeView/TreeView.js:716:        focusLastNode(event);
TreeView/TreeView.js:721:          expandAllSiblings(event, focusedNodeId);
TreeView/TreeView.js:727:          focusByFirstCharacter(event, focusedNodeId, key);
TreeView/TreeView.js:742:  const handleFocus = (event) => {
TreeView/TreeView.js:743:    // if the event bubbled (which is React specific) we don't want to steal focus
TreeView/TreeView.js:746:      focus(event, firstSelected || getNavigableChildrenIds(null)[0]);
TreeView/TreeView.js:749:    if (onFocus) {
TreeView/TreeView.js:750:      onFocus(event);
TreeView/TreeView.js:755:    setFocusedNodeId(null);
TreeView/TreeView.js:762:  const activeDescendant = nodeMap.current[focusedNodeId]
TreeView/TreeView.js:763:    ? nodeMap.current[focusedNodeId].idAttribute
TreeView/TreeView.js:770:        focus,
TreeView/TreeView.js:774:        isFocused,
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-24105/repo/packages/material-ui-lab/src; sed -n 215,240p TreeItem/TreeItem.js; sed -n 735,760p TreeView/TreeView.js; git log --oneline -1; grep -n "focus" TreeItem/TreeItem.test.js | grep -n "scroll\|preventScroll\|spy" 
```

tool result:

```
     *
     * If the tree does not support multiple selection, aria-selected
     * is set to true for the selected node and it is not present on any other node in the tree.
     * Source: https://www.w3.org/TR/wai-aria-practices/#TreeView
     */
    ariaSelected = true;
  }

  function handleFocus(event) {
    // DOM focus stays on the tree which manages focus with aria-activedescendant
    if (event.target === event.currentTarget) {
      ownerDocument(event.target).getElementById(treeId).focus();
    }

    const unfocusable = !disabledItemsFocusable && disabled;
    if (!focused && event.currentTarget === event.target && !unfocusable) {
      focus(event, nodeId);
    }
  }

  return (
    <li
      className={clsx(classes.root, className)}
      role="treeitem"
      aria-expanded={expandable ? expanded : null}
      aria-selected={ariaSelected}
    }

    if (onKeyDown) {
      onKeyDown(event);
    }
  };

  const handleFocus = (event) => {
    // if the event bubbled (which is React specific) we don't want to steal focus
    if (event.target === event.currentTarget) {
      const firstSelected = Array.isArray(selected) ? selected[0] : selected;
      focus(event, firstSelected || getNavigableChildrenIds(null)[0]);
    }

    if (onFocus) {
      onFocus(event);
    }
  };

  const handleBlur = (event) => {
    setFocusedNodeId(null);

    if (onBlur) {
      onBlur(event);
    }
  };
16c648dfd [styles] Fix for supporting non string props (#24101)
82:1955:          const focusSpy = spy();
94:2033:          const focusSpy = spy();
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-24105/repo/packages/material-ui-lab/src; grep -rn "preventScroll" . ; git status
```

tool result:

```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   ../../../package.json
	modified:   ../../../yarn.lock

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	../../../Dockerfile
	../../../custom-reporter.js

no changes added to commit (use "git add" and/or "git commit -a")
```

**thinking:**

```
Found it: clicking a tree item focuses the `<li>`, triggering `handleFocus` to call `.focus()` on the tree `<ul>` without `preventScroll`, which causes the browser to scroll the whole tree into view. I'll verify this by checking the focus call's arguments.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-24105/repo/packages/material-ui-lab/src; cat > TreeItem/repro.test.js <<'EOF'
import * as React from 'react';
import { expect } from 'chai';
import { spy } from 'sinon';
import { createClientRender, fireEvent } from 'test/utils';
import TreeView from '@material-ui/lab/TreeView';
import TreeItem from '@material-ui/lab/TreeItem';

describe('repro', () => {
  const render = createClientRender();
  it('focuses tree with preventScroll', () => {
    const { getByTestId } = render(
      <TreeView><TreeItem nodeId="one" label="one" data-testid="one" /></TreeView>,
    );
    const focusSpy = spy(HTMLElement.prototype, 'focus');
    try {
      getByTestId('one').focus();
      const treeCall = focusSpy.getCalls().find((c) => c.thisValue.getAttribute('role') === 'tree');
      expect(treeCall.args[0]).to.deep.equal({ preventScroll: true });
    } finally {
      focusSpy.restore();
    }
  });
});
EOF
cd ../../..; ../bin/envrun 'yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeItem/repro.test.js 2>&1 | tail -20'
```

tool result:

```
Command did not complete within its 120s timeout and was moved to the background (ID: bm1exunin). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/6f436fe6-053b-4a5a-a26a-9df98a6d4365/tasks/bm1exunin.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /work/mui__material-ui-24105/repo/packages/material-ui-lab/src; directory changes made by the backgrounded command do not apply to subsequent commands.
```

**tool call: Bash**

```bash
sleep 90; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/6f436fe6-053b-4a5a-a26a-9df98a6d4365/tasks/bm1exunin.output
```

tool result:

```
(Bash completed with no output)
```

**assistant:** The repro test is still running (Babel compilation is slow on first run). I'm waiting for it to finish.

**tool call: Bash**

```bash
sleep 120; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/6f436fe6-053b-4a5a-a26a-9df98a6d4365/tasks/bm1exunin.output
```

tool result:

```
Exit code 143
Command timed out after 2m 0s
```

**tool call: Bash**

```bash
cat /tmp/cell-scratch/claude-502/<actor-session-slug>/6f436fe6-053b-4a5a-a26a-9df98a6d4365/tasks/bm1exunin.output; cat ../../../.mocharc.js | head -30
```

tool result:

```
module.exports = {
  extension: ['js', 'ts', 'tsx'],
  ignore: [
    '**/build/**',
    '**/node_modules/**',
    // Mocha seems to ignore .next anyway (maybe because dotfiles?).
    // We're leaving this to make sure.
    'docs/.next/**',
  ],
  recursive: true,
  reporter: 'dot',
  require: [require.resolve('./test/utils/setupBabel'), require.resolve('./test/utils/setupJSDOM')],
  'watch-ignore': [
    // default
    '.git',
    // node_modules can be nested with workspaces
    '**/node_modules/**',
    // Unrelated directories with a large number of files
    '**/build/**',
    'docs/.next/**',
  ],
};
```

**tool call: Bash**

```bash
sleep 110; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/6f436fe6-053b-4a5a-a26a-9df98a6d4365/tasks/bm1exunin.output
```

tool result:

```
(Bash completed with no output)
```

**assistant:** Still no output after several minutes, so I'll check what's running in the container.

**tool call: Bash**

```bash
cd /work/mui__material-ui-24105; bin/envrun 'ps aux | grep -v grep | grep -E "mocha|node" | head'
```

tool result:

```
root         7  0.0  0.0 419788  6348 ?        Ss   12:26   0:00 bash -lc yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeItem/repro.test.js 2>&1 | tail -20
root        15  0.1  0.5 1049140 84176 ?       Sl   12:26   0:00 node --no-opt -r /proc/.reset /usr/local/nvm/versions/node/v16.20.2/bin/yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeItem/repro.test.js
root        23  0.1  0.5 1215056 92920 ?       Sl   12:26   0:00 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/.yarn/releases/yarn-1.22.4.js -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeItem/repro.test.js
root        34  0.0  0.0 418032  3360 ?        S    12:26   0:00 /bin/sh -c /testbed/node_modules/.bin/cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeItem/repro.test.js
root        35  0.0  0.3 945224 50936 ?        Sl   12:26   0:00 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/.bin/cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeItem/repro.test.js
root        42  1.5  1.4 1157532 231228 ?      Sl   12:26   0:07 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/.bin/mocha packages/material-ui-lab/src/TreeItem/repro.test.js
Shell cwd was reset to /work/mui__material-ui-24105/repo
```

**assistant:** Mocha is mostly idle, so the test probably finished and the process isn't exiting. I'll kill it and rerun with `--exit`.

**tool call: Bash**

```bash
bin/envrun 'pkill -f mocha; timeout 300 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js 2>&1 | tail -30'
```

tool result:

```
Exit code 127
(eval):1: no such file or directory: bin/envrun
```

**tool call: Bash**

```bash
../bin/envrun 'pkill -f mocha; timeout 300 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js 2>&1 | tail -30'
```

tool result:

```
Exit code 143
```

**assistant:** `pkill -f mocha` matched its own shell command and killed it. I'll run the test on its own.

**tool call: Bash**

```bash
../bin/envrun 'timeout 300 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js 2>&1 | tail -30'
```

tool result:

```
    at renderWithHooks (/testbed/node_modules/react-dom/cjs/react-dom.development.js:14803:18)
    at updateForwardRef (/testbed/node_modules/react-dom/cjs/react-dom.development.js:16821:24)
    at beginWork (/testbed/node_modules/react-dom/cjs/react-dom.development.js:18645:16)
    at beginWork$1 (/testbed/node_modules/react-dom/cjs/react-dom.development.js:23179:14)
    at performUnitOfWork (/testbed/node_modules/react-dom/cjs/react-dom.development.js:22157:12)
    at workLoopSync (/testbed/node_modules/react-dom/cjs/react-dom.development.js:22130:22)
    at performSyncWorkOnRoot (/testbed/node_modules/react-dom/cjs/react-dom.development.js:21756:9)
    at /testbed/node_modules/react-dom/cjs/react-dom.development.js:11089:24
    at unstable_runWithPriority (/testbed/node_modules/scheduler/cjs/scheduler.development.js:653:12)
    at runWithPriority$1 (/testbed/node_modules/react-dom/cjs/react-dom.development.js:11039:10)
    at flushSyncCallbackQueueImpl (/testbed/node_modules/react-dom/cjs/react-dom.development.js:11084:7)
    at flushSyncCallbackQueue (/testbed/node_modules/react-dom/cjs/react-dom.development.js:11072:3)
    at discreteUpdates$1 (/testbed/node_modules/react-dom/cjs/react-dom.development.js:21893:7)
    at discreteUpdates (/testbed/node_modules/react-dom/cjs/react-dom.development.js:806:12)
    at dispatchDiscreteEvent (/testbed/node_modules/react-dom/cjs/react-dom.development.js:4168:3)
    at Document.callTheUserObjectsOperation (/testbed/node_modules/jsdom/lib/jsdom/living/generated/EventListener.js:26:30)
    at innerInvokeEventListeners (/testbed/node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:318:25)
    at invokeEventListeners (/testbed/node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:274:3)
    at HTMLLIElementImpl._dispatch (/testbed/node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:205:9)
    at Object.exports.fireFocusEventWithTargetAdjustment (/testbed/node_modules/jsdom/lib/jsdom/living/helpers/focusing.js:103:10)
    at HTMLLIElementImpl.focus (/testbed/node_modules/jsdom/lib/jsdom/living/nodes/HTMLOrSVGElement-impl.js:68:14)
    at HTMLLIElement.focus (/testbed/node_modules/jsdom/lib/jsdom/living/generated/HTMLElement.js:117:34)
    at Function.invoke (/testbed/node_modules/sinon/lib/sinon/proxy-invoke.js:47:47)
    at HTMLLIElement.focus (/testbed/node_modules/sinon/lib/sinon/proxy.js:216:26)
    at Context.<anonymous> (/testbed/packages/material-ui-lab/src/TreeItem/repro.test.js:16:26)
    at processImmediate (node:internal/timers:466:21)
```

**tool call: Bash**

```bash
../bin/envrun 'timeout 300 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js 2>&1 | grep -v "^    at" | tail -30'
```

tool result:

```
    in StrictMode (created by Wrapper)
    in Wrapper

Stack:

console.error message:
  Warning: An update to ForwardRef(TreeItem) ran an effect, but was not wrapped in act(...).

When testing, code that causes React state updates should be wrapped into act(...):

act(() => {
  /* fire events that update state */
});
/* assert on the output */

This ensures that you're testing the behavior the user would see in the browser. Learn more at https://fb.me/react-wrap-tests-with-act
    in ForwardRef(TreeItem) (created by WithStyles(ForwardRef(TreeItem)))
    in WithStyles(ForwardRef(TreeItem))
    in ul (created by ForwardRef(TreeView))
    in DescendantProvider (created by ForwardRef(TreeView))
    in ForwardRef(TreeView) (created by WithStyles(ForwardRef(TreeView)))
    in WithStyles(ForwardRef(TreeView))
    in StrictMode (created by Wrapper)
    in Wrapper

Stack:
```

**assistant:** The test setup fails on React `act()` warnings, so I'll wrap the focus call in `act` and look at the assertion output.

**tool call: Bash**

```bash
cd packages/material-ui-lab/src/TreeItem && sed -i '' "s/import { createClientRender, fireEvent } from 'test\/utils';/import { act, createClientRender } from 'test\/utils';/; s/      getByTestId('one').focus();/      act(() => { getByTestId('one').focus(); });/" repro.test.js && cd ../../../.. && ../bin/envrun 'timeout 300 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js 2>&1 | grep -v "^    at" | tail -30'
```

tool result:

```
Browserslist: caniuse-lite is outdated. Please run:
npx browserslist@latest --update-db

Why you should do it regularly:
https://github.com/browserslist/browserslist#browsers-data-updating
including inaccessible elements by default


  !

  0 passing (119ms)
  1 failing

  1) repro
       focuses tree with preventScroll:
     AssertionError: expected undefined to deeply equal { preventScroll: true }
      at Context.<anonymous> (packages/material-ui-lab/src/TreeItem/repro.test.js:18:40)
      at processImmediate (node:internal/timers:466:21)
```

**assistant:** The repro confirms the bug: the tree is focused without `preventScroll`. Now the fix:

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/mui__material-ui-24105/repo/packages/material-ui-lab/src/TreeItem/TreeItem.js",
 "old_string": "      ownerDocument(event.target).getElementById(treeId).focus();",
 "new_string": "      // preventScroll avoids scrolling the whole tree into view when an item is clicked\n      ownerDocument(event.target).getElementById(treeId).focus({ preventScroll: true });"
}
```

tool result:

```
The file /work/mui__material-ui-24105/repo/packages/material-ui-lab/src/TreeItem/TreeItem.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
../bin/envrun 'timeout 300 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js 2>&1 | grep -v "^    at" | tail -8'
```

tool result:

```
https://github.com/browserslist/browserslist#browsers-data-updating
including inaccessible elements by default


  ․

  1 passing (158ms)
```

**assistant:** The fix works. I'll remove the repro file and run the existing TreeView/TreeItem tests.

**tool call: Bash**

```bash
rm packages/material-ui-lab/src/TreeItem/repro.test.js; grep -rn "\.focus(" packages/material-ui-lab/src/Tree*/*.js | grep -v test; ../bin/envrun 'timeout 500 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit "packages/material-ui-lab/src/Tree*/*.test.js" 2>&1 | grep -v "^    at" | tail -15'; git status --short
```

tool result:

```
packages/material-ui-lab/src/TreeItem/TreeItem.js:227:      ownerDocument(event.target).getElementById(treeId).focus({ preventScroll: true });
Browserslist: caniuse-lite is outdated. Please run:
npx browserslist@latest --update-db

Why you should do it regularly:
https://github.com/browserslist/browserslist#browsers-data-updating
including inaccessible elements by default


  ․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․
  ․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․
  ․․․․․․․․․․․․․․․․․․․․․․․․․

  137 passing (2s)


 M package.json
 M packages/material-ui-lab/src/TreeItem/TreeItem.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
```

**assistant:** I fixed the scroll jump with a one-line change in `packages/material-ui-lab/src/TreeItem/TreeItem.js:227`.

**Cause:** The tree keeps keyboard focus on its root `<ul>` and marks the current item with `aria-activedescendant`. When you click an item, the `<li>` gets focus first, and its focus handler passes focus back to the root with a plain `.focus()`. By default the browser then scrolls whatever gets focus into view. When the tree is taller than the window, that means jumping so the tree's top (or bottom) edge lines up with the window. That's why only the first and last items were affected, and why the first click didn't toggle: the item moved out from under the pointer.

**Fix:** Focus the root with `{ preventScroll: true }`, so it no longer scrolls the page:

```js
ownerDocument(event.target).getElementById(treeId).focus({ preventScroll: true });
```

**Verification:**
- The test environment (jsdom) doesn't actually scroll, so the reproduction test checked how the tree root gets focused instead. It failed before the change (focus had no options) and passed after it.
- All 137 existing TreeView/TreeItem tests pass.
- I didn't check it in a real browser.
- I deleted the reproduction test afterwards.

Keyboard navigation still scrolls the focused item into view, because that doesn't use this focus call. `package.json`, `yarn.lock`, `Dockerfile` and `custom-reporter.js` were already modified or untracked when I started, and I didn't touch them.

_session end: success, turns 18, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.15 s: ps aux | grep -v grep | grep -E "mocha|node" | head
- `rc=143` 0.14 s: pkill -f mocha; timeout 300 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js 2>&1 | tail -30
- `rc=143` 456.17 s: yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeItem/repro.test.js 2>&1 | tail -20
- `rc=0` 3.11 s: timeout 300 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js 2>&1 | tail -30
- `rc=0` 3.15 s: timeout 300 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js 2>&1 | grep -v "^    at" | tail -30
- `rc=0` 3.03 s: timeout 300 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js 2>&1 | grep -v "^    at" | tail -30
- `rc=0` 3.6 s: timeout 300 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js 2>&1 | grep -v "^    at" | tail -8
- `rc=0` 6.27 s: timeout 500 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit "packages/material-ui-lab/src/Tree*/*.test.js" 2>&1 | grep -v "^    at" | tail -15
