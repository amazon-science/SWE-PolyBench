# Instance: prettier__prettier-12930
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: True

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
Syntax error after formatting when using computed key in TypeScript enum
**Prettier 2.6.2**
[Playground link](https://prettier.io/playground/#N4Igxg9gdgLgprEAuECCuBbABAQS8AHSiywG0BLAakoF0iBfEAGhAgAcZzoBnZUAQwBOgiAHcACkIS8U-ADaj+AT14sARoP5gA1nBgBlfhjgAZclDjIAZvO5x1mnXv1st5gObIYgtPdQY1OAATIOCTfih3NH53OAAxCEEMfhhOSOQQfjQYCGYQAAsYDDkAdXzyeG5XMDh9aQryADcKpQywblUQcztBGHFNd2TrWz8AK24AD30POTgARTQIeGG5OxZXQR6MmCU2OG4wQXIOPLYj2BLyIJh85AAOAAZ1kTsSzTYMs-24QUbLFgAjot4P12DJMtwALQWYLBPKCOBA8gI-oxIZIGyrPx2DDkLw+bEzebAywYkYsGD8NSXa63JAAJgpmnIcg8AGEIBh0ahuABWPJoOwAFSpMkxaxAjV8AEkoKFYPpDscYDg5fodrMVnZ6PQgA)
<!-- prettier-ignore -->
```sh
--parser typescript
```

**Input 1:**
<!-- prettier-ignore -->
```tsx
enum A {
  [i++]
}
```

**Output 1:**
<!-- prettier-ignore -->
```tsx
enum A {
  i++,
}

```
**Input 2:**
<!-- prettier-ignore -->
```tsx
const a = "b"
enum A {
  [a] = 2
}
```

**Output 2:**
<!-- prettier-ignore -->
```tsx
const a = "b";
enum A {
  a = 2,
}

```

**Expected behavior:**
The output should be valid syntax. Although TypeScript will error during compiling that computed keys are not allowed in enums, they are valid syntax and parse correctly. Prettier should still support formatting this. Note that TypeScript still produces emit even when erroring, meaning the code would be able to run.

**Actual behavior:**
The output incorrectly removes the brackets, producing a syntax error on example 1, or modifying the runtime behaviour in example 2.

````

## Operational trajectory

### Turn 1 — thinking

````text
The user is asking me to inspect the repo.
````

### Turn 1 — tool call call_0001 (exec)

````json
{
 "command": "cd /testbed && git log --oneline -3 && ls && cat package.json | head -40"
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
 "stdout": "3147244f5 Update dependencies to support TypeScript 4.7 (#12921)\n5b113e71b Add changelog for TypeScript 4.7 (#12901)\n2fc6e5dd4 Support TS 4.7 optional variance (#12900)\nCHANGELOG.md\nCODE_OF_CONDUCT.md\nCONTRIBUTING.md\nDockerfile\nLICENSE\nREADME.md\nbin\nchangelog_unreleased\ncommands.md\ncspell.json\ndocs\nindex.js\njest.config.js\nnetlify.toml\nnode_modules\npackage.json\nscripts\nsrc\nstandalone.js\ntests\ntmp\ntsconfig.json\ntypes\nvendors\nwebsite\nyarn.lock\n{\n  \"name\": \"prettier\",\n  \"version\": \"2.7.0-dev\",\n  \"description\": \"Prettier is an opinionated code formatter\",\n  \"bin\": \"./bin/prettier.js\",\n  \"repository\": \"prettier/prettier\",\n  \"funding\": \"https://github.com/prettier/prettier?sponsor=1\",\n  \"homepage\": \"https://prettier.io\",\n  \"author\": \"James Long\",\n  \"license\": \"MIT\",\n  \"main\": \"./index.js\",\n  \"browser\": \"./standalone.js\",\n  \"unpkg\": \"./standalone.js\",\n  \"engines\": {\n    \"node\": \">=14\"\n  },\n  \"files\": [\n    \"index.js\",\n    \"standalone.js\",\n    \"src\",\n    \"bin\",\n    \"vendors\"\n  ],\n  \"dependencies\": {\n    \"@angular/compiler\": \"12.2.16\",\n    \"@babel/code-frame\": \"7.16.7\",\n    \"@babel/parser\": \"7.18.0\",\n    \"@glimmer/syntax\": \"0.84.2\",\n    \"@iarna/toml\": \"2.2.5\",\n    \"@typescript-eslint/typescript-estree\": \"5.26.0\",\n    \"acorn\": \"8.7.0\",\n    \"acorn-jsx\": \"5.3.2\",\n    \"angular-estree-parser\": \"2.5.0\",\n    \"angular-html-parser\": \"1.8.0\",\n    \"camelcase\": \"6.3.0\",\n    \"chalk\": \"5.0.1\",\n    \"ci-info\": \"3.3.0\",\n    \"cjk-regex\": \"2.0.1\",\n    \"cosmiconfig\": \"7.0.1\",\n    \"css-units-list\": \"1.1.0\",\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 729,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed",
   "package.json"
  ],
  "command_sha256": [
   "8a03407ad6f038912d51a1a802ef4473852a698c137b79861d22331d36cc9cfe"
  ]
 }
}
````

