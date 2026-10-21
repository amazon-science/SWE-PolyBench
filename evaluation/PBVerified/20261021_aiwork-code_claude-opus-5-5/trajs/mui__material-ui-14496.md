# Instance: mui__material-ui-14496
# Model: claude-opus-5-5
# Run status: agent_error
# Final resolved: True

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
[Tooltip] Tooltips aren't displayed on focus on TextFields
- [x] This is not a v0.x issue. <!-- (v0.x is no longer maintained) -->
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Expected Behavior 🤔
Using a `Tooltip` component with `disableHoverListener` around a `TextField` component should display the tooltip on focus

## Current Behavior 😯
No tooltip is displayed

## Steps to Reproduce 🕹
Link: https://codesandbox.io/s/ooywx0xlq9

1. Click on the TextField, nothing is displayed.

Testing anywhere the following code sample is enough to reproduce :
```js
<Tooltip title="TestTooltip" disableHoverListener>
  <TextField label="TestTooltip" />
</Tooltip>
```

## Context 🔦
Display hints for user entering their data.

This used to work, and, after trying a few versions, appears to be broken starting v3.1.1

## Your Environment 🌎

| Tech         | Version |
|--------------|---------|
| Material-UI  | v3.9.2  |
| React        | 16.6.3 |
| Browser      | Firefox 66b, Chromium 71 |

As always, thanks for the great project :slightly_smiling_face: 
````

## Operational trajectory

### Turn 1 — assistant text

I'll investigate the Tooltip component to find why focus events aren't triggering display.

### Turn 1 — tool call call_0001 (exec)

````json
{
 "command": "ls && cat package.json | head -40"
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
 "stdout": "BACKERS.md\nCHANGELOG.md\nCODE_OF_CONDUCT.md\nCONTRIBUTING.md\nDockerfile\nGOVERNANCE.md\nLICENSE\nREADME.md\nROADMAP.md\nSUPPORT.md\nbabel.config.js\ncrowdin.yml\ncustom-reporter.js\ndocker-compose.yml\ndocs\nexamples\nlerna.json\nmodules\nnext.config.js\nnode_modules\npackage.json\npackages\npages\nprettier.config.js\nscripts\nstatic\ntest\ntmp\ntsconfig.json\ntslint.json\nyarn.lock\n{\n  \"name\": \"@material-ui/workspace\",\n  \"private\": true,\n  \"author\": \"Material-UI Team\",\n  \"version\": \"3.9.2\",\n  \"description\": \"Material-UI's workspace package\",\n  \"keywords\": [\n    \"react\",\n    \"react-component\",\n    \"material design\",\n    \"material-ui\"\n  ],\n  \"repository\": {\n    \"type\": \"git\",\n    \"url\": \"https://github.com/mui-org/material-ui.git\"\n  },\n  \"license\": \"MIT\",\n  \"bugs\": {\n    \"url\": \"https://github.com/mui-org/material-ui/issues\"\n  },\n  \"homepage\": \"https://material-ui.com/\",\n  \"scripts\": {\n    \"argos\": \"argos upload test/regressions/screenshots/chrome --token $ARGOS_TOKEN\",\n    \"docs:api\": \"yarn docs:api:core && yarn docs:api:lab\",\n    \"docs:api:core\": \"rimraf ./pages/api && cross-env BABEL_ENV=docs-development babel-node ./docs/scripts/buildApi.js ./packages/material-ui/src ./pages/api\",\n    \"docs:api:lab\": \"rimraf ./pages/lab/api && cross-env BABEL_ENV=docs-development babel-node ./docs/scripts/buildApi.js ./packages/material-ui-lab/src ./pages/lab/api\",\n    \"docs:build\": \"rimraf .next && cross-env NODE_ENV=production BABEL_ENV=docs-production next build\",\n    \"docs:build-sw\": \"babel-node ./docs/scripts/buildServiceWorker.js\",\n    \"docs:deploy\": \"git push material-ui-docs master:latest\",\n    \"docs:dev\": \"rimraf node_modules/.cache/babel-loader && cross-env BABEL_ENV=docs-development next dev\",\n    \"docs:export\": \"rimraf docs/export && next export -o docs/export && yarn docs:build-sw && cp -r docs/static/. docs/export\",\n    \"docs:icons\": \"rimraf static/icons/* && babel-node ./docs/scripts/buildIcons.js\",\n    \"docs:size-why\": \"DOCS_STATS_ENABLED=true yarn docs:build\",\n    \"docs:start\": \"next start\",\n    \"docs:typescript\": \"cross-env NODE_ENV=development babel docs/src --config-file ./docs/babel.config.ts.js --extensions .tsx --out-dir docs/src\",\n    \"docs:typescript:formatted\": \"node docs/scripts/formattedTSDemos\",\n    \"jsonlint\": \"yarn --silent jsonlint:files | xargs -n1 jsonlint -q -c && echo \\\"jsonlint: no lint errors\\\"\",\n    \"jsonlint:files\": \"find . -name \\\"*.json\\\" | grep -v -f .eslintignore\",\n    \"lint\": \"eslint . --cache --report-unused-disable-directives && echo \\\"eslint: no lint errors\\\"\",\n    \"lint:fix\": \"eslint . --cache --fix && echo \\\"eslint: no lint errors\\\"\",\n",
 "device_targets": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "package.json"
  ],
  "command_sha256": [
   "6846067f5157c741037936b2788621c3b5efef83f7ff45db38e7da62a0cbe9b0"
  ]
 },
 "duration_ms": 483
}
````

