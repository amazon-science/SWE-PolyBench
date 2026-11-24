# Instance: mui__material-ui-11451

- Final resolved (evaluator, logs/mui__material-ui-11451_result.json): True
- Run state: DONE
- One attempt. Duration 58.4 s, turns 12, actor cost $0.2233888, container commands 4
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/mui__material-ui-11451/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-11451/repo. Consider the following issue description:

<issue_description>
MenuItem doesn't respect focusVisibleClassName
Related to #10976. 

The changes in #10976 work awesome for the `Switch`, however it looks like the `MenuItem`'s `focusVisibleClassName` prop doesn't work as expected. Passing a `focusVisibleClassName` to the item works great from a typing perspective, but they don't seem to be applied to the `ListItem` correctly.

Example: https://codesandbox.io/s/5638ox58n 

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-11451/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-11451/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-11451/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-11451/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/mui__material-ui-11451/repo; cat src/List/ListItem.js; cat src/Menu/MenuItem.js
```

tool result:

```
Exit code 1
cat: src/List/ListItem.js: No such file or directory
cat: src/Menu/MenuItem.js: No such file or directory
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-11451/repo; f=$(find packages -name ListItem.js -not -path '*/node_modules/*' | head -1); echo $f; cat $f
```

tool result:

```
packages/material-ui/src/ListItem/ListItem.js
import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import withStyles from '../styles/withStyles';
import ButtonBase from '../ButtonBase';
import { isMuiElement } from '../utils/reactHelpers';

export const styles = theme => ({
  root: {
    display: 'flex',
    justifyContent: 'flex-start',
    alignItems: 'center',
    position: 'relative',
    textDecoration: 'none',
    width: '100%',
    boxSizing: 'border-box',
    textAlign: 'left',
  },
  container: {
    position: 'relative',
  },
  focusVisible: {
    backgroundColor: theme.palette.action.hover,
  },
  default: {
    paddingTop: 12,
    paddingBottom: 12,
  },
  dense: {
    paddingTop: theme.spacing.unit,
    paddingBottom: theme.spacing.unit,
  },
  disabled: {
    opacity: 0.5,
  },
  divider: {
    borderBottom: `1px solid ${theme.palette.divider}`,
    backgroundClip: 'padding-box',
  },
  gutters: theme.mixins.gutters(),
  button: {
    transition: theme.transitions.create('background-color', {
      duration: theme.transitions.duration.shortest,
    }),
    '&:hover': {
      textDecoration: 'none',
      backgroundColor: theme.palette.action.hover,
      // Reset on touch devices, it doesn't add specificity
      '@media (hover: none)': {
        backgroundColor: 'transparent',
      },
    },
  },
  secondaryAction: {
    // Add some space to avoid collision as `ListItemSecondaryAction`
    // is absolutely positionned.
    paddingRight: theme.spacing.unit * 4,
  },
});

class ListItem extends React.Component {
  getChildContext() {
    return {
      dense: this.props.dense || this.context.dense || false,
    };
  }

  render() {
    const {
      button,
      children: childrenProp,
      classes,
      className: classNameProp,
      component: componentProp,
      ContainerComponent,
      ContainerProps: { className: ContainerClassName, ...ContainerProps } = {},
      dense,
      disabled,
      disableGutters,
      divider,
      ...other
    } = this.props;

    const isDense = dense || this.context.dense || false;
    const children = React.Children.toArray(childrenProp);
    const hasAvatar = children.some(value => isMuiElement(value, ['ListItemAvatar']));
    const hasSecondaryAction =
      children.length && isMuiElement(children[children.length - 1], ['ListItemSecondaryAction']);

    const className = classNames(
      classes.root,
      isDense || hasAvatar ? classes.dense : classes.default,
      {
        [classes.gutters]: !disableGutters,
        [classes.divider]: divider,
        [classes.disabled]: disabled,
        [classes.button]: button,
        [classes.secondaryAction]: hasSecondaryAction,
      },
      classNameProp,
    );

    const componentProps = { className, disabled, ...other };
    let Component = componentProp || 'li';

    if (button) {
      componentProps.component = componentProp || 'div';
      componentProps.focusVisibleClassName = classes.focusVisible;
      Component = ButtonBase;
    }

    if (hasSecondaryAction) {
      // Use div by default.
      Component = !componentProps.component && !componentProp ? 'div' : Component;

      // Avoid nesting of li > li.
      if (ContainerComponent === 'li') {
        if (Component === 'li') {
          Component = 'div';
        } else if (componentProps.component === 'li') {
          componentProps.component = 'div';
        }
      }

      return (
        <ContainerComponent
          className={classNames(classes.container, ContainerClassName)}
          {...ContainerProps}
        >
          <Component {...componentProps}>{children}</Component>
          {children.pop()}
        </ContainerComponent>
      );
    }

    return <Component {...componentProps}>{children}</Component>;
  }
}