### Turn 2 — tool call call_0002 (rg)

````json
{
 "pattern": "TSEnumMember",
 "path": "src",
 "context": 8
}
````

Result:

````text
{
 "output_mode": "content",
 "pattern": "TSEnumMember",
 "search_path": "/testbed/src",
 "matches": [
  {
   "path": "language-js/print/typescript.js",
   "line_number": 416,
   "line": "    case \"TSEnumMember\":",
   "context_before": [
    "            printDanglingComments(path, options, /* sameIndent */ true),",
    "            hardline,",
    "            \"}\",",
    "          ])",
    "        );",
    "      }",
    "",
    "      return parts;"
   ],
   "context_after": [
    "      parts.push(print(\"id\"));",
    "      if (node.initializer) {",
    "        parts.push(\" = \", print(\"initializer\"));",
    "      }",
    "      return parts;",
    "    case \"TSImportEqualsDeclaration\":",
    "      if (node.isExport) {",
    "        parts.push(\"export \");"
   ]
  }
 ],
 "stats": {
  "files_searched": 231,
  "files_with_matches": 1,
  "matches_found": 1,
  "matches_returned": 1,
  "denied_skips": 0,
  "duration_ms": 80,
  "timing": {
   "walk_ms": 0,
   "search_ms": 80,
   "collect_ms": 0,
   "total_ms": 80
  }
 },
 "truncated": false
}
````

### Turn 3 — thinking

````text
I'm checking whether TSEnumMember includes a computed property in typescript-estree and whether Babel can even parse computed enum members like `[i++]`.
````

### Turn 3 — tool call call_0003 (exec)

````json
{
 "command": "cd /testbed && grep -n \"EnumMember\" -A20 node_modules/@typescript-eslint/typescript-estree/dist/convert.js | head -40"
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
 "stdout": "2132:            case SyntaxKind.EnumMember: {\n2133-                const result = this.createNode(node, {\n2134:                    type: ts_estree_1.AST_NODE_TYPES.TSEnumMember,\n2135-                    id: this.convertChild(node.name),\n2136-                });\n2137-                if (node.initializer) {\n2138-                    result.initializer = this.convertChild(node.initializer);\n2139-                }\n2140-                if (node.name.kind === ts.SyntaxKind.ComputedPropertyName) {\n2141-                    result.computed = true;\n2142-                }\n2143-                return result;\n2144-            }\n2145-            case SyntaxKind.ModuleDeclaration: {\n2146-                const result = this.createNode(node, {\n2147-                    type: ts_estree_1.AST_NODE_TYPES.TSModuleDeclaration,\n2148-                    id: this.convertChild(node.name),\n2149-                });\n2150-                if (node.body) {\n2151-                    result.body = this.convertChild(node.body);\n2152-                }\n2153-                // apply modifiers first...\n2154-                this.applyModifiersToResult(result, node.modifiers);\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 206,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed",
   "node_modules/@typescript-eslint/typescript-estree/dist/convert.js"
  ],
  "command_sha256": [
   "4630c0bcb0621dc66a0447d9916779598f664a3d24e43d63812c498fdf05c2a1"
  ]
 }
}
````

### Turn 4 — tool call call_0004 (edit)

````json
{
 "file_path": "src/language-js/print/typescript.js",
 "old_string": "      parts.push(print(\"id\"));\n      if (node.initializer) {",
 "new_string": "      if (node.computed) {\n        parts.push(\"[\", print(\"id\"), \"]\");\n      } else {\n        parts.push(print(\"id\"));\n      }\n      if (node.initializer) {"
}
````

Result:

````text
{
 "path": "src/language-js/print/typescript.js",
 "edited": true,
 "replacements": 1,
 "total_file_lines": 538,
 "total_file_size_bytes": 15844,
 "diff": "-       parts.push(print(\"id\"));\n+       if (node.computed) {\n+         parts.push(\"[\", print(\"id\"), \"]\");\n+       } else {\n+         parts.push(print(\"id\"));\n+       }",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "edit",
    "paths": [
     "src/language-js/print/typescript.js"
    ]
   }
  ]
 },
 "file_change": {
  "kind": "diff",
  "operation": "update",
  "path": "src/language-js/print/typescript.js",
  "patch": "-       parts.push(print(\"id\"));\n+       if (node.computed) {\n+         parts.push(\"[\", print(\"id\"), \"]\");\n+       } else {\n+         parts.push(print(\"id\"));\n+       }",
  "additions": 5,
  "deletions": 1,
  "truncated": false,
  "omitted_lines": 0
 }
}
````

### Turn 5 — thinking

````text
I should also verify babel can parse the TS syntax correctly, and check whether the cleaning step in clean.js needs any adjustments to handle it.
````

### Turn 5 — tool call call_0005 (exec)

````json
{
 "command": "cd /testbed && printf 'enum A {\\n  [i++],\\n}\\nconst a = \"b\";\\nenum B {\\n  [a] = 2,\\n  [\"c\"] = 3,\\n  d\\n}\\n' > /tmp/t.ts && for p in typescript babel-ts; do echo \"== $p\"; ./bin/prettier.js --parser $p /tmp/t.ts --debug-check; ./bin/prettier.js --parser $p /tmp/t.ts; done"
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
 "stdout": "== typescript\n../tmp/t.ts\nenum A {\n  [i++],\n}\nconst a = \"b\";\nenum B {\n  [a] = 2,\n  [\"c\"] = 3,\n  d,\n}\n== babel-ts\n",
 "stderr": "[error] ../tmp/t.ts: SyntaxError: Unexpected token (2:3)\n[error]   1 | enum A {\n[error] > 2 |   [i++],\n[error]     |   ^\n[error]   3 | }\n[error]   4 | const a = \"b\";\n[error]   5 | enum B {\n[error] ../tmp/t.ts: SyntaxError: Unexpected token (2:3)\n[error]   1 | enum A {\n[error] > 2 |   [i++],\n[error]     |   ^\n[error]   3 | }\n[error]   4 | const a = \"b\";\n[error]   5 | enum B {\n",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed",
   "/tmp/t.ts"
  ],
  "command_sha256": [
   "ae0701030c807372de59825db83b05a445706f9cc61692643fdcd0e93ee15ca4"
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
  "evidence_tail": "[error] ../tmp/t.ts: SyntaxError: Unexpected token (2:3)\n[error]   1 | enum A {\n[error] > 2 |   [i++],\n[error]     |   ^\n[error]   3 | }\n[error]   4 | const a = \"b\";\n[error]   5 | enum B {\n[error] ../tmp/t.ts: SyntaxError: Unexpected token (2:3)\n[error]   1 | enum A {\n[error] > 2 |   [i++],\n[error]     |   ^\n[error]   3 | }\n[error]   4 | const a = \"b\";\n[error]   5 | enum B {\n"
 },
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "device_targets": [],
 "duration_ms": 3282
}
````

### Turn 6 — thinking

````text
Babel's parser simply doesn't support computed enum members, so that's just an inherent limitation. I'll go ahead and run the existing enum tests to check things quickly.
````

### Turn 7 — assistant text

The typescript parser output is correct now; Babel's parser itself rejects computed enum keys, which is outside this fix. I'll run the existing enum tests.

### Turn 7 — tool call call_0006 (exec)

