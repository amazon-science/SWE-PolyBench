# Instance: mui__material-ui-26170

- Final resolved (evaluator, logs/mui__material-ui-26170_result.json): True
- Run state: DONE
- One attempt. Duration 573.0 s, turns 15, actor cost $0.2613406, container commands 5
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/mui__material-ui-26170/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-26170/repo. Consider the following issue description:

<issue_description>
[TabList] Conditional rendering of Tab fails
<!-- Provide a general summary of the issue in the Title above -->

<!--
  Thank you very much for contributing to Material-UI by creating an issue! ❤️
  To avoid duplicate issues we ask you to check off the following list.
-->

<!-- Checked checkbox should look like this: [x] -->

- [x] The issue is present in the latest release.
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Current Behavior 😯
As pointed on [Issue 8093](https://github.com/mui-org/material-ui/issues/8093), when we have a conditional rendering of a Tab, it throws an error.
<!-- Describe what happens instead of the expected behavior. -->

## Expected Behavior 🤔
The expected behavior is not to consider a null as a valid component. This issue was resolved by [PR 8107](https://github.com/mui-org/material-ui/pull/8107), but for Tabs component.
<!-- Describe what should happen. -->

## Steps to Reproduce 🕹

Just use a condition to render a Tab inside a TabList

[Live example on CodeSandbox](https://codesandbox.io/s/materialui-tablist-conditional-tab-bug-f4rqy)
<!--
  Provide a link to a live example (you can use codesandbox.io) and an unambiguous set of steps to reproduce this bug.
  Include code to reproduce, if relevant (which it most likely is).

  You should use the official codesandbox template as a starting point: https://material-ui.com/r/issue-template-next

  If you have an issue concerning TypeScript please start from this TypeScript playground: https://material-ui.com/r/ts-issue-template

  Issues without some form of live example have a longer response time.
-->

Steps:

1. Render a TabList
2. Render some Tabs
3. Conditionaly render a Tab inside TabList

## Context 🔦

<!--
  What are you trying to accomplish? How has this issue affected you?
  Providing context helps us come up with a solution that is most useful in the real world.
-->
I was trying to render a Tab depending on a user state.

## Your Environment 🌎

<!--
  Run `npx @material-ui/envinfo` and post the results.
  If you encounter issues with TypeScript please include the used tsconfig.
-->
<details>
  <summary>`npx @material-ui/envinfo`</summary>
  
```
  System:
    OS: Linux 5.4 Linux Mint 20.1 (Ulyssa)
  Binaries:
    Node: 14.16.0 - /usr/local/bin/node
    Yarn: 1.22.10 - /usr/local/bin/yarn
    npm: 6.14.13 - /usr/local/bin/npm
  Browsers:
    Chrome: 90.0.4430.93
    Firefox: 88.0.1
  npmPackages:
    @material-ui/core: ^4.11.3 => 4.11.3 
    @material-ui/icons: ^4.11.2 => 4.11.2 
    @material-ui/lab: ^4.0.0-alpha.57 => 4.0.0-alpha.57 
    @material-ui/pickers: ^3.3.10 => 3.3.10 
    @material-ui/styles: ^4.11.3 => 4.11.3 
    @material-ui/system:  4.11.3 
    @material-ui/types:  5.1.0 
    @material-ui/utils:  4.11.2 
    @types/react:  17.0.3 
    react: ^17.0.1 => 17.0.1 
    react-dom: ^17.0.1 => 17.0.1 
    styled-components:  5.2.1
```
</details>


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-26170/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-26170/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-26170/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-26170/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
ls packages/material-ui-lab/src/TabList && cat packages/material-ui-lab/src/TabList/TabList.js
```

tool result:

```
TabList.d.ts
TabList.js
TabList.test.js
index.d.ts
index.js
import * as React from 'react';
import PropTypes from 'prop-types';
import Tabs from '@material-ui/core/Tabs';
import { useTabContext, getTabId, getPanelId } from '../TabContext';

const TabList = React.forwardRef(function TabList(props, ref) {
  const { children: childrenProp, ...other } = props;
  const context = useTabContext();
  if (context === null) {
    throw new TypeError('No TabContext provided');
  }
  const children = React.Children.map(childrenProp, (child) => {
    return React.cloneElement(child, {
      // SOMEDAY: `Tabs` will set those themselves
      'aria-controls': getPanelId(context, child.props.value),
      id: getTabId(context, child.props.value),
    });
  });

  return (
    <Tabs {...other} ref={ref} value={context.value}>
      {children}
    </Tabs>
  );
});

TabList.propTypes /* remove-proptypes */ = {
  // ----------------------------- Warning --------------------------------
  // | These PropTypes are generated from the TypeScript type definitions |
  // |     To update them edit the d.ts file and run "yarn proptypes"     |
  // ----------------------------------------------------------------------
  /**
   * A list of `<Tab />` elements.
   */
  children: PropTypes.arrayOf(PropTypes.element),
};

export default TabList;
```

**tool call: Bash**

```bash
cat packages/material-ui-lab/src/TabList/TabList.d.ts; cat packages/material-ui-lab/src/TabList/TabList.test.js | head -60
```

tool result:

```
import * as React from 'react';
import { TabsTypeMap } from '@material-ui/core/Tabs';
import { DistributiveOmit } from '@material-ui/types';
import { OverridableComponent, OverrideProps } from '@material-ui/core/OverridableComponent';

export interface TabListTypeMap<
  P = {},
  D extends React.ElementType = TabsTypeMap['defaultComponent']
> {
  props: P & {
    /**
     * A list of `<Tab />` elements.
     */
    children?: React.ReactElement[];
  } & DistributiveOmit<TabsTypeMap['props'], 'children' | 'value'>;
  defaultComponent: D;
}
/**
 *
 * Demos:
 *
 * - [Tabs](https://material-ui.com/components/tabs/)
 *
 * API:
 *
 * - [TabList API](https://material-ui.com/api/tab-list/)
 * - inherits [Tabs API](https://material-ui.com/api/tabs/)
 */
declare const TabList: OverridableComponent<TabListTypeMap>;

export type TabListClassKey = keyof NonNullable<TabListTypeMap['props']['classes']>;

export type TabListProps<
  D extends React.ElementType = TabListTypeMap['defaultComponent'],
  P = {}
> = OverrideProps<TabListTypeMap<P, D>, D>;

export default TabList;
// @ts-check
import * as React from 'react';
import { expect } from 'chai';
import { createClientRender, createMount, describeConformance } from 'test/utils';
import Tab from '@material-ui/core/Tab';
import Tabs, { tabsClasses as classes } from '@material-ui/core/Tabs';
import TabList from './TabList';
import TabContext from '../TabContext';

describe('<TabList />', () => {
  const mount = createMount();
  const render = createClientRender();

  /**
   *
   * @param {React.ReactNode} node
   */
  function mountInContext(node) {
    const wrapper = mount(<TabContext value="0">{node}</TabContext>);
    return wrapper.childAt(0);
  }

  describeConformance(<TabList />, () => ({
    classes,
    inheritComponent: Tabs,
    /**
     * @param {React.ReactNode} node
     */
    render: (node) => render(<TabContext value="0">{node}</TabContext>),
    mount: mountInContext,
    refInstanceof: window.HTMLDivElement,
    // TODO: no idea why reactTestRenderer fails
    skip: [/** @type {'reactTestRenderer'} */ ('reactTestRenderer')],
  }));

  // outside of TabContext pass every test in Tabs

  it('provides the active value to Tab so that they can be indicated as selected', () => {
    const { getAllByRole } = render(
      <TabContext value="0">
        <TabList>
          <Tab value="0" />
          <Tab value="1" />
        </TabList>
      </TabContext>,
    );
    const [tabOne, tabTwo] = getAllByRole('tab');

    expect(tabOne).to.have.attribute('aria-selected', 'true');
    expect(tabTwo).to.have.attribute('aria-selected', 'false');
  });
});
```

**assistant:** Reproduce first with a quick test file.

**tool call: Bash**

```bash
cat > packages/material-ui-lab/src/TabList/Repro.test.js <<'EOF'
import * as React from 'react';
import { expect } from 'chai';
import { createClientRender } from 'test/utils';
import Tab from '@material-ui/core/Tab';
import TabList from './TabList';
import TabContext from '../TabContext';

describe('repro', () => {
  const render = createClientRender();
  it('accepts null children', () => {
    const { getAllByRole } = render(
      <TabContext value="0">
        <TabList>
          <Tab value="0" />
          {null}
          {false && <Tab value="2" />}
        </TabList>
      </TabContext>,
    );
    expect(getAllByRole('tab')).to.have.length(1);
  });
});
EOF
../bin/envrun 'yarn -s mocha packages/material-ui-lab/src/TabList/Repro.test.js 2>&1 | tail -20'
```

tool result:

```
Command did not complete within its 120s timeout and was moved to the background (ID: bot6dw0r9). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/4a1101b0-871d-47e9-8b2f-f24d5186f7b4/tasks/bot6dw0r9.output. You will be notified when it completes. To check interim output, use Read on that file path.
```

**tool call: Bash**

```bash
sleep 100; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/4a1101b0-871d-47e9-8b2f-f24d5186f7b4/tasks/bot6dw0r9.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
sleep 120; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/4a1101b0-871d-47e9-8b2f-f24d5186f7b4/tasks/bot6dw0r9.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
cat .mocharc.js; grep '"test' package.json
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
```

**tool call: Bash**

```bash
sleep 180; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/4a1101b0-871d-47e9-8b2f-f24d5186f7b4/tasks/bot6dw0r9.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
../bin/envrun 'ps aux | grep -v grep | grep -E "mocha|node" | head'
```

tool result:

```
root         7  0.0  0.0 419788  6344 ?        Ss   12:15   0:00 bash -lc yarn -s mocha packages/material-ui-lab/src/TabList/Repro.test.js 2>&1 | tail -20
root        15  0.0  0.5 1049096 84112 ?       Sl   12:15   0:00 node --no-opt -r /proc/.reset /usr/local/nvm/versions/node/v16.20.2/bin/yarn -s mocha packages/material-ui-lab/src/TabList/Repro.test.js
root        23  0.1  0.5 1215300 91340 ?       Sl   12:15   0:00 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/.yarn/releases/yarn-1.22.10.js -s mocha packages/material-ui-lab/src/TabList/Repro.test.js
root        34  0.0  0.0 418032  3360 ?        S    12:15   0:00 /bin/sh -c /testbed/node_modules/.bin/mocha packages/material-ui-lab/src/TabList/Repro.test.js
root        35  1.7  1.3 1134580 217944 ?      Sl   12:15   0:09 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/.bin/mocha packages/material-ui-lab/src/TabList/Repro.test.js
```

**assistant:** The test process is hung, not just slow: it has used only ~9s of CPU, and piping through `tail` hides any output until it exits. I'll kill it and rerun with `--exit`.

**tool call: Bash**

```bash
../bin/envrun 'pkill -f mocha; timeout 300 node_modules/.bin/mocha --exit packages/material-ui-lab/src/TabList/Repro.test.js 2>&1 | head -40'
```

tool result:

```
Exit code 143
```

**tool call: Bash**

```bash
../bin/envrun 'timeout 300 node_modules/.bin/mocha --exit packages/material-ui-lab/src/TabList/Repro.test.js 2>&1 | head -40'
```

tool result:

```
Browserslist: caniuse-lite is outdated. Please run:
npx browserslist@latest --update-db

Why you should do it regularly:
https://github.com/browserslist/browserslist#browsers-data-updating
including inaccessible elements by default


  !!

  0 passing (39ms)
  2 failing

  1) repro
       accepts null children:
     TypeError: Cannot read properties of null (reading 'props')
      at /testbed/packages/material-ui-lab/src/TabList/TabList.js:15:50
      at /testbed/node_modules/react/cjs/react.development.js:1067:17
      at mapIntoArray (node_modules/react/cjs/react.development.js:964:23)
      at mapIntoArray (node_modules/react/cjs/react.development.js:1004:23)
      at Object.map (node_modules/react/cjs/react.development.js:1066:3)
      at TabList (packages/material-ui-lab/src/TabList/TabList.js:12:35)
      at renderWithHooks (node_modules/react-dom/cjs/react-dom.development.js:14985:18)
      at updateForwardRef (node_modules/react-dom/cjs/react-dom.development.js:17044:20)
      at beginWork (node_modules/react-dom/cjs/react-dom.development.js:19098:16)
      at HTMLUnknownElement.callCallback (node_modules/react-dom/cjs/react-dom.development.js:3945:14)
      at HTMLUnknownElement.callTheUserObjectsOperation (node_modules/jsdom/lib/jsdom/living/generated/EventListener.js:26:30)
      at innerInvokeEventListeners (node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:338:25)
      at invokeEventListeners (node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:274:3)
      at HTMLUnknownElementImpl._dispatch (node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:221:9)
      at HTMLUnknownElementImpl.dispatchEvent (node_modules/jsdom/lib/jsdom/living/events/EventTarget-impl.js:94:17)
      at HTMLUnknownElement.dispatchEvent (node_modules/jsdom/lib/jsdom/living/generated/EventTarget.js:231:34)
      at Object.invokeGuardedCallbackDev (node_modules/react-dom/cjs/react-dom.development.js:3994:16)
      at invokeGuardedCallback (node_modules/react-dom/cjs/react-dom.development.js:4056:31)
      at beginWork$1 (node_modules/react-dom/cjs/react-dom.development.js:23964:7)
      at performUnitOfWork (node_modules/react-dom/cjs/react-dom.development.js:22776:12)
      at workLoopSync (node_modules/react-dom/cjs/react-dom.development.js:22707:5)
      at renderRootSync (node_modules/react-dom/cjs/react-dom.development.js:22670:7)
      at performSyncWorkOnRoot (node_modules/react-dom/cjs/react-dom.development.js:22293:18)
      at scheduleUpdateOnFiber (node_modules/react-dom/cjs/react-dom.development.js:21881:7)
```

**thinking:**

```
I reproduced the error: `TabList` crashes because it calls `cloneElement` on null/false children instead of skipping them like `Tabs` does. I'll fix `TabList` to skip invalid elements and loosen the `children` type/propTypes to avoid warnings on conditional children.


```

**tool call: Bash**

```bash
cd packages/material-ui-lab/src/TabList && python3 - <<'EOF'
p='TabList.js'
s=open(p).read()
s=s.replace("""  const children = React.Children.map(childrenProp, (child) => {
    return""","""  const children = React.Children.map(childrenProp, (child) => {
    if (!React.isValidElement(child)) {
      return null;
    }

    return""")
s=s.replace("children: PropTypes.arrayOf(PropTypes.element),","children: PropTypes.node,")
open(p,'w').write(s)
p='TabList.d.ts'
s=open(p).read()
s=s.replace("children?: React.ReactElement[];","children?: React.ReactNode;")
open(p,'w').write(s)
EOF
git diff; grep -rn "arrayOf" ../../../../docs/pages/api-docs/tab-list.json
```

tool result:

```
<persisted-output>
Output too large (1.4MB). Full output saved to: <actor-session-dir>

Preview (first 2KB):
diff --git a/package.json b/package.json
index 30d3698464..f8bbe1ac9d 100644
--- a/package.json
+++ b/package.json
@@ -83,17 +83,20 @@
     "@rollup/plugin-replace": "^2.3.1",
     "@testing-library/dom": "^7.22.1",
     "@testing-library/react": "^11.0.2",
-    "@types/chai": "^4.2.3",
+    "@types/chai": "^4.3.20",
     "@types/chai-dom": "^0.0.10",
     "@types/enzyme": "^3.10.3",
-    "@types/format-util": "^1.0.1",
+    "@types/format-util": "^1.0.4",
     "@types/fs-extra": "^9.0.0",
     "@types/jsdom": "^16.1.0",
     "@types/lodash": "^4.14.138",
     "@types/mocha": "^8.0.0",
     "@types/prettier": "^2.0.0",
+    "@types/prop-types": "^15.7.15",
     "@types/react": "^17.0.3",
-    "@types/sinon": "^10.0.0",
+    "@types/react-dom": "^19.1.7",
+    "@types/sinon": "^10.0.20",
+    "@types/testing-library__react": "^10.2.0",
     "@types/webpack": "^4.41.22",
     "@types/yargs": "^16.0.0",
     "@typescript-eslint/eslint-plugin": "^4.11.1",
diff --git a/packages/material-ui-lab/src/TabList/TabList.d.ts b/packages/material-ui-lab/src/TabList/TabList.d.ts
index acb3fe4a95..1e90265690 100644
--- a/packages/material-ui-lab/src/TabList/TabList.d.ts
+++ b/packages/material-ui-lab/src/TabList/TabList.d.ts
@@ -11,7 +11,7 @@ export interface TabListTypeMap<
     /**
      * A list of `<Tab />` elements.
      */
-    children?: React.ReactElement[];
+    children?: React.ReactNode;
   } & DistributiveOmit<TabsTypeMap['props'], 'children' | 'value'>;
   defaultComponent: D;
 }