ListItem.propTypes = {
  /**
   * If `true`, the list item will be a button (using `ButtonBase`).
   */
  button: PropTypes.bool,
  /**
   * The content of the component.
   */
  children: PropTypes.node,
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
   * The component used for the root node.
   * Either a string to use a DOM element or a component.
   * By default, it's a `li` when `button` is `false` and a `div` when `button` is `true`.
   */
  component: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
  /**
   * The container component used when a `ListItemSecondaryAction` is rendered.
   */
  ContainerComponent: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
  /**
   * Properties applied to the container element when the component
   * is used to display a `ListItemSecondaryAction`.
   */
  ContainerProps: PropTypes.object,
  /**
   * If `true`, compact vertical padding designed for keyboard and mouse input will be used.
   */
  dense: PropTypes.bool,
  /**
   * @ignore
   */
  disabled: PropTypes.bool,
  /**
   * If `true`, the left and right padding is removed.
   */
  disableGutters: PropTypes.bool,
  /**
   * If `true`, a 1px light border is added to the bottom of the list item.
   */
  divider: PropTypes.bool,
};

ListItem.defaultProps = {
  button: false,
  ContainerComponent: 'li',
  dense: false,
  disabled: false,
  disableGutters: false,
  divider: false,
};

ListItem.contextTypes = {
  dense: PropTypes.bool,
};

ListItem.childContextTypes = {
  dense: PropTypes.bool,
};

