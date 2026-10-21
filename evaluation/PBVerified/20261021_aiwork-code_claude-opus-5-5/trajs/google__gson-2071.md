# Instance: google__gson-2071
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: True

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
`EnumMap` deserialization fails with `ClassCastException`
# Gson version
e2e851c9bc692cec68ba7b0cbb002f82b4a229e4

# Java / Android version
openjdk version "11.0.13" 2021-10-19
OpenJDK Runtime Environment Temurin-11.0.13+8 (build 11.0.13+8)
OpenJDK 64-Bit Server VM Temurin-11.0.13+8 (build 11.0.13+8, mixed mode)

# Description
`EnumMap` deserialization fails with `ClassCastException`:
```
java.lang.ClassCastException: class java.util.LinkedHashMap cannot be cast to class java.util.EnumMap
```

The underlying issue is related to #1708, it appears special handling for `EnumMap` is missing.
(I am a bit surprised that this issue has not been mentioned here anywhere before.)

# Reproduction steps
Test case:
```java
private static enum MyEnum {
  VALUE1, VALUE2
}

public void testEnumMap() throws Exception {
  EnumMap<MyEnum, String> map = new EnumMap<MyEnum, String>(MyEnum.class);
  map.put(MyEnum.VALUE1, "test");
  String json = gson.toJson(map);
  assertEquals("{\"VALUE1\":\"test\"}", json);

  Type type = new TypeToken<EnumMap<MyEnum, String>>() {}.getType();
  EnumMap<?, ?> actualMap = gson.fromJson("{\"VALUE1\":\"test\"}", type);
  Map<?, ?> expectedMap = Collections.singletonMap(MyEnum.VALUE1, "test");
  assertEquals(expectedMap, actualMap);
}
```

# Exception stack trace
Not really useful because `ClassCastException` occurs in user code.
````

## Operational trajectory

### Turn 1 — tool call call_0001 (rg)

````json
{
 "pattern": "EnumSet|newDefaultImplementationConstructor|private <T> ObjectConstructor<T> newDefaultConstructor",
 "path": "gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java",
 "context": 3
}
````

Result:

````text
{
 "output_mode": "content",
 "pattern": "EnumSet|newDefaultImplementationConstructor|private <T> ObjectConstructor<T> newDefaultConstructor",
 "search_path": "/testbed/gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java",
 "matches": [
  {
   "path": "ConstructorConstructor.java",
   "line_number": 26,
   "line": "import java.util.EnumSet;",
   "context_before": [
    "import java.util.ArrayDeque;",
    "import java.util.ArrayList;",
    "import java.util.Collection;"
   ],
   "context_after": [
    "import java.util.LinkedHashMap;",
    "import java.util.LinkedHashSet;",
    "import java.util.Map;"
   ]
  },
  {
   "path": "ConstructorConstructor.java",
   "line_number": 91,
   "line": "    ObjectConstructor<T> defaultImplementation = newDefaultImplementationConstructor(type, rawType);",
   "context_before": [
    "      return defaultConstructor;",
    "    }",
    ""
   ],
   "context_after": [
    "    if (defaultImplementation != null) {",
    "      return defaultImplementation;",
    "    }"
   ]
  },
  {
   "path": "ConstructorConstructor.java",
   "line_number": 100,
   "line": "  private <T> ObjectConstructor<T> newDefaultConstructor(Class<? super T> rawType) {",
   "context_before": [
    "    return newUnsafeAllocator(rawType);",
    "  }",
    ""
   ],
   "context_after": [
    "    final Constructor<? super T> constructor;",
    "    try {",
    "      constructor = rawType.getDeclaredConstructor();"
   ]
  },
  {
   "path": "ConstructorConstructor.java",
   "line_number": 155,
   "line": "  private <T> ObjectConstructor<T> newDefaultImplementationConstructor(",
   "context_before": [
    "   * subtypes.",
    "   */",
    "  @SuppressWarnings(\"unchecked\") // use runtime checks to guarantee that 'T' is what it is"
   ],
   "context_after": [
    "      final Type type, Class<? super T> rawType) {",
    "    if (Collection.class.isAssignableFrom(rawType)) {",
    "      if (SortedSet.class.isAssignableFrom(rawType)) {"
   ]
  },
  {
   "path": "ConstructorConstructor.java",
   "line_number": 164,
   "line": "      } else if (EnumSet.class.isAssignableFrom(rawType)) {",
   "context_before": [
    "            return (T) new TreeSet<Object>();",
    "          }",
    "        };"
   ],
   "context_after": [
    "        return new ObjectConstructor<T>() {",
    "          @SuppressWarnings(\"rawtypes\")",
    "          @Override public T construct() {"
   ]
  },
  {
   "path": "ConstructorConstructor.java",
   "line_number": 171,
   "line": "                return (T) EnumSet.noneOf((Class)elementType);",
   "context_before": [
    "            if (type instanceof ParameterizedType) {",
    "              Type elementType = ((ParameterizedType) type).getActualTypeArguments()[0];",
    "              if (elementType instanceof Class) {"
   ],
   "context_after": [
    "              } else {",
    "                throw new JsonIOException(\"Invalid EnumSet type: \" + type.toString());",
    "              }"
   ]
  },
  {
   "path": "ConstructorConstructor.java",
   "line_number": 173,
   "line": "                throw new JsonIOException(\"Invalid EnumSet type: \" + type.toString());",
   "context_before": [
    "              if (elementType instanceof Class) {",
    "                return (T) EnumSet.noneOf((Class)elementType);",
    "              } else {"
   ],
   "context_after": [
    "              }",
    "            } else {",
    "              throw new JsonIOException(\"Invalid EnumSet type: \" + type.toString());"
   ]
  },
  {
   "path": "ConstructorConstructor.java",
   "line_number": 176,
   "line": "              throw new JsonIOException(\"Invalid EnumSet type: \" + type.toString());",
   "context_before": [
    "                throw new JsonIOException(\"Invalid EnumSet type: \" + type.toString());",
    "              }",
    "            } else {"
   ],
   "context_after": [
    "            }",
    "          }",
    "        };"
   ]
  }
 ],
 "stats": {
  "files_searched": 1,
  "files_with_matches": 1,
  "matches_found": 8,
  "matches_returned": 8,
  "denied_skips": 0,
  "duration_ms": 9,
  "timing": {
   "walk_ms": 0,
   "search_ms": 8,
   "collect_ms": 0,
   "total_ms": 9
  }
 },
 "truncated": false
}
````