````json
{
 "command": "cd /testbed && rm /tmp/t.ts && yarn jest tests/format/typescript/enum 2>&1 | tail -8",
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
   "task_id": "bg_1_01e79ed46c25473d99255f4d07f600dd",
   "session_id": "cli:default:s401eaab9",
   "root_session_id": "cli:default:s401eaab9",
   "origin_session_id": "cli:default:s401eaab9",
   "status": "running",
   "controls": {
    "list": {
     "method": "background_exec.list",
     "params": {
      "sessionId": "cli:default:s401eaab9"
     }
    },
    "logs": {
     "method": "background_exec.logs",
     "params": {
      "sessionId": "cli:default:s401eaab9",
      "task_id": "bg_1_01e79ed46c25473d99255f4d07f600dd"
     }
    },
    "wait": {
     "method": "background_exec.wait",
     "params": {
      "sessionId": "cli:default:s401eaab9",
      "task_id": "bg_1_01e79ed46c25473d99255f4d07f600dd"
     }
    },
    "stop": {
     "method": "background_exec.stop",
     "params": {
      "sessionId": "cli:default:s401eaab9",
      "task_id": "bg_1_01e79ed46c25473d99255f4d07f600dd"
     }
    }
   },
   "title": null,
   "cwd": "/testbed",
   "pid": 851,
   "pgid": 851,
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
   "process_start_time_ticks": 38555574,
   "started_at_unix_secs": 1792244553,
   "updated_at_unix_secs": 1792244553,
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
  "work_id": "bg_1_01e79ed46c25473d99255f4d07f600dd",
  "work_terminal_revision": 1792244553,
  "controls": {
   "list": {
    "method": "background_exec.list",
    "params": {
     "sessionId": "cli:default:s401eaab9"
    }
   },
   "logs": {
    "method": "background_exec.logs",
    "params": {
     "sessionId": "cli:default:s401eaab9",
     "task_id": "bg_1_01e79ed46c25473d99255f4d07f600dd"
    }
   },
   "wait": {
    "method": "background_exec.wait",
    "params": {
     "sessionId": "cli:default:s401eaab9",
     "task_id": "bg_1_01e79ed46c25473d99255f4d07f600dd"
    }
   },
   "stop": {
    "method": "background_exec.stop",
    "params": {
     "sessionId": "cli:default:s401eaab9",
     "task_id": "bg_1_01e79ed46c25473d99255f4d07f600dd"
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
        "sessionId": "cli:default:s401eaab9"
       }
      },
      "logs": {
       "method": "background_exec.logs",
       "params": {
        "sessionId": "cli:default:s401eaab9",
        "task_id": "bg_1_01e79ed46c25473d99255f4d07f600dd"
       }
      },
      "wait": {
       "method": "background_exec.wait",
       "params": {
        "sessionId": "cli:default:s401eaab9",
        "task_id": "bg_1_01e79ed46c25473d99255f4d07f600dd"
       }
      },
      "stop": {
       "method": "background_exec.stop",
       "params": {
        "sessionId": "cli:default:s401eaab9",
        "task_id": "bg_1_01e79ed46c25473d99255f4d07f600dd"
       }
      }
     },
     "task": {
      "task_id": "bg_1_01e79ed46c25473d99255f4d07f600dd",
      "session_id": "cli:default:s401eaab9",
      "root_session_id": "cli:default:s401eaab9",
      "origin_session_id": "cli:default:s401eaab9",
      "status": "running",
      "controls": {
       "list": {
        "method": "background_exec.list",
        "params": {
         "sessionId": "cli:default:s401eaab9"
        }
       },
       "logs": {
        "method": "background_exec.logs",
        "params": {
         "sessionId": "cli:default:s401eaab9",
         "task_id": "bg_1_01e79ed46c25473d99255f4d07f600dd"
        }
       },
       "wait": {
        "method": "background_exec.wait",
        "params": {
         "sessionId": "cli:default:s401eaab9",
         "task_id": "bg_1_01e79ed46c25473d99255f4d07f600dd"
        }
       },
       "stop": {
        "method": "background_exec.stop",
        "params": {
         "sessionId": "cli:default:s401eaab9",
         "task_id": "bg_1_01e79ed46c25473d99255f4d07f600dd"
        }
       }
      },
      "title": null,
      "cwd": "/testbed",
      "pid": 851,
      "pgid": 851,
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
      "process_start_time_ticks": 38555574,
      "started_at_unix_secs": 1792244553,
      "updated_at_unix_secs": 1792244553,
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
   "result_id": "tr_ade29644831e4b499726019482b97f67",
   "total_bytes": 5226,
   "total_lines": 0,
   "omitted_bytes": 0,
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "artifact": {
   "result_id": "tr_ade29644831e4b499726019482b97f67",
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "content_preview": "{\"backgrounded\":true,\"background_exec\":{\"tool_action\":\"run\",\"task\":{\"task_id\":\"bg_1_01e79ed46\n...[agent-cli tool_result context preview: tool_result_delivery_status=delivered; content_status=partial_preview_not_failure; compatibility_marker=tool_result truncated; omitted_bytes=4752; total_bytes=4938; context_view_limit=512 bytes; context_view_strategy=head_tail_compact; guidance=preview_not_failure_outcome_neutral]...\nait timeouts do not kill the task; background_exec.stop is the explicit termination action.\"}"
 }
}
````

### Turn 8 — tool call call_0007 (background_exec)

````json
{
 "action": "wait",
 "task_id": "bg_1_01e79ed46c25473d99255f4d07f600dd",
 "until": "terminal"
}
````

Result:

````text
{
 "tool_action": "wait",
 "task_id": "bg_1_01e79ed46c25473d99255f4d07f600dd",
 "work_id": "bg_1_01e79ed46c25473d99255f4d07f600dd",
 "work_terminal_revision": 1792244558,
 "status": "completed",
 "terminal": true,
 "lease_mode": "renewable",
 "last_output_at_unix_secs": 1792244558,
 "duration_ms": 4582,
 "stdout_delta": "    ✓ [babel-ts] format (3 ms)\n\nTest Suites: 1 passed, 1 total\nTests:       4 passed, 4 total\nSnapshots:   2 passed, 2 total\nTime:        1.012 s\nRan all test suites matching /tests\\/format\\/typescript\\/enum/i.\nDone in 4.23s.\n",
 "stderr_delta": "",
 "from_cursor": {
  "stdout": 0,
  "stderr": 0
 },
 "next_cursor": {
  "stdout": 228,
  "stderr": 0
 },
 "truncated": false,
 "omitted_bytes": 0,
 "has_more": false,
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "background_exec",
  "status": "success",
  "exit_code": 0,
  "retryability": "not_needed",
  "open_work_at_failure": false
 },
 "wait_timed_out": false,
 "progress_state": "terminal"
}
````

