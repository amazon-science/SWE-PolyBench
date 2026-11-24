# Instance: google__gson-2060

- Final resolved (evaluator, logs/google__gson-2060_result.json): False
- Run state: DONE
- One attempt. Duration 88.8 s, turns 11, actor cost $0.2345844, container commands 5
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/google__gson-2060/repo
</uploaded_files>
I've uploaded a Java code repository in the directory /work/google__gson-2060/repo. Consider the following issue description:

<issue_description>
LazilyParsedNumber being serialised as JsonObject
When I deserialise a JSON object into a map and back into JSON it seems to serialise the `LazilyParsedNumber` as an object.

JSON being parsed:

``` js
{
    "class": "Setting",
    "event": 4,
    "severity": 2,
    "notify": true,
    "sound": false,
    "feeds": [
        {
            "code": "USGS",
            "language": "eng"
        }
    ]
}
```

Class JSON is being parsed into 

``` java
@NoArgsConstructor
@AllArgsConstructor(suppressConstructorProperties = true)
@Accessors(chain = true) @Data
public class MonitoredLocationSetting
{
    @SerializedName("class") private final String className = "Setting";

    protected int event = -1;
    protected Map<String, Object> settings = new HashMap<>();
    protected List<LocationSettingFeed> feeds = new ArrayList<>();
}
```

Basically all im doing is deserialising all fields except "event", "feeds", and "class" into the `settings` map using the following adapters

``` java
builder.registerTypeAdapter(MonitoredLocationSetting.class, new JsonDeserializer<MonitoredLocationSetting>()
{
    @Override public MonitoredLocationSetting deserialize(JsonElement json, Type typeOfT, JsonDeserializationContext context) throws JsonParseException
    {
        MonitoredLocationSetting setting = new Gson().fromJson(json, typeOfT);

        if (setting != null)
        {
            // Ignore for setting.settings
            List<String> fieldsToIgnore = new ArrayList<String>(Arrays.asList(new String[]{"event", "feeds", "class"}));
            Iterator<Map.Entry<String, JsonElement>> entries = json.getAsJsonObject().entrySet().iterator();
            while (entries.hasNext())
            {
                Map.Entry<String, JsonElement> next = entries.next();

                if (!fieldsToIgnore.contains(next.getKey()))
                {
                    if (next.getValue().isJsonPrimitive())
                    {
                        if (next.getValue().getAsJsonPrimitive().isBoolean())
                        {
                            setting.getSettings().put(next.getKey(), next.getValue().getAsBoolean());
                        }
                        else if (next.getValue().getAsJsonPrimitive().isNumber())
                        {
                            // This deserialises as LazilyParsedNumber
                            setting.getSettings().put(next.getKey(), next.getValue().getAsNumber());
                        }
                        else if (next.getValue().getAsJsonPrimitive().isString())
                        {
                            setting.getSettings().put(next.getKey(), next.getValue().getAsString());
                        }
                        else
                        {
                            setting.getSettings().put(next.getKey(), next.getValue());
                        }
                    }
                }
            }
        }

        return setting;
    }
});
builder.registerTypeAdapter(MonitoredLocationSetting.class, new JsonSerializer<MonitoredLocationSetting>()
{
    @Override public JsonElement serialize(MonitoredLocationSetting src, Type typeOfSrc, JsonSerializationContext context)
    {
        JsonObject serialised = (JsonObject)new Gson().toJsonTree(src);
        // After the above line is called the following JSON is produced
        /*
                {
                    "class": "Setting",
                    "event": 4,
                    "feeds": [
                        {
                            "code": "USGS",
                            "language": "eng"
                        }
                    ],
                    "settings": {
                        "notify": true,
                        "severity": {  <-- Issue here
                            "value": "2"
                        },
                        "sound": false
                    }
                }
        */
        JsonObject setting = serialised.get("settings").getAsJsonObject();

        // Ignore for setting.settings
        Iterator<Map.Entry<String, JsonElement>> entries = setting.entrySet().iterator();
        while (entries.hasNext())
        {
            Map.Entry<String, JsonElement> next = entries.next();
            serialised.add(next.getKey(), next.getValue());
        }

        serialised.remove("settings");
        return serialised;
    }
});
```