### Turn 2 — tool call call_0002 (read)

````json
{
 "file_path": "gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java",
 "offset": 70,
 "limit": 180
}
````

Result:

````text
{
 "type": "file",
 "path": "gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java",
 "full_read": false,
 "output": "gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java\n\n70:         }\n71:       };\n72:     }\n73: \n74:     // Next try raw type match for instance creators\n75:     @SuppressWarnings(\"unchecked\") // types must agree\n76:     final InstanceCreator<T> rawTypeCreator =\n77:         (InstanceCreator<T>) instanceCreators.get(rawType);\n78:     if (rawTypeCreator != null) {\n79:       return new ObjectConstructor<T>() {\n80:         @Override public T construct() {\n81:           return rawTypeCreator.createInstance(type);\n82:         }\n83:       };\n84:     }\n85: \n86:     ObjectConstructor<T> defaultConstructor = newDefaultConstructor(rawType);\n87:     if (defaultConstructor != null) {\n88:       return defaultConstructor;\n89:     }\n90: \n91:     ObjectConstructor<T> defaultImplementation = newDefaultImplementationConstructor(type, rawType);\n92:     if (defaultImplementation != null) {\n93:       return defaultImplementation;\n94:     }\n95: \n96:     // finally try unsafe\n97:     return newUnsafeAllocator(rawType);\n98:   }\n99: \n100:   private <T> ObjectConstructor<T> newDefaultConstructor(Class<? super T> rawType) {\n101:     final Constructor<? super T> constructor;\n102:     try {\n103:       constructor = rawType.getDeclaredConstructor();\n104:     } catch (NoSuchMethodException e) {\n105:       return null;\n106:     }\n107: \n108:     final String exceptionMessage = ReflectionHelper.tryMakeAccessible(constructor);\n109:     if (exceptionMessage != null) {\n110:       /*\n111:        * Create ObjectConstructor which throws exception.\n112:        * This keeps backward compatibility (compared to returning `null` which\n113:        * would then choose another way of creating object).\n114:        * And it supports types which are only serialized but not deserialized\n115:        * (compared to directly throwing exception here), e.g. when runtime type\n116:        * of object is inaccessible, but compile-time type is accessible.\n117:        */\n118:       return new ObjectConstructor<T>() {\n119:         @Override\n120:         public T construct() {\n121:           // New exception is created every time to avoid keeping reference\n122:           // to exception with potentially long stack trace, causing a\n123:           // memory leak\n124:           throw new JsonIOException(exceptionMessage);\n125:         }\n126:       };\n127:     }\n128: \n129:     return new ObjectConstructor<T>() {\n130:       @Override public T construct() {\n131:         try {\n132:           @SuppressWarnings(\"unchecked\") // T is the same raw type as is requested\n133:           T newInstance = (T) constructor.newInstance();\n134:           return newInstance;\n135:         } catch (InstantiationException e) {\n136:           // TODO: JsonParseException ?\n137:           throw new RuntimeException(\"Failed to invoke \" + constructor + \" with no args\", e);\n138:         } catch (InvocationTargetException e) {\n139:           // TODO: don't wrap if cause is unchecked!\n140:           // TODO: JsonParseException ?\n141:           throw new RuntimeException(\"Failed to invoke \" + constructor + \" with no args\",\n142:               e.getTargetException());\n143:         } catch (IllegalAccessException e) {\n144:           throw new AssertionError(e);\n145:         }\n146:       }\n147:     };\n148:   }\n149: \n150:   /**\n151:    * Constructors for common interface types like Map and List and their\n152:    * subtypes.\n153:    */\n154:   @SuppressWarnings(\"unchecked\") // use runtime checks to guarantee that 'T' is what it is\n155:   private <T> ObjectConstructor<T> newDefaultImplementationConstructor(\n156:       final Type type, Class<? super T> rawType) {\n157:     if (Collection.class.isAssignableFrom(rawType)) {\n158:       if (SortedSet.class.isAssignableFrom(rawType)) {\n159:         return new ObjectConstructor<T>() {\n160:           @Override public T construct() {\n161:             return (T) new TreeSet<Object>();\n162:           }\n163:         };\n164:       } else if (EnumSet.class.isAssignableFrom(rawType)) {\n165:         return new ObjectConstructor<T>() {\n166:           @SuppressWarnings(\"rawtypes\")\n167:           @Override public T construct() {\n168:             if (type instanceof ParameterizedType) {\n169:               Type elementType = ((ParameterizedType) type).getActualTypeArguments()[0];\n170:               if (elementType instanceof Class) {\n171:                 return (T) EnumSet.noneOf((Class)elementType);\n172:               } else {\n173:                 throw new JsonIOException(\"Invalid EnumSet type: \" + type.toString());\n174:               }\n175:             } else {\n176:               throw new JsonIOException(\"Invalid EnumSet type: \" + type.toString());\n177:             }\n178:           }\n179:         };\n180:       } else if (Set.class.isAssignableFrom(rawType)) {\n181:         return new ObjectConstructor<T>() {\n182:           @Override public T construct() {\n183:             return (T) new LinkedHashSet<Object>();\n184:           }\n185:         };\n186:       } else if (Queue.class.isAssignableFrom(rawType)) {\n187:         return new ObjectConstructor<T>() {\n188:           @Override public T construct() {\n189:             return (T) new ArrayDeque<Object>();\n190:           }\n191:         };\n192:       } else {\n193:         return new ObjectConstructor<T>() {\n194:           @Override public T construct() {\n195:             return (T) new ArrayList<Object>();\n196:           }\n197:         };\n198:       }\n199:     }\n200: \n201:     if (Map.class.isAssignableFrom(rawType)) {\n202:       if (ConcurrentNavigableMap.class.isAssignableFrom(rawType)) {\n203:         return new ObjectConstructor<T>() {\n204:           @Override public T construct() {\n205:             return (T) new ConcurrentSkipListMap<Object, Object>();\n206:           }\n207:         };\n208:       } else if (ConcurrentMap.class.isAssignableFrom(rawType)) {\n209:         return new ObjectConstructor<T>() {\n210:           @Override public T construct() {\n211:             return (T) new ConcurrentHashMap<Object, Object>();\n212:           }\n213:         };\n214:       } else if (SortedMap.class.isAssignableFrom(rawType)) {\n215:         return new ObjectConstructor<T>() {\n216:           @Override public T construct() {\n217:             return (T) new TreeMap<Object, Object>();\n218:           }\n219:         };\n220:       } else if (type instanceof ParameterizedType && !(String.class.isAssignableFrom(\n221:           TypeToken.get(((ParameterizedType) type).getActualTypeArguments()[0]).getRawType()))) {\n222:         return new ObjectConstructor<T>() {\n223:           @Override public T construct() {\n224:             return (T) new LinkedHashMap<Object, Object>();\n225:           }\n226:         };\n227:       } else {\n228:         return new ObjectConstructor<T>() {\n229:           @Override public T construct() {\n230:             return (T) new LinkedTreeMap<String, Object>();\n231:           }\n232:         };\n233:       }\n234:     }\n235: \n236:     return null;\n237:   }\n238: \n239:   private <T> ObjectConstructor<T> newUnsafeAllocator(final Class<? super T> rawType) {\n240:     if (useJdkUnsafe) {\n241:       return new ObjectConstructor<T>() {\n242:         private final UnsafeAllocator unsafeAllocator = UnsafeAllocator.create();\n243:         @Override public T construct() {\n244:           try {\n245:             @SuppressWarnings(\"unchecked\")\n246:             T newInstance = (T) unsafeAllocator.newInstance(rawType);\n247:             return newInstance;\n248:           } catch (Exception e) {\n249:             throw new RuntimeException((\"Unable to create instance of \" + rawType + \". \"\n\n(Returned 180 lines starting at 70; total 270; output truncated — call read again with a higher offset or limit to continue)",
 "offset": 70,
 "limit": 180,
 "lines_returned": 180,
 "total_lines": 270,
 "observed_lines": 270,
 "total_lines_lower_bound": 270,
 "total_lines_exact": true,
 "truncated": true,
 "next_offset": 250,
 "window_bytes_limit": 102400,
 "size_bytes": 9880
}
````

