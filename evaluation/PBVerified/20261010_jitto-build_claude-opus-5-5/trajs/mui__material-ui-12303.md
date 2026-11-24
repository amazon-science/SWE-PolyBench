# Instance: mui__material-ui-12303

- Final resolved (evaluator, logs/mui__material-ui-12303_result.json): False
- Run state: DONE
- One attempt. Duration 50.3 s, turns 10, actor cost $0.19796999999999998, container commands 5
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/mui__material-ui-12303/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-12303/repo. Consider the following issue description:

<issue_description>
How to position Switch label to the left of the switch?
- [x] This is a v1.x issue (v0.x is no longer maintained).
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

[The examples here](https://material-ui.com/demos/selection-controls/) demonstrate how to add a label to various forms of input, including the `Switch` component.

Unfortunately, every single example on that page that includes a label has it positioned to the right of the component. I've looked through the props of `FormControlLabel`, and there doesn't seem to be any option that allows me to change this. In fact, looking at the code of `FormControlLabel`, it seems to be hard-coded his way.

I was able to work around this by setting the Label's direction to rtl (and setting the Switch's direction back to ltr):
```
import React from "react";
import styled from "react-emotion";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import Switch from "@material-ui/core/Switch";

const StyledLabel = styled(FormControlLabel)`
  direction: ${({ rtl }) => rtl && "rtl"};
  margin: 0;
`;

const StyledSwitch = styled(Switch)`
  direction: ltr;
`;

export default ({ label, rtl, ...props }) => (
  <StyledLabel rtl={rtl} control={<StyledSwitch {...props} />} label={label} />
);
```
But this feels very hacky and potentially unstable to me.

Is there any way I can have a `Switch` with its label on the left without resorting to `rtl` hacks? If so, can it please be documented? If not, please consider this a feature request.

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-12303/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-12303/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-12303/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-12303/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/mui__material-ui-12303/repo/packages/material-ui/src/FormControlLabel && ls && cat FormControlLabel.js FormControlLabel.d.ts
```

tool result:

```
FormControlLabel.d.ts
FormControlLabel.js
FormControlLabel.test.js
index.d.ts
index.js
/* eslint-disable jsx-a11y/label-has-for */

import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import withStyles from '../styles/withStyles';
import Typography from '../Typography';

export const styles = theme => ({
  /* Styles applied to the root element. */
  root: {
    display: 'inline-flex',
    alignItems: 'center',
    cursor: 'pointer',
    // For correct alignment with the text.
    verticalAlign: 'middle',
    // Remove grey highlight
    WebkitTapHighlightColor: 'transparent',
    marginLeft: -14,
    marginRight: 16, // used for row presentation of radio/checkbox
    '&$disabled': {
      cursor: 'default',
    },
  },
  /* Styles applied to the root element if `disabled={true}`. */
  disabled: {},
  /* Styles applied to the label's Typography component. */
  label: {
    '&$disabled': {
      color: theme.palette.text.disabled,
    },
  },
});

/**
 * Drop in replacement of the `Radio`, `Switch` and `Checkbox` component.
 * Use this component if you want to display an extra label.
 */
function FormControlLabel(props, context) {
  const {
    checked,
    classes,
    className: classNameProp,
    control,
    disabled: disabledProp,
    inputRef,
    label,
    name,
    onChange,
    value,
    ...other
  } = props;
  const { muiFormControl } = context;

  let disabled = disabledProp;
  if (typeof disabled === 'undefined' && typeof control.props.disabled !== 'undefined') {
    disabled = control.props.disabled;
  }
  if (typeof disabled === 'undefined' && muiFormControl) {
    disabled = muiFormControl.disabled;
  }

  const controlProps = {
    disabled,
  };
  ['checked', 'name', 'onChange', 'value', 'inputRef'].forEach(key => {
    if (typeof control.props[key] === 'undefined' && typeof props[key] !== 'undefined') {
      controlProps[key] = props[key];
    }
  });

  return (
    <label
      className={classNames(
        classes.root,
        {
          [classes.disabled]: disabled,
        },
        classNameProp,
      )}
      {...other}
    >
      {React.cloneElement(control, controlProps)}
      <Typography
        component="span"
        className={classNames(classes.label, { [classes.disabled]: disabled })}
      >
        {label}
      </Typography>
    </label>
  );
}

