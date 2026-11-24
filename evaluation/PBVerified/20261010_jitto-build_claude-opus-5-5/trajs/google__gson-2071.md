# Instance: google__gson-2071

- Final resolved (evaluator, logs/google__gson-2071_result.json): True
- Run state: DONE
- One attempt. Duration 85.8 s, turns 11, actor cost $0.2295212, container commands 6
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/google__gson-2071/repo
</uploaded_files>
I've uploaded a Java code repository in the directory /work/google__gson-2071/repo. Consider the following issue description:

<issue_description>
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


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/google__gson-2071/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/google__gson-2071/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/google__gson-2071/bin/envrun 'git status --short && ls'
Edits you make under /work/google__gson-2071/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
grep -n "EnumSet\|newDefaultImplementationConstructor\|Map\b" -n gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java | head -50
```

tool result:

```
26:import java.util.EnumSet;
27:import java.util.LinkedHashMap;
29:import java.util.Map;
32:import java.util.SortedMap;
34:import java.util.TreeMap;
36:import java.util.concurrent.ConcurrentHashMap;
37:import java.util.concurrent.ConcurrentMap;
38:import java.util.concurrent.ConcurrentNavigableMap;
39:import java.util.concurrent.ConcurrentSkipListMap;
50:  private final Map<Type, InstanceCreator<?>> instanceCreators;
53:  public ConstructorConstructor(Map<Type, InstanceCreator<?>> instanceCreators, boolean useJdkUnsafe) {
91:    ObjectConstructor<T> defaultImplementation = newDefaultImplementationConstructor(type, rawType);
151:   * Constructors for common interface types like Map and List and their
155:  private <T> ObjectConstructor<T> newDefaultImplementationConstructor(
164:      } else if (EnumSet.class.isAssignableFrom(rawType)) {
171:                return (T) EnumSet.noneOf((Class)elementType);
173:                throw new JsonIOException("Invalid EnumSet type: " + type.toString());
176:              throw new JsonIOException("Invalid EnumSet type: " + type.toString());
201:    if (Map.class.isAssignableFrom(rawType)) {
202:      if (ConcurrentNavigableMap.class.isAssignableFrom(rawType)) {
205:            return (T) new ConcurrentSkipListMap<Object, Object>();
208:      } else if (ConcurrentMap.class.isAssignableFrom(rawType)) {
211:            return (T) new ConcurrentHashMap<Object, Object>();
214:      } else if (SortedMap.class.isAssignableFrom(rawType)) {
217:            return (T) new TreeMap<Object, Object>();
224:            return (T) new LinkedHashMap<Object, Object>();
230:            return (T) new LinkedTreeMap<String, Object>();
```

**tool call: Bash**

```bash
sed -n 80,240p gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java
```

tool result:

```
        @Override public T construct() {
          return rawTypeCreator.createInstance(type);
        }
      };
    }

    ObjectConstructor<T> defaultConstructor = newDefaultConstructor(rawType);
    if (defaultConstructor != null) {
      return defaultConstructor;
    }

    ObjectConstructor<T> defaultImplementation = newDefaultImplementationConstructor(type, rawType);
    if (defaultImplementation != null) {
      return defaultImplementation;
    }

    // finally try unsafe
    return newUnsafeAllocator(rawType);
  }

  private <T> ObjectConstructor<T> newDefaultConstructor(Class<? super T> rawType) {
    final Constructor<? super T> constructor;
    try {
      constructor = rawType.getDeclaredConstructor();
    } catch (NoSuchMethodException e) {
      return null;
    }

    final String exceptionMessage = ReflectionHelper.tryMakeAccessible(constructor);
    if (exceptionMessage != null) {
      /*
       * Create ObjectConstructor which throws exception.
       * This keeps backward compatibility (compared to returning `null` which
       * would then choose another way of creating object).
       * And it supports types which are only serialized but not deserialized
       * (compared to directly throwing exception here), e.g. when runtime type
       * of object is inaccessible, but compile-time type is accessible.
       */
      return new ObjectConstructor<T>() {
        @Override
        public T construct() {
          // New exception is created every time to avoid keeping reference
          // to exception with potentially long stack trace, causing a
          // memory leak
          throw new JsonIOException(exceptionMessage);
        }
      };
    }

    return new ObjectConstructor<T>() {
      @Override public T construct() {
        try {
          @SuppressWarnings("unchecked") // T is the same raw type as is requested
          T newInstance = (T) constructor.newInstance();
          return newInstance;
        } catch (InstantiationException e) {
          // TODO: JsonParseException ?
          throw new RuntimeException("Failed to invoke " + constructor + " with no args", e);
        } catch (InvocationTargetException e) {
          // TODO: don't wrap if cause is unchecked!
          // TODO: JsonParseException ?
          throw new RuntimeException("Failed to invoke " + constructor + " with no args",
              e.getTargetException());
        } catch (IllegalAccessException e) {
          throw new AssertionError(e);
        }
      }
    };
  }

  /**
   * Constructors for common interface types like Map and List and their
   * subtypes.
   */
  @SuppressWarnings("unchecked") // use runtime checks to guarantee that 'T' is what it is
  private <T> ObjectConstructor<T> newDefaultImplementationConstructor(
      final Type type, Class<? super T> rawType) {
    if (Collection.class.isAssignableFrom(rawType)) {
      if (SortedSet.class.isAssignableFrom(rawType)) {
        return new ObjectConstructor<T>() {
          @Override public T construct() {
            return (T) new TreeSet<Object>();
          }
        };
      } else if (EnumSet.class.isAssignableFrom(rawType)) {
        return new ObjectConstructor<T>() {
          @SuppressWarnings("rawtypes")
          @Override public T construct() {
            if (type instanceof ParameterizedType) {
              Type elementType = ((ParameterizedType) type).getActualTypeArguments()[0];
              if (elementType instanceof Class) {
                return (T) EnumSet.noneOf((Class)elementType);
              } else {
                throw new JsonIOException("Invalid EnumSet type: " + type.toString());
              }
            } else {
              throw new JsonIOException("Invalid EnumSet type: " + type.toString());
            }
          }
        };
      } else if (Set.class.isAssignableFrom(rawType)) {
        return new ObjectConstructor<T>() {
          @Override public T construct() {
            return (T) new LinkedHashSet<Object>();
          }
        };
      } else if (Queue.class.isAssignableFrom(rawType)) {
        return new ObjectConstructor<T>() {
          @Override public T construct() {
            return (T) new ArrayDeque<Object>();
          }
        };
      } else {
        return new ObjectConstructor<T>() {
          @Override public T construct() {
            return (T) new ArrayList<Object>();
          }
        };
      }
    }

    if (Map.class.isAssignableFrom(rawType)) {
      if (ConcurrentNavigableMap.class.isAssignableFrom(rawType)) {
        return new ObjectConstructor<T>() {
          @Override public T construct() {
            return (T) new ConcurrentSkipListMap<Object, Object>();
          }
        };
      } else if (ConcurrentMap.class.isAssignableFrom(rawType)) {
        return new ObjectConstructor<T>() {
          @Override public T construct() {
            return (T) new ConcurrentHashMap<Object, Object>();
          }
        };
      } else if (SortedMap.class.isAssignableFrom(rawType)) {
        return new ObjectConstructor<T>() {
          @Override public T construct() {
            return (T) new TreeMap<Object, Object>();
          }
        };
      } else if (type instanceof ParameterizedType && !(String.class.isAssignableFrom(
          TypeToken.get(((ParameterizedType) type).getActualTypeArguments()[0]).getRawType()))) {
        return new ObjectConstructor<T>() {
          @Override public T construct() {
            return (T) new LinkedHashMap<Object, Object>();
          }
        };
      } else {
        return new ObjectConstructor<T>() {
          @Override public T construct() {
            return (T) new LinkedTreeMap<String, Object>();
          }
        };
      }
    }

    return null;
  }

  private <T> ObjectConstructor<T> newUnsafeAllocator(final Class<? super T> rawType) {
    if (useJdkUnsafe) {
```

**tool call: Bash**

```bash
grep -rn "EnumMap" gson/src/test | head; ls ~/.m2 2>/dev/null; /work/google__gson-2071/bin/envrun 'ls; ls gson/target 2>/dev/null | head'
```

tool result:

```
CHANGELOG.md
Dockerfile
GsonDesignDocument.md
LICENSE
README.md
ReleaseProcess.md
UserGuide.md
codegen
examples
extras
gson
lib
metrics
pom.xml
proto
target
classes
generated-sources
generated-test-sources
gson-2.9.0-SNAPSHOT.jar
maven-archiver
maven-status
moditect
modules
proguard_map.txt
proguard_seed.txt
```

**assistant:** Let me reproduce with a small program.

**tool call: Bash**

```bash
mkdir -p /tmp/x && cat > gson/Repro.java <<'EOF'
import com.google.gson.*; import com.google.gson.reflect.TypeToken; import java.util.*; import java.lang.reflect.Type;
public class Repro {
  enum MyEnum { VALUE1, VALUE2 }
  public static void main(String[] a) {
    Gson gson = new Gson();
    EnumMap<MyEnum, String> map = new EnumMap<MyEnum, String>(MyEnum.class);
    map.put(MyEnum.VALUE1, "test");
    System.out.println(gson.toJson(map));
    Type type = new TypeToken<EnumMap<MyEnum, String>>() {}.getType();
    EnumMap<?, ?> m = gson.fromJson("{\"VALUE1\":\"test\"}", type);
    System.out.println(m + " " + m.equals(Collections.singletonMap(MyEnum.VALUE1, "test")));
    try { gson.fromJson("{}", EnumMap.class); } catch (Exception e) { System.out.println(e); }
  }
}
EOF
/work/google__gson-2071/bin/envrun 'cd gson && mvn -o -q compile 2>&1 | tail -5; mkdir -p /tmp/r && javac -d /tmp/r -cp target/classes Repro.java && java -cp /tmp/r:target/classes Repro'
```

tool result:

```
Exit code 2
mkdir: /tmp/x: Operation not permitted
error: file not found: Repro.java
Usage: javac <options> <source files>
use --help for a list of possible options
```

**tool call: Bash**

```bash
cat > gson/Repro.java <<'EOF'
import com.google.gson.*; import com.google.gson.reflect.TypeToken; import java.util.*; import java.lang.reflect.Type;
public class Repro {
  enum MyEnum { VALUE1, VALUE2 }
  public static void main(String[] a) {
    Gson gson = new Gson();
    EnumMap<MyEnum, String> map = new EnumMap<MyEnum, String>(MyEnum.class);
    map.put(MyEnum.VALUE1, "test");
    System.out.println(gson.toJson(map));
    Type type = new TypeToken<EnumMap<MyEnum, String>>() {}.getType();
    EnumMap<?, ?> m = gson.fromJson("{\"VALUE1\":\"test\"}", type);
    System.out.println(m + " " + m.equals(Collections.singletonMap(MyEnum.VALUE1, "test")));
    try { gson.fromJson("{}", EnumMap.class); } catch (Exception e) { System.out.println(e); }
  }
}
EOF
/work/google__gson-2071/bin/envrun 'cd gson && mvn -o -q compile 2>&1 | tail -5; mkdir -p /tmp/r && javac -d /tmp/r -cp target/classes Repro.java && java -cp /tmp/r:target/classes Repro'
```

tool result:

```
Exit code 1
Error: LinkageError occurred while loading main class Repro
	java.lang.UnsupportedClassVersionError: Repro has been compiled by a more recent version of the Java Runtime (class file version 61.0), this version of the Java Runtime only recognizes class file versions up to 55.0
```

**tool call: Bash**

```bash
/work/google__gson-2071/bin/envrun 'cd gson && javac --release 8 -d /tmp/r -cp target/classes Repro.java 2>&1 | grep -v warning; java -cp /tmp/r:target/classes Repro'
```

tool result:

```
Exit code 1
{"VALUE1":"test"}
Exception in thread "main" java.lang.ClassCastException: class java.util.LinkedHashMap cannot be cast to class java.util.EnumMap (java.util.LinkedHashMap and java.util.EnumMap are in module java.base of loader 'bootstrap')
	at Repro.main(Repro.java:10)
```

**assistant:** Reproduced. Now the fix, mirroring the existing `EnumSet` handling:

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/google__gson-2071/repo/gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java",
 "old_string": "    if (Map.class.isAssignableFrom(rawType)) {\n      if (ConcurrentNavigableMap.class.isAssignableFrom(rawType)) {",
 "new_string": "    if (Map.class.isAssignableFrom(rawType)) {\n      // Only support creation of EnumMap, but not of custom subtypes; for them type parameters\n      // and constructor parameter might have completely different meaning\n      if (rawType == EnumMap.class) {\n        return new ObjectConstructor<T>() {\n          @SuppressWarnings(\"rawtypes\")\n          @Override public T construct() {\n            if (type instanceof ParameterizedType) {\n              Type elementType = ((ParameterizedType) type).getActualTypeArguments()[0];\n              if (elementType instanceof Class) {\n                return (T) new EnumMap((Class) elementType);\n              } else {\n                throw new JsonIOException(\"Invalid EnumMap type: \" + type.toString());\n              }\n            } else {\n              throw new JsonIOException(\"Invalid EnumMap type: \" + type.toString());\n            }\n          }\n        };\n      } else if (ConcurrentNavigableMap.class.isAssignableFrom(rawType)) {"
}
```

tool result:

```
The file /work/google__gson-2071/repo/gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
cd gson/src/main/java/com/google/gson/internal && sed -i '' 's/^import java.util.EnumSet;/import java.util.EnumMap;\nimport java.util.EnumSet;/' ConstructorConstructor.java && sed -n 20,30p ConstructorConstructor.java
```

tool result:

```
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collection;
import java.util.EnumMap;
import java.util.EnumSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.Map;
```

**tool call: Bash**

```bash
/work/google__gson-2071/bin/envrun 'cd gson && mvn -o -q compile 2>&1 | tail -5; javac --release 8 -d /tmp/r -cp target/classes Repro.java 2>&1 | grep -v warning; java -cp /tmp/r:target/classes Repro'
```

tool result:

```
{"VALUE1":"test"}
{VALUE1=test} true
com.google.gson.JsonIOException: Invalid EnumMap type: class java.util.EnumMap
```

**assistant:** Fixed. Raw `EnumMap` gives a clear `JsonIOException`. Now cleanup and run the related tests.

**tool call: Bash**

```bash
cd /work/google__gson-2071/repo && rm gson/Repro.java && /work/google__gson-2071/bin/envrun 'rm -rf /tmp/r; cd gson && mvn -o -q test -Dtest="MapTest,EnumTest,ConstructorConstructorTest,CollectionTest" 2>&1 | tail -30; git status --short'
```

tool result:

```
 [proguard] ProGuard, version 7.2.0-beta4
 M src/main/java/com/google/gson/internal/ConstructorConstructor.java
?? ../Dockerfile
```

**assistant:** `EnumMap` deserialization now works: the issue's example produces an `EnumMap` equal to `{VALUE1=test}` instead of throwing `ClassCastException`.

**Cause:** `EnumMap` has no no-argument constructor. So Gson used its general `Map` fallback, which builds a `LinkedHashMap`, and the cast to `EnumMap` then failed in the calling code. `EnumSet` already had special handling for this; `EnumMap` didn't.

**Fix:** In `gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java`, I added an `EnumMap` case before the other `Map` cases, copying the existing `EnumSet` handling. It reads the enum key type from the type you ask for (e.g. `TypeToken<EnumMap<MyEnum, String>>`) and creates `new EnumMap(keyClass)`. If the key type isn't available, such as when you pass the raw `EnumMap.class`, it throws `JsonIOException("Invalid EnumMap type: ...")` instead of a confusing cast error.

Two choices worth knowing:
- **Exact class only:** I match `EnumMap` itself, not subclasses, because a subclass's type parameters may mean something different. A subclass with a no-argument constructor still works through Gson's normal path. This differs from the `EnumSet` handling, which matches subclasses too.
- **Key type must be a plain class:** if the key type is a type variable, you get the same `JsonIOException`, as with `EnumSet`.

**Verification:** I reproduced the original error with a small program, then reran it after the change:
- Serialization gives `{"VALUE1":"test"}`.
- Deserialization returns an `EnumMap` equal to the expected map.
- Raw `EnumMap.class` gives the new `JsonIOException`.

`MapTest`, `EnumTest`, `ConstructorConstructorTest` and `CollectionTest` ran with no failures reported. I've deleted the reproduction program, so the only change is `ConstructorConstructor.java`. The untracked `Dockerfile` at the repo root was there before I started, and I left it alone.

_session end: success, turns 11, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.3 s: ls; ls gson/target 2>/dev/null | head
- `rc=2` 8.92 s: cd gson && mvn -o -q compile 2>&1 | tail -5; mkdir -p /tmp/r && javac -d /tmp/r -cp target/classes Repro.java && java -cp /tmp/r:target/classes Repro
- `rc=1` 9.66 s: cd gson && mvn -o -q compile 2>&1 | tail -5; mkdir -p /tmp/r && javac -d /tmp/r -cp target/classes Repro.java && java -cp /tmp/r:target/classes Repro
- `rc=1` 1.89 s: cd gson && javac --release 8 -d /tmp/r -cp target/classes Repro.java 2>&1 | grep -v warning; java -cp /tmp/r:target/classes Repro
- `rc=0` 10.01 s: cd gson && mvn -o -q compile 2>&1 | tail -5; javac --release 8 -d /tmp/r -cp target/classes Repro.java 2>&1 | grep -v warning; java -cp /tmp/r:target/classes Repro
- `rc=0` 17.13 s: rm -rf /tmp/r; cd gson && mvn -o -q test -Dtest="MapTest,EnumTest,ConstructorConstructorTest,CollectionTest" 2>&1 | tail -30; git status --short
