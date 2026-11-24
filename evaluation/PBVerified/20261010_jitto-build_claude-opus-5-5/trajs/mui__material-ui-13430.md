# Instance: mui__material-ui-13430

- Final resolved (evaluator, logs/mui__material-ui-13430_result.json): True
- Run state: DONE
- One attempt. Duration 116.6 s, turns 19, actor cost $0.36875139999999995, container commands 6
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/mui__material-ui-13430/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-13430/repo. Consider the following issue description:

<issue_description>
CircularProgress, length of the line does not animate under load
<!-- Checked checkbox should look like this: [x] -->
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Expected Behavior
CircularProgress animation should be smooth and predictable under load

## Current Behavior
The animation is okay but the dynamic length of the line only updates once a while under load.  Maybe my understanding of Promise is wrong? I thought it would move the load away from the main UI thread?

![sept -08-2018 12-00-39](https://user-images.githubusercontent.com/3165635/45252949-df553080-b35e-11e8-9d3c-934f2e959019.gif)

## Steps to Reproduce (for bugs)
1. generate some load inside a promise
2. observe CircularProgress animation, it still runs but the length of the circle stays constant

demo: https://codesandbox.io/s/j4xvnvv8nv (warning, Chrome pls, firefox crashes under this artificial load)


## Context
My app uses canvas to resize a bunch of user selected files.  I tried CircularProgress but to my surprise the animation is semi broken.  My workaround: animated Gif.

## Your Environment

| Tech         | Version |
|--------------|---------|
| Material-UI  |    v1.0.0-beta.33     |
| React        |     16.3    |
| browser      |     Chrome    |


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-13430/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-13430/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-13430/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-13430/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
ls packages/material-ui/src/CircularProgress && cat packages/material-ui/src/CircularProgress/CircularProgress.js packages/material-ui/src/CircularProgress/CircularProgress.d.ts && grep -n "disableShrink\|Shrink" -r packages/material-ui/src/CircularProgress docs/src/pages/demos/progress | head
```

tool result:

```
CircularProgress.d.ts
CircularProgress.js
CircularProgress.test.js
index.d.ts
index.js
import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import withStyles from '../styles/withStyles';
import { capitalize } from '../utils/helpers';

const SIZE = 44;

function getRelativeValue(value, min, max) {
  const clampedValue = Math.min(Math.max(min, value), max);
  return (clampedValue - min) / (max - min);
}

function easeOut(t) {
  t = getRelativeValue(t, 0, 1);
  // https://gist.github.com/gre/1650294
  t = (t -= 1) * t * t + 1;
  return t;
}

function easeIn(t) {
  return t * t;
}

export const styles = theme => ({
  /* Styles applied to the root element. */
  root: {
    display: 'inline-block',
    lineHeight: 1, // Keep the progress centered
  },
  /* Styles applied to the root element if `variant="static"`. */
  static: {
    transition: theme.transitions.create('transform'),
  },
  /* Styles applied to the root element if `variant="indeterminate"`. */
  indeterminate: {
    animation: 'mui-progress-circular-rotate 1.4s linear infinite',
  },
  /* Styles applied to the root element if `color="primary"`. */
  colorPrimary: {
    color: theme.palette.primary.main,
  },
  /* Styles applied to the root element if `color="secondary"`. */
  colorSecondary: {
    color: theme.palette.secondary.main,
  },
  /* Styles applied to the `svg` element. */
  svg: {},
  /* Styles applied to the `circle` svg path. */
  circle: {
    stroke: 'currentColor',
    // Use butt to follow the specification, by chance, it's already the default CSS value.
    // strokeLinecap: 'butt',
  },
  /* Styles applied to the `circle` svg path if `variant="static"`. */
  circleStatic: {
    transition: theme.transitions.create('stroke-dashoffset'),
  },
  /* Styles applied to the `circle` svg path if `variant="indeterminate"`. */
  circleIndeterminate: {
    animation: 'mui-progress-circular-dash 1.4s ease-in-out infinite',
    // Some default value that looks fine waiting for the animation to kicks in.
    strokeDasharray: '80px, 200px',
    strokeDashoffset: '0px', // Add the unit to fix a Edge 16 and below bug.
  },
  '@keyframes mui-progress-circular-rotate': {
    '100%': {
      transform: 'rotate(360deg)',
    },
  },
  '@keyframes mui-progress-circular-dash': {
    '0%': {
      strokeDasharray: '1px, 200px',
      strokeDashoffset: '0px',
    },
    '50%': {
      strokeDasharray: '100px, 200px',
      strokeDashoffset: '-15px',
    },
    '100%': {
      strokeDasharray: '100px, 200px',
      strokeDashoffset: '-120px',
    },
  },
});

/**
 * ## ARIA
 *
 * If the progress bar is describing the loading progress of a particular region of a page,
 * you should use `aria-describedby` to point to the progress bar, and set the `aria-busy`
 * attribute to `true` on that region until it has finished loading.
 */
function CircularProgress(props) {
  const { classes, className, color, size, style, thickness, value, variant, ...other } = props;

  const circleStyle = {};
  const rootStyle = {};
  const rootProps = {};

  if (variant === 'determinate' || variant === 'static') {
    const circumference = 2 * Math.PI * ((SIZE - thickness) / 2);
    circleStyle.strokeDasharray = circumference.toFixed(3);
    rootProps['aria-valuenow'] = Math.round(value);

    if (variant === 'static') {
      circleStyle.strokeDashoffset = `${(((100 - value) / 100) * circumference).toFixed(3)}px`;
      rootStyle.transform = 'rotate(-90deg)';
    } else {
      circleStyle.strokeDashoffset = `${(easeIn((100 - value) / 100) * circumference).toFixed(
        3,
      )}px`;
      rootStyle.transform = `rotate(${(easeOut(value / 70) * 270).toFixed(3)}deg)`;
    }
  }

  return (
    <div
      className={classNames(
        classes.root,
        {
          [classes[`color${capitalize(color)}`]]: color !== 'inherit',
          [classes.indeterminate]: variant === 'indeterminate',
          [classes.static]: variant === 'static',
        },
        className,
      )}
      style={{ width: size, height: size, ...rootStyle, ...style }}
      role="progressbar"
      {...rootProps}
      {...other}
    >
      <svg className={classes.svg} viewBox={`${SIZE / 2} ${SIZE / 2} ${SIZE} ${SIZE}`}>
        <circle
          className={classNames(classes.circle, {
            [classes.circleIndeterminate]: variant === 'indeterminate',
            [classes.circleStatic]: variant === 'static',
          })}
          style={circleStyle}
          cx={SIZE}
          cy={SIZE}
          r={(SIZE - thickness) / 2}
          fill="none"
          strokeWidth={thickness}
        />
      </svg>
    </div>
  );
}

CircularProgress.propTypes = {
  /**
   * Override or extend the styles applied to the component.
   * See [CSS API](#css-api) below for more details.
   */
  classes: PropTypes.object.isRequired,
  /**
   * @ignore
   */
  className: PropTypes.string,
  /**
   * The color of the component. It supports those theme colors that make sense for this component.
   */
  color: PropTypes.oneOf(['primary', 'secondary', 'inherit']),
  /**
   * The size of the circle.
   */
  size: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),
  /**
   * @ignore
   */
  style: PropTypes.object,
  /**
   * The thickness of the circle.
   */
  thickness: PropTypes.number,
  /**
   * The value of the progress indicator for the determinate and static variants.
   * Value between 0 and 100.
   */
  value: PropTypes.number,
  /**
   * The variant to use.
   * Use indeterminate when there is no progress value.
   */
  variant: PropTypes.oneOf(['determinate', 'indeterminate', 'static']),
};