### Turn 2 — tool call call_0002 (exec)

````json
{
 "command": "ls packages/material-ui/src/Tooltip/ 2>/dev/null || find . -path ./node_modules -prune -o -name \"Tooltip.js\" -print"
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
 "stdout": "Tooltip.d.ts\nTooltip.js\nTooltip.test.js\nindex.d.ts\nindex.js\n",
 "device_targets": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "packages/material-ui/src/Tooltip/"
  ],
  "command_sha256": [
   "4af235b03199bbc890505df75ab1eff6adeb04d117ffbacd6209c051773ed3b2"
  ]
 },
 "duration_ms": 166
}
````

### Turn 3 — tool call call_0003 (read)

````json
{
 "file_path": "packages/material-ui/src/Tooltip/Tooltip.js",
 "limit": 340
}
````

Result:

````text
{
 "type": "file",
 "path": "packages/material-ui/src/Tooltip/Tooltip.js",
 "full_read": false,
 "output": "packages/material-ui/src/Tooltip/Tooltip.js\n\n1: import React from 'react';\n2: import PropTypes from 'prop-types';\n3: import warning from 'warning';\n4: import classNames from 'classnames';\n5: import { componentPropType } from '@material-ui/utils';\n6: import RootRef from '../RootRef';\n7: import withStyles from '../styles/withStyles';\n8: import { capitalize } from '../utils/helpers';\n9: import Grow from '../Grow';\n10: import Popper from '../Popper';\n11: \n12: export const styles = theme => ({\n13:   /* Styles applied to the Popper component. */\n14:   popper: {\n15:     zIndex: theme.zIndex.tooltip,\n16:     opacity: 0.9,\n17:     pointerEvents: 'none',\n18:   },\n19:   /* Styles applied to the Popper component if `interactive={true}`. */\n20:   popperInteractive: {\n21:     pointerEvents: 'auto',\n22:   },\n23:   /* Styles applied to the tooltip (label wrapper) element. */\n24:   tooltip: {\n25:     backgroundColor: theme.palette.grey[700],\n26:     borderRadius: theme.shape.borderRadius,\n27:     color: theme.palette.common.white,\n28:     fontFamily: theme.typography.fontFamily,\n29:     padding: '4px 8px',\n30:     fontSize: theme.typography.pxToRem(10),\n31:     lineHeight: `${theme.typography.round(14 / 10)}em`,\n32:     maxWidth: 300,\n33:   },\n34:   /* Styles applied to the tooltip (label wrapper) element if the tooltip is opened by touch. */\n35:   touch: {\n36:     padding: '8px 16px',\n37:     fontSize: theme.typography.pxToRem(14),\n38:     lineHeight: `${theme.typography.round(16 / 14)}em`,\n39:   },\n40:   /* Styles applied to the tooltip (label wrapper) element if `placement` contains \"left\". */\n41:   tooltipPlacementLeft: {\n42:     transformOrigin: 'right center',\n43:     margin: '0 24px ',\n44:     [theme.breakpoints.up('sm')]: {\n45:       margin: '0 14px',\n46:     },\n47:   },\n48:   /* Styles applied to the tooltip (label wrapper) element if `placement` contains \"right\". */\n49:   tooltipPlacementRight: {\n50:     transformOrigin: 'left center',\n51:     margin: '0 24px',\n52:     [theme.breakpoints.up('sm')]: {\n53:       margin: '0 14px',\n54:     },\n55:   },\n56:   /* Styles applied to the tooltip (label wrapper) element if `placement` contains \"top\". */\n57:   tooltipPlacementTop: {\n58:     transformOrigin: 'center bottom',\n59:     margin: '24px 0',\n60:     [theme.breakpoints.up('sm')]: {\n61:       margin: '14px 0',\n62:     },\n63:   },\n64:   /* Styles applied to the tooltip (label wrapper) element if `placement` contains \"bottom\". */\n65:   tooltipPlacementBottom: {\n66:     transformOrigin: 'center top',\n67:     margin: '24px 0',\n68:     [theme.breakpoints.up('sm')]: {\n69:       margin: '14px 0',\n70:     },\n71:   },\n72: });\n73: \n74: class Tooltip extends React.Component {\n75:   ignoreNonTouchEvents = false;\n76: \n77:   constructor(props) {\n78:     super();\n79:     this.isControlled = props.open != null;\n80:     this.state = {\n81:       open: null,\n82:     };\n83: \n84:     if (!this.isControlled) {\n85:       // not controlled, use internal state\n86:       this.state.open = false;\n87:     }\n88:   }\n89: \n90:   componentDidMount() {\n91:     warning(\n92:       !this.childrenRef.disabled ||\n93:         (this.childrenRef.disabled && this.props.title === '') ||\n94:         this.childrenRef.tagName.toLowerCase() !== 'button',\n95:       [\n96:         'Material-UI: you are providing a disabled `button` child to the Tooltip component.',\n97:         'A disabled element does not fire events.',\n98:         \"Tooltip needs to listen to the child element's events to display the title.\",\n99:         '',\n100:         'Place a `div` container on top of the element.',\n101:       ].join('\\n'),\n102:     );\n103: \n104:     // Fallback to this default id when possible.\n105:     // Use the random value for client side rendering only.\n106:     // We can't use it server-side.\n107:     this.defaultId = `mui-tooltip-${Math.round(Math.random() * 1e5)}`;\n108: \n109:     // Rerender with this.defaultId and this.childrenRef.\n110:     if (this.props.open) {\n111:       this.forceUpdate();\n112:     }\n113:   }\n114: \n115:   componentWillUnmount() {\n116:     clearTimeout(this.closeTimer);\n117:     clearTimeout(this.enterTimer);\n118:     clearTimeout(this.focusTimer);\n119:     clearTimeout(this.leaveTimer);\n120:     clearTimeout(this.touchTimer);\n121:   }\n122: \n123:   onRootRef = ref => {\n124:     this.childrenRef = ref;\n125:   };\n126: \n127:   handleFocus = event => {\n128:     event.persist();\n129:     // The autoFocus of React might trigger the event before the componentDidMount.\n130:     // We need to account for this eventuality.\n131:     this.focusTimer = setTimeout(() => {\n132:       // We need to make sure the focus hasn't moved since the event was triggered.\n133:       if (this.childrenRef === document.activeElement) {\n134:         this.handleEnter(event);\n135:       }\n136:     });\n137: \n138:     const childrenProps = this.props.children.props;\n139:     if (childrenProps.onFocus) {\n140:       childrenProps.onFocus(event);\n141:     }\n142:   };\n143: \n144:   handleEnter = event => {\n145:     const { children, enterDelay } = this.props;\n146:     const childrenProps = children.props;\n147: \n148:     if (event.type === 'mouseover' && childrenProps.onMouseOver) {\n149:       childrenProps.onMouseOver(event);\n150:     }\n151: \n152:     if (this.ignoreNonTouchEvents && event.type !== 'touchstart') {\n153:       return;\n154:     }\n155: \n156:     // Remove the title ahead of time.\n157:     // We don't want to wait for the next render commit.\n158:     // We would risk displaying two tooltips at the same time (native + this one).\n159:     this.childrenRef.setAttribute('title', '');\n160: \n161:     clearTimeout(this.enterTimer);\n162:     clearTimeout(this.leaveTimer);\n163:     if (enterDelay) {\n164:       event.persist();\n165:       this.enterTimer = setTimeout(() => {\n166:         this.handleOpen(event);\n167:       }, enterDelay);\n168:     } else {\n169:       this.handleOpen(event);\n170:     }\n171:   };\n172: \n173:   handleOpen = event => {\n174:     // The mouseover event will trigger for every nested element in the tooltip.\n175:     // We can skip rerendering when the tooltip is already open.\n176:     // We are using the mouseover event instead of the mouseenter event to fix a hide/show issue.\n177:     if (!this.isControlled && !this.state.open) {\n178:       this.setState({ open: true });\n179:     }\n180: \n181:     if (this.props.onOpen) {\n182:       this.props.onOpen(event);\n183:     }\n184:   };\n185: \n186:   handleLeave = event => {\n187:     const { children, leaveDelay } = this.props;\n188:     const childrenProps = children.props;\n189: \n190:     if (event.type === 'blur' && childrenProps.onBlur) {\n191:       childrenProps.onBlur(event);\n192:     }\n193: \n194:     if (event.type === 'mouseleave' && childrenProps.onMouseLeave) {\n195:       childrenProps.onMouseLeave(event);\n196:     }\n197: \n198:     clearTimeout(this.enterTimer);\n199:     clearTimeout(this.leaveTimer);\n200:     if (leaveDelay) {\n201:       event.persist();\n202:       this.leaveTimer = setTimeout(() => {\n203:         this.handleClose(event);\n204:       }, leaveDelay);\n205:     } else {\n206:       this.handleClose(event);\n207:     }\n208:   };\n209: \n210:   handleClose = event => {\n211:     if (!this.isControlled) {\n212:       this.setState({ open: false });\n213:     }\n214: \n215:     if (this.props.onClose) {\n216:       this.props.onClose(event);\n217:     }\n218: \n219:     clearTimeout(this.closeTimer);\n220:     this.closeTimer = setTimeout(() => {\n221:       this.ignoreNonTouchEvents = false;\n222:     }, this.props.theme.transitions.duration.shortest);\n223:   };\n224: \n225:   handleTouchStart = event => {\n226:     this.ignoreNonTouchEvents = true;\n227:     const { children, enterTouchDelay } = this.props;\n228: \n229:     if (children.props.onTouchStart) {\n230:       children.props.onTouchStart(event);\n231:     }\n232: \n233:     clearTimeout(this.leaveTimer);\n234:     clearTimeout(this.closeTimer);\n235:     clearTimeout(this.touchTimer);\n236:     event.persist();\n237:     this.touchTimer = setTimeout(() => {\n238:       this.handleEnter(event);\n239:     }, enterTouchDelay);\n240:   };\n241: \n242:   handleTouchEnd = event => {\n243:     const { children, leaveTouchDelay } = this.props;\n244: \n245:     if (children.props.onTouchEnd) {\n246:       children.props.onTouchEnd(event);\n247:     }\n248: \n249:     clearTimeout(this.touchTimer);\n250:     clearTimeout(this.leaveTimer);\n251:     event.persist();\n252:     this.leaveTimer = setTimeout(() => {\n253:       this.handleClose(event);\n254:     }, leaveTouchDelay);\n255:   };\n256: \n257:   render() {\n258:     const {\n259:       children,\n260:       classes,\n261:       disableFocusListener,\n262:       disableHoverListener,\n263:       disableTouchListener,\n264:       enterDelay,\n265:       enterTouchDelay,\n266:       id,\n267:       interactive,\n268:       leaveDelay,\n269:       leaveTouchDelay,\n270:       onClose,\n271:       onOpen,\n272:       open: openProp,\n273:       placement,\n274:       PopperProps,\n275:       theme,\n276:       title,\n277:       TransitionComponent,\n278:       TransitionProps,\n279:       ...other\n280:     } = this.props;\n281: \n282:     let open = this.isControlled ? openProp : this.state.open;\n283: \n284:     // There is no point in displaying an empty tooltip.\n285:     if (title === '') {\n286:       open = false;\n287:     }\n288: \n289:     // For accessibility and SEO concerns, we render the title to the DOM node when\n290:     // the tooltip is hidden. However, we have made a tradeoff when\n291:     // `disableHoverListener` is set. This title logic is disabled.\n292:     // It's allowing us to keep the implementation size minimal.\n293:     // We are open to change the tradeoff.\n294:     const shouldShowNativeTitle = !open && !disableHoverListener;\n295:     const childrenProps = {\n296:       'aria-describedby': open ? id || this.defaultId : null,\n297:       title: shouldShowNativeTitle && typeof title === 'string' ? title : null,\n298:       ...other,\n299:       ...children.props,\n300:       className: classNames(other.className, children.props.className),\n301:     };\n302: \n303:     if (!disableTouchListener) {\n304:       childrenProps.onTouchStart = this.handleTouchStart;\n305:       childrenProps.onTouchEnd = this.handleTouchEnd;\n306:     }\n307: \n308:     if (!disableHoverListener) {\n309:       childrenProps.onMouseOver = this.handleEnter;\n310:       childrenProps.onMouseLeave = this.handleLeave;\n311:     }\n312: \n313:     if (!disableFocusListener) {\n314:       childrenProps.onFocus = this.handleFocus;\n315:       childrenProps.onBlur = this.handleLeave;\n316:     }\n317: \n318:     const interactiveWrapperListeners = interactive\n319:       ? {\n320:           onMouseOver: childrenProps.onMouseOver,\n321:           onMouseLeave: childrenProps.onMouseLeave,\n322:           onFocus: childrenProps.onFocus,\n323:           onBlur: childrenProps.onBlur,\n324:         }\n325:       : {};\n326: \n327:     warning(\n328:       !children.props.title,\n329:       [\n330:         'Material-UI: you have provided a `title` property to the child of <Tooltip />.',\n331:         `Remove this title property \\`${children.props.title}\\` or the Tooltip component.`,\n332:       ].join('\\n'),\n333:     );\n334: \n335:     return (\n336:       <React.Fragment>\n337:         <RootRef rootRef={this.onRootRef}>{React.cloneElement(children, childrenProps)}</RootRef>\n338:         <Popper\n339:           className={classNames(classes.popper, {\n340:             [classes.popperInteractive]: interactive,\n\n(Returned 340 lines starting at 1; total 494; output truncated — call read again with a higher offset or limit to continue)",
 "offset": 1,
 "limit": 340,
 "lines_returned": 340,
 "total_lines": 494,
 "observed_lines": 494,
 "total_lines_lower_bound": 494,
 "total_lines_exact": true,
 "truncated": true,
 "next_offset": 341,
 "window_bytes_limit": 102400,
 "size_bytes": 14069
}
````