diff --git a/packages/material-ui-lab/src/TabList/TabList.js b/packages/material-ui-lab/src/TabList/TabList.js
index 95a1783db7..6cf2dce143 100644
--- a/packages/material-ui-lab/src/TabList/TabList.js
+++ b/packages/material-ui-lab/src/TabList/TabList.js
@@ -10,6 +10,10 @@ const TabList = React.forwardRef(function TabList(props, ref) {
     throw new TypeError('No TabContext provided');
   }
   const children = React.Children.map(childrenProp, (child) => {
...
</persisted-output>
```

**assistant:** The diff contains much more than my edit. Before going on, I'll check which files actually differ.

**tool call: Bash**

```bash
cd /work/mui__material-ui-26170/repo && git status --short | head; git diff --stat | tail -3; grep -n "children" docs/pages/api-docs/tab-list.json
```

tool result:

```
 M package.json
 M packages/material-ui-lab/src/TabList/TabList.d.ts
 M packages/material-ui-lab/src/TabList/TabList.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
?? packages/material-ui-lab/src/TabList/Repro.test.js
 packages/material-ui-lab/src/TabList/TabList.js   |     6 +-
 yarn.lock                                         | 31128 ++++++++++----------
 4 files changed, 16384 insertions(+), 14761 deletions(-)
2:  "props": { "children": { "type": { "name": "arrayOf", "description": "Array&lt;element&gt;" } } },
```

**thinking:**

```
I'll leave the pre-existing changes to package.json, yarn.lock, Dockerfile, and custom-reporter.js untouched. Next, I'll update the generated API docs JSON for the new `children` type, then rerun the repro and existing TabList tests.


```

**tool call: Bash**

```bash
sed -i '' 's|"children": { "type": { "name": "arrayOf", "description": "Array&lt;element&gt;" } }|"children": { "type": { "name": "node" } }|' docs/pages/api-docs/tab-list.json && head -3 docs/pages/api-docs/tab-list.json
../bin/envrun 'timeout 300 node_modules/.bin/mocha --exit packages/material-ui-lab/src/TabList/*.test.js 2>&1 | tail -15'
```

tool result:

```
{
  "props": { "children": { "type": { "name": "node" } } },
  "name": "TabList",
Browserslist: caniuse-lite is outdated. Please run:
npx browserslist@latest --update-db

Why you should do it regularly:
https://github.com/browserslist/browserslist#browsers-data-updating
including inaccessible elements by default


  ․․․․․․․

  7 passing (463ms)
```

**assistant:** Everything passes now: the repro and all existing TabList tests (7 passing). I'll delete the repro file.

**tool call: Bash**

```bash
rm packages/material-ui-lab/src/TabList/Repro.test.js && git status --short && git diff packages/material-ui-lab docs
```

tool result:

```
 M docs/pages/api-docs/tab-list.json
 M package.json
 M packages/material-ui-lab/src/TabList/TabList.d.ts
 M packages/material-ui-lab/src/TabList/TabList.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
diff --git a/docs/pages/api-docs/tab-list.json b/docs/pages/api-docs/tab-list.json
index 443416edc7..18ccb94679 100644
--- a/docs/pages/api-docs/tab-list.json
+++ b/docs/pages/api-docs/tab-list.json
@@ -1,5 +1,5 @@
 {
-  "props": { "children": { "type": { "name": "arrayOf", "description": "Array&lt;element&gt;" } } },
+  "props": { "children": { "type": { "name": "node" } } },
   "name": "TabList",
   "styles": { "classes": [], "globalClasses": {}, "name": null },
   "spread": true,
diff --git a/packages/material-ui-lab/src/TabList/TabList.d.ts b/packages/material-ui-lab/src/TabList/TabList.d.ts
index acb3fe4a95..1e90265690 100644
--- a/packages/material-ui-lab/src/TabList/TabList.d.ts
+++ b/packages/material-ui-lab/src/TabList/TabList.d.ts
@@ -11,7 +11,7 @@ export interface TabListTypeMap<
     /**
      * A list of `<Tab />` elements.
      */
-    children?: React.ReactElement[];
+    children?: React.ReactNode;
   } & DistributiveOmit<TabsTypeMap['props'], 'children' | 'value'>;
   defaultComponent: D;
 }
diff --git a/packages/material-ui-lab/src/TabList/TabList.js b/packages/material-ui-lab/src/TabList/TabList.js
index 95a1783db7..6cf2dce143 100644
--- a/packages/material-ui-lab/src/TabList/TabList.js
+++ b/packages/material-ui-lab/src/TabList/TabList.js
@@ -10,6 +10,10 @@ const TabList = React.forwardRef(function TabList(props, ref) {
     throw new TypeError('No TabContext provided');
   }
   const children = React.Children.map(childrenProp, (child) => {
+    if (!React.isValidElement(child)) {
+      return null;
+    }
+
     return React.cloneElement(child, {
       // SOMEDAY: `Tabs` will set those themselves
       'aria-controls': getPanelId(context, child.props.value),
@@ -32,7 +36,7 @@ TabList.propTypes /* remove-proptypes */ = {
   /**
    * A list of `<Tab />` elements.
    */
-  children: PropTypes.arrayOf(PropTypes.element),
+  children: PropTypes.node,
 };
 
 export default TabList;
```

**assistant:** `TabList` no longer crashes when a `Tab` is rendered conditionally (`{cond && <Tab … />}` or `{null}`).

**Cause:** `TabList` called `React.cloneElement(child, …)` and read `child.props.value` for every child. A `null` or `false` child threw `TypeError: Cannot read properties of null (reading 'props')`. I reproduced this with a small test before changing anything.

**Changes:**
- **`packages/material-ui-lab/src/TabList/TabList.js`:** children that aren't valid React elements are now skipped instead of cloned. `Tabs` already ignores such children, which is how #8107 fixed the same bug there.
- **`TabList.js` propTypes and `TabList.d.ts`:** `children` is now `PropTypes.node` / `React.ReactNode` instead of an array of elements. Without this, conditional children would still raise a prop-type warning and be rejected by TypeScript.
- **`docs/pages/api-docs/tab-list.json`:** I edited this by hand to match the new propType; I didn't run the docs generator.

**Testing:** The repro (one real `Tab` plus `{null}` and `{false && <Tab/>}`, expecting one tab to render) passes now, and so do all existing `TabList` tests: 7 passing in total. I didn't run a TypeScript type check on the `.d.ts` change. I deleted the repro file afterwards.

The working tree also shows changes to `package.json` and `yarn.lock`, plus untracked `Dockerfile` and `custom-reporter.js`. Those were already there before I started, and I left them untouched.

_session end: success, turns 15, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.13 s: ps aux | grep -v grep | grep -E "mocha|node" | head
- `rc=143` 0.14 s: pkill -f mocha; timeout 300 node_modules/.bin/mocha --exit packages/material-ui-lab/src/TabList/Repro.test.js 2>&1 | head -40
- `rc=143` 533.83 s: yarn -s mocha packages/material-ui-lab/src/TabList/Repro.test.js 2>&1 | tail -20
- `rc=0` 2.55 s: timeout 300 node_modules/.bin/mocha --exit packages/material-ui-lab/src/TabList/Repro.test.js 2>&1 | head -40
- `rc=0` 4.01 s: timeout 300 node_modules/.bin/mocha --exit packages/material-ui-lab/src/TabList/*.test.js 2>&1 | tail -15