CircularProgress.defaultProps = {
  color: 'primary',
  size: 40,
  thickness: 3.6,
  value: 0,
  variant: 'indeterminate',
};

export default withStyles(styles, { name: 'MuiCircularProgress', flip: false })(CircularProgress);
import * as React from 'react';
import { StandardProps } from '..';

export interface CircularProgressProps
  extends
[... 555 more characters not shown]
```

**tool call: Bash**

```bash
grep -n "disableShrink\|Shrink" -i -B3 -A20 packages/material-ui/src/CircularProgress/CircularProgress.test.js; git log --oneline -1
```

tool result:

```
fa2b154ff [Slider] Fix hover state not being registered (#13437)
```

**thinking:**

```
The stroke-dasharray animation runs on the main thread and stalls under load, unlike the GPU-accelerated rotation — so I'll add a `disableShrink` prop to disable it, mirroring Material-UI's upstream fix.


```

**tool call: Bash**

```bash
ls packages/material-ui/src/utils/ | grep -i chain; grep -rn "chainPropTypes" packages/material-ui/src --include=*.js | head -3; ls pages/api | grep circular; ls docs/src/pages/demos/progress/
```

tool result:

```
chainPropTypes.js
chainPropTypes.test.js
(eval):1: no matches found: --include=*.js
circular-progress.js
circular-progress.md
CircularDeterminate.js
CircularIndeterminate.js
CircularIntegration.js
CircularStatic.js
DelayingAppearance.js
LinearBuffer.js
LinearDeterminate.js
LinearIndeterminate.js
LinearQuery.js
progress-zh.md
progress.md
```

**assistant:** Now the edits:

**tool call: Bash**

```bash
cd packages/material-ui/src/CircularProgress && python3 - <<'EOF'
p='CircularProgress.js'
s=open(p).read()
s=s.replace("""import { capitalize } from '../utils/helpers';
""","""import { capitalize } from '../utils/helpers';
import chainPropTypes from '../utils/chainPropTypes';
""")
s=s.replace("""    strokeDashoffset: '0px', // Add the unit to fix a Edge 16 and below bug.
  },
""","""    strokeDashoffset: '0px', // Add the unit to fix a Edge 16 and below bug.
  },
  /* Styles applied to the `circle` svg path if `disableShrink={true}`. */
  circleDisableShrink: {
    animation: 'none',
  },
""")
s=s.replace("""  const { classes, className, color, size, style, thickness, value, variant, ...other } = props;""","""  const {
    classes,
    className,
    color,
    disableShrink,
    size,
    style,
    thickness,
    value,
    variant,
    ...other
  } = props;""")
s=s.replace("""            [classes.circleStatic]: variant === 'static',
""","""            [classes.circleStatic]: variant === 'static',
            [classes.circleDisableShrink]: disableShrink,
""")
s=s.replace("""  color: PropTypes.oneOf(['primary', 'secondary', 'inherit']),
  /**
   * The size""","""  color: PropTypes.oneOf(['primary', 'secondary', 'inherit']),
  /**
   * If `true`, the shrink animation is disabled.
   * This only works if variant is `indeterminate`.
   */
  disableShrink: chainPropTypes(PropTypes.bool, props => {
    /* istanbul ignore if */
    if (props.disableShrink && props.variant !== 'indeterminate') {
      return new Error(
        'Material-UI: you have provided the `disableShrink` property ' +
          'with a variant other than `indeterminate`. This will have no effect.',
      );
    }

    return null;
  }),
  /**
   * The size""")
s=s.replace("""  color: 'primary',
  size: 40,""","""  color: 'primary',
  disableShrink: false,
  size: 40,""")
open(p,'w').write(s)
p='CircularProgress.d.ts'
s=open(p).read()
s=s.replace("""  color?: 'primary' | 'secondary' | 'inherit';
""","""  color?: 'primary' | 'secondary' | 'inherit';
  disableShrink?: boolean;
""")
s=s.replace("""  | 'circleIndeterminate';""","""  | 'circleIndeterminate'
  | 'circleDisableShrink';""")
open(p,'w').write(s)
EOF
git diff --stat; cat ../utils/chainPropTypes.js
```

tool result:

```
 package.json                                       |  6 +++
 .../src/CircularProgress/CircularProgress.d.ts     |  4 +-
 .../src/CircularProgress/CircularProgress.js       | 35 +++++++++++++++-
 yarn.lock                                          | 46 ++++++++++++++++++++++
 4 files changed, 89 insertions(+), 2 deletions(-)
function chainPropTypes(propType1, propType2) {
  /* istanbul ignore if */
  if (process.env.NODE_ENV === 'production') {
    return () => null;
  }

  return function validate(...args) {
    return propType1(...args) || propType2(...args);
  };
}

export default chainPropTypes;
```

**assistant:** `package.json` and `yarn.lock` show changes I didn't make. Let me check them.

**tool call: Bash**

```bash
cd /work/mui__material-ui-13430/repo && git diff package.json; git diff yarn.lock | head -20
```

tool result:

```
diff --git a/package.json b/package.json
index ca1edc8f7..dcd206444 100644
--- a/package.json
+++ b/package.json
@@ -69,8 +69,14 @@
     "@babel/preset-env": "7.1.0",
     "@babel/preset-react": "7.0.0",
     "@babel/register": "7.0.0",
+    "@types/chai": "^5.2.2",
+    "@types/chai-dom": "^1.11.3",
     "@types/enzyme": "^3.1.4",
+    "@types/format-util": "^1.0.4",
+    "@types/prop-types": "^15.7.15",
     "@types/react": "^16.3.14",
+    "@types/react-dom": "^19.1.8",
+    "@types/sinon": "^17.0.4",
     "accept-language": "^3.0.18",
     "argos-cli": "^0.0.9",
     "autoprefixer": "^9.0.0",
diff --git a/yarn.lock b/yarn.lock
index a4cca266f..0fba4c8cc 100644
--- a/yarn.lock
+++ b/yarn.lock
@@ -953,11 +953,30 @@
   resolved "https://registry.yarnpkg.com/@sinonjs/samsam/-/samsam-2.1.2.tgz#16947fce5f57258d01f1688fdc32723093c55d3f"
   integrity sha512-ZwTHAlC9akprWDinwEPD4kOuwaYZlyMwVJIANsKNC3QVp0AHB04m7RnB4eqeWfgmxw8MGTzS9uMaw93Z3QcZbw==
 
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
```

**assistant:** Those dependency changes come from the environment setup, not from me, so I'll leave them alone. Next I'll write a quick check script and run it along with the existing tests:

**tool call: Bash**

```bash
cat > packages/material-ui/src/CircularProgress/tmpRepro.test.js <<'EOF'
import React from 'react';
import { assert } from 'chai';
import { createShallow, getClasses } from '../test-utils';
import CircularProgress from './CircularProgress';

describe('repro disableShrink', () => {
  const shallow = createShallow({ dive: true });
  const classes = getClasses(<CircularProgress />);
  it('works', () => {
    const circle = w => w.childAt(0).childAt(0);
    assert.strictEqual(circle(shallow(<CircularProgress />)).hasClass(classes.circleDisableShrink), false);
    assert.strictEqual(circle(shallow(<CircularProgress disableShrink />)).hasClass(classes.circleDisableShrink), true);
  });
});
EOF
bin=../bin/envrun; $bin 'NODE_ENV=test npx mocha --require @babel/register packages/material-ui/src/CircularProgress/*.test.js packages/material-ui/src/utils/chainPropTypes.test.js 2>&1 | tail -15'
```

tool result:

```
  1) repro disableShrink
       works:

      AssertionError: expected false to equal true
      + expected - actual

      -false
      +true
      
      at Context.strictEqual (packages/material-ui/src/CircularProgress/tmpRepro.test.js:12:12)
      at processImmediate (node:internal/timers:466:21)
