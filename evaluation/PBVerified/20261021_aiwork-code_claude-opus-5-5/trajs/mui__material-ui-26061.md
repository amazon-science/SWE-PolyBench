# Instance: mui__material-ui-26061
# Model: claude-opus-5-5
# Run status: agent_error
# Final resolved: True

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
[Tabs] When a Tab is disabled, keyboard traversal is stuck
<!-- Provide a general summary of the issue in the Title above -->
Normally keyboard users will tab into a Tabs group, then use either Left/Right (if horizontal tab) or Up/Down (vertical) to traverse the Tabs and according to [WAI aria practices](https://www.w3.org/TR/wai-aria-practices/#keyboard-interaction-19), the Tabs should wrap around (last <-> first tabs); this works great right now unless a Tab is disabled, in which case it will break the traversal instead of skip the disabled Tab.
<!--
  Thank you very much for contributing to Material-UI by creating an issue! ❤️
  To avoid duplicate issues we ask you to check off the following list.
-->

<!-- Checked checkbox should look like this: [x] -->

- [x] The issue is present in the latest release.
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Current Behavior 😯
If a Tab is in disabled state, then it acts like a hard stop in the traversal order. 
<!-- Describe what happens instead of the expected behavior. -->

## Expected Behavior 🤔
Match the behavior to the way MenuItems with disabled items are traversed and just skip the disabled Tab.  

Maybe you could do something in Tabs.js, handleKeyDown, around here:
```
case previousItemKey:
        newFocusTarget = target.previousElementSibling || tabListRef.current.lastChild;
```
look for disabled state

<!-- Describe what should happen. -->

## Steps to Reproduce 🕹
https://codesandbox.io/s/basictabs-material-demo-forked-sh1rd?file=/demo.js
Hope I forked and saved this correctly.  it's the basic Tab example with a button for convenient focus.  Tab 2 is disabled; you can tab into the Tabs group and then you can see how the arrow traversal hits a wall when it encounters disabled Tab 2.  
<!--
  Provide a link to a live example (you can use codesandbox.io) and an unambiguous set of steps to reproduce this bug.
  Include code to reproduce, if relevant (which it most likely is).

  You should use the official codesandbox template as a starting point: https://material-ui.com/r/issue-template-next

  If you have an issue concerning TypeScript please start from this TypeScript playground: https://material-ui.com/r/ts-issue-template

  Issues without some form of live example have a longer response time.
-->

Steps:

1. Take a look at the codesandbox link
2. If I messed that up, then just take the simple tab demo (first one) and add a disabled on any one of the Tab components

## Context 🔦
a11y compliance
<!--
  What are you trying to accomplish? How has this issue affected you?
  Providing context helps us come up with a solution that is most useful in the real world.
-->

## Your Environment 🌎
this happens on the demo code.
<!--
  Run `npx @material-ui/envinfo` and post the results.
  If you encounter issues with TypeScript please include the used tsconfig.
-->
<details>
  <summary>`npx @material-ui/envinfo`</summary>
  
```
  Don't forget to mention which browser you used.
  Output from `npx @material-ui/envinfo` goes here.
```
</details>
````

## Operational trajectory

### Turn 1 — tool call call_0001 (exec)

````json
{
 "command": "f=$(git ls-files | grep -E 'Tabs/Tabs\\.js$'); echo $f; grep -n \"handleKeyDown\" -A50 $f | head -90"
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
 "stdout": "packages/material-ui/src/Tabs/Tabs.js\n590:  const handleKeyDown = (event) => {\n591-    const { target } = event;\n592-    // Keyboard navigation assumes that [role=\"tab\"] are siblings\n593-    // though we might warn in the future about nested, interactive elements\n594-    // as a a11y violation\n595-    const role = target.getAttribute('role');\n596-    if (role !== 'tab') {\n597-      return;\n598-    }\n599-\n600-    let newFocusTarget = null;\n601-    let previousItemKey = orientation === 'horizontal' ? 'ArrowLeft' : 'ArrowUp';\n602-    let nextItemKey = orientation === 'horizontal' ? 'ArrowRight' : 'ArrowDown';\n603-    if (orientation === 'horizontal' && isRtl) {\n604-      // swap previousItemKey with nextItemKey\n605-      previousItemKey = 'ArrowRight';\n606-      nextItemKey = 'ArrowLeft';\n607-    }\n608-\n609-    switch (event.key) {\n610-      case previousItemKey:\n611-        newFocusTarget = target.previousElementSibling || tabListRef.current.lastChild;\n612-        break;\n613-      case nextItemKey:\n614-        newFocusTarget = target.nextElementSibling || tabListRef.current.firstChild;\n615-        break;\n616-      case 'Home':\n617-        newFocusTarget = tabListRef.current.firstChild;\n618-        break;\n619-      case 'End':\n620-        newFocusTarget = tabListRef.current.lastChild;\n621-        break;\n622-      default:\n623-        break;\n624-    }\n625-\n626-    if (newFocusTarget !== null) {\n627-      newFocusTarget.focus();\n628-      event.preventDefault();\n629-    }\n630-  };\n631-\n632-  const conditionalElements = getConditionalElements();\n633-\n634-  return (\n635-    <TabsRoot\n636-      className={clsx(classes.root, className)}\n637-      styleProps={styleProps}\n638-      ref={ref}\n639-      as={component}\n640-      {...other}\n--\n663:          onKeyDown={handleKeyDown}\n664-          ref={tabListRef}\n665-          role=\"tablist\"\n666-        >\n667-          {children}\n668-        </FlexContainer>\n669-        {mounted && indicator}\n670-      </TabsScroller>\n671-      {conditionalElements.scrollButtonEnd}\n672-    </TabsRoot>\n673-  );\n674-});\n675-\n676-Tabs.propTypes /* remove-proptypes */ = {\n677-  // ----------------------------- Warning --------------------------------\n678-  // | These PropTypes are generated from the TypeScript type definitions |\n679-  // |     To update them edit the d.ts file and run \"yarn proptypes\"     |\n680-  // ----------------------------------------------------------------------\n681-  /**\n682-   * Callback fired when the component mounts.\n683-   * This is useful when you want to trigger an action programmatically.\n684-   * It supports two actions: `updateIndicator()` and `updateScrollButtons()`\n685-   *\n686-   * @param {object} actions This object contains all possible actions\n687-   * that can be triggered programmatically.\n688-   */\n689-  action: refType,\n690-  /**\n691-   * If `true`, the scroll buttons aren't forced hidden on mobile.\n692-   * By default the scroll buttons are hidden on mobile and takes precedence over `scrollButtons`.\n693-   * @default false\n694-   */\n695-  allowScrollButtonsMobile: PropTypes.bool,\n696-  /**\n697-   * The label for the Tabs as a string.\n698-   */\n699-  'aria-label': PropTypes.string,\n700-  /**\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 947,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "$f"
  ],
  "command_sha256": [
   "4fe175208b35dd6c964393e9845b054f55b1aa4fe10dd9697ecad8bf1bca2b95"
  ]
 }
}
````