### Turn 9 — assistant text

I fixed the bug: Prettier now keeps the square brackets on computed TypeScript enum keys when using `--parser typescript`.

The fix is in `src/language-js/print/typescript.js`. The typescript parser already marks a bracketed enum key with `computed: true`, but the printer ignored that flag and printed only the name inside. It now adds `[` and `]` when the flag is set.

**Checks:**
- Running `./bin/prettier.js --parser typescript` on a sample file with `[i++]`, `[a] = 2`, `["c"] = 3` and a plain `d` gives back `[i++],`, `[a] = 2,`, `["c"] = 3,` and `d,`. The `--debug-check` option also passed on that file.
- The existing enum tests pass (`yarn jest tests/format/typescript/enum`: 4 tests, 2 snapshots).
- I didn't add or change any tests.

`--parser babel-ts` still can't format this code: Babel's parser rejects `[i++]` inside an enum with "SyntaxError: Unexpected token". That error comes from Babel itself, not Prettier's printer, so I left it alone.

### Turn 10 — assistant text

I fixed the bug: Prettier now keeps the brackets on computed enum keys when using the `typescript` parser.

The cause was in `src/language-js/print/typescript.js`. The parser already marks these enum members as computed, but the code that prints them always wrote the bare name and dropped the brackets. It now writes `[`, the name, `]` when the member is computed.

I ran `--debug-check` with the `typescript` parser on both examples plus a string key and a normal member. They now print as:

```ts
enum A {
  [i++],
}
const a = "b";
enum B {
  [a] = 2,
  ["c"] = 3,
  d,
}
```

The existing enum tests (`yarn jest tests/format/typescript/enum`) pass. I didn't add a new test.

The `babel-ts` parser still fails on this input with `SyntaxError: Unexpected token`, because Babel's parser doesn't accept computed enum keys. That's a parser limitation, not something this fix touches.

## Final answer

I fixed the bug: Prettier now keeps the brackets on computed enum keys when using the `typescript` parser.

The cause was in `src/language-js/print/typescript.js`. The parser already marks these enum members as computed, but the code that prints them always wrote the bare name and dropped the brackets. It now writes `[`, the name, `]` when the member is computed.

I ran `--debug-check` with the `typescript` parser on both examples plus a string key and a normal member. They now print as:

```ts
enum A {
  [i++],
}
const a = "b";
enum B {
  [a] = 2,
  ["c"] = 3,
  d,
}
```

The existing enum tests (`yarn jest tests/format/typescript/enum`) pass. I didn't add a new test.

The `babel-ts` parser still fails on this input with `SyntaxError: Unexpected token`, because Babel's parser doesn't accept computed enum keys. That's a parser limitation, not something this fix touches.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 148803 | 1862 | 115780 | 33003 | 150665 |