### Turn 3 — thinking

````text
Since EnumMap lacks a no-arg constructor, I need a special branch for it before the general Map handling, keeping in mind that enum key deserialization already works through the enum type adapter.
````

### Turn 3 — tool call call_0003 (apply_patch)

````json
{
 "patch_text": "*** Begin Patch\n*** Update File: gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java\n@@\n     if (Map.class.isAssignableFrom(rawType)) {\n-      if (ConcurrentNavigableMap.class.isAssignableFrom(rawType)) {\n+      // Only support creation of EnumMap, but not of custom subtypes; for them type parameters\n+      // and constructor parameter might have completely different meaning\n+      if (rawType == EnumMap.class) {\n+        return new ObjectConstructor<T>() {\n+          @SuppressWarnings(\"rawtypes\")\n+          @Override public T construct() {\n+            if (type instanceof ParameterizedType) {\n+              Type elementType = ((ParameterizedType) type).getActualTypeArguments()[0];\n+              if (elementType instanceof Class) {\n+                return (T) new EnumMap((Class) elementType);\n+              } else {\n+                throw new JsonIOException(\"Invalid EnumMap type: \" + type.toString());\n+              }\n+            } else {\n+              throw new JsonIOException(\"Invalid EnumMap type: \" + type.toString());\n+            }\n+          }\n+        };\n+      } else if (ConcurrentNavigableMap.class.isAssignableFrom(rawType)) {\n*** End Patch"
}
````

