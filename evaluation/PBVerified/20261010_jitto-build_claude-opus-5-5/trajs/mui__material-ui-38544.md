# Instance: mui__material-ui-38544

- Final resolved (evaluator, logs/mui__material-ui-38544_result.json): True
- Run state: DONE
- One attempt. Duration 68.3 s, turns 9, actor cost $0.156368, container commands 4
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/mui__material-ui-38544/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-38544/repo. Consider the following issue description:

<issue_description>
[Tabs] Scrollable tabs crashes when overriding styles in theme using slots callback
### Duplicates

- [X] I have searched the existing issues

### Latest version

- [X] I have tested the latest version

### Steps to reproduce 🕹

Link to live example: https://codesandbox.io/s/mui-tabs-style-override-crash-p9wfjm-p9wfjm?file=/package.json

Downgrading the package version in the live example will "fix" the error.

Steps:

1. Use a `Tabs` component, set its variant to `scrollable`.
2. Create a custom theme which uses a function to override `Tabs` styling. This function uses the `props` parameter to decide which styles to apply. The `ownerState.orientation` field is deconstructed out of the object.


### Current behavior 😯

The rendering crashes, stating that `_ref.ownerState` is undefined (where `_ref` is the name of the `props` parameter after downleveling). This happens because the `props` object does not have the `ownerState` prop, even though its typings suggest that it does have that prop.

### Expected behavior 🤔

The `props` object should have the `ownerState` prop, as the typings describe.

### Context 🔦

This appears to happen because `TabsScrollbarSize` is being rendered. It uses the same style overrides as the other `Tabs` components, but it does not get an `ownerState` prop. Thus, it is undefined.

### Your environment 🌎

This error started appearing during routine package upgrades. In one package, it began to occur after upgrading from `5.14.2` to `5.14.4`. But in others, the upgrade to `5.14.4` did not trigger the same issue, and only appeared when we forced nested dependencies to upgrade as well.

We are not completely sure, but believe that it is related to `@mui/system`. Downgrading that package appears to resolve the issue on the latest version of `@mui/material`.

```
"resolutions": {
    "@mui/system": "5.14.1"
}
```

It happens in all browsers.

<details>
  <summary><code>npx @mui/envinfo</code></summary>

