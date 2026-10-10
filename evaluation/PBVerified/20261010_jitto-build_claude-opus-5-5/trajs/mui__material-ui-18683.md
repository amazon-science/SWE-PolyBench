# Instance: mui__material-ui-18683

- Final resolved (evaluator, logs/mui__material-ui-18683_result.json): True
- Run state: DONE
- One attempt. Duration 538.1 s, turns 17, actor cost $0.36211219999999994, container commands 6
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/mui__material-ui-18683/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-18683/repo. Consider the following issue description:

<issue_description>
[useMediaQuery] hydrationCompleted is true before hydrated
- [x] The issue is present in the latest release.
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Current Behavior 😯

The `hydrationCompleted` variable in `useMediaQuery()` can become `true` before all  components in the document are actually hydrated.

## Expected Behavior 🤔

`useMediaQuery()` should not have side-effects across components in a single document.

## Steps to Reproduce 🕹

https://codesandbox.io/s/sweet-wilbur-5t0l6

In this sandbox, please observe that `hydrationCompleted` is set to `true` after `ReactDOM.render()` (app 1) but before `ReactDOM.hydrate()` (app 2).

Unfortunately, I'm having trouble reproducing the visual bug in our app that caused us to take notice of this issue in the first place. I'll keep at it!

## Context 🔦

The impact on our app is ``Prop `className` did not match`` warnings and mismatches between CSS class names.

I'm able to work around the issue by:

* changing the load order so the SSR component is hydrated first
* manually resetting `hydrationCompleted` back to `false` after it's set to `true`
* forcing the app to re-render (by interacting with the app)

## Your Environment 🌎

| Tech        | Version |
| ----------- | ------- |
| Material-UI | v4.5.0  |
| React       | v16.8.6        |


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-18683/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-18683/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-18683/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-18683/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/mui__material-ui-18683/repo; ls packages/material-ui/src/useMediaQuery/; cat packages/material-ui/src/useMediaQuery/useMediaQuery.js; grep -rn "testReset\|hydrationCompleted" packages docs --include=*.js --include=*.ts --include=*.tsx --include=*.md | grep -v node_modules
```

tool result:

```
index.d.ts
index.js
useMediaQuery.d.ts
useMediaQuery.js
useMediaQuery.test.js
useMediaQueryTheme.d.ts
useMediaQueryTheme.js
import React from 'react';
import { getThemeProps, useTheme } from '@material-ui/styles';

// This variable will be true once the server-side hydration is completed.
let hydrationCompleted = false;

function useMediaQuery(queryInput, options = {}) {
  const theme = useTheme();
  const props = getThemeProps({
    theme,
    name: 'MuiUseMediaQuery',
    props: {},
  });

  if (process.env.NODE_ENV !== 'production') {
    if (typeof queryInput === 'function' && theme === null) {
      console.error(
        [
          'Material-UI: the `query` argument provided is invalid.',
          'You are providing a function without a theme in the context.',
          'One of the parent elements needs to use a ThemeProvider.',
        ].join('\n'),
      );
    }
  }

  let query = typeof queryInput === 'function' ? queryInput(theme) : queryInput;
  query = query.replace(/^@media( ?)/m, '');

  // Wait for jsdom to support the match media feature.
  // All the browsers Material-UI support have this built-in.
  // This defensive check is here for simplicity.
  // Most of the time, the match media logic isn't central to people tests.
  const supportMatchMedia =
    typeof window !== 'undefined' && typeof window.matchMedia !== 'undefined';

  const { defaultMatches = false, noSsr = false, ssrMatchMedia = null } = {
    ...props,
    ...options,
  };

  const [match, setMatch] = React.useState(() => {
    if ((hydrationCompleted || noSsr) && supportMatchMedia) {
      return window.matchMedia(query).matches;
    }
    if (ssrMatchMedia) {
      return ssrMatchMedia(query).matches;
    }

    // Once the component is mounted, we rely on the
    // event listeners to return the correct matches value.
    return defaultMatches;
  });

  React.useEffect(() => {
    let active = true;
    hydrationCompleted = true;

    if (!supportMatchMedia) {
      return undefined;
    }

    const queryList = window.matchMedia(query);
    const updateMatch = () => {
      // Workaround Safari wrong implementation of matchMedia
      // TODO can we remove it?
      // https://github.com/mui-org/material-ui/pull/17315#issuecomment-528286677
      if (active) {
        setMatch(queryList.matches);
      }
    };
    updateMatch();
    queryList.addListener(updateMatch);
    return () => {
      active = false;
      queryList.removeListener(updateMatch);
    };
  }, [query, supportMatchMedia]);

  return match;
}