Result:

````text
{
 "plan_id": "dbbebce0ea08d8a78ff7eb30b0be5c25b1585ed0a6d602b20fecb6f728ef45fb",
 "applied": true,
 "files_modified": [
  "gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java"
 ],
 "conflicts": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "apply_patch",
    "paths": [
     "gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java"
    ]
   }
  ]
 }
}
````

### Turn 4 — tool call call_0004 (edit)

````json
{
 "file_path": "gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java",
 "old_string": "import java.util.EnumSet;",
 "new_string": "import java.util.EnumMap;\nimport java.util.EnumSet;"
}
````

Result:

````text
{
 "path": "gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java",
 "edited": true,
 "replacements": 1,
 "total_file_lines": 289,
 "total_file_size_bytes": 10771,
 "diff": "+ import java.util.EnumMap;",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "edit",
    "paths": [
     "gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java"
    ]
   }
  ]
 },
 "file_change": {
  "kind": "diff",
  "operation": "update",
  "path": "gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java",
  "patch": "+ import java.util.EnumMap;",
  "additions": 1,
  "deletions": 0,
  "truncated": false,
  "omitted_lines": 0
 }
}
````

### Turn 5 — assistant text

Now a quick check with the reproduction test.

### Turn 5 — tool call call_0005 (exec)