### Turn 2 — thinking

````text
I'm looking at how MUI implements moveFocus for MenuList to model disabled-item skipping, with Home/End keys jumping to the first non-disabled item and disabled buttons getting the proper disabled attribute instead of just aria-disabled.
````

### Turn 2 — tool call call_0002 (exec)

````json
{
 "command": "cd packages/material-ui/src/Tabs && python3 - <<'EOF'\np='Tabs.js'\ns=open(p).read()\nold=s[s.index(\"    let newFocusTarget = null;\\n\"):s.index(\"  const conditionalElements = getConditionalElements();\")]\nnew='''    let previousItemKey = orientation === 'horizontal' ? 'ArrowLeft' : 'ArrowUp';\n    let nextItemKey = orientation === 'horizontal' ? 'ArrowRight' : 'ArrowDown';\n    if (orientation === 'horizontal' && isRtl) {\n      // swap previousItemKey with nextItemKey\n      previousItemKey = 'ArrowRight';\n      nextItemKey = 'ArrowLeft';\n    }\n\n    const list = tabListRef.current;\n\n    switch (event.key) {\n      case previousItemKey:\n        event.preventDefault();\n        moveFocus(list, target, previousItem);\n        break;\n      case nextItemKey:\n        event.preventDefault();\n        moveFocus(list, target, nextItem);\n        break;\n      case 'Home':\n        event.preventDefault();\n        moveFocus(list, null, nextItem);\n        break;\n      case 'End':\n        event.preventDefault();\n        moveFocus(list, null, previousItem);\n        break;\n      default:\n        break;\n    }\n  };\n\n'''\ns=s.replace(old,new)\nhelpers='''const nextItem = (list, item) => {\n  if (list === item) {\n    return list.firstChild;\n  }\n  if (item && item.nextElementSibling) {\n    return item.nextElementSibling;\n  }\n  return list.firstChild;\n};\n\nconst previousItem = (list, item) => {\n  if (list === item) {\n    return list.lastChild;\n  }\n  if (item && item.previousElementSibling) {\n    return item.previousElementSibling;\n  }\n  return list.lastChild;\n};\n\nconst moveFocus = (list, currentFocus, traversalFunction) => {\n  let wrappedOnce = false;\n  let nextFocus = traversalFunction(list, currentFocus);\n\n  while (nextFocus) {\n    // Prevent infinite loop.\n    if (nextFocus === list.firstChild) {\n      if (wrappedOnce) {\n        return;\n      }\n      wrappedOnce = true;\n    }\n\n    // Same logic as useAutocomplete.js\n    const nextFocusDisabled =\n      nextFocus.disabled || nextFocus.getAttribute('aria-disabled') === 'true';\n\n    if (!nextFocus.hasAttribute('tabindex') || nextFocusDisabled) {\n      // Move to the next element.\n      nextFocus = traversalFunction(list, nextFocus);\n    } else {\n      nextFocus.focus();\n      return;\n    }\n  }\n};\n\nconst Tabs = React.forwardRef('''\nassert s.count(\"const Tabs = React.forwardRef(\")==1\ns=s.replace(\"const Tabs = React.forwardRef(\",helpers)\nopen(p,'w').write(s)\nEOF\ngit diff --stat; grep -n \"tabIndex\" Tab.js"
}
````