export function testReset() {
  hydrationCompleted = false;
}

export default useMediaQuery;
(eval):1: no matches found: --include=*.js
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-18683/repo; grep -rn "testReset\|hydrationCompleted" packages docs | grep -v node_modules; sed -n 1,80p packages/material-ui/src/useMediaQuery/useMediaQuery.test.js
```

tool result:

```
packages/material-ui/src/Tooltip/Tooltip.test.js:10:import Tooltip, { testReset } from './Tooltip';
packages/material-ui/src/Tooltip/Tooltip.test.js:51:    testReset();
packages/material-ui/src/Tooltip/Tooltip.js:156:export function testReset() {
packages/material-ui/src/withWidth/withWidth.test.js:8:import { testReset } from '../useMediaQuery/useMediaQuery';
packages/material-ui/src/withWidth/withWidth.test.js:51:    testReset();
packages/material-ui/src/useMediaQuery/useMediaQuery.test.js:10:import useMediaQuery, { testReset } from './useMediaQuery';
packages/material-ui/src/useMediaQuery/useMediaQuery.test.js:48:    testReset();
packages/material-ui/src/useMediaQuery/useMediaQuery.js:5:let hydrationCompleted = false;
packages/material-ui/src/useMediaQuery/useMediaQuery.js:43:    if ((hydrationCompleted || noSsr) && supportMatchMedia) {
packages/material-ui/src/useMediaQuery/useMediaQuery.js:57:    hydrationCompleted = true;
packages/material-ui/src/useMediaQuery/useMediaQuery.js:83:export function testReset() {
packages/material-ui/src/useMediaQuery/useMediaQuery.js:84:  hydrationCompleted = false;
import React from 'react';
import PropTypes from 'prop-types';
import { ThemeProvider } from '@material-ui/styles';
import consoleErrorMock from 'test/utils/consoleErrorMock';
import { act, createClientRender } from 'test/utils/createClientRender';
import { createRender } from '@material-ui/core/test-utils';
import mediaQuery from 'css-mediaquery';
import { expect } from 'chai';
import { spy, stub } from 'sinon';
import useMediaQuery, { testReset } from './useMediaQuery';

function createMatchMedia(width, ref) {
  const listeners = [];
  return query => {
    const instance = {
      matches: mediaQuery.match(query, {
        width,
      }),
      addListener: listener => {
        listeners.push(listener);
      },
      removeListener: listener => {
        const index = listeners.indexOf(listener);
        if (index > -1) {
          listeners.splice(index, 1);
        }
      },
    };
    ref.push({
      instance,
      listeners,
    });
    return instance;
  };
}

describe('useMediaQuery', () => {
  // Only run the test on node.
  // Waiting for https://github.com/facebook/react/issues/14050
  if (!/jsdom/.test(window.navigator.userAgent)) {
    return;
  }

  const render = createClientRender({ strict: true });
  let values;

  beforeEach(() => {
    testReset();
    values = spy();
  });

  describe('without feature', () => {
    it('should work without window.matchMedia available', () => {
      expect(typeof window.matchMedia).to.equal('undefined');
      const ref = React.createRef();
      const text = () => ref.current.textContent;
      const Test = () => {
        const matches = useMediaQuery('(min-width:100px)');
        return <span ref={ref}>{`${matches}`}</span>;
      };

      render(<Test />);
      expect(text()).to.equal('false');
    });
  });

  describe('with feature', () => {
    let matchMediaInstances;

    beforeEach(() => {
      matchMediaInstances = [];
      const fakeMatchMedia = createMatchMedia(1200, matchMediaInstances);
      // can't stub non-existent properties with sinon
      // jsdom does not implement window.matchMedia
      if (window.matchMedia === undefined) {
        window.matchMedia = fakeMatchMedia;
        window.matchMedia.restore = () => {
          delete window.matchMedia;
        };
      } else {
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-18683/repo; sed -n 80,400p packages/material-ui/src/useMediaQuery/useMediaQuery.test.js | grep -n "it(\|describe\|hydrat\|ssr\|noSsr" 
```

tool result:

```
10:    describe('option: defaultMatches', () => {
11:      it('should be false by default', () => {
25:      it('should take the option into account', () => {
42:    describe('option: noSsr', () => {
43:      it('should render once if the default value match the expectation', () => {
59:      it('should render twice if the default value does not match the expectation', () => {
75:      it('should render once if the default value does not match the expectation', () => {
81:            noSsr: true,
93:    it('should try to reconcile only the first time', () => {
115:    it('should be able to change the query dynamically', () => {
137:    it('should observe the media query', () => {
162:  describe('server-side', () => {
169:    it('should use the ssr match media ponyfill', () => {
178:        const ssrMatchMedia = query => ({
185:          <ThemeProvider theme={{ props: { MuiUseMediaQuery: { ssrMatchMedia } } }}>
197:  describe('warnings', () => {
207:    it('warns on invalid `query` argument', () => {
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-18683/repo; sed -n 170,195p packages/material-ui/src/useMediaQuery/useMediaQuery.test.js
```

tool result:

```
    });

    it('should try to reconcile only the first time', () => {
      const ref = React.createRef();
      const text = () => ref.current.textContent;
      const Test = () => {
        const matches = useMediaQuery('(min-width:2000px)', {
          defaultMatches: true,
        });
        React.useEffect(() => values(matches));
        return <span ref={ref}>{`${matches}`}</span>;
      };

      const { unmount } = render(<Test />);
      expect(text()).to.equal('false');
      expect(values.callCount).to.equal(2);

      unmount();

      render(<Test />);
      expect(text()).to.equal('false');
      expect(values.callCount).to.equal(3);
    });

    it('should be able to change the query dynamically', () => {
      const ref = React.createRef();
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-18683/repo; git log --oneline -3; grep -n "version" packages/material-ui/package.json | head -2; grep -n "noSsr\|hydrat" -i docs/src/pages/components/use-media-query/use-media-query.md
```

tool result:

```
dfe2779b8 [docs] `ssrMatchMedia` required for client rending as well (#18680)
b14c7a4d4 [TablePagination] Fix responsive display issue (#18668)
b2c5e2d86 [Autocomplete] Prevent tag overflow (#18662)
3:  "version": "4.7.1",
147:Make sure you provide the same custom match media implementation to the client-side to guarantee a hydration match.
167:  - `options.noSsr` (*Boolean* [optional]): Defaults to `false`.
```

**thinking:**

```
That shared `hydrationCompleted` flag in useMediaQuery.js causes later hydrate() calls to read matchMedia on first render, mismatching server markup once another root has mounted. I'll reproduce this issue first.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-18683/repo; cat > packages/material-ui/src/useMediaQuery/repro.test.js <<'EOF'
import React from 'react';
import ReactDOM from 'react-dom';
import ReactDOMServer from 'react-dom/server';
import { act } from 'react-dom/test-utils';
import { expect } from 'chai';
import useMediaQuery from './useMediaQuery';

describe('repro: multiple roots', () => {
  it('second root hydrates with defaultMatches', () => {
    window.matchMedia = () => ({ matches: true, addListener() {}, removeListener() {} });
    const firstRenders = [];
    const Test = () => {
      const m = useMediaQuery('(min-width:100px)');
      firstRenders.push(m);
      return <span>{`${m}`}</span>;
    };
    const a = document.createElement('div');
    act(() => { ReactDOM.render(<Test />, a); });
    const b = document.createElement('div');
    b.innerHTML = ReactDOMServer.renderToString(<Test />);
    firstRenders.length = 0;
    act(() => { ReactDOM.hydrate(<Test />, b); });
    delete window.matchMedia;
    expect(firstRenders[0]).to.equal(false);
  });
});
EOF
../bin/envrun 'yarn -s cross-env NODE_ENV=test mocha packages/material-ui/src/useMediaQuery/repro.test.js 2>&1 | tail -20'
```

tool result:

```
Command did not complete within its 120s timeout and was moved to the background (ID: btfqzwjtn). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/219da450-dab8-4f58-ad12-8228be764979/tasks/btfqzwjtn.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /work/mui__material-ui-18683/repo; directory changes made by the backgrounded command do not apply to subsequent commands.
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-18683/repo; cat .mocharc.js 2>/dev/null; grep -n '"test' package.json
```

tool result:

```
34:    "test": "yarn lint && yarn typescript && yarn test:coverage",
35:    "test:coverage": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha 'packages/**/*.test.js' 'docs/**/*.test.js' --exclude '**/node_modules/**' && nyc report -r lcovonly",
36:    "test:coverage:html": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha 'packages/**/**/*.test.js' --exclude '**/node_modules/**' && nyc report --reporter=html",
37:    "test:karma": "cross-env NODE_ENV=test karma start test/karma.conf.js",
38:    "test:regressions": "webpack --config test/regressions/webpack.config.js && rimraf test/regressions/screenshots/chrome/* && vrtest run --config test/vrtest.config.js --record",
39:    "test:umd": "node packages/material-ui/test/umd/run.js",
40:    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/*.test.js' 'docs/**/*.test.js' --exclude '**/node_modules/**'",
41:    "test:watch": "yarn test:unit --watch",
```

**assistant:** Probably just slow startup (babel register); I'll wait for it.

**tool call: Bash**

```bash
sleep 90; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/219da450-dab8-4f58-ad12-8228be764979/tasks/btfqzwjtn.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
sleep 120; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/219da450-dab8-4f58-ad12-8228be764979/tasks/btfqzwjtn.output
```

tool result:

```
Exit code 143
Command timed out after 2m 0s
```

**tool call: Bash**

```bash
sleep 30; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/219da450-dab8-4f58-ad12-8228be764979/tasks/btfqzwjtn.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
sleep 100; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/219da450-dab8-4f58-ad12-8228be764979/tasks/btfqzwjtn.output; /work/mui__material-ui-18683/bin/envrun 'ps aux | grep -c mocha'
```

tool result:

```
7
```

**tool call: Bash**

```bash
/work/mui__material-ui-18683/bin/envrun 'ps aux | grep mocha | grep -v grep | cut -c1-250'
```

tool result:

```
root         7  0.0  0.0 289612  6288 ?        Ss   11:03   0:00 bash -lc yarn -s cross-env NODE_ENV=test mocha packages/material-ui/src/useMediaQuery/repro.test.js 2>&1 | tail -20
root        15  0.1  1.1 1151516 92588 ?       Sl   11:03   0:00 node --no-opt -r /proc/.reset /usr/local/nvm/versions/node/v16.20.2/bin/yarn -s cross-env NODE_ENV=test mocha packages/material-ui/src/useMediaQuery/repro.test.js
root        27  0.0  0.0 287852  3340 ?        S    11:03   0:00 /bin/sh -c /testbed/node_modules/.bin/cross-env NODE_ENV=test mocha packages/material-ui/src/useMediaQuery/repro.test.js
root        28  0.0  0.6 815028 50872 ?        Sl   11:03   0:00 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/.bin/cross-env NODE_ENV=test mocha packages/material-ui/src/useMediaQuery/repro.test.js
root        35  0.6  1.9 973228 156520 ?       Sl   11:03   0:02 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/.bin/mocha packages/material-ui/src/useMediaQuery/repro.test.js
```

**assistant:** The process is idle (2s of CPU), so mocha is likely waiting on an open handle and not exiting. I'll kill it and rerun with `--exit`.

**tool call: Bash**

```bash
cd /work/mui__material-ui-18683/repo; ../bin/envrun 'pkill -f mocha; cat .mocharc* 2>/dev/null; timeout 100 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui/src/useMediaQuery/repro.test.js 2>&1 | tail -20'
```

tool result:

```
Exit code 143
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-18683/repo; ls -a | grep -i mocha; ../bin/envrun 'timeout 100 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui/src/useMediaQuery/repro.test.js 2>&1 | tail -20'
```

tool result:

```
  !

  0 passing (49ms)
  1 failing

  1) repro: multiple roots
       second root hydrates with defaultMatches:

      AssertionError: expected true to equal false
      + expected - actual

      -true
      +false
      
      at Context.<anonymous> (packages/material-ui/src/useMediaQuery/repro.test.js:24:32)
      at processImmediate (node:internal/timers:466:21)
```

**thinking:**

```
I've confirmed the bug: a second root's `hydrate()` picks up the real `matchMedia` result instead of `defaultMatches` on first render. Now I'll fix it by removing the module-level flag so skipping reconciliation only happens when `noSsr` is explicitly set.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-18683/repo; python3 - <<'EOF'
p='packages/material-ui/src/useMediaQuery/useMediaQuery.js'
s=open(p).read()
s=s.replace("""// This variable will be true once the server-side hydration is completed.
let hydrationCompleted = false;

""","")
s=s.replace("if ((hydrationCompleted || noSsr) && supportMatchMedia)","if (noSsr && supportMatchMedia)")
s=s.replace("""    let active = true;
    hydrationCompleted = true;
""","""    let active = true;
""")
s=s.replace("""export function testReset() {
  hydrationCompleted = false;
}
""","""// Kept for backward compatibility of the test utilities, there is no module state to reset anymore.
export function testReset() {}
""")
open(p,'w').write(s)
EOF
git diff; ../bin/envrun 'timeout 200 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui/src/useMediaQuery/*.test.js packages/material-ui/src/withWidth/*.test.js packages/material-ui/src/Hidden/*.test.js 2>&1 | tail -40'
```

tool result:

```
diff --git a/package.json b/package.json
index f33926ca9..9fa089604 100644
--- a/package.json
+++ b/package.json
@@ -54,17 +54,20 @@
     "@babel/register": "^7.7.4",
     "@testing-library/dom": "^6.8.1",
     "@testing-library/react": "^9.3.2",
-    "@types/chai": "^4.2.3",
-    "@types/chai-dom": "^0.0.8",
+    "@types/chai": "^5.2.2",
+    "@types/chai-dom": "^1.11.3",
     "@types/enzyme": "^3.10.3",
+    "@types/format-util": "^1.0.4",
     "@types/fs-extra": "^8.0.0",
     "@types/glob": "^7.1.1",
     "@types/jsdom": "^12.2.4",
     "@types/lodash": "^4.14.138",
     "@types/mocha": "^5.2.7",
     "@types/prettier": "^1.18.0",
+    "@types/prop-types": "^15.7.15",
     "@types/react": "^16.9.3",
-    "@types/sinon": "^7.0.13",
+    "@types/react-dom": "^19.1.8",
+    "@types/sinon": "^17.0.4",
     "argos-cli": "^0.1.2",
     "babel-core": "^7.0.0-bridge.0",
     "babel-eslint": "^10.0.3",
diff --git a/packages/material-ui/src/useMediaQuery/useMediaQuery.js b/packages/material-ui/src/useMediaQuery/useMediaQuery.js
index e969caa2f..ef920cbde 100644
--- a/packages/material-ui/src/useMediaQuery/useMediaQuery.js
+++ b/packages/material-ui/src/useMediaQuery/useMediaQuery.js
@@ -1,9 +1,6 @@
 import React from 'react';
 import { getThemeProps, useTheme } from '@material-ui/styles';
 
-// This variable will be true once the server-side hydration is completed.
-let hydrationCompleted = false;
-
 function useMediaQuery(queryInput, options = {}) {
   const theme = useTheme();
   const props = getThemeProps({
@@ -40,7 +37,7 @@ function useMediaQuery(queryInput, options = {}) {
   };
 
   const [match, setMatch] = React.useState(() => {
-    if ((hydrationCompleted || noSsr) && supportMatchMedia) {
+    if (noSsr && supportMatchMedia) {
       return window.matchMedia(query).matches;
     }
     if (ssrMatchMedia) {
@@ -54,7 +51,6 @@ function useMediaQuery(queryInput, options = {}) {
 
   React.useEffect(() => {
     let active = true;
-    hydrationCompleted = true;
 
     if (!supportMatchMedia) {
       return undefined;
@@ -80,8 +76,7 @@ function useMediaQuery(queryInput, options = {}) {
   return match;
 }
 
-export function testReset() {
-  hydrationCompleted = false;
-}
+// Kept for backward compatibility of the test utilities, there is no module state to reset anymore.
+export function testReset() {}
 
 export default useMediaQuery;
diff --git a/yarn.lock b/yarn.lock
index 9622c3d0d..e2cbb6d38 100644
--- a/yarn.lock
+++ b/yarn.lock
@@ -2009,18 +2009,25 @@
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
   version "4.2.5"
   resolved "https://registry.yarnpkg.com/@types/chai/-/chai-4.2.5.tgz#f8da153ebbe30babb0adc9a528b9ad32be3175a2"
   integrity sha512-YvbLiIc0DbbhiANrfVObdkLEHJksQZVq0Uvfg550SRAKVYaEJy+V70j65BVe2WNp6E3HtKsUczeijHFCjba3og==
 
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
@@ -2038,6 +2045,11 @@
   resolved "https://registry.yarnpkg.com/@types/css-mediaquery/-/css-mediaquery-0.1.0.tgz#61d439d8163880e90b61d19aba24f7b778c4e77d"
   integrity sha512-jzZ9bRw8fTgCEllDvE7GHR1zTP5LsDHJbAX6BCwD9qdxIOq/Le5TTsdteoCIdEQaFpDMvudLHU/hLo1Lmfcy0Q==
 
+"@types/deep-eql@*":
+  version "4.0.2"
+  resolved "https://registry.yarnpkg.com/@types/deep-eql/-/deep-eql-4.0.2.tgz#334311971d3a07121e7eb91b684a605e7eea9cbd"
+  integrity sha512-c9h9dVVMigMPc4bwTvC5dxqtqJZwQPePsWjPlpSOnojbor6pGqdk541lfA7AqFQr5pB1BRdq0juY9db81BwyFw==
+
 "@types/enzyme@^3.10.3":
   version "3.10.3"
   resolved "https://registry.yarnpkg.com/@types/enzyme/-/enzyme-3.10.3.tgz#02b6c5ac7d0472005944a652e79045e2f6c66804"
@@ -2056,6 +2068,11 @@
   resolved "https://registry.yarnpkg.com/@types/events/-/events-3.0.0.tgz#2862f3f58a9a7f7c3e78d79f130dd4d71c25c2a7"
   integrity sha512-EaObqwIvayI5a8dCzhFrjKzVwKLxjoG9T6Ppd5CEo07LRKfQ8Yokw54r5+Wq7FaBQ+yXRvQAYPrHwya1/UFt9g==
 
+"@types/format-util@^1.0.4":
+  version "1.0.4"
+  resolved "https://registry.yarnpkg.com/@types/format-util/-/format-util-1.0.4.tgz#c4e3b556735149fdf047898a5b9c04650491509b"
+  integrity sha512-xrCYOdHh5zA3LUrn6CvspYwlzSWxPso11Lx32WnAG6KvLCRecKZ/Rh21PLXUkzUFsQmrGcx/traJAFjR6dVS5Q==
+
 "@types/fs-extra@^8.0.0":
   version "8.0.1"
   resolved "https://registry.yarnpkg.com/@types/fs-extra/-/fs-extra-8.0.1.tgz#a2378d6e7e8afea1564e44aafa2e207dadf77686"
@@ -2151,6 +2168,11 @@
   resolved "https://registry.yarnpkg.com/@types/prop-types/-/prop-types-15.7.1.tgz#f1a11e7babb0c3cad68100be381d1e064c68f1f6"
   integrity sha512-CFzn9idOEpHrgdw8JsoTkaDDyRWk1jrzIV8djzcgpq0y9tG4B4lFT+Nxh52DVpDXV+n4+NPNv7M1Dj5uMp6XFg==
 
+"@types/prop-types@^15.7.15":
+  version "15.7.15"
+  resolved "https://registry.yarnpkg.com/@types/prop-types/-/prop-types-15.7.15.tgz#e6e5a86d602beaca71ce5163fadf5f95d70931c7"
+  integrity sha512-
[... 2427 more characters not shown]
```

**thinking:**

```
My fix passes the repro and 123 of 124 tests; the one failure asserts the old cross-component side effect that this fix intentionally removes. I'll check the docs for that behavior next, then clean up.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-18683/repo; rm packages/material-ui/src/useMediaQuery/repro.test.js; grep -n -i "first time\|reconcil\|twice\|hydrat" docs/src/pages/components/use-media-query/use-media-query.md; git status --short
```

tool result:

```
147:Make sure you provide the same custom match media implementation to the client-side to guarantee a hydration match.
168:  In order to perform the server-side rendering reconciliation, it needs to render twice.
169:  A first time with nothing and a second time with the children.
 M package.json
 M packages/material-ui/src/useMediaQuery/useMediaQuery.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
```

**assistant:** I fixed the bug in `packages/material-ui/src/useMediaQuery/useMediaQuery.js`. One existing test now fails because it checks for the old behaviour.

**Cause:** a single `hydrationCompleted` flag was shared by the whole module. As soon as any `useMediaQuery` component mounted (for example in an app started with `ReactDOM.render()`), every later component skipped the server-rendering step and read `window.matchMedia` on its first render. That included components inside a separate root that was still being hydrated with `ReactDOM.hydrate()`. That's what caused the `className` mismatch warnings in the issue.

**Fix:** I removed the shared flag. Each component now reads `matchMedia` on its first render only when `noSsr: true` is set. Otherwise it starts with `ssrMatchMedia` or `defaultMatches` and then updates in its effect. That matches the documented "renders twice" behaviour for `noSsr: false`. `testReset()` is kept as an empty function because `useMediaQuery.test.js` and `withWidth.test.js` still import and call it.

**Checks:**
- **Reproduction:** I wrote a test that does `ReactDOM.render()` into one root, then `ReactDOM.hydrate()` into a second, server-rendered root. Before the fix, the hydrating component's first render returned `true` (from `matchMedia`) instead of the server's `false`. After the fix it returns `false`. I deleted the script afterwards.
- **Tests:** the `useMediaQuery`, `withWidth` and `Hidden` tests: 123 pass, 1 fails.

**The failing test:** `useMediaQuery › should try to reconcile only the first time` expects 3 renders and now gets 4. It unmounts a component, mounts a new one, and expects the new one to skip the server-rendering step because an earlier component had already mounted. That is the cross-component side effect the issue asks to remove, so the failure is expected. You'll need to update that test to expect 4 renders, or remove it; I didn't change it because you asked me to leave the tests alone.

`package.json`, `yarn.lock`, `Dockerfile` and `custom-reporter.js` show changes that I didn't make; they look like environment setup, so I left them as they were.

_session end: success, turns 17, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.12 s: ps aux | grep -c mocha
- `rc=0` 0.15 s: ps aux | grep mocha | grep -v grep | cut -c1-250
- `rc=143` 477.52 s: yarn -s cross-env NODE_ENV=test mocha packages/material-ui/src/useMediaQuery/repro.test.js 2>&1 | tail -20
- `rc=143` 0.16 s: pkill -f mocha; cat .mocharc* 2>/dev/null; timeout 100 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui/src/useMediaQuery/repro.test.js 2>&1 | tail -20
- `rc=0` 1.73 s: timeout 100 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui/src/useMediaQuery/repro.test.js 2>&1 | tail -20
- `rc=0` 3.6 s: timeout 200 node_modules/.bin/cross-env NODE_ENV=test node_modules/.bin/mocha --exit packages/material-ui/src/useMediaQuery/*.test.js packages/material-ui/src/withWidth/*.test.js packages/material-ui/src/Hidden/*.test.js 2>&1 | tail -40