````json
{
 "command": "cd gson && mkdir -p /tmp/em && cat > /tmp/em/EnumMapRepro.java <<'EOF'\nimport com.google.gson.*; import com.google.gson.reflect.TypeToken; import java.util.*; import java.lang.reflect.Type;\npublic class EnumMapRepro { enum MyEnum { VALUE1, VALUE2 }\n public static void main(String[] a){ Gson gson=new Gson(); EnumMap<MyEnum,String> m=new EnumMap<>(MyEnum.class); m.put(MyEnum.VALUE1,\"test\");\n System.out.println(gson.toJson(m)); Type t=new TypeToken<EnumMap<MyEnum,String>>(){}.getType();\n EnumMap<?,?> r=gson.fromJson(\"{\\\"VALUE1\\\":\\\"test\\\"}\",t); System.out.println(r.getClass()+\" \"+r.equals(Collections.singletonMap(MyEnum.VALUE1,\"test\"))); } }\nEOF\nmvn -q -o compile 2>&1 | tail -5; javac -cp target/classes -d /tmp/em /tmp/em/EnumMapRepro.java && java -cp target/classes:/tmp/em EnumMapRepro; rm -rf /tmp/em",
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
   "task_id": "bg_1_72bce6e6e3a44ffcbbd89b1d16d0d54d",
   "session_id": "cli:default:sb03f1575",
   "root_session_id": "cli:default:sb03f1575",
   "origin_session_id": "cli:default:sb03f1575",
   "status": "running",
   "controls": {
    "list": {
     "method": "background_exec.list",
     "params": {
      "sessionId": "cli:default:sb03f1575"
     }
    },
    "logs": {
     "method": "background_exec.logs",
     "params": {
      "sessionId": "cli:default:sb03f1575",
      "task_id": "bg_1_72bce6e6e3a44ffcbbd89b1d16d0d54d"
     }
    },
    "wait": {
     "method": "background_exec.wait",
     "params": {
      "sessionId": "cli:default:sb03f1575",
      "task_id": "bg_1_72bce6e6e3a44ffcbbd89b1d16d0d54d"
     }
    },
    "stop": {
     "method": "background_exec.stop",
     "params": {
      "sessionId": "cli:default:sb03f1575",
      "task_id": "bg_1_72bce6e6e3a44ffcbbd89b1d16d0d54d"
     }
    }
   },
   "title": null,
   "cwd": "/testbed",
   "pid": 516,
   "pgid": 516,
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
   "process_start_time_ticks": 33373941,
   "started_at_unix_secs": 1792192737,
   "updated_at_unix_secs": 1792192737,
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
  "work_id": "bg_1_72bce6e6e3a44ffcbbd89b1d16d0d54d",
  "work_terminal_revision": 1792192737,
  "controls": {
   "list": {
    "method": "background_exec.list",
    "params": {
     "sessionId": "cli:default:sb03f1575"
    }
   },
   "logs": {
    "method": "background_exec.logs",
    "params": {
     "sessionId": "cli:default:sb03f1575",
     "task_id": "bg_1_72bce6e6e3a44ffcbbd89b1d16d0d54d"
    }
   },
   "wait": {
    "method": "background_exec.wait",
    "params": {
     "sessionId": "cli:default:sb03f1575",
     "task_id": "bg_1_72bce6e6e3a44ffcbbd89b1d16d0d54d"
    }
   },
   "stop": {
    "method": "background_exec.stop",
    "params": {
     "sessionId": "cli:default:sb03f1575",
     "task_id": "bg_1_72bce6e6e3a44ffcbbd89b1d16d0d54d"
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
        "sessionId": "cli:default:sb03f1575"
       }
      },
      "logs": {
       "method": "background_exec.logs",
       "params": {
        "sessionId": "cli:default:sb03f1575",
        "task_id": "bg_1_72bce6e6e3a44ffcbbd89b1d16d0d54d"
       }
      },
      "wait": {
       "method": "background_exec.wait",
       "params": {
        "sessionId": "cli:default:sb03f1575",
        "task_id": "bg_1_72bce6e6e3a44ffcbbd89b1d16d0d54d"
       }
      },
      "stop": {
       "method": "background_exec.stop",
       "params": {
        "sessionId": "cli:default:sb03f1575",
        "task_id": "bg_1_72bce6e6e3a44ffcbbd89b1d16d0d54d"
       }
      }
     },
     "task": {
      "task_id": "bg_1_72bce6e6e3a44ffcbbd89b1d16d0d54d",
      "session_id": "cli:default:sb03f1575",
      "root_session_id": "cli:default:sb03f1575",
      "origin_session_id": "cli:default:sb03f1575",
      "status": "running",
      "controls": {
       "list": {
        "method": "background_exec.list",
        "params": {
         "sessionId": "cli:default:sb03f1575"
        }
       },
       "logs": {
        "method": "background_exec.logs",
        "params": {
         "sessionId": "cli:default:sb03f1575",
         "task_id": "bg_1_72bce6e6e3a44ffcbbd89b1d16d0d54d"
        }
       },
       "wait": {
        "method": "background_exec.wait",
        "params": {
         "sessionId": "cli:default:sb03f1575",
         "task_id": "bg_1_72bce6e6e3a44ffcbbd89b1d16d0d54d"
        }
       },
       "stop": {
        "method": "background_exec.stop",
        "params": {
         "sessionId": "cli:default:sb03f1575",
         "task_id": "bg_1_72bce6e6e3a44ffcbbd89b1d16d0d54d"
        }
       }
      },
      "title": null,
      "cwd": "/testbed",
      "pid": 516,
      "pgid": 516,
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
      "process_start_time_ticks": 33373941,
      "started_at_unix_secs": 1792192737,
      "updated_at_unix_secs": 1792192737,
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
   "result_id": "tr_31ef0a646ba94e489b4e734c3a22e687",
   "total_bytes": 6488,
   "total_lines": 0,
   "omitted_bytes": 0,
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "artifact": {
   "result_id": "tr_31ef0a646ba94e489b4e734c3a22e687",
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "content_preview": "{\"backgrounded\":true,\"background_exec\":{\"tool_action\":\"run\",\"task\":{\"task_id\":\"bg_1_72bce6e6e\n...[agent-cli tool_result context preview: tool_result_delivery_status=delivered; content_status=partial_preview_not_failure; compatibility_marker=tool_result truncated; omitted_bytes=4752; total_bytes=4938; context_view_limit=512 bytes; context_view_strategy=head_tail_compact; guidance=preview_not_failure_outcome_neutral]...\nait timeouts do not kill the task; background_exec.stop is the explicit termination action.\"}"
 }
}
````

### Turn 6 — tool call call_0006 (background_exec)

````json
{
 "action": "wait",
 "task_id": "bg_1_72bce6e6e3a44ffcbbd89b1d16d0d54d",
 "until": "terminal"
}
````

Result:

````text
{
 "tool_action": "wait",
 "task_id": "bg_1_72bce6e6e3a44ffcbbd89b1d16d0d54d",
 "work_id": "bg_1_72bce6e6e3a44ffcbbd89b1d16d0d54d",
 "work_terminal_revision": 1792192742,
 "status": "completed",
 "terminal": true,
 "lease_mode": "renewable",
 "last_output_at_unix_secs": 1792192742,
 "duration_ms": 4744,
 "stdout_delta": "",
 "stderr_delta": "Error: LinkageError occurred while loading main class EnumMapRepro\n\tjava.lang.UnsupportedClassVersionError: EnumMapRepro has been compiled by a more recent version of the Java Runtime (class file version 61.0), this version of the Java Runtime only recognizes class file versions up to 55.0\n",
 "from_cursor": {
  "stdout": 0,
  "stderr": 0
 },
 "next_cursor": {
  "stdout": 0,
  "stderr": 291
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

### Turn 7 — thinking

````text
There's a mismatch between javac and java versions, and mvn compile didn't show any output confirming success—I should try using --release 8 or ensure java comes from the same JDK.
````

### Turn 7 — tool call call_0007 (exec)

````json
{
 "command": "cd gson && mkdir -p /tmp/em && cat > /tmp/em/EnumMapRepro.java <<'EOF'\nimport com.google.gson.*; import com.google.gson.reflect.TypeToken; import java.util.*; import java.lang.reflect.Type;\npublic class EnumMapRepro { enum MyEnum { VALUE1, VALUE2 }\n public static void main(String[] a){ Gson gson=new Gson(); EnumMap<MyEnum,String> m=new EnumMap<>(MyEnum.class); m.put(MyEnum.VALUE1,\"test\");\n System.out.println(gson.toJson(m)); Type t=new TypeToken<EnumMap<MyEnum,String>>(){}.getType();\n EnumMap<?,?> r=gson.fromJson(\"{\\\"VALUE1\\\":\\\"test\\\"}\",t); System.out.println(r.getClass()+\" \"+r.equals(Collections.singletonMap(MyEnum.VALUE1,\"test\"))); } }\nEOF\nls -la target/classes/com/google/gson/internal/ConstructorConstructor.class; javac --release 8 -cp target/classes -d /tmp/em /tmp/em/EnumMapRepro.java && java -cp target/classes:/tmp/em EnumMapRepro; rm -rf /tmp/em",
 "timeout_secs": 120
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
 "stdout": "-rw-r--r-- 1 root root 6659 Oct 16 23:19 target/classes/com/google/gson/internal/ConstructorConstructor.class\n{\"VALUE1\":\"test\"}\nclass java.util.EnumMap true\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 933,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "write",
    "paths": [
     "/tmp/em",
     "/tmp/em/EnumMapRepro.java"
    ]
   }
  ],
  "reads": [
   "/tmp/em",
   "/tmp/em/EnumMapRepro.java",
   "gson",
   "target/classes/com/google/gson/internal/ConstructorConstructor.class"
  ],
  "command_sha256": [
   "369c27af33b6fb1706b32aa160b22ad6089118ecc46a016be188e9f4e1fb7fb6"
  ]
 }
}
````

