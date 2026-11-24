# Instance: mui__material-ui-20657

- Final resolved (evaluator, logs/mui__material-ui-20657_result.json): True
- Run state: DONE
- One attempt. Duration 1001.9 s, turns 20, actor cost $0.4183962000000001, container commands 9
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/mui__material-ui-20657/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-20657/repo. Consider the following issue description:

<issue_description>
[TreeView] Expand/collapse node only when clicking on expand/collapse icon
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Summary 💡

When I click on a tree item that has children, the node expands, wherever I click on the line. While this behavior might be ok for most users, I would like to have the possibility to expand/collapse only when I click on the expand/collapse icon - not on the label.

## Motivation 🔦

In my project, I have a tree and I'd like to display a panel with information about a node when I click on it.
When my node does not have children, it is very easy to achieve this behavior. But when my node has children, it expends at the same time its information are displayed, which is not the behavior I want. So I lack a way to have a different behavior when I click on the label (display node info) and when I click on the expand/collapse icon (expand/collapse the node).

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-20657/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-20657/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-20657/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-20657/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd packages/material-ui-lab/src/TreeItem && ls && cat TreeItem.js TreeItem.d.ts; grep -n "IconClick\|LabelClick" TreeItem.test.js | head -30
```

tool result:

```
TreeItem.d.ts
TreeItem.js
TreeItem.test.js
index.d.ts
index.js
/* eslint-disable jsx-a11y/click-events-have-key-events, jsx-a11y/no-static-element-interactions  */
import * as React from 'react';
import clsx from 'clsx';
import PropTypes from 'prop-types';
import Typography from '@material-ui/core/Typography';
import Collapse from '@material-ui/core/Collapse';
import { fade, withStyles, useTheme } from '@material-ui/core/styles';
import { useForkRef } from '@material-ui/core/utils';
import TreeViewContext from '../TreeView/TreeViewContext';

export const styles = (theme) => ({
  /* Styles applied to the root element. */
  root: {
    listStyle: 'none',
    margin: 0,
    padding: 0,
    outline: 0,
    WebkitTapHighlightColor: 'transparent',
    '&:focus > $content $label': {
      backgroundColor: theme.palette.action.hover,
    },
    '&$selected > $content $label': {
      backgroundColor: fade(theme.palette.primary.main, theme.palette.action.selectedOpacity),
    },
    '&$selected > $content $label:hover, &$selected:focus > $content $label': {
      backgroundColor: fade(
        theme.palette.primary.main,
        theme.palette.action.selectedOpacity + theme.palette.action.hoverOpacity,
      ),
      // Reset on touch devices, it doesn't add specificity
      '@media (hover: none)': {
        backgroundColor: 'transparent',
      },
    },
  },
  /* Pseudo-class applied to the root element when expanded. */
  expanded: {},
  /* Pseudo-class applied to the root element when selected. */
  selected: {},
  /* Styles applied to the `role="group"` element. */
  group: {
    margin: 0,
    padding: 0,
    marginLeft: 17,
  },
  /* Styles applied to the tree node content. */
  content: {
    width: '100%',
    display: 'flex',
    alignItems: 'center',
    cursor: 'pointer',
  },
  /* Styles applied to the tree node icon and collapse/expand icon. */
  iconContainer: {
    marginRight: 4,
    width: 15,
    display: 'flex',
    flexShrink: 0,
    justifyContent: 'center',
    '& svg': {
      fontSize: 18,
    },
  },
  /* Styles applied to the label element. */
  label: {
    width: '100%',
    paddingLeft: 4,
    position: 'relative',
    '&:hover': {
      backgroundColor: theme.palette.action.hover,
      // Reset on touch devices, it doesn't add specificity
      '@media (hover: none)': {
        backgroundColor: 'transparent',
      },
    },
  },
});

const isPrintableCharacter = (str) => {
  return str && str.length === 1 && str.match(/\S/);
};