### Turn 4 — thinking

````text
I realize the focus check fails for TextField since focus lands on the inner input, not the div itself—so I need to use a containment check instead of strict equality, matching the upstream fix that adjusted the focus-detection timer logic.

This matches my memory of the fix: setting childrenRef synchronously if unset, then calling handleEnter directly rather than deferring through a timeout. I should verify against existing tests to see if they expect synchronous or delayed behavior.
````

### Turn 4 — tool call call_0004 (rg)

````json
{
 "pattern": "focus|activeElement",
 "path": "packages/material-ui/src/Tooltip/Tooltip.test.js",
 "context": 4
}
````

Result:

````text
{
 "output_mode": "content",
 "pattern": "focus|activeElement",
 "search_path": "/testbed/packages/material-ui/src/Tooltip/Tooltip.test.js",
 "matches": [
  {
   "path": "Tooltip.test.js",
   "line_number": 127,
   "line": "    childrenRef.focus();",
   "context_before": [
    "    wrapper.instance().childrenRef = childrenRef;",
    "    const children = wrapper.childAt(0).childAt(0);",
    "    assert.strictEqual(wrapper.state().open, false);",
    "    children.simulate('mouseOver', { type: 'mouseover' });"
   ],
   "context_after": [
    "    children.simulate('focus', { type: 'focus', persist });",
    "    clock.tick(0);",
    "    assert.strictEqual(wrapper.state().open, true);",
    "    children.simulate('mouseLeave', { type: 'mouseleave' });"
   ]
  },
  {
   "path": "Tooltip.test.js",
   "line_number": 128,
   "line": "    children.simulate('focus', { type: 'focus', persist });",
   "context_before": [
    "    const children = wrapper.childAt(0).childAt(0);",
    "    assert.strictEqual(wrapper.state().open, false);",
    "    children.simulate('mouseOver', { type: 'mouseover' });",
    "    childrenRef.focus();"
   ],
   "context_after": [
    "    clock.tick(0);",
    "    assert.strictEqual(wrapper.state().open, true);",
    "    children.simulate('mouseLeave', { type: 'mouseleave' });",
    "    assert.strictEqual(wrapper.state().open, false);"
   ]
  },
  {
   "path": "Tooltip.test.js",
   "line_number": 146,
   "line": "      childrenRef.focus();",
   "context_before": [
    "      wrapper.instance().childrenRef = childrenRef;",
    "      const children = wrapper.childAt(0).childAt(0);",
    "      children.simulate('touchStart', { type: 'touchstart', persist });",
    "      children.simulate('touchEnd', { type: 'touchend', persist });"
   ],
   "context_after": [
    "      children.simulate('focus', { type: 'focus', persist });",
    "      assert.strictEqual(wrapper.state().open, false);",
    "    });",
    ""
   ]
  },
  {
   "path": "Tooltip.test.js",
   "line_number": 147,
   "line": "      children.simulate('focus', { type: 'focus', persist });",
   "context_before": [
    "      const children = wrapper.childAt(0).childAt(0);",
    "      children.simulate('touchStart', { type: 'touchstart', persist });",
    "      children.simulate('touchEnd', { type: 'touchend', persist });",
    "      childrenRef.focus();"
   ],
   "context_after": [
    "      assert.strictEqual(wrapper.state().open, false);",
    "    });",
    "",
    "    it('should open on long press', () => {"
   ]
  },
  {
   "path": "Tooltip.test.js",
   "line_number": 158,
   "line": "      childrenRef.focus();",
   "context_before": [
    "      childrenRef.tabIndex = 0;",
    "      wrapper.instance().childrenRef = childrenRef;",
    "      const children = wrapper.childAt(0).childAt(0);",
    "      children.simulate('touchStart', { type: 'touchstart', persist });"
   ],
   "context_after": [
    "      children.simulate('focus', { type: 'focus', persist });",
    "      clock.tick(1e3);",
    "      assert.strictEqual(wrapper.state().open, true);",
    "      children.simulate('touchEnd', { type: 'touchend', persist });"
   ]
  },
  {
   "path": "Tooltip.test.js",
   "line_number": 159,
   "line": "      children.simulate('focus', { type: 'focus', persist });",
   "context_before": [
    "      wrapper.instance().childrenRef = childrenRef;",
    "      const children = wrapper.childAt(0).childAt(0);",
    "      children.simulate('touchStart', { type: 'touchstart', persist });",
    "      childrenRef.focus();"
   ],
   "context_after": [
    "      clock.tick(1e3);",
    "      assert.strictEqual(wrapper.state().open, true);",
    "      children.simulate('touchEnd', { type: 'touchend', persist });",
    "      children.simulate('blur', { type: 'blur' });"
   ]
  },
  {
   "path": "Tooltip.test.js",
   "line_number": 180,
   "line": "      childrenRef.focus();",
   "context_before": [
    "    it('should take the enterDelay into account', () => {",
    "      const wrapper = mount(<TooltipNaked classes={{}} enterDelay={111} {...defaultProps} />);",
    "      const childrenRef = wrapper.instance().childrenRef;",
    "      childrenRef.tabIndex = 0;"
   ],
   "context_after": [
    "      assert.strictEqual(document.activeElement, childrenRef);",
    "      assert.strictEqual(wrapper.state().open, false);",
    "      clock.tick(111);",
    "      assert.strictEqual(wrapper.state().open, true);"
   ]
  },
  {
   "path": "Tooltip.test.js",
   "line_number": 181,
   "line": "      assert.strictEqual(document.activeElement, childrenRef);",
   "context_before": [
    "      const wrapper = mount(<TooltipNaked classes={{}} enterDelay={111} {...defaultProps} />);",
    "      const childrenRef = wrapper.instance().childrenRef;",
    "      childrenRef.tabIndex = 0;",
    "      childrenRef.focus();"
   ],
   "context_after": [
    "      assert.strictEqual(wrapper.state().open, false);",
    "      clock.tick(111);",
    "      assert.strictEqual(wrapper.state().open, true);",
    "    });"
   ]
  },
  {
   "path": "Tooltip.test.js",
   "line_number": 191,
   "line": "      childrenRef.focus();",
   "context_before": [
    "    it('should take the leaveDelay into account', () => {",
    "      const wrapper = mount(<TooltipNaked classes={{}} leaveDelay={111} {...defaultProps} />);",
    "      const childrenRef = wrapper.instance().childrenRef;",
    "      childrenRef.tabIndex = 0;"
   ],
   "context_after": [
    "      assert.strictEqual(document.activeElement, childrenRef);",
    "      clock.tick(0);",
    "      assert.strictEqual(wrapper.state().open, true);",
    "      childrenRef.blur();"
   ]
  },
  {
   "path": "Tooltip.test.js",
   "line_number": 192,
   "line": "      assert.strictEqual(document.activeElement, childrenRef);",
   "context_before": [
    "      const wrapper = mount(<TooltipNaked classes={{}} leaveDelay={111} {...defaultProps} />);",
    "      const childrenRef = wrapper.instance().childrenRef;",
    "      childrenRef.tabIndex = 0;",
    "      childrenRef.focus();"
   ],
   "context_after": [
    "      clock.tick(0);",
    "      assert.strictEqual(wrapper.state().open, true);",
    "      childrenRef.blur();",
    "      assert.strictEqual(wrapper.state().open, true);"
   ]
  }
 ],
 "stats": {
  "files_searched": 1,
  "files_with_matches": 1,
  "matches_found": 10,
  "matches_returned": 10,
  "denied_skips": 0,
  "duration_ms": 7,
  "timing": {
   "walk_ms": 0,
   "search_ms": 6,
   "collect_ms": 0,
   "total_ms": 7
  }
 },
 "truncated": false
}
````