```

**assistant:** The check failed even with the fix applied, so I'll look into why:

**tool call: Bash**

```bash
grep -n '"test:unit"' package.json; cat test/mocha.opts 2>/dev/null; ../bin/envrun 'NODE_ENV=test npx mocha --require @babel/register packages/material-ui/src/CircularProgress/*.test.js 2>&1 | head -40'
```

tool result:

```
47:    "test:unit": "cross-env NODE_ENV=test mocha packages/material-ui/test/**/*.test.js packages/material-ui/src/{,**/}*.test.js docs/src/**/*.test.js",
--require @babel/register
--reporter dot
--recursive
test/utils/setup.js
Browserslist: caniuse-lite is outdated. Please run next command `yarn upgrade caniuse-lite browserslist`


  ․․․․․․․․․․․!

  11 passing (87ms)
  1 failing

  1) repro disableShrink
       works:

      AssertionError: expected false to equal true
      + expected - actual

      -false
      +true
      
      at Context.strictEqual (packages/material-ui/src/CircularProgress/tmpRepro.test.js:12:12)
      at processImmediate (node:internal/timers:466:21)
```

**tool call: Bash**

```bash
../bin/envrun 'grep -n "DisableShrink" packages/material-ui/src/CircularProgress/CircularProgress.js; cat > /tmp/d.test.js <<EOF
import React from "react";
import { createShallow, getClasses } from "/testbed/packages/material-ui/src/test-utils";
import CircularProgress from "/testbed/packages/material-ui/src/CircularProgress/CircularProgress";
it("x", () => { const s = createShallow({ dive: true }); console.log(getClasses(<CircularProgress />)); console.log(s(<CircularProgress disableShrink />).debug()); });
EOF
cp /tmp/d.test.js packages/material-ui/src/CircularProgress/tmpd.test.js; NODE_ENV=test npx mocha packages/material-ui/src/CircularProgress/tmpd.test.js 2>&1 | tail -30; rm packages/material-ui/src/CircularProgress/tmpd.test.js'
```

tool result:

```
68:  circleDisableShrink: {
154:            [classes.circleDisableShrink]: disableShrink,
Browserslist: caniuse-lite is outdated. Please run next command `yarn upgrade caniuse-lite browserslist`

{
  root: 'MuiCircularProgress-root-1',
  static: 'MuiCircularProgress-static-2',
  indeterminate: 'MuiCircularProgress-indeterminate-3',
  colorPrimary: 'MuiCircularProgress-colorPrimary-4',
  colorSecondary: 'MuiCircularProgress-colorSecondary-5',
  svg: 'MuiCircularProgress-svg-6',
  circle: 'MuiCircularProgress-circle-7',
  circleStatic: 'MuiCircularProgress-circleStatic-8',
  circleIndeterminate: 'MuiCircularProgress-circleIndeterminate-9',
  circleDisableShrink: 'MuiCircularProgress-circleDisableShrink-10'
}
<div className="MuiCircularProgress-root-1 MuiCircularProgress-colorPrimary-4 MuiCircularProgress-indeterminate-3" style={{...}} role="progressbar">
  <svg className="MuiCircularProgress-svg-6" viewBox="22 22 44 44">
    <circle className="MuiCircularProgress-circle-7 MuiCircularProgress-circleIndeterminate-9 MuiCircularProgress-circleDisableShrink-10" style={{...}} cx={44} cy={44} r={20.2} fill="none" strokeWidth={3.6} />
  </svg>
</div>

  ․

  1 passing (56ms)
```

**thinking:**

```
The component is rendering the new class correctly—the repro only failed because it computed class names at suite definition instead of in `before()`. I'll fix that in the script and rerun it.


```

**tool call: Bash**

```bash
cd packages/material-ui/src/CircularProgress && python3 - <<'EOF'
p='tmpRepro.test.js'
s=open(p).read()
s=s.replace("""  const shallow = createShallow({ dive: true });
  const classes = getClasses(<CircularProgress />);""","""  let shallow;
  let classes;
  before(() => {
    shallow = createShallow({ dive: true });
    classes = getClasses(<CircularProgress />);
  });""")
open(p,'w').write(s)
EOF
../../../../../bin/envrun 'NODE_ENV=test npx mocha packages/material-ui/src/CircularProgress/*.test.js packages/material-ui/src/utils/chainPropTypes.test.js 2>&1 | tail -5'
```

tool result:

```
  ․․․․․․․․․․․․․․․

  15 passing (122ms)
```

**assistant:** Before the fix the repro should fail. To confirm, I'll stash my component change and rerun it:

**tool call: Bash**

```bash
cd /work/mui__material-ui-13430/repo && cp packages/material-ui/src/CircularProgress/CircularProgress.js /tmp/cp.js && git checkout packages/material-ui/src/CircularProgress/CircularProgress.js && ../bin/envrun 'NODE_ENV=test npx mocha packages/material-ui/src/CircularProgress/tmpRepro.test.js 2>&1 | grep -E "passing|failing|Error"'; cp /tmp/cp.js packages/material-ui/src/CircularProgress/CircularProgress.js; rm packages/material-ui/src/CircularProgress/tmpRepro.test.js
```

tool result:

```
cp: /tmp/cp.js: Operation not permitted
cp: /tmp/cp.js: No such file or directory
```

**assistant:** The first copy failed, so the `&&` chain stopped before `git checkout`. Let me check that my edit is still in place:

**tool call: Bash**

```bash
git status --short; grep -c DisableShrink packages/material-ui/src/CircularProgress/CircularProgress.js
```

tool result:

```
 M package.json
 M packages/material-ui/src/CircularProgress/CircularProgress.d.ts
 M packages/material-ui/src/CircularProgress/CircularProgress.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
2
```

**assistant:** The edit is intact. I'm skipping the before-fix check: that class key didn't exist before, so the assertion couldn't have passed. Next I'll regenerate the API docs and add a demo:

**tool call: Bash**

```bash
grep -n '"docs:api"' package.json; ../bin/envrun 'yarn -s docs:api >/dev/null 2>&1; echo $?; git status --short; git diff pages/'; cat docs/src/pages/demos/progress/CircularIndeterminate.js; grep -n "Circular" docs/src/pages/demos/progress/progress.md
```

tool result:

```
25:    "docs:api": "yarn docs:api:core && yarn docs:api:lab",
0
 M package.json
 M packages/material-ui/src/CircularProgress/CircularProgress.d.ts
 M packages/material-ui/src/CircularProgress/CircularProgress.js
 M pages/api/circular-progress.md
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
diff --git a/pages/api/circular-progress.md b/pages/api/circular-progress.md
index dfe012a33..a7d4cc1de 100644
--- a/pages/api/circular-progress.md
+++ b/pages/api/circular-progress.md
@@ -25,6 +25,7 @@ attribute to `true` on that region until it has finished loading.
 |:-----|:-----|:--------|:------------|
 | <span class="prop-name">classes</span> | <span class="prop-type">object</span> |   | Override or extend the styles applied to the component. See [CSS API](#css-api) below for more details. |
 | <span class="prop-name">color</span> | <span class="prop-type">enum:&nbsp;'primary'&nbsp;&#124;<br>&nbsp;'secondary'&nbsp;&#124;<br>&nbsp;'inherit'<br></span> | <span class="prop-default">'primary'</span> | The color of the component. It supports those theme colors that make sense for this component. |
+| <span class="prop-name">disableShrink</span> | <span class="prop-type">bool</span> | <span class="prop-default">false</span> | If `true`, the shrink animation is disabled. This only works if variant is `indeterminate`. |
 | <span class="prop-name">size</span> | <span class="prop-type">union:&nbsp;number&nbsp;&#124;<br>&nbsp;string<br></span> | <span class="prop-default">40</span> | The size of the circle. |
 | <span class="prop-name">thickness</span> | <span class="prop-type">number</span> | <span class="prop-default">3.6</span> | The thickness of the circle. |
 | <span class="prop-name">value</span> | <span class="prop-type">number</span> | <span class="prop-default">0</span> | The value of the progress indicator for the determinate and static variants. Value between 0 and 100. |
@@ -49,6 +50,7 @@ This property accepts the following keys:
 | <span class="prop-name">circle</span> | Styles applied to the `circle` svg path.
 | <span class="prop-name">circleStatic</span> | Styles applied to the `circle` svg path if `variant="static"`.
 | <span class="prop-name">circleIndeterminate</span> | Styles applied to the `circle` svg path if `variant="indeterminate"`.
+| <span class="prop-name">circleDisableShrink</span> | Styles applied to the `circle` svg path if `disableShrink={true}`.
 
 Have a look at [overriding with classes](/customization/overrides/#overriding-with-classes) section
 and the [implementation of the component](https://github.com/mui-org/material-ui/tree/master/packages/material-ui/src/CircularProgress/CircularProgress.js)

import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import CircularProgress from '@material-ui/core/CircularProgress';
import purple from '@material-ui/core/colors/purple';

const styles = theme => ({
  progress: {
    margin: theme.spacing.unit * 2,
  },
});

function CircularIndeterminate(props) {
  const { classes } = props;
  return (
    <div>
      <CircularProgress className={classes.progress} />
      <CircularProgress className={classes.progress} size={50} />
      <CircularProgress className={classes.progress} color="secondary" />
      <CircularProgress className={classes.progress} style={{ color: purple[500] }} thickness={7} />
    </div>
  );
}

CircularIndeterminate.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(CircularIndeterminate);
2:title: Circular Progress, Linear Progress React component
3:components: CircularProgress, LinearProgress
20:## Circular
22:[Circular progress](https://material.io/design/components/progress-indicators.html#circular-progress-indicators) support both determinate and indeterminate processes.
27:### Circular Indeterminate
29:{{"demo": "pages/demos/progress/CircularIndeterminate.js"}}
33:{{"demo": "pages/demos/progress/CircularIntegration.js"}}
35:### Circular Determinate
37:{{"demo": "pages/demos/progress/CircularDeterminate.js"}}
39:### Circular Static
41:{{"demo": "pages/demos/progress/CircularStatic.js"}}
78:      <CircularProgress variant="determinate" value={normalise(props.value)} />
96:Under heavy load, you might lose the stroke dash animation or see random CircularProgress ring widths.
```

**tool call: Bash**

```bash
sed -n 85,110p docs/src/pages/demos/progress/progress.md
```

tool result:

```
## Delaying appearance

There are [3 important limits](https://www.nngroup.com/articles/response-times-3-important-limits/) to know around response time.
The ripple effect of the `ButtonBase` component ensures that the user feels that the system is reacting instantaneously.
Normally, no special feedback is necessary during delays of more than 0.1 but less than 1.0 second.
After 1.0 second, you can display a loader to keep user's flow of thought uninterrupted.

{{"demo": "pages/demos/progress/DelayingAppearance.js"}}

## Limitations

Under heavy load, you might lose the stroke dash animation or see random CircularProgress ring widths.
You should run processor intensive operations in a web worker or by batch in order not to block the main rendering thread.

![heavy load](/static/images/progress/heavy-load.gif)

See https://github.com/mui-org/material-ui/issues/10327
```

**tool call: Bash**

```bash
python3 - <<'EOF'
p='docs/src/pages/demos/progress/progress.md'
s=open(p).read()
s=s.replace("""
![heavy load](/static/images/progress/heavy-load.gif)

See https://github.com/mui-org/material-ui/issues/10327""","""
![heavy load](/static/images/progress/heavy-load.gif)

When it's not possible, you can leverage the `disableShrink` property to mitigate the issue.
See https://github.com/mui-org/material-ui/issues/10327

{{"demo": "pages/demos/progress/CircularUnderLoad.js"}}""")
open(p,'w').write(s)
EOF
cat > docs/src/pages/demos/progress/CircularUnderLoad.js <<'EOF'
import React from 'react';
import CircularProgress from '@material-ui/core/CircularProgress';

function CircularUnderLoad() {
  return <CircularProgress disableShrink />;
}

export default CircularUnderLoad;
EOF
grep -rln "CircularStatic" docs pages | grep -v "progress.md\|CircularStatic.js"
```

tool result:

```
docs/src/pages/demos/progress/progress-zh.md
pages/demos/progress.js
```

**tool call: Bash**

```bash
grep -n -A8 "CircularStatic" pages/demos/progress.js
```

tool result:

```
33:        'pages/demos/progress/CircularStatic.js': {
34:          js: require('docs/src/pages/demos/progress/CircularStatic').default,
35-          raw: preval`
36-module.exports = require('fs')
37:  .readFileSync(require.resolve('docs/src/pages/demos/progress/CircularStatic'), 'utf8')
38-`,
39-        },
40-        'pages/demos/progress/LinearIndeterminate.js': {
41-          js: require('docs/src/pages/demos/progress/LinearIndeterminate').default,
42-          raw: preval`
43-module.exports = require('fs')
44-  .readFileSync(require.resolve('docs/src/pages/demos/progress/LinearIndeterminate'), 'utf8')
45-`,
```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/mui__material-ui-13430/repo/pages/demos/progress.js",
 "old_string": "  .readFileSync(require.resolve('docs/src/pages/demos/progress/CircularStatic'), 'utf8')\n`,\n        },",
 "new_string": "  .readFileSync(require.resolve('docs/src/pages/demos/progress/CircularStatic'), 'utf8')\n`,\n        },\n        'pages/demos/progress/CircularUnderLoad.js': {\n          js: require('docs/src/pages/demos/progress/CircularUnderLoad').default,\n          raw: preval`\nmodule.exports = require('fs')\n  .readFileSync(require.resolve('docs/src/pages/demos/progress/CircularUnderLoad'), 'utf8')\n`,\n        },"
}
```

tool result:

```
The file /work/mui__material-ui-13430/repo/pages/demos/progress.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
../bin/envrun 'npx eslint packages/material-ui/src/CircularProgress docs/src/pages/demos/progress pages/demos/progress.js && npx prettier --list-different packages/material-ui/src/CircularProgress/*.js docs/src/pages/demos/progress/*.js; NODE_ENV=test npx mocha packages/material-ui/src/CircularProgress/*.test.js 2>&1 | tail -3; npx tsc -p . --noEmit 2>&1 | grep -i circular | head'
```

tool result:

```
  11 passing (95ms)
```

**tool call: Bash**

```bash
git status --short
```

tool result:

```
 M docs/src/pages/demos/progress/progress.md
 M package.json
 M packages/material-ui/src/CircularProgress/CircularProgress.d.ts
 M packages/material-ui/src/CircularProgress/CircularProgress.js
 M pages/api/circular-progress.md
 M pages/demos/progress.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
?? docs/src/pages/demos/progress/CircularUnderLoad.js
```

**assistant:** I added a `disableShrink` prop to `CircularProgress`. With it set, the spinner keeps turning smoothly even when the page is busy.

**Why the issue happens:** the indeterminate spinner runs two CSS animations at once. The rotation (a `transform`) runs off the main thread, which is why it stays smooth under load. The growing and shrinking of the line animates `stroke-dasharray`, which needs the main thread, so it stalls whenever the main thread is blocked. Wrapping heavy work in a Promise doesn't help, because Promise callbacks still run on the main thread. The real fix on the app side is to move the work into a Web Worker or split it into smaller chunks. When that isn't possible, `disableShrink` gives up the length animation so the spinner doesn't look broken.

**Changes:**
- **`CircularProgress.js`:**
  - New style class `circleDisableShrink` (`animation: 'none'`), applied to the `<circle>` when `disableShrink` is true. The prop defaults to `false`, so current behaviour is unchanged.
  - A dev-only warning if `disableShrink` is used with a variant other than `indeterminate`, since it has no effect there.
- **`CircularProgress.d.ts`:** added the `disableShrink?: boolean` prop and the `'circleDisableShrink'` class key.
- **Docs:**
  - Regenerated `pages/api/circular-progress.md` with `yarn docs:api`.
  - Added a sentence to the "Limitations" section of `progress.md` pointing to `disableShrink`.
  - Added a new demo, `CircularUnderLoad.js`, and registered it in `pages/demos/progress.js`.

**Checks:**
- A temporary test confirmed the circle gets the new class with `disableShrink` and doesn't get it by default; I've deleted it.
- I didn't run that test against the unfixed code. My attempt to stash the change stopped early when a copy to `/tmp` failed. The class didn't exist before, so it couldn't have passed.
- The existing `CircularProgress` tests (11) pass. ESLint and Prettier report nothing on the changed files, and `tsc` shows no errors for `CircularProgress`.
- I didn't watch the animation in a browser under load. The visual result rests on how the CSS works, not on a test.

The working tree also has changes I didn't make and left alone: `package.json` and `yarn.lock` (added `@types/*` dev dependencies), plus untracked `Dockerfile` and `custom-reporter.js`. They look like they come from the test environment setup.

_session end: success, turns 19, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 3.95 s: NODE_ENV=test npx mocha --require @babel/register packages/material-ui/src/CircularProgress/*.test.js packages/material-ui/src/utils/chainPropTypes.test.js 2>&1 | tail -15
- `rc=0` 2.44 s: NODE_ENV=test npx mocha --require @babel/register packages/material-ui/src/CircularProgress/*.test.js 2>&1 | head -40
- `rc=0` 2.69 s: grep -n "DisableShrink" packages/material-ui/src/CircularProgress/CircularProgress.js; cat > /tmp/d.test.js <<EOF import React from "react"; import { createShallow, getClasses } from "/testbed/packages/material-ui/src/test-utils"; import CircularProgress from "/testbed/packages/material-ui/src/CircularProgress/CircularProgress"; it("x", () => { const s = createShallow({ dive: true }); console.log(getClasses(<CircularProgress />)); console.log(s(<CircularProgress disableShrink />).debug()); }); EOF cp /tmp/d.test.js packages/material-ui/src/CircularProgress/tmpd.test.js; NODE_ENV=test npx mocha
- `rc=0` 2.63 s: NODE_ENV=test npx mocha packages/material-ui/src/CircularProgress/*.test.js packages/material-ui/src/utils/chainPropTypes.test.js 2>&1 | tail -5
- `rc=0` 17.77 s: yarn -s docs:api >/dev/null 2>&1; echo $?; git status --short; git diff pages/
- `rc=0` 9.92 s: npx eslint packages/material-ui/src/CircularProgress docs/src/pages/demos/progress pages/demos/progress.js && npx prettier --list-different packages/material-ui/src/CircularProgress/*.js docs/src/pages/demos/progress/*.js; NODE_ENV=test npx mocha packages/material-ui/src/CircularProgress/*.test.js 2>&1 | tail -3; npx tsc -p . --noEmit 2>&1 | grep -i circular | head
