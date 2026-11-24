# Instance: mui__material-ui-26170
# Model: claude-opus-5-5
# Run status: agent_error
# Final resolved: True

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
[TabList] Conditional rendering of Tab fails
<!-- Provide a general summary of the issue in the Title above -->

<!--
  Thank you very much for contributing to Material-UI by creating an issue! ❤️
  To avoid duplicate issues we ask you to check off the following list.
-->

<!-- Checked checkbox should look like this: [x] -->

- [x] The issue is present in the latest release.
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Current Behavior 😯
As pointed on [Issue 8093](https://github.com/mui-org/material-ui/issues/8093), when we have a conditional rendering of a Tab, it throws an error.
<!-- Describe what happens instead of the expected behavior. -->

## Expected Behavior 🤔
The expected behavior is not to consider a null as a valid component. This issue was resolved by [PR 8107](https://github.com/mui-org/material-ui/pull/8107), but for Tabs component.
<!-- Describe what should happen. -->

## Steps to Reproduce 🕹

Just use a condition to render a Tab inside a TabList

[Live example on CodeSandbox](https://codesandbox.io/s/materialui-tablist-conditional-tab-bug-f4rqy)
<!--
  Provide a link to a live example (you can use codesandbox.io) and an unambiguous set of steps to reproduce this bug.
  Include code to reproduce, if relevant (which it most likely is).

  You should use the official codesandbox template as a starting point: https://material-ui.com/r/issue-template-next

  If you have an issue concerning TypeScript please start from this TypeScript playground: https://material-ui.com/r/ts-issue-template

  Issues without some form of live example have a longer response time.
-->

Steps:

1. Render a TabList
2. Render some Tabs
3. Conditionaly render a Tab inside TabList

## Context 🔦

<!--
  What are you trying to accomplish? How has this issue affected you?
  Providing context helps us come up with a solution that is most useful in the real world.
-->
I was trying to render a Tab depending on a user state.

## Your Environment 🌎

<!--
  Run `npx @material-ui/envinfo` and post the results.
  If you encounter issues with TypeScript please include the used tsconfig.
-->
<details>
  <summary>`npx @material-ui/envinfo`</summary>
  
```
  System:
    OS: Linux 5.4 Linux Mint 20.1 (Ulyssa)
  Binaries:
    Node: 14.16.0 - /usr/local/bin/node
    Yarn: 1.22.10 - /usr/local/bin/yarn
    npm: 6.14.13 - /usr/local/bin/npm
  Browsers:
    Chrome: 90.0.4430.93
    Firefox: 88.0.1
  npmPackages:
    @material-ui/core: ^4.11.3 => 4.11.3 
    @material-ui/icons: ^4.11.2 => 4.11.2 
    @material-ui/lab: ^4.0.0-alpha.57 => 4.0.0-alpha.57 
    @material-ui/pickers: ^3.3.10 => 3.3.10 
    @material-ui/styles: ^4.11.3 => 4.11.3 
    @material-ui/system:  4.11.3 
    @material-ui/types:  5.1.0 
    @material-ui/utils:  4.11.2 
    @types/react:  17.0.3 
    react: ^17.0.1 => 17.0.1 
    react-dom: ^17.0.1 => 17.0.1 
    styled-components:  5.2.1
```
</details>
````

## Operational trajectory

### Turn 1 — tool call call_0001 (exec)

````json
{
 "command": "f=$(find packages -path '*TabList/TabList.js' -not -path '*/node_modules/*'); echo $f; cat $f"
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
 "stdout": "packages/material-ui-lab/src/TabList/TabList.js\nimport * as React from 'react';\nimport PropTypes from 'prop-types';\nimport Tabs from '@material-ui/core/Tabs';\nimport { useTabContext, getTabId, getPanelId } from '../TabContext';\n\nconst TabList = React.forwardRef(function TabList(props, ref) {\n  const { children: childrenProp, ...other } = props;\n  const context = useTabContext();\n  if (context === null) {\n    throw new TypeError('No TabContext provided');\n  }\n  const children = React.Children.map(childrenProp, (child) => {\n    return React.cloneElement(child, {\n      // SOMEDAY: `Tabs` will set those themselves\n      'aria-controls': getPanelId(context, child.props.value),\n      id: getTabId(context, child.props.value),\n    });\n  });\n\n  return (\n    <Tabs {...other} ref={ref} value={context.value}>\n      {children}\n    </Tabs>\n  );\n});\n\nTabList.propTypes /* remove-proptypes */ = {\n  // ----------------------------- Warning --------------------------------\n  // | These PropTypes are generated from the TypeScript type definitions |\n  // |     To update them edit the d.ts file and run \"yarn proptypes\"     |\n  // ----------------------------------------------------------------------\n  /**\n   * A list of `<Tab />` elements.\n   */\n  children: PropTypes.arrayOf(PropTypes.element),\n};\n\nexport default TabList;\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 960,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "$f"
  ],
  "command_sha256": [
   "8e461201e3cc8af963f0b3f8265181f26391ab5ed9da6d1be2108e50ab80bd45"
  ]
 }
}
````

### Turn 2 — thinking

````text
I recall that React.Children.map actually invokes the callback even for null children, so I need to guard with isValidElement checks rather than assuming null gets skipped automatically.
````

### Turn 2 — tool call call_0002 (edit)

````json
{
 "file_path": "packages/material-ui-lab/src/TabList/TabList.js",
 "old_string": "  const children = React.Children.map(childrenProp, (child) => {\n    return",
 "new_string": "  const children = React.Children.map(childrenProp, (child) => {\n    if (!React.isValidElement(child)) {\n      return null;\n    }\n\n    return"
}
````

Result:

````text
{
 "path": "packages/material-ui-lab/src/TabList/TabList.js",
 "edited": true,
 "replacements": 1,
 "total_file_lines": 42,
 "total_file_size_bytes": 1340,
 "diff": "+     if (!React.isValidElement(child)) {\n+       return null;\n+     }\n+ ",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "edit",
    "paths": [
     "packages/material-ui-lab/src/TabList/TabList.js"
    ]
   }
  ]
 },
 "file_change": {
  "kind": "diff",
  "operation": "update",
  "path": "packages/material-ui-lab/src/TabList/TabList.js",
  "patch": "+     if (!React.isValidElement(child)) {\n+       return null;\n+     }\n+ ",
  "additions": 4,
  "deletions": 0,
  "truncated": false,
  "omitted_lines": 0
 }
}
````