### Turn 8 — thinking

````text
Let me quickly run the existing MapTest and EnumTest offline to check things pass.
````

### Turn 8 — tool call call_0008 (exec)

````json
{
 "command": "cd gson && mvn -q -o test -Dtest='MapTest,EnumTest,ConstructorConstructorTest*' -DfailIfNoTests=false 2>&1 | tail -30",
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
   "task_id": "bg_2_1c823fc66d4f4078acea224cc8bf3f9a",
   "session_id": "cli:default:sb03f1575",
   "root_session_id": "cli:default:sb03f1575",
   "origin_session_id": "cli:default:sb03f1575",
   "status": "running",
   "controls": {
    "list": {
     "method": "background_exec.list",
     "params": {
      "sessionId": "cli:default:sb03f1575"
     }
    },
    "logs": {
     "method": "background_exec.logs",
     "params": {
      "sessionId": "cli:default:sb03f1575",
      "task_id": "bg_2_1c823fc66d4f4078acea224cc8bf3f9a"
     }
    },
    "wait": {
     "method": "background_exec.wait",
     "params": {
      "sessionId": "cli:default:sb03f1575",
      "task_id": "bg_2_1c823fc66d4f4078acea224cc8bf3f9a"
     }
    },
    "stop": {
     "method": "background_exec.stop",
     "params": {
      "sessionId": "cli:default:sb03f1575",
      "task_id": "bg_2_1c823fc66d4f4078acea224cc8bf3f9a"
     }
    }
   },
   "title": null,
   "cwd": "/testbed",
   "pid": 643,
   "pgid": 643,
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
   "process_start_time_ticks": 33376021,
   "started_at_unix_secs": 1792192758,
   "updated_at_unix_secs": 1792192758,
   "finished_at_unix_secs": null,
   "duration_ms": 3,
   "exit_code": null,
   "requested_foreground_timeout_secs": 300,
   "effective_background_timeout_secs": 14400,
   "lease_mode": "renewable",
   "lease_source": "daemon_default",
   "timeout_secs": 14400,
   "output_bytes": 0,
   "last_output_at_unix_secs": null
  },
  "work_id": "bg_2_1c823fc66d4f4078acea224cc8bf3f9a",
  "work_terminal_revision": 1792192758,
  "controls": {
   "list": {
    "method": "background_exec.list",
    "params": {
     "sessionId": "cli:default:sb03f1575"
    }
   },
   "logs": {
    "method": "background_exec.logs",
    "params": {
     "sessionId": "cli:default:sb03f1575",
     "task_id": "bg_2_1c823fc66d4f4078acea224cc8bf3f9a"
    }
   },
   "wait": {
    "method": "background_exec.wait",
    "params": {
     "sessionId": "cli:default:sb03f1575",
     "task_id": "bg_2_1c823fc66d4f4078acea224cc8bf3f9a"
    }
   },
   "stop": {
    "method": "background_exec.stop",
    "params": {
     "sessionId": "cli:default:sb03f1575",
     "task_id": "bg_2_1c823fc66d4f4078acea224cc8bf3f9a"
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
        "sessionId": "cli:default:sb03f1575"
       }
      },
      "logs": {
       "method": "background_exec.logs",
       "params": {
        "sessionId": "cli:default:sb03f1575",
        "task_id": "bg_2_1c823fc66d4f4078acea224cc8bf3f9a"
       }
      },
      "wait": {
       "method": "background_exec.wait",
       "params": {
        "sessionId": "cli:default:sb03f1575",
        "task_id": "bg_2_1c823fc66d4f4078acea224cc8bf3f9a"
       }
      },
      "stop": {
       "method": "background_exec.stop",
       "params": {
        "sessionId": "cli:default:sb03f1575",
        "task_id": "bg_2_1c823fc66d4f4078acea224cc8bf3f9a"
       }
      }
     },
     "task": {
      "task_id": "bg_2_1c823fc66d4f4078acea224cc8bf3f9a",
      "session_id": "cli:default:sb03f1575",
      "root_session_id": "cli:default:sb03f1575",
      "origin_session_id": "cli:default:sb03f1575",
      "status": "running",
      "controls": {
       "list": {
        "method": "background_exec.list",
        "params": {
         "sessionId": "cli:default:sb03f1575"
        }
       },
       "logs": {
        "method": "background_exec.logs",
        "params": {
         "sessionId": "cli:default:sb03f1575",
         "task_id": "bg_2_1c823fc66d4f4078acea224cc8bf3f9a"
        }
       },
       "wait": {
        "method": "background_exec.wait",
        "params": {
         "sessionId": "cli:default:sb03f1575",
         "task_id": "bg_2_1c823fc66d4f4078acea224cc8bf3f9a"
        }
       },
       "stop": {
        "method": "background_exec.stop",
        "params": {
         "sessionId": "cli:default:sb03f1575",
         "task_id": "bg_2_1c823fc66d4f4078acea224cc8bf3f9a"
        }
       }
      },
      "title": null,
      "cwd": "/testbed",
      "pid": 643,
      "pgid": 643,
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
      "process_start_time_ticks": 33376021,
      "started_at_unix_secs": 1792192758,
      "updated_at_unix_secs": 1792192758,
      "finished_at_unix_secs": null,
      "duration_ms": 3,
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
   "result_id": "tr_0f0dd941c69d4b84b0ab76899e5b893f",
   "total_bytes": 5292,
   "total_lines": 0,
   "omitted_bytes": 0,
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "artifact": {
   "result_id": "tr_0f0dd941c69d4b84b0ab76899e5b893f",
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "content_preview": "{\"backgrounded\":true,\"background_exec\":{\"tool_action\":\"run\",\"task\":{\"task_id\":\"bg_2_1c823fc66\n...[agent-cli tool_result context preview: tool_result_delivery_status=delivered; content_status=partial_preview_not_failure; compatibility_marker=tool_result truncated; omitted_bytes=4752; total_bytes=4938; context_view_limit=512 bytes; context_view_strategy=head_tail_compact; guidance=preview_not_failure_outcome_neutral]...\nait timeouts do not kill the task; background_exec.stop is the explicit termination action.\"}"
 }
}
````

