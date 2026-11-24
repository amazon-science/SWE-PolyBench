# Instance: mui__material-ui-18824

- Final resolved (evaluator, logs/mui__material-ui-18824_result.json): True
- Run state: DONE
- One attempt. Duration 645.8 s, turns 18, actor cost $0.3160374000000001, container commands 8
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/mui__material-ui-18824/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-18824/repo. Consider the following issue description:

<issue_description>
[Paper] Support outlined Card / Paper
The Material spec states that cards on the desktop have 0dp elevation, and should be outlined instead of being delimited using their shadow. I think this variant should be supported.

This [has been mentioned in an unrelated issue](https://github.com/mui-org/material-ui/pull/15243#issuecomment-480784851), but seems to not have been brought back up.

<!--
    Thank you very much for contributing to Material-UI by creating an issue! ❤️
    To avoid duplicate issues we ask you to check off the following list.
-->

<!-- Checked checkbox should look like this: [x] -->
- [x] This is not a v0.x issue. <!-- (v0.x is no longer maintained) -->
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Expected Behavior 🤔
There should be a way to get an outlined `Card` or `Paper` with 0dp elevation.
This could either take the form of `<Card variant="outlined">` (issues - should this automatically set elevation to 0? Should it work with elevation not 0?) or by automatically adopting the style when `<Card elevation={0}>` is used (issues - does this mean you cannot have a no-outline no-shadow `Card`?)

I'm not sure whether determining in some global fashion whether we are on "desktop" or not is feasible and whether it should change the default elevation of the card - my instinct is that it should not.

## Current Behavior 😯
Currently a `Card` or `Paper` with no elevation is flat with no outline or shadow and there is no outlined variant.

## Examples 🌈
[Material spec](https://material.io/design/environment/elevation.html) states under the "Resting elevation and environment" heading that
>The resting elevations on mobile are designed to provide visual cues, like shadows, to indicate when components are interactive. In contrast, resting elevations on desktop are shallower because other cues, like hover states, communicate when a component is interactive. For example, **cards at 0dp elevation on desktop are outlined with a stroke.**

and the second image in that section illustrates this.

The [styles implemented in material-components-web](https://github.com/material-components/material-components-web/blob/9f37016490b37deaf87a23b9dc813f5233610635/packages/mdc-card/_mixins.scss#L294) could be an inspiration for this, but it basically boils down to applying a border correctly and making sure this does not impact spacing (e.g. in the Material docs example, the outline seamlessly merges into the media block at the top of the card).

## Context 🔦
I am writing a desktop-only web app using a dense Material design and when there are lots of components on the screen, a flat outlined style is easier to look at and use.


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-18824/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-18824/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-18824/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-18824/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/mui__material-ui-18824/repo/packages/material-ui/src/Paper && ls && cat Paper.js Paper.d.ts && grep -n "outlined\|variant" Paper.test.js
```

tool result:

```
Paper.d.ts
Paper.js
Paper.test.js
index.d.ts
index.js
import React from 'react';
import PropTypes from 'prop-types';
import clsx from 'clsx';
import withStyles from '../styles/withStyles';

export const styles = theme => {
  const elevations = {};
  theme.shadows.forEach((shadow, index) => {
    elevations[`elevation${index}`] = {
      boxShadow: shadow,
    };
  });

  return {
    /* Styles applied to the root element. */
    root: {
      backgroundColor: theme.palette.background.paper,
      color: theme.palette.text.primary,
      transition: theme.transitions.create('box-shadow'),
    },
    /* Styles applied to the root element if `square={false}`. */
    rounded: {
      borderRadius: theme.shape.borderRadius,
    },
    ...elevations,
  };
};

const Paper = React.forwardRef(function Paper(props, ref) {
  const {
    classes,
    className,
    component: Component = 'div',
    square = false,
    elevation = 1,
    ...other
  } = props;

  if (process.env.NODE_ENV !== 'production') {
    if (classes[`elevation${elevation}`] === undefined) {
      console.error(`Material-UI: this elevation \`${elevation}\` is not implemented.`);
    }
  }

  return (
    <Component
      className={clsx(
        classes.root,
        classes[`elevation${elevation}`],
        {
          [classes.rounded]: !square,
        },
        className,
      )}
      ref={ref}
      {...other}
    />
  );
});

Paper.propTypes = {
  /**
   * The content of the component.
   */
  children: PropTypes.node,
  /**
   * Override or extend the styles applied to the component.
   * See [CSS API](#css) below for more details.
   */
  classes: PropTypes.object.isRequired,
  /**
   * @ignore
   */
  className: PropTypes.string,
  /**
   * The component used for the root node.
   * Either a string to use a DOM element or a component.
   */
  component: PropTypes.elementType,
  /**
   * Shadow depth, corresponds to `dp` in the spec.
   * It accepts values between 0 and 24 inclusive.
   */
  elevation: PropTypes.number,
  /**
   * If `true`, rounded corners are disabled.
   */
  square: PropTypes.bool,
};

export default withStyles(styles, { name: 'MuiPaper' })(Paper);
import * as React from 'react';
import { StandardProps } from '..';

export interface PaperProps
  extends StandardProps<React.HTMLAttributes<HTMLDivElement>, PaperClassKey> {
  component?: React.ElementType<React.HTMLAttributes<HTMLElement>>;
  elevation?: number;
  square?: boolean;
}

export type PaperClassKey =
  | 'root'
  | 'rounded'
  | 'elevation0'
  | 'elevation1'
  | 'elevation2'
  | 'elevation3'
  | 'elevation4'
  | 'elevation5'
  | 'elevation6'
  | 'elevation7'
  | 'elevation8'
  | 'elevation9'
  | 'elevation10'
  | 'elevation11'
  | 'elevation12'
  | 'elevation13'
  | 'elevation14'
  | 'elevation15'
  | 'elevation16'
  | 'elevation17'
  | 'elevation18'
  | 'elevation19'
  | 'elevation20'
  | 'elevation21'
  | 'elevation22'
  | 'elevation23'
  | 'elevation24';

declare const Paper: React.ComponentType<PaperProps>;

export default Paper;
```

**tool call: Bash**

```bash
cat packages/material-ui/src/Card/Card.js | head -40; cat packages/material-ui/src/Paper/Paper.test.js | head -60; ls docs/pages/api/paper.md docs/src/pages/components/paper/
```

tool result:

```
import React from 'react';
import PropTypes from 'prop-types';
import clsx from 'clsx';
import Paper from '../Paper';
import withStyles from '../styles/withStyles';

export const styles = {
  /* Styles applied to the root element. */
  root: {
    overflow: 'hidden',
  },
};

const Card = React.forwardRef(function Card(props, ref) {
  const { classes, className, raised = false, ...other } = props;

  return (
    <Paper
      className={clsx(classes.root, className)}
      elevation={raised ? 8 : 1}
      ref={ref}
      {...other}
    />
  );
});

Card.propTypes = {
  /**
   * The content of the component.
   */
  children: PropTypes.node,
  /**
   * Override or extend the styles applied to the component.
   * See [CSS API](#css) below for more details.
   */
  classes: PropTypes.object.isRequired,
  /**
   * @ignore
   */
  className: PropTypes.string,
import React from 'react';
import { assert } from 'chai';
import { createMount, createShallow, getClasses } from '@material-ui/core/test-utils';
import describeConformance from '../test-utils/describeConformance';
import Paper from './Paper';
import { createMuiTheme, ThemeProvider } from '../styles';
import consoleErrorMock from 'test/utils/consoleErrorMock';

describe('<Paper />', () => {
  let mount;
  let shallow;
  let classes;

  beforeEach(() => {
    consoleErrorMock.spy();
  });

  afterEach(() => {
    consoleErrorMock.reset();
  });

  before(() => {
    mount = createMount({ strict: true });
    shallow = createShallow({ dive: true });
    classes = getClasses(<Paper />);
  });

  after(() => {
    mount.cleanUp();
  });

  describeConformance(<Paper />, () => ({
    classes,
    inheritComponent: 'div',
    mount,
    refInstanceof: window.HTMLDivElement,
    testComponentPropWith: 'header',
  }));

  describe('prop: square', () => {
    it('can disable the rounded class', () => {
      const wrapper = mount(<Paper square>Hello World</Paper>);
      assert.strictEqual(wrapper.find(`.${classes.root}`).some(`.${classes.rounded}`), false);
    });

    it('adds a rounded class to the root when omitted', () => {
      const wrapper = mount(<Paper>Hello World</Paper>);
      assert.strictEqual(wrapper.find(`.${classes.root}`).every(`.${classes.rounded}`), true);
    });
  });

  it('should set the elevation elevation class', () => {
    const wrapper = shallow(<Paper elevation={16}>Hello World</Paper>);
    assert.strictEqual(
      wrapper.hasClass(classes.elevation16),
      true,
      'should have the 16 elevation class',
    );
    wrapper.setProps({ elevation: 24 });
    assert.strictEqual(
docs/pages/api/paper.md

docs/src/pages/components/paper/:
PaperSheet.js
PaperSheet.tsx
paper-aa.md
paper-de.md
paper-es.md
paper-fr.md
paper-ja.md
paper-pt.md
paper-ru.md
paper-zh.md
paper.md
```

**assistant:** Now implement the `variant` prop on Paper.

**tool call: Bash**

```bash
cd packages/material-ui/src/Paper && python3 - <<'EOF'
p='Paper.js'
s=open(p).read()
s=s.replace("""      borderRadius: theme.shape.borderRadius,
    },
""","""      borderRadius: theme.shape.borderRadius,
    },
    /* Styles applied to the root element if `variant="outlined"` */
    outlined: {
      border: `1px solid ${theme.palette.divider}`,
    },
""")
s=s.replace("""    elevation = 1,
    ...other""","""    elevation = 1,
    variant = 'elevation',
    ...other""")
s=s.replace("""        classes.root,
        classes[`elevation${elevation}`],
        {
          [classes.rounded]: !square,
        },""","""        classes.root,
        {
          [classes.rounded]: !square,
          [classes[`elevation${elevation}`]]: variant === 'elevation',
          [classes.outlined]: variant === 'outlined',
        },""")
s=s.replace("""  square: PropTypes.bool,
};""","""  square: PropTypes.bool,
  /**
   * The variant to use.
   */
  variant: PropTypes.oneOf(['elevation', 'outlined']),
};""")
open(p,'w').write(s)
p='Paper.d.ts'
s=open(p).read()
s=s.replace("""  square?: boolean;
}""","""  square?: boolean;
  variant?: 'elevation' | 'outlined';
}""")
s=s.replace("""  | 'rounded'
""","""  | 'rounded'
  | 'outlined'
""")
open(p,'w').write(s)
EOF
git diff --stat
```

tool result:

```
 package.json                              |  9 ++++--
 packages/material-ui/src/Paper/Paper.d.ts |  2 ++
 packages/material-ui/src/Paper/Paper.js   | 12 ++++++-
 yarn.lock                                 | 52 +++++++++++++++++++++++++------
 4 files changed, 62 insertions(+), 13 deletions(-)
```

**tool call: Bash**

```bash
cd ../../../.. && git diff package.json
```

tool result:

```
diff --git a/package.json b/package.json
index 24a8a61b7..72f93ffa1 100644
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
```

**assistant:** The `package.json`/`yarn.lock` changes predate my edits (environment setup), so I'll leave them alone. Now a quick check plus the existing tests:

**tool call: Bash**

```bash
cat > packages/material-ui/src/Paper/Tmp.test.js <<'EOF'
import React from 'react';
import { expect } from 'chai';
import { createClientRender } from 'test/utils/createClientRender';
import { getClasses } from '@material-ui/core/test-utils';
import Paper from './Paper';
import Card from '../Card';

describe('tmp variant', () => {
  const render = createClientRender({ strict: true });
  const classes = getClasses(<Paper />);
  it('outlined', () => {
    const { container } = render(<Paper variant="outlined">x</Paper>);
    expect(container.firstChild).to.have.class(classes.outlined);
    expect(container.firstChild).not.to.have.class(classes.elevation1);
  });
  it('default', () => {
    const { container } = render(<Card>x</Card>);
    expect(container.firstChild).to.have.class(classes.elevation1);
    expect(container.firstChild).not.to.have.class(classes.outlined);
  });
  it('card outlined', () => {
    const { container } = render(<Card variant="outlined">x</Card>);
    expect(container.firstChild).to.have.class(classes.outlined);
  });
});
EOF
ls test/utils/ | head -30
../bin/envrun 'yarn -s mocha packages/material-ui/src/Paper/*.test.js packages/material-ui/src/Card/*.test.js 2>&1 | tail -30'
```

tool result:

```
consoleError.js
consoleErrorMock.js
consoleErrorMock.test.js
createClientRender.js
createDOM.d.ts
createDOM.js
createServerRender.js
init.d.ts
init.js
initMatchers.js
setup.js
    at Function.Module._load (node:internal/modules/cjs/loader:911:12)
    at Module.require (node:internal/modules/cjs/loader:1100:19)
    at require (node:internal/modules/cjs/helpers:119:18)
    at /testbed/node_modules/mocha/lib/mocha.js:334:36
    at Array.forEach (<anonymous>)
    at Mocha.loadFiles (/testbed/node_modules/mocha/lib/mocha.js:331:14)
    at Mocha.run (/testbed/node_modules/mocha/lib/mocha.js:809:10)
    at Object.exports.singleRun (/testbed/node_modules/mocha/lib/cli/run-helpers.js:108:16)
    at exports.runMocha (/testbed/node_modules/mocha/lib/cli/run-helpers.js:142:13)
    at Object.exports.handler (/testbed/node_modules/mocha/lib/cli/run.js:292:3)
    at Object.runCommand (/testbed/node_modules/yargs/lib/command.js:242:26)
    at Object.parseArgs [as _parseArgs] (/testbed/node_modules/yargs/yargs.js:1087:28)
    at Object.parse (/testbed/node_modules/yargs/yargs.js:566:25)
    at Object.exports.main (/testbed/node_modules/mocha/lib/cli/cli.js:68:6)
    at Object.<anonymous> (/testbed/node_modules/mocha/bin/mocha:164:29)
    at Module._compile (node:internal/modules/cjs/loader:1198:14)
    at Object.Module._extensions..js (node:internal/modules/cjs/loader:1252:10)
    at Module.load (node:internal/modules/cjs/loader:1076:32)
    at Function.Module._load (node:internal/modules/cjs/loader:911:12)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:81:12)
    at node:internal/main/run_main_module:22:47 {
  code: 'MODULE_NOT_FOUND',
  requireStack: [
    '/testbed/packages/material-ui/src/Paper/Paper.test.js',
    '/testbed/node_modules/mocha/lib/mocha.js',
    '/testbed/node_modules/mocha/lib/cli/one-and-dones.js',
    '/testbed/node_modules/mocha/lib/cli/options.js',
    '/testbed/node_modules/mocha/bin/mocha'
  ]
}
```

**tool call: Bash**

```bash
grep -n '"test' package.json; cat .mocharc* 2>/dev/null; ../bin/envrun 'yarn -s mocha packages/material-ui/src/Paper/*.test.js packages/material-ui/src/Card/*.test.js 2>&1 | grep -m3 -i "cannot find"'
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
(eval):1: no matches found: .mocharc*
Error: Cannot find module '@material-ui/core/test-utils'
```

**assistant:** Needs `NODE_ENV=test` for babel module aliasing.

**tool call: Bash**

```bash
../bin/envrun 'NODE_ENV=test yarn -s mocha packages/material-ui/src/Paper/*.test.js packages/material-ui/src/Card/*.test.js 2>&1 | tail -30'
```

tool result:

```
Command did not complete within its 120s timeout and was moved to the background (ID: bkkp3nu4g). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/616bb66b-14bd-433c-a4cc-b26ec19922f4/tasks/bkkp3nu4g.output. You will be notified when it completes. To check interim output, use Read on that file path.
```

**tool call: Bash**

```bash
sleep 90; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/616bb66b-14bd-433c-a4cc-b26ec19922f4/tasks/bkkp3nu4g.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
sleep 120; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/616bb66b-14bd-433c-a4cc-b26ec19922f4/tasks/bkkp3nu4g.output
```

tool result:

```
Exit code 143
Command timed out after 2m 0s
```

**tool call: Bash**

```bash
cat /tmp/cell-scratch/claude-502/<actor-session-slug>/616bb66b-14bd-433c-a4cc-b26ec19922f4/tasks/bkkp3nu4g.output; ls test/; cat test/mocha.opts 2>/dev/null
```

tool result:

```
README.md
docs-regressions-before.png
docs-regressions-diff.png
karma.conf.js
karma.tests.js
mocha.opts
regressions
utils
vrtest.config.js
--require @babel/register
--reporter dot
--recursive
--require test/utils/setup.js
```

**assistant:** Likely just slow babel compilation on first run; waiting for the background job.

**tool call: Bash**

```bash
sleep 240; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/616bb66b-14bd-433c-a4cc-b26ec19922f4/tasks/bkkp3nu4g.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
../bin/envrun 'ps aux | grep -c mocha; ps aux | grep mocha | head -3'
```

tool result:

```
6
root        63  0.0  0.0 289612  6288 ?        Ss   10:59   0:00 bash -lc NODE_ENV=test yarn -s mocha packages/material-ui/src/Paper/*.test.js packages/material-ui/src/Card/*.test.js 2>&1 | tail -30
root        71  0.1  0.9 1138788 79480 ?       Sl   10:59   0:00 node --no-opt -r /proc/.reset /usr/local/nvm/versions/node/v16.20.2/bin/yarn -s mocha packages/material-ui/src/Paper/Paper.test.js packages/material-ui/src/Paper/Tmp.test.js packages/material-ui/src/Card/Card.test.js
root        83  0.0  0.0 287852  3336 ?        S    10:59   0:00 /bin/sh -c /testbed/node_modules/.bin/mocha packages/material-ui/src/Paper/Paper.test.js packages/material-ui/src/Paper/Tmp.test.js packages/material-ui/src/Card/Card.test.js
```

**assistant:** The run seems to be hanging after the tests finish (mocha without `--exit`), and piping through `tail` hides the output. I'll kill it and rerun with `--exit`.

**tool call: Bash**

```bash
../bin/envrun 'pkill -f mocha; NODE_ENV=test timeout 250 node_modules/.bin/mocha --exit packages/material-ui/src/Paper/*.test.js packages/material-ui/src/Card/*.test.js 2>&1 | tail -30'
```

tool result:

```
Exit code 143
```

**assistant:** `pkill -f mocha` matched its own shell command and killed it. Rerunning without that:

**tool call: Bash**

```bash
../bin/envrun 'NODE_ENV=test timeout 280 node_modules/.bin/mocha --exit packages/material-ui/src/Paper/*.test.js packages/material-ui/src/Card/*.test.js > /tmp/out.txt 2>&1; echo rc=$?; tail -40 /tmp/out.txt'
```

tool result:

```
rc=0
Browserslist: caniuse-lite is outdated. Please run next command `yarn upgrade`
including inaccessible elements by default


  ․․․․․․․․․․․․․․․․․․․․

  20 passing (254ms)
```

**assistant:** All 20 pass, including my three temporary variant checks. Next I'll update the generated API doc and run the TypeScript check, then delete the temp test.

**tool call: Bash**

```bash
rm packages/material-ui/src/Paper/Tmp.test.js; grep -n "square\|rounded\|elevation" docs/pages/api/paper.md docs/pages/api/card.md
```

tool result:

```
docs/pages/api/paper.md:30:| <span class="prop-name">elevation</span> | <span class="prop-type">number</span> | <span class="prop-default">1</span> | Shadow depth, corresponds to `dp` in the spec. It accepts values between 0 and 24 inclusive. |
docs/pages/api/paper.md:31:| <span class="prop-name">square</span> | <span class="prop-type">bool</span> | <span class="prop-default">false</span> | If `true`, rounded corners are disabled. |
docs/pages/api/paper.md:45:| <span class="prop-name">rounded</span> | <span class="prop-name">.MuiPaper-rounded</span> | Styles applied to the root element if `square={false}`.
docs/pages/api/paper.md:46:| <span class="prop-name">elevation0</span> | <span class="prop-name">.MuiPaper-elevation0</span> | 
docs/pages/api/paper.md:47:| <span class="prop-name">elevation1</span> | <span class="prop-name">.MuiPaper-elevation1</span> | 
docs/pages/api/paper.md:48:| <span class="prop-name">elevation2</span> | <span class="prop-name">.MuiPaper-elevation2</span> | 
docs/pages/api/paper.md:49:| <span class="prop-name">elevation3</span> | <span class="prop-name">.MuiPaper-elevation3</span> | 
docs/pages/api/paper.md:50:| <span class="prop-name">elevation4</span> | <span class="prop-name">.MuiPaper-elevation4</span> | 
docs/pages/api/paper.md:51:| <span class="prop-name">elevation5</span> | <span class="prop-name">.MuiPaper-elevation5</span> | 
docs/pages/api/paper.md:52:| <span class="prop-name">elevation6</span> | <span class="prop-name">.MuiPaper-elevation6</span> | 
docs/pages/api/paper.md:53:| <span class="prop-name">elevation7</span> | <span class="prop-name">.MuiPaper-elevation7</span> | 
docs/pages/api/paper.md:54:| <span class="prop-name">elevation8</span> | <span class="prop-name">.MuiPaper-elevation8</span> | 
docs/pages/api/paper.md:55:| <span class="prop-name">elevation9</span> | <span class="prop-name">.MuiPaper-elevation9</span> | 
docs/pages/api/paper.md:56:| <span class="prop-name">elevation10</span> | <span class="prop-name">.MuiPaper-elevation10</span> | 
docs/pages/api/paper.md:57:| <span class="prop-name">elevation11</span> | <span class="prop-name">.MuiPaper-elevation11</span> | 
docs/pages/api/paper.md:58:| <span class="prop-name">elevation12</span> | <span class="prop-name">.MuiPaper-elevation12</span> | 
docs/pages/api/paper.md:59:| <span class="prop-name">elevation13</span> | <span class="prop-name">.MuiPaper-elevation13</span> | 
docs/pages/api/paper.md:60:| <span class="prop-name">elevation14</span> | <span class="prop-name">.MuiPaper-elevation14</span> | 
docs/pages/api/paper.md:61:| <span class="prop-name">elevation15</span> | <span class="prop-name">.MuiPaper-elevation15</span> | 
docs/pages/api/paper.md:62:| <span class="prop-name">elevation16</span> | <span class="prop-name">.MuiPaper-elevation16</span> | 
docs/pages/api/paper.md:63:| <span class="prop-name">elevation17</span> | <span class="prop-name">.MuiPaper-elevation17</span> | 
docs/pages/api/paper.md:64:| <span class="prop-name">elevation18</span> | <span class="prop-name">.MuiPaper-elevation18</span> | 
docs/pages/api/paper.md:65:| <span class="prop-name">elevation19</span> | <span class="prop-name">.MuiPaper-elevation19</span> | 
docs/pages/api/paper.md:66:| <span class="prop-name">elevation20</span> | <span class="prop-name">.MuiPaper-elevation20</span> | 
docs/pages/api/paper.md:67:| <span class="prop-name">elevation21</span> | <span class="prop-name">.MuiPaper-elevation21</span> | 
docs/pages/api/paper.md:68:| <span class="prop-name">elevation22</span> | <span class="prop-name">.MuiPaper-elevation22</span> | 
docs/pages/api/paper.md:69:| <span class="prop-name">elevation23</span> | <span class="prop-name">.MuiPaper-elevation23</span> | 
docs/pages/api/paper.md:70:| <span class="prop-name">elevation24</span> | <span class="prop-name">.MuiPaper-elevation24</span> |
```

**tool call: Bash**

```bash
python3 - <<'EOF'
p='docs/pages/api/paper.md'
s=open(p).read()
a="| <span class=\"prop-name\">square</span> | <span class=\"prop-type\">bool</span> | <span class=\"prop-default\">false</span> | If `true`, rounded corners are disabled. |\n"
s=s.replace(a, a+"| <span class=\"prop-name\">variant</span> | <span class=\"prop-type\">'elevation'<br>&#124;&nbsp;'outlined'</span> | <span class=\"prop-default\">'elevation'</span> | The variant to use. |\n")
b="Styles applied to the root element if `square={false}`.\n"
s=s.replace(b, b+"| <span class=\"prop-name\">outlined</span> | <span class=\"prop-name\">.MuiPaper-outlined</span> | Styles applied to the root element if `variant=\"outlined\"`\n")
open(p,'w').write(s)
EOF
git diff docs; ../bin/envrun 'cd packages/material-ui && timeout 280 yarn -s tsc -p tsconfig.json 2>&1 | tail -5; echo rc=$?'
```

tool result:

```
diff --git a/docs/pages/api/paper.md b/docs/pages/api/paper.md
index 8d9d5aae7..dd67513b6 100644
--- a/docs/pages/api/paper.md
+++ b/docs/pages/api/paper.md
@@ -29,6 +29,7 @@ You can learn more about the difference by [reading this guide](/guides/minimizi
 | <span class="prop-name">component</span> | <span class="prop-type">elementType</span> | <span class="prop-default">'div'</span> | The component used for the root node. Either a string to use a DOM element or a component. |
 | <span class="prop-name">elevation</span> | <span class="prop-type">number</span> | <span class="prop-default">1</span> | Shadow depth, corresponds to `dp` in the spec. It accepts values between 0 and 24 inclusive. |
 | <span class="prop-name">square</span> | <span class="prop-type">bool</span> | <span class="prop-default">false</span> | If `true`, rounded corners are disabled. |
+| <span class="prop-name">variant</span> | <span class="prop-type">'elevation'<br>&#124;&nbsp;'outlined'</span> | <span class="prop-default">'elevation'</span> | The variant to use. |
 
 The `ref` is forwarded to the root element.
 
@@ -43,6 +44,7 @@ Any other props supplied will be provided to the root element (native element).
 |:-----|:-------------|:------------|
 | <span class="prop-name">root</span> | <span class="prop-name">.MuiPaper-root</span> | Styles applied to the root element.
 | <span class="prop-name">rounded</span> | <span class="prop-name">.MuiPaper-rounded</span> | Styles applied to the root element if `square={false}`.
+| <span class="prop-name">outlined</span> | <span class="prop-name">.MuiPaper-outlined</span> | Styles applied to the root element if `variant="outlined"`
 | <span class="prop-name">elevation0</span> | <span class="prop-name">.MuiPaper-elevation0</span> | 
 | <span class="prop-name">elevation1</span> | <span class="prop-name">.MuiPaper-elevation1</span> | 
 | <span class="prop-name">elevation2</span> | <span class="prop-name">.MuiPaper-elevation2</span> | 
../../node_modules/@types/sinon/index.d.ts(1539,9): error TS1128: Declaration or statement expected.
../../node_modules/@types/sinon/index.d.ts(1539,10): error TS1128: Declaration or statement expected.
../../node_modules/@types/sinon/index.d.ts(1539,41): error TS1005: '(' expected.
../../node_modules/@types/sinon/index.d.ts(1540,5): error TS1128: Declaration or statement expected.
../../node_modules/@types/sinon/index.d.ts(1750,1): error TS1128: Declaration or statement expected.
rc=0
```

**assistant:** The `tsc` errors come from the environment's upgraded `@types/sinon`, not from my change. Let me make sure nothing in the output points at Paper or Card:

**tool call: Bash**

```bash
../bin/envrun 'cd packages/material-ui && timeout 280 yarn -s tsc -p tsconfig.json 2>&1 | grep -v node_modules/@types | head; echo done'; git status --short
```

tool result:

```
warning You don't appear to have an internet connection. Try the --offline flag to use the cache for registry queries.
done

 M docs/pages/api/paper.md
 M package.json
 M packages/material-ui/src/Paper/Paper.d.ts
 M packages/material-ui/src/Paper/Paper.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
```

**assistant:** I added an outlined variant to `Paper`. `Card` is built on `Paper` and passes extra props through, so `<Card variant="outlined">` works too, with no changes to `Card` itself.

**Changes**
- **`packages/material-ui/src/Paper/Paper.js`**
  - New prop `variant`, either `'elevation'` (the default) or `'outlined'`.
  - New style class `outlined` that adds a 1px border in the theme's divider colour (`theme.palette.divider`).
  - The `elevationN` shadow class is now only applied when `variant="elevation"`. So an outlined Paper or Card has no shadow, whatever `elevation` is set to. This settles the issue's question: outlined means the flat, 0dp look the spec describes, and `elevation={0}` still gives a card with no border and no shadow.
- **`packages/material-ui/src/Paper/Paper.d.ts`**: added `variant?: 'elevation' | 'outlined'` and the `'outlined'` class key.
- **`docs/pages/api/paper.md`**: added the new prop and CSS class to the API table. I edited this by hand rather than running the docs generator.

**Checks**
- The existing Paper and Card tests pass (20 tests, with `NODE_ENV=test mocha --exit`). That run included a temporary test file I wrote and then deleted. It confirmed that an outlined Paper gets the `outlined` class and no `elevation1` class, that a default Card keeps `elevation1` with no outline, and that `<Card variant="outlined">` gets the `outlined` class.
- The TypeScript check fails, but every error is inside `node_modules/@types/sinon`. None point at the Paper or Card files.

**Files I didn't touch:** `package.json` and `yarn.lock` already had changes I didn't make (including the upgraded `@types` packages behind those TypeScript errors), and `Dockerfile` and `custom-reporter.js` are untracked. These look like they come from the environment setup, so I left them as they were.

_session end: success, turns 18, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 2.07 s: yarn -s mocha packages/material-ui/src/Paper/*.test.js packages/material-ui/src/Card/*.test.js 2>&1 | tail -30
- `rc=0` 1.74 s: yarn -s mocha packages/material-ui/src/Paper/*.test.js packages/material-ui/src/Card/*.test.js 2>&1 | grep -m3 -i "cannot find"
- `rc=0` 0.18 s: ps aux | grep -c mocha; ps aux | grep mocha | head -3
- `rc=143` 0.12 s: pkill -f mocha; NODE_ENV=test timeout 250 node_modules/.bin/mocha --exit packages/material-ui/src/Paper/*.test.js packages/material-ui/src/Card/*.test.js 2>&1 | tail -30
- `rc=143` 584.53 s: NODE_ENV=test yarn -s mocha packages/material-ui/src/Paper/*.test.js packages/material-ui/src/Card/*.test.js 2>&1 | tail -30
- `rc=0` 1.92 s: NODE_ENV=test timeout 280 node_modules/.bin/mocha --exit packages/material-ui/src/Paper/*.test.js packages/material-ui/src/Card/*.test.js > /tmp/out.txt 2>&1; echo rc=$?; tail -40 /tmp/out.txt
- `rc=0` 3.45 s: cd packages/material-ui && timeout 280 yarn -s tsc -p tsconfig.json 2>&1 | tail -5; echo rc=$?
- `rc=0` 3.3 s: cd packages/material-ui && timeout 280 yarn -s tsc -p tsconfig.json 2>&1 | grep -v node_modules/@types | head; echo done