```
  System:
    OS: Windows 10 10.0.22621
  Binaries:
    Node: 18.17.0 - C:\Program Files\nodejs\node.EXE
    Yarn: 1.22.19 - C:\Program Files\nodejs\yarn.CMD
    npm: 9.6.7 - C:\Program Files\nodejs\npm.CMD
  Browsers:
    Chrome: Not Found
    Edge: Spartan (44.22621.1992.0), Chromium (115.0.1901.200)
  npmPackages:
    @emotion/react: 11.11.1 => 11.11.1 
    @emotion/styled: 11.11.0 => 11.11.0 
    @mui/base:  5.0.0-beta.10 
    @mui/core-downloads-tracker:  5.14.4 
    @mui/material: 5.14.4 => 5.14.4 
    @mui/private-theming:  5.14.4 
    @mui/styled-engine:  5.13.2 
    @mui/system:  5.14.4 
    @mui/types:  7.2.4 
    @mui/utils:  5.14.4 
    @types/react: 18.2.18 => 18.2.18 
    react: 18.2.0 => 18.2.0 
    react-dom: 18.2.0 => 18.2.0 
    typescript: 5.1.6 => 5.1.6 
```
</details>


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-38544/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-38544/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-38544/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-38544/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/mui__material-ui-38544/repo; grep -n "ScrollbarSize\|TabsScrollbarSize" -A12 packages/mui-material/src/Tabs/Tabs.js | head -80
```

tool result:

```
14:import ScrollbarSize from './ScrollbarSize';
15-import TabScrollButton from '../TabScrollButton';
16-import useEventCallback from '../utils/useEventCallback';
17-import tabsClasses, { getTabsUtilityClass } from './tabsClasses';
18-import ownerDocument from '../utils/ownerDocument';
19-import ownerWindow from '../utils/ownerWindow';
20-
21-const nextItem = (list, item) => {
22-  if (list === item) {
23-    return list.firstChild;
24-  }
25-  if (item && item.nextElementSibling) {
26-    return item.nextElementSibling;
--
216:const TabsScrollbarSize = styled(ScrollbarSize, {
217-  name: 'MuiTabs',
218:  slot: 'ScrollbarSize',
219-})({
220-  overflowX: 'auto',
221-  overflowY: 'hidden',
222-  // Hide dimensionless scrollbar on macOS
223-  scrollbarWidth: 'none', // Firefox
224-  '&::-webkit-scrollbar': {
225-    display: 'none', // Safari + Chrome
226-  },
227-});
228-
229-const defaultIndicatorStyle = {};
230-
--
491:  // TODO Remove <ScrollbarSize /> as browser support for hiding the scrollbar
492-  // with CSS improves.
493:  const handleScrollbarSizeChange = React.useCallback((scrollbarWidth) => {
494-    setScrollerStyle({
495-      overflow: null,
496-      scrollbarWidth,
497-    });
498-  }, []);
499-
500-  const getConditionalElements = () => {
501-    const conditionalElements = {};
502-
503-    conditionalElements.scrollbarSizeListener = scrollable ? (
504:      <TabsScrollbarSize
505:        onChange={handleScrollbarSizeChange}
506-        className={clsx(classes.scrollableX, classes.hideScrollbar)}
507-      />
508-    ) : null;
509-
510-    const scrollButtonsActive = displayStartScroll || displayEndScroll;
511-    const showScrollButtons =
512-      scrollable && ((scrollButtons === 'auto' && scrollButtonsActive) || scrollButtons === true);
513-
514-    conditionalElements.scrollButtonStart = showScrollButtons ? (
515-      <ScrollButtonComponent
516-        slots={{ StartScrollButtonIcon: slots.StartScrollButtonIcon }}
517-        slotProps={{ startScrollButtonIcon: startScrollButtonIconProps }}
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-38544/repo; cat packages/mui-material/src/Tabs/ScrollbarSize.js | head -30; grep -n "ShouldForwardProp" -A5 packages/mui-system/src/createStyled.js | head -60
```

tool result:

```
'use client';
import * as React from 'react';
import PropTypes from 'prop-types';
import debounce from '../utils/debounce';
import { ownerWindow, unstable_useEnhancedEffect as useEnhancedEffect } from '../utils';

const styles = {
  width: 99,
  height: 99,
  position: 'absolute',
  top: -9999,
  overflow: 'scroll',
};

/**
 * @ignore - internal component.
 * The component originates from https://github.com/STORIS/react-scrollbar-size.
 * It has been moved into the core in order to minimize the bundle size.
 */
export default function ScrollbarSize(props) {
  const { onChange, ...other } = props;
  const scrollbarHeight = React.useRef();
  const nodeRef = React.useRef(null);

  const setMeasurements = () => {
    scrollbarHeight.current = nodeRef.current.offsetHeight - nodeRef.current.clientHeight;
  };

  useEnhancedEffect(() => {
    const handleResize = debounce(() => {
97:    rootShouldForwardProp = shouldForwardProp,
98:    slotShouldForwardProp = shouldForwardProp,
99-  } = input;
100-
101-  const systemSx = (props) => {
102-    return styleFunctionSx({ ...props, theme: resolveTheme({ ...props, defaultTheme, themeId }) });
103-  };
--
146:      shouldForwardPropOption = rootShouldForwardProp;
147-    } else if (componentSlot) {
148-      // any other slot specified
149:      shouldForwardPropOption = slotShouldForwardProp;
150-    } else if (isStringTag(tag)) {
151-      // for string (html) tag, preserve the behavior in emotion & styled-components.
152-      shouldForwardPropOption = undefined;
153-    }
154-
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-38544/repo; cat packages/mui-material/src/styles/styled.js; git log --oneline -1; grep -n "ScrollbarSize\|ownerState" packages/mui-material/src/Tabs/Tabs.test.js | head -20
```

tool result:

```
'use client';
import { createStyled, shouldForwardProp } from '@mui/system';
import defaultTheme from './defaultTheme';
import THEME_ID from './identifier';

export const rootShouldForwardProp = (prop) => shouldForwardProp(prop) && prop !== 'classes';

export const slotShouldForwardProp = shouldForwardProp;

const styled = createStyled({
  themeId: THEME_ID,
  defaultTheme,
  rootShouldForwardProp,
});

export default styled;
f22e995193 [docs-infra] Improve show code button affordance (#38824)
182:          endScrollButtonIcon: (ownerState) => ({
184:            fontSize: ownerState.textColor === 'secondary' ? 'large' : 'small',
186:          startScrollButtonIcon: (ownerState) => ({
188:            fontSize: ownerState.textColor === 'secondary' ? 'large' : 'small',
```

**assistant:** Material's `styled` filters out `ownerState` for slot components, so passing it won't leak onto the DOM. First, a quick reproduction:

**tool call: Bash**

```bash
cd /work/mui__material-ui-38544/repo; cat > packages/mui-material/src/Tabs/repro.test.js <<'EOF'
import * as React from 'react';
import { expect } from 'chai';
import { createRenderer } from 'test/utils';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import { createTheme, ThemeProvider } from '@mui/material/styles';

describe('repro', () => {
  const { render } = createRenderer();
  it('should not crash', () => {
    const theme = createTheme({
      components: {
        MuiTabs: {
          styleOverrides: {
            root: ({ ownerState: { orientation } }) => ({ ...(orientation === 'vertical' ? { color: 'red' } : {}) }),
          },
        },
      },
    });
    const { container } = render(
      <ThemeProvider theme={theme}>
        <Tabs value={0} variant="scrollable"><Tab /></Tabs>
      </ThemeProvider>,
    );
    expect(container.firstChild).not.to.equal(null);
  });
});
EOF
../bin/envrun 'yarn cross-env NODE_ENV=test mocha packages/mui-material/src/Tabs/repro.test.js 2>&1 | tail -20'
```

tool result:

```
    at commitRoot (/testbed/node_modules/react-dom/cjs/react-dom.development.js:26682:5)
    at finishConcurrentRender (/testbed/node_modules/react-dom/cjs/react-dom.development.js:25892:9)
    at performConcurrentWorkOnRoot (/testbed/node_modules/react-dom/cjs/react-dom.development.js:25809:7)
    at flushActQueue (/testbed/node_modules/react/cjs/react.development.js:2667:24)
    at act (/testbed/node_modules/react/cjs/react.development.js:2582:11)
    at /testbed/node_modules/@testing-library/react/dist/act-compat.js:46:25
    at renderRoot (/testbed/node_modules/@testing-library/react/dist/pure.js:161:26)
    at render (/testbed/node_modules/@testing-library/react/dist/pure.js:247:10)
    at callback (/testbed/test/utils/createRenderer.tsx:290:25)
    at traceSync (/testbed/test/utils/createRenderer.tsx:29:10)
    at render (/testbed/test/utils/createRenderer.tsx:289:38)
    at render (/testbed/test/utils/createRenderer.tsx:589:14)
    at Context.<anonymous> (/testbed/packages/mui-material/src/Tabs/repro.test.js:20:27)
    at processImmediate (node:internal/timers:466:21)
  



error Command failed with exit code 2.
info Visit https://yarnpkg.com/en/docs/cli/run for documentation about this command.
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-38544/repo; ../bin/envrun 'yarn cross-env NODE_ENV=test mocha packages/mui-material/src/Tabs/repro.test.js 2>&1 | grep -m3 Error'
```

tool result:

```
     TypeError: Cannot read properties of undefined (reading 'orientation')
      at recoverFromConcurrentError (node_modules/react-dom/cjs/react-dom.development.js:25850:20)
If the warning is expected, test for it explicitly by using the toErrorDev() matcher.
```

**assistant:** Reproduced. Now the fix:

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/mui__material-ui-38544/repo/packages/mui-material/src/Tabs/Tabs.js",
 "old_string": "      <TabsScrollbarSize\n        onChange={handleScrollbarSizeChange}",
 "new_string": "      <TabsScrollbarSize\n        onChange={handleScrollbarSizeChange}\n        ownerState={ownerState}"
}
```

tool result:

```
The file /work/mui__material-ui-38544/repo/packages/mui-material/src/Tabs/Tabs.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-38544/repo; ../bin/envrun 'yarn cross-env NODE_ENV=test mocha packages/mui-material/src/Tabs/repro.test.js 2>&1 | tail -8'
```

tool result:

```
including inaccessible elements by default


  .

  1 passing (165ms)

Done in 4.69s.
```

**assistant:** The repro passes now, and no unknown-prop warning showed up (the test harness fails on unexpected console errors). Next I'll run the existing Tabs tests and delete the repro file:

**tool call: Bash**

```bash
cd /work/mui__material-ui-38544/repo; rm packages/mui-material/src/Tabs/repro.test.js; ../bin/envrun 'yarn cross-env NODE_ENV=test mocha "packages/mui-material/src/Tabs/**/*.test.js" "packages/mui-material/src/Tab/**/*.test.js" 2>&1 | tail -8'; git status --short
```

tool result:

```
  .............,,,..........,..,,..........,,,,,..,.,.....
  ...................................,..........,,,,,.....
  ......

  99 passing (2s)
  19 pending

Done in 7.18s.

 M package.json
 M packages/mui-material/src/Tabs/Tabs.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
```

**assistant:** I fixed the crash: scrollable `Tabs` no longer breaks when a theme style override reads `ownerState` from its props.

**Cause:** The hidden `TabsScrollbarSize` element that scrollable tabs render uses the same `MuiTabs` theme style overrides as the other Tabs parts. It was the only one rendered without an `ownerState` prop, so an override like `({ ownerState: { orientation } }) => ...` received `undefined` and crashed.

**Fix** (`packages/mui-material/src/Tabs/Tabs.js`): one line, passing `ownerState={ownerState}` to `<TabsScrollbarSize>`, as the other styled parts in this file already do. Material UI's `styled` doesn't forward `ownerState` to the underlying component, so it isn't passed through to the DOM `<div>` and React doesn't warn about an unknown prop.

**Checks:**
- **Reproduction:** I wrote a temporary test with a scrollable `Tabs` and a theme `root` override that destructures `ownerState.orientation`. Before the fix it failed with `TypeError: Cannot read properties of undefined (reading 'orientation')`. After the fix it passes with no console warnings, which the test harness would have reported as failures. I deleted the test afterwards.
- **Existing tests:** the `Tabs` and `Tab` suites pass (99 passing, 19 pending).

`git status` also lists changes to `package.json` and `yarn.lock`, plus new `Dockerfile` and `custom-reporter.js` files. I didn't make those changes and left them alone; they appear to come from the test environment setup.

_session end: success, turns 9, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 16.86 s: yarn cross-env NODE_ENV=test mocha packages/mui-material/src/Tabs/repro.test.js 2>&1 | tail -20
- `rc=0` 4.87 s: yarn cross-env NODE_ENV=test mocha packages/mui-material/src/Tabs/repro.test.js 2>&1 | grep -m3 Error
- `rc=0` 5.57 s: yarn cross-env NODE_ENV=test mocha packages/mui-material/src/Tabs/repro.test.js 2>&1 | tail -8
- `rc=0` 8.03 s: yarn cross-env NODE_ENV=test mocha "packages/mui-material/src/Tabs/**/*.test.js" "packages/mui-material/src/Tab/**/*.test.js" 2>&1 | tail -8
