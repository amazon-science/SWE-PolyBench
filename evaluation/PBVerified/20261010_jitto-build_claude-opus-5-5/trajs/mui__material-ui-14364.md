# Instance: mui__material-ui-14364

- Final resolved (evaluator, logs/mui__material-ui-14364_result.json): True
- Run state: DONE
- One attempt. Duration 644.7 s, turns 17, actor cost $0.3847654, container commands 7
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/mui__material-ui-14364/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-14364/repo. Consider the following issue description:

<issue_description>
Select inside InputAdornment causes crash with material-ui/core 3.9.1 (works with 3.9.0)
<!--- Provide a general summary of the issue in the Title above -->

We use a Select as InputAdornment to let users choose a unit. It worked fine until material-ui/core 3.9.0, but now crashes the whole application.

<!--
    Thank you very much for contributing to Material-UI by creating an issue! ❤️
    To avoid duplicate issues we ask you to check off the following list.
-->

<!-- Checked checkbox should look like this: [x] -->
- [x] This is not a v0.x issue. <!-- (v0.x is no longer maintained) -->
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Expected Behavior 🤔
<!---
    Describe what should happen.
-->
![material_ui_text_field_select_adornment](https://user-images.githubusercontent.com/10057387/52056798-80899100-2563-11e9-98c2-3af3392baba9.png)


## Current Behavior 😯
<!---
    Describe what happens instead of the expected behavior.
-->

```
Uncaught Error: Maximum update depth exceeded. This can happen when a component repeatedly calls setState inside componentWillUpdate or componentDidUpdate. React limits the number of nested updates to prevent infinite loops.
    at invariant (VM77 0.chunk.js:110042)
    at scheduleWork (VM77 0.chunk.js:129702)
    at Object.enqueueSetState (VM77 0.chunk.js:122921)
    at FormControl.push../node_modules/react/cjs/react.development.js.Component.setState (VM77 0.chunk.js:139977)
    at Object.FormControl._this.handleClean [as onEmpty] (VM77 0.chunk.js:9830)
    at InputBase.checkDirty (VM77 0.chunk.js:14100)
    at InputBase.componentDidUpdate (VM77 0.chunk.js:14078)
    at commitLifeCycles (VM77 0.chunk.js:126998)
    at commitAllLifeCycles (VM77 0.chunk.js:128497)
    at HTMLUnknownElement.callCallback (VM77 0.chunk.js:110132)
    at Object.invokeGuardedCallbackDev (VM77 0.chunk.js:110181)
    at invokeGuardedCallback (VM77 0.chunk.js:110235)
    at commitRoot (VM77 0.chunk.js:128702)
    at completeRoot (VM77 0.chunk.js:130232)
    at performWorkOnRoot (VM77 0.chunk.js:130155)
    at performWork (VM77 0.chunk.js:130060)
    at performSyncWork (VM77 0.chunk.js:130034)
    at interactiveUpdates$1 (VM77 0.chunk.js:130322)
    at interactiveUpdates (VM77 0.chunk.js:112252)
    at dispatchInteractiveEvent (VM77 0.chunk.js:115068)
VM77 0.chunk.js:133526 

The above error occurred in the <InputBase> component:
    in InputBase (created by Context.Consumer)
    in WithFormControlContext(InputBase) (created by WithStyles(WithFormControlContext(InputBase)))
    in WithStyles(WithFormControlContext(InputBase)) (created by Input)
    in Input (created by WithStyles(Input))
    in WithStyles(Input) (created by TextField)
    in div (created by FormControl)
    in FormControl (created by WithStyles(FormControl))
    in WithStyles(FormControl) (created by TextField)
    in TextField (at ObjectField.js:202)
    in ObjectField (created by WithStyles(ObjectField))
    in WithStyles(ObjectField) (at ObjectFieldSet.js:38)
    in div (at ObjectFieldSet.js:28)
    in div (at ObjectFieldSet.js:27)
    in ObjectFieldSet (created by WithStyles(ObjectFieldSet))
    in WithStyles(ObjectFieldSet) (at ObjectEditPanel.js:91)
    in div (at ObjectEditPanel.js:90)
    in div (created by Typography)
    in Typography (created by WithStyles(Typography))
    in WithStyles(Typography) (at ObjectEditPanel.js:74)
    in div (created by Paper)
    in Paper (created by WithStyles(Paper))
    in WithStyles(Paper) (at ObjectEditPanel.js:66)
    in div (at ObjectEditPanel.js:65)
    in ObjectEditPanel (created by WithStyles(ObjectEditPanel))
    in WithStyles(ObjectEditPanel) (created by Connect(WithStyles(ObjectEditPanel)))
    in Connect(WithStyles(ObjectEditPanel)) (at ObjectEditPage.js:32)
    in div (at ObjectEditPage.js:30)
    in ObjectEditPage (created by Connect(ObjectEditPage))
    in Connect(ObjectEditPage) (at MainView.js:61)
    in div (at MainView.js:44)
    in div (at MainView.js:40)
    in div (at MainView.js:38)
    in MainView (created by Connect(MainView))
    in Connect(MainView) (at App.js:180)
    in div (at App.js:179)
    in div (at App.js:178)
    in Provider (at App.js:177)
    in MuiPickersUtilsProvider (at App.js:176)
    in MuiThemeProviderOld (at App.js:175)
    in App (at src/index.js:16)

Consider adding an error boundary to your tree to customize error handling behavior.
Visit https://fb.me/react-error-boundaries to learn more about error boundaries.
VM77 0.chunk.js:110042 Uncaught Error: Maximum update depth exceeded. This can happen when a component repeatedly calls setState inside componentWillUpdate or componentDidUpdate. React limits the number of nested updates to prevent infinite loops.
    at invariant (VM77 0.chunk.js:110042)
    at scheduleWork (VM77 0.chunk.js:129702)
    at Object.enqueueSetState (VM77 0.chunk.js:122921)
    at FormControl.push../node_modules/react/cjs/react.development.js.Component.setState (VM77 0.chunk.js:139977)
    at Object.FormControl._this.handleClean [as onEmpty] (VM77 0.chunk.js:9830)
    at InputBase.checkDirty (VM77 0.chunk.js:14100)
    at InputBase.componentDidUpdate (VM77 0.chunk.js:14078)
    at commitLifeCycles (VM77 0.chunk.js:126998)
    at commitAllLifeCycles (VM77 0.chunk.js:128497)
    at HTMLUnknownElement.callCallback (VM77 0.chunk.js:110132)
    at Object.invokeGuardedCallbackDev (VM77 0.chunk.js:110181)
    at invokeGuardedCallback (VM77 0.chunk.js:110235)
    at commitRoot (VM77 0.chunk.js:128702)
    at completeRoot (VM77 0.chunk.js:130232)
    at performWorkOnRoot (VM77 0.chunk.js:130155)
    at performWork (VM77 0.chunk.js:130060)
    at performSyncWork (VM77 0.chunk.js:130034)
    at interactiveUpdates$1 (VM77 0.chunk.js:130322)
    at interactiveUpdates (VM77 0.chunk.js:112252)
    at dispatchInteractiveEvent (VM77 0.chunk.js:115068)
```


## Steps to Reproduce 🕹
<!---
    Provide a link to a live example (you can use codesandbox.io) and an unambiguous set of steps to reproduce this bug.
    Include code to reproduce, if relevant (which it most likely is).

    This codesandbox.io template _may_ be a good starting point:
    https://codesandbox.io/s/github/mui-org/material-ui/tree/master/examples/create-react-app

    If you're using typescript a better starting point would be
    https://codesandbox.io/s/github/mui-org/material-ui/tree/master/examples/create-react-app-with-typescript

    If YOU DO NOT take time to provide a codesandbox.io reproduction, should the COMMUNITY take time to help you?

-->
Unfortunately, we cannot reproduce this Exception using codesandbox.

This is basically the code for our TextField.
The crash occurs only if a value is given for the Select Element.

```
render() {
    const { classes } = this.props;

    const inputProps = {};
    inputProps.endAdornment = this.createEndAdornment();

    return (
      <MuiThemeProvider theme={theme}>
        <MuiPickersUtilsProvider utils={DateFnsUtils}>
          <Provider store={store}>
            <div className={classes.root}>
              <TextField value="123" InputProps={inputProps} />
            </div>
          </Provider>
        </MuiPickersUtilsProvider>
      </MuiThemeProvider>
    );
  }

  createEndAdornment = () => {
    return (
    <InputAdornment position="end">
      <Select value="kg">
        <MenuItem key="kg" value="kg">
          kg
        </MenuItem>
        <MenuItem key="gram" value="gram">
          gram
        </MenuItem>
      </Select>
    </InputAdornment>
    );
  };
```

## Your Environment 🌎
<!---
    Include as many relevant details about the environment with which you experienced the bug.
    If you encounter issues with typescript please include version and tsconfig.
-->

| Tech         | Version |
|--------------|---------|
| Material-UI  | v3.9.1  |
| React        | v16.7.0       |
| Browser      | Chrome and Firefox       |

### package.json
```
"dependencies": {
    "@date-io/date-fns": "^1.0.2",
    "@material-ui/core": "^3.9.0",
    "@material-ui/icons": "^3.0.2",
    "ajv": "^6.7.0",
    "autosuggest-highlight": "^3.1.1",
    "core-js": "^2.6.3",
    "date-fns": "^2.0.0-alpha.27",
    "fetch-mock": "^7.3.0",
    "file-saver": "^2.0.0",
    "lodash": "^4.17.11",
    "material-ui-pickers": "^2.1.2",
    "prop-types": "^15.6.2",
    "react": "^16.7.0",
    "react-autosuggest": "^9.4.3",
    "react-dom": "^16.7.0",
    "react-dropzone": "^6.2.4",
    "react-markdown": "^4.0.6",
    "react-redux": "^5.1.1",
    "react-scripts": "^.1.3",
    "redux": "^4.0.1",
    "redux-thunk": "^2.3.0",
    "socket.io-client": "^2.2.0"
  }
```

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-14364/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-14364/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-14364/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-14364/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
ls packages/material-ui/src/InputBase packages/material-ui/src/FormControl && cat packages/material-ui/src/FormControl/withFormControlContext.js packages/material-ui/src/FormControl/FormControlContext.js && grep -n "checkDirty\|muiFormControl\|componentDidUpdate\|adornment\|Adornment" packages/material-ui/src/InputBase/InputBase.js
```

tool result:

```
packages/material-ui/src/FormControl:
FormControl.d.ts
FormControl.js
FormControl.spec.tsx
FormControl.test.js
FormControlContext.d.ts
FormControlContext.js
formControlState.js
index.d.ts
index.js
withFormControlContext.js

packages/material-ui/src/InputBase:
InputBase.d.ts
InputBase.js
InputBase.test.js
Textarea.d.ts
Textarea.js
Textarea.test.js
index.d.ts
index.js
utils.js
utils.test.js
import React from 'react';
import hoistNonReactStatics from 'hoist-non-react-statics';
import FormControlContext from './FormControlContext';
import { getDisplayName } from '@material-ui/utils';

export default function withFormControlContext(Component) {
  const EnhancedComponent = props => (
    <FormControlContext.Consumer>
      {context => <Component muiFormControl={context} {...props} />}
    </FormControlContext.Consumer>
  );

  if (process.env.NODE_ENV !== 'production') {
    EnhancedComponent.displayName = `WithFormControlContext(${getDisplayName(Component)})`;
  }

  hoistNonReactStatics(EnhancedComponent, Component);

  return EnhancedComponent;
}
import React from 'react';

/**
 * @ignore - internal component.
 */
const FormControlContext = React.createContext();

export default FormControlContext;
54:    /* Styles applied to the root element if `startAdornment` is provided. */
56:    /* Styles applied to the root element if `endAdornment` is provided. */
135:    /* Styles applied to the `input` element if `startAdornment` is provided. */
137:    /* Styles applied to the `input` element if `endAdornment` is provided. */
161:      this.checkDirty(props);
171:      this.checkDirty(this.inputRef);
175:  componentDidUpdate(prevProps) {
178:      const { muiFormControl } = this.props;
179:      if (muiFormControl && muiFormControl.onBlur) {
180:        muiFormControl.onBlur();
184:      this.checkDirty(this.props);
189:    const { muiFormControl } = this.props;
192:    if (formControlState({ props: this.props, muiFormControl, states: ['disabled'] }).disabled) {
202:    if (muiFormControl && muiFormControl.onFocus) {
203:      muiFormControl.onFocus(event);
213:    const { muiFormControl } = this.props;
214:    if (muiFormControl && muiFormControl.onBlur) {
215:      muiFormControl.onBlur(event);
221:      this.checkDirty(this.inputRef);
263:  checkDirty(obj) {
264:    const { muiFormControl } = this.props;
267:      if (muiFormControl && muiFormControl.onFilled) {
268:        muiFormControl.onFilled();
276:    if (muiFormControl && muiFormControl.onEmpty) {
277:      muiFormControl.onEmpty();
292:      endAdornment,
300:      muiFormControl,
316:      startAdornment,
327:      muiFormControl,
331:    const focused = muiFormControl ? muiFormControl.focused : this.state.focused;
340:        [classes.formControl]: muiFormControl,
343:        [classes.adornedStart]: startAdornment,
344:        [classes.adornedEnd]: endAdornment,
357:        [classes.inputAdornedStart]: startAdornment,
358:        [classes.inputAdornedEnd]: endAdornment,
402:              startAdornment,
406:        {startAdornment}
431:        {endAdornment}
475:   * End `InputAdornment` for this component.
477:  endAdornment: PropTypes.node,
512:  muiFormControl: PropTypes.object,
582:   * Start `InputAdornment` for this component.
584:  startAdornment: PropTypes.node,
```

**tool call: Bash**

```bash
git log --oneline -3; sed -n 1,60p packages/material-ui/src/InputAdornment/InputAdornment.js; grep -n "muiFormControl\|Context\|render()" -A2 packages/material-ui/src/InputAdornment/InputAdornment.js | head -40; ls packages/material-ui/src/InputAdornment
```

tool result:

```
b5d9b243d [docs] Remove recompose/compose (#14421)
937b1623a [core] Enable innerRef on ListItem and MenuItem (#14423)
cce90f18f [core] Use common copy-files script (#14406)
import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import { componentPropType } from '@material-ui/utils';
import warning from 'warning';
import Typography from '../Typography';
import withStyles from '../styles/withStyles';
import withFormControlContext from '../FormControl/withFormControlContext';

export const styles = {
  /* Styles applied to the root element. */
  root: {
    display: 'flex',
    height: '0.01em', // Fix IE 11 flexbox alignment. To remove at some point.
    maxHeight: '2em',
    alignItems: 'center',
  },
  /* Styles applied to the root element if `variant="filled"`. */
  filled: {
    '&$positionStart': {
      marginTop: 16,
    },
  },
  /* Styles applied to the root element if `position="start"`. */
  positionStart: {
    marginRight: 8,
  },
  /* Styles applied to the root element if `position="end"`. */
  positionEnd: {
    marginLeft: 8,
  },
  /* Styles applied to the root element if `disablePointerEvents=true`. */
  disablePointerEvents: {
    pointerEvents: 'none',
  },
};

function InputAdornment(props) {
  const {
    children,
    component: Component,
    classes,
    className,
    disablePointerEvents,
    disableTypography,
    muiFormControl,
    position,
    variant: variantProp,
    ...other
  } = props;

  let variant = variantProp;

  if (variantProp && muiFormControl) {
    warning(
      variantProp !== muiFormControl.variant,
      'Material-UI: The `InputAdornment` variant infers the variant property ' +
        'you do not have to provide one.',
    );
  }
8:import withFormControlContext from '../FormControl/withFormControlContext';
9-
10-export const styles = {
--
46:    muiFormControl,
47-    position,
48-    variant: variantProp,
--
54:  if (variantProp && muiFormControl) {
55-    warning(
56:      variantProp !== muiFormControl.variant,
57-      'Material-UI: The `InputAdornment` variant infers the variant property ' +
58-        'you do not have to provide one.',
--
62:  if (muiFormControl && !variant) {
63:    variant = muiFormControl.variant;
64-  }
65-
--
120:  muiFormControl: PropTypes.object,
121-  /**
122-   * The position this adornment should appear relative to the `Input`.
--
140:  withFormControlContext(InputAdornment),
141-);
InputAdornment.d.ts
InputAdornment.js
InputAdornment.test.js
index.d.ts
index.js
```

**tool call: Bash**

```bash
grep -n "Adornment\|nested\|Select" packages/material-ui/src/InputBase/InputBase.test.js packages/material-ui/src/FormControl/FormControl.test.js | head -30; sed -n 255,440p packages/material-ui/src/InputBase/InputBase.js
```

tool result:

```
packages/material-ui/src/InputBase/InputBase.test.js:12:import InputAdornment from '../InputAdornment';
packages/material-ui/src/InputBase/InputBase.test.js:469:  describe('prop: startAdornment, prop: endAdornment', () => {
packages/material-ui/src/InputBase/InputBase.test.js:472:        <InputBase startAdornment={<InputAdornment position="start">$</InputAdornment>} />,
packages/material-ui/src/InputBase/InputBase.test.js:479:        InputAdornment,
packages/material-ui/src/InputBase/InputBase.test.js:485:        <InputBase endAdornment={<InputAdornment position="end">$</InputAdornment>} />,
packages/material-ui/src/InputBase/InputBase.test.js:492:        InputAdornment,
packages/material-ui/src/FormControl/FormControl.test.js:5:import Select from '../Select';
packages/material-ui/src/FormControl/FormControl.test.js:107:    it('should be adorned with an endAdornment', () => {
packages/material-ui/src/FormControl/FormControl.test.js:110:          <Input endAdornment={<div />} />
packages/material-ui/src/FormControl/FormControl.test.js:116:    it('should be adorned with a startAdornment', () => {
packages/material-ui/src/FormControl/FormControl.test.js:119:          <Input startAdornment={<div />} />
packages/material-ui/src/FormControl/FormControl.test.js:127:    it('should not be adorned without a startAdornment', () => {
packages/material-ui/src/FormControl/FormControl.test.js:130:          <Select value="" />
packages/material-ui/src/FormControl/FormControl.test.js:136:    it('should be adorned with a startAdornment', () => {
packages/material-ui/src/FormControl/FormControl.test.js:139:          <Select value="" input={<Input startAdornment={<div />} />} />
      this.inputRef.focus();
    }

    if (this.props.onClick) {
      this.props.onClick(event);
    }
  };

  checkDirty(obj) {
    const { muiFormControl } = this.props;

    if (isFilled(obj)) {
      if (muiFormControl && muiFormControl.onFilled) {
        muiFormControl.onFilled();
      }
      if (this.props.onFilled) {
        this.props.onFilled();
      }
      return;
    }

    if (muiFormControl && muiFormControl.onEmpty) {
      muiFormControl.onEmpty();
    }
    if (this.props.onEmpty) {
      this.props.onEmpty();
    }
  }

  render() {
    const {
      autoComplete,
      autoFocus,
      classes,
      className: classNameProp,
      defaultValue,
      disabled,
      endAdornment,
      error,
      fullWidth,
      id,
      inputComponent,
      inputProps: { className: inputPropsClassName, ...inputPropsProp } = {},
      inputRef,
      margin,
      muiFormControl,
      multiline,
      name,
      onBlur,
      onChange,
      onClick,
      onEmpty,
      onFilled,
      onFocus,
      onKeyDown,
      onKeyUp,
      placeholder,
      readOnly,
      renderPrefix,
      rows,
      rowsMax,
      startAdornment,
      type,
      value,
      ...other
    } = this.props;

    const ariaDescribedby = other['aria-describedby'];
    delete other['aria-describedby'];

    const fcs = formControlState({
      props: this.props,
      muiFormControl,
      states: ['disabled', 'error', 'margin', 'required', 'filled'],
    });

    const focused = muiFormControl ? muiFormControl.focused : this.state.focused;

    const className = classNames(
      classes.root,
      {
        [classes.disabled]: fcs.disabled,
        [classes.error]: fcs.error,
        [classes.fullWidth]: fullWidth,
        [classes.focused]: focused,
        [classes.formControl]: muiFormControl,
        [classes.marginDense]: fcs.margin === 'dense',
        [classes.multiline]: multiline,
        [classes.adornedStart]: startAdornment,
        [classes.adornedEnd]: endAdornment,
      },
      classNameProp,
    );

    const inputClassName = classNames(
      classes.input,
      {
        [classes.disabled]: fcs.disabled,
        [classes.inputType]: type !== 'text',
        [classes.inputTypeSearch]: type === 'search',
        [classes.inputMultiline]: multiline,
        [classes.inputMarginDense]: fcs.margin === 'dense',
        [classes.inputAdornedStart]: startAdornment,
        [classes.inputAdornedEnd]: endAdornment,
      },
      inputPropsClassName,
    );

    let InputComponent = inputComponent;
    let inputProps = {
      ...inputPropsProp,
      ref: this.handleRefInput,
    };

    if (typeof InputComponent !== 'string') {
      inputProps = {
        // Rename ref to inputRef as we don't know the
        // provided `inputComponent` structure.
        inputRef: this.handleRefInput,
        type,
        ...inputProps,
        ref: null,
      };
    } else if (multiline) {
      if (rows && !rowsMax) {
        InputComponent = 'textarea';
      } else {
        inputProps = {
          rowsMax,
          textareaRef: this.handleRefInput,
          ...inputProps,
          ref: null,
        };
        InputComponent = Textarea;
      }
    } else {
      inputProps = {
        type,
        ...inputProps,
      };
    }

    return (
      <div className={className} onClick={this.handleClick} {...other}>
        {renderPrefix
          ? renderPrefix({
              ...fcs,
              startAdornment,
              focused,
            })
          : null}
        {startAdornment}
        <FormControlContext.Provider value={null}>
          <InputComponent
            aria-invalid={fcs.error}
            aria-describedby={ariaDescribedby}
            autoComplete={autoComplete}
            autoFocus={autoFocus}
            className={inputClassName}
            defaultValue={defaultValue}
            disabled={fcs.disabled}
            id={id}
            name={name}
            onBlur={this.handleBlur}
            onChange={this.handleChange}
            onFocus={this.handleFocus}
            onKeyDown={onKeyDown}
            onKeyUp={onKeyUp}
            placeholder={placeholder}
            readOnly={readOnly}
            required={fcs.required}
            rows={rows}
            value={value}
            {...in
[... 287 more characters not shown]
```

**tool call: Bash**

```bash
grep -n "handleClean\|handleDirty\|handleFocus\|handleBlur" -A10 packages/material-ui/src/FormControl/FormControl.js | head -60
```

tool result:

```
91:  handleFocus = () => {
92-    this.setState(state => (!state.focused ? { focused: true } : null));
93-  };
94-
95:  handleBlur = () => {
96-    this.setState(state => (state.focused ? { focused: false } : null));
97-  };
98-
99:  handleDirty = () => {
100-    if (!this.state.filled) {
101-      this.setState({ filled: true });
102-    }
103-  };
104-
105:  handleClean = () => {
106-    if (this.state.filled) {
107-      this.setState({ filled: false });
108-    }
109-  };
110-
111-  render() {
112-    const {
113-      classes,
114-      className,
115-      component: Component,
--
133:      onBlur: this.handleBlur,
134:      onEmpty: this.handleClean,
135:      onFilled: this.handleDirty,
136:      onFocus: this.handleFocus,
137-      required,
138-      variant,
139-    };
140-
141-    return (
142-      <FormControlContext.Provider value={childContext}>
143-        <Component
144-          className={classNames(
145-            classes.root,
146-            {
```

**tool call: Bash**

```bash
sed -n 60,110p packages/material-ui/src/InputAdornment/InputAdornment.js; grep -n "\"test" package.json
```

tool result:

```
  }

  if (muiFormControl && !variant) {
    variant = muiFormControl.variant;
  }

  return (
    <Component
      className={classNames(
        classes.root,
        {
          [classes.filled]: variant === 'filled',
          [classes.positionStart]: position === 'start',
          [classes.positionEnd]: position === 'end',
          [classes.disablePointerEvents]: disablePointerEvents,
        },
        className,
      )}
      {...other}
    >
      {typeof children === 'string' && !disableTypography ? (
        <Typography color="textSecondary">{children}</Typography>
      ) : (
        children
      )}
    </Component>
  );
}

InputAdornment.propTypes = {
  /**
   * The content of the component, normally an `IconButton` or string.
   */
  children: PropTypes.node.isRequired,
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
  component: componentPropType,
  /**
   * Disable pointer events on the root.
   * This allows for the content of the adornment to focus the input on click.
47:    "test": "yarn lint && yarn typescript && yarn test:coverage",
48:    "test:coverage": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha 'packages/**/*.test.js' 'docs/**/*.test.js' --exclude '**/node_modules/**' && nyc report -r lcovonly",
49:    "test:coverage:html": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha 'packages/material-ui/**/*.test.js' 'packages/material-ui-utils/**/*.test.js' 'packages/material-ui-styles/**/*.test.js' --exclude '**/node_modules/**' && nyc report --reporter=html",
50:    "test:karma": "cross-env NODE_ENV=test karma start test/karma.conf.js --single-run",
51:    "test:regressions": "webpack --config test/regressions/webpack.config.js && rimraf test/regressions/screenshots/chrome/* && vrtest run --config test/vrtest.config.js --record",
52:    "test:umd": "yarn babel-node packages/material-ui/test/umd/run.js",
53:    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/*.test.js' 'docs/**/*.test.js' --exclude '**/node_modules/**'",
54:    "test:watch": "yarn test:unit --watch",
```

**assistant:** Now a reproduction test:

**tool call: Bash**

```bash
cat > packages/material-ui/src/InputAdornment/repro.test.js <<'EOF'
import React from 'react';
import { assert } from 'chai';
import { createMount } from '@material-ui/core/test-utils';
import TextField from '../TextField';
import Select from '../Select';
import MenuItem from '../MenuItem';
import InputAdornment from './InputAdornment';

describe('repro', () => {
  it('should not loop with a Select in an adornment', () => {
    const mount = createMount();
    const wrapper = mount(
      <TextField
        value=""
        InputProps={{
          endAdornment: (
            <InputAdornment position="end">
              <Select value="kg">
                <MenuItem value="kg">kg</MenuItem>
              </Select>
            </InputAdornment>
          ),
        }}
      />,
    );
    wrapper.setProps({ value: '' });
    assert.ok(true);
    mount.cleanUp();
  });
});
EOF
/work/mui__material-ui-14364/bin/envrun 'NODE_ENV=test npx mocha packages/material-ui/src/InputAdornment/repro.test.js 2>&1 | tail -20'
```

tool result:

```
Command did not complete within its 120s timeout and was moved to the background (ID: bk7hzg0c7). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/d707a824-1bef-4c58-97bd-b6ddc086d94a/tasks/bk7hzg0c7.output. You will be notified when it completes. To check interim output, use Read on that file path.
```

**tool call: Bash**

```bash
sleep 90; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/d707a824-1bef-4c58-97bd-b6ddc086d94a/tasks/bk7hzg0c7.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
cat /work/mui__material-ui-14364/repo/.mocharc* /work/mui__material-ui-14364/repo/test/mocha.opts 2>/dev/null; /work/mui__material-ui-14364/bin/envrun 'ps aux | grep -c mocha'
```

tool result:

```
(eval):1: no matches found: /work/mui__material-ui-14364/repo/.mocharc*
7
```

**tool call: Bash**

```bash
sleep 60; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/d707a824-1bef-4c58-97bd-b6ddc086d94a/tasks/bk7hzg0c7.output; ls test; cat test/mocha.opts 2>/dev/null
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
test/utils/setup.js
```

**tool call: Bash**

```bash
/work/mui__material-ui-14364/bin/envrun 'pkill -f mocha; time (NODE_ENV=test timeout 300 npx mocha packages/material-ui/src/InputAdornment/InputAdornment.test.js 2>&1 | tail -5)'
```

tool result:

```
Exit code 143
```

**tool call: Bash**

```bash
/work/mui__material-ui-14364/bin/envrun 'time (NODE_ENV=test timeout 300 npx mocha packages/material-ui/src/InputAdornment/InputAdornment.test.js 2>&1 | tail -5)'
```

tool result:

```
  ․․․․․․․․․․․․․

  13 passing (275ms)


real	5m0.037s
user	0m0.675s
sys	0m0.071s
```

**assistant:** The existing tests pass quickly, but mocha doesn't exit afterward because something keeps the process open. I'll add `--exit` and run the reproduction.

**tool call: Bash**

```bash
/work/mui__material-ui-14364/bin/envrun 'NODE_ENV=test timeout 200 npx mocha --exit packages/material-ui/src/InputAdornment/repro.test.js 2>&1 | grep -v "^\s*at " | head -30'
```

tool result:

```
Browserslist: caniuse-lite is outdated. Please run next command `yarn upgrade caniuse-lite browserslist`

Error: Uncaught [Invariant Violation: Maximum update depth exceeded. This can happen when a component repeatedly calls setState inside componentWillUpdate or componentDidUpdate. React limits the number of nested updates to prevent infinite loops.]
  framesToPop: 1
}

  !

  0 passing (321ms)
  1 failing

  1) repro
       should not loop with a Select in an adornment:
     Error: Uncaught [Invariant Violation: Maximum update depth exceeded. This can happen when a component repeatedly calls setState inside componentWillUpdate or componentDidUpdate. React limits the number of nested updates to prevent infinite loops.]
  Error: Error: Uncaught [Invariant Violation: Maximum update depth exceeded. This can happen when a component repeatedly calls setState inside componentWillUpdate or componentDidUpdate. React limits the number of nested updates to prevent infinite loops.]
```

**thinking:**

```
Found it: the `Select` inside the adornment reads the outer `TextField`'s `FormControl` context, causing `onFilled`/`onEmpty` to flip-flop and hit React's update-depth limit. I'll fix this by resetting the context to `null` in `InputAdornment` for its children, like `InputBase` already does.


```

**tool call: Bash**

```bash
cd packages/material-ui/src/InputAdornment && python3 - <<'EOF'
p='InputAdornment.js'
s=open(p).read()
s=s.replace("""import withFormControlContext from '../FormControl/withFormControlContext';
""","""import withFormControlContext from '../FormControl/withFormControlContext';
import FormControlContext from '../FormControl/FormControlContext';
""")
old_start="""  return (
    <Component
"""
assert old_start in s
s=s.replace(old_start,"""  return (
    <FormControlContext.Provider value={null}>
      <Component
""")
old_end="""      {typeof children === 'string' && !disableTypography ? (
        <Typography color="textSecondary">{children}</Typography>
      ) : (
        children
      )}
    </Component>
  );"""
assert old_end in s
s=s.replace(old_end,"""        {typeof children === 'string' && !disableTypography ? (
          <Typography color="textSecondary">{children}</Typography>
        ) : (
          children
        )}
      </Component>
    </FormControlContext.Provider>
  );""")
open(p,'w').write(s)
EOF
cd /work/mui__material-ui-14364/repo && npx prettier --version >/dev/null 2>&1; /work/mui__material-ui-14364/bin/envrun 'npx prettier --write packages/material-ui/src/InputAdornment/InputAdornment.js && npx eslint packages/material-ui/src/InputAdornment/InputAdornment.js && git diff'
```

tool result:

```
<persisted-output>
Output too large (32.6KB). Full output saved to: <actor-session-dir>

Preview (first 2KB):
packages/material-ui/src/InputAdornment/InputAdornment.js 124ms
diff --git a/package.json b/package.json
index 0e05925d0..417646e1a 100644
--- a/package.json
+++ b/package.json
@@ -73,12 +73,17 @@
     "@date-io/date-fns": "^1.0.0",
     "@emotion/core": "^10.0.0",
     "@emotion/styled": "^10.0.0",
+    "@types/chai": "^5.2.2",
+    "@types/chai-dom": "^1.11.3",
     "@types/classnames": "^2.2.6",
     "@types/enzyme": "^3.1.4",
+    "@types/format-util": "^1.0.4",
+    "@types/prop-types": "^15.7.15",
     "@types/react": "^16.7.10",
-    "@types/react-dom": "^16.0.9",
+    "@types/react-dom": "^19.1.8",
     "@types/react-router-dom": "^4.3.1",
     "@types/react-text-mask": "^5.4.2",
+    "@types/sinon": "^17.0.4",
     "@weco/next-plugin-transpile-modules": "0.0.2",
     "accept-language": "^3.0.18",
     "argos-cli": "^0.0.9",
diff --git a/packages/material-ui/src/InputAdornment/InputAdornment.js b/packages/material-ui/src/InputAdornment/InputAdornment.js
index 52493e3b0..7e87c968a 100644
--- a/packages/material-ui/src/InputAdornment/InputAdornment.js
+++ b/packages/material-ui/src/InputAdornment/InputAdornment.js
@@ -6,6 +6,7 @@ import warning from 'warning';
 import Typography from '../Typography';
 import withStyles from '../styles/withStyles';
 import withFormControlContext from '../FormControl/withFormControlContext';
+import FormControlContext from '../FormControl/FormControlContext';
 
 export const styles = {
   /* Styles applied to the root element. */
@@ -64,25 +65,27 @@ function InputAdornment(props) {
   }
 
   return (
-    <Component
-      className={classNames(
-        classes.root,
-        {
-          [classes.filled]: variant === 'filled',
-          [classes.positionStart]: position === 'start',
-          [classes.positionEnd]: position === 'end',
-          [classes.disablePointerEvents]: disablePointerEvents,
-        },
-        className,
-      )}
-      {...other}
-    >
...
</persisted-output>
```

**assistant:** Prettier and ESLint pass. The diff also shows changes to `package.json`, which I didn't touch, so I'll check where they came from.

**tool call: Bash**

```bash
git status --short; git stash list; stat -f '%Sm' package.json packages/material-ui/src/InputAdornment/InputAdornment.js
```

tool result:

```
 M package.json
 M packages/material-ui/src/InputAdornment/InputAdornment.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
?? packages/material-ui/src/InputAdornment/repro.test.js
Aug 27 21:36:01 2025
Oct  9 01:40:36 2026
```

**thinking:**

```
The package.json, yarn.lock, Dockerfile, and custom-reporter.js changes are pre-existing from the environment setup, so I'll leave them untouched. Now I'll rerun the reproduction and the nearby test suites.


```

**tool call: Bash**

```bash
/work/mui__material-ui-14364/bin/envrun 'NODE_ENV=test timeout 250 npx mocha --exit packages/material-ui/src/InputAdornment/*.test.js packages/material-ui/src/InputBase/*.test.js packages/material-ui/src/Input/*.test.js packages/material-ui/src/FormControl/*.test.js packages/material-ui/src/TextField/*.test.js packages/material-ui/src/Select/*.test.js packages/material-ui/src/FilledInput/*.test.js packages/material-ui/src/OutlinedInput/*.test.js 2>&1 | grep -v Browserslist | tail -15'
```

tool result:

```
  ․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․
  ․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․
  ․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․․
  ․․․․

  172 passing (1s)
```

**thinking:**

```
All 172 tests pass, including existing InputAdornment variant inference tests. Now I'll remove the reproduction file.


```

**tool call: Bash**

```bash
rm packages/material-ui/src/InputAdornment/repro.test.js && git status --short && git diff packages/material-ui/src/InputAdornment/InputAdornment.js | head -20
```

tool result:

```
 M package.json
 M packages/material-ui/src/InputAdornment/InputAdornment.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
diff --git a/packages/material-ui/src/InputAdornment/InputAdornment.js b/packages/material-ui/src/InputAdornment/InputAdornment.js
index 52493e3b0..7e87c968a 100644
--- a/packages/material-ui/src/InputAdornment/InputAdornment.js
+++ b/packages/material-ui/src/InputAdornment/InputAdornment.js
@@ -6,6 +6,7 @@ import warning from 'warning';
 import Typography from '../Typography';
 import withStyles from '../styles/withStyles';
 import withFormControlContext from '../FormControl/withFormControlContext';
+import FormControlContext from '../FormControl/FormControlContext';
 
 export const styles = {
   /* Styles applied to the root element. */
@@ -64,25 +65,27 @@ function InputAdornment(props) {
   }
 
   return (
-    <Component
-      className={classNames(
-        classes.root,
-        {
```

**assistant:** I fixed the crash: a `Select` inside an `InputAdornment` no longer causes the "Maximum update depth exceeded" error.

**Cause:** The `Select` in the adornment was picking up the surrounding `TextField`'s `FormControl` context. After every update, the `Select`'s input (value `"kg"`) told the `FormControl` it was filled, and the main input (value `""`) told it it was empty. The two reports kept overriding each other, so React hit its update limit and threw. `InputBase` already shields its own input element by resetting this context to `null`, but nothing did the same for adornments.

**Fix:** In `packages/material-ui/src/InputAdornment/InputAdornment.js`, the adornment's content is now wrapped in `<FormControlContext.Provider value={null}>`. Anything rendered inside an adornment is now cut off from the outer `FormControl`. The adornment itself still reads the context, so it still picks up the `FormControl`'s variant (for example `filled`).

**Verification:**
- I reproduced the error with a temporary test: a `TextField` with `value=""` and a `Select value="kg"` in its `endAdornment`, re-rendered once.
- After the fix, that test passes, along with all 172 tests in the InputAdornment, InputBase, Input, FilledInput, OutlinedInput, FormControl, TextField and Select suites. Prettier and ESLint pass on the changed file.
- I've deleted the temporary test.

The repo also has changes I didn't make, which were there before I started: modified `package.json` and `yarn.lock`, plus untracked `Dockerfile` and `custom-reporter.js`. I left them alone.

_session end: success, turns 17, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.13 s: ps aux | grep -c mocha
- `rc=143` 0.15 s: pkill -f mocha; time (NODE_ENV=test timeout 300 npx mocha packages/material-ui/src/InputAdornment/InputAdornment.test.js 2>&1 | tail -5)
- `rc=143` 279.26 s: NODE_ENV=test npx mocha packages/material-ui/src/InputAdornment/repro.test.js 2>&1 | tail -20
- `rc=0` 300.17 s: time (NODE_ENV=test timeout 300 npx mocha packages/material-ui/src/InputAdornment/InputAdornment.test.js 2>&1 | tail -5)
- `rc=0` 2.58 s: NODE_ENV=test timeout 200 npx mocha --exit packages/material-ui/src/InputAdornment/repro.test.js 2>&1 | grep -v "^\s*at " | head -30
- `rc=0` 5.8 s: npx prettier --write packages/material-ui/src/InputAdornment/InputAdornment.js && npx eslint packages/material-ui/src/InputAdornment/InputAdornment.js && git diff
- `rc=0` 4.38 s: NODE_ENV=test timeout 250 npx mocha --exit packages/material-ui/src/InputAdornment/*.test.js packages/material-ui/src/InputBase/*.test.js packages/material-ui/src/Input/*.test.js packages/material-ui/src/FormControl/*.test.js packages/material-ui/src/TextField/*.test.js packages/material-ui/src/Select/*.test.js packages/material-ui/src/FilledInput/*.test.js packages/material-ui/src/OutlinedInput/*.test.js 2>&1 | grep -v Browserslist | tail -15