Result:

````text
{
 "tool_diagnostic": {
  "schema_version": 1,
  "code": "exec.execution.nonzero_exit",
  "failure_stage": "execution",
  "cause_domain": "local_process",
  "owner": "exec",
  "classification_source": "producer_explicit",
  "failure_scope": "invocation",
  "action": "run"
 },
 "stdout": " package.json                          |     9 +-\n packages/material-ui/src/Tabs/Tabs.js |    67 +-\n yarn.lock                             | 31090 +++++++++++++++++---------------\n 3 files changed, 16412 insertions(+), 14754 deletions(-)\n",
 "stderr": "grep: Tab.js: No such file or directory\n",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "Tab.js",
   "packages/material-ui/src/Tabs"
  ],
  "command_sha256": [
   "cd456b0a76a514b5c734f1d79e406f566e5fc0758d5a310feb93cb098d110aff"
  ]
 },
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "failed",
  "exit_code": 2,
  "failure_class": "unknown",
  "retryability": "retry_after_change",
  "open_work_at_failure": false,
  "evidence_tail": "grep: Tab.js: No such file or directory\n"
 },
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "device_targets": [],
 "duration_ms": 508
}
````

### Turn 3 — thinking

````text
I'm noting the package.json/yarn.lock changes were already there, and verifying that tabIndex is correctly handled through ButtonBase and Tab — selected tabs get tabIndex 0, others -1. That looks correct, so I'll move on to running the tests.
````

### Turn 3 — tool call call_0003 (exec)

