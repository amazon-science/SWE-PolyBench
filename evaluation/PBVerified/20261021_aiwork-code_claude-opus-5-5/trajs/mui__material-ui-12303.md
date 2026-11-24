# Instance: mui__material-ui-12303
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: False

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
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
````

## Operational trajectory

### Turn 1 — tool call call_0001 (exec)

````json
{
 "command": "cd packages/material-ui/src/FormControlLabel && ls && cat FormControlLabel.js && cat FormControlLabel.d.ts"
}
````

Result:

````text
{
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "success",
  "exit_code": 0,
  "retryability": "not_needed",
  "open_work_at_failure": false
 },
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "FormControlLabel.d.ts",
   "FormControlLabel.js",
   "packages/material-ui/src/FormControlLabel"
  ],
  "command_sha256": [
   "097041aea5d05d3f9d62b0b23c5b7ce0c048ed0404a06101c6d25d9aa16ac69a"
  ]
 },
 "_agent_context_projection": {
  "schema_version": "agent.exec_tool_result_receipt_preview.v1",
  "content_status": "partial_preview",
  "context_view_limit_bytes": 16384,
  "receipt": {
   "result_id": "tr_8b69fda41f5d424dbf8b5102cd5d5957",
   "total_bytes": 5533,
   "total_lines": 175,
   "omitted_bytes": 0,
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "artifact": {
   "result_id": "tr_8b69fda41f5d424dbf8b5102cd5d5957",
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "content_preview": "{\"tool_outcome\":{\"schema_version\":1,\"tool_name\":\"exec\",\"status\":\"success\",\"exit_code\":0,\"retr\n...[agent-cli tool_result context preview: tool_result_delivery_status=delivered; content_status=partial_preview_not_failure; compatibility_marker=tool_result truncated; omitted_bytes=5003; total_bytes=5189; context_view_limit=512 bytes; context_view_strategy=head_tail_compact; guidance=preview_not_failure_outcome_neutral]...\nbel\"],\"command_sha256\":[\"097041aea5d05d3f9d62b0b23c5b7ce0c048ed0404a06101c6d25d9aa16ac69a\"]}}",
  "stdout": {
   "total_bytes": 4479,
   "total_lines": 175,
   "omitted_bytes": 0,
   "preview": "FormControlLabel.d.ts\nFormControlLabel.js\nFormControlLabel.test.js\nindex.d.ts\nindex.js\n/* eslint-disable jsx-a11y/label-has-for */\n\nimport React from 'react';\nimport PropTypes from 'prop-types';\nimport classNames from 'classnames';\nimport withStyles from '../styles/withStyles';\nimport Typography from '../Typography';\n\nexport const styles = theme => ({\n  /* Styles applied to the root element. */\n  root: {\n    display: 'inline-flex',\n    alignItems: 'center',\n    cursor: 'pointer',\n    // For correct alignment with the text.\n    verticalAlign: 'middle',\n    // Remove grey highlight\n    WebkitTapHighlightColor: 'transparent',\n    marginLeft: -14,\n    marginRight: 16, // used for row presentation of radio/checkbox\n    '&$disabled': {\n      cursor: 'default',\n    },\n  },\n  /* Styles applied to the root element if `disabled={true}`. */\n  disabled: {},\n  /* Styles applied to the label's Typography component. */\n  label: {\n    '&$disabled': {\n      color: theme.palette.text.disabled,\n    },\n  },\n});\n\n/**\n * Drop in replacement of the `Radio`, `Switch` and `Checkbox` component.\n * Use this component if you want to display an extra label.\n */\nfunction FormControlLabel(props, context) {\n  const {\n    checked,\n    classes,\n    className: classNameProp,\n    control,\n    disabled: disabledProp,\n    inputRef,\n    label,\n    name,\n    onChange,\n    value,\n    ...other\n  } = props;\n  const { muiFormControl } = context;\n\n  let disabled = disabledProp;\n  if (typeof disabled === 'undefined' && typeof control.props.disabled !== 'undefined') {\n    disabled = control.props.disabled;\n  }\n  if (typeof disabled === 'undefined' && muiFormControl) {\n    disabled = muiFormControl.disabled;\n  }\n\n  const controlProps = {\n    disabled,\n  };\n  ['checked', 'name', 'onChange', 'value', 'inputRef'].forEach(key => {\n    if (typeof control.props[key] === 'undefined' && typeof props[key] !== 'undefined') {\n      controlProps[key] = props[key];\n    }\n  });\n\n  return (\n    <label\n      className={classNames(\n        classes.root,\n        {\n          [classes.disabled]: disabled,\n        },\n        classNameProp,\n      )}\n      {...other}\n    >\n      {React.cloneElement(control, controlProps)}\n      <Typography\n        component=\"span\"\n        className={classNames(classes.label, { [classes.disabled]: disabled })}\n      >\n        {label}\n      </Typography>\n    </label>\n  );\n}\n\nFormControlLabel.propTypes = {\n  /**\n   * If `true`, the component appears selected.\n   */\n  checked: PropTypes.oneOfType([PropTypes.bool, PropTypes.string]),\n  /**\n   * Override or extend the styles applied to the component.\n   * See [CSS API](#css-api) below for more details.\n   */\n  classes: PropTypes.object.isRequired,\n  /**\n   * @ignore\n   */\n  className: PropTypes.string,\n  /**\n   * A control element. For instance, it can be be a `Radio`, a `Switch` or a `Checkbox`.\n   */\n  control: PropTypes.element,\n  /**\n   * If `true`, the control will be disabled.\n   */\n  disabled: PropTypes.bool,\n  /**\n   * Use that property to pass a ref callback to the native input component.\n   */\n  inputRef: PropTypes.oneOfType([PropTypes.func, PropTypes.object]),\n  /**\n   * The text to be used in an enclosing label element.\n   */\n  label: PropTypes.node,\n  /*\n   * @ignore\n   */\n  name: PropTypes.string,\n  /**\n   * Callback fired when the state is changed.\n   *\n   * @param {object} event The event source of the callback.\n   * You can pull out the new value by accessing `event.target.checked`.\n   * @param {boolean} checked The `checked` value of the switch\n   */\n  onChange: PropTypes.func,\n  /**\n   * The value of the component.\n   */\n  value: PropTypes.string,\n};\n\nFormControlLabel.contextTypes = {\n  muiFormControl: PropTypes.object,\n};\n\nexport default withStyles(styles, { name: 'MuiFormControlLabel' })(FormControlLabel);\nimport * as React from 'react';\nimport { StandardProps } from '..';\n\nexport interface FormControlLabelProps\n  extends StandardProps<\n      React.LabelHTMLAttributes<HTMLLabelElement>,\n      FormControlLabelClassKey,\n      'onChange'\n    > {\n  checked?: boolean | string;\n  control: React.ReactElement<any>;\n  disabled?: boolean;\n  inputRef?: React.Ref<any>;\n  label: React.ReactNode;\n  name?: string;\n  onChange?: (event: React.ChangeEvent<{}>, checked: boolean) => void;\n  value?: string;\n}\n\nexport type FormControlLabelClassKey = 'root' | 'disabled' | 'label';\n\ndeclare const FormControlLabel: React.ComponentType<FormControlLabelProps>;\n\nexport default FormControlLabel;\n"
  }
 }
}
````

### Turn 2 — thinking

````text
I'm recalling the upstream styling fix for label placement: a `labelPlacementStart` style that reverses the flex direction and adjusts the margins so the label sits properly on the opposite side.
````

### Turn 2 — tool call call_0002 (rg)

````json
{
 "pattern": "labelPlacement|Placement",
 "path": "packages/material-ui/src/FormControlLabel"
}
````

Result:

````text
{
 "output_mode": "content",
 "pattern": "labelPlacement|Placement",
 "search_path": "/testbed/packages/material-ui/src/FormControlLabel",
 "matches": [],
 "stats": {
  "files_searched": 5,
  "files_with_matches": 0,
  "matches_found": 0,
  "matches_returned": 0,
  "denied_skips": 0,
  "duration_ms": 9,
  "timing": {
   "walk_ms": 0,
   "search_ms": 9,
   "collect_ms": 0,
   "total_ms": 9
  }
 },
 "truncated": false
}
````

### Turn 3 — assistant text

I'll add a `labelPlacement` prop (`'end'` default, `'start'`) matching the upstream API.

### Turn 3 — tool call call_0003 (apply_patch)

````json
{
 "patch_text": "*** Begin Patch\n*** Update File: packages/material-ui/src/FormControlLabel/FormControlLabel.js\n@@\n       cursor: 'default',\n     },\n   },\n+  /* Styles applied to the root element if `labelPlacement=\"start\"`. */\n+  labelPlacementStart: {\n+    flexDirection: 'row-reverse',\n+    marginLeft: 16, // used for row presentation of radio/checkbox\n+    marginRight: -14,\n+  },\n   /* Styles applied to the root element if `disabled={true}`. */\n@@\n     inputRef,\n     label,\n+    labelPlacement,\n     name,\n@@\n         classes.root,\n         {\n+          [classes.labelPlacementStart]: labelPlacement === 'start',\n           [classes.disabled]: disabled,\n         },\n@@\n   label: PropTypes.node,\n+  /**\n+   * The position of the label.\n+   */\n+  labelPlacement: PropTypes.oneOf(['end', 'start']),\n   /*\n@@\n FormControlLabel.contextTypes = {\n   muiFormControl: PropTypes.object,\n };\n+\n+FormControlLabel.defaultProps = {\n+  labelPlacement: 'end',\n+};\n*** Update File: packages/material-ui/src/FormControlLabel/FormControlLabel.d.ts\n@@\n   label: React.ReactNode;\n+  labelPlacement?: 'end' | 'start';\n   name?: string;\n@@\n-export type FormControlLabelClassKey = 'root' | 'disabled' | 'label';\n+export type FormControlLabelClassKey = 'root' | 'labelPlacementStart' | 'disabled' | 'label';\n*** End Patch"
}
````

Result:

````text
{
 "plan_id": "85193338266738283d23b756e57ec3f9c2f125cef07cffcf948591adba02f42f",
 "applied": true,
 "files_modified": [
  "packages/material-ui/src/FormControlLabel/FormControlLabel.js",
  "packages/material-ui/src/FormControlLabel/FormControlLabel.d.ts"
 ],
 "conflicts": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "apply_patch",
    "paths": [
     "packages/material-ui/src/FormControlLabel/FormControlLabel.js",
     "packages/material-ui/src/FormControlLabel/FormControlLabel.d.ts"
    ]
   }
  ]
 }
}
````