### Turn 9 — tool call call_0009 (background_exec)

````json
{
 "action": "wait",
 "task_id": "bg_2_1c823fc66d4f4078acea224cc8bf3f9a",
 "until": "terminal"
}
````

Result:

````text
{
 "tool_action": "wait",
 "task_id": "bg_2_1c823fc66d4f4078acea224cc8bf3f9a",
 "work_id": "bg_2_1c823fc66d4f4078acea224cc8bf3f9a",
 "work_terminal_revision": 1792192767,
 "status": "completed",
 "terminal": true,
 "lease_mode": "renewable",
 "last_output_at_unix_secs": 1792192767,
 "duration_ms": 8988,
 "stdout_delta": " [proguard] ProGuard, version 7.2.0-beta4\n",
 "stderr_delta": "",
 "from_cursor": {
  "stdout": 0,
  "stderr": 0
 },
 "next_cursor": {
  "stdout": 42,
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

### Turn 10 — thinking

````text
That exits cleanly with no output, which is fine.
````

### Turn 10 — assistant text

`EnumMap` deserialization now works, and the scenario from the report passes.

**Cause:** `EnumMap` has no no-argument constructor, so Gson fell back to its generic `Map` handling and created a `LinkedHashMap`. Your code then failed when it cast that result to `EnumMap`.

**Fix:** In `gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java`, I added a case for `EnumMap` to `newDefaultImplementationConstructor`, checked before the other `Map` cases. It works the same way as the existing `EnumSet` case: it reads the enum key type from the type you pass in and calls `new EnumMap(keyType)`. If the type has no type parameters or the key type isn't a plain class, it throws `JsonIOException("Invalid EnumMap type: ...")`. It only matches `EnumMap` itself, not subclasses, because a subclass's type parameters may not line up with the enum key type. I also added the `java.util.EnumMap` import.

**Checks:**
- I compiled a small standalone program reproducing the report. Serializing gives `{"VALUE1":"test"}`, and deserializing returns a `java.util.EnumMap` equal to the expected map.
- `mvn -o test -Dtest='MapTest,EnumTest,ConstructorConstructorTest*'` exited with code 0. The output was in quiet mode, so I didn't see a per-test summary.

I didn't change any tests or run the full test suite.

### Turn 11 — assistant text

I fixed the bug: deserializing to `EnumMap` now returns an actual `EnumMap`, so the `ClassCastException` no longer happens.

**Cause:** `EnumMap` has no no-argument constructor. Gson treated it like any other `Map` and built a `LinkedHashMap`, which then failed to cast to `EnumMap` in user code.

**Fix:** The only file changed is `gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java`. In `newDefaultImplementationConstructor`, I added an `EnumMap` case at the start of the `Map` section. It works the same way as the existing `EnumSet` handling: it takes the enum key type from the type parameters and calls `new EnumMap(keyClass)`. If the type has no parameters, or the key type isn't a plain class, it throws `JsonIOException("Invalid EnumMap type: ...")`. Only `EnumMap` itself is handled, not its subclasses, because a subclass's type parameters may mean something else.

**Checks:**
- I compiled and ran a scratch program with the reproduction from the issue, then deleted it. Serialization gave `{"VALUE1":"test"}`. Deserialization returned a `java.util.EnumMap` equal to `{VALUE1=test}`.
- `mvn -o test -Dtest='MapTest,EnumTest,ConstructorConstructorTest*'` finished with exit code 0 and reported no failures.
- I didn't run the full test suite, and I didn't add or change any tests.

## Final answer

I fixed the bug: deserializing to `EnumMap` now returns an actual `EnumMap`, so the `ClassCastException` no longer happens.

**Cause:** `EnumMap` has no no-argument constructor. Gson treated it like any other `Map` and built a `LinkedHashMap`, which then failed to cast to `EnumMap` in user code.

**Fix:** The only file changed is `gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java`. In `newDefaultImplementationConstructor`, I added an `EnumMap` case at the start of the `Map` section. It works the same way as the existing `EnumSet` handling: it takes the enum key type from the type parameters and calls `new EnumMap(keyClass)`. If the type has no parameters, or the key type isn't a plain class, it throws `JsonIOException("Invalid EnumMap type: ...")`. Only `EnumMap` itself is handled, not its subclasses, because a subclass's type parameters may mean something else.

**Checks:**
- I compiled and ran a scratch program with the reproduction from the issue, then deleted it. Serialization gave `{"VALUE1":"test"}`. Deserialization returned a `java.util.EnumMap` equal to `{VALUE1=test}`.
- `mvn -o test -Dtest='MapTest,EnumTest,ConstructorConstructorTest*'` finished with exit code 0 and reported no failures.
- I didn't run the full test suite, and I didn't add or change any tests.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 208973 | 3567 | 193790 | 15159 | 212540 |
