# Instance: mui__material-ui-12968

- Final resolved (evaluator, logs/mui__material-ui-12968_result.json): False
- Run state: DONE
- One attempt. Duration 97.4 s, turns 16, actor cost $0.4068302000000001, container commands 2
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/mui__material-ui-12968/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-12968/repo. Consider the following issue description:

<issue_description>
Demo do not explain that FilledInput and OutlinedInput are needed instead of Input when you want Filled/Outlined textfields
- [x] This is not a v0.x issue. <!-- (v0.x is no longer maintained) -->
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Expected Behavior
Filled and outlined should work like it works on TextField with FormControl. FormControl api specifies that this prop should work. 

## Current Behavior
It doesn't. Codesandbox link below explains it pretty well. 

## Steps to Reproduce
https://codesandbox.io/s/nwl42ym41p

## Your Environment

| Tech         | Version |
|--------------|---------|
| Material-UI  | v3.1.0  |

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-12968/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-12968/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-12968/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-12968/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
git log --oneline -2; ls packages/material-ui/src/FormControl packages/material-ui/src/InputLabel packages/material-ui/src/FormLabel; cat packages/material-ui/src/FormControl/FormControl.js; cat packages/material-ui/src/InputLabel/InputLabel.js
```

tool result:

```
ea462822d [docs] Fix IconButton Snackbar demos (#12964)
3204104bb [docs] Add Emotion to style interoperability guide (#12966)
packages/material-ui/src/FormControl:
FormControl.d.ts
FormControl.js
FormControl.test.js
index.d.ts
index.js

packages/material-ui/src/FormLabel:
FormLabel.d.ts
FormLabel.js
FormLabel.test.js
index.d.ts
index.js

packages/material-ui/src/InputLabel:
InputLabel.d.ts
InputLabel.js
InputLabel.test.js
index.d.ts
index.js
import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import { isFilled, isAdornedStart } from '../InputBase/utils';
import withStyles from '../styles/withStyles';
import { capitalize } from '../utils/helpers';
import { isMuiElement } from '../utils/reactHelpers';

export const styles = {
  /* Styles applied to the root element. */
  root: {
    display: 'inline-flex',
    flexDirection: 'column',
    position: 'relative',
    // Reset fieldset default style.
    minWidth: 0,
    padding: 0,
    margin: 0,
    border: 0,
    verticalAlign: 'top', // Fix alignment issue on Safari.
  },
  /* Styles applied to the root element if `margin="normal"`. */
  marginNormal: {
    marginTop: 16,
    marginBottom: 8,
  },
  /* Styles applied to the root element if `margin="dense"`. */
  marginDense: {
    marginTop: 8,
    marginBottom: 4,
  },
  /* Styles applied to the root element if `fullWidth={true}`. */
  fullWidth: {
    width: '100%',
  },
};

/**
 * Provides context such as filled/focused/error/required for form inputs.
 * Relying on the context provides high flexibilty and ensures that the state always stays
 * consistent across the children of the `FormControl`.
 * This context is used by the following components:
 *  - FormLabel
 *  - FormHelperText
 *  - Input
 *  - InputLabel
 */
class FormControl extends React.Component {
  constructor(props) {
    super();
    // We need to iterate through the children and find the Input in order
    // to fully support server side rendering.
    const { children } = props;
    if (children) {
      React.Children.forEach(children, child => {
        if (!isMuiElement(child, ['Input', 'Select'])) {
          return;
        }

        if (isFilled(child.props, true)) {
          this.state.filled = true;
        }

        const input = isMuiElement(child, ['Select']) ? child.props.input : child;

        if (input && isAdornedStart(input.props)) {
          this.state.adornedStart = true;
        }
      });
    }
  }

  state = {
    adornedStart: false,
    filled: false,
    focused: false,
  };

  getChildContext() {
    const { disabled, error, required, margin, variant } = this.props;
    const { adornedStart, filled, focused } = this.state;

    return {
      muiFormControl: {
        adornedStart,
        disabled,
        error,
        filled,
        focused,
        margin,
        onBlur: this.handleBlur,
        onEmpty: this.handleClean,
        onFilled: this.handleDirty,
        onFocus: this.handleFocus,
        required,
        variant,
      },
    };
  }

  handleFocus = () => {
    this.setState(state => (!state.focused ? { focused: true } : null));
  };

  handleBlur = () => {
    this.setState(state => (state.focused ? { focused: false } : null));
  };

  handleDirty = () => {
    if (!this.state.filled) {
      this.setState({ filled: true });
    }
  };

  handleClean = () => {
    if (this.state.filled) {
      this.setState({ filled: false });
    }
  };

  render() {
    const {
      classes,
      className,
      component: Component,
      disabled,
      error,
      fullWidth,
      margin,
      required,
      variant,
      ...other
    } = this.props;

    return (
      <Component
        className={classNames(
          classes.root,
          {
            [classes[`margin${capitalize(margin)}`]]: margin !== 'none',
            [classes.fullWidth]: fullWidth,
          },
          className,
        )}
        {...other}
      />
    );
  }
}

FormControl.propTypes = {
  /**
   * The contents of the form control.
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
   */
  component: PropTypes.oneOfType([PropTypes.string, PropTypes.func, PropTypes.object]),
  /**
   * If `true`, the label, input and helper text should be displayed in a disabled state.
   */
  disabled: PropTypes.bool,
  /**
   * If `true`, the label should be displayed in an error state.
   */
  error: PropTypes.bool,
  /**
   * If `true`, the component will take up the full width of its container.
   */
  fullWidth: PropTypes.bool,
  /**
   * If `dense` or `normal`, will adjust vertical spacing of this and contained components.
   */
  margin: PropTypes.oneOf(['none', 'dense', 'normal']),
  /**
   * If `true`, the label will indicate that the input is required.
   */
  required: PropTypes.bool,
  /**
   * The variant to use.
   */
  variant: PropTypes.oneOf(['standard', 'outlined', 'filled']),
};

FormControl.defaultProps = {
  component: 'div',
  disabled: false,
  error: false,
  fullWidth: false,
  margin: 'none',
  required: false,
  variant: 'standard',
};

FormControl.childContextTypes = {
  muiFormControl: PropTypes.object,
};

export default withStyles(styles, { name: 'MuiFormControl' })(FormControl);
// @inheritedComponent FormLabel

import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import withStyles from '../styles/withStyles';
import FormLabel from '../FormLabel';
import { formControlState } from '../InputBase/InputBase';

export const styles = theme => ({
  /* Styles applied to the root element. */
  root: {
    transformOrigin: 'top left',
  },
  /* Styles applied to the root element if th
[... 4487 more characters not shown]
```

**tool call: Bash**

```bash
grep -rn "muiName" packages/material-ui/src/ | grep -v test; grep -n "Filled\|Outlined\|muiName" packages/material-ui/src/FormControl/FormControl.test.js
```

tool result:

```
packages/material-ui/src/ListSubheader/ListSubheader.js:115:ListSubheader.muiName = 'ListSubheader';
packages/material-ui/src/Input/Input.js:238:Input.muiName = 'Input';
packages/material-ui/src/FilledInput/FilledInput.js:261:FilledInput.muiName = 'Input';
packages/material-ui/src/ListItemSecondaryAction/ListItemSecondaryAction.js:42:ListItemSecondaryAction.muiName = 'ListItemSecondaryAction';
packages/material-ui/src/internal/svg-icons/ArrowDropDown.js:15:ArrowDropDown.muiName = 'SvgIcon';
packages/material-ui/src/internal/svg-icons/KeyboardArrowRight.js:14:KeyboardArrowRight.muiName = 'SvgIcon';
packages/material-ui/src/internal/svg-icons/Warning.js:14:Warning.muiName = 'SvgIcon';
packages/material-ui/src/internal/svg-icons/CheckCircle.js:14:CheckCircle.muiName = 'SvgIcon';
packages/material-ui/src/internal/svg-icons/RadioButtonUnchecked.js:14:RadioButtonUnchecked.muiName = 'SvgIcon';
packages/material-ui/src/internal/svg-icons/Cancel.js:14:Cancel.muiName = 'SvgIcon';
packages/material-ui/src/internal/svg-icons/RadioButtonChecked.js:14:RadioButtonChecked.muiName = 'SvgIcon';
packages/material-ui/src/internal/svg-icons/ArrowDownward.js:15:ArrowDownward.muiName = 'SvgIcon';
packages/material-ui/src/internal/svg-icons/KeyboardArrowLeft.js:14:KeyboardArrowLeft.muiName = 'SvgIcon';
packages/material-ui/src/internal/svg-icons/CheckBox.js:14:CheckBox.muiName = 'SvgIcon';
packages/material-ui/src/internal/svg-icons/CheckBoxOutlineBlank.js:14:CheckBoxOutlineBlank.muiName = 'SvgIcon';
packages/material-ui/src/internal/svg-icons/IndeterminateCheckBox.js:14:IndeterminateCheckBox.muiName = 'SvgIcon';
packages/material-ui/src/SvgIcon/SvgIcon.js:146:SvgIcon.muiName = 'SvgIcon';
packages/material-ui/src/Stepper/Stepper.js:140:Stepper.muiName = 'Stepper';
packages/material-ui/src/utils/reactHelpers.js:18:export function isMuiElement(element, muiNames) {
packages/material-ui/src/utils/reactHelpers.js:19:  return React.isValidElement(element) && muiNames.indexOf(element.type.muiName) !== -1;
packages/material-ui/src/utils/reactHelpers.d.ts:6:export type NamedMuiComponent = React.ComponentType & { muiName: string };
packages/material-ui/src/utils/reactHelpers.d.ts:14:export function isMuiElement(element: any, muiNames: string[]): element is NamedMuiElement;
packages/material-ui/src/ExpansionPanelSummary/ExpansionPanelSummary.js:203:ExpansionPanelSummary.muiName = 'ExpansionPanelSummary';
packages/material-ui/src/NativeSelect/NativeSelect.js:156:NativeSelect.muiName = 'Select';
packages/material-ui/src/OutlinedInput/OutlinedInput.js:230:OutlinedInput.muiName = 'Input';
packages/material-ui/src/StepLabel/StepLabel.js:203:StepLabel.muiName = 'StepLabel';
packages/material-ui/src/Select/Select.js:196:Select.muiName = 'Select';
packages/material-ui/src/Icon/Icon.js:109:Icon.muiName = 'Icon';
packages/material-ui/src/ListItemAvatar/ListItemAvatar.js:72:ListItemAvatar.muiName = 'ListItemAvatar';
199:      describe('onFilled', () => {
202:          muiFormControlContext.onFilled();
205:          muiFormControlContext.onFilled();
212:          muiFormControlContext.onFilled();
```

**tool call: Bash**

```bash
ls docs/src/pages/demos/text-fields/ docs/src/pages/demos/selects/; cat docs/src/pages/demos/text-fields/ComposedTextField.js; grep -rn "variant" packages/material-ui/src/InputBase/InputBase.js packages/material-ui/src/Input/Input.js packages/material-ui/src/OutlinedInput/*.js | head -30
```

tool result:

```
docs/src/pages/demos/selects/:
ControlledOpenSelect.js
DialogSelect.js
MultipleSelect.js
NativeSelects.js
SimpleSelect.js
selects.md

docs/src/pages/demos/text-fields/:
ComposedTextField.js
CustomizedInputs.js
FilledInputAdornments.js
FilledTextFields.js
FormattedInputs.js
InputAdornments.js
InputWithIcon.js
Inputs.js
OutlinedInputAdornments.js
OutlinedTextFields.js
TextFieldMargins.js
TextFields.js
text-fields.md
import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Input from '@material-ui/core/Input';
import InputLabel from '@material-ui/core/InputLabel';
import FormHelperText from '@material-ui/core/FormHelperText';
import FormControl from '@material-ui/core/FormControl';

const styles = theme => ({
  container: {
    display: 'flex',
    flexWrap: 'wrap',
  },
  formControl: {
    margin: theme.spacing.unit,
  },
});

class ComposedTextField extends React.Component {
  state = {
    name: 'Composed TextField',
  };

  handleChange = event => {
    this.setState({ name: event.target.value });
  };

  render() {
    const { classes } = this.props;

    return (
      <div className={classes.container}>
        <FormControl className={classes.formControl}>
          <InputLabel htmlFor="name-simple">Name</InputLabel>
          <Input id="name-simple" value={this.state.name} onChange={this.handleChange} />
        </FormControl>
        <FormControl className={classes.formControl} aria-describedby="name-helper-text">
          <InputLabel htmlFor="name-helper">Name</InputLabel>
          <Input id="name-helper" value={this.state.name} onChange={this.handleChange} />
          <FormHelperText id="name-helper-text">Some important helper text</FormHelperText>
        </FormControl>
        <FormControl className={classes.formControl} disabled>
          <InputLabel htmlFor="name-disabled">Name</InputLabel>
          <Input id="name-disabled" value={this.state.name} onChange={this.handleChange} />
          <FormHelperText>Disabled</FormHelperText>
        </FormControl>
        <FormControl className={classes.formControl} error aria-describedby="name-error-text">
          <InputLabel htmlFor="name-error">Name</InputLabel>
          <Input id="name-error" value={this.state.name} onChange={this.handleChange} />
          <FormHelperText id="name-error-text">Error</FormHelperText>
        </FormControl>
      </div>
    );
  }
}

ComposedTextField.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(ComposedTextField);
```

**tool call: Bash**

```bash
cat package.json | grep -n '"test' ; git show --stat HEAD | head -30
```

tool result:

```
45:    "test": "yarn lint && yarn typescript && yarn test:coverage",
46:    "test:unit": "cross-env NODE_ENV=test mocha packages/material-ui/test/**/*.test.js packages/material-ui/src/{,**/}*.test.js docs/src/**/*.test.js",
47:    "test:watch": "yarn test:unit --watch",
48:    "test:coverage": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha packages/material-ui/test/**/*.test.js packages/material-ui/src/{,**/}*.test.js && nyc report -r lcovonly",
49:    "test:coverage:html": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha packages/material-ui/test/**/*.test.js packages/material-ui/src/{,**/}*.test.js && nyc report --reporter=html",
50:    "test:karma": "cross-env NODE_ENV=test karma start test/karma.conf.js --single-run",
51:    "test:regressions": "webpack --config test/regressions/webpack.config.js && rimraf test/regressions/screenshots/chrome/* && vrtest run --config test/vrtest.config.js --record",
commit ea462822d9881478efcf08829a60e3ff818f5d2d
Author: bhalahariharan <bhala.vishnu@gmail.com>
Date:   Sun Sep 23 14:55:49 2018 +0530

    [docs] Fix IconButton Snackbar demos (#12964)
    
    * Remove styles for IconButton
    
    * Prettify the changes
    
    * keep the height invariant

 docs/src/pages/demos/snackbars/ConsecutiveSnackbars.js | 3 +--
 docs/src/pages/demos/snackbars/SimpleSnackbar.js       | 3 +--
 2 files changed, 2 insertions(+), 4 deletions(-)
```

**tool call: Bash**

```bash
sed -n 1,80p packages/material-ui/src/OutlinedInput/OutlinedInput.js; sed -n 1,80p packages/material-ui/src/OutlinedInput/NotchedOutline.js; cat packages/material-ui/src/OutlinedInput/*.test.js
```

tool result:

```
// @inheritedComponent InputBase

import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import InputBase from '../InputBase';
import NotchedOutline from './NotchedOutline';
import withStyles from '../styles/withStyles';

export const styles = theme => {
  return {
    /* Styles applied to the root element. */
    root: {
      position: 'relative',
      '&:hover:not($disabled):not($focused):not($error) $notchedOutline': {
        borderColor: theme.palette.text.primary,
      },
    },
    /* Styles applied to the root element if the component is focused. */
    focused: {},
    /* Styles applied to the root element if `disabled={true}`. */
    disabled: {},
    /* Styles applied to the root element if `startAdornment` is provided. */
    adornedStart: {
      paddingLeft: 14,
    },
    /* Styles applied to the root element if `endAdornment` is provided. */
    adornedEnd: {
      paddingRight: 14,
    },
    /* Styles applied to the root element if `error={true}`. */
    error: {},
    /* Styles applied to the root element if `multiline={true}`. */
    multiline: {
      padding: '18.5px 14px',
      // // These values are needed to prevent us from
      // // overrunning the notched outline (including label)
      // paddingTop: 27,
      // paddingBottom: 10,
    },
    /* Styles applied to the `NotchedOutline` element. */
    notchedOutline: {},
    /* Styles applied to the `input` element. */
    input: {
      padding: '18.5px 14px',
    },
    /* Styles applied to the `input` element if `margin="dense"`. */
    inputMarginDense: {
      paddingTop: 15,
      paddingBottom: 15,
    },
    /* Styles applied to the `input` element if `multiline={true}`. */
    inputMultiline: {
      padding: 0,
    },
    /* Styles applied to the `input` element if `startAdornment` is provided. */
    inputAdornedStart: {
      paddingLeft: 0,
    },
    /* Styles applied to the `input` element if `endAdornment` is provided. */
    inputAdornedEnd: {
      paddingRight: 0,
    },
  };
};

function OutlinedInput(props) {
  const { classes, labelWidth, notched, ...other } = props;

  return (
    <InputBase
      renderPrefix={state => (
        <NotchedOutline
          className={classes.notchedOutline}
          disabled={state.disabled}
          error={state.error}
          focused={state.focused}
          labelWidth={labelWidth}
          notched={
            typeof notched !== 'undefined'
import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import { withStyles } from '../styles';
import { capitalize } from '../utils/helpers';

export const styles = theme => {
  const light = theme.palette.type === 'light';
  const align = theme.direction === 'rtl' ? 'right' : 'left';

  return {
    /* Styles applied to the root element. */
    root: {
      position: 'absolute',
      width: '100%',
      height: '100%',
      boxSizing: 'border-box',
      top: 0,
      left: 0,
      margin: 0,
      padding: 0,
      pointerEvents: 'none',
      borderRadius: theme.shape.borderRadius,
      borderStyle: 'solid',
      borderWidth: 1,
      borderColor: light ? 'rgba(0, 0, 0, 0.23)' : 'rgba(255, 255, 255, 0.23)',
      // Match the Input Label
      transition: theme.transitions.create([`padding-${align}`, 'border-color', 'border-width'], {
        duration: theme.transitions.duration.shorter,
        easing: theme.transitions.easing.easeOut,
      }),
    },
    /* Styles applied to the legend element. */
    legend: {
      textAlign: 'left',
      padding: 0,
      transition: theme.transitions.create('width', {
        duration: theme.transitions.duration.shorter,
        easing: theme.transitions.easing.easeOut,
      }),
      // Firefox workaround. Firefox will only obscure the
      // rendered height of the legend and, unlike other browsers,
      // will not push fieldset contents.
      '@supports (-moz-appearance:none)': {
        height: 2,
      },
    },
    /* Styles applied to the root element if the control is focused. */
    focused: {
      borderColor: theme.palette.primary.main,
      borderWidth: 2,
    },
    /* Styles applied to the root element if `error={true}`. */
    error: {
      borderColor: theme.palette.error.main,
    },
    /* Styles applied to the root element if `disabled={true}`. */
    disabled: {
      borderColor: theme.palette.action.disabled,
    },
  };
};

/**
 * @ignore - internal component.
 */
function NotchedOutline(props) {
  const {
    children,
    classes,
    className,
    disabled,
    error,
    focused,
    labelWidth,
    notched,
    style,
    theme,
    ...other
  } = props;
import React from 'react';
import { assert } from 'chai';
import { createShallow, getClasses } from '../test-utils';
import NotchedOutline from './NotchedOutline';

describe('<NotchedOutline />', () => {
  let shallow;
  let classes;
  const theme = {
    direction: 'ltr',
  };
  const defaultProps = {
    labelWidth: 36,
    notched: true,
  };

  before(() => {
    shallow = createShallow({ dive: true });
    classes = getClasses(<NotchedOutline {...defaultProps} />);
  });

  it('should be a fieldset', () => {
    const wrapper = shallow(<NotchedOutline {...defaultProps} />);
    assert.strictEqual(wrapper.name(), 'fieldset');
    assert.strictEqual(wrapper.props()['aria-hidden'], true);
    assert.strictEqual(wrapper.children().length, 1);
    assert.strictEqual(wrapper.childAt(0).name(), 'legend');
  });

  it('should pass props', () => {
    const wrapper = shallow(
      <NotchedOutline
        {...defaultProps}
        className="notched-outline"
        style={{
          width: 17,
        }}
      />,
    );

    // Ensure that these overrides are properly spread
    assert.notStrictEqual(wrapper.props().style, 17);
    assert.strictEqual(wrapper.hasClass('notched-outline'), true);
    const legend = wrapper.find('legend');
    assert.strictEqual(legend.hasClass(class
[... 1408 more characters not shown]
```

**tool call: Bash**

```bash
cat docs/src/pages/demos/text-fields/text-fields.md; grep -n "variant" packages/material-ui/src/FormControl/FormControl.d.ts; cat docs/src/pages/demos/text-fields/OutlinedInputAdornments.js | head -40
```

tool result:

````
---
title: Text Field React component
components: FilledInput, FormControl, FormHelperText, Input, InputAdornment, InputBase, InputLabel, OutlinedInput, TextField
---

# Text Fields

<p class="description">Text fields let users enter and edit text.</p>

[Text fields](https://material.io/design/components/text-fields.html) allow users to enter text into a UI. They typically appear in forms and dialogs.

## TextField

The `TextField` wrapper component is a complete form control including a label, input and help text.

{{"demo": "pages/demos/text-fields/TextFields.js"}}

## Outlined

`TextField` supports outlined styling.

{{"demo": "pages/demos/text-fields/OutlinedTextFields.js"}}

## Filled

`TextField` supports filled styling.

{{"demo": "pages/demos/text-fields/FilledTextFields.js"}}

## Components

`TextField` is composed of smaller components ([`FormControl`](/api/form-control), [`InputLabel`](/api/input-label), [`Input`](/api/input), and [`FormHelperText`](/api/form-helper-text)) that you can leverage directly to significantly customize your form inputs.

You might also have noticed that some native HTML input properties are missing from the `TextField` component.
This is on purpose.
The component takes care of the most used properties, then it's up to the user to use the underlying component shown in the following demo. Still, you can use `inputProps` (and `InputProps`, `InputLabelProps` properties) if you want to avoid some boilerplate.

{{"demo": "pages/demos/text-fields/ComposedTextField.js"}}

## Inputs

{{"demo": "pages/demos/text-fields/Inputs.js"}}

## Layout

`TextField`, `FormControl` allow the specification of `margin` to alter the vertical spacing of inputs. Using
`none` (default) will not apply margins to the `FormControl`, whereas `dense` and `normal` will as well as alter
other styles to meet the specification.

{{"demo": "pages/demos/text-fields/TextFieldMargins.js"}}

## Input Adornments

`Input` allows the provision of `InputAdornment`.
These can be used to add a prefix, a suffix or an action to an input.
For instance, you can use an icon button to hide or reveal the password.

{{"demo": "pages/demos/text-fields/InputAdornments.js"}}

## Filled Input Adornments

{{"demo": "pages/demos/text-fields/FilledInputAdornments.js"}}

## Outlined Input Adornments

{{"demo": "pages/demos/text-fields/OutlinedInputAdornments.js"}}

## Formatted inputs

You can use third-party libraries to format an input.
You have to provide a custom implementation of the `<input>` element with the `inputComponent` property.

The following demo uses the [react-text-mask](https://github.com/text-mask/text-mask) and [react-number-format](https://github.com/s-yadav/react-number-format) libraries.

{{"demo": "pages/demos/text-fields/FormattedInputs.js"}}

## Customized inputs

If you have been reading the [overrides documentation page](/customization/overrides)
but you are not confident jumping in, here's an example of how you can change the main color of an Input.

{{"demo": "pages/demos/text-fields/CustomizedInputs.js"}}

## With icon

Icons can be specified as prepended or appended.

{{"demo": "pages/demos/text-fields/InputWithIcon.js"}}

## Limitations

The input label "shrink" state isn't always correct.
The input label is supposed to shrink as soon as the input is displaying something.
In some circumstances, we can't determine the "shrink" state (number input, datetime input, Stripe input). You might notice an overlap.

![shrink](/static/images/text-fields/shrink.png)

To workaround the issue, you can force the "shrink" state of the label.
```jsx
<TextField InputLabelProps={{ shrink: true }} />
```
or
```jsx
<InputLabel shrink>Count</InputLabel>
```
import React from 'react';
import classNames from 'classnames';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import IconButton from '@material-ui/core/IconButton';
import InputAdornment from '@material-ui/core/InputAdornment';
import TextField from '@material-ui/core/TextField';
import MenuItem from '@material-ui/core/MenuItem';
import Visibility from '@material-ui/icons/Visibility';
import VisibilityOff from '@material-ui/icons/VisibilityOff';

const styles = theme => ({
  root: {
    display: 'flex',
    flexWrap: 'wrap',
  },
  margin: {
    margin: theme.spacing.unit,
  },
  textField: {
    flexBasis: 280,
  },
});

const ranges = [
  {
    value: '0-20',
    label: '0 to 20',
  },
  {
    value: '21-50',
    label: '21 to 50',
  },
  {
    value: '51-100',
    label: '51 to 100',
  },
];

class OutlinedInputAdornments extends React.Component {
````

**thinking:**

```
The components already work correctly when paired—the actual issue is that docs/demos never clarify that `FormControl variant="outlined"` requires using `OutlinedInput`, not plain `Input`. I'll check how `TextField` handles this pairing, then update the docs and demos accordingly.


```

**tool call: Bash**

```bash
grep -n "labelRef\|labelNode\|labelWidth\|findDOMNode\|InputComponent\|variantComponent" packages/material-ui/src/TextField/TextField.js
```

tool result:

```
15:const variantComponent = {
50:  labelNode = null;
52:  labelRef = null;
56:    this.labelRef = React.createRef();
61:      this.labelNode = ReactDOM.findDOMNode(this.labelRef.current);
112:      InputMore.labelWidth = this.labelNode ? this.labelNode.offsetWidth * 0.75 + 8 : 0;
116:    const InputComponent = variantComponent[variant];
118:      <InputComponent
152:          <InputLabel htmlFor={id} ref={this.labelRef} {...InputLabelProps}>
```

**tool call: Bash**

```bash
sed -n 50,70p packages/material-ui/src/TextField/TextField.js
```

tool result:

```
  labelNode = null;

  labelRef = null;

  constructor(props) {
    super(props);
    this.labelRef = React.createRef();
  }

  componentDidMount() {
    if (this.props.variant === 'outlined') {
      this.labelNode = ReactDOM.findDOMNode(this.labelRef.current);
      this.forceUpdate();
    }
  }

  render() {
    const {
      autoComplete,
      autoFocus,
      children,
```

**assistant:** Now I'll update the composed demo to show outlined and filled variants:

**tool call: Bash**

```bash
cd docs/src/pages/demos/text-fields && python3 - <<'EOF'
p='ComposedTextField.js'
s=open(p).read()
s=s.replace("""import React from 'react';
import PropTypes""","""import React from 'react';
import ReactDOM from 'react-dom';
import PropTypes""")
s=s.replace("""import Input from '@material-ui/core/Input';
""","""import Input from '@material-ui/core/Input';
import OutlinedInput from '@material-ui/core/OutlinedInput';
import FilledInput from '@material-ui/core/FilledInput';
""")
s=s.replace("""  state = {
    name: 'Composed TextField',
  };
""","""  labelRef = null;

  state = {
    name: 'Composed TextField',
  };

  componentDidMount() {
    this.forceUpdate();
  }
""")
s=s.replace("""          <FormHelperText id="name-error-text">Error</FormHelperText>
        </FormControl>
""","""          <FormHelperText id="name-error-text">Error</FormHelperText>
        </FormControl>
        <FormControl className={classes.formControl} variant="outlined">
          <InputLabel
            ref={ref => {
              this.labelRef = ReactDOM.findDOMNode(ref);
            }}
            htmlFor="component-outlined"
          >
            Name
          </InputLabel>
          <OutlinedInput
            id="component-outlined"
            value={this.state.name}
            onChange={this.handleChange}
            labelWidth={this.labelRef ? this.labelRef.offsetWidth : 0}
          />
        </FormControl>
        <FormControl className={classes.formControl} variant="filled">
          <InputLabel htmlFor="component-filled">Name</InputLabel>
          <FilledInput id="component-filled" value={this.state.name} onChange={this.handleChange} />
        </FormControl>
""")
open(p,'w').write(s)

p='text-fields.md'
s=open(p).read()
old="""{{"demo": "pages/demos/text-fields/ComposedTextField.js"}}
"""
s=s.replace(old, old+"""
When using the components directly, the `variant` property of `FormControl` is only applied to the `InputLabel` and `FormHelperText`.
You need to use the matching input component yourself:
- `Input` for the `standard` variant,
- [`OutlinedInput`](/api/outlined-input) for the `outlined` variant,
- [`FilledInput`](/api/filled-input) for the `filled` variant.
""")
s=s.replace("([`FormControl`](/api/form-control), [`InputLabel`](/api/input-label), [`Input`](/api/input), and [`FormHelperText`](/api/form-helper-text))",
"([`FormControl`](/api/form-control), [`Input`](/api/input), [`FilledInput`](/api/filled-input), [`InputLabel`](/api/input-label), [`OutlinedInput`](/api/outlined-input), and [`FormHelperText`](/api/form-helper-text))")
open(p,'w').write(s)
EOF
git diff --stat
```

tool result:

```
 .../pages/demos/text-fields/ComposedTextField.js   | 29 ++++++++++++
 docs/src/pages/demos/text-fields/text-fields.md    |  8 +++-
 package.json                                       |  6 +++
 yarn.lock                                          | 52 ++++++++++++++++++++++
 4 files changed, 94 insertions(+), 1 deletion(-)
```

**assistant:** `package.json` and `yarn.lock` show up as changed even though I didn't edit them. Checking what that is:

**tool call: Bash**

```bash
cd /work/mui__material-ui-12968/repo && git diff package.json
```

tool result:

```
diff --git a/package.json b/package.json
index b5563268d..01d05b8fb 100644
--- a/package.json
+++ b/package.json
@@ -68,8 +68,14 @@
     "@babel/preset-env": "7.0.0",
     "@babel/preset-react": "7.0.0",
     "@babel/register": "7.0.0",
+    "@types/chai": "^5.2.3",
+    "@types/chai-dom": "^1.11.3",
     "@types/enzyme": "^3.1.4",
+    "@types/format-util": "^1.0.4",
+    "@types/prop-types": "^15.7.15",
     "@types/react": "^16.3.14",
+    "@types/react-dom": "^19.2.3",
+    "@types/sinon": "^21.0.0",
     "argos-cli": "^0.0.9",
     "autoprefixer": "^9.0.0",
     "autosuggest-highlight": "^3.1.1",
```

**thinking:**

```
The package.json/yarn.lock changes are from environment setup, not my edits, so I'll leave them as-is. Next I'll update FormControl's doc comment to list the context-reading input components and verify the generated API page.


```

**tool call: Bash**

```bash
sed -n 1,25p pages/api/form-control.md; grep -n "docs:api" package.json
```

tool result:

````
---
filename: /packages/material-ui/src/FormControl/FormControl.js
title: FormControl API
---

<!--- This documentation is automatically generated, do not try to edit it. -->

# FormControl

<p class="description">The API documentation of the FormControl React component.</p>

```js
import FormControl from '@material-ui/core/FormControl';
```

Provides context such as filled/focused/error/required for form inputs.
Relying on the context provides high flexibilty and ensures that the state always stays
consistent across the children of the `FormControl`.
This context is used by the following components:
 - FormLabel
 - FormHelperText
 - Input
 - InputLabel

## Props
25:    "docs:api": "yarn docs:api:core && yarn docs:api:lab",
26:    "docs:api:core": "rimraf ./pages/api && cross-env BABEL_ENV=docs-development babel-node ./docs/scripts/buildApi.js ./packages/material-ui/src ./pages/api",
27:    "docs:api:lab": "rimraf ./pages/lab/api && cross-env BABEL_ENV=docs-development babel-node ./docs/scripts/buildApi.js ./packages/material-ui-lab/src ./pages/lab/api",
````

**tool call: Bash**

```bash
python3 - <<'EOF'
for p,prefix in [('packages/material-ui/src/FormControl/FormControl.js',' * '),('pages/api/form-control.md','')]:
    s=open(p).read()
    old=f"""{prefix}This context is used by the following components:
{prefix} - FormLabel
{prefix} - FormHelperText
{prefix} - Input
{prefix} - InputLabel
"""
    new=f"""{prefix}This context is used by the following components:
{prefix} - FormLabel
{prefix} - FormHelperText
{prefix} - Input
{prefix} - InputLabel

{prefix}⚠️ The `variant` property isn't propagated to the input component.
{prefix}You need to use the matching input component: `Input`, `FilledInput` or `OutlinedInput`.
""".replace(' * \n',' *\n')
    assert old in s, p
    s=s.replace(old,new)
    open(p,'w').write(s)
EOF
git diff packages pages
```

tool result:

```
diff --git a/packages/material-ui/src/FormControl/FormControl.js b/packages/material-ui/src/FormControl/FormControl.js
index 82d00797d..fc3330381 100644
--- a/packages/material-ui/src/FormControl/FormControl.js
+++ b/packages/material-ui/src/FormControl/FormControl.js
@@ -44,6 +44,9 @@ export const styles = {
  *  - FormHelperText
  *  - Input
  *  - InputLabel
+
+ * ⚠️ The `variant` property isn't propagated to the input component.
+ * You need to use the matching input component: `Input`, `FilledInput` or `OutlinedInput`.
  */
 class FormControl extends React.Component {
   constructor(props) {
diff --git a/pages/api/form-control.md b/pages/api/form-control.md
index b5857c884..744621593 100644
--- a/pages/api/form-control.md
+++ b/pages/api/form-control.md
@@ -22,6 +22,9 @@ This context is used by the following components:
  - Input
  - InputLabel
 
+⚠️ The `variant` property isn't propagated to the input component.
+You need to use the matching input component: `Input`, `FilledInput` or `OutlinedInput`.
+
 ## Props
 
 | Name | Type | Default | Description |
```

**assistant:** One small formatting slip: the blank line in the JSDoc is missing its ` *`. Fixing it:

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/mui__material-ui-12968/repo/packages/material-ui/src/FormControl/FormControl.js",
 "old_string": " *  - InputLabel\n\n * \u26a0\ufe0f",
 "new_string": " *  - InputLabel\n *\n * \u26a0\ufe0f"
}
```

tool result:

```
The file /work/mui__material-ui-12968/repo/packages/material-ui/src/FormControl/FormControl.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**assistant:** Now I'll check three things: the API markdown generator gives the same output as my hand edit, lint passes on the changed files, and the nearby unit tests pass.

**tool call: Bash**

```bash
/work/mui__material-ui-12968/bin/envrun 'BABEL_ENV=docs-development npx babel-node ./docs/scripts/buildApi.js ./packages/material-ui/src /tmp/apiout >/dev/null 2>&1; diff /tmp/apiout/form-control.md pages/api/form-control.md && echo API_SAME; npx eslint docs/src/pages/demos/text-fields/ComposedTextField.js packages/material-ui/src/FormControl/FormControl.js && echo LINT_OK; npx prettier --list-different docs/src/pages/demos/text-fields/ComposedTextField.js packages/material-ui/src/FormControl/FormControl.js; NODE_ENV=test npx mocha packages/material-ui/test/**/*.test.js "packages/material-ui/src/{FormControl,InputLabel,TextField,OutlinedInput,FilledInput,Input,InputBase}/*.test.js" docs/src/**/*.test.js 2>&1 | tail -8'
```

tool result:

```
API_SAME
LINT_OK


  ․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․
  ․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․
  ․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․

  157 passing (827ms)
```

**assistant:** All good. Last, I'll mount the updated demo in a scratch test to confirm the outlined and filled examples render with the right classes.

**tool call: Bash**

```bash
cat > packages/material-ui/src/tmpRepro.test.js <<'EOF'
import React from 'react';
import { assert } from 'chai';
import { createMount } from './test-utils';
import Demo from '../../../docs/src/pages/demos/text-fields/ComposedTextField';

describe('repro', () => {
  it('renders outlined & filled', () => {
    const mount = createMount();
    const html = mount(<Demo />).html();
    assert.include(html, 'MuiInputLabel-outlined');
    assert.include(html, 'MuiOutlinedInput-root');
    assert.include(html, 'MuiInputLabel-filled');
    assert.include(html, 'MuiFilledInput-root');
    mount.cleanUp();
  });
});
EOF
/work/mui__material-ui-12968/bin/envrun 'NODE_ENV=test npx mocha packages/material-ui/test/**/*.test.js packages/material-ui/src/tmpRepro.test.js 2>&1 | tail -5'; rm packages/material-ui/src/tmpRepro.test.js; git status --short
```

tool result:

```
  ․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․

  33 passing (633ms)


 M docs/src/pages/demos/text-fields/ComposedTextField.js
 M docs/src/pages/demos/text-fields/text-fields.md
 M package.json
 M packages/material-ui/src/FormControl/FormControl.js
 M pages/api/form-control.md
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
```

**assistant:** I fixed this by updating the docs and the demo; the component code itself didn't need to change. `FormControl`'s `variant` prop only affects `InputLabel` and `FormHelperText`, not the input inside it. The codesandbox puts a plain `<Input>` inside `<FormControl variant="outlined">`, so the input stays standard. You have to use `OutlinedInput` or `FilledInput` yourself, which is what `TextField` does internally, and nothing in the docs said so.

**Changes:**
- **`docs/src/pages/demos/text-fields/ComposedTextField.js`**: added two examples to the demo:
  - `<FormControl variant="outlined">` with `InputLabel` and `OutlinedInput`. It measures the label to set `labelWidth`, so the outline has a gap for the label, the same way `TextField` does it.
  - `<FormControl variant="filled">` with `InputLabel` and `FilledInput`.
- **`docs/src/pages/demos/text-fields/text-fields.md`**:
  - A note under the composed demo saying which input goes with which variant: `Input` for standard, `OutlinedInput` for outlined, `FilledInput` for filled.
  - The list of components that `TextField` is built from now includes `FilledInput` and `OutlinedInput`.
- **`packages/material-ui/src/FormControl/FormControl.js`** (doc comment only) and **`pages/api/form-control.md`**: a warning that `variant` isn't passed on to the input, so you have to pick the matching input component. I checked that running the API doc generator produces exactly my edited `form-control.md`.

**Checks:**
- A scratch test mounted the updated demo and confirmed it renders the outlined and filled label classes plus `MuiOutlinedInput-root` and `MuiFilledInput-root`. I deleted it afterwards.
- ESLint passes on the changed files.
- 157 tests pass across FormControl, InputLabel, TextField, OutlinedInput, FilledInput, Input, InputBase and the docs.

The working tree also shows `package.json`, `yarn.lock`, `Dockerfile` and `custom-reporter.js` as changed or new. They came from the environment setup, not from me, and I left them alone.

_session end: success, turns 16, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 24.6 s: BABEL_ENV=docs-development npx babel-node ./docs/scripts/buildApi.js ./packages/material-ui/src /tmp/apiout >/dev/null 2>&1; diff /tmp/apiout/form-control.md pages/api/form-control.md && echo API_SAME; npx eslint docs/src/pages/demos/text-fields/ComposedTextField.js packages/material-ui/src/FormControl/FormControl.js && echo LINT_OK; npx prettier --list-different docs/src/pages/demos/text-fields/ComposedTextField.js packages/material-ui/src/FormControl/FormControl.js; NODE_ENV=test npx mocha packages/material-ui/test/**/*.test.js "packages/material-ui/src/{FormControl,InputLabel,TextField,Outl
- `rc=0` 3.48 s: NODE_ENV=test npx mocha packages/material-ui/test/**/*.test.js packages/material-ui/src/tmpRepro.test.js 2>&1 | tail -5