### Turn 4 — tool call call_0004 (exec)

````json
{
 "command": "cd /testbed && timeout 300 npx mocha --require @babel/register packages/material-ui/src/FormControlLabel/FormControlLabel.test.js 2>&1 | tail -20 || (cat package.json | grep '\"test')"
}
````

Result:

````text
{
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "success",
  "exit_code": 0,
  "retryability": "not_needed",
  "open_work_at_failure": false
 },
 "stdout": "\n\n  ․․․․․․․․․․\n\n  10 passing (85ms)\n\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 3348,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed"
  ],
  "command_sha256": [
   "0e3cd9c470456d9cc994e42a01f8b5080cdcccb4ff12f446e8b332d7136e4fb3"
  ]
 }
}
````

### Turn 5 — thinking

````text
I should quickly verify labelPlacement works, and the existing tests already pass—let me do a quick smoke test to confirm.
````

### Turn 5 — tool call call_0005 (exec)

````json
{
 "command": "cd /testbed && cat > /tmp/smoke.test.js <<'EOF'\nimport React from 'react';\nimport { assert } from 'chai';\nimport { createShallow, getClasses } from '/testbed/packages/material-ui/src/test-utils';\nimport FormControlLabel from '/testbed/packages/material-ui/src/FormControlLabel';\ndescribe('smoke', () => {\n  it('start', () => {\n    const shallow = createShallow({ dive: true });\n    const classes = getClasses(<FormControlLabel label=\"x\" control={<div />} />);\n    const w = shallow(<FormControlLabel label=\"x\" labelPlacement=\"start\" control={<div />} />);\n    assert.strictEqual(w.hasClass(classes.labelPlacementStart), true);\n    const w2 = shallow(<FormControlLabel label=\"x\" control={<div />} />);\n    assert.strictEqual(w2.hasClass(classes.labelPlacementStart), false);\n  });\n});\nEOF\ncp /tmp/smoke.test.js packages/material-ui/src/FormControlLabel/zz_smoke.test.js && timeout 300 npx mocha --require @babel/register packages/material-ui/src/FormControlLabel/zz_smoke.test.js 2>&1 | tail -8; rm packages/material-ui/src/FormControlLabel/zz_smoke.test.js"
}
````