const TreeItem = React.forwardRef(function TreeItem(props, ref) {
  const {
    children,
    classes,
    className,
    collapseIcon,
    endIcon,
    expandIcon,
    icon: iconProp,
    label,
    nodeId,
    onClick,
    onFocus,
    onKeyDown,
    onMouseDown,
    TransitionComponent = Collapse,
    TransitionProps,
    ...other
  } = props;

  const {
    icons: contextIcons,
    focus,
    focusFirstNode,
    focusLastNode,
    focusNextNode,
    focusPreviousNode,
    focusByFirstCharacter,
    selectNode,
    selectRange,
    selectNextNode,
    selectPreviousNode,
    rangeSelectToFirst,
    rangeSelectToLast,
    selectAllNodes,
    expandAllSiblings,
    toggleExpansion,
    isExpanded,
    isFocused,
    isSelected,
    isTabbable,
    multiSelect,
    getParent,
    mapFirstChar,
    addNodeToNodeMap,
    removeNodeFromNodeMap,
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

  if (!icon) {
    if (expandable) {
      if (!expanded) {
        icon = expandIcon || icons.defaultExpandIcon;
      } else {
        icon = collapseIcon || icons.defaultCollapseIcon;
      }

      if (!icon) {
        icon = icons.defaultParentIcon;
      }
    } else {
      icon = endIcon || icons.defaultEndIcon;
    }
  }

  const handleClick = (event) => {
    if (!focused) {
      focus(nodeId);
    }

    const multiple = multiSelect && (event.shiftKey || event.ctrlKey || event.metaKey);

    // If already expanded and trying to toggle selection don't close
    if (expandable && !(multiple && isExpanded(nodeId))) {
      toggleExpansion(event, nodeId);
    }

    if (multiple) {
      if (event.shiftKey) {
        selectRange(event, { end: nodeId });
      } else {
        selectNode(event, nodeId, true);
      }
    } else {
      selectNode(event, nodeId);
    }

    if (onClick) {
      onClick(event);
    }
  };

  const handleMouseDown = (event) => {
    if (event.shiftKey || event.ctrlKey || event.metaKey) {
      event.preventDefault();
    }

    if (onMouseDown) {
      onMouseDown(event);
    }
  };

  const handleNextArrow = (event) => {
    if (expandable) {
      if (expanded) {
        focusNextNode(nodeId);
      } else {
        toggleExpansion(event);
      }
    }
    return true;
  };

  const handlePreviousArrow = (event) => {
    if (expanded) {
      toggleExpansion(event, nodeId);
      return true;
    }

    const parent = getParent(nodeId);
    if (parent) {
      focus(parent);
      return true;
    }
    return false;
  };

  const handleKeyDown = (event) => {
    let flag = false;
    const key = event.key;

    if (event.altKey || event.currentTarget !== event.target) {
      return;
    }

    const ctrlPressed = event.ctrlKey || event.metaKey;

    switch (key) {
      case ' ':
        if (nodeRef.current === event.currentTarget) {
          if (multiSelect && event.shiftKey) {
            flag = selectRange(event, { end: nodeId });
          } else if (multiSelect) {
            flag = sele
[... 7599 more characters not shown]
```

**tool call: Bash**

```bash
cd packages/material-ui-lab/src/TreeItem && grep -n "onIconClick\|onLabelClick" -A30 TreeItem.test.js | head -80; ls /work/mui__material-ui-20657/repo/docs/pages/api-docs 2>/dev/null | grep -i tree; ls /work/mui__material-ui-20657/repo/docs/pages/api | grep -i tree
```

tool result:

```
(eval):cd:1: no such file or directory: packages/material-ui-lab/src/TreeItem
tree-item.js
tree-item.md
tree-view.js
tree-view.md
ls: /work/mui__material-ui-20657/repo/docs/pages/api: No such file or directory
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-20657/repo && grep -n "preventDefault\|IconClick\|LabelClick" packages/material-ui-lab/src/TreeItem/TreeItem.test.js packages/material-ui-lab/src/TreeView/*.test.js; cat docs/pages/api-docs/tree-item.md | sed -n 20,50p
```

tool result:

```
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:1216:    keydownEvent.preventDefault = spy();
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:1218:    expect(keydownEvent.preventDefault.callCount).to.equal(0);



## Component name

The `MuiTreeItem` name can be used for providing [default props](/customization/globals/#default-props) or [style overrides](/customization/globals/#css) at the theme level.

## Props

| Name | Type | Default | Description |
|:-----|:-----|:--------|:------------|
| <span class="prop-name">children</span> | <span class="prop-type">node</span> |  | The content of the component. |
| <span class="prop-name">classes</span> | <span class="prop-type">object</span> |  | Override or extend the styles applied to the component. See [CSS API](#css) below for more details. |
| <span class="prop-name">collapseIcon</span> | <span class="prop-type">node</span> |  | The icon used to collapse the node. |
| <span class="prop-name">endIcon</span> | <span class="prop-type">node</span> |  | The icon displayed next to a end node. |
| <span class="prop-name">expandIcon</span> | <span class="prop-type">node</span> |  | The icon used to expand the node. |
| <span class="prop-name">icon</span> | <span class="prop-type">node</span> |  | The icon to display next to the tree node's label. |
| <span class="prop-name">label</span> | <span class="prop-type">node</span> |  | The tree node label. |
| <span class="prop-name required">nodeId&nbsp;*</span> | <span class="prop-type">string</span> |  | The id of the node. |
| <span class="prop-name">TransitionComponent</span> | <span class="prop-type">elementType</span> | <span class="prop-default">Collapse</span> | The component used for the transition. [Follow this guide](/components/transitions/#transitioncomponent-prop) to learn more about the requirements for this component. |
| <span class="prop-name">TransitionProps</span> | <span class="prop-type">object</span> |  | Props applied to the [`Transition`](http://reactcommunity.org/react-transition-group/transition#Transition-props) element. |

The `ref` is forwarded to the root element.

Any other props supplied will be provided to the root element (native element).

## CSS

| Rule name | Global class | Description |
|:-----|:-------------|:------------|
| <span class="prop-name">root</span> | <span class="prop-name">.MuiTreeItem-root</span> | Styles applied to the root element.
```

**assistant:** I'll add `onIconClick` and `onLabelClick` props. When a handler calls `event.preventDefault()`, the node won't expand or collapse.

**tool call: Bash**

```bash
python3 - <<'EOF'
p='packages/material-ui-lab/src/TreeItem/TreeItem.js'
s=open(p).read()
s=s.replace("""    onFocus,
    onKeyDown,
    onMouseDown,
    TransitionComponent""","""    onFocus,
    onIconClick,
    onKeyDown,
    onLabelClick,
    onMouseDown,
    TransitionComponent""")
s=s.replace("""    if (expandable && !(multiple && isExpanded(nodeId))) {""","""    if (expandable && !event.defaultPrevented && !(multiple && isExpanded(nodeId))) {""")
s=s.replace("""        <div className={classes.iconContainer}>{icon}</div>
        <Typography component="div" className={classes.label}>""","""        <div onClick={onIconClick} className={classes.iconContainer}>
          {icon}
        </div>
        <Typography onClick={onLabelClick} component="div" className={classes.label}>""")
s=s.replace("""  /**
   * @ignore
   */
  onKeyDown: PropTypes.func,
  /**
   * @ignore
   */
  onMouseDown""","""  /**
   * `onClick` handler for the icon container. Call `event.preventDefault()` to prevent `onNodeToggle` from being called.
   */
  onIconClick: PropTypes.func,
  /**
   * @ignore
   */
  onKeyDown: PropTypes.func,
  /**
   * `onClick` handler for the label container. Call `event.preventDefault()` to prevent `onNodeToggle` from being called.
   */
  onLabelClick: PropTypes.func,
  /**
   * @ignore
   */
  onMouseDown""")
open(p,'w').write(s)
p='packages/material-ui-lab/src/TreeItem/TreeItem.d.ts'
s=open(p).read()
s=s.replace("""  nodeId: string;
""","""  nodeId: string;
  /**
   * `onClick` handler for the icon container. Call `event.preventDefault()` to prevent `onNodeToggle` from being called.
   */
  onIconClick?: React.MouseEventHandler;
  /**
   * `onClick` handler for the label container. Call `event.preventDefault()` to prevent `onNodeToggle` from being called.
   */
  onLabelClick?: React.MouseEventHandler;
""")
open(p,'w').write(s)
p='docs/pages/api-docs/tree-item.md'
s=open(p).read()
a='| <span class="prop-name required">nodeId&nbsp;*</span> | <span class="prop-type">string</span> |  | The id of the node. |\n'
s=s.replace(a,a+'| <span class="prop-name">onIconClick</span> | <span class="prop-type">func</span> |  | `onClick` handler for the icon container. Call `event.preventDefault()` to prevent `onNodeToggle` from being called. |\n| <span class="prop-name">onLabelClick</span> | <span class="prop-type">func</span> |  | `onClick` handler for the label container. Call `event.preventDefault()` to prevent `onNodeToggle` from being called. |\n')
open(p,'w').write(s)
EOF
git diff --stat
```

tool result:

```
 docs/pages/api-docs/tree-item.md                   |   2 +
 package.json                                       |  10 +-
 .../material-ui-lab/src/TreeItem/TreeItem.d.ts     |   8 +
 packages/material-ui-lab/src/TreeItem/TreeItem.js  |  18 +-
 yarn.lock                                          | 283 ++++-----------------
 5 files changed, 84 insertions(+), 237 deletions(-)
```

**assistant:** `package.json` and `yarn.lock` show changes that I didn't make. Let me look at them.

**tool call: Bash**

```bash
git diff package.json; git log --oneline -2
```

tool result:

```
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
72a477f3c Skip locales in dev
74c6155f2 [docs] Parse markdown on mount (#20601)
```

**assistant:** Those dependency changes come from the environment setup, not from me, so I'll leave them alone. Next, a quick repro test:

**tool call: Bash**

```bash
cat > packages/material-ui-lab/src/TreeItem/repro.test.js <<'EOF'
import * as React from 'react';
import { expect } from 'chai';
import { spy } from 'sinon';
import { createClientRender, fireEvent } from 'test/utils/createClientRender';
import TreeItem from './TreeItem';
import TreeView from '../TreeView';

describe('repro', () => {
  const render = createClientRender();
  it('label preventDefault blocks expansion, icon click expands', () => {
    const onLabelClick = spy((e) => e.preventDefault());
    const onIconClick = spy();
    const { getByTestId, getByText } = render(
      <TreeView defaultExpandIcon={<span>icon</span>}>
        <TreeItem nodeId="1" label="one" data-testid="one" onLabelClick={onLabelClick} onIconClick={onIconClick}>
          <TreeItem nodeId="2" label="two" />
        </TreeItem>
      </TreeView>,
    );
    fireEvent.click(getByText('one'));
    expect(onLabelClick.callCount).to.equal(1);
    expect(getByTestId('one')).to.have.attribute('aria-expanded', 'false');
    expect(getByTestId('one')).to.have.attribute('aria-selected', 'true');
    fireEvent.click(getByText('icon'));
    expect(onIconClick.callCount).to.equal(1);
    expect(getByTestId('one')).to.have.attribute('aria-expanded', 'true');
  });
});
EOF
/work/mui__material-ui-20657/bin/envrun 'yarn -s mocha packages/material-ui-lab/src/TreeItem/repro.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js 2>&1 | tail -20'
```

tool result:

```
    at Object.exports.main (/testbed/node_modules/mocha/lib/cli/cli.js:68:6)
    at Object.<anonymous> (/testbed/node_modules/mocha/bin/mocha:133:29)
    at Module._compile (node:internal/modules/cjs/loader:1198:14)
    at Object.Module._extensions..js (node:internal/modules/cjs/loader:1252:10)
    at Module.load (node:internal/modules/cjs/loader:1076:32)
    at Function.Module._load (node:internal/modules/cjs/loader:911:12)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:81:12)
    at node:internal/main/run_main_module:22:47
/testbed/node_modules/mocha/node_modules/yargs/lib/usage.js:240
      .concat(Object.keys(yargs.parsed.newAliases) || [])
                     ^

TypeError: Cannot convert undefined or null to object
    at Function.keys (<anonymous>)
    at Object.help (/testbed/node_modules/mocha/node_modules/yargs/lib/usage.js:240:22)
    at Object.self.showHelp (/testbed/node_modules/mocha/node_modules/yargs/lib/usage.js:432:15)
    at Array.<anonymous> (/testbed/node_modules/mocha/lib/cli/cli.js:50:13)
    at Object.fail (/testbed/node_modules/mocha/node_modules/yargs/lib/usage.js:41:17)
    at /testbed/node_modules/mocha/node_modules/yargs/lib/command.js:246:36
    at processTicksAndRejections (node:internal/process/task_queues:96:5)
```

**tool call: Bash**

```bash
grep -n '"test' package.json; cat .mocharc.js
```

tool result:

```
34:    "test": "yarn lint && yarn typescript && yarn test:coverage",
35:    "test:coverage": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha 'packages/**/*.test.js' 'docs/**/*.test.js' --exclude '**/node_modules/**' && nyc report -r lcovonly",
36:    "test:coverage:html": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha 'packages/**/**/*.test.js' --exclude '**/node_modules/**' && nyc report --reporter=html",
37:    "test:karma": "cross-env NODE_ENV=test karma start test/karma.conf.js",
38:    "test:regressions": "yarn test:regressions:build && rimraf test/regressions/screenshots/chrome/* && vrtest run --config test/vrtest.config.js --record",
39:    "test:regressions:build": "webpack --config test/regressions/webpack.config.js",
40:    "test:umd": "node packages/material-ui/test/umd/run.js",
41:    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/*.test.js' 'docs/**/*.test.js' 'scripts/**/*.test.js' --exclude '**/node_modules/**'",
42:    "test:watch": "yarn test:unit --watch",
module.exports = {
  recursive: true,
  reporter: 'dot',
  require: [require.resolve('@babel/register'), require.resolve('./test/utils/setup')],
};
```

**tool call: Bash**

```bash
/work/mui__material-ui-20657/bin/envrun 'NODE_ENV=test npx mocha packages/material-ui-lab/src/TreeItem/repro.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js 2>&1 | tail -30'
```

tool result:

```
Command did not complete within its 120s timeout and was moved to the background (ID: btbz1n8k6). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/a9afa872-b3af-4356-9fa6-eedf4b322b65/tasks/btbz1n8k6.output. You will be notified when it completes. To check interim output, use Read on that file path.
```

**tool call: Bash**

```bash
sleep 120; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/a9afa872-b3af-4356-9fa6-eedf4b322b65/tasks/btbz1n8k6.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
sleep 240; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/a9afa872-b3af-4356-9fa6-eedf4b322b65/tasks/btbz1n8k6.output
```

tool result:

```
(Bash completed with no output)
```

**assistant:** Babel compilation is slow the first time. I'll wait for the run to finish.

**tool call: Bash**

```bash
sleep 400; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/a9afa872-b3af-4356-9fa6-eedf4b322b65/tasks/btbz1n8k6.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
/work/mui__material-ui-20657/bin/envrun 'ps aux | grep -v grep | grep -i mocha | head; nproc'
```

tool result:

```
root        35  0.0  0.0 289612  6288 ?        Ss   10:58   0:00 bash -lc NODE_ENV=test npx mocha packages/material-ui-lab/src/TreeItem/repro.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js 2>&1 | tail -30
root        43  0.0  1.0 1139368 80880 ?       Sl   10:58   0:00 node --no-opt -r /proc/.reset /usr/local/nvm/versions/node/v16.20.2/bin/npx mocha packages/material-ui-lab/src/TreeItem/repro.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js
root        55  0.0  0.0 287844  3328 ?        S    10:58   0:00 sh -c -- mocha packages/material-ui-lab/src/TreeItem/repro.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js
root        56  0.9  2.5 997176 207560 ?       Sl   10:58   0:08 node --no-opt -r /proc/.reset /testbed/node_modules/.bin/mocha packages/material-ui-lab/src/TreeItem/repro.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js
14
```

**assistant:** Mocha has used only 8s of CPU, so it's probably done but not exiting (`tail` only prints once the process ends). I'll kill it and rerun with `--exit`.

**tool call: Bash**

```bash
/work/mui__material-ui-20657/bin/envrun 'pkill -f mocha; NODE_ENV=test timeout 300 npx mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js > /tmp/out.txt 2>&1; tail -30 /tmp/out.txt'
```

tool result:

```
Exit code 143
```

**assistant:** `pkill -f mocha` matched and killed its own shell, since that command line contains "mocha". Running again without it:

**tool call: Bash**

```bash
/work/mui__material-ui-20657/bin/envrun 'NODE_ENV=test timeout 300 npx mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js > /tmp/out.txt 2>&1; tail -30 /tmp/out.txt'
```

tool result:

```
      at /testbed/node_modules/@testing-library/dom/dist/query-helpers.js:76:38
      at getByRole (node_modules/@testing-library/dom/dist/query-helpers.js:59:17)
      at Context.<anonymous> (packages/material-ui-lab/src/TreeView/TreeView.test.js:227:14)
      at processImmediate (node:internal/timers:466:21)

  84) <TreeView />
       Accessibility
         (TreeView) should have the attribute `aria-multiselectable=true if using multi select`:
     TestingLibraryElementError: Unable to find an element with the role "tree"

Here are the available roles:

  document:

  Name "":
  [36m<body />[39m

  --------------------------------------------------

[36m<body>[39m
  [36m<div />[39m
[36m</body>[39m
      at Object.getElementError (node_modules/@testing-library/dom/dist/config.js:30:19)
      at /testbed/node_modules/@testing-library/dom/dist/query-helpers.js:76:38
      at getByRole (node_modules/@testing-library/dom/dist/query-helpers.js:59:17)
      at Context.<anonymous> (packages/material-ui-lab/src/TreeView/TreeView.test.js:233:14)
      at processImmediate (node:internal/timers:466:21)
```

**assistant:** A lot of tests are failing, and the rendered body is empty. That looks like an environment problem. Checking the beginning of the output:

**tool call: Bash**

```bash
/work/mui__material-ui-20657/bin/envrun 'grep -n "passing\|failing\|pending" /tmp/out.txt; grep -n -m3 -A25 "  1) " /tmp/out.txt | head -60'
```

tool result:

```
97:  2 passing (403ms)
98:  84 failing
100:  1) repro
101-       label preventDefault blocks expansion, icon click expands:
102-     Error: Uncaught [Error: Warning: %s is deprecated in StrictMode. %s was passed an instance of %s which is inside StrictMode. Instead, add a ref directly to the element you want to reference. Learn more about using refs safely here: https://fb.me/react-strict-mode-find-node%s]
103-    at reportException (/testbed/node_modules/jsdom/lib/jsdom/living/helpers/runtime-script-errors.js:62:24)
104-    at innerInvokeEventListeners (/testbed/node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:346:9)
105-    at invokeEventListeners (/testbed/node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:281:3)
106-    at HTMLUnknownElementImpl._dispatch (/testbed/node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:228:9)
107-    at HTMLUnknownElementImpl.dispatchEvent (/testbed/node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:101:17)
108-    at HTMLUnknownElement.dispatchEvent (/testbed/node_modules/jsdom/lib/jsdom/living/generated/EventTarget.js:207:34)
109-    at Object.invokeGuardedCallbackDev (/testbed/node_modules/react-dom/cjs/react-dom.development.js:237:16)
110-    at invokeGuardedCallback (/testbed/node_modules/react-dom/cjs/react-dom.development.js:292:31)
111-    at commitRootImpl (/testbed/node_modules/react-dom/cjs/react-dom.development.js:22541:9)
112-    at unstable_runWithPriority (/testbed/node_modules/scheduler/cjs/scheduler.development.js:653:12)
113-    at runWithPriority$1 (/testbed/node_modules/react-dom/cjs/react-dom.development.js:11039:10)
114-    at commitRoot (/testbed/node_modules/react-dom/cjs/react-dom.development.js:22381:3)
115-    at finishSyncRender (/testbed/node_modules/react-dom/cjs/react-dom.development.js:21807:3)
116-    at performSyncWorkOnRoot (/testbed/node_modules/react-dom/cjs/react-dom.development.js:21793:7)
117-    at /testbed/node_modules/react-dom/cjs/react-dom.development.js:11089:24
118-    at unstable_runWithPriority (/testbed/node_modules/scheduler/cjs/scheduler.development.js:653:12)
119-    at runWithPriority$1 (/testbed/node_modules/react-dom/cjs/react-dom.development.js:11039:10)
120-    at flushSyncCallbackQueueImpl (/testbed/node_modules/react-dom/cjs/react-dom.development.js:11084:7)
121-    at flushSyncCallbackQueue (/testbed/node_modules/react-dom/cjs/react-dom.development.js:11072:3)
122-    at batchedUpdates$1 (/testbed/node_modules/react-dom/cjs/react-dom.development.js:21862:7)
123-    at act (/testbed/node_modules/react-dom/cjs/react-dom-test-utils.development.js:929:14)
124-    at Function.click (/testbed/node_modules/@testing-library/react/dist/pure.js:150:28)
125-    at Context.<anonymous> (/testbed/packages/material-ui-lab/src/TreeItem/repro.test.js:24:15)
```

**thinking:**

```
The label-click assertions passed, but the icon click fails because expanding mounts `Collapse`, triggering a StrictMode `findDOMNode` warning that the test setup escalates into an error—likely causing the subsequent 84 failures. I'll run the existing suites without the repro to confirm.


```

**tool call: Bash**

```bash
/work/mui__material-ui-20657/bin/envrun 'NODE_ENV=test timeout 300 npx mocha --exit packages/material-ui-lab/src/TreeItem/TreeItem.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js > /tmp/out.txt 2>&1; grep -n "passing\|failing\|pending" /tmp/out.txt; grep -m5 -A3 "^  [0-9]*) " /tmp/out.txt'
```

tool result:

```
Exit code 1
9:  84 passing (1s)
```

**assistant:** All 84 existing tests pass. Now I'll see how the existing tests avoid the StrictMode problem when they expand nodes:

**tool call: Bash**

```bash
grep -n "createClientRender(" packages/material-ui-lab/src/TreeItem/TreeItem.test.js
```

tool result:

```
13:  const render = createClientRender({ strict: false });
```

**tool call: Bash**

```bash
sed -i '' 's/createClientRender();/createClientRender({ strict: false });/' packages/material-ui-lab/src/TreeItem/repro.test.js
/work/mui__material-ui-20657/bin/envrun 'NODE_ENV=test timeout 300 npx mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js > /tmp/out.txt 2>&1; grep -n "passing\|failing" /tmp/out.txt; git stash push packages/material-ui-lab/src/TreeItem/TreeItem.js -q; NODE_ENV=test timeout 300 npx mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js 2>&1 | grep -A3 "passing\|failing"; git stash pop -q; git diff --stat -- packages'
```

tool result:

```
8:  1 passing (164ms)
  0 passing (104ms)
  1 failing

  1) repro
       label preventDefault blocks expansion, icon click expands:
 packages/material-ui-lab/src/TreeItem/TreeItem.d.ts |  8 ++++++++
 packages/material-ui-lab/src/TreeItem/TreeItem.js   | 18 +++++++++++++++---
 2 files changed, 23 insertions(+), 3 deletions(-)
```

**assistant:** The repro passes with the fix and fails without it. Last steps: delete the repro, then lint and format-check the changed files.

**tool call: Bash**

```bash
rm packages/material-ui-lab/src/TreeItem/repro.test.js
/work/mui__material-ui-20657/bin/envrun 'npx eslint packages/material-ui-lab/src/TreeItem/ && npx prettier --check packages/material-ui-lab/src/TreeItem/TreeItem.js packages/material-ui-lab/src/TreeItem/TreeItem.d.ts && echo OK'; git status --short
```

tool result:

```
Checking formatting...
All matched files use Prettier code style!
OK

 M docs/pages/api-docs/tree-item.md
 M package.json
 M packages/material-ui-lab/src/TreeItem/TreeItem.d.ts
 M packages/material-ui-lab/src/TreeItem/TreeItem.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
```

**assistant:** `TreeItem` now has two new props, `onLabelClick` and `onIconClick`. If either handler calls `event.preventDefault()`, the click won't expand or collapse the node. For the case in the issue, you'd write:

```jsx
<TreeItem
  nodeId="1"
  label="Parent"
  onLabelClick={(event) => {
    event.preventDefault(); // don't expand/collapse
    showNodeInfo('1');      // still focuses and selects the node
  }}
>
  …
</TreeItem>
```

Clicking the expand/collapse icon still toggles the node as usual.

**Changes:**
- `packages/material-ui-lab/src/TreeItem/TreeItem.js`: the click handler on the row now skips `toggleExpansion` if the event was already prevented. Both handlers are attached to their elements (the icon container and the label), and their PropTypes are added. Focus, selection and `onClick` still work the same either way.
- `TreeItem.d.ts`: types for both props (`React.MouseEventHandler`).
- `docs/pages/api-docs/tree-item.md`: both props added to the props table.

**Checks:**
- I wrote a small test where `onLabelClick` calls `preventDefault()`. It failed before the change and passed after: clicking the label selected the node without expanding it, and clicking the icon expanded it.
- All 84 existing `TreeItem` and `TreeView` tests pass, and ESLint and Prettier report no problems in the changed files. I deleted the test afterwards.

The working tree also shows changes I didn't make: `package.json` and `yarn.lock` are modified, and `Dockerfile` and `custom-reporter.js` are untracked. They look like part of the environment setup, so I left them alone. To run mocha here you need `--exit`, otherwise it finishes the tests but never returns.

_session end: success, turns 20, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 3.3 s: yarn -s mocha packages/material-ui-lab/src/TreeItem/repro.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js 2>&1 | tail -20
- `rc=0` 0.14 s: ps aux | grep -v grep | grep -i mocha | head; nproc
- `rc=143` 901.09 s: NODE_ENV=test npx mocha packages/material-ui-lab/src/TreeItem/repro.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js 2>&1 | tail -30
- `rc=143` 0.13 s: pkill -f mocha; NODE_ENV=test timeout 300 npx mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js > /tmp/out.txt 2>&1; tail -30 /tmp/out.txt
- `rc=0` 4.37 s: NODE_ENV=test timeout 300 npx mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js > /tmp/out.txt 2>&1; tail -30 /tmp/out.txt
- `rc=0` 0.21 s: grep -n "passing\|failing\|pending" /tmp/out.txt; grep -n -m3 -A25 "  1) " /tmp/out.txt | head -60
- `rc=1` 3.54 s: NODE_ENV=test timeout 300 npx mocha --exit packages/material-ui-lab/src/TreeItem/TreeItem.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js > /tmp/out.txt 2>&1; grep -n "passing\|failing\|pending" /tmp/out.txt; grep -m5 -A3 "^  [0-9]*) " /tmp/out.txt
- `rc=0` 8.6 s: NODE_ENV=test timeout 300 npx mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js > /tmp/out.txt 2>&1; grep -n "passing\|failing" /tmp/out.txt; git stash push packages/material-ui-lab/src/TreeItem/TreeItem.js -q; NODE_ENV=test timeout 300 npx mocha --exit packages/material-ui-lab/src/TreeItem/repro.test.js 2>&1 | grep -A3 "passing\|failing"; git stash pop -q; git diff --stat -- packages
- `rc=0` 4.97 s: npx eslint packages/material-ui-lab/src/TreeItem/ && npx prettier --check packages/material-ui-lab/src/TreeItem/TreeItem.js packages/material-ui-lab/src/TreeItem/TreeItem.d.ts && echo OK