### Turn 5 — thinking

````text
I'll keep the timer approach but switch to using a contains check instead, since contains already covers the case where the element itself is the active element—I just need to guard against childrenRef being unset before the timer fires.
````

### Turn 5 — tool call call_0005 (edit)

````json
{
 "file_path": "packages/material-ui/src/Tooltip/Tooltip.js",
 "old_string": "      // We need to make sure the focus hasn't moved since the event was triggered.\n      if (this.childrenRef === document.activeElement) {",
 "new_string": "      // We need to make sure the focus hasn't moved since the event was triggered.\n      // The focused element can be a descendant of the children (e.g. the input of a TextField).\n      if (this.childrenRef && this.childrenRef.contains(document.activeElement)) {"
}
````

Result:

````text
{
 "path": "packages/material-ui/src/Tooltip/Tooltip.js",
 "edited": true,
 "replacements": 1,
 "total_file_lines": 495,
 "total_file_size_bytes": 14193,
 "diff": "-       if (this.childrenRef === document.activeElement) {\n+       // The focused element can be a descendant of the children (e.g. the input of a TextField).\n+       if (this.childrenRef && this.childrenRef.contains(document.activeElement)) {",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "edit",
    "paths": [
     "packages/material-ui/src/Tooltip/Tooltip.js"
    ]
   }
  ]
 },
 "file_change": {
  "kind": "diff",
  "operation": "update",
  "path": "packages/material-ui/src/Tooltip/Tooltip.js",
  "patch": "-       if (this.childrenRef === document.activeElement) {\n+       // The focused element can be a descendant of the children (e.g. the input of a TextField).\n+       if (this.childrenRef && this.childrenRef.contains(document.activeElement)) {",
  "additions": 2,
  "deletions": 1,
  "truncated": false,
  "omitted_lines": 0
 }
}
````

