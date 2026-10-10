# Instance: google__gson-2479

- Final resolved (evaluator, logs/google__gson-2479_result.json): True
- Run state: DONE
- One attempt. Duration 95.0 s, turns 12, actor cost $0.28884300000000007, container commands 6
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/google__gson-2479/repo
</uploaded_files>
I've uploaded a Java code repository in the directory /work/google__gson-2479/repo. Consider the following issue description:

<issue_description>
`GsonBuilder` should throw exception when trying to register adapter for `Object` or `JsonElement`
# Problem solved by the feature
`GsonBuilder` does not support overwriting the built-in adapters for `Object` and for `JsonElement` (and subclasses). This might not be obvious to users (see #1177).
https://github.com/google/gson/blob/6d9c3566b71900c54644a9f71ce028696ee5d4bd/gson/src/main/java/com/google/gson/Gson.java#L283-L285

(Side note: This only affects `GsonBuilder`; it is possible to overwrite these adapters when using `@JsonAdapter` on a field.)

# Feature description
- `GsonBuilder.registerTypeAdapter` should throw an exception when the type is `Object` or `JsonElement` or a subclass of it
- `GsonBuilder.registerTypeHierarchyAdapter` should throw an exception when the type is `JsonElement` or a subclass of it

Additionally for both methods the documentation should be extended to specify that overwriting these adapters is not possible (but maybe mention that `@JsonAdapter` can be used instead).

# Alternatives / workarounds
Only adjust the documentation (and Troubleshooting Guide) to mention that these adapters cannot be overwritten.

Or as proposed by #1177 let users overwrite the built-in adapters for these types.


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/google__gson-2479/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/google__gson-2479/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/google__gson-2479/bin/envrun 'git status --short && ls'
Edits you make under /work/google__gson-2479/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

Follow these steps to resolve the issue:
1. As a first step, explore the repo to find and read the code relevant to the <issue_description>.
2. Create a script or a small test to reproduce the error and execute it with envrun, to confirm the error.
3. Edit the source code of the repo to resolve the issue.
4. Rerun your reproduction and confirm that the error is fixed.
5. Think about edge cases and make sure your fix handles them as well; run the existing tests closest to the code you changed.
6. Delete any scripts or files you created only for reproduction or checking, so that only the fix remains in the repository.

```

## Trajectory

_session start: model claude-opus-5-5, tools ['Bash', 'Edit', 'Glob', 'Grep', 'Read', 'Write'], MCP servers []_

**tool call: Bash**

```bash
grep -n "registerTypeAdapter\|registerTypeHierarchyAdapter\|^import" -A0 gson/src/main/java/com/google/gson/GsonBuilder.java
```

tool result:

```
19:import static com.google.gson.Gson.DEFAULT_COMPLEX_MAP_KEYS;
20:import static com.google.gson.Gson.DEFAULT_DATE_PATTERN;
21:import static com.google.gson.Gson.DEFAULT_ESCAPE_HTML;
22:import static com.google.gson.Gson.DEFAULT_FORMATTING_STYLE;
23:import static com.google.gson.Gson.DEFAULT_JSON_NON_EXECUTABLE;
24:import static com.google.gson.Gson.DEFAULT_NUMBER_TO_NUMBER_STRATEGY;
25:import static com.google.gson.Gson.DEFAULT_OBJECT_TO_NUMBER_STRATEGY;
26:import static com.google.gson.Gson.DEFAULT_SERIALIZE_NULLS;
27:import static com.google.gson.Gson.DEFAULT_SPECIALIZE_FLOAT_VALUES;
28:import static com.google.gson.Gson.DEFAULT_STRICTNESS;
29:import static com.google.gson.Gson.DEFAULT_USE_JDK_UNSAFE;
31:import com.google.errorprone.annotations.CanIgnoreReturnValue;
32:import com.google.errorprone.annotations.InlineMe;
33:import com.google.gson.annotations.Since;
34:import com.google.gson.annotations.Until;
35:import com.google.gson.internal.$Gson$Preconditions;
36:import com.google.gson.internal.Excluder;
37:import com.google.gson.internal.bind.DefaultDateTypeAdapter;
38:import com.google.gson.internal.bind.TreeTypeAdapter;
39:import com.google.gson.internal.bind.TypeAdapters;
40:import com.google.gson.internal.sql.SqlTypesSupport;
41:import com.google.gson.reflect.TypeToken;
42:import com.google.gson.stream.JsonReader;
43:import com.google.gson.stream.JsonWriter;
44:import java.lang.reflect.Type;
45:import java.text.DateFormat;
46:import java.util.ArrayDeque;
47:import java.util.ArrayList;
48:import java.util.Collections;
49:import java.util.Date;
50:import java.util.HashMap;
51:import java.util.List;
52:import java.util.Map;
53:import java.util.Objects;
65: *     .registerTypeAdapter(Id.class, new IdTypeAdapter())
669:  public GsonBuilder registerTypeAdapter(Type type, Object typeAdapter) {
703:  public GsonBuilder registerTypeAdapterFactory(TypeAdapterFactory factory) {
724:  public GsonBuilder registerTypeHierarchyAdapter(Class<?> baseType, Object typeAdapter) {
```

**tool call: Bash**

```bash
sed -n 640,745p gson/src/main/java/com/google/gson/GsonBuilder.java; grep -rn "Object.class\|JsonElement" gson/src/test/java/com/google/gson/GsonBuilderTest.java | head -30
```

tool result:

```
    this.dateStyle = dateStyle;
    this.timeStyle = timeStyle;
    this.datePattern = null;
    return this;
  }

  /**
   * Configures Gson for custom serialization or deserialization. This method combines the
   * registration of an {@link TypeAdapter}, {@link InstanceCreator}, {@link JsonSerializer}, and a
   * {@link JsonDeserializer}. It is best used when a single object {@code typeAdapter} implements
   * all the required interfaces for custom serialization with Gson. If a type adapter was
   * previously registered for the specified {@code type}, it is overwritten.
   *
   * <p>This registers the type specified and no other types: you must manually register related
   * types! For example, applications registering {@code boolean.class} should also register {@code
   * Boolean.class}.
   *
   * <p>{@link JsonSerializer} and {@link JsonDeserializer} are made "{@code null}-safe". This
   * means when trying to serialize {@code null}, Gson will write a JSON {@code null} and the
   * serializer is not called. Similarly when deserializing a JSON {@code null}, Gson will emit
   * {@code null} without calling the deserializer. If it is desired to handle {@code null} values,
   * a {@link TypeAdapter} should be used instead.
   *
   * @param type the type definition for the type adapter being registered
   * @param typeAdapter This object must implement at least one of the {@link TypeAdapter},
   * {@link InstanceCreator}, {@link JsonSerializer}, and a {@link JsonDeserializer} interfaces.
   * @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
   */
  @CanIgnoreReturnValue
  public GsonBuilder registerTypeAdapter(Type type, Object typeAdapter) {
    Objects.requireNonNull(type);
    $Gson$Preconditions.checkArgument(typeAdapter instanceof JsonSerializer<?>
        || typeAdapter instanceof JsonDeserializer<?>
        || typeAdapter instanceof InstanceCreator<?>
        || typeAdapter instanceof TypeAdapter<?>);
    if (typeAdapter instanceof InstanceCreator<?>) {
      instanceCreators.put(type, (InstanceCreator<?>) typeAdapter);
    }
    if (typeAdapter instanceof JsonSerializer<?> || typeAdapter instanceof JsonDeserializer<?>) {
      TypeToken<?> typeToken = TypeToken.get(type);
      factories.add(TreeTypeAdapter.newFactoryWithMatchRawType(typeToken, typeAdapter));
    }
    if (typeAdapter instanceof TypeAdapter<?>) {
      @SuppressWarnings({"unchecked", "rawtypes"})
      TypeAdapterFactory factory = TypeAdapters.newFactory(TypeToken.get(type), (TypeAdapter)typeAdapter);
      factories.add(factory);
    }
    return this;
  }

  /**
   * Register a factory for type adapters. Registering a factory is useful when the type
   * adapter needs to be configured based on the type of the field being processed. Gson
   * is designed to handle a large number of factories, so you should consider registering
   * them to be at par with registering an individual type adapter.
   *
   * <p>The created Gson instance might only use the factory once to create an adapter for
   * a specific type and cache the result. It is not guaranteed that the factory will be used
   * again every time the type is serialized or deserialized.
   *
   * @since 2.1
   */
  @CanIgnoreReturnValue
  public GsonBuilder registerTypeAdapterFactory(TypeAdapterFactory factory) {
    Objects.requireNonNull(factory);
    factories.add(factory);
    return this;
  }

  /**
   * Configures Gson for custom serialization or deserialization for an inheritance type hierarchy.
   * This method combines the registration of a {@link TypeAdapter}, {@link JsonSerializer} and
   * a {@link JsonDeserializer}. If a type adapter was previously registered for the specified
   * type hierarchy, it is overridden. If a type adapter is registered for a specific type in
   * the type hierarchy, it will be invoked instead of the one registered for the type hierarchy.
   *
   * @param baseType the class definition for the type adapter being registered for the base class
   *        or interface
   * @param typeAdapter This object must implement at least one of {@link TypeAdapter},
   *        {@link JsonSerializer} or {@link JsonDeserializer} interfaces.
   * @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
   * @since 1.7
   */
  @CanIgnoreReturnValue
  public GsonBuilder registerTypeHierarchyAdapter(Class<?> baseType, Object typeAdapter) {
    Objects.requireNonNull(baseType);
    $Gson$Preconditions.checkArgument(typeAdapter instanceof JsonSerializer<?>
        || typeAdapter instanceof JsonDeserializer<?>
        || typeAdapter instanceof TypeAdapter<?>);
    if (typeAdapter instanceof JsonDeserializer || typeAdapter instanceof JsonSerializer) {
      hierarchyFactories.add(TreeTypeAdapter.newTypeHierarchyFactory(baseType, typeAdapter));
    }
    if (typeAdapter instanceof TypeAdapter<?>) {
      @SuppressWarnings({"unchecked", "rawtypes"})
      TypeAdapterFactory factory = TypeAdapters.newTypeHierarchyFactory(baseType, (TypeAdapter)typeAdapter);
      factories.add(factory);
    }
    return this;
  }

  /**
   * Section 6 of <a href="https://www.ietf.org/rfc/rfc8259.txt">JSON specification</a> disallows
   * special double values (NaN, Infinity, -Infinity). However,
   * <a href="http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-262.pdf">Javascript
   * specification</a> (see section 4.3.20, 4.3.22, 4.3.23) allows these values as valid Javascript
   * values. Moreover, most JavaScript engines will accept these special values in JSON without
gson/src/test/java/com/google/gson/GsonBuilderTest.java:86:      @Override public JsonElement serialize(CustomClass2 src, Type typeOfSrc, JsonSerializationContext context) {
```

**assistant:** Tests aren't in the repo yet. I'll check whether any non-test code registers adapters for these types before adding the checks.

**tool call: Bash**

```bash
grep -rn "registerType\(Hierarchy\)\?Adapter(\(Object\|Json\(Element\|Object\|Array\|Primitive\|Null\)\)\.class" --include=*.java . | grep -v "/test/"; git log --oneline -1
```

tool result:

```
(eval):1: no matches found: --include=*.java
4dfae77a Bump com.github.siom79.japicmp:japicmp-maven-plugin (#2504)
```

**tool call: Bash**

```bash
grep -rnE "registerType(Hierarchy)?Adapter\((Object|Json(Element|Object|Array|Primitive|Null))\.class" --include='*.java' .
```

tool result:

```
./gson/src/test/java/com/google/gson/GsonTest.java:96:        .registerTypeAdapter(Object.class, new TestTypeAdapter())
```

**assistant:** Only one test uses this, and that test will be replaced by the updated tests. Next I'll write a reproduction script:

**tool call: Bash**

```bash
mkdir -p /tmp/x && cat > Repro.java <<'EOF'
import com.google.gson.*;
public class Repro {
  public static void main(String[] a) {
    TypeAdapter<Object> ta = new TypeAdapter<Object>() {
      public void write(com.google.gson.stream.JsonWriter o, Object v) {}
      public Object read(com.google.gson.stream.JsonReader i) { return null; }
    };
    Object[][] cases = {{Object.class, false}, {JsonElement.class, false}, {JsonArray.class, false},
        {JsonElement.class, true}, {JsonPrimitive.class, true}, {Object.class, true}, {String.class, false}};
    for (Object[] c : cases) {
      try {
        if ((Boolean) c[1]) new GsonBuilder().registerTypeHierarchyAdapter((Class<?>) c[0], ta);
        else new GsonBuilder().registerTypeAdapter((Class<?>) c[0], ta);
        System.out.println(c[0] + " hierarchy=" + c[1] + ": no exception");
      } catch (IllegalArgumentException e) {
        System.out.println(c[0] + " hierarchy=" + c[1] + ": " + e.getMessage());
      }
    }
  }
}
EOF
/work/google__gson-2479/bin/envrun 'cd gson && mvn -q -o compile 2>&1 | tail -5; cd .. && javac -cp gson/target/classes -d /tmp/x Repro.java && java -cp gson/target/classes:/tmp/x Repro'
```

tool result:

```
Exit code 2
mkdir: /tmp/x: Operation not permitted
error: file not found: Repro.java
Usage: javac <options> <source files>
use --help for a list of possible options
```

**assistant:** The local `mkdir` in `/tmp` was blocked, so the file never got written. I'll create it in the repo instead and compile it inside the container.

**tool call: Bash**

```bash
cat > Repro.java <<'EOF'
import com.google.gson.*;
public class Repro {
  public static void main(String[] a) {
    TypeAdapter<Object> ta = new TypeAdapter<Object>() {
      public void write(com.google.gson.stream.JsonWriter o, Object v) {}
      public Object read(com.google.gson.stream.JsonReader i) { return null; }
    };
    Object[][] cases = {{Object.class, false}, {JsonElement.class, false}, {JsonArray.class, false},
        {JsonElement.class, true}, {JsonPrimitive.class, true}, {Object.class, true}, {String.class, false}};
    for (Object[] c : cases) {
      try {
        if ((Boolean) c[1]) new GsonBuilder().registerTypeHierarchyAdapter((Class<?>) c[0], ta);
        else new GsonBuilder().registerTypeAdapter((Class<?>) c[0], ta);
        System.out.println(c[0] + " hierarchy=" + c[1] + ": no exception");
      } catch (IllegalArgumentException e) {
        System.out.println(c[0] + " hierarchy=" + c[1] + ": " + e.getMessage());
      }
    }
  }
}
EOF
/work/google__gson-2479/bin/envrun 'cd gson && mvn -q -o compile 2>&1 | tail -5; cd .. && mkdir -p /tmp/x && javac -cp gson/target/classes -d /tmp/x Repro.java && java -cp gson/target/classes:/tmp/x Repro'
```

tool result:

```
Exit code 1
Error: LinkageError occurred while loading main class Repro
	java.lang.UnsupportedClassVersionError: Repro has been compiled by a more recent version of the Java Runtime (class file version 61.0), this version of the Java Runtime only recognizes class file versions up to 55.0
```

**tool call: Bash**

```bash
/work/google__gson-2479/bin/envrun 'mkdir -p /tmp/x && javac --release 8 -cp gson/target/classes -d /tmp/x Repro.java 2>&1 | grep -v warning; java -cp gson/target/classes:/tmp/x Repro'
```

tool result:

```
class java.lang.Object hierarchy=false: no exception
class com.google.gson.JsonElement hierarchy=false: no exception
class com.google.gson.JsonArray hierarchy=false: no exception
class com.google.gson.JsonElement hierarchy=true: no exception
class com.google.gson.JsonPrimitive hierarchy=true: no exception
class java.lang.Object hierarchy=true: no exception
class java.lang.String hierarchy=false: no exception
```

**assistant:** The problem reproduces: none of these calls throw. Now I'll make the fix.

**tool call: Bash**

```bash
python3 - <<'EOF'
p='gson/src/main/java/com/google/gson/GsonBuilder.java'
s=open(p).read()
s=s.replace("""   * a {@link TypeAdapter} should be used instead.
   *
   * @param type the type definition for the type adapter being registered
   * @param typeAdapter This object must implement at least one of the {@link TypeAdapter},
   * {@link InstanceCreator}, {@link JsonSerializer}, and a {@link JsonDeserializer} interfaces.
   * @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
   */
  @CanIgnoreReturnValue
  public GsonBuilder registerTypeAdapter(Type type, Object typeAdapter) {
    Objects.requireNonNull(type);
    $Gson$Preconditions.checkArgument(typeAdapter instanceof JsonSerializer<?>
        || typeAdapter instanceof JsonDeserializer<?>
        || typeAdapter instanceof InstanceCreator<?>
        || typeAdapter instanceof TypeAdapter<?>);
""","""   * a {@link TypeAdapter} should be used instead.
   *
   * <p>Gson already has built-in adapters for {@code Object} and {@link JsonElement} (and its
   * subclasses); they cannot be overwritten with this method. If a custom adapter is needed for
   * one of these types, consider using {@link com.google.gson.annotations.JsonAdapter @JsonAdapter}
   * on the field instead.
   *
   * @param type the type definition for the type adapter being registered
   * @param typeAdapter This object must implement at least one of the {@link TypeAdapter},
   * {@link InstanceCreator}, {@link JsonSerializer}, and a {@link JsonDeserializer} interfaces.
   * @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
   * @throws IllegalArgumentException if the type adapter being registered is for {@code Object}
   * class or {@link JsonElement} or any of its subclasses
   */
  @CanIgnoreReturnValue
  public GsonBuilder registerTypeAdapter(Type type, Object typeAdapter) {
    Objects.requireNonNull(type);
    $Gson$Preconditions.checkArgument(typeAdapter instanceof JsonSerializer<?>
        || typeAdapter instanceof JsonDeserializer<?>
        || typeAdapter instanceof InstanceCreator<?>
        || typeAdapter instanceof TypeAdapter<?>);

    if (isTypeObjectOrJsonElement(type)) {
      throw new IllegalArgumentException("Cannot override built-in adapter for " + type);
    }

""")
s=s.replace("""    return this;
  }

  /**
   * Register a factory for type adapters.""","""    return this;
  }

  private boolean isTypeObjectOrJsonElement(Type type) {
    return type instanceof Class
        && (type == Object.class || JsonElement.class.isAssignableFrom((Class<?>) type));
  }

  /**
   * Register a factory for type adapters.""")
s=s.replace("""   * the type hierarchy, it will be invoked instead of the one registered for the type hierarchy.
   *
   * @param baseType""","""   * the type hierarchy, it will be invoked instead of the one registered for the type hierarchy.
   *
   * <p>Gson already has built-in adapters for {@link JsonElement} and its subclasses; they cannot
   * be overwritten with this method. If a custom adapter is needed for one of these types, consider
   * using {@link com.google.gson.annotations.JsonAdapter @JsonAdapter} on the field instead.
   *
   * @param baseType""")
s=s.replace("""   *        {@link JsonSerializer} or {@link JsonDeserializer} interfaces.
   * @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
   * @since 1.7
   */
  @CanIgnoreReturnValue
  public GsonBuilder registerTypeHierarchyAdapter(Class<?> baseType, Object typeAdapter) {
    Objects.requireNonNull(baseType);
    $Gson$Preconditions.checkArgument(typeAdapter instanceof JsonSerializer<?>
        || typeAdapter instanceof JsonDeserializer<?>
        || typeAdapter instanceof TypeAdapter<?>);
""","""   *        {@link JsonSerializer} or {@link JsonDeserializer} interfaces.
   * @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
   * @throws IllegalArgumentException if the base type is {@link JsonElement} or any of its
   *        subclasses
   * @since 1.7
   */
  @CanIgnoreReturnValue
  public GsonBuilder registerTypeHierarchyAdapter(Class<?> baseType, Object typeAdapter) {
    Objects.requireNonNull(baseType);
    $Gson$Preconditions.checkArgument(typeAdapter instanceof JsonSerializer<?>
        || typeAdapter instanceof JsonDeserializer<?>
        || typeAdapter instanceof TypeAdapter<?>);

    if (JsonElement.class.isAssignableFrom(baseType)) {
      throw new IllegalArgumentException("Cannot override built-in adapter for " + baseType);
    }

""")
open(p,'w').write(s)
EOF
git diff --stat
```

tool result:

```
 .../src/main/java/com/google/gson/GsonBuilder.java | 28 ++++++++++++++++++++++
 1 file changed, 28 insertions(+)
```

**assistant:** I'll make the helper `static`, then rebuild and rerun the reproduction.

**tool call: Bash**

```bash
sed -i '' 's/  private boolean isTypeObjectOrJsonElement/  private static boolean isTypeObjectOrJsonElement/' gson/src/main/java/com/google/gson/GsonBuilder.java
/work/google__gson-2479/bin/envrun 'cd gson && mvn -q -o compile 2>&1 | tail -5; cd .. && java -cp gson/target/classes:/tmp/x Repro'
```

tool result:

```
class java.lang.Object hierarchy=false: Cannot override built-in adapter for class java.lang.Object
class com.google.gson.JsonElement hierarchy=false: Cannot override built-in adapter for class com.google.gson.JsonElement
class com.google.gson.JsonArray hierarchy=false: Cannot override built-in adapter for class com.google.gson.JsonArray
class com.google.gson.JsonElement hierarchy=true: Cannot override built-in adapter for class com.google.gson.JsonElement
class com.google.gson.JsonPrimitive hierarchy=true: Cannot override built-in adapter for class com.google.gson.JsonPrimitive
class java.lang.Object hierarchy=true: no exception
class java.lang.String hierarchy=false: no exception
```

**assistant:** The behaviour now matches the issue. Next I'll run the test suite.

**tool call: Bash**

```bash
rm Repro.java; /work/google__gson-2479/bin/envrun 'cd gson && mvn -o test 2>&1 | grep -E "Tests run:|FAIL|ERROR" | tail -15'
```

tool result:

```
[ERROR] Errors: 
[ERROR]   GsonTest.testClonedTypeAdapterFactoryListsAreIndependent:96 ? IllegalArgument Cannot override built-in adapter for class java.lang.Object
[ERROR] Tests run: 1313, Failures: 0, Errors: 1, Skipped: 19
[INFO] BUILD FAILURE
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:3.1.2:test (default-test) on project gson: 
[ERROR] 
[ERROR] Please refer to /testbed/gson/target/surefire-reports for the individual test results.
[ERROR] Please refer to dump files (if any exist) [date].dump, [date]-jvmRun[N].dump and [date].dumpstream.
[ERROR] -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoFailureException
```

**thinking:**

```
1312 of 1313 tests pass—the only failure is expected, since `GsonTest.testClonedTypeAdapterFactoryListsAreIndependent` registers an adapter for `Object.class`, which now must throw per the issue. I left that test unchanged since you're handling tests yourself.


```

**tool call: Bash**

```bash
/work/google__gson-2479/bin/envrun 'rm -rf /tmp/x; git status --short'; git diff
```

tool result:

```
 M gson/src/main/java/com/google/gson/GsonBuilder.java
?? Dockerfile

diff --git a/gson/src/main/java/com/google/gson/GsonBuilder.java b/gson/src/main/java/com/google/gson/GsonBuilder.java
index 68eb7d71..0202c9bb 100644
--- a/gson/src/main/java/com/google/gson/GsonBuilder.java
+++ b/gson/src/main/java/com/google/gson/GsonBuilder.java
@@ -660,10 +660,17 @@ public final class GsonBuilder {
    * {@code null} without calling the deserializer. If it is desired to handle {@code null} values,
    * a {@link TypeAdapter} should be used instead.
    *
+   * <p>Gson already has built-in adapters for {@code Object} and {@link JsonElement} (and its
+   * subclasses); they cannot be overwritten with this method. If a custom adapter is needed for
+   * one of these types, consider using {@link com.google.gson.annotations.JsonAdapter @JsonAdapter}
+   * on the field instead.
+   *
    * @param type the type definition for the type adapter being registered
    * @param typeAdapter This object must implement at least one of the {@link TypeAdapter},
    * {@link InstanceCreator}, {@link JsonSerializer}, and a {@link JsonDeserializer} interfaces.
    * @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
+   * @throws IllegalArgumentException if the type adapter being registered is for {@code Object}
+   * class or {@link JsonElement} or any of its subclasses
    */
   @CanIgnoreReturnValue
   public GsonBuilder registerTypeAdapter(Type type, Object typeAdapter) {
@@ -672,6 +679,11 @@ public final class GsonBuilder {
         || typeAdapter instanceof JsonDeserializer<?>
         || typeAdapter instanceof InstanceCreator<?>
         || typeAdapter instanceof TypeAdapter<?>);
+
+    if (isTypeObjectOrJsonElement(type)) {
+      throw new IllegalArgumentException("Cannot override built-in adapter for " + type);
+    }
+
     if (typeAdapter instanceof InstanceCreator<?>) {
       instanceCreators.put(type, (InstanceCreator<?>) typeAdapter);
     }
@@ -687,6 +699,11 @@ public final class GsonBuilder {
     return this;
   }
 
+  private static boolean isTypeObjectOrJsonElement(Type type) {
+    return type instanceof Class
+        && (type == Object.class || JsonElement.class.isAssignableFrom((Class<?>) type));
+  }
+
   /**
    * Register a factory for type adapters. Registering a factory is useful when the type
    * adapter needs to be configured based on the type of the field being processed. Gson
@@ -713,11 +730,17 @@ public final class GsonBuilder {
    * type hierarchy, it is overridden. If a type adapter is registered for a specific type in
    * the type hierarchy, it will be invoked instead of the one registered for the type hierarchy.
    *
+   * <p>Gson already has built-in adapters for {@link JsonElement} and its subclasses; they cannot
+   * be overwritten with this method. If a custom adapter is needed for one of these types, consider
+   * using {@link com.google.gson.annotations.JsonAdapter @JsonAdapter} on the field instead.
+   *
    * @param baseType the class definition for the type adapter being registered for the base class
    *        or interface
    * @param typeAdapter This object must implement at least one of {@link TypeAdapter},
    *        {@link JsonSerializer} or {@link JsonDeserializer} interfaces.
    * @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
+   * @throws IllegalArgumentException if the base type is {@link JsonElement} or any of its
+   *        subclasses
    * @since 1.7
    */
   @CanIgnoreReturnValue
@@ -726,6 +749,11 @@ public final class GsonBuilder {
     $Gson$Preconditions.checkArgument(typeAdapter instanceof JsonSerializer<?>
         || typeAdapter instanceof JsonDeserializer<?>
         || typeAdapter instanceof TypeAdapter<?>);
+
+    if (JsonElement.class.isAssignableFrom(baseType)) {
+      throw new IllegalArgumentException("Cannot override built-in adapter for " + baseType);
+    }
+
     if (typeAdapter instanceof JsonDeserializer || typeAdapter instanceof JsonSerializer) {
       hierarchyFactories.add(TreeTypeAdapter.newTypeHierarchyFactory(baseType, typeAdapter));
     }
```

**assistant:** `GsonBuilder` now throws an `IllegalArgumentException` when you try to register an adapter that would override the built-in ones. The change is all in `gson/src/main/java/com/google/gson/GsonBuilder.java`.

**What changed:**
- **`registerTypeAdapter`** throws `"Cannot override built-in adapter for <type>"` when the type is `Object` or `JsonElement` or any subclass (`JsonArray`, `JsonObject`, `JsonPrimitive`, `JsonNull`). A small helper, `isTypeObjectOrJsonElement`, does this check.
- **`registerTypeHierarchyAdapter`** throws the same exception when the base type is `JsonElement` or a subclass. As the issue specifies, a hierarchy adapter for `Object` is still allowed.
- **Javadoc:** both methods now say these adapters can't be overwritten, suggest using `@JsonAdapter` on the field instead, and have an `@throws IllegalArgumentException` entry.

**Verification:**
- Before the fix, a reproduction script showed none of these registrations threw. After it, every disallowed case throws with the expected message, and the allowed ones (`String` with `registerTypeAdapter`, `Object` with `registerTypeHierarchyAdapter`) still go through.
- The full `gson` test suite ran 1313 tests: 1312 passed and 1 failed. The failure is `GsonTest.testClonedTypeAdapterFactoryListsAreIndependent` (`GsonTest.java:96`), which registers an adapter for `Object.class`. That call is now meant to throw, so this failure is expected. I didn't touch the test since you said you're handling test changes; the updated version will need to register some other class.

I deleted the reproduction script and its compiled output. The untracked `Dockerfile` in the repo root was already there and I didn't touch it. I didn't update the Troubleshooting Guide that the issue mentions as an alternative.

_session end: success, turns 12, is_error False_

## Container commands (task container, no network; broker log)

- `rc=2` 5.15 s: cd gson && mvn -q -o compile 2>&1 | tail -5; cd .. && javac -cp gson/target/classes -d /tmp/x Repro.java && java -cp gson/target/classes:/tmp/x Repro
- `rc=1` 5.89 s: cd gson && mvn -q -o compile 2>&1 | tail -5; cd .. && mkdir -p /tmp/x && javac -cp gson/target/classes -d /tmp/x Repro.java && java -cp gson/target/classes:/tmp/x Repro
- `rc=0` 1.73 s: mkdir -p /tmp/x && javac --release 8 -cp gson/target/classes -d /tmp/x Repro.java 2>&1 | grep -v warning; java -cp gson/target/classes:/tmp/x Repro
- `rc=0` 14.43 s: cd gson && mvn -q -o compile 2>&1 | tail -5; cd .. && java -cp gson/target/classes:/tmp/x Repro
- `rc=0` 11.48 s: cd gson && mvn -o test 2>&1 | grep -E "Tests run:|FAIL|ERROR" | tail -15
- `rc=0` 0.42 s: rm -rf /tmp/x; git status --short