Result:

````text
{
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "success",
  "exit_code": 0,
  "retryability": "not_needed",
  "open_work_at_failure": false
 },
 "stdout": "\n\n  ․\n\n  1 passing (35ms)\n\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 1664,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "write",
    "paths": [
     "/tmp/smoke.test.js",
     "packages/material-ui/src/FormControlLabel/zz_smoke.test.js"
    ]
   }
  ],
  "reads": [
   "/testbed",
   "/tmp/smoke.test.js"
  ],
  "command_sha256": [
   "9698ba5df8eb5816579ee852df685969d49684eaae8e3d80942dbb18abb1d52f"
  ]
 }
}
````

### Turn 6 — thinking

````text
A minimal API markdown doc should be fine for this.
````

### Turn 6 — assistant text

I added a `labelPlacement` prop to `FormControlLabel`, so a Switch label can go on the left without the `rtl` workaround. Use `labelPlacement="start"`:

```jsx
<FormControlLabel labelPlacement="start" control={<Switch />} label="Label" />
```

Changes, in `packages/material-ui/src/FormControlLabel/`:
- **`FormControlLabel.js`**: new `labelPlacement` prop. It accepts `'end'` (the default, so current behaviour is unchanged) or `'start'`.
- **New `labelPlacementStart` style**: applied when the prop is `'start'`. It sets `flexDirection: 'row-reverse'` and swaps the left and right margins so spacing still lines up when controls sit in a row.
- **`FormControlLabel.d.ts`**: added `labelPlacement?: 'end' | 'start'` and the `labelPlacementStart` class key to the types.