FormControlLabel.propTypes = {
  /**
   * If `true`, the component appears selected.
   */
  checked: PropTypes.oneOfType([PropTypes.bool, PropTypes.string]),
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
   * A control element. For instance, it can be be a `Radio`, a `Switch` or a `Checkbox`.
   */
  control: PropTypes.element,
  /**
   * If `true`, the control will be disabled.
   */
  disabled: PropTypes.bool,
  /**
   * Use that property to pass a ref callback to the native input component.
   */
  inputRef: PropTypes.oneOfType([PropTypes.func, PropTypes.object]),
  /**
   * The text to be used in an enclosing label element.
   */
  label: PropTypes.node,
  /*
   * @ignore
   */
  name: PropTypes.string,
  /**
   * Callback fired when the state is changed.
   *
   * @param {object} event The event source of the callback.
   * You can pull out the new value by accessing `event.target.checked`.
   * @param {boolean} checked The `checked` value of the switch
   */
  onChange: PropTypes.func,
  /**
   * The value of the component.
   */
  value: PropTypes.string,
};

FormControlLabel.contextTypes = {
  muiFormControl: PropTypes.object,
};

export default withStyles(styles, { name: 'MuiFormControlLabel' })(FormControlLabel);
import * as React from 'react';
import { StandardProps } from '..';

export interface FormControlLabelProps
  extends StandardProps<
      React.LabelHTMLAttributes<HTMLLabelElement>,
      FormControlLabelClassKey,
      'onChange'
    > {
  checked?: boolean | string;
  control: React.ReactElement<any>;
  disabled?: boolean;
  inputRef?: React.Ref<any>;
  label: React.ReactNode;
  name?: string;
  onChange?: (event: React.ChangeEvent<{}>, checked: boolean) => void;
  value?: string;
}

export type FormControlLabelClassKey = 'root' | 'disabled' | 'label';

declare const FormControlLabel: React.ComponentType<FormControlLabelProps>;