````json
{
 "command": "grep -n \"tabIndex\" packages/material-ui/src/Tab/Tab.js packages/material-ui/src/ButtonBase/ButtonBase.js | head; yarn -s mocha packages/material-ui/src/Tabs/Tabs.test.js 2>&1 | tail -30",
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
   "task_id": "bg_1_209fde2f627a44d58f695569ecd2a83c",
   "session_id": "cli:default:s22393d76",
   "root_session_id": "cli:default:s22393d76",
   "origin_session_id": "cli:default:s22393d76",
   "status": "running",
   "controls": {
    "list": {
     "method": "background_exec.list",
     "params": {
      "sessionId": "cli:default:s22393d76"
     }
    },
    "logs": {
     "method": "background_exec.logs",
     "params": {
      "sessionId": "cli:default:s22393d76",
      "task_id": "bg_1_209fde2f627a44d58f695569ecd2a83c"
     }
    },
    "wait": {
     "method": "background_exec.wait",
     "params": {
      "sessionId": "cli:default:s22393d76",
      "task_id": "bg_1_209fde2f627a44d58f695569ecd2a83c"
     }
    },
    "stop": {
     "method": "background_exec.stop",
     "params": {
      "sessionId": "cli:default:s22393d76",
      "task_id": "bg_1_209fde2f627a44d58f695569ecd2a83c"
     }
    }
   },
   "title": null,
   "cwd": "/testbed",
   "pid": 857,
   "pgid": 857,
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
   "process_start_time_ticks": 51818826,
   "started_at_unix_secs": 1792377186,
   "updated_at_unix_secs": 1792377186,
   "finished_at_unix_secs": null,
   "duration_ms": 1,
   "exit_code": null,
   "requested_foreground_timeout_secs": 300,
   "effective_background_timeout_secs": 14400,
   "lease_mode": "renewable",
   "lease_source": "daemon_default",
   "timeout_secs": 14400,
   "output_bytes": 0,
   "last_output_at_unix_secs": null
  },
  "work_id": "bg_1_209fde2f627a44d58f695569ecd2a83c",
  "work_terminal_revision": 1792377186,
  "controls": {
   "list": {
    "method": "background_exec.list",
    "params": {
     "sessionId": "cli:default:s22393d76"
    }
   },
   "logs": {
    "method": "background_exec.logs",
    "params": {
     "sessionId": "cli:default:s22393d76",
     "task_id": "bg_1_209fde2f627a44d58f695569ecd2a83c"
    }
   },
   "wait": {
    "method": "background_exec.wait",
    "params": {
     "sessionId": "cli:default:s22393d76",
     "task_id": "bg_1_209fde2f627a44d58f695569ecd2a83c"
    }
   },
   "stop": {
    "method": "background_exec.stop",
    "params": {
     "sessionId": "cli:default:s22393d76",
     "task_id": "bg_1_209fde2f627a44d58f695569ecd2a83c"
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
        "sessionId": "cli:default:s22393d76"
       }
      },
      "logs": {
       "method": "background_exec.logs",
       "params": {
        "sessionId": "cli:default:s22393d76",
        "task_id": "bg_1_209fde2f627a44d58f695569ecd2a83c"
       }
      },
      "wait": {
       "method": "background_exec.wait",
       "params": {
        "sessionId": "cli:default:s22393d76",
        "task_id": "bg_1_209fde2f627a44d58f695569ecd2a83c"
       }
      },
      "stop": {
       "method": "background_exec.stop",
       "params": {
        "sessionId": "cli:default:s22393d76",
        "task_id": "bg_1_209fde2f627a44d58f695569ecd2a83c"
       }
      }
     },
     "task": {
      "task_id": "bg_1_209fde2f627a44d58f695569ecd2a83c",
      "session_id": "cli:default:s22393d76",
      "root_session_id": "cli:default:s22393d76",
      "origin_session_id": "cli:default:s22393d76",
      "status": "running",
      "controls": {
       "list": {
        "method": "background_exec.list",
        "params": {
         "sessionId": "cli:default:s22393d76"
        }
       },
       "logs": {
        "method": "background_exec.logs",
        "params": {
         "sessionId": "cli:default:s22393d76",
         "task_id": "bg_1_209fde2f627a44d58f695569ecd2a83c"
        }
       },
       "wait": {
        "method": "background_exec.wait",
        "params": {
         "sessionId": "cli:default:s22393d76",
         "task_id": "bg_1_209fde2f627a44d58f695569ecd2a83c"
        }
       },
       "stop": {
        "method": "background_exec.stop",
        "params": {
         "sessionId": "cli:default:s22393d76",
         "task_id": "bg_1_209fde2f627a44d58f695569ecd2a83c"
        }
       }
      },
      "title": null,
      "cwd": "/testbed",
      "pid": 857,
      "pgid": 857,
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
      "process_start_time_ticks": 51818826,
      "started_at_unix_secs": 1792377186,
      "updated_at_unix_secs": 1792377186,
      "finished_at_unix_secs": null,
      "duration_ms": 1,
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
   "result_id": "tr_9a69d1a7d46c4a92a66f5f4ad556de1e",
   "total_bytes": 5432,
   "total_lines": 0,
   "omitted_bytes": 0,
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "artifact": {
   "result_id": "tr_9a69d1a7d46c4a92a66f5f4ad556de1e",
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "content_preview": "{\"backgrounded\":true,\"background_exec\":{\"tool_action\":\"run\",\"task\":{\"task_id\":\"bg_1_209fde2f6\n...[agent-cli tool_result context preview: tool_result_delivery_status=delivered; content_status=partial_preview_not_failure; compatibility_marker=tool_result truncated; omitted_bytes=4752; total_bytes=4938; context_view_limit=512 bytes; context_view_strategy=head_tail_compact; guidance=preview_not_failure_outcome_neutral]...\nait timeouts do not kill the task; background_exec.stop is the explicit termination action.\"}"
 }
}
````

### Turn 4 — tool call call_0004 (background_exec)

````json
{
 "action": "wait",
 "task_id": "bg_1_209fde2f627a44d58f695569ecd2a83c",
 "until": "terminal"
}
````