The existing `FormControlLabel` tests pass (10/10). I also ran a short throwaway test that checked the new class is added only when `labelPlacement="start"`; it passed and I deleted it. I didn't check the result visually in a browser or update the demo docs.

### Turn 7 — assistant text

I added a `labelPlacement` prop to `FormControlLabel`, so a label can now go on the left of a `Switch`, `Checkbox` or `Radio` without the `rtl` workaround:

```jsx
<FormControlLabel labelPlacement="start" control={<Switch />} label="Label" />
```

The existing `FormControlLabel` tests still pass (10 of 10). I also ran a throwaway check, since deleted, which confirmed the new start-placement class is applied only when `labelPlacement="start"`. I didn't render it in a browser, so I haven't seen the visual result.

The changes, all in `packages/material-ui/src/FormControlLabel/`:
- **`FormControlLabel.js`:**
  - Adds `labelPlacement`, which accepts `'end'` (the default, so current behaviour is unchanged) or `'start'`.
  - With `'start'`, a new `labelPlacementStart` class reverses the order of the control and label. It also swaps the left and right margins so spacing stays right when several controls sit in a row.
- **`FormControlLabel.d.ts`:** adds the matching TypeScript types for the prop and the new class.

The issue also asked for this to be documented, and I didn't update the selection-controls demo page.

## Final answer

I added a `labelPlacement` prop to `FormControlLabel`, so a label can now go on the left of a `Switch`, `Checkbox` or `Radio` without the `rtl` workaround:

```jsx
<FormControlLabel labelPlacement="start" control={<Switch />} label="Label" />
```

The existing `FormControlLabel` tests still pass (10 of 10). I also ran a throwaway check, since deleted, which confirmed the new start-placement class is applied only when `labelPlacement="start"`. I didn't render it in a browser, so I haven't seen the visual result.

The changes, all in `packages/material-ui/src/FormControlLabel/`:
- **`FormControlLabel.js`:**
  - Adds `labelPlacement`, which accepts `'end'` (the default, so current behaviour is unchanged) or `'start'`.
  - With `'start'`, a new `labelPlacementStart` class reverses the order of the control and label. It also swaps the left and right margins so spacing stays right when several controls sit in a row.
- **`FormControlLabel.d.ts`:** adds the matching TypeScript types for the prop and the new class.

The issue also asked for this to be documented, and I didn't update the selection-controls demo page.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 112441 | 2601 | 104533 | 7890 | 115042 |
