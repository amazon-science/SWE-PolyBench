# Instance: mui__material-ui-20232

- Final resolved (evaluator, logs/mui__material-ui-20232_result.json): True
- Run state: DONE
- One attempt. Duration 1292.9 s, turns 22, actor cost $0.5718966000000002, container commands 7
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/mui__material-ui-20232/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-20232/repo. Consider the following issue description:

<issue_description>
[TreeItem] TreeItem hijacks focus when typing on an input box that updates it.
I am using a <TextField /> to change the contents of a TreeView and a matching TreeItem is being focused when I backspace.

CodeSandbox: https://codesandbox.io/s/bold-hill-rw9y5

- [X] The issue is present in the latest release.
- [X] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Current Behavior 😯

The focus is lost from the text field and hijacked by the TreeItem

## Expected Behavior 🤔

The focus should remain on the TextField since the user never selected or focused on the TreeItem.

1. Go to the sandbox: https://codesandbox.io/s/bold-hill-rw9y5
2. Collapse and expand a category.
3. Click the TextField search box and type "bananas"
4. Start deleting and you'll notice you loose focus mid way before you clear the query.

## Context 🔦
I want to be able to filter out items from a tree view.


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-20232/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-20232/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-20232/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-20232/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/mui__material-ui-20232/repo; ls packages/material-ui-lab/src/TreeItem packages/material-ui-lab/src/TreeView; grep -n "focus" packages/material-ui-lab/src/TreeItem/TreeItem.js packages/material-ui-lab/src/TreeView/TreeView.js
```

tool result:

```
packages/material-ui-lab/src/TreeItem:
TreeItem.d.ts
TreeItem.js
TreeItem.test.js
index.d.ts
index.js