### Turn 6 — assistant text

Now running the existing Tooltip tests:

### Turn 6 — tool call call_0006 (exec)

````json
{
 "command": "grep '\"test:unit\"' package.json; NODE_ENV=test npx mocha packages/material-ui/src/Tooltip/Tooltip.test.js 2>&1 | tail -20",
 "timeout_secs": 300
}
````

Result:

````text
{
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "backgrounded",
  "retryability": "retry_after_wait",
  "open_work_at_failure": false
 },
 "background_exec": {
  "tool_action": "run",
  "task": {
   "task_id": "bg_1_920e96bc47924315a0d81063053e9904",
   "session_id": "cli:default:sa2501976",
   "root_session_id": "cli:default:sa2501976",
   "origin_session_id": "cli:default:sa2501976",
   "status": "running",
   "controls": {
    "list": {
     "method": "background_exec.list",
     "params": {
      "sessionId": "cli:default:sa2501976"
     }
    },
    "logs": {
     "method": "background_exec.logs",
     "params": {
      "sessionId": "cli:default:sa2501976",
      "task_id": "bg_1_920e96bc47924315a0d81063053e9904"
     }
    },
    "wait": {
     "method": "background_exec.wait",
     "params": {
      "sessionId": "cli:default:sa2501976",
      "task_id": "bg_1_920e96bc47924315a0d81063053e9904"
     }
    },
    "stop": {
     "method": "background_exec.stop",
     "params": {
      "sessionId": "cli:default:sa2501976",
      "task_id": "bg_1_920e96bc47924315a0d81063053e9904"
     }
    }
   },
   "title": null,
   "cwd": "/testbed",
   "pid": 813,
   "pgid": 813,
   "runtime_identity_kind": "process",
   "lifecycle_intent": "session_bound",
   "operation_descriptor": {
    "schema_id": "agent.background-exec.operation.v1",
    "requested_type": "auto",
    "session_effective_type": "native",
    "operation_family": "native",
    "isolation_tier": "none",
    "lifecycle_mode": "host-process-group",
    "policy": "transitional-native",
    "reason": {
     "code": "session-native-fallback"
    }
   },
   "process_start_time_ticks": 42821906,
   "started_at_unix_secs": 1792287217,
   "updated_at_unix_secs": 1792287217,
   "finished_at_unix_secs": null,
   "duration_ms": 2,
   "exit_code": null,
   "requested_foreground_timeout_secs": 300,
   "effective_background_timeout_secs": 14400,
   "lease_mode": "renewable",
   "lease_source": "daemon_default",
   "timeout_secs": 14400,
   "output_bytes": 0,
   "last_output_at_unix_secs": null
  },
  "work_id": "bg_1_920e96bc47924315a0d81063053e9904",
  "work_terminal_revision": 1792287217,
  "controls": {
   "list": {
    "method": "background_exec.list",
    "params": {
     "sessionId": "cli:default:sa2501976"
    }
   },
   "logs": {
    "method": "background_exec.logs",
    "params": {
     "sessionId": "cli:default:sa2501976",
     "task_id": "bg_1_920e96bc47924315a0d81063053e9904"
    }
   },
   "wait": {
    "method": "background_exec.wait",
    "params": {
     "sessionId": "cli:default:sa2501976",
     "task_id": "bg_1_920e96bc47924315a0d81063053e9904"
    }
   },
   "stop": {
    "method": "background_exec.stop",
    "params": {
     "sessionId": "cli:default:sa2501976",
     "task_id": "bg_1_920e96bc47924315a0d81063053e9904"
    }
   }
  },
  "_meta": {
   "agent": {
    "background_exec_v1": {
     "controls": {
      "list": {
       "method": "background_exec.list",
       "params": {
        "sessionId": "cli:default:sa2501976"
       }
      },
      "logs": {
       "method": "background_exec.logs",
       "params": {
        "sessionId": "cli:default:sa2501976",
        "task_id": "bg_1_920e96bc47924315a0d81063053e9904"
       }
      },
      "wait": {
       "method": "background_exec.wait",
       "params": {
        "sessionId": "cli:default:sa2501976",
        "task_id": "bg_1_920e96bc47924315a0d81063053e9904"
       }
      },
      "stop": {
       "method": "background_exec.stop",
       "params": {
        "sessionId": "cli:default:sa2501976",
        "task_id": "bg_1_920e96bc47924315a0d81063053e9904"
       }
      }
     },
     "task": {
      "task_id": "bg_1_920e96bc47924315a0d81063053e9904",
      "session_id": "cli:default:sa2501976",
      "root_session_id": "cli:default:sa2501976",
      "origin_session_id": "cli:default:sa2501976",
      "status": "running",
      "controls": {
       "list": {
        "method": "background_exec.list",
        "params": {
         "sessionId": "cli:default:sa2501976"
        }
       },
       "logs": {
        "method": "background_exec.logs",
        "params": {
         "sessionId": "cli:default:sa2501976",
         "task_id": "bg_1_920e96bc47924315a0d81063053e9904"
        }
       },
       "wait": {
        "method": "background_exec.wait",
        "params": {
         "sessionId": "cli:default:sa2501976",
         "task_id": "bg_1_920e96bc47924315a0d81063053e9904"
        }
       },
       "stop": {
        "method": "background_exec.stop",
        "params": {
         "sessionId": "cli:default:sa2501976",
         "task_id": "bg_1_920e96bc47924315a0d81063053e9904"
        }
       }
      },
      "title": null,
      "cwd": "/testbed",
      "pid": 813,
      "pgid": 813,
      "runtime_identity_kind": "process",
      "lifecycle_intent": "session_bound",
      "operation_descriptor": {
       "schema_id": "agent.background-exec.operation.v1",
       "requested_type": "auto",
       "session_effective_type": "native",
       "operation_family": "native",
       "isolation_tier": "none",
       "lifecycle_mode": "host-process-group",
       "policy": "transitional-native",
       "reason": {
        "code": "session-native-fallback"
       }
      },
      "process_start_time_ticks": 42821906,
      "started_at_unix_secs": 1792287217,
      "updated_at_unix_secs": 1792287217,
      "finished_at_unix_secs": null,
      "duration_ms": 2,
      "exit_code": null,
      "requested_foreground_timeout_secs": 300,
      "effective_background_timeout_secs": 14400,
      "lease_mode": "renewable",
      "lease_source": "daemon_default",
      "timeout_secs": 14400,
      "output_bytes": 0,
      "last_output_at_unix_secs": null
     },
     "status": "running",
     "terminal": false
    }
   }
  },
  "tool_outcome": {
   "schema_version": 1,
   "tool_name": "background_exec",
   "status": "backgrounded",
   "retryability": "retry_after_wait",
   "open_work_at_failure": false
  }
 },
 "_agent_context_projection": {
  "schema_version": "agent.exec_tool_result_receipt_preview.v1",
  "content_status": "partial_preview",
  "context_view_limit_bytes": 16384,
  "receipt": {
   "result_id": "tr_a8155d45a26a44e8915d80c3d5bda453",
   "total_bytes": 5304,
   "total_lines": 0,
   "omitted_bytes": 0,
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "artifact": {
   "result_id": "tr_a8155d45a26a44e8915d80c3d5bda453",
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "content_preview": "{\"backgrounded\":true,\"background_exec\":{\"tool_action\":\"run\",\"task\":{\"task_id\":\"bg_1_920e96bc4\n...[agent-cli tool_result context preview: tool_result_delivery_status=delivered; content_status=partial_preview_not_failure; compatibility_marker=tool_result truncated; omitted_bytes=4752; total_bytes=4938; context_view_limit=512 bytes; context_view_strategy=head_tail_compact; guidance=preview_not_failure_outcome_neutral]...\nait timeouts do not kill the task; background_exec.stop is the explicit termination action.\"}"
 }
}
````

### Turn 7 — tool call call_0007 (background_exec)

````json
{
 "action": "wait",
 "task_id": "bg_1_920e96bc47924315a0d81063053e9904",
 "until": "terminal"
}
````