### Turn 3 — thinking

````text
Let me run the existing TabList tests to check things still work.
````

### Turn 3 — tool call call_0003 (exec)

````json
{
 "command": "yarn -s cross-env NODE_ENV=test mocha 'packages/material-ui-lab/src/TabList/*.test.js' 2>&1 | tail -15",
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
   "task_id": "bg_1_ea324a1d3e594f00af84c4472a1279a3",
   "session_id": "cli:default:s11dc5fd1",
   "root_session_id": "cli:default:s11dc5fd1",
   "origin_session_id": "cli:default:s11dc5fd1",
   "status": "running",
   "controls": {
    "list": {
     "method": "background_exec.list",
     "params": {
      "sessionId": "cli:default:s11dc5fd1"
     }
    },
    "logs": {
     "method": "background_exec.logs",
     "params": {
      "sessionId": "cli:default:s11dc5fd1",
      "task_id": "bg_1_ea324a1d3e594f00af84c4472a1279a3"
     }
    },
    "wait": {
     "method": "background_exec.wait",
     "params": {
      "sessionId": "cli:default:s11dc5fd1",
      "task_id": "bg_1_ea324a1d3e594f00af84c4472a1279a3"
     }
    },
    "stop": {
     "method": "background_exec.stop",
     "params": {
      "sessionId": "cli:default:s11dc5fd1",
      "task_id": "bg_1_ea324a1d3e594f00af84c4472a1279a3"
     }
    }
   },
   "title": null,
   "cwd": "/testbed",
   "pid": 830,
   "pgid": 830,
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
   "process_start_time_ticks": 52249431,
   "started_at_unix_secs": 1792381492,
   "updated_at_unix_secs": 1792381492,
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
  "work_id": "bg_1_ea324a1d3e594f00af84c4472a1279a3",
  "work_terminal_revision": 1792381492,
  "controls": {
   "list": {
    "method": "background_exec.list",
    "params": {
     "sessionId": "cli:default:s11dc5fd1"
    }
   },
   "logs": {
    "method": "background_exec.logs",
    "params": {
     "sessionId": "cli:default:s11dc5fd1",
     "task_id": "bg_1_ea324a1d3e594f00af84c4472a1279a3"
    }
   },
   "wait": {
    "method": "background_exec.wait",
    "params": {
     "sessionId": "cli:default:s11dc5fd1",
     "task_id": "bg_1_ea324a1d3e594f00af84c4472a1279a3"
    }
   },
   "stop": {
    "method": "background_exec.stop",
    "params": {
     "sessionId": "cli:default:s11dc5fd1",
     "task_id": "bg_1_ea324a1d3e594f00af84c4472a1279a3"
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
        "sessionId": "cli:default:s11dc5fd1"
       }
      },
      "logs": {
       "method": "background_exec.logs",
       "params": {
        "sessionId": "cli:default:s11dc5fd1",
        "task_id": "bg_1_ea324a1d3e594f00af84c4472a1279a3"
       }
      },
      "wait": {
       "method": "background_exec.wait",
       "params": {
        "sessionId": "cli:default:s11dc5fd1",
        "task_id": "bg_1_ea324a1d3e594f00af84c4472a1279a3"
       }
      },
      "stop": {
       "method": "background_exec.stop",
       "params": {
        "sessionId": "cli:default:s11dc5fd1",
        "task_id": "bg_1_ea324a1d3e594f00af84c4472a1279a3"
       }
      }
     },
     "task": {
      "task_id": "bg_1_ea324a1d3e594f00af84c4472a1279a3",
      "session_id": "cli:default:s11dc5fd1",
      "root_session_id": "cli:default:s11dc5fd1",
      "origin_session_id": "cli:default:s11dc5fd1",
      "status": "running",
      "controls": {
       "list": {
        "method": "background_exec.list",
        "params": {
         "sessionId": "cli:default:s11dc5fd1"
        }
       },
       "logs": {
        "method": "background_exec.logs",
        "params": {
         "sessionId": "cli:default:s11dc5fd1",
         "task_id": "bg_1_ea324a1d3e594f00af84c4472a1279a3"
        }
       },
       "wait": {
        "method": "background_exec.wait",
        "params": {
         "sessionId": "cli:default:s11dc5fd1",
         "task_id": "bg_1_ea324a1d3e594f00af84c4472a1279a3"
        }
       },
       "stop": {
        "method": "background_exec.stop",
        "params": {
         "sessionId": "cli:default:s11dc5fd1",
         "task_id": "bg_1_ea324a1d3e594f00af84c4472a1279a3"
        }
       }
      },
      "title": null,
      "cwd": "/testbed",
      "pid": 830,
      "pgid": 830,
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
      "process_start_time_ticks": 52249431,
      "started_at_unix_secs": 1792381492,
      "updated_at_unix_secs": 1792381492,
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
   "result_id": "tr_24e87ee9fc064d92b0845edb1b3f7f90",
   "total_bytes": 5262,
   "total_lines": 0,
   "omitted_bytes": 0,
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "artifact": {
   "result_id": "tr_24e87ee9fc064d92b0845edb1b3f7f90",
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "content_preview": "{\"backgrounded\":true,\"background_exec\":{\"tool_action\":\"run\",\"task\":{\"task_id\":\"bg_1_ea324a1d3\n...[agent-cli tool_result context preview: tool_result_delivery_status=delivered; content_status=partial_preview_not_failure; compatibility_marker=tool_result truncated; omitted_bytes=4752; total_bytes=4938; context_view_limit=512 bytes; context_view_strategy=head_tail_compact; guidance=preview_not_failure_outcome_neutral]...\nait timeouts do not kill the task; background_exec.stop is the explicit termination action.\"}"
 }
}
````

### Turn 4 — tool call call_0004 (background_exec)

````json
{
 "action": "wait",
 "task_id": "bg_1_ea324a1d3e594f00af84c4472a1279a3",
 "until": "terminal"
}
````