packages/material-ui-lab/src/TreeView:
TreeView.d.ts
TreeView.js
TreeView.test.js
TreeViewContext.js
index.d.ts
index.js
packages/material-ui-lab/src/TreeItem/TreeItem.js:19:    '&:focus > $content $label': {
packages/material-ui-lab/src/TreeItem/TreeItem.js:25:    '&$selected > $content $label:hover, &$selected:focus > $content $label': {
packages/material-ui-lab/src/TreeItem/TreeItem.js:105:    focus,
packages/material-ui-lab/src/TreeItem/TreeItem.js:106:    focusFirstNode,
packages/material-ui-lab/src/TreeItem/TreeItem.js:107:    focusLastNode,
packages/material-ui-lab/src/TreeItem/TreeItem.js:108:    focusNextNode,
packages/material-ui-lab/src/TreeItem/TreeItem.js:109:    focusPreviousNode,
packages/material-ui-lab/src/TreeItem/TreeItem.js:110:    focusByFirstCharacter,
packages/material-ui-lab/src/TreeItem/TreeItem.js:140:  const focused = isFocused ? isFocused(nodeId) : false;
packages/material-ui-lab/src/TreeItem/TreeItem.js:163:    if (!focused) {
packages/material-ui-lab/src/TreeItem/TreeItem.js:164:      focus(nodeId);
packages/material-ui-lab/src/TreeItem/TreeItem.js:203:      focusByFirstCharacter(nodeId, key);
packages/material-ui-lab/src/TreeItem/TreeItem.js:212:        focusNextNode(nodeId);
packages/material-ui-lab/src/TreeItem/TreeItem.js:228:      focus(parent);
packages/material-ui-lab/src/TreeItem/TreeItem.js:270:        focusNextNode(nodeId);
packages/material-ui-lab/src/TreeItem/TreeItem.js:277:        focusPreviousNode(nodeId);
packages/material-ui-lab/src/TreeItem/TreeItem.js:298:        focusFirstNode();
packages/material-ui-lab/src/TreeItem/TreeItem.js:305:        focusLastNode();
packages/material-ui-lab/src/TreeItem/TreeItem.js:331:    if (!focused && tabbable) {
packages/material-ui-lab/src/TreeItem/TreeItem.js:332:      focus(nodeId);
packages/material-ui-lab/src/TreeItem/TreeItem.js:363:    if (focused) {
packages/material-ui-lab/src/TreeItem/TreeItem.js:364:      nodeRef.current.focus();
packages/material-ui-lab/src/TreeItem/TreeItem.js:366:  }, [focused]);
packages/material-ui-lab/src/TreeView/TreeView.js:59:  const [focused, setFocused] = React.useState(null);
packages/material-ui-lab/src/TreeView/TreeView.js:91:  const isFocused = (id) => focused === id;
packages/material-ui-lab/src/TreeView/TreeView.js:129:  const focus = (id) => {
packages/material-ui-lab/src/TreeView/TreeView.js:136:  const focusNextNode = (id) => focus(getNextNode(id));
packages/material-ui-lab/src/TreeView/TreeView.js:137:  const focusPreviousNode = (id) => focus(getPreviousNode(id));
packages/material-ui-lab/src/TreeView/TreeView.js:138:  const focusFirstNode = () => focus(getFirstNode());
packages/material-ui-lab/src/TreeView/TreeView.js:139:  const focusLastNode = () => focus(getLastNode());
packages/material-ui-lab/src/TreeView/TreeView.js:141:  const focusByFirstCharacter = (id, char) => {
packages/material-ui-lab/src/TreeView/TreeView.js:176:      focus(firstCharIds[index]);
packages/material-ui-lab/src/TreeView/TreeView.js:184:  const toggleExpansion = (event, value = focused) => {
packages/material-ui-lab/src/TreeView/TreeView.js:490:        focus,
packages/material-ui-lab/src/TreeView/TreeView.js:491:        focusFirstNode,
packages/material-ui-lab/src/TreeView/TreeView.js:492:        focusLastNode,
packages/material-ui-lab/src/TreeView/TreeView.js:493:        focusNextNode,
packages/material-ui-lab/src/TreeView/TreeView.js:494:        focusPreviousNode,
packages/material-ui-lab/src/TreeView/TreeView.js:495:        focusByFirstCharacter,
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-20232/repo; sed -n 50,140p packages/material-ui-lab/src/TreeView/TreeView.js; sed -n 380,520p packages/material-ui-lab/src/TreeView/TreeView.js; sed -n 320,420p packages/material-ui-lab/src/TreeItem/TreeItem.js
```

tool result:

```
    disableSelection = false,
    multiSelect = false,
    expanded: expandedProp,
    onNodeSelect,
    onNodeToggle,
    selected: selectedProp,
    ...other
  } = props;
  const [tabbable, setTabbable] = React.useState(null);
  const [focused, setFocused] = React.useState(null);

  const nodeMap = React.useRef({});
  const firstCharMap = React.useRef({});
  const visibleNodes = React.useRef([]);

  const [expanded, setExpandedState] = useControlled({
    controlled: expandedProp,
    default: defaultExpanded,
    name: 'TreeView',
  });

  const [selected, setSelectedState] = useControlled({
    controlled: selectedProp,
    default: defaultSelected,
    name: 'TreeView',
  });

  /*
   * Status Helpers
   */
  const isExpanded = React.useCallback(
    (id) => (Array.isArray(expanded) ? expanded.indexOf(id) !== -1 : false),
    [expanded],
  );

  const isSelected = React.useCallback(
    (id) => (Array.isArray(selected) ? selected.indexOf(id) !== -1 : selected === id),
    [selected],
  );

  const isTabbable = (id) => tabbable === id;
  const isFocused = (id) => focused === id;

  /*
   * Node Helpers
   */

  const getNextNode = (id) => {
    const nodeIndex = visibleNodes.current.indexOf(id);
    if (nodeIndex !== -1 && nodeIndex + 1 < visibleNodes.current.length) {
      return visibleNodes.current[nodeIndex + 1];
    }
    return null;
  };

  const getPreviousNode = (id) => {
    const nodeIndex = visibleNodes.current.indexOf(id);
    if (nodeIndex !== -1 && nodeIndex - 1 >= 0) {
      return visibleNodes.current[nodeIndex - 1];
    }
    return null;
  };

  const getLastNode = () => visibleNodes.current[visibleNodes.current.length - 1];
  const getFirstNode = () => visibleNodes.current[0];
  const getParent = (id) => nodeMap.current[id].parent;

  const getNodesInRange = (a, b) => {
    const aIndex = visibleNodes.current.indexOf(a);
    const bIndex = visibleNodes.current.indexOf(b);
    const start = Math.min(aIndex, bIndex);
    const end = Math.max(aIndex, bIndex);
    return visibleNodes.current.slice(start, end + 1);
  };

  /*
   * Focus Helpers
   */

  const focus = (id) => {
    if (id) {
      setTabbable(id);
      setFocused(id);
    }
  };

  const focusNextNode = (id) => focus(getNextNode(id));
  const focusPreviousNode = (id) => focus(getPreviousNode(id));
  const focusFirstNode = () => focus(getFirstNode());
  const focusLastNode = () => focus(getLastNode());

    );

  const selectAllNodes = (event) =>
    selectRange(event, { start: getFirstNode(), end: getLastNode() });

  /*
   * Mapping Helpers
   */

  const addNodeToNodeMap = (id, childrenIds) => {
    const currentMap = nodeMap.current[id];
    nodeMap.current[id] = { ...currentMap, children: childrenIds, id };

    childrenIds.forEach((childId) => {
      const currentChildMap = nodeMap.current[childId];
      nodeMap.current[childId] = { ...currentChildMap, parent: id, id: childId };
    });
  };

  const getNodesToRemove = React.useCallback((id) => {
    const map = nodeMap.current[id];
    const nodes = [];
    if (map) {
      nodes.push(id);
      if (map.children) {
        nodes.push(...map.children);
        map.children.forEach((node) => {
          nodes.push(...getNodesToRemove(node));
        });
      }
    }
    return nodes;
  }, []);

  const removeNodeFromNodeMap = React.useCallback(
    (id) => {
      const nodes = getNodesToRemove(id);
      const newMap = { ...nodeMap.current };

      nodes.forEach((node) => {
        const map = newMap[node];
        if (map) {
          if (map.parent) {
            const parentMap = newMap[map.parent];
            if (parentMap && parentMap.children) {
              const parentChildren = parentMap.children.filter((c) => c !== node);
              newMap[map.parent] = { ...parentMap, children: parentChildren };
            }
          }

          delete newMap[node];
        }
      });
      nodeMap.current = newMap;
    },
    [getNodesToRemove],
  );

  const mapFirstChar = (id, firstChar) => {
    firstCharMap.current[id] = firstChar;
  };

  const prevChildIds = React.useRef([]);
  const [childrenCalculated, setChildrenCalculated] = React.useState(false);
  React.useEffect(() => {
    const childIds = [];

    React.Children.forEach(children, (child) => {
      if (React.isValidElement(child) && child.props.nodeId) {
        childIds.push(child.props.nodeId);
      }
    });
    if (arrayDiff(prevChildIds.current, childIds)) {
      nodeMap.current[-1] = { parent: null, children: childIds };

      childIds.forEach((id, index) => {
        if (index === 0) {
          setTabbable(id);
        }
        nodeMap.current[id] = { parent: null };
      });
      visibleNodes.current = nodeMap.current[-1].children;
      prevChildIds.current = childIds;
      setChildrenCalculated(true);
    }
  }, [children]);

  React.useEffect(() => {
    const buildVisible = (nodes) => {
      let list = [];
      for (let i = 0; i < nodes.length; i += 1) {
        const item = nodes[i];
        list.push(item);
        const childs = nodeMap.current[item].children;
        if (isExpanded(item) && childs) {
          list = list.concat(buildVisible(childs));
        }
      }
      return list;
    };

    if (childrenCalculated) {
      visibleNodes.current = buildVisible(nodeMap.current[-1].children);
    }
  }, [expanded, childrenCalculated, isExpanded]);

  return (
    <TreeViewContext.Provider
      value={{
        icons: { defaultCollapseIcon, defaultExpandIcon, defaultParentIcon, defaultEndIcon },
        focus,
        focusFirstNode,
        focusLastNode,
        focusNextNode,
        focusPreviousNode,
        focusByFirstCharacter,
        expandAllSiblings,
        toggleExpansion,
        isExpanded,
        isFocused,
        isSelected,
        selectNode,
        selectRange,
        selectNextNode,
        selectPreviousNode,
        rangeSelectToFirst,
        rangeSelectToLast,
        selectAllNodes,
        isTabbable,
        mul
[... 2683 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-20232/repo; git log --oneline -1; grep -n "focus\|blur" packages/material-ui-lab/src/TreeView/TreeView.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js | head -60
```

tool result:

```
7e1da61f3 [core] Add debug values to various hooks (#19515)
packages/material-ui-lab/src/TreeView/TreeView.test.js:168:    expect(getByTestId('one')).to.have.focus;
packages/material-ui-lab/src/TreeView/TreeView.test.js:170:    expect(getByTestId('two')).to.have.focus;
packages/material-ui-lab/src/TreeView/TreeView.test.js:172:    expect(getByTestId('one')).to.have.focus;
packages/material-ui-lab/src/TreeView/TreeView.test.js:174:    expect(getByTestId('two')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:110:  it('should call onFocus when focused', () => {
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:119:    getByTestId('test').focus();
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:133:    getByTestId('test').focus();
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:256:    describe('when a tree receives focus', () => {
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:257:      it('should focus the first node if none of the nodes are selected before the tree receives focus', () => {
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:270:        getByTestId('start').focus();
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:271:        expect(getByTestId('start')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:274:        getByTestId('one').focus();
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:276:        expect(getByTestId('one')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:279:      it('should focus the selected node if a node is selected before the tree receives focus', () => {
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:293:        expect(getByTestId('two')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:295:        getByTestId('start').focus();
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:296:        expect(getByTestId('start')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:299:        getByTestId('two').focus();
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:301:        expect(getByTestId('two')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:307:        it('should open the node and not move the focus if focus is on a closed node', () => {
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:317:          getByTestId('one').focus();
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:320:          expect(getByTestId('one')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:323:        it('should move focus to the first child if focus is on an open node', () => {
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:333:          getByTestId('one').focus();
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:335:          expect(getByTestId('two')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:338:        it('should do nothing if focus is on an end node', () => {
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:348:          expect(getByTestId('two')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:350:          expect(getByTestId('two')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:355:        it('should close the node if focus is on an open node', () => {
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:366:          getByTestId('one').focus();
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:369:          expect(getByTestId('one')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:372:        it("should move focus to the node's parent node if focus is on a child node that is an end node", () => {
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:384:          expect(getByTestId('one')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:388:        it("should move focus to the node's parent node if focus is on a child node that is closed", () => {
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:401:          // move focus to node two
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:406:          expect(getByTestId('one')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:410:        it('should do nothing if focus is on a root node that is closed', () => {
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:419:          getByTestId('one').focus();
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:422:          expect(getByTestId('one')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:425:        it('should do nothing if focus is on a root node that is an end node', () => {
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:432:          getByTestId('one').focus();
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:434:          expect(getByTestId('one')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:439:        it('moves focus to a sibling node', () => {
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:447:          getByTestId('one').focus();
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:449:          expect(getByTestId('two')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:452:        it('moves focus to a child node', () => {
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:462:          getByTestId('one').focus();
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:464:          expect(getByTestId('two')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:467:        it("moves focus to a parent's sibling", () => {
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:479:          expect(getByTestId('two')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:481:          expect(getByTestId('three')).to.have.focus;
packages/material-ui-lab/src/TreeItem/TreeItem.test.js:486:        it('moves focus to a sibling node', () => {

[... 886 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-20232/repo; sed -n 1,30p packages/material-ui-lab/src/TreeItem/TreeItem.test.js; sed -n 150,180p packages/material-ui-lab/src/TreeView/TreeView.test.js; grep -n "toggleExpansion\|focused\b" packages/material-ui-lab/src/TreeView/TreeView.js packages/material-ui-lab/src/TreeItem/TreeItem.js
```

tool result:

```
import * as React from 'react';
import { expect } from 'chai';
import { spy } from 'sinon';
import { createMount, getClasses } from '@material-ui/core/test-utils';
import describeConformance from '@material-ui/core/test-utils/describeConformance';
import { createEvent, createClientRender, fireEvent } from 'test/utils/createClientRender';
import TreeItem from './TreeItem';
import TreeView from '../TreeView';

describe('<TreeItem />', () => {
  let classes;
  let mount;
  const render = createClientRender({ strict: false });

  before(() => {
    // StrictModeViolation: uses Collapse
    mount = createMount({ strict: false });
    classes = getClasses(<TreeItem nodeId="one" label="one" />);
  });

  describeConformance(<TreeItem nodeId="one" label="one" />, () => ({
    classes,
    inheritComponent: 'li',
    mount,
    refInstanceof: window.HTMLLIElement,
    skip: ['componentProp'],
    after: () => mount.cleanUp(),
  }));

  it('should call onClick when clicked', () => {
        <TreeView>
          <TreeItem
            nodeId="one"
            label="one"
            data-testid="one"
            onFocus={() => {
              setState(Math.random);
            }}
          >
            <TreeItem nodeId="two" label="two" data-testid="two" />
          </TreeItem>
        </TreeView>
      );
    }

    const { getByText, getByTestId } = render(<MyComponent />);

    fireEvent.click(getByText('one'));
    expect(getByTestId('one')).to.have.focus;
    fireEvent.keyDown(document.activeElement, { key: 'ArrowDown' });
    expect(getByTestId('two')).to.have.focus;
    fireEvent.keyDown(document.activeElement, { key: 'ArrowUp' });
    expect(getByTestId('one')).to.have.focus;
    fireEvent.keyDown(document.activeElement, { key: 'ArrowDown' });
    expect(getByTestId('two')).to.have.focus;
  });

  it('should support conditional rendered tree items', () => {
    function TestComponent() {
      const [hide, setState] = React.useState(false);

packages/material-ui-lab/src/TreeView/TreeView.js:59:  const [focused, setFocused] = React.useState(null);
packages/material-ui-lab/src/TreeView/TreeView.js:91:  const isFocused = (id) => focused === id;
packages/material-ui-lab/src/TreeView/TreeView.js:184:  const toggleExpansion = (event, value = focused) => {
packages/material-ui-lab/src/TreeView/TreeView.js:497:        toggleExpansion,
packages/material-ui-lab/src/TreeItem/TreeItem.js:119:    toggleExpansion,
packages/material-ui-lab/src/TreeItem/TreeItem.js:140:  const focused = isFocused ? isFocused(nodeId) : false;
packages/material-ui-lab/src/TreeItem/TreeItem.js:163:    if (!focused) {
packages/material-ui-lab/src/TreeItem/TreeItem.js:171:      toggleExpansion(event, nodeId);
packages/material-ui-lab/src/TreeItem/TreeItem.js:214:        toggleExpansion(event);
packages/material-ui-lab/src/TreeItem/TreeItem.js:222:      toggleExpansion(event, nodeId);
packages/material-ui-lab/src/TreeItem/TreeItem.js:261:          toggleExpansion(event);
packages/material-ui-lab/src/TreeItem/TreeItem.js:331:    if (!focused && tabbable) {
packages/material-ui-lab/src/TreeItem/TreeItem.js:363:    if (focused) {
packages/material-ui-lab/src/TreeItem/TreeItem.js:366:  }, [focused]);
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-20232/repo; sed -n 515,540p packages/material-ui-lab/src/TreeView/TreeView.js; sed -n 1,20p packages/material-ui-lab/src/TreeView/TreeView.js
```

tool result:

```
      }}
    >
      <ul
        role="tree"
        aria-multiselectable={multiSelect}
        className={clsx(classes.root, className)}
        ref={ref}
        {...other}
      >
        {children}
      </ul>
    </TreeViewContext.Provider>
  );
});

TreeView.propTypes = {
  // ----------------------------- Warning --------------------------------
  // | These PropTypes are generated from the TypeScript type definitions |
  // |     To update them edit the d.ts file and run "yarn proptypes"     |
  // ----------------------------------------------------------------------
  /**
   * The content of the component.
   */
  children: PropTypes.node,
  /**
   * Override or extend the styles applied to the component.
import * as React from 'react';
import clsx from 'clsx';
import PropTypes from 'prop-types';
import TreeViewContext from './TreeViewContext';
import { withStyles } from '@material-ui/core/styles';
import { useControlled } from '@material-ui/core/utils';

export const styles = {
  /* Styles applied to the root element. */
  root: {
    padding: 0,
    margin: 0,
    listStyle: 'none',
  },
};

function arrayDiff(arr1, arr2) {
  if (arr1.length !== arr2.length) return true;

  for (let i = 0; i < arr1.length; i += 1) {
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-20232/repo; python3 - <<'EOF'
p='packages/material-ui-lab/src/TreeView/TreeView.js'
s=open(p).read()
s=s.replace("""  const focusNextNode = (id) => focus(getNextNode(id));""","""  const blur = (id) => {
    setFocused((prevFocused) => (prevFocused === id ? null : prevFocused));
  };

  const focusNextNode = (id) => focus(getNextNode(id));""",1)
s=s.replace("""        focus,
        focusFirstNode,""","""        focus,
        blur,
        focusFirstNode,""",1)
open(p,'w').write(s)
p='packages/material-ui-lab/src/TreeItem/TreeItem.js'
s=open(p).read()
s=s.replace("""    focus,
    focusFirstNode,""","""    focus,
    blur,
    focusFirstNode,""",1)
s=s.replace("""  React.useEffect(() => {
    const childIds""","""  const handleBlur = (event) => {
    if (blur) {
      blur(nodeId);
    }

    if (onBlur) {
      onBlur(event);
    }
  };

  React.useEffect(() => {
    const childIds""",1)
s=s.replace("""      onFocus={handleFocus}
""","""      onFocus={handleFocus}
      onBlur={handleBlur}
""",1)
open(p,'w').write(s)
EOF
sed -n 75,105p packages/material-ui-lab/src/TreeItem/TreeItem.js
```

tool result:

```
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
```

**assistant:** Fix is in place (TreeView exposes a `blur(id)` that clears the focused state only if that node was focused; TreeItem calls it on blur). Now wiring up the `onBlur` prop and checking propTypes.

**tool call: Bash**

```bash
cd /work/mui__material-ui-20232/repo; sed -i '' 's/^    onClick,$/    onBlur,\n    onClick,/' packages/material-ui-lab/src/TreeItem/TreeItem.js; sed -n 90,100p packages/material-ui-lab/src/TreeItem/TreeItem.js; grep -n "onFocus\|onClick\|onBlur" packages/material-ui-lab/src/TreeItem/TreeItem.js packages/material-ui-lab/src/TreeItem/TreeItem.d.ts
```

tool result:

```
    expandIcon,
    icon: iconProp,
    label,
    nodeId,
    onBlur,
    onClick,
    onFocus,
    onKeyDown,
    onMouseDown,
    TransitionComponent = Collapse,
    TransitionProps,
packages/material-ui-lab/src/TreeItem/TreeItem.js:94:    onBlur,
packages/material-ui-lab/src/TreeItem/TreeItem.js:95:    onClick,
packages/material-ui-lab/src/TreeItem/TreeItem.js:96:    onFocus,
packages/material-ui-lab/src/TreeItem/TreeItem.js:188:    if (onClick) {
packages/material-ui-lab/src/TreeItem/TreeItem.js:189:      onClick(event);
packages/material-ui-lab/src/TreeItem/TreeItem.js:337:    if (onFocus) {
packages/material-ui-lab/src/TreeItem/TreeItem.js:338:      onFocus(event);
packages/material-ui-lab/src/TreeItem/TreeItem.js:347:    if (onBlur) {
packages/material-ui-lab/src/TreeItem/TreeItem.js:348:      onBlur(event);
packages/material-ui-lab/src/TreeItem/TreeItem.js:396:      onFocus={handleFocus}
packages/material-ui-lab/src/TreeItem/TreeItem.js:397:      onBlur={handleBlur}
packages/material-ui-lab/src/TreeItem/TreeItem.js:406:        onClick={handleClick}
packages/material-ui-lab/src/TreeItem/TreeItem.js:476:  onClick: PropTypes.func,
packages/material-ui-lab/src/TreeItem/TreeItem.js:480:  onFocus: PropTypes.func,
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-20232/repo; sed -n 470,482p packages/material-ui-lab/src/TreeItem/TreeItem.js
```

tool result:

```
   * The id of the node.
   */
  nodeId: PropTypes.string.isRequired,
  /**
   * @ignore
   */
  onClick: PropTypes.func,
  /**
   * @ignore
   */
  onFocus: PropTypes.func,
  /**
   * @ignore
```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/mui__material-ui-20232/repo/packages/material-ui-lab/src/TreeItem/TreeItem.js",
 "old_string": "  nodeId: PropTypes.string.isRequired,\n  /**\n   * @ignore\n   */\n  onClick: PropTypes.func,",
 "new_string": "  nodeId: PropTypes.string.isRequired,\n  /**\n   * @ignore\n   */\n  onBlur: PropTypes.func,\n  /**\n   * @ignore\n   */\n  onClick: PropTypes.func,"
}
```

tool result:

```
The file /work/mui__material-ui-20232/repo/packages/material-ui-lab/src/TreeItem/TreeItem.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**assistant:** Now a reproduction test (focus an item, move focus to an outside input, hide/show the items, check focus stays on the input):

**tool call: Bash**

```bash
cd /work/mui__material-ui-20232/repo; cat > packages/material-ui-lab/src/TreeView/repro.test.js <<'EOF'
import * as React from 'react';
import { expect } from 'chai';
import { createClientRender, fireEvent } from 'test/utils/createClientRender';
import TreeItem from '../TreeItem';
import TreeView from './TreeView';

describe('repro focus steal', () => {
  const render = createClientRender({ strict: false });
  it('does not steal focus', () => {
    function Test() {
      const [hide, setHide] = React.useState(false);
      return (
        <React.Fragment>
          <input data-testid="input" onChange={() => setHide((h) => !h)} />
          <TreeView>
            {!hide && <TreeItem nodeId="one" label="one" data-testid="one" />}
            <TreeItem nodeId="two" label="two" data-testid="two" />
          </TreeView>
        </React.Fragment>
      );
    }
    const { getByTestId, getByText } = render(<Test />);
    fireEvent.click(getByText('one'));
    expect(getByTestId('one')).to.have.focus;
    getByTestId('input').focus();
    expect(getByTestId('input')).to.have.focus;
    fireEvent.change(getByTestId('input'), { target: { value: 'a' } });
    fireEvent.change(getByTestId('input'), { target: { value: '' } });
    expect(getByTestId('one')).not.to.equal(null);
    expect(getByTestId('input')).to.have.focus;
  });
});
EOF
git stash -q -- packages/material-ui-lab/src/TreeItem packages/material-ui-lab/src/TreeView/TreeView.js
../bin/envrun 'yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeView/repro.test.js 2>&1 | tail -15'
git stash pop -q
../bin/envrun 'yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeView/repro.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js 2>&1 | tail -15'
```

tool result:

```
Command did not complete within its 120s timeout and was moved to the background (ID: b081o4orz). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/1237aa22-8800-4767-8779-d415ffab6245/tasks/b081o4orz.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /work/mui__material-ui-20232/repo; directory changes made by the backgrounded command do not apply to subsequent commands.
```

**assistant:** That change is just my temporary `git stash` (so the repro can run against the original code first). It gets restored when the background command finishes.

**tool call: Bash**

```bash
sleep 200; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/1237aa22-8800-4767-8779-d415ffab6245/tasks/b081o4orz.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
sleep 240; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/1237aa22-8800-4767-8779-d415ffab6245/tasks/b081o4orz.output; cd /work/mui__material-ui-20232/repo; git status --short; git stash list
```

tool result:

```
 M package.json
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
?? packages/material-ui-lab/src/TreeView/repro.test.js
stash@{0}: WIP on main: 7e1da61f3 [core] Add debug values to various hooks (#19515)
```

**tool call: Bash**

```bash
sleep 280; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/1237aa22-8800-4767-8779-d415ffab6245/tasks/b081o4orz.output
```

tool result:

```
(Bash completed with no output)
```

**assistant:** Mocha is slow to finish; let me check how tests are meant to be run here.

**tool call: Bash**

```bash
cd /work/mui__material-ui-20232/repo; grep -n '"test' package.json; cat .mocharc.js 2>/dev/null | head -30; git diff package.json
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
diff --git a/package.json b/package.json
index e1b6c999e..bde4e149b 100644
--- a/package.json
+++ b/package.json
@@ -58,17 +58,20 @@
     "@testing-library/dom": "^7.0.3",
     "@testing-library/react": "^10.0.1",
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
@@ -144,7 +147,6 @@
     "typescript": "^3.8.2",
     "typescript-to-proptypes": "^1.4.0",
     "unist-util-visit": "^2.0.2",
-    "vrtest-mui": "^0.3.3",
     "webpack": "^4.41.0",
     "webpack-cli": "^3.3.9",
     "yargs": "^15.2.0",
```

**assistant:** The `package.json`/`yarn.lock` changes and `Dockerfile` come from the environment setup, not from me. First-run Babel compilation is probably what's slow, so I'll keep waiting.

**tool call: Bash**

```bash
sleep 290; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/1237aa22-8800-4767-8779-d415ffab6245/tasks/b081o4orz.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-20232/repo; timeout 60 ../bin/envrun 'ps aux | head -30'
```

tool result:

```
Exit code 127
(eval):1: command not found: timeout
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-20232/repo; ../bin/envrun 'ps aux | head -30'
```

tool result:

```
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0 287720  2968 ?        Ss   10:34   0:00 sleep infinity
root         7  0.0  0.0 289612  6288 ?        Ss   10:35   0:00 bash -lc yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeView/repro.test.js 2>&1 | tail -15
root        15  0.1  1.1 1151416 92912 ?       Sl   10:35   0:01 node --no-opt -r /proc/.reset /usr/local/nvm/versions/node/v16.20.2/bin/yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeView/repro.test.js
root        16  0.0  0.0 287760  2980 ?        S    10:35   0:00 tail -15
root        27  0.0  0.0 287856  3344 ?        S    10:35   0:00 /bin/sh -c /testbed/node_modules/.bin/cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeView/repro.test.js
root        28  0.0  0.6 815036 50888 ?        Sl   10:35   0:00 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/.bin/cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeView/repro.test.js
root        35  0.4  2.3 985808 188328 ?       Sl   10:35   0:05 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/.bin/mocha packages/material-ui-lab/src/TreeView/repro.test.js
root        42  0.0  0.0 289612  6288 ?        Ss   10:54   0:00 bash -lc ps aux | head -30
root        50  0.0  0.0 292124  5148 ?        R    10:54   0:00 ps aux
root        51  0.0  0.0 287732  2932 ?        S    10:54   0:00 head -30
```

**assistant:** Mocha finished its work but isn't exiting (idle process, output held back by `tail`). I'll kill it and rerun with `--exit`.

**tool call: Bash**

```bash
cd /work/mui__material-ui-20232/repo; ../bin/envrun 'kill 35'; sleep 5; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/1237aa22-8800-4767-8779-d415ffab6245/tasks/b081o4orz.output
```

tool result:

```
      -      [33mclass[39m=[32m"MuiTypography-root MuiTreeItem-label MuiTypography-body1"[39m
      -    [36m>[39m
      -      [0mone[0m
      -    [36m</div>[39m
      -  [36m</div>[39m
      -[36m</li>[39m
      +[36m<input[39m
      +  [33mdata-testid[39m=[32m"input"[39m
      +[36m/>[39m
      
      at Context.<anonymous> (packages/material-ui-lab/src/TreeView/repro.test.js:30:5)
      at processImmediate (node:internal/timers:466:21)
```

**assistant:** The repro fails on the original code: the remounted item steals focus from the input. Once the stash pop finishes, I'll run the fixed version.

**tool call: Bash**

```bash
sleep 30; cd /work/mui__material-ui-20232/repo; git stash list; git status --short; ../bin/envrun 'ps aux | grep mocha | grep -v grep'
```

tool result:

```
 M package.json
 M packages/material-ui-lab/src/TreeItem/TreeItem.js
 M packages/material-ui-lab/src/TreeView/TreeView.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
?? packages/material-ui-lab/src/TreeView/repro.test.js
root        60  0.0  0.0 289612  6288 ?        Ss   10:54   0:00 bash -lc yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeView/repro.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js 2>&1 | tail -15
root        68  1.2  0.9 1139000 79956 ?       Sl   10:54   0:00 node --no-opt -r /proc/.reset /usr/local/nvm/versions/node/v16.20.2/bin/yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeView/repro.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js
root        80  0.0  0.0 287856  3348 ?        S    10:54   0:00 /bin/sh -c /testbed/node_modules/.bin/cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeView/repro.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js
root        81  0.6  0.6 815036 50908 ?        Sl   10:54   0:00 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/.bin/cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeView/repro.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js
root        88 11.8  2.5 997736 204424 ?       Sl   10:54   0:04 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/.bin/mocha packages/material-ui-lab/src/TreeView/repro.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js
```

**tool call: Bash**

```bash
sleep 20; cd /work/mui__material-ui-20232/repo; ../bin/envrun 'pkill -f bin/mocha'; sleep 5; tail -30 /tmp/cell-scratch/claude-502/<actor-session-slug>/1237aa22-8800-4767-8779-d415ffab6245/tasks/b081o4orz.output
```

tool result:

```
      -      [33mclass[39m=[32m"MuiTypography-root MuiTreeItem-label MuiTypography-body1"[39m
      -    [36m>[39m
      -      [0mone[0m
      -    [36m</div>[39m
      -  [36m</div>[39m
      -[36m</li>[39m
      +[36m<input[39m
      +  [33mdata-testid[39m=[32m"input"[39m
      +[36m/>[39m
      
      at Context.<anonymous> (packages/material-ui-lab/src/TreeView/repro.test.js:30:5)
      at processImmediate (node:internal/timers:466:21)




warning You don't appear to have an internet connection. Try the --offline flag to use the cache for registry queries.
Browserslist: caniuse-lite is outdated. Please run the following command: `npx browserslist --update-db`
including inaccessible elements by default


  ․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․
  ․․․․․․․․․․․․․․․․․․

  74 passing (914ms)



[exited with code 0]
```

**assistant:** With the fix, all 74 tests pass: the repro plus the existing TreeView and TreeItem suites. Next I'll lint the changed files and delete the repro.

**tool call: Bash**

```bash
cd /work/mui__material-ui-20232/repo; rm packages/material-ui-lab/src/TreeView/repro.test.js; ../bin/envrun 'npx eslint packages/material-ui-lab/src/TreeItem/TreeItem.js packages/material-ui-lab/src/TreeView/TreeView.js && npx prettier --check packages/material-ui-lab/src/TreeItem/TreeItem.js packages/material-ui-lab/src/TreeView/TreeView.js'; git status --short; git diff packages/
```

tool result:

```
Checking formatting...
All matched files use Prettier code style!

 M package.json
 M packages/material-ui-lab/src/TreeItem/TreeItem.js
 M packages/material-ui-lab/src/TreeView/TreeView.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
diff --git a/packages/material-ui-lab/src/TreeItem/TreeItem.js b/packages/material-ui-lab/src/TreeItem/TreeItem.js
index d6f8a835e..9501bf209 100644
--- a/packages/material-ui-lab/src/TreeItem/TreeItem.js
+++ b/packages/material-ui-lab/src/TreeItem/TreeItem.js
@@ -91,6 +91,7 @@ const TreeItem = React.forwardRef(function TreeItem(props, ref) {
     icon: iconProp,
     label,
     nodeId,
+    onBlur,
     onClick,
     onFocus,
     onKeyDown,
@@ -103,6 +104,7 @@ const TreeItem = React.forwardRef(function TreeItem(props, ref) {
   const {
     icons: contextIcons,
     focus,
+    blur,
     focusFirstNode,
     focusLastNode,
     focusNextNode,
@@ -337,6 +339,16 @@ const TreeItem = React.forwardRef(function TreeItem(props, ref) {
     }
   };
 
+  const handleBlur = (event) => {
+    if (blur) {
+      blur(nodeId);
+    }
+
+    if (onBlur) {
+      onBlur(event);
+    }
+  };
+
   React.useEffect(() => {
     const childIds = React.Children.map(children, (child) => child.props.nodeId) || [];
     if (addNodeToNodeMap) {
@@ -382,6 +394,7 @@ const TreeItem = React.forwardRef(function TreeItem(props, ref) {
       role="treeitem"
       onKeyDown={handleKeyDown}
       onFocus={handleFocus}
+      onBlur={handleBlur}
       aria-expanded={expandable ? expanded : null}
       aria-selected={ariaSelected}
       ref={handleRef}
@@ -457,6 +470,10 @@ TreeItem.propTypes = {
    * The id of the node.
    */
   nodeId: PropTypes.string.isRequired,
+  /**
+   * @ignore
+   */
+  onBlur: PropTypes.func,
   /**
    * @ignore
    */
diff --git a/packages/material-ui-lab/src/TreeView/TreeView.js b/packages/material-ui-lab/src/TreeView/TreeView.js
index b60bd1801..8d0ae5dea 100644
--- a/packages/material-ui-lab/src/TreeView/TreeView.js
+++ b/packages/material-ui-lab/src/TreeView/TreeView.js
@@ -133,6 +133,10 @@ const TreeView = React.forwardRef(function TreeView(props, ref) {
     }
   };
 
+  const blur = (id) => {
+    setFocused((prevFocused) => (prevFocused === id ? null : prevFocused));
+  };
+
   const focusNextNode = (id) => focus(getNextNode(id));
   const focusPreviousNode = (id) => focus(getPreviousNode(id));
   const focusFirstNode = () => focus(getFirstNode());
@@ -488,6 +492,7 @@ const TreeView = React.forwardRef(function TreeView(props, ref) {
       value={{
         icons: { defaultCollapseIcon, defaultExpandIcon, defaultParentIcon, defaultEndIcon },
         focus,
+        blur,
         focusFirstNode,
         focusLastNode,
         focusNextNode,
```

**assistant:** I fixed the focus stealing: a TreeItem that comes back into the tree no longer takes focus away from the text box.

**Cause:** TreeView keeps track of which node is focused, but it never cleared that when focus left the tree. TreeItem has an effect that runs on mount: if the item is marked as focused, it calls `.focus()` on itself. So when you filter the tree and the last-focused item disappears and then reappears (in the issue, while deleting "bananas"), the remounted item grabbed focus from the TextField.

**Fix:**
- `packages/material-ui-lab/src/TreeView/TreeView.js`: added a `blur(id)` function, passed down to the items, that clears the focused node only if `id` is still the focused one.
- `packages/material-ui-lab/src/TreeItem/TreeItem.js`: added an `onBlur` handler on the `<li>` that calls `blur(nodeId)` and then any `onBlur` the user passed in. I also added `onBlur` to the props it reads and to the propTypes.

Arrow-key navigation inside the tree still works. When you move to the next item, the focused node is already set to that item before the old one fires its blur event, so the check in `blur` does nothing. Tabbing back into the tree works as before.

**Verification:**
- I wrote a temporary mocha test: focus a tree item, move focus to an outside `<input>`, then hide and re-show that item from the input's `onChange`. On the original code it failed because the item took focus; with the fix it passes.
- With the fix, the repro plus the existing `TreeView.test.js` and `TreeItem.test.js` give 74 passing.
- ESLint and Prettier pass on both changed files.
- I deleted the repro test afterwards.

**One case not covered:** if the focused item itself is filtered out, the browser doesn't fire a blur event when it's removed, so the tree still treats it as focused. If it comes back, it will take focus again. That only happens when focus was on that item to begin with, so it isn't the bug from the issue.

The changes to `package.json` and `yarn.lock`, and the untracked `Dockerfile` and `custom-reporter.js`, were already there from the environment setup. I didn't touch them.

_session end: success, turns 22, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.12 s: ps aux | head -30
- `rc=0` 0.12 s: kill 35
- `rc=0` 1151.29 s: yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeView/repro.test.js 2>&1 | tail -15
- `rc=0` 0.13 s: ps aux | grep mocha | grep -v grep
- `rc=0` 0.14 s: pkill -f bin/mocha
- `rc=0` 59.88 s: yarn -s cross-env NODE_ENV=test mocha packages/material-ui-lab/src/TreeView/repro.test.js packages/material-ui-lab/src/TreeView/TreeView.test.js packages/material-ui-lab/src/TreeItem/TreeItem.test.js 2>&1 | tail -15
- `rc=0` 4.36 s: npx eslint packages/material-ui-lab/src/TreeItem/TreeItem.js packages/material-ui-lab/src/TreeView/TreeView.js && npx prettier --check packages/material-ui-lab/src/TreeItem/TreeItem.js packages/material-ui-lab/src/TreeView/TreeView.js
