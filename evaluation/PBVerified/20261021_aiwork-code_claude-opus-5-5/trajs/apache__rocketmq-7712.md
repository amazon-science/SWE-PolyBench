# Instance: apache__rocketmq-7712
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: True

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
[Bug] Deleting the last item problem of the ACL topic/group perms or the global white list caused by the UtilAll#split func flaw
### Before Creating the Bug Report

- [X] I found a bug, not just asking a question, which should be created in [GitHub Discussions](https://github.com/apache/rocketmq/discussions).

- [X] I have searched the [GitHub Issues](https://github.com/apache/rocketmq/issues) and [GitHub Discussions](https://github.com/apache/rocketmq/discussions)  of this repository and believe that this is not a duplicate.

- [X] I have confirmed that this bug belongs to the current repository, not other repositories of RocketMQ.


### Runtime platform environment

OS(CentOS release 7.6.1810)

### RocketMQ version

branch(develop) version(5.1.5-SNAPSHOT)

### JDK Version

Compliler(Oracke JDK 1.8.0_361) OS(CentOS release 7.6.1810)

### Describe the Bug

I found an bug of ACL during my work on RocketMQ.
When I tried to delete the last item of the ACL topic/group perms, there was an error which indicates the resouce fomat is incrorrect. And there's also an similar problem of the global white list, which is always remain an empty data at last.

### Steps to Reproduce

**To reproduce you can use two ways:**
1. If you use the Dashboard(take the topic/group perms for example)
1.1 Create an ACL with mutiple topic perms and group perms.
1.2 Delete the topic perms or group perms one by one.
1.3 The error woud appear when delete the last one.

![AgAACF5zlnReY1XDkERMf6P-SgV5fqC1](https://github.com/apache/rocketmq/assets/29912051/10e0ddc4-84a9-4306-9f13-b29a26c2cddc)
![AgAACF5zlnR_G2hISrFGkp9IHvbLVnhw](https://github.com/apache/rocketmq/assets/29912051/641c7900-25ae-422f-b892-78725dba4fe3)
![AgAACF5zlnQIxRfBwMZA4odWFJ1KCjd_](https://github.com/apache/rocketmq/assets/29912051/64ca490f-838a-43da-b16a-92fc2995a509)

2. If you want to create an test method for reproduce
2.1 New an DefaultMQAdminExt and config it with namesrv and then start it.
2.2 New an PlainAccessConfig and setGroupPerms(Collections.EMPTY_LIST), setTopicPerms(Collections.EMPTY_LIST).
2.3 Then call DefaultMQAdminExt #createAndUpdatePlainAccessConfig.
2.4 Or to call DefaultMQAdminExt #updateGlobalWhiteAddrConfig with the second parmeter an empty string.

![图片](https://github.com/apache/rocketmq/assets/29912051/978d469c-a105-4109-bc9a-76491a5b7cbc)
![图片](https://github.com/apache/rocketmq/assets/29912051/f0c277ee-1e91-4c6e-a627-320c2ac59ec4)


### What Did You Expect to See?

For the topic/group perms, it should not be an error to delete the last item.
![图片](https://github.com/apache/rocketmq/assets/29912051/26cc5b3d-6b9f-455f-a1ba-5c67668dc20f)


For the global white list, it should not be an empty data

![图片](https://github.com/apache/rocketmq/assets/29912051/04377834-cdd7-4a6f-a929-c68bd00482ce)


### What Did You See Instead?

For the topic/group perms, it popup an error: 
org.apache.rocketmq.client.exception.MQClientException: CODE: 209  DESC: Parse Resource format error for .
The expected resource format is 'Res=Perm'. For example: topicA=SUB

![AgAACF5zlnReY1XDkERMf6P-SgV5fqC1](https://github.com/apache/rocketmq/assets/29912051/b06c98b8-852e-4227-9d13-dde47df42f03)

For the global white list, it remains an empty data

![AgAACF5zlnR_G2hISrFGkp9IHvbLVnhw](https://github.com/apache/rocketmq/assets/29912051/794828f0-6471-446c-a885-6e4cd4949803)


### Additional Context

**I've already found and fixed the bug, and I'll submit an PR later.**
````

## Operational trajectory

### Turn 1 — tool call call_0001 (rg)

````json
{
 "pattern": "public static List<String> split",
 "context": 20
}
````

Result:

````text
{
 "output_mode": "content",
 "pattern": "public static List<String> split",
 "search_path": "/testbed",
 "matches": [
  {
   "path": "common/src/main/java/org/apache/rocketmq/common/UtilAll.java",
   "line_number": 679,
   "line": "    public static List<String> split(String str, String splitter) {",
   "context_before": [
    "            file.delete();",
    "        }",
    "    }",
    "",
    "    public static String join(List<String> list, String splitter) {",
    "        if (list == null) {",
    "            return null;",
    "        }",
    "",
    "        StringBuilder str = new StringBuilder();",
    "        for (int i = 0; i < list.size(); i++) {",
    "            str.append(list.get(i));",
    "            if (i == list.size() - 1) {",
    "                break;",
    "            }",
    "            str.append(splitter);",
    "        }",
    "        return str.toString();",
    "    }",
    ""
   ],
   "context_after": [
    "        if (str == null) {",
    "            return null;",
    "        }",
    "",
    "        String[] addrArray = str.split(splitter);",
    "        return Arrays.asList(addrArray);",
    "    }",
    "",
    "    public static void deleteEmptyDirectory(File file) {",
    "        if (file == null || !file.exists()) {",
    "            return;",
    "        }",
    "        if (!file.isDirectory()) {",
    "            return;",
    "        }",
    "        File[] files = file.listFiles();",
    "        if (files == null || files.length <= 0) {",
    "            file.delete();",
    "            STORE_LOG.info(\"delete empty direct, {}\", file.getPath());",
    "        }"
   ]
  }
 ],
 "stats": {
  "files_searched": 2305,
  "files_with_matches": 1,
  "matches_found": 1,
  "matches_returned": 1,
  "denied_skips": 0,
  "duration_ms": 1606,
  "timing": {
   "walk_ms": 0,
   "search_ms": 1605,
   "collect_ms": 0,
   "total_ms": 1606
  }
 },
 "truncated": false
}
````

### Turn 2 — thinking

````text
Splitting an empty string gives a list with one empty string instead of an empty list, so I need to special-case that and return an empty list when the input is blank. I should check what the existing tests expect before changing it.
````

### Turn 2 — tool call call_0002 (rg)

````json
{
 "pattern": "UtilAll.split\\(|testSplit",
 "context": 3
}
````

Result:

````text
{
 "output_mode": "content",
 "pattern": "UtilAll.split\\(|testSplit",
 "search_path": "/testbed",
 "matches": [
  {
   "path": "broker/src/main/java/org/apache/rocketmq/broker/processor/AdminBrokerProcessor.java",
   "line_number": 598,
   "line": "        accessConfig.setTopicPerms(UtilAll.split(requestHeader.getTopicPerms(), \",\"));",
   "context_before": [
    "        accessConfig.setWhiteRemoteAddress(requestHeader.getWhiteRemoteAddress());",
    "        accessConfig.setDefaultTopicPerm(requestHeader.getDefaultTopicPerm());",
    "        accessConfig.setDefaultGroupPerm(requestHeader.getDefaultGroupPerm());"
   ],
   "context_after": [
    "        accessConfig.setGroupPerms(UtilAll.split(requestHeader.getGroupPerms(), \",\"));",
    "        accessConfig.setAdmin(requestHeader.isAdmin());",
    "        try {"
   ]
  },
  {
   "path": "broker/src/main/java/org/apache/rocketmq/broker/processor/AdminBrokerProcessor.java",
   "line_number": 599,
   "line": "        accessConfig.setGroupPerms(UtilAll.split(requestHeader.getGroupPerms(), \",\"));",
   "context_before": [
    "        accessConfig.setDefaultTopicPerm(requestHeader.getDefaultTopicPerm());",
    "        accessConfig.setDefaultGroupPerm(requestHeader.getDefaultGroupPerm());",
    "        accessConfig.setTopicPerms(UtilAll.split(requestHeader.getTopicPerms(), \",\"));"
   ],
   "context_after": [
    "        accessConfig.setAdmin(requestHeader.isAdmin());",
    "        try {",
    ""
   ]
  },
  {
   "path": "broker/src/main/java/org/apache/rocketmq/broker/processor/AdminBrokerProcessor.java",
   "line_number": 672,
   "line": "            if (accessValidator.updateGlobalWhiteAddrsConfig(UtilAll.split(requestHeader.getGlobalWhiteAddrs(), \",\"),",
   "context_before": [
    "",
    "        try {",
    "            AccessValidator accessValidator = this.brokerController.getAccessValidatorMap().get(PlainAccessValidator.class);"
   ],
   "context_after": [
    "                requestHeader.getAclFileFullPath())) {",
    "                response.setCode(ResponseCode.SUCCESS);",
    "                response.setOpaque(request.getOpaque());"
   ]
  },
  {
   "path": "tieredstore/src/test/java/org/apache/rocketmq/tieredstore/util/MessageBufferUtilTest.java",
   "line_number": 153,
   "line": "    public void testSplitMessages() {",
   "context_before": [
    "    }",
    "",
    "    @Test"
   ],
   "context_after": [
    "        ByteBuffer msgBuffer1 = buildMockedMessageBuffer();",
    "        msgBuffer1.putLong(MessageBufferUtil.QUEUE_OFFSET_POSITION, 10);",
    ""
   ]
  }
 ],
 "stats": {
  "files_searched": 2305,
  "files_with_matches": 2,
  "matches_found": 4,
  "matches_returned": 4,
  "denied_skips": 0,
  "duration_ms": 1784,
  "timing": {
   "walk_ms": 0,
   "search_ms": 1782,
   "collect_ms": 0,
   "total_ms": 1784
  }
 },
 "truncated": false
}
````

### Turn 3 — thinking

````text
I recall the upstream fix handles null by returning null early, and blank strings by returning an empty list instead of proceeding further. I should double check the imports are in place for that.
````

### Turn 3 — tool call call_0003 (exec)

````json
{
 "command": "grep -n \"^import\" common/src/main/java/org/apache/rocketmq/common/UtilAll.java"
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
 "stdout": "19:import io.netty.util.internal.PlatformDependent;\n20:import java.io.ByteArrayInputStream;\n21:import java.io.ByteArrayOutputStream;\n22:import java.io.File;\n23:import java.io.IOException;\n24:import java.lang.management.ManagementFactory;\n25:import java.net.Inet4Address;\n26:import java.net.Inet6Address;\n27:import java.net.InetAddress;\n28:import java.net.NetworkInterface;\n29:import java.nio.ByteBuffer;\n30:import java.nio.file.Files;\n31:import java.text.NumberFormat;\n32:import java.text.ParseException;\n33:import java.text.SimpleDateFormat;\n34:import java.util.Arrays;\n35:import java.util.Calendar;\n36:import java.util.Date;\n37:import java.util.Enumeration;\n38:import java.util.Iterator;\n39:import java.util.List;\n40:import java.util.Map;\n41:import java.util.concurrent.TimeUnit;\n42:import java.util.function.Supplier;\n43:import java.util.zip.CRC32;\n44:import java.util.zip.DeflaterOutputStream;\n45:import java.util.zip.InflaterInputStream;\n46:import org.apache.commons.lang3.StringUtils;\n47:import org.apache.commons.validator.routines.InetAddressValidator;\n48:import org.apache.rocketmq.common.constant.LoggerName;\n49:import org.apache.rocketmq.logging.org.slf4j.Logger;\n50:import org.apache.rocketmq.logging.org.slf4j.LoggerFactory;\n",
 "device_targets": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "common/src/main/java/org/apache/rocketmq/common/UtilAll.java"
  ],
  "command_sha256": [
   "30cbce708727db5c065022037af3c2212a855d11562301bca2362c86f35f5063"
  ]
 },
 "duration_ms": 360
}
````

### Turn 4 — tool call call_0004 (apply_patch)

````json
{
 "patch_text": "*** Begin Patch\n*** Update File: common/src/main/java/org/apache/rocketmq/common/UtilAll.java\n@@\n-import java.util.Calendar;\n+import java.util.Calendar;\n+import java.util.Collections;\n@@\n         if (str == null) {\n             return null;\n         }\n \n+        if (StringUtils.isBlank(str)) {\n+            return Collections.emptyList();\n+        }\n+\n         String[] addrArray = str.split(splitter);\n*** End Patch"
}
````

Result:

````text
{
 "plan_id": "3ab507d8b65c8392d0c12def0b06b4f225342ac50bcaf4a401bc6aa082c65622",
 "applied": true,
 "files_modified": [
  "common/src/main/java/org/apache/rocketmq/common/UtilAll.java"
 ],
 "conflicts": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "apply_patch",
    "paths": [
     "common/src/main/java/org/apache/rocketmq/common/UtilAll.java"
    ]
   }
  ]
 }
}
````

### Turn 5 — thinking

````text
I'm wondering whether returning an immutable empty list could cause issues if callers try to mutate it afterward, so maybe using a fresh mutable ArrayList would be safer than Collections.emptyList.
````

### Turn 5 — tool call call_0005 (exec)

````json
{
 "command": "cd common && timeout 300 mvn -q -o compile -Dcheckstyle.skip 2>&1 | tail -20",
 "timeout_secs": 320
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
   "task_id": "bg_1_fce49f75c5544efea8f9f1af09b25b74",
   "session_id": "cli:default:s4ebd8645",
   "root_session_id": "cli:default:s4ebd8645",
   "origin_session_id": "cli:default:s4ebd8645",
   "status": "running",
   "controls": {
    "list": {
     "method": "background_exec.list",
     "params": {
      "sessionId": "cli:default:s4ebd8645"
     }
    },
    "logs": {
     "method": "background_exec.logs",
     "params": {
      "sessionId": "cli:default:s4ebd8645",
      "task_id": "bg_1_fce49f75c5544efea8f9f1af09b25b74"
     }
    },
    "wait": {
     "method": "background_exec.wait",
     "params": {
      "sessionId": "cli:default:s4ebd8645",
      "task_id": "bg_1_fce49f75c5544efea8f9f1af09b25b74"
     }
    },
    "stop": {
     "method": "background_exec.stop",
     "params": {
      "sessionId": "cli:default:s4ebd8645",
      "task_id": "bg_1_fce49f75c5544efea8f9f1af09b25b74"
     }
    }
   },
   "title": null,
   "cwd": "/testbed",
   "pid": 557,
   "pgid": 557,
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
   "process_start_time_ticks": 33205567,
   "started_at_unix_secs": 1792191053,
   "updated_at_unix_secs": 1792191053,
   "finished_at_unix_secs": null,
   "duration_ms": 1,
   "exit_code": null,
   "requested_foreground_timeout_secs": 320,
   "effective_background_timeout_secs": 14400,
   "lease_mode": "renewable",
   "lease_source": "daemon_default",
   "timeout_secs": 14400,
   "output_bytes": 0,
   "last_output_at_unix_secs": null
  },
  "work_id": "bg_1_fce49f75c5544efea8f9f1af09b25b74",
  "work_terminal_revision": 1792191053,
  "controls": {
   "list": {
    "method": "background_exec.list",
    "params": {
     "sessionId": "cli:default:s4ebd8645"
    }
   },
   "logs": {
    "method": "background_exec.logs",
    "params": {
     "sessionId": "cli:default:s4ebd8645",
     "task_id": "bg_1_fce49f75c5544efea8f9f1af09b25b74"
    }
   },
   "wait": {
    "method": "background_exec.wait",
    "params": {
     "sessionId": "cli:default:s4ebd8645",
     "task_id": "bg_1_fce49f75c5544efea8f9f1af09b25b74"
    }
   },
   "stop": {
    "method": "background_exec.stop",
    "params": {
     "sessionId": "cli:default:s4ebd8645",
     "task_id": "bg_1_fce49f75c5544efea8f9f1af09b25b74"
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
        "sessionId": "cli:default:s4ebd8645"
       }
      },
      "logs": {
       "method": "background_exec.logs",
       "params": {
        "sessionId": "cli:default:s4ebd8645",
        "task_id": "bg_1_fce49f75c5544efea8f9f1af09b25b74"
       }
      },
      "wait": {
       "method": "background_exec.wait",
       "params": {
        "sessionId": "cli:default:s4ebd8645",
        "task_id": "bg_1_fce49f75c5544efea8f9f1af09b25b74"
       }
      },
      "stop": {
       "method": "background_exec.stop",
       "params": {
        "sessionId": "cli:default:s4ebd8645",
        "task_id": "bg_1_fce49f75c5544efea8f9f1af09b25b74"
       }
      }
     },
     "task": {
      "task_id": "bg_1_fce49f75c5544efea8f9f1af09b25b74",
      "session_id": "cli:default:s4ebd8645",
      "root_session_id": "cli:default:s4ebd8645",
      "origin_session_id": "cli:default:s4ebd8645",
      "status": "running",
      "controls": {
       "list": {
        "method": "background_exec.list",
        "params": {
         "sessionId": "cli:default:s4ebd8645"
        }
       },
       "logs": {
        "method": "background_exec.logs",
        "params": {
         "sessionId": "cli:default:s4ebd8645",
         "task_id": "bg_1_fce49f75c5544efea8f9f1af09b25b74"
        }
       },
       "wait": {
        "method": "background_exec.wait",
        "params": {
         "sessionId": "cli:default:s4ebd8645",
         "task_id": "bg_1_fce49f75c5544efea8f9f1af09b25b74"
        }
       },
       "stop": {
        "method": "background_exec.stop",
        "params": {
         "sessionId": "cli:default:s4ebd8645",
         "task_id": "bg_1_fce49f75c5544efea8f9f1af09b25b74"
        }
       }
      },
      "title": null,
      "cwd": "/testbed",
      "pid": 557,
      "pgid": 557,
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
      "process_start_time_ticks": 33205567,
      "started_at_unix_secs": 1792191053,
      "updated_at_unix_secs": 1792191053,
      "finished_at_unix_secs": null,
      "duration_ms": 1,
      "exit_code": null,
      "requested_foreground_timeout_secs": 320,
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
   "result_id": "tr_07429e9843e54b5c8aa3b22d608f3b82",
   "total_bytes": 5210,
   "total_lines": 0,
   "omitted_bytes": 0,
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "artifact": {
   "result_id": "tr_07429e9843e54b5c8aa3b22d608f3b82",
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "content_preview": "{\"backgrounded\":true,\"background_exec\":{\"tool_action\":\"run\",\"task\":{\"task_id\":\"bg_1_fce49f75c\n...[agent-cli tool_result context preview: tool_result_delivery_status=delivered; content_status=partial_preview_not_failure; compatibility_marker=tool_result truncated; omitted_bytes=4752; total_bytes=4938; context_view_limit=512 bytes; context_view_strategy=head_tail_compact; guidance=preview_not_failure_outcome_neutral]...\nait timeouts do not kill the task; background_exec.stop is the explicit termination action.\"}"
 }
}
````

### Turn 6 — tool call call_0006 (background_exec)

````json
{
 "action": "wait",
 "task_id": "bg_1_fce49f75c5544efea8f9f1af09b25b74",
 "until": "terminal"
}
````

Result:

````text
{
 "tool_action": "wait",
 "task_id": "bg_1_fce49f75c5544efea8f9f1af09b25b74",
 "work_id": "bg_1_fce49f75c5544efea8f9f1af09b25b74",
 "work_terminal_revision": 1792191068,
 "status": "completed",
 "terminal": true,
 "lease_mode": "renewable",
 "last_output_at_unix_secs": 1792191068,
 "duration_ms": 15083,
 "stdout_delta": "     [java] JVM args ignored when same JVM is used.\n",
 "stderr_delta": "",
 "from_cursor": {
  "stdout": 0,
  "stderr": 0
 },
 "next_cursor": {
  "stdout": 52,
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

### Turn 7 — assistant text

I fixed the bug in `UtilAll.split` (`common/src/main/java/org/apache/rocketmq/common/UtilAll.java`). The `common` module compiles, but I didn't run any tests or reproduce the original ACL error.

**Cause:** Java's `"".split(",")` returns `[""]`, not an empty array. So when the last topic/group perm was deleted, the broker got a list holding one empty string. It then tried to parse that `""` as `Res=Perm` and failed with error 209. The same thing happened with the global white list: an empty string was saved as one empty entry instead of an empty list.

**Fix:** `split` now returns an empty list when the input is blank. A `null` input still returns `null`, as before. I also added the `java.util.Collections` import.

```java
if (StringUtils.isBlank(str)) {
    return Collections.emptyList();
}
```

This applies to all three places that call it in `AdminBrokerProcessor`: `setTopicPerms`, `setGroupPerms` and `updateGlobalWhiteAddrsConfig`.

The returned empty list can't be modified. That matches the old behaviour, since `Arrays.asList` lists can't be resized either.

### Turn 8 — assistant text

I fixed the bug in `UtilAll#split` (`common/src/main/java/org/apache/rocketmq/common/UtilAll.java`). The `common` module compiles cleanly, but I didn't run any tests, including the ACL calls from the bug report.

**Cause:** in Java, `"".split(",")` returns `[""]` rather than an empty array. So when the last topic/group perm was deleted, the broker got a list holding one empty string. It then tried to parse that as `Res=Perm`, which gave the `CODE: 209 ... Parse Resource format error for .` error. The global white list had the same issue: an empty string was stored as one empty entry.

**Fix:** `split` now returns an empty list when the input is blank or only whitespace. A `null` input still returns `null`. I also added the `java.util.Collections` import.

```java
if (StringUtils.isBlank(str)) {
    return Collections.emptyList();
}
```

The returned empty list can't be changed. That should be fine, because the old result from `Arrays.asList` couldn't have elements added either.

## Final answer

I fixed the bug in `UtilAll#split` (`common/src/main/java/org/apache/rocketmq/common/UtilAll.java`). The `common` module compiles cleanly, but I didn't run any tests, including the ACL calls from the bug report.

**Cause:** in Java, `"".split(",")` returns `[""]` rather than an empty array. So when the last topic/group perm was deleted, the broker got a list holding one empty string. It then tried to parse that as `Res=Perm`, which gave the `CODE: 209 ... Parse Resource format error for .` error. The global white list had the same issue: an empty string was stored as one empty entry.

**Fix:** `split` now returns an empty list when the input is blank or only whitespace. A `null` input still returns `null`. I also added the `java.util.Collections` import.

```java
if (StringUtils.isBlank(str)) {
    return Collections.emptyList();
}
```

The returned empty list can't be changed. That should be fine, because the old result from `Arrays.asList` couldn't have elements added either.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 134714 | 1768 | 126150 | 8544 | 136482 |