export default withStyles(styles, { name: 'MuiListItem' })(ListItem);
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-11451/repo; grep -n -i "focusVisible" -r packages/material-ui/src/ListItem packages/material-ui/src/MenuItem; git log --oneline -2
```

tool result:

```
packages/material-ui/src/ListItem/ListItem.js:22:  focusVisible: {
packages/material-ui/src/ListItem/ListItem.js:108:      componentProps.focusVisibleClassName = classes.focusVisible;
packages/material-ui/src/ListItem/ListItem.d.ts:24:  | 'focusVisible'
04fae47c2 [BACKERS] Add 3 new backers :)
8667b66ba [docs] Specify correct corner to locate directional toggle (#11479)
```

**assistant:** Root cause: `ListItem` takes `focusVisibleClassName` from `...other`, but then overwrites it with `classes.focusVisible` when `button` is true. Let me reproduce.

**tool call: Bash**

```bash
cd /work/mui__material-ui-11451/repo; cat > packages/material-ui/src/ListItem/repro.test.js <<'EOF'
import React from 'react';
import { assert } from 'chai';
import { createShallow, getClasses } from '../test-utils';
import ListItem from './ListItem';
import MenuItem from '../MenuItem';

describe('repro', () => {
  it('merges focusVisibleClassName', () => {
    const shallow = createShallow({ dive: true });
    const classes = getClasses(<ListItem />);
    const wrapper = shallow(<ListItem button focusVisibleClassName="foo" />);
    const fv = wrapper.props().focusVisibleClassName;
    assert.include(fv, 'foo');
    assert.include(fv, classes.focusVisible);
  });
});
EOF
../bin/envrun 'cat package.json | grep -n "\"test' ; NODE_ENV=test npx mocha --require @babel/register packages/material-ui/src/ListItem/repro.test.js 2>&1 | tail -20' 
```

tool result:

```
Exit code 1
(eval):19: unmatched '
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-11451/repo; grep -n '"test' package.json
```

tool result:

```
41:    "test": "yarn lint && yarn flow && yarn typescript && yarn test:unit",
42:    "test:unit": "cross-env NODE_ENV=test mocha packages/material-ui/test/**/*.test.js packages/material-ui/src/{,**/}*.test.js docs/src/**/*.test.js",
43:    "test:watch": "yarn test:unit --watch",
44:    "test:coverage": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha packages/material-ui/test/**/*.test.js packages/material-ui/src/{,**/}*.test.js && nyc report -r lcovonly",
45:    "test:coverage:html": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha packages/material-ui/test/**/*.test.js packages/material-ui/src/{,**/}*.test.js && nyc report --reporter=html",
46:    "test:karma": "cross-env NODE_ENV=test karma start test/karma.conf.js --single-run",
47:    "test:regressions": "webpack --config test/regressions/webpack.config.js && rimraf test/regressions/screenshots/chrome/* && vrtest run --config test/vrtest.config.js --record",
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-11451/repo; ../bin/envrun 'NODE_ENV=test npx mocha packages/material-ui/src/ListItem/repro.test.js 2>&1 | tail -20'
```

tool result:

```
Warning: Could not find any test files matching pattern: packages/material-ui/src/ListItem/repro.test.js



  0 passing (0ms)
```

**assistant:** The earlier zsh parse error meant the file was never written; recreating it.

**tool call: Write**

```json
{
 "file_path": "/work/mui__material-ui-11451/repo/packages/material-ui/src/ListItem/repro.test.js",
 "content": "import React from 'react';\nimport { assert } from 'chai';\nimport { createShallow, getClasses } from '../test-utils';\nimport ListItem from './ListItem';\n\ndescribe('repro', () => {\n  it('merges focusVisibleClassName', () => {\n    const shallow = createShallow({ dive: true });\n    const classes = getClasses(<ListItem />);\n    const wrapper = shallow(<ListItem button focusVisibleClassName=\"foo\" />);\n    const fv = wrapper.props().focusVisibleClassName;\n    assert.include(fv, 'foo');\n    assert.include(fv, classes.focusVisible);\n  });\n});\n"
}
```

tool result:

```
File created successfully at: /work/mui__material-ui-11451/repo/packages/material-ui/src/ListItem/repro.test.js (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-11451/repo; ../bin/envrun 'NODE_ENV=test npx mocha packages/material-ui/src/ListItem/repro.test.js 2>&1 | tail -20'
```

tool result:

```
  !

  0 passing (48ms)
  1 failing

  1) repro
       merges focusVisibleClassName:
     AssertionError: expected 'MuiListItem-focusVisible-3' to include 'foo'
      at Context.<anonymous> (packages/material-ui/src/ListItem/repro.test.js:12:12)
      at processImmediate (node:internal/timers:466:21)
```

**assistant:** Confirmed. Now the fix:

**tool call: Bash**

```bash
cd /work/mui__material-ui-11451/repo; python3 - <<'EOF'
p='packages/material-ui/src/ListItem/ListItem.js'
s=open(p).read()
s=s.replace("""      divider,
      ...other
    } = this.props;""","""      divider,
      focusVisibleClassName,
      ...other
    } = this.props;""")
s=s.replace("componentProps.focusVisibleClassName = classes.focusVisible;","componentProps.focusVisibleClassName = classNames(classes.focusVisible, focusVisibleClassName);")
s=s.replace("""  divider: PropTypes.bool,
};""","""  divider: PropTypes.bool,
  /**
   * @ignore
   */
  focusVisibleClassName: PropTypes.string,
};""")
open(p,'w').write(s)
EOF
git diff; sed -n 1,40p packages/material-ui/src/ListItem/ListItem.d.ts
```

tool result:

```
diff --git a/package.json b/package.json
index 58947d775..2fe2c3d6e 100644
--- a/package.json
+++ b/package.json
@@ -66,8 +66,14 @@
     "@babel/preset-react": "7.0.0-beta.42",
     "@babel/preset-stage-1": "7.0.0-beta.42",
     "@babel/register": "7.0.0-beta.42",
+    "@types/chai": "^5.2.3",
+    "@types/chai-dom": "^1.11.3",
     "@types/enzyme": "^3.1.4",
+    "@types/format-util": "^1.0.4",
+    "@types/prop-types": "^15.7.15",
     "@types/react": "^16.3.14",
+    "@types/react-dom": "^19.2.3",
+    "@types/sinon": "^21.0.0",
     "argos-cli": "^0.0.9",
     "autoprefixer": "^8.0.0",
     "autosuggest-highlight": "^3.1.1",
diff --git a/packages/material-ui/src/ListItem/ListItem.js b/packages/material-ui/src/ListItem/ListItem.js
index 991895770..8f1415280 100644
--- a/packages/material-ui/src/ListItem/ListItem.js
+++ b/packages/material-ui/src/ListItem/ListItem.js
@@ -78,6 +78,7 @@ class ListItem extends React.Component {
       disabled,
       disableGutters,
       divider,
+      focusVisibleClassName,
       ...other
     } = this.props;
 
@@ -105,7 +106,7 @@ class ListItem extends React.Component {
 
     if (button) {
       componentProps.component = componentProp || 'div';
-      componentProps.focusVisibleClassName = classes.focusVisible;
+      componentProps.focusVisibleClassName = classNames(classes.focusVisible, focusVisibleClassName);
       Component = ButtonBase;
     }
 
@@ -186,6 +187,10 @@ ListItem.propTypes = {
    * If `true`, a 1px light border is added to the bottom of the list item.
    */
   divider: PropTypes.bool,
+  /**
+   * @ignore
+   */
+  focusVisibleClassName: PropTypes.string,
 };
 
 ListItem.defaultProps = {
diff --git a/yarn.lock b/yarn.lock
index b0540b417..24f3384da 100644
--- a/yarn.lock
+++ b/yarn.lock
@@ -937,10 +937,30 @@
   dependencies:
     samsam "1.3.0"
 
+"@types/chai-dom@^1.11.3":
+  version "1.11.3"
+  resolved "https://registry.yarnpkg.com/@types/chai-dom/-/chai-dom-1.11.3.tgz#1659ace2698cdcd9ed8b2c007876f53e37d9cc89"
+  integrity sha512-EUEZI7uID4ewzxnU7DJXtyvykhQuwe+etJ1wwOiJyQRTH/ifMWKX+ghiXkxCUvNJ6IQDodf0JXhuP6zZcy2qXQ==
+  dependencies:
+    "@types/chai" "*"
+
+"@types/chai@*", "@types/chai@^5.2.3":
+  version "5.2.3"
+  resolved "https://registry.yarnpkg.com/@types/chai/-/chai-5.2.3.tgz#8e9cd9e1c3581fa6b341a5aed5588eb285be0b4a"
+  integrity sha512-Mw558oeA9fFbv65/y4mHtXDs9bPnFMZAL/jxdPFUpOHHIXX91mcgEHbS5Lahr+pwZFR8A7GQleRWeI6cGFC2UA==
+  dependencies:
+    "@types/deep-eql" "*"
+    assertion-error "^2.0.1"
+
 "@types/cheerio@*":
   version "0.22.7"
   resolved "https://registry.yarnpkg.com/@types/cheerio/-/cheerio-0.22.7.tgz#4a92eafedfb2b9f4437d3a4410006d81114c66ce"
 
+"@types/deep-eql@*":
+  version "4.0.2"
+  resolved "https://registry.yarnpkg.com/@types/deep-eql/-/deep-eql-4.0.2.tgz#334311971d3a07121e7eb91b684a605e7eea9cbd"
+  integrity sha512-c9h9dVVMigMPc4bwTvC5dxqtqJZwQPePsWjPlpSOnojbor6pGqdk541lfA7AqFQr5pB1BRdq0juY9db81BwyFw==
+
 "@types/enzyme@^3.1.4":
   version "3.1.10"
   resolved "https://registry.yarnpkg.com/@types/enzyme/-/enzyme-3.1.10.tgz#28108a9864e65699751469551a803a35d2e26160"
@@ -956,6 +976,11 @@
   version "1.2.0"
   resolved "https://registry.yarnpkg.com/@types/events/-/events-1.2.0.tgz#81a6731ce4df43619e5c8c945383b3e62a89ea86"
 
+"@types/format-util@^1.0.4":
+  version "1.0.4"
+  resolved "https://registry.yarnpkg.com/@types/format-util/-/format-util-1.0.4.tgz#c4e3b556735149fdf047898a5b9c04650491509b"
+  integrity sha512-xrCYOdHh5zA3LUrn6CvspYwlzSWxPso11Lx32WnAG6KvLCRecKZ/Rh21PLXUkzUFsQmrGcx/traJAFjR6dVS5Q==
+
 "@types/glob@*":
   version "5.0.35"
   resolved "https://registry.yarnpkg.com/@types/glob/-/glob-5.0.35.tgz#1ae151c802cece940443b5ac246925c85189f32a"
@@ -979,6 +1004,16 @@
   version "10.0.10"
   resolved "https://registry.yarnpkg.com/@types/node/-/node-10.0.10.tgz#7f4667269e086daeef8667069f9f2cd862f49eb7"
 
+"@types/prop-types@^15.7.15":
+  version "15.7.15"
+  resolved "https://registry.yarnpkg.com/@types/prop-types/-/prop-types-15.7.15.tgz#e6e5a86d602beaca71ce5163fadf5f95d70931c7"
+  integrity sha512-F6bEyamV9jKGAFBEmlQnesRPGOQqS2+Uwi0Em15xenOxHaf2hv6L8YCVn3rPdPJOiJfPiCnLIRyvwVaqMY3MIw==
+
+"@types/react-dom@^19.2.3":
+  version "19.2.3"
+  resolved "https://registry.yarnpkg.com/@types/react-dom/-/react-dom-19.2.3.tgz#c1e305d15a52a3e508d54dca770d202cb63abf2c"
+  integrity sha512-jp2L/eY6fn+KgVVQAOqYItbF0VY/YApe5Mz2F0aykSO8gx31bYCZyvSeYxCHKvzHG5eZjc+zyaS5BrBWya2+kQ==
+
 "@types/react-transition-group@^2.0.8":
   version "2.0.9"
   resolved "https://registry.yarnpkg.com/@types/react-transition-group/-/react-transition-group-2.0.9.tgz#ed6a71fb711e524345844defec2a861c1a222a03"
@@ -991,6 +1026,18 @@
   dependencies:
     csstype "^2.2.0"
 
+"@types/sinon@^21.0.0":
+  version "21.0.0"
+  resolved "https://registry.yarnpkg.com/@types/sinon/-/sinon-21.0.0.tgz#3a598a29b3aec0512a21e57ae0fd4c09aa013ca9"
+  integrity sha512-+oHKZ0lTI+WVLxx1IbJDNmReQaIsQJjN2e7UUrJHEeByG7bFeKJYsv1E75JxTQ9QKJDp21bAa/0W2Xo4srsDnw==
+  dependencies:
+    "@types/sinonjs__fake-timers" "*"
+
+"@types/sinonjs__fake-timers@*":
+  version "15.0.1"
+  resolved "https://registry.yarnpkg.com/@types/sinonjs__fake-timers/-/sinonjs__fake-timers-15.0.1.tgz#49f731d9453f52d64dd79f5a5626c1cf1b81bea4"
+  integrity sha512-Ko2tjWJq8oozHzHV+reuvS5KYIRAokHnGbDwGh/J64LntgpbuylF74ipEL24HCyRjf9FOlBiBHWBR1RlVKsI1w==
+
 "@webassemblyjs/ast@1.4.3":
   version "1.4.3"
   resolved "https://registry.yarnpkg.com/@webassemblyjs/ast/-/ast-1.4.3.tgz#3b3f6fced944d8660273347533e6d4d315b5934a"
@@ -1470,6 +1517,11 @@ assertion-error@^1.0.1:
   version "1.1.0"
   resolved "https://registry.yarnpkg.com/assertion-error/-/assertion-error-1.1.0.tgz#e60b6b0e8f301bd97e5375215bda406c85118c0b"
 
+assertion-error@^2.0.1:
+  version "2.0.1"
+  resolved "https://registry.yarnpkg.com/assertion-error/-/assertion-error-2.0.1.tgz#f641a196b335690b1070bf00b6e7593fec190bf7"
+  integrity sha512-Izi8RQcffqCeNVgFigKli1ssklIbpHnCYc6AknXGYoB6grJqyeby7jv12JUQgmTAnIDnbck1uxksT4dzN3PWB
[... 1022 more characters not shown]
```

**assistant:** The `package.json`/`yarn.lock` changes aren't mine, so I'm leaving them alone. Typings already cover the prop via `ButtonBaseProps`. Next I'll run the repro, the nearby tests, and lint/prettier.

**tool call: Bash**

```bash
cd /work/mui__material-ui-11451/repo; ../bin/envrun 'NODE_ENV=test npx mocha packages/material-ui/src/ListItem/*.test.js packages/material-ui/src/MenuItem/*.test.js packages/material-ui/src/Menu/*.test.js packages/material-ui/src/ListItem/repro.test.js 2>&1 | tail -15; npx eslint packages/material-ui/src/ListItem/ListItem.js && npx prettier --list-different packages/material-ui/src/ListItem/ListItem.js; echo done'
```

tool result:

```
  ․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․

  43 passing (340ms)


/testbed/packages/material-ui/src/ListItem/ListItem.js
  109:1   error  Line 109 exceeds the maximum line length of 100                                                                                    max-len
  109:57  error  Replace `classes.focusVisible,·focusVisibleClassName` with `⏎········classes.focusVisible,⏎········focusVisibleClassName,⏎······`  prettier/prettier

✖ 2 problems (2 errors, 0 warnings)
  1 error, 0 warnings potentially fixable with the `--fix` option.

done
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-11451/repo; rm packages/material-ui/src/ListItem/repro.test.js; ../bin/envrun 'npx prettier --write packages/material-ui/src/ListItem/ListItem.js && npx eslint packages/material-ui/src/ListItem/ListItem.js && NODE_ENV=test npx mocha packages/material-ui/src/ListItem/*.test.js packages/material-ui/src/MenuItem/*.test.js 2>&1 | tail -3'; git status --short; git diff packages/
```

tool result:

```
packages/material-ui/src/ListItem/ListItem.js 135ms

  23 passing (261ms)


 M package.json
 M packages/material-ui/src/ListItem/ListItem.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
diff --git a/packages/material-ui/src/ListItem/ListItem.js b/packages/material-ui/src/ListItem/ListItem.js
index 991895770..12d5049ad 100644
--- a/packages/material-ui/src/ListItem/ListItem.js
+++ b/packages/material-ui/src/ListItem/ListItem.js
@@ -78,6 +78,7 @@ class ListItem extends React.Component {
       disabled,
       disableGutters,
       divider,
+      focusVisibleClassName,
       ...other
     } = this.props;
 
@@ -105,7 +106,10 @@ class ListItem extends React.Component {
 
     if (button) {
       componentProps.component = componentProp || 'div';
-      componentProps.focusVisibleClassName = classes.focusVisible;
+      componentProps.focusVisibleClassName = classNames(
+        classes.focusVisible,
+        focusVisibleClassName,
+      );
       Component = ButtonBase;
     }
 
@@ -186,6 +190,10 @@ ListItem.propTypes = {
    * If `true`, a 1px light border is added to the bottom of the list item.
    */
   divider: PropTypes.bool,
+  /**
+   * @ignore
+   */
+  focusVisibleClassName: PropTypes.string,
 };
 
 ListItem.defaultProps = {
```

**assistant:** `MenuItem` now applies the `focusVisibleClassName` you pass it. The bug was in `ListItem`, which `MenuItem` renders through: when `button` was true, `ListItem` replaced any `focusVisibleClassName` it received with its own `classes.focusVisible`, so the user's class was thrown away.

**Fix** (`packages/material-ui/src/ListItem/ListItem.js`):
- `ListItem` now takes `focusVisibleClassName` out of the props separately and merges it with its own class: `classNames(classes.focusVisible, focusVisibleClassName)`. The default focus style still applies, and the user's class is added on top.
- I added an `@ignore` propTypes entry for it. The TypeScript types didn't need changing, since `ListItemProps` already gets the prop from `ButtonBaseProps`.
- When `button` is false there's no `ButtonBase`, so the prop is now dropped instead of being passed through to a plain `<li>`, where React would warn about an unknown attribute.

**Testing:**
- A temporary test showed the bug: the result was `'MuiListItem-focusVisible-3'` with `'foo'` missing. After the fix it passed, and I then deleted it.
- The existing `ListItem`, `MenuItem` and `Menu` tests pass (43 in total).
- ESLint and Prettier are clean. Prettier split the new line because it went over the 100-character limit.

`package.json`, `yarn.lock`, `Dockerfile` and `custom-reporter.js` show as modified or untracked in the repo, but I didn't change them. They look like they came from setting up the environment, so I left them as they were.

_session end: success, turns 12, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 2.62 s: NODE_ENV=test npx mocha packages/material-ui/src/ListItem/repro.test.js 2>&1 | tail -20
- `rc=0` 4.33 s: NODE_ENV=test npx mocha packages/material-ui/src/ListItem/repro.test.js 2>&1 | tail -20
- `rc=0` 8.7 s: NODE_ENV=test npx mocha packages/material-ui/src/ListItem/*.test.js packages/material-ui/src/MenuItem/*.test.js packages/material-ui/src/Menu/*.test.js packages/material-ui/src/ListItem/repro.test.js 2>&1 | tail -15; npx eslint packages/material-ui/src/ListItem/ListItem.js && npx prettier --list-different packages/material-ui/src/ListItem/ListItem.js; echo done
- `rc=0` 6.69 s: npx prettier --write packages/material-ui/src/ListItem/ListItem.js && npx eslint packages/material-ui/src/ListItem/ListItem.js && NODE_ENV=test npx mocha packages/material-ui/src/ListItem/*.test.js packages/material-ui/src/MenuItem/*.test.js 2>&1 | tail -3