export default FormControlLabel;
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-12303/repo && grep -n -i "labelPlacement\|start\|placement" -r packages/material-ui/src/FormControlLabel/ docs/src/pages/demos/selection-controls/*.js | head -30
```

tool result:

```
packages/material-ui/src/FormControlLabel/FormControlLabel.js:36: * Drop in replacement of the `Radio`, `Switch` and `Checkbox` component.
```

**assistant:** Upstream MUI handled this with a `labelPlacement` prop (`'end' | 'start'`) and a `labelPlacementStart` class. I'll add the same.

**tool call: Bash**

```bash
cd /work/mui__material-ui-12303/repo/packages/material-ui/src/FormControlLabel && python3 - <<'EOF'
p='FormControlLabel.js'
s=open(p).read()
s=s.replace("""  /* Styles applied to the root element if `disabled={true}`. */
  disabled: {},""","""  /* Styles applied to the root element if `labelPlacement="start"`. */
  labelPlacementStart: {
    flexDirection: 'row-reverse',
    marginLeft: 16, // used for row presentation of radio/checkbox
    marginRight: -14,
  },
  /* Styles applied to the root element if `disabled={true}`. */
  disabled: {},""")
s=s.replace("""    label,
    name,""","""    label,
    labelPlacement,
    name,""")
s=s.replace("""        {
          [classes.disabled]: disabled,
        },""","""        {
          [classes.labelPlacementStart]: labelPlacement === 'start',
          [classes.disabled]: disabled,
        },""")
s=s.replace("""  label: PropTypes.node,
  /*""","""  label: PropTypes.node,
  /**
   * The position of the label.
   */
  labelPlacement: PropTypes.oneOf(['end', 'start']),
  /*""")
s=s.replace("""FormControlLabel.contextTypes""","""FormControlLabel.defaultProps = {
  labelPlacement: 'end',
};

FormControlLabel.contextTypes""")
open(p,'w').write(s)
p='FormControlLabel.d.ts'
s=open(p).read()
s=s.replace("""  label: React.ReactNode;
""","""  label: React.ReactNode;
  labelPlacement?: 'end' | 'start';
""")
s=s.replace("'root' | 'disabled' | 'label'","'root' | 'labelPlacementStart' | 'disabled' | 'label'")
open(p,'w').write(s)
EOF
git diff --stat; grep -rln "FormControlLabel" ../../../../pages/api/ 2>/dev/null
```

tool result:

```
 package.json                                       |  6 +++
 .../src/FormControlLabel/FormControlLabel.d.ts     |  3 +-
 .../src/FormControlLabel/FormControlLabel.js       | 16 +++++++
 yarn.lock                                          | 52 ++++++++++++++++++++++
 4 files changed, 76 insertions(+), 1 deletion(-)
../../../../pages/api/form-control-label.md
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-12303/repo && sed -n 1,200p pages/api/form-control-label.md; ls docs/src/pages/demos/selection-controls/
```

tool result:

```
---
filename: /packages/material-ui/src/FormControlLabel/FormControlLabel.js
title: FormControlLabel API
---

<!--- This documentation is automatically generated, do not try to edit it. -->

# FormControlLabel

<p class="description">The API documentation of the FormControlLabel React component.</p>

Drop in replacement of the `Radio`, `Switch` and `Checkbox` component.
Use this component if you want to display an extra label.

## Props

| Name | Type | Default | Description |
|:-----|:-----|:--------|:------------|
| <span class="prop-name">checked</span> | <span class="prop-type">union:&nbsp;bool&nbsp;&#124;<br>&nbsp;string<br> |   | If `true`, the component appears selected. |
| <span class="prop-name">classes</span> | <span class="prop-type">object |   | Override or extend the styles applied to the component. See [CSS API](#css-api) below for more details. |
| <span class="prop-name">control</span> | <span class="prop-type">element |   | A control element. For instance, it can be be a `Radio`, a `Switch` or a `Checkbox`. |
| <span class="prop-name">disabled</span> | <span class="prop-type">bool |   | If `true`, the control will be disabled. |
| <span class="prop-name">inputRef</span> | <span class="prop-type">union:&nbsp;func&nbsp;&#124;<br>&nbsp;object<br> |   | Use that property to pass a ref callback to the native input component. |
| <span class="prop-name">label</span> | <span class="prop-type">node |   | The text to be used in an enclosing label element. |
| <span class="prop-name">name</span> | <span class="prop-type">string |   |  |
| <span class="prop-name">onChange</span> | <span class="prop-type">func |   | Callback fired when the state is changed.<br><br>**Signature:**<br>`function(event: object, checked: boolean) => void`<br>*event:* The event source of the callback. You can pull out the new value by accessing `event.target.checked`.<br>*checked:* The `checked` value of the switch |
| <span class="prop-name">value</span> | <span class="prop-type">string |   | The value of the component. |

Any other properties supplied will be spread to the root element (native element).

## CSS API

You can override all the class names injected by Material-UI thanks to the `classes` property.
This property accepts the following keys:


| Name | Description |
|:-----|:------------|
| <span class="prop-name">root</span> | Styles applied to the root element.
| <span class="prop-name">disabled</span> | Styles applied to the root element if `disabled={true}`.
| <span class="prop-name">label</span> | Styles applied to the label's Typography component.

Have a look at [overriding with classes](/customization/overrides#overriding-with-classes) section
and the [implementation of the component](https://github.com/mui-org/material-ui/tree/master/packages/material-ui/src/FormControlLabel/FormControlLabel.js)
for more detail.

If using the `overrides` key of the theme as documented
[here](/customization/themes#customizing-all-instances-of-a-component-type),
you need to use the following style sheet name: `MuiFormControlLabel`.

## Demos

- [Selection Controls](/demos/selection-controls)

CheckboxLabels.js
Checkboxes.js
CheckboxesGroup.js
CustomizedSwitches.js
RadioButtons.js
RadioButtonsGroup.js
SwitchLabels.js
Switches.js
SwitchesGroup.js
selection-controls.md
```

**assistant:** `package.json` and `yarn.lock` were already modified by the environment setup, so I'm leaving them alone. Next I'll update the generated API doc by hand:

**tool call: Bash**

```bash
python3 - <<'EOF'
p='pages/api/form-control-label.md'
s=open(p).read()
s=s.replace("""The text to be used in an enclosing label element. |
""","""The text to be used in an enclosing label element. |
| <span class="prop-name">labelPlacement</span> | <span class="prop-type">enum:&nbsp;'end'&nbsp;&#124;<br>&nbsp;'start'<br> | <span class="prop-default">'end'</span> | The position of the label. |
""")
s=s.replace("""| <span class="prop-name">disabled</span> | Styles applied to the root element if `disabled={true}`.""","""| <span class="prop-name">labelPlacementStart</span> | Styles applied to the root element if `labelPlacement="start"`.
| <span class="prop-name">disabled</span> | Styles applied to the root element if `disabled={true}`.""")
open(p,'w').write(s)
EOF
grep -n "prop-default" pages/api/*.md | head -2
cat > /tmp/x.test.js <<'EOF'
EOF
cat > packages/material-ui/src/FormControlLabel/repro.test.js <<'EOF'
import React from 'react';
import { assert } from 'chai';
import { createShallow, getClasses } from '../test-utils';
import FormControlLabel from './FormControlLabel';
describe('repro', () => {
  it('start class', () => {
    const shallow = createShallow({ dive: true });
    const classes = getClasses(<FormControlLabel label="Pizza" control={<div />} />);
    const w = shallow(<FormControlLabel label="Pizza" labelPlacement="start" control={<div />} />);
    assert.strictEqual(w.hasClass(classes.labelPlacementStart), true);
    const w2 = shallow(<FormControlLabel label="Pizza" control={<div />} />);
    assert.strictEqual(w2.hasClass(classes.labelPlacementStart), false);
  });
});
EOF
../bin/envrun 'yarn -s mocha packages/material-ui/src/FormControlLabel/*.test.js 2>&1 | tail -30'
```

tool result:

```
pages/api/app-bar.md:20:| <span class="prop-name">color</span> | <span class="prop-type">enum:&nbsp;'inherit'&nbsp;&#124;<br>&nbsp;'primary'&nbsp;&#124;<br>&nbsp;'secondary'&nbsp;&#124;<br>&nbsp;'default'<br> | <span class="prop-default">'primary'</span> | The color of the component. It supports those theme colors that make sense for this component. |
pages/api/app-bar.md:21:| <span class="prop-name">position</span> | <span class="prop-type">enum:&nbsp;'fixed'&nbsp;&#124;<br>&nbsp;'absolute'&nbsp;&#124;<br>&nbsp;'sticky'&nbsp;&#124;<br>&nbsp;'static'<br> | <span class="prop-default">'fixed'</span> | The positioning type. The behavior of the different options is described [here](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Positioning). Note: `sticky` is not universally supported and will fall back to `static` when unavailable. |
(eval):13: operation not permitted: /tmp/x.test.js
warning You don't appear to have an internet connection. Try the --offline flag to use the cache for registry queries.


  ․․․․․․․․․․․

  11 passing (185ms)
```

**assistant:** All 11 tests pass, including the repro. Now I'll remove the repro and run lint and the TypeScript check:

**tool call: Bash**

```bash
rm packages/material-ui/src/FormControlLabel/repro.test.js; ../bin/envrun 'npx eslint packages/material-ui/src/FormControlLabel && npx tsc -p packages/material-ui 2>&1 | tail -5; echo done'; git status --short
```

tool result:

```
(node:62) [ESLINT_LEGACY_OBJECT_REST_SPREAD] DeprecationWarning: The 'parserOptions.ecmaFeatures.experimentalObjectRestSpread' option is deprecated. Use 'parserOptions.ecmaVersion' instead. (found in "node_modules/eslint-config-airbnb-base/index.js")
(Use `node --trace-deprecation ...` to show where the warning was created)
error TS5057: Cannot find a tsconfig.json file at the specified directory: 'packages/material-ui'.
done

 M package.json
 M packages/material-ui/src/FormControlLabel/FormControlLabel.d.ts
 M packages/material-ui/src/FormControlLabel/FormControlLabel.js
 M pages/api/form-control-label.md
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
```

**tool call: Bash**

```bash
ls tsconfig*.json; ../bin/envrun 'npx tsc -p tsconfig.json --noEmit 2>&1 | tail -5; echo rc=$?'
```

tool result:

```
tsconfig.json
node_modules/@types/sinon/index.d.ts(1277,9): error TS1128: Declaration or statement expected.
node_modules/@types/sinon/index.d.ts(1277,10): error TS1128: Declaration or statement expected.
node_modules/@types/sinon/index.d.ts(1277,41): error TS1005: '(' expected.
node_modules/@types/sinon/index.d.ts(1278,5): error TS1128: Declaration or statement expected.
node_modules/@types/sinon/index.d.ts(1460,1): error TS1128: Declaration or statement expected.
rc=0
```

**tool call: Bash**

```bash
../bin/envrun 'npx tsc -p tsconfig.json --noEmit 2>&1 | grep -v node_modules/@types/sinon | tail -5'
```

tool result:

```
node_modules/@types/react-dom/index.d.ts(49,36): error TS1005: ',' expected.
node_modules/@types/react-dom/index.d.ts(49,59): error TS1005: ',' expected.
node_modules/@types/react-dom/index.d.ts(54,10): error TS1005: ',' expected.
node_modules/@types/react-dom/index.d.ts(54,36): error TS1005: ',' expected.
node_modules/@types/react-dom/index.d.ts(54,75): error TS1005: ',' expected.
```

**tool call: Bash**

```bash
../bin/envrun 'npx tsc -p tsconfig.json --noEmit 2>&1 | grep -v "^node_modules" | head'
```

tool result:

```
(Bash completed with no output)
```

**assistant:** `FormControlLabel` has a new `labelPlacement` prop. It defaults to `'end'`, which keeps the current layout. Setting it to `'start'` puts the label to the left of the control, so the `rtl` workaround from the issue is no longer needed:

```jsx
<FormControlLabel control={<Switch />} label="Wi-Fi" labelPlacement="start" />
```

**Changes:**
- `packages/material-ui/src/FormControlLabel/FormControlLabel.js`:
  - Added the `labelPlacement` prop, accepting `'end'` or `'start'`.
  - Added a `labelPlacementStart` style class, applied to the root when `labelPlacement="start"`. It uses `flexDirection: 'row-reverse'` and swaps the `-14` / `16` left and right margins so the control still lines up correctly.
- `FormControlLabel.d.ts`: added `labelPlacement?: 'end' | 'start'` to the props type and `'labelPlacementStart'` to the class keys.
- `pages/api/form-control-label.md`: documented the new prop and CSS class. This file is normally generated; I edited it by hand to match the generator's format and didn't run the generator.

**Testing:**
- I wrote a temporary test checking that the `labelPlacementStart` class is applied with `labelPlacement="start"` and not by default. It and the existing `FormControlLabel` tests passed (11 in total), and I've deleted the test file.
- ESLint reports no errors on the component.
- The TypeScript check (`tsc`) prints errors, but every one is inside `node_modules` type packages (`@types/sinon`, `@types/react-dom`), not in the repo's own files.

I didn't touch `package.json`, `yarn.lock`, `Dockerfile` or `custom-reporter.js`; they were already changed or added before I started.

_session end: success, turns 10, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 4.43 s: yarn -s mocha packages/material-ui/src/FormControlLabel/*.test.js 2>&1 | tail -30
- `rc=0` 4.03 s: npx eslint packages/material-ui/src/FormControlLabel && npx tsc -p packages/material-ui 2>&1 | tail -5; echo done
- `rc=0` 2.21 s: npx tsc -p tsconfig.json --noEmit 2>&1 | tail -5; echo rc=$?
- `rc=0` 2.17 s: npx tsc -p tsconfig.json --noEmit 2>&1 | grep -v node_modules/@types/sinon | tail -5
- `rc=0` 2.14 s: npx tsc -p tsconfig.json --noEmit 2>&1 | grep -v "^node_modules" | head
