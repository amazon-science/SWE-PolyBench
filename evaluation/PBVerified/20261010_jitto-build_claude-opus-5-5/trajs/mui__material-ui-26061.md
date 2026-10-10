# Instance: mui__material-ui-26061

- Final resolved (evaluator, logs/mui__material-ui-26061_result.json): True
- Run state: DONE
- One attempt. Duration 524.7 s, turns 21, actor cost $0.41126739999999995, container commands 8
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/mui__material-ui-26061/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-26061/repo. Consider the following issue description:

<issue_description>
[Tabs] When a Tab is disabled, keyboard traversal is stuck
<!-- Provide a general summary of the issue in the Title above -->
Normally keyboard users will tab into a Tabs group, then use either Left/Right (if horizontal tab) or Up/Down (vertical) to traverse the Tabs and according to [WAI aria practices](https://www.w3.org/TR/wai-aria-practices/#keyboard-interaction-19), the Tabs should wrap around (last <-> first tabs); this works great right now unless a Tab is disabled, in which case it will break the traversal instead of skip the disabled Tab.
<!--
  Thank you very much for contributing to Material-UI by creating an issue! ❤️
  To avoid duplicate issues we ask you to check off the following list.
-->

<!-- Checked checkbox should look like this: [x] -->

- [x] The issue is present in the latest release.
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Current Behavior 😯
If a Tab is in disabled state, then it acts like a hard stop in the traversal order. 
<!-- Describe what happens instead of the expected behavior. -->

## Expected Behavior 🤔
Match the behavior to the way MenuItems with disabled items are traversed and just skip the disabled Tab.  

Maybe you could do something in Tabs.js, handleKeyDown, around here:
```
case previousItemKey:
        newFocusTarget = target.previousElementSibling || tabListRef.current.lastChild;
```
look for disabled state

<!-- Describe what should happen. -->

## Steps to Reproduce 🕹
https://codesandbox.io/s/basictabs-material-demo-forked-sh1rd?file=/demo.js
Hope I forked and saved this correctly.  it's the basic Tab example with a button for convenient focus.  Tab 2 is disabled; you can tab into the Tabs group and then you can see how the arrow traversal hits a wall when it encounters disabled Tab 2.  
<!--
  Provide a link to a live example (you can use codesandbox.io) and an unambiguous set of steps to reproduce this bug.
  Include code to reproduce, if relevant (which it most likely is).

  You should use the official codesandbox template as a starting point: https://material-ui.com/r/issue-template-next

  If you have an issue concerning TypeScript please start from this TypeScript playground: https://material-ui.com/r/ts-issue-template

  Issues without some form of live example have a longer response time.
-->

Steps:

1. Take a look at the codesandbox link
2. If I messed that up, then just take the simple tab demo (first one) and add a disabled on any one of the Tab components

## Context 🔦
a11y compliance
<!--
  What are you trying to accomplish? How has this issue affected you?
  Providing context helps us come up with a solution that is most useful in the real world.
-->

## Your Environment 🌎
this happens on the demo code.
<!--
  Run `npx @material-ui/envinfo` and post the results.
  If you encounter issues with TypeScript please include the used tsconfig.
-->
<details>
  <summary>`npx @material-ui/envinfo`</summary>
  
```
  Don't forget to mention which browser you used.
  Output from `npx @material-ui/envinfo` goes here.
```
</details>


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-26061/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-26061/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-26061/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-26061/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
grep -n "handleKeyDown" -A45 packages/material-ui/src/Tabs/Tabs.js | head -70
```

tool result:

```
590:  const handleKeyDown = (event) => {
591-    const { target } = event;
592-    // Keyboard navigation assumes that [role="tab"] are siblings
593-    // though we might warn in the future about nested, interactive elements
594-    // as a a11y violation
595-    const role = target.getAttribute('role');
596-    if (role !== 'tab') {
597-      return;
598-    }
599-
600-    let newFocusTarget = null;
601-    let previousItemKey = orientation === 'horizontal' ? 'ArrowLeft' : 'ArrowUp';
602-    let nextItemKey = orientation === 'horizontal' ? 'ArrowRight' : 'ArrowDown';
603-    if (orientation === 'horizontal' && isRtl) {
604-      // swap previousItemKey with nextItemKey
605-      previousItemKey = 'ArrowRight';
606-      nextItemKey = 'ArrowLeft';
607-    }
608-
609-    switch (event.key) {
610-      case previousItemKey:
611-        newFocusTarget = target.previousElementSibling || tabListRef.current.lastChild;
612-        break;
613-      case nextItemKey:
614-        newFocusTarget = target.nextElementSibling || tabListRef.current.firstChild;
615-        break;
616-      case 'Home':
617-        newFocusTarget = tabListRef.current.firstChild;
618-        break;
619-      case 'End':
620-        newFocusTarget = tabListRef.current.lastChild;
621-        break;
622-      default:
623-        break;
624-    }
625-
626-    if (newFocusTarget !== null) {
627-      newFocusTarget.focus();
628-      event.preventDefault();
629-    }
630-  };
631-
632-  const conditionalElements = getConditionalElements();
633-
634-  return (
635-    <TabsRoot
--
663:          onKeyDown={handleKeyDown}
664-          ref={tabListRef}
665-          role="tablist"
666-        >
667-          {children}
668-        </FlexContainer>
669-        {mounted && indicator}
670-      </TabsScroller>
671-      {conditionalElements.scrollButtonEnd}
672-    </TabsRoot>
673-  );
674-});
675-
676-Tabs.propTypes /* remove-proptypes */ = {
677-  // ----------------------------- Warning --------------------------------
678-  // | These PropTypes are generated from the TypeScript type definitions |
679-  // |     To update them edit the d.ts file and run "yarn proptypes"     |
680-  // ----------------------------------------------------------------------
681-  /**
682-   * Callback fired when the component mounts.
683-   * This is useful when you want to trigger an action programmatically.
684-   * It supports two actions: `updateIndicator()` and `updateScrollButtons()`
685-   *
```

**tool call: Bash**

```bash
grep -n "disabled" packages/material-ui/src/Tabs/Tabs.test.js | head -30; grep -n "function moveFocus" -A40 packages/material-ui/src/MenuList/MenuList.js; grep -n "Tab.*disabled\|disabledFocus" packages/material-ui/src/Tab/Tab.js | head
```

tool result:

```
29:  return !scrollButton.parentElement.classList.contains('Mui-disabled');
39:  return !scrollButton.parentElement.classList.contains('Mui-disabled');
49:function moveFocus(
50-  list,
51-  currentFocus,
52-  disableListWrap,
53-  disabledItemsFocusable,
54-  traversalFunction,
55-  textCriteria,
56-) {
57-  let wrappedOnce = false;
58-  let nextFocus = traversalFunction(list, currentFocus, currentFocus ? disableListWrap : false);
59-
60-  while (nextFocus) {
61-    // Prevent infinite loop.
62-    if (nextFocus === list.firstChild) {
63-      if (wrappedOnce) {
64-        return;
65-      }
66-      wrappedOnce = true;
67-    }
68-
69-    // Same logic as useAutocomplete.js
70-    const nextFocusDisabled = disabledItemsFocusable
71-      ? false
72-      : nextFocus.disabled || nextFocus.getAttribute('aria-disabled') === 'true';
73-
74-    if (
75-      !nextFocus.hasAttribute('tabindex') ||
76-      !textCriteriaMatches(nextFocus, textCriteria) ||
77-      nextFocusDisabled
78-    ) {
79-      // Move to the next element.
80-      nextFocus = traversalFunction(list, nextFocus, disableListWrap);
81-    } else {
82-      nextFocus.focus();
83-      return;
84-    }
85-  }
86-}
87-
88-/**
89- * A permanently displayed menu following https://www.w3.org/TR/wai-aria-practices/#menubutton.
```

**tool call: Bash**

```bash
cd packages/material-ui/src/Tabs && python3 - <<'EOF'
p='Tabs.js'
s=open(p).read()
old=s[s.index("    let newFocusTarget = null;\n"):s.index("  const conditionalElements")]
new='''    let previousItemKey = orientation === 'horizontal' ? 'ArrowLeft' : 'ArrowUp';
    let nextItemKey = orientation === 'horizontal' ? 'ArrowRight' : 'ArrowDown';
    if (orientation === 'horizontal' && isRtl) {
      // swap previousItemKey with nextItemKey
      previousItemKey = 'ArrowRight';
      nextItemKey = 'ArrowLeft';
    }

    const list = tabListRef.current;

    switch (event.key) {
      case previousItemKey:
        event.preventDefault();
        moveFocus(list, target, previousItem);
        break;
      case nextItemKey:
        event.preventDefault();
        moveFocus(list, target, nextItem);
        break;
      case 'Home':
        event.preventDefault();
        moveFocus(list, null, nextItem);
        break;
      case 'End':
        event.preventDefault();
        moveFocus(list, null, previousItem);
        break;
      default:
        break;
    }
  };

'''
s=s.replace(old,new)
anchor="const defaultIndicatorStyle = {};"
assert anchor in s
helpers='''const nextItem = (list, item) => {
  if (list === item) {
    return list.firstChild;
  }
  if (item && item.nextElementSibling) {
    return item.nextElementSibling;
  }
  return list.firstChild;
};

const previousItem = (list, item) => {
  if (list === item) {
    return list.lastChild;
  }
  if (item && item.previousElementSibling) {
    return item.previousElementSibling;
  }
  return list.lastChild;
};

const moveFocus = (list, currentFocus, traversalFunction) => {
  let wrappedOnce = false;
  let nextFocus = traversalFunction(list, currentFocus);

  while (nextFocus) {
    // Prevent infinite loop.
    if (nextFocus === list.firstChild) {
      if (wrappedOnce) {
        return;
      }
      wrappedOnce = true;
    }

    // Same logic as useAutocomplete.js
    const nextFocusDisabled =
      nextFocus.disabled || nextFocus.getAttribute('aria-disabled') === 'true';

    if (!nextFocus.hasAttribute('tabindex') || nextFocusDisabled) {
      // Move to the next element.
      nextFocus = traversalFunction(list, nextFocus);
    } else {
      nextFocus.focus();
      return;
    }
  }
};

'''
s=s.replace(anchor,helpers+anchor,1)
open(p,'w').write(s)
EOF
grep -n "defaultIndicatorStyle = {}" Tabs.js; git diff --stat
```

tool result:

```
Traceback (most recent call last):
  File "<stdin>", line 39, in <module>
AssertionError
195:const defaultIndicatorStyle = {};
 package.json |     9 +-
 yarn.lock    | 31090 ++++++++++++++++++++++++++++++---------------------------
 2 files changed, 16355 insertions(+), 14744 deletions(-)
```

**tool call: Bash**

```bash
cd packages/material-ui/src/Tabs && sed -n 193,196p Tabs.js | cat -A | head; git status --short
```

tool result:

```
(eval):cd:1: no such file or directory: packages/material-ui/src/Tabs
 M ../../../../package.json
 M ../../../../yarn.lock
?? ../../../../Dockerfile
?? ../../../../custom-reporter.js
```

**tool call: Bash**

```bash
sed -n 193,196p Tabs.js | od -c | head
```

tool result:

```
0000000    }   )   ;  \n  \n   c   o   n   s   t       d   e   f   a   u
0000020    l   t   I   n   d   i   c   a   t   o   r   S   t   y   l   e
0000040        =       {   }   ;  \n  \n                                
0000050
```

**thinking:**

```
My scripted edit failed with an assertion error, so I'll switch to using the Edit tool for the changes instead—I'll leave the already-modified package.json/yarn.lock alone.


```

**tool call: Read**

```json
{
 "file_path": "/work/mui__material-ui-26061/repo/packages/material-ui/src/Tabs/Tabs.js",
 "offset": 190,
 "limit": 8
}
```

**tool call: Read**

```json
{
 "file_path": "/work/mui__material-ui-26061/repo/packages/material-ui/src/Tabs/Tabs.js",
 "offset": 598,
 "limit": 33
}
```

tool result:

```
190	  '&::-webkit-scrollbar': {
191	    display: 'none', // Safari + Chrome
192	  },
193	});
194	
195	const defaultIndicatorStyle = {};
196	
197	const Tabs = React.forwardRef(function Tabs(inProps, ref) {
```

tool result:

```
598	    }
599	
600	    let newFocusTarget = null;
601	    let previousItemKey = orientation === 'horizontal' ? 'ArrowLeft' : 'ArrowUp';
602	    let nextItemKey = orientation === 'horizontal' ? 'ArrowRight' : 'ArrowDown';
603	    if (orientation === 'horizontal' && isRtl) {
604	      // swap previousItemKey with nextItemKey
605	      previousItemKey = 'ArrowRight';
606	      nextItemKey = 'ArrowLeft';
607	    }
608	
609	    switch (event.key) {
610	      case previousItemKey:
611	        newFocusTarget = target.previousElementSibling || tabListRef.current.lastChild;
612	        break;
613	      case nextItemKey:
614	        newFocusTarget = target.nextElementSibling || tabListRef.current.firstChild;
615	        break;
616	      case 'Home':
617	        newFocusTarget = tabListRef.current.firstChild;
618	        break;
619	      case 'End':
620	        newFocusTarget = tabListRef.current.lastChild;
621	        break;
622	      default:
623	        break;
624	    }
625	
626	    if (newFocusTarget !== null) {
627	      newFocusTarget.focus();
628	      event.preventDefault();
629	    }
630	  };
```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/mui__material-ui-26061/repo/packages/material-ui/src/Tabs/Tabs.js",
 "old_string": "    let newFocusTarget = null;\n    let previousItemKey",
 "new_string": "    let previousItemKey"
}
```

tool result:

```
The file /work/mui__material-ui-26061/repo/packages/material-ui/src/Tabs/Tabs.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/mui__material-ui-26061/repo/packages/material-ui/src/Tabs/Tabs.js",
 "old_string": "    switch (event.key) {\n      case previousItemKey:\n        newFocusTarget = target.previousElementSibling || tabListRef.current.lastChild;\n        break;\n      case nextItemKey:\n        newFocusTarget = target.nextElementSibling || tabListRef.current.firstChild;\n        break;\n      case 'Home':\n        newFocusTarget = tabListRef.current.firstChild;\n        break;\n      case 'End':\n        newFocusTarget = tabListRef.current.lastChild;\n        break;\n      default:\n        break;\n    }\n\n    if (newFocusTarget !== null) {\n      newFocusTarget.focus();\n      event.preventDefault();\n    }\n  };",
 "new_string": "    const list = tabListRef.current;\n\n    switch (event.key) {\n      case previousItemKey:\n        event.preventDefault();\n        moveFocus(list, target, previousItem);\n        break;\n      case nextItemKey:\n        event.preventDefault();\n        moveFocus(list, target, nextItem);\n        break;\n      case 'Home':\n        event.preventDefault();\n        moveFocus(list, null, nextItem);\n        break;\n      case 'End':\n        event.preventDefault();\n        moveFocus(list, null, previousItem);\n        break;\n      default:\n        break;\n    }\n  };"
}
```

tool result:

```
The file /work/mui__material-ui-26061/repo/packages/material-ui/src/Tabs/Tabs.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/mui__material-ui-26061/repo/packages/material-ui/src/Tabs/Tabs.js",
 "old_string": "const defaultIndicatorStyle = {};\n",
 "new_string": "const nextItem = (list, item) => {\n  if (item && item.nextElementSibling) {\n    return item.nextElementSibling;\n  }\n  return list.firstChild;\n};\n\nconst previousItem = (list, item) => {\n  if (item && item.previousElementSibling) {\n    return item.previousElementSibling;\n  }\n  return list.lastChild;\n};\n\nconst moveFocus = (list, currentFocus, traversalFunction) => {\n  let wrappedOnce = false;\n  let nextFocus = traversalFunction(list, currentFocus);\n\n  while (nextFocus) {\n    // Prevent infinite loop.\n    if (nextFocus === list.firstChild) {\n      if (wrappedOnce) {\n        return;\n      }\n      wrappedOnce = true;\n    }\n\n    // Same logic as MenuList.js\n    const nextFocusDisabled =\n      nextFocus.disabled || nextFocus.getAttribute('aria-disabled') === 'true';\n\n    if (!nextFocus.hasAttribute('tabindex') || nextFocusDisabled) {\n      // Move to the next element.\n      nextFocus = traversalFunction(list, nextFocus);\n    } else {\n      nextFocus.focus();\n      return;\n    }\n  }\n};\n\nconst defaultIndicatorStyle = {};\n"
}
```

tool result:

```
The file /work/mui__material-ui-26061/repo/packages/material-ui/src/Tabs/Tabs.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**assistant:** Now a quick repro test with disabled tabs, plus the existing Tabs tests:

**tool call: Bash**

```bash
cat > repro.test.js <<'EOF'
import * as React from 'react';
import { expect } from 'chai';
import { createClientRender, fireEvent } from 'test/utils';
import Tab from '../Tab';
import Tabs from './Tabs';

describe('repro disabled tabs', () => {
  const render = createClientRender();
  it('skips disabled tabs and wraps', () => {
    const { getAllByRole } = render(
      <Tabs value={0}>
        <Tab />
        <Tab disabled />
        <Tab />
        <Tab disabled />
      </Tabs>,
    );
    const [a, , c] = getAllByRole('tab');
    a.focus();
    fireEvent.keyDown(a, { key: 'ArrowRight' });
    expect(document.activeElement).to.equal(c);
    fireEvent.keyDown(c, { key: 'ArrowRight' });
    expect(document.activeElement).to.equal(a);
    fireEvent.keyDown(a, { key: 'ArrowLeft' });
    expect(document.activeElement).to.equal(c);
    fireEvent.keyDown(c, { key: 'End' });
    expect(document.activeElement).to.equal(c);
    fireEvent.keyDown(c, { key: 'Home' });
    expect(document.activeElement).to.equal(a);
  });
});
EOF
cd /work/mui__material-ui-26061/repo && ../bin/envrun 'yarn -s mocha packages/material-ui/src/Tabs/repro.test.js packages/material-ui/src/Tabs/Tabs.test.js 2>&1 | tail -30'
```

tool result:

```
Command did not complete within its 120s timeout and was moved to the background (ID: bh9lu342y). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/4558309b-cd13-46c7-ab05-6b4a3c1b952a/tasks/bh9lu342y.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /work/mui__material-ui-26061/repo/packages/material-ui/src/Tabs; directory changes made by the backgrounded command do not apply to subsequent commands.
```

**tool call: Bash**

```bash
sleep 120; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/4558309b-cd13-46c7-ab05-6b4a3c1b952a/tasks/bh9lu342y.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
sleep 180; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/4558309b-cd13-46c7-ab05-6b4a3c1b952a/tasks/bh9lu342y.output
```

tool result:

```
(Bash completed with no output)
```

**assistant:** Still no output after 5 minutes; let me check what's running in the container.

**tool call: Bash**

```bash
cd /work/mui__material-ui-26061/repo && cat .mocharc.js; grep '"test' package.json; ../bin/envrun 'ps aux | head -20'
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
  timeout: (process.env.CIRCLECI === 'true' ? 5 : 2) * 1000, // Circle CI has low-performance CPUs.
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
    "test": "yarn lint && yarn typescript && yarn test:coverage",
    "test:coverage": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc --reporter=text mocha 'packages/**/*.test.{js,ts,tsx}' 'docs/**/*.test.{js,ts,tsx}' 'scripts/**/*.test.{js,ts,tsx}' 'test/utils/**/*.test.{js,ts,tsx}'",
    "test:coverage:ci": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc --reporter=lcov mocha 'packages/**/*.test.{js,ts,tsx}' 'docs/**/*.test.{js,ts,tsx}' 'scripts/**/*.test.{js,ts,tsx}' 'test/utils/**/*.test.{js,ts,tsx}'",
    "test:coverage:html": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc --reporter=html mocha 'packages/**/*.test.{js,ts,tsx}' 'docs/**/*.test.{js,ts,tsx}' 'scripts/**/*.test.{js,ts,tsx}' 'test/utils/**/*.test.{js,ts,tsx}'",
    "test:e2e": "cross-env NODE_ENV=production yarn test:e2e:build && concurrently --success first --kill-others \"yarn test:e2e:run\" \"yarn test:e2e:server\"",
    "test:e2e:build": "webpack --config test/e2e/webpack.config.js",
    "test:e2e:dev": "concurrently \"yarn test:e2e:build --watch\" \"yarn test:e2e:server\"",
    "test:e2e:run": "mocha --config test/e2e/.mocharc.js 'test/e2e/**/*.test.{js,ts,tsx}'",
    "test:e2e:server": "serve test/e2e",
    "test:karma": "cross-env NODE_ENV=test karma start test/karma.conf.js",
    "test:karma:profile": "cross-env NODE_ENV=test karma start test/karma.conf.profile.js",
    "test:regressions": "cross-env NODE_ENV=production yarn test:regressions:build && concurrently --success first --kill-others \"yarn test:regressions:run\" \"yarn test:regressions:server\"",
    "test:regressions:build": "webpack --config test/regressions/webpack.config.js",
    "test:regressions:dev": "concurrently \"yarn test:regressions:build --watch\" \"yarn test:regressions:server\"",
    "test:regressions:run": "mocha --config test/regressions/.mocharc.js --delay 'test/regressions/**/*.test.js'",
    "test:regressions:server": "serve test/regressions",
    "test:umd": "node packages/material-ui/test/umd/run.js",
    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/*.test.{js,ts,tsx}' 'docs/**/*.test.{js,ts,tsx}' 'scripts/**/*.test.{js,ts,tsx}' 'test/utils/**/*.test.{js,ts,tsx}'",
    "test:watch": "yarn test:unit --watch",
    "test:argos": "node ./scripts/pushArgos.js",
    "test"
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0 417896  4648 ?        Ss   12:06   0:00 sleep infinity
root         7  0.0  0.0 419788  6796 ?        Ss   12:06   0:00 bash -lc yarn -s mocha packages/material-ui/src/Tabs/repro.test.js packages/material-ui/src/Tabs/Tabs.test.js 2>&1 | tail -30
root        15  0.1  0.5 1049140 84260 ?       Sl   12:06   0:00 node --no-opt -r /proc/.reset /usr/local/nvm/versions/node/v16.20.2/bin/yarn -s mocha packages/material-ui/src/Tabs/repro.test.js packages/material-ui/src/Tabs/Tabs.test.js
root        16  0.0  0.0 417936  4636 ?        S    12:06   0:00 tail -30
root        23  0.1  0.5 1215280 92992 ?       Sl   12:06   0:00 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/.yarn/releases/yarn-1.22.10.js -s mocha packages/material-ui/src/Tabs/repro.test.js packages/material-ui/src/Tabs/Tabs.test.js
root        34  0.0  0.0 418036  4892 ?        S    12:06   0:00 /bin/sh -c /testbed/node_modules/.bin/mocha packages/material-ui/src/Tabs/repro.test.js packages/material-ui/src/Tabs/Tabs.test.js
root        35  4.1  1.7 1167552 282872 ?      Sl   12:06   0:17 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/.bin/mocha packages/material-ui/src/Tabs/repro.test.js packages/material-ui/src/Tabs/Tabs.test.js
root        42  0.0  0.0 419788  6344 ?        Ss   12:13   0:00 bash -lc ps aux | head -20
root        50  0.0  0.0 422300  5172 ?        R    12:13   0:00 ps aux
root        51  0.0  0.0 417908  2972 ?        S    12:13   0:00 head -20
```

**assistant:** Mocha is mostly idle, so it's probably finished but not exiting (the `tail` pipe hides output until exit). I'll kill it and rerun with `--exit`.

**tool call: Bash**

```bash
../bin/envrun 'pkill -f mocha; NODE_ENV=test timeout 300 node_modules/.bin/mocha --exit packages/material-ui/src/Tabs/repro.test.js packages/material-ui/src/Tabs/Tabs.test.js 2>&1 | tail -30'
```

tool result:

```
Exit code 143
```

**assistant:** `pkill -f mocha` matched its own shell command. Running the two steps separately:

**tool call: Bash**

```bash
../bin/envrun 'pkill -f node_modules/.bin/moch[a]; true'; ../bin/envrun 'NODE_ENV=test timeout 300 node_modules/.bin/mocha --exit packages/material-ui/src/Tabs/repro.test.js packages/material-ui/src/Tabs/Tabs.test.js > /tmp/out.txt 2>&1; echo rc=$?; tail -40 /tmp/out.txt'
```

tool result:

```
rc=1
    at Tabs (/testbed/packages/material-ui/src/Tabs/Tabs.js:202:44)
    at Wrapper (/testbed/test/utils/createClientRender.tsx:178:5)

Stack:
    at printWarning (/testbed/node_modules/react-dom/cjs/react-dom.development.js:67:30)
    at error (/testbed/node_modules/react-dom/cjs/react-dom.development.js:43:5)
    at warnIfNotCurrentlyActingEffectsInDEV (/testbed/node_modules/react-dom/cjs/react-dom.development.js:24051:7)
    at updateEffect (/testbed/node_modules/react-dom/cjs/react-dom.development.js:15743:7)
    at Object.useEffect (/testbed/node_modules/react-dom/cjs/react-dom.development.js:16394:14)
    at Object.useEffect (/testbed/node_modules/react/cjs/react.development.js:1520:21)
    at TouchRipple (/testbed/packages/material-ui/src/ButtonBase/TouchRipple.js:129:9)
    at renderWithHooks (/testbed/node_modules/react-dom/cjs/react-dom.development.js:14985:18)
    at updateForwardRef (/testbed/node_modules/react-dom/cjs/react-dom.development.js:17044:20)
    at beginWork (/testbed/node_modules/react-dom/cjs/react-dom.development.js:19098:16)
    at beginWork$1 (/testbed/node_modules/react-dom/cjs/react-dom.development.js:23940:14)
    at performUnitOfWork (/testbed/node_modules/react-dom/cjs/react-dom.development.js:22776:12)
    at workLoopSync (/testbed/node_modules/react-dom/cjs/react-dom.development.js:22707:5)
    at renderRootSync (/testbed/node_modules/react-dom/cjs/react-dom.development.js:22670:7)
    at performSyncWorkOnRoot (/testbed/node_modules/react-dom/cjs/react-dom.development.js:22293:18)
    at /testbed/node_modules/react-dom/cjs/react-dom.development.js:11327:26
    at unstable_runWithPriority (/testbed/node_modules/scheduler/cjs/scheduler.development.js:468:12)
    at runWithPriority$1 (/testbed/node_modules/react-dom/cjs/react-dom.development.js:11276:10)
    at flushSyncCallbackQueueImpl (/testbed/node_modules/react-dom/cjs/react-dom.development.js:11322:9)
    at flushSyncCallbackQueue (/testbed/node_modules/react-dom/cjs/react-dom.development.js:11309:3)
    at discreteUpdates$1 (/testbed/node_modules/react-dom/cjs/react-dom.development.js:22420:9)
    at discreteUpdates (/testbed/node_modules/react-dom/cjs/react-dom.development.js:3756:12)
    at dispatchDiscreteEvent (/testbed/node_modules/react-dom/cjs/react-dom.development.js:5889:3)
    at HTMLDivElement.callTheUserObjectsOperation (/testbed/node_modules/jsdom/lib/jsdom/living/generated/EventListener.js:26:30)
    at innerInvokeEventListeners (/testbed/node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:338:25)
    at invokeEventListeners (/testbed/node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:274:3)
    at HTMLButtonElementImpl._dispatch (/testbed/node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:221:9)
    at Object.exports.fireFocusEventWithTargetAdjustment (/testbed/node_modules/jsdom/lib/jsdom/living/helpers/focusing.js:103:10)
    at HTMLButtonElementImpl.focus (/testbed/node_modules/jsdom/lib/jsdom/living/nodes/HTMLOrSVGElement-impl.js:69:14)
    at HTMLButtonElement.focus (/testbed/node_modules/jsdom/lib/jsdom/living/generated/HTMLElement.js:119:34)
    at Context.<anonymous> (/testbed/packages/material-ui/src/Tabs/repro.test.js:19:7)
    at processImmediate (node:internal/timers:466:21)
```

**assistant:** My repro test triggers a React `act()` warning because it calls `a.focus()` directly. I'll wrap that in `act` and look at the summary.

**tool call: Bash**

```bash
sed -i '' 's/createClientRender, fireEvent }/act, createClientRender, fireEvent }/; s/^    a.focus();/    act(() => { a.focus(); });/' packages/material-ui/src/Tabs/repro.test.js && ../bin/envrun 'NODE_ENV=test timeout 300 node_modules/.bin/mocha --exit packages/material-ui/src/Tabs/repro.test.js packages/material-ui/src/Tabs/Tabs.test.js > /tmp/out.txt 2>&1; echo rc=$?; grep -nE "passing|failing|pending" /tmp/out.txt; grep -n -A15 "1) " /tmp/out.txt | head -40'
```

tool result:

```
rc=0
12:  69 passing (2s)
13:  7 pending
```

**assistant:** Everything passes. Now I'll confirm the repro actually fails without the fix:

**tool call: Bash**

```bash
git diff packages/material-ui/src/Tabs/Tabs.js > /tmp/fix.patch && git checkout packages/material-ui/src/Tabs/Tabs.js && ../bin/envrun 'NODE_ENV=test timeout 300 node_modules/.bin/mocha --exit packages/material-ui/src/Tabs/repro.test.js > /tmp/out.txt 2>&1; grep -nE "passing|failing|AssertionError" /tmp/out.txt | head'; git apply /tmp/fix.patch && git diff --stat packages/
```

tool result:

```
Exit code 128
(eval):1: operation not permitted: /tmp/fix.patch
error: can't open patch '/tmp/fix.patch': No such file or directory
```

**assistant:** Writing to `/tmp` was blocked, so the chain stopped before the checkout and the fix is still in place. I'll retry with the patch saved inside the repo:

**tool call: Bash**

```bash
git diff --stat packages/ && git diff packages/material-ui/src/Tabs/Tabs.js > fix.patch && git checkout packages/material-ui/src/Tabs/Tabs.js && ../bin/envrun 'NODE_ENV=test timeout 300 node_modules/.bin/mocha --exit packages/material-ui/src/Tabs/repro.test.js > /tmp/out.txt 2>&1; grep -nE "passing|failing|AssertionError" /tmp/out.txt | head'; git apply fix.patch && rm fix.patch && git diff --stat packages/
```

tool result:

```
 packages/material-ui/src/Tabs/Tabs.js | 61 +++++++++++++++++++++++++++++------
 1 file changed, 51 insertions(+), 10 deletions(-)
Updated 1 path from the index
11:  0 passing (261ms)
12:  2 failing

 packages/material-ui/src/Tabs/Tabs.js | 61 +++++++++++++++++++++++++++++------
 1 file changed, 51 insertions(+), 10 deletions(-)
```

**assistant:** The repro fails without the fix and passes with it. Last steps: lint the file and clean up.

**tool call: Bash**

```bash
rm packages/material-ui/src/Tabs/repro.test.js && ../bin/envrun 'node_modules/.bin/eslint packages/material-ui/src/Tabs/Tabs.js && node_modules/.bin/prettier --check packages/material-ui/src/Tabs/Tabs.js' ; git status --short
```

tool result:

```
Checking formatting...
All matched files use Prettier code style!

 M package.json
 M packages/material-ui/src/Tabs/Tabs.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
```

**assistant:** I fixed it: arrow keys in `Tabs` now skip disabled tabs and wrap from last to first and back, the same way `MenuList` skips disabled items. The change is all in `packages/material-ui/src/Tabs/Tabs.js`.

**What changed**
- Before, `handleKeyDown` always focused the next or previous sibling. A disabled tab can't take focus, so focus stayed put and traversal stopped there.
- I added three small helpers before the component: `nextItem` and `previousItem` (step to the neighbouring tab, wrapping at the ends) and `moveFocus` (keeps stepping until it reaches a tab that can take focus).
- A tab counts as unfocusable if it is disabled, has `aria-disabled="true"`, or has no `tabindex` — the same rule `MenuList` uses. A guard stops the loop once it has wrapped all the way round, so it can't run forever.
- Previous/next arrow keys (including the vertical and right-to-left layouts), Home and End all go through this. Home and End now land on the first or last *enabled* tab instead of a disabled one.

**Testing**
- I wrote a temporary test with tabs `[enabled, disabled, enabled, disabled]` covering Right, wrap-around Right, Left, End and Home. It failed without the fix and passed with it.
- Together with the existing `Tabs.test.js`: 69 passing, 7 pending, 0 failing. ESLint and Prettier are clean on the changed file.
- I deleted the temporary test afterwards.

`package.json`, `yarn.lock`, `Dockerfile` and `custom-reporter.js` show as changed or untracked, but those changes came from the environment setup, not from me, and I left them alone.

_session end: success, turns 21, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.14 s: ps aux | head -20
- `rc=143` 0.14 s: pkill -f mocha; NODE_ENV=test timeout 300 node_modules/.bin/mocha --exit packages/material-ui/src/Tabs/repro.test.js packages/material-ui/src/Tabs/Tabs.test.js 2>&1 | tail -30
- `rc=143` 432.63 s: yarn -s mocha packages/material-ui/src/Tabs/repro.test.js packages/material-ui/src/Tabs/Tabs.test.js 2>&1 | tail -30
- `rc=0` 0.13 s: pkill -f node_modules/.bin/moch[a]; true
- `rc=0` 8.98 s: NODE_ENV=test timeout 300 node_modules/.bin/mocha --exit packages/material-ui/src/Tabs/repro.test.js packages/material-ui/src/Tabs/Tabs.test.js > /tmp/out.txt 2>&1; echo rc=$?; tail -40 /tmp/out.txt
- `rc=0` 4.6 s: NODE_ENV=test timeout 300 node_modules/.bin/mocha --exit packages/material-ui/src/Tabs/repro.test.js packages/material-ui/src/Tabs/Tabs.test.js > /tmp/out.txt 2>&1; echo rc=$?; grep -nE "passing|failing|pending" /tmp/out.txt; grep -n -A15 "1) " /tmp/out.txt | head -40
- `rc=0` 2.96 s: NODE_ENV=test timeout 300 node_modules/.bin/mocha --exit packages/material-ui/src/Tabs/repro.test.js > /tmp/out.txt 2>&1; grep -nE "passing|failing|AssertionError" /tmp/out.txt | head
- `rc=0` 4.7 s: node_modules/.bin/eslint packages/material-ui/src/Tabs/Tabs.js && node_modules/.bin/prettier --check packages/material-ui/src/Tabs/Tabs.js
