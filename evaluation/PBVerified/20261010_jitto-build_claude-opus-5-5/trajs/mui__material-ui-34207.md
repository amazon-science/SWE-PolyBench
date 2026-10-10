# Instance: mui__material-ui-34207

- Final resolved (evaluator, logs/mui__material-ui-34207_result.json): True
- Run state: DONE
- One attempt. Duration 267.3 s, turns 9, actor cost $0.27700040000000004, container commands 5
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/mui__material-ui-34207/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-34207/repo. Consider the following issue description:

<issue_description>
[FormControlLabel] Support `required`
### Duplicates

- [X] I have searched the existing issues

### Latest version

- [X] I have tested the latest version

### Current behavior 😯

Implementing a labeled checkbox with a "required" asterisk, such as the following, is currently not possible without workarounds:

![image](https://user-images.githubusercontent.com/7543552/188464851-dd8f884d-3d66-4e47-b630-67d2c6cdba4b.png)

This would normally be coded like this:

```tsx
<FormControlLabel required label={label} control={<Checkbox />} />
```

but [`FormControlLabel`](https://mui.com/material-ui/api/form-control-label/) doesn't support the `required` prop.

### Expected behavior 🤔

`FormControlLabel` supports the `required` prop.

### Steps to reproduce 🕹

_No response_

### Context 🔦

Related issues:
- https://github.com/mui/material-ui/issues/11038
- https://github.com/mui/material-ui/issues/12180


We would be willing to contribute this feature, if this gets the green light.

### Your environment 🌎

_No response_

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-34207/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-34207/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-34207/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-34207/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/mui__material-ui-34207/repo/packages/mui-material/src/FormControlLabel && ls && cat FormControlLabel.js FormControlLabel.d.ts formControlLabelClasses.ts; grep -n "asterisk" -A12 ../FormLabel/FormLabel.js | head -60
```

tool result:

```
FormControlLabel.d.ts
FormControlLabel.js
FormControlLabel.test.js
formControlLabelClasses.ts
index.d.ts
index.js
import * as React from 'react';
import PropTypes from 'prop-types';
import clsx from 'clsx';
import { refType } from '@mui/utils';
import { unstable_composeClasses as composeClasses } from '@mui/base';
import { useFormControl } from '../FormControl';
import Typography from '../Typography';
import capitalize from '../utils/capitalize';
import styled from '../styles/styled';
import useThemeProps from '../styles/useThemeProps';
import formControlLabelClasses, {
  getFormControlLabelUtilityClasses,
} from './formControlLabelClasses';
import formControlState from '../FormControl/formControlState';

const useUtilityClasses = (ownerState) => {
  const { classes, disabled, labelPlacement, error } = ownerState;
  const slots = {
    root: [
      'root',
      disabled && 'disabled',
      `labelPlacement${capitalize(labelPlacement)}`,
      error && 'error',
    ],
    label: ['label', disabled && 'disabled'],
  };

  return composeClasses(slots, getFormControlLabelUtilityClasses, classes);
};

export const FormControlLabelRoot = styled('label', {
  name: 'MuiFormControlLabel',
  slot: 'Root',
  overridesResolver: (props, styles) => {
    const { ownerState } = props;

    return [
      { [`& .${formControlLabelClasses.label}`]: styles.label },
      styles.root,
      styles[`labelPlacement${capitalize(ownerState.labelPlacement)}`],
    ];
  },
})(({ theme, ownerState }) => ({
  display: 'inline-flex',
  alignItems: 'center',
  cursor: 'pointer',
  // For correct alignment with the text.
  verticalAlign: 'middle',
  WebkitTapHighlightColor: 'transparent',
  marginLeft: -11,
  marginRight: 16, // used for row presentation of radio/checkbox
  [`&.${formControlLabelClasses.disabled}`]: {
    cursor: 'default',
  },
  ...(ownerState.labelPlacement === 'start' && {
    flexDirection: 'row-reverse',
    marginLeft: 16, // used for row presentation of radio/checkbox
    marginRight: -11,
  }),
  ...(ownerState.labelPlacement === 'top' && {
    flexDirection: 'column-reverse',
    marginLeft: 16,
  }),
  ...(ownerState.labelPlacement === 'bottom' && {
    flexDirection: 'column',
    marginLeft: 16,
  }),
  [`& .${formControlLabelClasses.label}`]: {
    [`&.${formControlLabelClasses.disabled}`]: {
      color: (theme.vars || theme).palette.text.disabled,
    },
  },
}));

/**
 * Drop-in replacement of the `Radio`, `Switch` and `Checkbox` component.
 * Use this component if you want to display an extra label.
 */
const FormControlLabel = React.forwardRef(function FormControlLabel(inProps, ref) {
  const props = useThemeProps({ props: inProps, name: 'MuiFormControlLabel' });
  const {
    checked,
    className,
    componentsProps = {},
    control,
    disabled: disabledProp,
    disableTypography,
    inputRef,
    label: labelProp,
    labelPlacement = 'end',
    name,
    onChange,
    slotProps = {},
    value,
    ...other
  } = props;

  const muiFormControl = useFormControl();

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

  ['checked', 'name', 'onChange', 'value', 'inputRef'].forEach((key) => {
    if (typeof control.props[key] === 'undefined' && typeof props[key] !== 'undefined') {
      controlProps[key] = props[key];
    }
  });

  const fcs = formControlState({
    props,
    muiFormControl,
    states: ['error'],
  });

  const ownerState = {
    ...props,
    disabled,
    labelPlacement,
    error: fcs.error,
  };

  const classes = useUtilityClasses(ownerState);

  const typographySlotProps = slotProps.typography ?? componentsProps.typography;

  let label = labelProp;
  if (label != null && label.type !== Typography && !disableTypography) {
    label = (
      <Typography
        component="span"
        {...typographySlotProps}
        className={clsx(classes.label, typographySlotProps?.className)}
      >
        {label}
      </Typography>
    );
  }

  return (
    <FormControlLabelRoot
      className={clsx(classes.root, className)}
      ownerState={ownerState}
      ref={ref}
      {...other}
    >
      {React.cloneElement(control, controlProps)}
      {label}
    </FormControlLabelRoot>
  );
});

FormControlLabel.propTypes /* remove-proptypes */ = {
  // ----------------------------- Warning --------------------------------
  // | These PropTypes are generated from the TypeScript type definitions |
  // |     To update them edit the d.ts file and run "yarn proptypes"     |
  // ----------------------------------------------------------------------
  /**
   * If `true`, the component appears selected.
   */
  checked: PropTypes.bool,
  /**
   * Override or extend the styles applied to the component.
   */
  classes: PropTypes.object,
  /**
   * @ignore
   */
  className: PropTypes.string,
  /**
   * The props used for each slot inside.
   * @default {}
   */
  componentsProps: PropTypes.shape({
    typography: PropTypes.object,
  }),
  /**
   * A control element. For instance, it can be a `Radio`, a `Switch` or a `Checkbox`.
   */
  control: PropTypes.element.isRequired,
  /**
   * If `true`, the control is disabled.
   */
  disabled: PropTypes.bool,
  /**
   * If `true`, the label is rendered as it is passed without an additional typography node.
   */
  disableTypography: PropTypes.bool,
  /**
   * Pass a ref to the `input` element.
   */
  inputRef: refType,
  /**
   * A text or an element to be used in an enclosing label element.
   */
  label: PropTypes.node,
  /**
   * The position of the label.
   * @default 'end'
   */
  labelPlacement: PropTypes.oneOf(['bottom', 'end', 'start', 'top']),
  /**
   * @ignore
   */
  name: PropTypes.string,
  /**
   * Callback fired when the state is changed.
   *

[... 6313 more characters not shown]
```

**assistant:** Let me look at the tests for expectations.

**tool call: Bash**

```bash
cd /work/mui__material-ui-34207/repo && grep -n -i "required\|asterisk" -B3 -A20 packages/mui-material/src/FormControlLabel/FormControlLabel.test.js | head -80
```

tool result:

```
(Bash completed with no output)
```

**assistant:** No existing tests cover `required`, so I'll follow the `FormLabel` pattern: add a `required` prop, forward it to the control, and render an asterisk with `asterisk` and `required` utility classes.

**tool call: Bash**

```bash
cd /work/mui__material-ui-34207/repo/packages/mui-material/src/FormControlLabel && python3 - <<'EOF'
import re
p='FormControlLabel.js'; s=open(p).read()
def r(a,b):
    global s
    assert a in s, a
    s=s.replace(a,b,1)
r("""  const { classes, disabled, labelPlacement, error } = ownerState;""","""  const { classes, disabled, labelPlacement, error, required } = ownerState;""")
r("""      error && 'error',
    ],
    label: ['label', disabled && 'disabled'],
""","""      error && 'error',
      required && 'required',
    ],
    label: ['label', disabled && 'disabled'],
    asterisk: ['asterisk', error && 'error'],
""")
r("""/**
 * Drop-in""","""const AsteriskComponent = styled('span', {
  name: 'MuiFormControlLabel',
  slot: 'Asterisk',
  overridesResolver: (props, styles) => styles.asterisk,
})(({ theme }) => ({
  [`&.${formControlLabelClasses.error}`]: {
    color: (theme.vars || theme).palette.error.main,
  },
}));

/**
 * Drop-in""")
r("""    onChange,
    slotProps""","""    onChange,
    required: requiredProp,
    slotProps""")
r("""  const controlProps = {
    disabled,
  };""","""  const required = requiredProp ?? control.props.required;

  const controlProps = {
    disabled,
    required,
  };""")
r("""    labelPlacement,
    error: fcs.error,""","""    labelPlacement,
    required,
    error: fcs.error,""")
r("""      {label}
    </FormControlLabelRoot>""","""      {label}
      {required && (
        <AsteriskComponent ownerState={ownerState} aria-hidden className={classes.asterisk}>
          &thinsp;{'*'}
        </AsteriskComponent>
      )}
    </FormControlLabelRoot>""")
r("""  onChange: PropTypes.func,
  /**
   * The props""","""  onChange: PropTypes.func,
  /**
   * If `true`, the label will indicate that the `input` is required.
   */
  required: PropTypes.bool,
  /**
   * The props""")
open(p,'w').write(s)

p='FormControlLabel.d.ts'; s=open(p).read()
r("""  onChange?: (event: React.SyntheticEvent, checked: boolean) => void;
""","""  onChange?: (event: React.SyntheticEvent, checked: boolean) => void;
  /**
   * If `true`, the label will indicate that the `input` is required.
   */
  required?: boolean;
""")
open(p,'w').write(s)

p='formControlLabelClasses.ts'; s=open(p).read()
r("""  error: string;
}""","""  error: string;
  /** State class applied to the root element if `required={true}`. */
  required: string;
  /** Styles applied to the asterisk element. */
  asterisk: string;
}""")
r("""    'error',
  ],""","""    'error',
    'required',
    'asterisk',
  ],""")
open(p,'w').write(s)
EOF
git diff --stat
```

tool result:

```
 package.json                                       |    11 +-
 .../src/FormControlLabel/FormControlLabel.d.ts     |     4 +
 .../src/FormControlLabel/FormControlLabel.js       |    28 +-
 .../FormControlLabel/formControlLabelClasses.ts    |     6 +
 yarn.lock                                          | 30720 ++++++++++---------
 5 files changed, 16136 insertions(+), 14633 deletions(-)
```

**assistant:** `package.json` and `yarn.lock` show as changed, but I didn't touch them. Let me check what changed there.

**tool call: Bash**

```bash
cd /work/mui__material-ui-34207/repo && git diff package.json; git log --oneline -1; git stash list
```

tool result:

```
diff --git a/package.json b/package.json
index f4f44026de..2245d7dcac 100644
--- a/package.json
+++ b/package.json
@@ -94,21 +94,24 @@
     "@slack/bolt": "^3.13.0",
     "@testing-library/dom": "^9.2.0",
     "@testing-library/react": "^14.0.0",
-    "@types/chai": "^4.3.4",
-    "@types/chai-dom": "^1.11.0",
+    "@types/chai": "^4.3.20",
+    "@types/chai-dom": "^1.11.3",
     "@types/enzyme": "^3.10.12",
-    "@types/format-util": "^1.0.2",
+    "@types/format-util": "^1.0.4",
     "@types/fs-extra": "^9.0.13",
     "@types/jsdom": "^21.1.1",
     "@types/lodash": "^4.14.192",
     "@types/mocha": "^10.0.1",
     "@types/node": "^18.11.9",
     "@types/prettier": "^2.7.2",
+    "@types/prop-types": "^15.7.15",
     "@types/react": "^18.0.26",
+    "@types/react-dom": "^19.1.8",
     "@types/react-is": "^17.0.3",
     "@types/react-test-renderer": "^18.0.0",
-    "@types/sinon": "^10.0.13",
+    "@types/sinon": "^10.0.20",
     "@types/stylis": "^4.0.2",
+    "@types/testing-library__react": "^10.2.0",
     "@types/webpack": "^5.28.0",
     "@types/yargs": "^17.0.24",
     "@typescript-eslint/eslint-plugin": "^5.53.0",
1a4263a50a  [docs][base] Move styles to the bottom of demos code for `BadgeUnstyled` (#36723)
```

**assistant:** Those `package.json`/`yarn.lock` changes come from the environment setup, not from me, so I'll leave them alone. Next I'll write a temporary test and run it:

**tool call: Bash**

```bash
cat > packages/mui-material/src/FormControlLabel/tmpRequired.test.js <<'EOF'
import * as React from 'react';
import { expect } from 'chai';
import { createRenderer } from 'test/utils';
import FormControlLabel, { formControlLabelClasses as classes } from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import FormControl from '@mui/material/FormControl';

describe('tmp required', () => {
  const { render } = createRenderer();
  it('none by default', () => {
    const { container } = render(<FormControlLabel label="Pizza" control={<Checkbox />} />);
    expect(container.querySelectorAll(`.${classes.asterisk}`)).to.have.lengthOf(0);
    expect(container.querySelector('input')).not.to.have.attribute('required');
  });
  it('asterisk when required', () => {
    const { container } = render(<FormControlLabel required label="Pizza" control={<Checkbox />} />);
    expect(container.querySelectorAll(`.${classes.asterisk}`)).to.have.lengthOf(1);
    expect(container.firstChild).to.have.class(classes.required);
    expect(container.querySelector('input')).to.have.attribute('required');
  });
  it('control required', () => {
    const { container } = render(<FormControlLabel label="Pizza" control={<Checkbox required />} />);
    expect(container.querySelectorAll(`.${classes.asterisk}`)).to.have.lengthOf(1);
  });
  it('error class on asterisk', () => {
    const { container } = render(<FormControl error><FormControlLabel required label="Pizza" control={<Checkbox />} /></FormControl>);
    expect(container.querySelector(`.${classes.asterisk}`)).to.have.class(classes.error);
  });
});
EOF
/work/mui__material-ui-34207/bin/envrun 'yarn -s cross-env NODE_ENV=test mocha "packages/mui-material/src/FormControlLabel/*.test.js" 2>&1 | tail -30'
```

tool result:

```
warning You don't appear to have an internet connection. Try the --offline flag to use the cache for registry queries.
Browserslist: caniuse-lite is outdated. Please run:
  npx update-browserslist-db@latest
  Why you should do it regularly: https://github.com/browserslist/update-db#readme
including inaccessible elements by default


  ............,,,,,......................

  34 passing (646ms)
  5 pending
```

**assistant:** The full suite passes. Next I'll confirm the new tests actually ran and that they fail without the fix:

**tool call: Bash**

```bash
E=/work/mui__material-ui-34207/bin/envrun; $E 'yarn -s cross-env NODE_ENV=test mocha --reporter dot packages/mui-material/src/FormControlLabel/tmpRequired.test.js 2>&1 | grep -E "passing|failing"'; git stash push packages/mui-material/src/FormControlLabel/FormControlLabel.js packages/mui-material/src/FormControlLabel/formControlLabelClasses.ts -q; $E 'yarn -s cross-env NODE_ENV=test mocha --reporter dot packages/mui-material/src/FormControlLabel/tmpRequired.test.js 2>&1 | grep -E "passing|failing"'; git stash pop -q; git diff --stat packages
```

tool result:

```
  4 passing (285ms)

  1 passing (409ms)
  3 failing

 .../src/FormControlLabel/FormControlLabel.d.ts     |  4 ++++
 .../src/FormControlLabel/FormControlLabel.js       | 28 +++++++++++++++++++++-
 .../FormControlLabel/formControlLabelClasses.ts    |  6 +++++
 3 files changed, 37 insertions(+), 1 deletion(-)
```

**assistant:** Without the fix, 3 of the 4 tests fail. With it, all 4 pass. Next I'll regenerate the API docs and check the TypeScript types:

**tool call: Bash**

```bash
rm packages/mui-material/src/FormControlLabel/tmpRequired.test.js; E=/work/mui__material-ui-34207/bin/envrun; $E 'yarn -s docs:api 2>&1 | tail -5; yarn -s prettier --write docs/pages/material-ui/api/form-control-label.json docs/translations/api-docs/form-control-label/form-control-label.json >/dev/null 2>&1; git status --short; cd packages/mui-material && npx tsc -p tsconfig.build.json --noEmit 2>&1 | tail -5'
```

tool result:

```
Built API docs for Grid
No declaration for BoxSlots
Built API docs for Box
No declaration for ContainerSlots
Built API docs for Container
 M docs/pages/material-ui/api/form-control-label.json
 M docs/translations/api-docs/form-control-label/form-control-label.json
 M package.json
 M packages/mui-material/src/FormControlLabel/FormControlLabel.d.ts
 M packages/mui-material/src/FormControlLabel/FormControlLabel.js
 M packages/mui-material/src/FormControlLabel/formControlLabelClasses.ts
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
tsconfig.build.json(8,5): error TS5053: Option 'emitDeclarationOnly' cannot be specified with option 'noEmit'.
tsconfig.build.json(9,5): error TS5053: Option 'emitDeclarationOnly' cannot be specified with option 'noEmit'.
```

**tool call: Bash**

```bash
git diff docs/; /work/mui__material-ui-34207/bin/envrun 'cd packages/mui-material && npx tsc -p tsconfig.json --noEmit 2>&1 | tail -5; cd /testbed && npx eslint packages/mui-material/src/FormControlLabel'
```

tool result:

```
diff --git a/docs/pages/material-ui/api/form-control-label.json b/docs/pages/material-ui/api/form-control-label.json
index c6eae1100d..58d7aea55a 100644
--- a/docs/pages/material-ui/api/form-control-label.json
+++ b/docs/pages/material-ui/api/form-control-label.json
@@ -19,6 +19,7 @@
       "default": "'end'"
     },
     "onChange": { "type": { "name": "func" } },
+    "required": { "type": { "name": "bool" } },
     "slotProps": {
       "type": { "name": "shape", "description": "{ typography?: object }" },
       "default": "{}"
@@ -40,9 +41,15 @@
       "labelPlacementBottom",
       "disabled",
       "label",
-      "error"
+      "error",
+      "required",
+      "asterisk"
     ],
-    "globalClasses": { "disabled": "Mui-disabled", "error": "Mui-error" },
+    "globalClasses": {
+      "disabled": "Mui-disabled",
+      "error": "Mui-error",
+      "required": "Mui-required"
+    },
     "name": "MuiFormControlLabel"
   },
   "spread": true,
diff --git a/docs/translations/api-docs/form-control-label/form-control-label.json b/docs/translations/api-docs/form-control-label/form-control-label.json
index 8c49084c06..dbc53fd933 100644
--- a/docs/translations/api-docs/form-control-label/form-control-label.json
+++ b/docs/translations/api-docs/form-control-label/form-control-label.json
@@ -11,6 +11,7 @@
     "label": "A text or an element to be used in an enclosing label element.",
     "labelPlacement": "The position of the label.",
     "onChange": "Callback fired when the state is changed.<br><br><strong>Signature:</strong><br><code>function(event: React.SyntheticEvent) =&gt; void</code><br><em>event:</em> The event source of the callback. You can pull out the new checked state by accessing <code>event.target.checked</code> (boolean).",
+    "required": "If <code>true</code>, the label will indicate that the <code>input</code> is required.",
     "slotProps": "The props used for each slot inside.",
     "sx": "The system prop that allows defining system overrides as well as additional CSS styles. See the <a href=\"/system/getting-started/the-sx-prop/\">`sx` page</a> for more details.",
     "value": "The value of the component."
@@ -45,6 +46,15 @@
       "description": "State class applied to {{nodeName}} if {{conditions}}.",
       "nodeName": "the root element",
       "conditions": "<code>error={true}</code>"
+    },
+    "required": {
+      "description": "State class applied to {{nodeName}} if {{conditions}}.",
+      "nodeName": "the root element",
+      "conditions": "<code>required={true}</code>"
+    },
+    "asterisk": {
+      "description": "Styles applied to {{nodeName}}.",
+      "nodeName": "the asterisk element"
     }
   }
 }
../../node_modules/@types/react-dom/test-utils/index.d.ts(6,9): error TS2305: Module '"react"' has no exported member 'act'.
../../test/utils/createMount.tsx(88,16): error TS2339: Property 'unmountComponentAtNode' does not exist on type 'typeof import("/testbed/node_modules/@types/react-dom/index")'.
../../test/utils/createMount.tsx(106,16): error TS2339: Property 'unmountComponentAtNode' does not exist on type 'typeof import("/testbed/node_modules/@types/react-dom/index")'.
```

**assistant:** `FormControlLabel` now supports `required`. `<FormControlLabel required label="..." control={<Checkbox />} />` shows a "*" after the label and marks the checkbox input as required.

**Changes, in `packages/mui-material/src/FormControlLabel/`:**
- **`FormControlLabel.js`:**
  - Added a `required` prop. If you don't set it, the component uses the control's own `required` value.
  - The value is passed to the control, so the native input gets `required` too.
  - When it's true, a hidden-from-screen-readers ` *` is drawn after the label, built the same way as the asterisk in `FormLabel`. It turns red when the field is in an error state, including when a surrounding `FormControl` sets `error`.
  - Also added the matching `propTypes` entry.
- **`FormControlLabel.d.ts`:** added the `required?: boolean` type.
- **`formControlLabelClasses.ts`:** added a `required` class (applied to the outer label element) and an `asterisk` class.
- **Docs:** I regenerated the API docs, which updated `docs/pages/material-ui/api/form-control-label.json` and its translation file.

**One choice to check:** a `required` set only on the control (e.g. `<Checkbox required />`) also shows the asterisk, so the label matches what the input actually requires. If you'd rather the asterisk appear only when `required` is set on `FormControlLabel` itself, that's a one-line change.

**Testing:**
- I wrote a temporary test covering: no asterisk by default, the asterisk and `required` class with `required`, `required` reaching the input, `required` coming from the control, and the error colour.
- Without the fix 3 of its 4 cases failed; with the fix all 4 passed. I then deleted the test.
- The existing `FormControlLabel` tests pass (34 passing, 5 pending) and ESLint reports nothing on the folder.
- Type-checking the package reports three errors, all in shared test helpers (`test/utils/createMount.tsx`) and the installed `@types/react-dom`, none in the files I changed. A newer `@types/react-dom` has been installed in this environment.

The changes to `package.json`, `yarn.lock` and the untracked `Dockerfile` and `custom-reporter.js` were already there before I started; I left them alone.

_session end: success, turns 9, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 14.98 s: yarn -s cross-env NODE_ENV=test mocha "packages/mui-material/src/FormControlLabel/*.test.js" 2>&1 | tail -30
- `rc=0` 4.04 s: yarn -s cross-env NODE_ENV=test mocha --reporter dot packages/mui-material/src/FormControlLabel/tmpRequired.test.js 2>&1 | grep -E "passing|failing"
- `rc=0` 5.62 s: yarn -s cross-env NODE_ENV=test mocha --reporter dot packages/mui-material/src/FormControlLabel/tmpRequired.test.js 2>&1 | grep -E "passing|failing"
- `rc=0` 121.49 s: yarn -s docs:api 2>&1 | tail -5; yarn -s prettier --write docs/pages/material-ui/api/form-control-label.json docs/translations/api-docs/form-control-label/form-control-label.json >/dev/null 2>&1; git status --short; cd packages/mui-material && npx tsc -p tsconfig.build.json --noEmit 2>&1 | tail -5
- `rc=0` 66.63 s: cd packages/mui-material && npx tsc -p tsconfig.json --noEmit 2>&1 | tail -5; cd /testbed && npx eslint packages/mui-material/src/FormControlLabel