From what I can see, _technically_ this is correct because as far as Gson is concerned `LazilyParsedNumber` IS an object and not a 'primitive', however, doing a straight convert from and then back to json causes a problem because the object isnt parsed back as a primitive after being read as a primitive (Number)


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/google__gson-2060/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/google__gson-2060/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/google__gson-2060/bin/envrun 'git status --short && ls'
Edits you make under /work/google__gson-2060/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/google__gson-2060/repo; grep -n "NUMBER\|BIG_DECIMAL\|BIG_INTEGER" gson/src/main/java/com/google/gson/Gson.java gson/src/main/java/com/google/gson/internal/bind/TypeAdapters.java | head -40; grep -rn "LazilyParsedNumber" gson/src/test | head
```

tool result:

```
gson/src/main/java/com/google/gson/Gson.java:116:  static final ToNumberStrategy DEFAULT_OBJECT_TO_NUMBER_STRATEGY = ToNumberPolicy.DOUBLE;
gson/src/main/java/com/google/gson/Gson.java:117:  static final ToNumberStrategy DEFAULT_NUMBER_TO_NUMBER_STRATEGY = ToNumberPolicy.LAZILY_PARSED_NUMBER;
gson/src/main/java/com/google/gson/Gson.java:201:        Collections.<TypeAdapterFactory>emptyList(), DEFAULT_OBJECT_TO_NUMBER_STRATEGY, DEFAULT_NUMBER_TO_NUMBER_STRATEGY);
gson/src/main/java/com/google/gson/Gson.java:268:    factories.add(TypeAdapters.newFactory(BigDecimal.class, TypeAdapters.BIG_DECIMAL));
gson/src/main/java/com/google/gson/Gson.java:269:    factories.add(TypeAdapters.newFactory(BigInteger.class, TypeAdapters.BIG_INTEGER));
gson/src/main/java/com/google/gson/internal/bind/TypeAdapters.java:95:        case NUMBER:
gson/src/main/java/com/google/gson/internal/bind/TypeAdapters.java:401:  public static final TypeAdapter<BigDecimal> BIG_DECIMAL = new TypeAdapter<BigDecimal>() {
gson/src/main/java/com/google/gson/internal/bind/TypeAdapters.java:420:  public static final TypeAdapter<BigInteger> BIG_INTEGER = new TypeAdapter<BigInteger>() {
gson/src/main/java/com/google/gson/internal/bind/TypeAdapters.java:689:      case NUMBER:
gson/src/test/java/com/google/gson/internal/LazilyParsedNumberTest.java:27:public class LazilyParsedNumberTest extends TestCase {
gson/src/test/java/com/google/gson/internal/LazilyParsedNumberTest.java:29:    LazilyParsedNumber n1 = new LazilyParsedNumber("1");
gson/src/test/java/com/google/gson/internal/LazilyParsedNumberTest.java:30:    LazilyParsedNumber n1Another = new LazilyParsedNumber("1");
gson/src/test/java/com/google/gson/internal/LazilyParsedNumberTest.java:35:    LazilyParsedNumber n1 = new LazilyParsedNumber("1");
gson/src/test/java/com/google/gson/internal/LazilyParsedNumberTest.java:36:    LazilyParsedNumber n1Another = new LazilyParsedNumber("1");
gson/src/test/java/com/google/gson/internal/LazilyParsedNumberTest.java:43:    objOut.writeObject(new LazilyParsedNumber("123"));
gson/src/test/java/com/google/gson/ToNumberPolicyTest.java:22:import com.google.gson.internal.LazilyParsedNumber;
gson/src/test/java/com/google/gson/ToNumberPolicyTest.java:45:  public void testLazilyParsedNumber() throws IOException {
gson/src/test/java/com/google/gson/ToNumberPolicyTest.java:47:    assertEquals(new LazilyParsedNumber("10.1"), strategy.readNumber(fromString("10.1")));
gson/src/test/java/com/google/gson/ToNumberPolicyTest.java:48:    assertEquals(new LazilyParsedNumber("3.141592653589793238462643383279"), strategy.readNumber(fromString("3.141592653589793238462643383279")));
```

**tool call: Bash**

```bash
cd /work/google__gson-2060/repo; sed -n 395,440p gson/src/main/java/com/google/gson/internal/bind/TypeAdapters.java; sed -n 15,60p gson/src/main/java/com/google/gson/internal/bind/TypeAdapters.java | grep import; sed -n 260,275p gson/src/main/java/com/google/gson/Gson.java; grep -rn "LAZILY_PARSED_NUMBER\b" gson/src/test | grep -v ToNumberPolicy | head
```

tool result:

```
    @Override
    public void write(JsonWriter out, String value) throws IOException {
      out.value(value);
    }
  };

  public static final TypeAdapter<BigDecimal> BIG_DECIMAL = new TypeAdapter<BigDecimal>() {
    @Override public BigDecimal read(JsonReader in) throws IOException {
      if (in.peek() == JsonToken.NULL) {
        in.nextNull();
        return null;
      }
      String s = in.nextString();
      try {
        return new BigDecimal(s);
      } catch (NumberFormatException e) {
        throw new JsonSyntaxException("Failed parsing '" + s + "' as BigDecimal; at path " + in.getPreviousPath(), e);
      }
    }

    @Override public void write(JsonWriter out, BigDecimal value) throws IOException {
      out.value(value);
    }
  };

  public static final TypeAdapter<BigInteger> BIG_INTEGER = new TypeAdapter<BigInteger>() {
    @Override public BigInteger read(JsonReader in) throws IOException {
      if (in.peek() == JsonToken.NULL) {
        in.nextNull();
        return null;
      }
      String s = in.nextString();
      try {
        return new BigInteger(s);
      } catch (NumberFormatException e) {
        throw new JsonSyntaxException("Failed parsing '" + s + "' as BigInteger; at path " + in.getPreviousPath(), e);
      }
    }

    @Override public void write(JsonWriter out, BigInteger value) throws IOException {
      out.value(value);
    }
  };

  public static final TypeAdapterFactory STRING_FACTORY = newFactory(String.class, STRING);

import java.io.IOException;
import java.lang.reflect.AccessibleObject;
import java.lang.reflect.Field;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.net.InetAddress;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;
import java.security.AccessController;
import java.security.PrivilegedAction;
import java.util.ArrayList;
import java.util.BitSet;
import java.util.Calendar;
import java.util.Currency;
import java.util.GregorianCalendar;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.StringTokenizer;
import java.util.UUID;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicIntegerArray;
import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonIOException;
import com.google.gson.JsonNull;
import com.google.gson.JsonObject;
import com.google.gson.JsonPrimitive;
import com.google.gson.JsonSyntaxException;
import com.google.gson.TypeAdapter;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.annotations.SerializedName;
import com.google.gson.internal.LazilyParsedNumber;
import com.google.gson.reflect.TypeToken;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonToken;
import com.google.gson.stream.JsonWriter;
    factories.add(TypeAdapters.ATOMIC_INTEGER_FACTORY);
    factories.add(TypeAdapters.ATOMIC_BOOLEAN_FACTORY);
    factories.add(TypeAdapters.newFactory(AtomicLong.class, atomicLongAdapter(longAdapter)));
    factories.add(TypeAdapters.newFactory(AtomicLongArray.class, atomicLongArrayAdapter(longAdapter)));
    factories.add(TypeAdapters.ATOMIC_INTEGER_ARRAY_FACTORY);
    factories.add(TypeAdapters.CHARACTER_FACTORY);
    factories.add(TypeAdapters.STRING_BUILDER_FACTORY);
    factories.add(TypeAdapters.STRING_BUFFER_FACTORY);
    factories.add(TypeAdapters.newFactory(BigDecimal.class, TypeAdapters.BIG_DECIMAL));
    factories.add(TypeAdapters.newFactory(BigInteger.class, TypeAdapters.BIG_INTEGER));
    factories.add(TypeAdapters.URL_FACTORY);
    factories.add(TypeAdapters.URI_FACTORY);
    factories.add(TypeAdapters.UUID_FACTORY);
    factories.add(TypeAdapters.CURRENCY_FACTORY);
    factories.add(TypeAdapters.LOCALE_FACTORY);
    factories.add(TypeAdapters.INET_ADDRESS_FACTORY);
```

**assistant:** Let me reproduce first.

**tool call: Bash**

```bash
cd /work/google__gson-2060/repo; mkdir -p /tmp/repro 2>/dev/null; cat > Repro.java <<'EOF'
import com.google.gson.*;
import com.google.gson.internal.LazilyParsedNumber;
public class Repro {
  public static void main(String[] a) {
    Gson g = new Gson();
    System.out.println(g.toJson(new LazilyParsedNumber("2")));
    System.out.println(g.fromJson("2.5", LazilyParsedNumber.class));
    java.util.Map<String,Object> m = new java.util.HashMap<>();
    m.put("severity", JsonParser.parseString("2").getAsNumber());
    System.out.println(g.toJson(m));
  }
}
EOF
../bin/envrun 'cd gson && mvn -o -q compile 2>&1 | tail -5; javac -cp target/classes -d /tmp/repro ../Repro.java && java -cp target/classes:/tmp/repro Repro'
```

tool result:

```
Exit code 1
Error: LinkageError occurred while loading main class Repro
	java.lang.UnsupportedClassVersionError: Repro has been compiled by a more recent version of the Java Runtime (class file version 61.0), this version of the Java Runtime only recognizes class file versions up to 55.0
```

**tool call: Bash**

```bash
cd /work/google__gson-2060/repo; ../bin/envrun 'cd gson && javac --release 8 -cp target/classes -d /tmp/repro ../Repro.java && java -cp target/classes:/tmp/repro Repro'
```

tool result:

```
Exit code 1
{"value":"2"}
Exception in thread "main" com.google.gson.JsonSyntaxException: java.lang.IllegalStateException: Expected BEGIN_OBJECT but was NUMBER at line 1 column 1 path $
	at com.google.gson.internal.bind.ReflectiveTypeAdapterFactory$Adapter.read(ReflectiveTypeAdapterFactory.java:225)
	at com.google.gson.Gson.fromJson(Gson.java:988)
	at com.google.gson.Gson.fromJson(Gson.java:953)
	at com.google.gson.Gson.fromJson(Gson.java:902)
	at com.google.gson.Gson.fromJson(Gson.java:873)
	at Repro.main(Repro.java:7)
Caused by: java.lang.IllegalStateException: Expected BEGIN_OBJECT but was NUMBER at line 1 column 1 path $
	at com.google.gson.stream.JsonReader.beginObject(JsonReader.java:385)
	at com.google.gson.internal.bind.ReflectiveTypeAdapterFactory$Adapter.read(ReflectiveTypeAdapterFactory.java:214)
	... 5 more
```

**assistant:** Reproduced. Now add a dedicated `LazilyParsedNumber` adapter and register it.

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/google__gson-2060/repo/gson/src/main/java/com/google/gson/internal/bind/TypeAdapters.java",
 "old_string": "    @Override public void write(JsonWriter out, BigInteger value) throws IOException {\n      out.value(value);\n    }\n  };\n",
 "new_string": "    @Override public void write(JsonWriter out, BigInteger value) throws IOException {\n      out.value(value);\n    }\n  };\n\n  public static final TypeAdapter<LazilyParsedNumber> LAZILY_PARSED_NUMBER = new TypeAdapter<LazilyParsedNumber>() {\n    // Normally users should not be able to access and deserialize LazilyParsedNumber because\n    // it is an internal type, but implement this nonetheless in case there are legit corner\n    // cases where this is possible\n    @Override public LazilyParsedNumber read(JsonReader in) throws IOException {\n      if (in.peek() == JsonToken.NULL) {\n        in.nextNull();\n        return null;\n      }\n      return new LazilyParsedNumber(in.nextString());\n    }\n\n    @Override public void write(JsonWriter out, LazilyParsedNumber value) throws IOException {\n      out.value(value);\n    }\n  };\n"
}
```

tool result:

```
The file /work/google__gson-2060/repo/gson/src/main/java/com/google/gson/internal/bind/TypeAdapters.java has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/google__gson-2060/repo/gson/src/main/java/com/google/gson/Gson.java",
 "old_string": "    factories.add(TypeAdapters.newFactory(BigInteger.class, TypeAdapters.BIG_INTEGER));\n",
 "new_string": "    factories.add(TypeAdapters.newFactory(BigInteger.class, TypeAdapters.BIG_INTEGER));\n    // Add adapter for LazilyParsedNumber because user can obtain it from Gson and then try to serialize it again\n    factories.add(TypeAdapters.newFactory(LazilyParsedNumber.class, TypeAdapters.LAZILY_PARSED_NUMBER));\n"
}
```

tool result:

```
The file /work/google__gson-2060/repo/gson/src/main/java/com/google/gson/Gson.java has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
cd /work/google__gson-2060/repo; grep -n "^import com.google.gson.internal" gson/src/main/java/com/google/gson/Gson.java
```

tool result:

```
38:import com.google.gson.internal.ConstructorConstructor;
39:import com.google.gson.internal.Excluder;
40:import com.google.gson.internal.GsonBuildConfig;
41:import com.google.gson.internal.Primitives;
42:import com.google.gson.internal.Streams;
43:import com.google.gson.internal.bind.ArrayTypeAdapter;
44:import com.google.gson.internal.bind.CollectionTypeAdapterFactory;
45:import com.google.gson.internal.bind.DateTypeAdapter;
46:import com.google.gson.internal.bind.JsonAdapterAnnotationTypeAdapterFactory;
47:import com.google.gson.internal.bind.JsonTreeReader;
48:import com.google.gson.internal.bind.JsonTreeWriter;
49:import com.google.gson.internal.bind.MapTypeAdapterFactory;
50:import com.google.gson.internal.bind.NumberTypeAdapter;
51:import com.google.gson.internal.bind.ObjectTypeAdapter;
52:import com.google.gson.internal.bind.ReflectiveTypeAdapterFactory;
53:import com.google.gson.internal.bind.TypeAdapters;
54:import com.google.gson.internal.sql.SqlTypesSupport;
```

**tool call: Bash**

```bash
cd /work/google__gson-2060/repo; sed -i '' 's/^import com.google.gson.internal.GsonBuildConfig;/&\nimport com.google.gson.internal.LazilyParsedNumber;/' gson/src/main/java/com/google/gson/Gson.java; sed -n 38,43p gson/src/main/java/com/google/gson/Gson.java
../bin/envrun 'cd gson && mvn -o -q compile 2>&1 | tail -5; java -cp target/classes:/tmp/repro Repro'
```

tool result:

```
import com.google.gson.internal.ConstructorConstructor;
import com.google.gson.internal.Excluder;
import com.google.gson.internal.GsonBuildConfig;
import com.google.gson.internal.LazilyParsedNumber;
import com.google.gson.internal.Primitives;
import com.google.gson.internal.Streams;
2
2.5
{"severity":2}
```

**assistant:** Fixed: serializes as `2`, deserializes `2.5`, and the map case gives `{"severity":2}`. Now clean up and run the related tests.

**tool call: Bash**

```bash
cd /work/google__gson-2060/repo; rm Repro.java; ../bin/envrun 'rm -rf /tmp/repro; cd gson && mvn -o -q test -Dtest="PrimitiveTest,DefaultTypeAdaptersTest,ToNumberPolicyTest,LazilyParsedNumberTest,GsonTest,ObjectTest,MapTest,JsonPrimitiveTest" 2>&1 | tail -20'; git status --short
```

tool result:

```
 [proguard] ProGuard, version 7.2.0-beta4

 M gson/src/main/java/com/google/gson/Gson.java
 M gson/src/main/java/com/google/gson/internal/bind/TypeAdapters.java
?? Dockerfile
```

**assistant:** The targeted tests pass. Running the full suite as well:

**tool call: Bash**

```bash
cd /work/google__gson-2060/repo; ../bin/envrun 'cd gson && mvn -o test 2>&1 | grep -E "Tests run:|FAIL|ERROR|BUILD" | tail -5'
```

tool result:

```
[INFO] Tests run: 14, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.003 s - in com.google.gson.JsonObjectTest
[INFO] Tests run: 6, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0 s - in com.google.gson.GsonTest
[INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0 s - in com.google.gson.JsonNullTest
[WARNING] Tests run: 1082, Failures: 0, Errors: 0, Skipped: 1
[INFO] BUILD SUCCESS
```

**assistant:** Gson now writes a `LazilyParsedNumber` as a plain JSON number instead of an object like `{"value":"2"}`, so the round trip in the issue works. The full test suite passes (1082 tests, 0 failures, 1 skipped).

**Cause:** `JsonPrimitive.getAsNumber()` returns a `LazilyParsedNumber`, but Gson had no adapter for that class. It fell through to the reflection-based adapter, which serialized its internal `value` field as an object.

**Fix:**
- `gson/src/main/java/com/google/gson/internal/bind/TypeAdapters.java`: added a `LAZILY_PARSED_NUMBER` adapter. It writes the value with `out.value(Number)`, which outputs the original number text. It reads with `new LazilyParsedNumber(in.nextString())` and handles JSON `null`.
- `gson/src/main/java/com/google/gson/Gson.java`: registered that adapter next to the `BigDecimal` and `BigInteger` adapters, and added the import.

**Before and after (my reproduction):**

| Case | Before | After |
|---|---|---|
| `toJson(new LazilyParsedNumber("2"))` | `{"value":"2"}` | `2` |
| `fromJson("2.5", LazilyParsedNumber.class)` | `JsonSyntaxException` (expected an object) | `2.5` |
| Map holding `getAsNumber()`'s result | `{"severity":{"value":"2"}}` | `{"severity":2}` |

I deleted the reproduction script. There's an untracked `Dockerfile` in the repo root that I didn't create, so I left it alone.

_session end: success, turns 11, is_error False_

## Container commands (task container, no network; broker log)

- `rc=1` 9.45 s: cd gson && mvn -o -q compile 2>&1 | tail -5; javac -cp target/classes -d /tmp/repro ../Repro.java && java -cp target/classes:/tmp/repro Repro
- `rc=1` 1.85 s: cd gson && javac --release 8 -cp target/classes -d /tmp/repro ../Repro.java && java -cp target/classes:/tmp/repro Repro
- `rc=0` 8.26 s: cd gson && mvn -o -q compile 2>&1 | tail -5; java -cp target/classes:/tmp/repro Repro
- `rc=0` 17.28 s: rm -rf /tmp/repro; cd gson && mvn -o -q test -Dtest="PrimitiveTest,DefaultTypeAdaptersTest,ToNumberPolicyTest,LazilyParsedNumberTest,GsonTest,ObjectTest,MapTest,JsonPrimitiveTest" 2>&1 | tail -20
- `rc=0` 18.62 s: cd gson && mvn -o test 2>&1 | grep -E "Tests run:|FAIL|ERROR|BUILD" | tail -5
