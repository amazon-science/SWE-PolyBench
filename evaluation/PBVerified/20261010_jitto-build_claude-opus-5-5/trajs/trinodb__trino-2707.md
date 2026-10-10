# Instance: trinodb__trino-2707

- Final resolved (evaluator, logs/trinodb__trino-2707_result.json): False
- Run state: DONE
- One attempt. Duration 179.2 s, turns 27, actor cost $0.6100290000000002, container commands 5
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/trinodb__trino-2707/repo
</uploaded_files>
I've uploaded a Java code repository in the directory /work/trinodb__trino-2707/repo. Consider the following issue description:

<issue_description>
Fix format for @Description value
Currently, the format of function description is varied as below (The first character uppercase/lowercase and the following period)
- `word_stem`: returns the stem of a word in the given language
- `zip`: Merges the given arrays, element-wise, into a single array of rows. 


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/trinodb__trino-2707/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/trinodb__trino-2707/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/trinodb__trino-2707/bin/envrun 'git status --short && ls'
Edits you make under /work/trinodb__trino-2707/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/trinodb__trino-2707/repo; git log --oneline -2; grep -rn "@Description(" --include=*.java . | grep -v /test/ | wc -l; grep -rln "Description" --include=*.java . | grep /test/ | head -20
```

tool result:

```
2dd60c71da Remove redundant else
e3615c1e5e Compare enums with ==
(eval):1: no matches found: --include=*.java
       0
(eval):1: no matches found: --include=*.java
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; grep -rn '@Description(' --include='*.java' . | grep -v /test/ | wc -l; grep -rn '@Description(' --include='*.java' . | grep /test/ | head; grep -rln 'getDescription' --include='*.java' . | grep /test/ | head
```

tool result:

```
     441
./presto-tests/src/test/java/io/prestosql/execution/TestDeprecatedFunctionWarning.java:189:        @Description(EXPECTED_WARNING_MSG)
./presto-tests/src/test/java/io/prestosql/execution/DeprecatedFunctionsPlugin.java:40:        @Description("Returns TRUE")
./presto-tests/src/test/java/io/prestosql/execution/DeprecatedFunctionsPlugin.java:48:        @Description("Returns TRUE")
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:82:    @Description("Simple exact aggregate description")
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:133:    @Description("Simple exact function which has @AggregationState on different than first positions")
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:173:    @Description("Aggregate with no @AggregationState annotations")
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:211:    @Description("Aggregate with no @AggregationState annotations")
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:263:    @Description("Aggregate with Decomposable=false")
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:317:    @Description("Simple aggregate with two generic implementations")
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:416:    @Description("Simple aggregate with @BlockPosition usage")
./presto-hive/src/test/java/io/prestosql/plugin/hive/metastore/glue/TestGlueInputConverter.java
./presto-hive/src/test/java/io/prestosql/plugin/hive/metastore/glue/TestGlueToPrestoConverter.java
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForScalars.java
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; grep -rhn '@Description(' --include='*.java' . | grep -v /test/ | sed 's/.*@Description(//' | grep -v '^"[A-Z]' | head -50; echo ---; grep -rhn '@Description(' --include='*.java' . | grep '\.")' | wc -l
```

tool result:

```
"suffix starting at given index")
"substring of given length starting at an index")
"mongodb ObjectId")
"mongodb ObjectId from the given string")
EXPECTED_WARNING_MSG)
"varchar length")
"round to given number of decimal places")
"generates a random UUID")
"internal try function for desugaring TRY")
"current date")
"current time with time zone")
"current time without time zone")
"current time zone")
"current timestamp with time zone")
"current timestamp without time zone")
"truncate to the specified precision in the session timezone")
"truncate to the specified precision in the session timezone")
"truncate to the specified precision")
"truncate to the specified precision in the session timezone")
"truncate to the specified precision")
"add the specified amount of date to the given date")
"add the specified amount of time to the given time")
"add the specified amount of time to the given time")
"add the specified amount of time to the given timestamp")
"add the specified amount of time to the given timestamp")
"difference of the given dates in the given unit")
"difference of the given times in the given unit")
"difference of the given times in the given unit")
"difference of the given times in the given unit")
"difference of the given times in the given unit")
"parses the specified date/time by the given format")
"formats the given time by the given format")
"formats the given time by the given format")
"millisecond of the second of the given timestamp")
"millisecond of the second of the given timestamp")
"millisecond of the second of the given time")
"millisecond of the second of the given time")
"millisecond of the second of the given interval")
"second of the minute of the given timestamp")
"second of the minute of the given timestamp")
"second of the minute of the given time")
"second of the minute of the given time")
"second of the minute of the given interval")
"minute of the hour of the given timestamp")
"minute of the hour of the given timestamp")
"minute of the hour of the given time")
"minute of the hour of the given time")
"minute of the hour of the given interval")
"hour of the day of the given timestamp")
"hour of the day of the given timestamp")
---
      22
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; grep -rn 'getDescription()\|Description\b.*startsWith\|isUpperCase' --include='*.java' . | grep /test/ | head -20; grep -rn 'Description' --include='*.java' presto-main/src/main/java/io/prestosql/operator/annotations presto-main/src/main/java/io/prestosql/operator/scalar/annotations 2>/dev/null| head
```

tool result:

```
./presto-hive/src/test/java/io/prestosql/plugin/hive/metastore/glue/TestGlueInputConverter.java:50:        assertEquals(dbInput.getDescription(), testDb.getComment().get());
./presto-hive/src/test/java/io/prestosql/plugin/hive/metastore/glue/TestGlueToPrestoConverter.java:65:        assertEquals(prestoDatabase.getComment().get(), testDatabase.getDescription());
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:113:        assertEquals(aggregation.getFunctionMetadata().getDescription(), "Simple exact aggregate description");
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:306:        assertEquals(aggregation.getFunctionMetadata().getDescription(), "Aggregate with Decomposable=false");
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:383:        assertEquals(aggregation.getFunctionMetadata().getDescription(), "Simple aggregate with two generic implementations");
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:454:        assertEquals(aggregation.getFunctionMetadata().getDescription(), "Simple aggregate with @BlockPosition usage");
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:540:        assertEquals(aggregation.getFunctionMetadata().getDescription(), "Simple implicit specialized aggregate");
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:631:        assertEquals(aggregation.getFunctionMetadata().getDescription(), "Simple explicit specialized aggregate");
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:711:        assertEquals(aggregation1.getFunctionMetadata().getDescription(), "Simple multi output function aggregate specialized description");
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:716:        assertEquals(aggregation2.getFunctionMetadata().getDescription(), "Simple multi output function aggregate generic description");
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:786:        assertEquals(aggregation.getFunctionMetadata().getDescription(), "Simple aggregate with operator injected");
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:866:        assertEquals(aggregation.getFunctionMetadata().getDescription(), "Simple aggregate with type injected");
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:944:        assertEquals(aggregation.getFunctionMetadata().getDescription(), "Simple aggregate with type literal");
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:1018:        assertEquals(aggregation.getFunctionMetadata().getDescription(), "Parametric aggregate with parametric type returned");
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:1093:        assertEquals(aggregation.getFunctionMetadata().getDescription(), "Simple aggregate with fixed parameter type injected");
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForAggregates.java:1158:        assertEquals(aggregation.getFunctionMetadata().getDescription(), "Simple aggregate with fixed parameter type injected");
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForScalars.java:96:        assertEquals(functionMetadata.getDescription(), "Simple scalar with single implementation based on class");
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForScalars.java:182:        assertEquals(functionMetadata.getDescription(), "Simple scalar with nullable primitive");
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForScalars.java:220:        assertEquals(functionMetadata.getDescription(), "Simple scalar with nullable complex type");
./presto-main/src/test/java/io/prestosql/operator/TestAnnotationEngineForScalars.java:256:        assertEquals(functionMetadata.getDescription(), "Simple scalar with single implementation based on method");
presto-main/src/main/java/io/prestosql/operator/annotations/FunctionsParserHelper.java:22:import io.prestosql.spi.function.Description;
presto-main/src/main/java/io/prestosql/operator/annotations/FunctionsParserHelper.java:267:    public static Optional<String> parseDescription(AnnotatedElement base, AnnotatedElement override)
presto-main/src/main/java/io/prestosql/operator/annotations/FunctionsParserHelper.java:269:        Optional<String> overrideDescription = parseDescription(override);
presto-main/src/main/java/io/prestosql/operator/annotations/FunctionsParserHelper.java:270:        if (overrideDescription.isPresent()) {
presto-main/src/main/java/io/prestosql/operator/annotations/FunctionsParserHelper.java:271:            return overrideDescription;
presto-main/src/main/java/io/prestosql/operator/annotations/FunctionsParserHelper.java:274:        return parseDescription(base);
presto-main/src/main/java/io/prestosql/operator/annotations/FunctionsParserHelper.java:277:    public static Optional<String> parseDescription(AnnotatedElement base)
presto-main/src/main/java/io/prestosql/operator/annotations/FunctionsParserHelper.java:279:        Description description = base.getAnnotation(Description.class);
presto-main/src/main/java/io/prestosql/operator/scalar/annotations/ScalarImplementationHeader.java:31:import static io.prestosql.operator.annotations.FunctionsParserHelper.parseDescription;
presto-main/src/main/java/io/prestosql/operator/scalar/annotations/ScalarImplementationHeader.java:76:        Optional<String> description = parseDescription(annotated);
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; grep -n 'EXPECTED_WARNING_MSG\s*=' -A2 presto-tests/src/test/java/io/prestosql/execution/TestDeprecatedFunctionWarning.java; grep -rni 'stem of a word\|single array of rows\|SHOW FUNCTIONS' --include='*.java' . | grep /test/ | head
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; sed -n 1,120p presto-main/src/test/java/io/prestosql/sql/query/TestShowQueries.java
```

tool result:

```
/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package io.prestosql.sql.query;

import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class TestShowQueries
{
    private QueryAssertions assertions;

    @BeforeClass
    public void init()
    {
        assertions = new QueryAssertions();
    }

    @AfterClass(alwaysRun = true)
    public void teardown()
    {
        assertions.close();
        assertions = null;
    }

    @Test
    public void testShowCatalogsLikeWithEscape()
    {
        assertions.assertFails("SHOW CATALOGS LIKE 't$_%' ESCAPE ''", "Escape string must be a single character");
        assertions.assertFails("SHOW CATALOGS LIKE 't$_%' ESCAPE '$$'", "Escape string must be a single character");
        assertions.assertQuery("SHOW CATALOGS LIKE '%$_%' ESCAPE '$'", "VALUES('testing_catalog')");
        assertions.assertQuery("SHOW CATALOGS LIKE '$_%' ESCAPE '$'", "SELECT 'testing_catalog' WHERE FALSE");
    }

    @Test
    public void testShowFunctionLike()
    {
        assertions.assertQuery("SHOW FUNCTIONS LIKE 'split%'",
                "VALUES " +
                        "(cast('split' AS VARCHAR(24)), cast('array(varchar(x))' AS VARCHAR(28)), cast('varchar(x), varchar(y)' AS VARCHAR(62)), cast('scalar' AS VARCHAR(9)), true, cast('' AS VARCHAR(131)))," +
                        "('split', 'array(varchar(x))', 'varchar(x), varchar(y), bigint', 'scalar', true, '')," +
                        "('split_part', 'varchar(x)', 'varchar(x), varchar(y), bigint', 'scalar', true, 'splits a string by a delimiter and returns the specified field (counting from one)')," +
                        "('split_to_map', 'map(varchar,varchar)', 'varchar, varchar, varchar', 'scalar', true, 'creates a map using entryDelimiter and keyValueDelimiter')," +
                        "('split_to_multimap', 'map(varchar,array(varchar))', 'varchar, varchar, varchar', 'scalar', true, 'creates a multimap by splitting a string into key/value pairs')");
    }

    @Test
    public void testShowFunctionsLikeWithEscape()
    {
        assertions.assertQuery("SHOW FUNCTIONS LIKE 'split$_to$_%' ESCAPE '$'",
                "VALUES " +
                        "(cast('split_to_map' AS VARCHAR(24)), cast('map(varchar,varchar)' AS VARCHAR(28)), cast('varchar, varchar, varchar' AS VARCHAR(62)), cast('scalar' AS VARCHAR(9)), true, cast('creates a map using entryDelimiter and keyValueDelimiter' AS VARCHAR(131)))," +
                        "('split_to_multimap', 'map(varchar,array(varchar))', 'varchar, varchar, varchar', 'scalar', true, 'creates a multimap by splitting a string into key/value pairs')");
    }

    @Test
    public void testShowSessionLike()
    {
        assertions.assertQuery(
                "SHOW SESSION LIKE '%page_row_c%'",
                "VALUES ('filter_and_project_min_output_page_row_count', cast('256' as VARCHAR(14)), cast('256' as VARCHAR(14)), 'integer', cast('Experimental: Minimum output page row count for filter and project operators' as VARCHAR(118)))");
    }

    @Test
    public void testShowSessionLikeWithEscape()
    {
        assertions.assertFails("SHOW SESSION LIKE 't$_%' ESCAPE ''", "Escape string must be a single character");
        assertions.assertFails("SHOW SESSION LIKE 't$_%' ESCAPE '$$'", "Escape string must be a single character");
        assertions.assertQuery(
                "SHOW SESSION LIKE '%page$_row$_c%' ESCAPE '$'",
                "VALUES ('filter_and_project_min_output_page_row_count', cast('256' as VARCHAR(14)), cast('256' as VARCHAR(14)), 'integer', cast('Experimental: Minimum output page row count for filter and project operators' as VARCHAR(118)))");
    }

    @Test
    public void testListingEmptyCatalogs()
    {
        assertions.executeExclusively(() -> {
            assertions.getQueryRunner().getAccessControl().denyCatalogs(catalog -> false);
            assertions.assertQueryReturnsEmptyResult("SHOW CATALOGS");
            assertions.getQueryRunner().getAccessControl().reset();
        });
    }
}
```

tool result:

```
55:    private static final String EXPECTED_WARNING_MSG = "(DEPRECATED) Use foo() instead.";
56-
57-    private QueryRunner queryRunner;
./presto-parser/src/test/java/io/prestosql/sql/parser/TestSqlParserErrorHandling.java:142:                {"SHOW FUNCTIONS LIKE '%$_%' ESCAPE",
./presto-parser/src/test/java/io/prestosql/sql/parser/TestStatementBuilder.java:119:        printStatement("show functions");
./presto-parser/src/test/java/io/prestosql/sql/parser/TestSqlParser.java:803:        assertStatement("SHOW FUNCTIONS", new ShowFunctions(Optional.empty(), Optional.empty()));
./presto-parser/src/test/java/io/prestosql/sql/parser/TestSqlParser.java:804:        assertStatement("SHOW FUNCTIONS LIKE '%'", new ShowFunctions(Optional.of("%"), Optional.empty()));
./presto-parser/src/test/java/io/prestosql/sql/parser/TestSqlParser.java:805:        assertStatement("SHOW FUNCTIONS LIKE '%' ESCAPE '$'", new ShowFunctions(Optional.of("%"), Optional.of("$")));
./presto-main/src/test/java/io/prestosql/sql/query/TestShowQueries.java:49:        assertions.assertQuery("SHOW FUNCTIONS LIKE 'split%'",
./presto-main/src/test/java/io/prestosql/sql/query/TestShowQueries.java:61:        assertions.assertQuery("SHOW FUNCTIONS LIKE 'split$_to$_%' ESCAPE '$'",
```

**thinking:**

```
I'll standardize function descriptions to start with an uppercase letter and have no trailing period, matching existing conventions. First, I'll list all descriptions that currently break this pattern.


```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; grep -rn '@Description' --include='*.java' . | grep -v /test/ | grep -v '@Description("[^"]*")' ; echo ---; grep -rn '@Description("[^"]*\.")' --include='*.java' . | grep -v /test/
```

tool result:

```
./presto-geospatial/src/main/java/io/prestosql/plugin/geospatial/GeoFunctions.java:1016:    @Description("Returns a \"simplified\" version of the given geometry")
./presto-geospatial/src/main/java/io/prestosql/plugin/geospatial/BingTileFunctions.java:199:    @Description("Given a (latitude, longitude) point, a radius in kilometers and a zoom level, " +
---
./presto-geospatial/src/main/java/io/prestosql/plugin/geospatial/aggregation/GeometryUnionAgg.java:35:@Description("Returns a geometry that represents the point set union of the input geometries.")
./presto-geospatial/src/main/java/io/prestosql/plugin/geospatial/aggregation/ConvexHullAggregation.java:42:@Description("Returns a geometry that is the convex hull of all the geometries in the set.")
./presto-geospatial/src/main/java/io/prestosql/plugin/geospatial/GeoFunctions.java:363:    @Description("Converts a SphericalGeography object to a Geometry object.")
./presto-geospatial/src/main/java/io/prestosql/plugin/geospatial/GeoFunctions.java:538:    @Description("Returns the reason for why the input geometry is not valid. Returns null if the input is valid.")
./presto-geospatial/src/main/java/io/prestosql/plugin/geospatial/GeoFunctions.java:622:    @Description("Returns a float between 0 and 1 representing the location of the closest point on the LineString to the given Point, as a fraction of total 2d line length.")
./presto-geospatial/src/main/java/io/prestosql/plugin/geospatial/GeoFunctions.java:648:    @Description("Returns a Point interpolated along a LineString at the fraction given.")
./presto-geospatial/src/main/java/io/prestosql/plugin/geospatial/GeoFunctions.java:665:    @Description("Returns an array of Points interpolated along a LineString.")
./presto-geospatial/src/main/java/io/prestosql/plugin/geospatial/GeoFunctions.java:835:    @Description("Returns a geometry that represents the point set union of the input geometries.")
./presto-geospatial/src/main/java/io/prestosql/plugin/geospatial/GeoFunctions.java:843:    @Description("Returns a geometry that represents the point set union of the input geometries.")
./presto-geospatial/src/main/java/io/prestosql/plugin/geospatial/GeoFunctions.java:1697:    @Description("Returns the great-circle distance in meters between two SphericalGeography points.")
./presto-main/src/main/java/io/prestosql/operator/scalar/ArraySortFunction.java:36:@Description("Sorts the given array in ascending order according to the natural ordering of its elements.")
./presto-main/src/main/java/io/prestosql/operator/scalar/ArraySortComparatorFunction.java:38:@Description("Sorts the given array with a lambda comparator.")
./presto-main/src/main/java/io/prestosql/operator/scalar/ArrayShuffleFunction.java:29:@Description("Generates a random permutation of the given array.")
./presto-main/src/main/java/io/prestosql/operator/scalar/Re2JRegexpFunctions.java:119:    @Description("returns the index of the matched substring.")
./presto-main/src/main/java/io/prestosql/operator/scalar/QuantileDigestFunctions.java:42:    @Description("Given an input q between [0, 1], find the value whose rank in the sorted sequence of the n values represented by the qdigest is qn.")
./presto-main/src/main/java/io/prestosql/operator/scalar/QuantileDigestFunctions.java:50:    @Description("Given an input q between [0, 1], find the value whose rank in the sorted sequence of the n values represented by the qdigest is qn.")
./presto-main/src/main/java/io/prestosql/operator/scalar/QuantileDigestFunctions.java:58:    @Description("Given an input q between [0, 1], find the value whose rank in the sorted sequence of the n values represented by the qdigest is qn.")
./presto-main/src/main/java/io/prestosql/operator/scalar/QuantileDigestFunctions.java:66:    @Description("For each input q between [0, 1], find the value whose rank in the sorted sequence of the n values represented by the qdigest is qn.")
./presto-main/src/main/java/io/prestosql/operator/scalar/QuantileDigestFunctions.java:79:    @Description("For each input q between [0, 1], find the value whose rank in the sorted sequence of the n values represented by the qdigest is qn.")
./presto-main/src/main/java/io/prestosql/operator/scalar/QuantileDigestFunctions.java:92:    @Description("For each input q between [0, 1], find the value whose rank in the sorted sequence of the n values represented by the qdigest is qn.")
./presto-main/src/main/java/io/prestosql/operator/scalar/ArrayReverseFunction.java:27:@Description("Returns an array which has the reversed order of the given array.")
./presto-main/src/main/java/io/prestosql/operator/scalar/ArrayExceptFunction.java:26:@Description("Returns an array of elements that are in the first array but not the second, without duplicates.")
```

**assistant:** Now the descriptions that are passed as plain strings in `FunctionMetadata` constructors instead of annotations:

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; grep -n 'public FunctionMetadata(' -A14 presto-main/src/main/java/io/prestosql/metadata/FunctionMetadata.java | head -40; grep -rln 'new FunctionMetadata(' --include='*.java' . | grep -v /test/ | wc -l
```

tool result:

```
34:    public FunctionMetadata(
35-            Signature signature,
36-            boolean nullable,
37-            List<FunctionArgumentDefinition> argumentDefinitions,
38-            boolean hidden,
39-            boolean deterministic,
40-            String description,
41-            FunctionKind kind)
42-    {
43-        this(FunctionId.toFunctionId(signature), signature, nullable, argumentDefinitions, hidden, deterministic, description, kind, false);
44-    }
45-
46:    public FunctionMetadata(
47-            Signature signature,
48-            boolean nullable,
49-            List<FunctionArgumentDefinition> argumentDefinitions,
50-            boolean hidden,
51-            boolean deterministic,
52-            String description,
53-            FunctionKind kind,
54-            boolean deprecated)
55-    {
56-        this(FunctionId.toFunctionId(signature), signature, nullable, argumentDefinitions, hidden, deterministic, description, kind, deprecated);
57-    }
58-
59:    public FunctionMetadata(
60-            FunctionId functionId,
61-            Signature signature,
62-            boolean nullable,
63-            List<FunctionArgumentDefinition> argumentDefinitions,
64-            boolean hidden,
65-            boolean deterministic,
66-            String description,
67-            FunctionKind kind,
68-            boolean deprecated)
69-    {
70-        this.functionId = requireNonNull(functionId, "functionId is null");
71-        this.signature = requireNonNull(signature, "signature is null");
72-        this.nullable = nullable;
73-        this.argumentDefinitions = ImmutableList.copyOf(requireNonNull(argumentDefinitions, "argumentDefinitions is null"));
      52
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; for f in $(grep -rln 'new FunctionMetadata(' --include='*.java' . | grep -v /test/); do grep -nB2 -E '^\s*(FunctionKind\.)?(SCALAR|AGGREGATE|WINDOW)\b' $f | grep -E '"' | sed "s|^|$f:|"; done
```

tool result:

```
./presto-testing/src/main/java/io/prestosql/testing/StatefulSleepingSum.java:63-                "testing not thread safe function",
./presto-main/src/main/java/io/prestosql/metadata/LiteralFunction.java:61-                "literal",
./presto-main/src/main/java/io/prestosql/metadata/SqlOperator.java:55-                "",
./presto-main/src/main/java/io/prestosql/operator/aggregation/MapUnionAggregation.java:75-                        "Aggregate all the maps into a single map",
./presto-main/src/main/java/io/prestosql/operator/aggregation/MapAggregationFunction.java:79-                        "Aggregates all the rows (key/value pairs) into a single map",
./presto-main/src/main/java/io/prestosql/operator/aggregation/ArbitraryAggregationFunction.java:88-                        "return an arbitrary non-null input value",
./presto-main/src/main/java/io/prestosql/operator/aggregation/DecimalAverageAggregation.java:91-                        "Calculates the average value",
./presto-main/src/main/java/io/prestosql/operator/aggregation/DecimalSumAggregation.java:83-                        "Calculates the sum over the input values",
./presto-main/src/main/java/io/prestosql/operator/aggregation/MergeQuantileDigestFunction.java:82-                        "Merges the input quantile digests into a single quantile digest",
./presto-main/src/main/java/io/prestosql/operator/aggregation/ReduceAggregationFunction.java:91-                        "Reduce input elements into a single value",
./presto-main/src/main/java/io/prestosql/operator/aggregation/CountColumn.java:74-                        "Counts the non-null values",
./presto-main/src/main/java/io/prestosql/operator/aggregation/RealAverageAggregation.java:75-                        "Returns the average value of the argument",
./presto-main/src/main/java/io/prestosql/operator/aggregation/arrayagg/ArrayAggregationFunction.java:78-                        "return an array of values",
./presto-main/src/main/java/io/prestosql/operator/aggregation/ParametricAggregation.java:70-                        details.getDescription().orElse(""),
./presto-main/src/main/java/io/prestosql/operator/aggregation/ChecksumAggregationFunction.java:76-                        "Checksum of the given values",
./presto-main/src/main/java/io/prestosql/operator/aggregation/QuantileDigestAggregationFunction.java:92-                        "Returns a qdigest from the set of reals, bigints or doubles",
./presto-main/src/main/java/io/prestosql/operator/aggregation/multimapagg/MultimapAggregationFunction.java:85-                        "Aggregates all the rows (key/value pairs) into a single multimap",
./presto-main/src/main/java/io/prestosql/operator/aggregation/histogram/Histogram.java:79-                        "Count the number of times each value occurs",
./presto-main/src/main/java/io/prestosql/operator/scalar/FormatFunction.java:109-                "formats the input arguments using a format string",
./presto-main/src/main/java/io/prestosql/operator/scalar/ArrayTransformFunction.java:95-                "apply lambda to each element of the array",
./presto-main/src/main/java/io/prestosql/operator/scalar/MapElementAtFunction.java:69-                "Get value for the given key, or null if it does not exist",
./presto-main/src/main/java/io/prestosql/operator/scalar/JsonStringToMapCast.java:52-                "",
./presto-main/src/main/java/io/prestosql/operator/scalar/ArrayConstructor.java:92-                "",
./presto-main/src/main/java/io/prestosql/operator/scalar/ArrayToElementConcatFunction.java:65-                "Concatenates an array to an element",
./presto-main/src/main/java/io/prestosql/operator/scalar/MapZipWithFunction.java:77-                "merge two maps into a single map by applying the lambda function to the pair of values with the same key",
./presto-main/src/main/java/io/prestosql/operator/scalar/JsonStringToArrayCast.java:51-                "",
./presto-main/src/main/java/io/prestosql/operator/scalar/JsonStringToRowCast.java:50-                "",
./presto-main/src/main/java/io/prestosql/operator/scalar/ArrayReduceFunction.java:72-                "Reduce elements of the array into a single value",
./presto-main/src/main/java/io/prestosql/operator/scalar/TryCastFunction.java:59-                "",
./presto-main/src/main/java/io/prestosql/operator/scalar/ArrayFlattenFunction.java:61-                "Flattens the given array",
./presto-main/src/main/java/io/prestosql/operator/scalar/ZipWithFunction.java:75-                "merge two arrays, element-wise, into a single array using the lambda function",
./presto-main/src/main/java/io/prestosql/operator/scalar/ElementToArrayConcatFunction.java:65-                "Concatenates an element to an array",
./presto-main/src/main/java/io/prestosql/operator/scalar/ParametricScalar.java:55-                details.getDescription().orElse(""),
./presto-main/src/main/java/io/prestosql/operator/scalar/MapFilterFunction.java:102-                "return map containing entries that match the given predicate",
./presto-main/src/main/java/io/prestosql/operator/scalar/MapTransformValuesFunction.java:109-                "apply lambda to each entry of the map and transform the value",
./presto-main/src/main/java/io/prestosql/operator/scalar/ApplyFunction.java:67-                "lambda apply function",
./presto-main/src/main/java/io/prestosql/operator/scalar/MapTransformKeysFunction.java:111-                "apply lambda to each entry of the map and transform the key",
./presto-main/src/main/java/io/prestosql/operator/scalar/InvokeFunction.java:61-                "lambda invoke function",
./presto-main/src/main/java/io/prestosql/operator/scalar/ZipFunction.java:88-                "Merges the given arrays, element-wise, into a single array of rows.",
```

**assistant:** The pattern caught 39 of the 52 files. Checking the other 13 by hand:

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; for f in $(grep -rln 'new FunctionMetadata(' --include='*.java' . | grep -v /test/); do if ! grep -qB2 -E '^\s*(FunctionKind\.)?(SCALAR|AGGREGATE|WINDOW)\b' $f; then echo "== $f"; grep -n -A9 'new FunctionMetadata(' $f | grep '"' ; fi; done
```

tool result:

```
== ./presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; for f in $(grep -rln 'new FunctionMetadata(' --include='*.java' . | grep -v /test/); do grep -B2 -E '^\s*(FunctionKind\.)?(SCALAR|AGGREGATE|WINDOW)\b' $f | grep -q '"' || { echo "== $f"; grep -nB2 -E '^\s*(FunctionKind\.)?(SCALAR|AGGREGATE|WINDOW)\b' $f | head -3; }; done
```

tool result:

```
== ./presto-main/src/main/java/io/prestosql/metadata/PolymorphicScalarFunctionBuilder.java
119-                        deterministic,
120-                        description,
121:                        SCALAR),
== ./presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java
== ./presto-main/src/main/java/io/prestosql/operator/aggregation/minmaxby/AbstractMinMaxByNAggregationFunction.java
89-                        true,
90-                        description,
91:                        AGGREGATE),
== ./presto-main/src/main/java/io/prestosql/operator/aggregation/minmaxby/AbstractMinMaxBy.java
106-                        true,
107-                        description,
108:                        AGGREGATE),
== ./presto-main/src/main/java/io/prestosql/operator/aggregation/AbstractMinMaxAggregationFunction.java
96-                        true,
97-                        description,
98:                        AGGREGATE),
== ./presto-main/src/main/java/io/prestosql/operator/aggregation/AbstractMinMaxNAggregationFunction.java
82-                        true,
83-                        description,
84:                        AGGREGATE),
== ./presto-main/src/main/java/io/prestosql/operator/window/SqlWindowFunction.java
43-                true,
44-                nullToEmpty(supplier.getDescription()),
45:                WINDOW,
== ./presto-main/src/main/java/io/prestosql/operator/scalar/AbstractGreatestLeast.java
88-                true,
89-                description,
90:                SCALAR));
== ./presto-main/src/main/java/io/prestosql/operator/scalar/MapConcatFunction.java
74-                true,
75-                DESCRIPTION,
76:                SCALAR));
== ./presto-main/src/main/java/io/prestosql/operator/scalar/ConcatFunction.java
88-                true,
89-                description,
90:                SCALAR));
== ./presto-main/src/main/java/io/prestosql/operator/scalar/MapConstructor.java
89-                true,
90-                DESCRIPTION,
91:                SCALAR));
== ./presto-main/src/main/java/io/prestosql/operator/scalar/ArrayConcatFunction.java
69-                true,
70-                DESCRIPTION,
71:                SCALAR));
== ./presto-main/src/main/java/io/prestosql/operator/scalar/ArrayJoin.java
109-                    true,
110-                    DESCRIPTION,
111:                    SCALAR));
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; grep -rn 'DESCRIPTION = "\|super(.*"' presto-main/src/main/java/io/prestosql/operator/scalar/{MapConcatFunction,MapConstructor,ArrayConcatFunction,ArrayJoin,ConcatFunction}.java; grep -rnE 'super\("[a-z_]+", .*"|^\s*super\(.*"[^"]*"\);' --include='*.java' presto-main/src/main/java/io/prestosql/operator presto-main/src/main/java/io/prestosql/metadata | grep -v /test/ | head -40; grep -rn '\.description("' --include='*.java' . | grep -v /test/
```

tool result:

```
presto-main/src/main/java/io/prestosql/operator/scalar/MapConcatFunction.java:56:    private static final String DESCRIPTION = "Concatenates given maps";
presto-main/src/main/java/io/prestosql/operator/scalar/MapConstructor.java:72:    private static final String DESCRIPTION = "Constructs a map from the given key/value arrays";
presto-main/src/main/java/io/prestosql/operator/scalar/ArrayConcatFunction.java:51:    private static final String DESCRIPTION = "Concatenates given arrays";
presto-main/src/main/java/io/prestosql/operator/scalar/ArrayJoin.java:63:    private static final String DESCRIPTION = "Concatenates the elements of the given array using a delimiter and an optional string to replace nulls";
presto-main/src/main/java/io/prestosql/operator/aggregation/minmaxby/MaxByAggregationFunction.java:23:        super(false, "Returns the value of the first argument, associated with the maximum value of the second argument");
presto-main/src/main/java/io/prestosql/operator/aggregation/minmaxby/MaxByNAggregationFunction.java:25:        super(NAME, t -> t::compareTo, "Returns the values of the first argument associated with the maximum values of the second argument");
presto-main/src/main/java/io/prestosql/operator/aggregation/minmaxby/MinByAggregationFunction.java:23:        super(true, "Returns the value of the first argument, associated with the minimum value of the second argument");
presto-main/src/main/java/io/prestosql/operator/aggregation/MinAggregationFunction.java:25:        super(NAME, true, "Returns the minimum value of the argument");
presto-main/src/main/java/io/prestosql/operator/aggregation/MaxAggregationFunction.java:25:        super(NAME, false, "Returns the maximum value of the argument");
presto-main/src/main/java/io/prestosql/operator/aggregation/MaxNAggregationFunction.java:25:        super(NAME, t -> t::compareTo, "Returns the maximum values of the argument");
presto-main/src/main/java/io/prestosql/operator/scalar/QuarterOfYearDateTimeField.java:37:        super("quarterOfYear");
presto-main/src/main/java/io/prestosql/operator/scalar/QuarterOfYearDateTimeField.java:65:            super("quarters");
presto-main/src/main/java/io/prestosql/operator/scalar/Greatest.java:25:        super("greatest", OperatorType.GREATER_THAN, "get the largest of the given values");
presto-main/src/main/java/io/prestosql/operator/scalar/Least.java:25:        super("least", OperatorType.LESS_THAN, "get the smallest of the given values");
presto-main/src/main/java/io/prestosql/operator/PageTooLargeException.java:25:        super(PAGE_TOO_LARGE, "Remote page is too large");
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; grep -rn 'new ConcatFunction\|ConcatFunction(' --include='*.java' presto-main/src/main | head; grep -rn 'description(' --include='*.java' presto-main/src/main | grep -v 'getDescription\|parseDescription' | head; cat presto-main/src/main/java/io/prestosql/operator/aggregation/MinNAggregationFunction.java | grep super
```

tool result:

```
presto-main/src/main/java/io/prestosql/operator/scalar/ArrayToElementConcatFunction.java:40:    public static final ArrayToElementConcatFunction ARRAY_TO_ELEMENT_CONCAT_FUNCTION = new ArrayToElementConcatFunction();
presto-main/src/main/java/io/prestosql/operator/scalar/ArrayToElementConcatFunction.java:49:    public ArrayToElementConcatFunction()
presto-main/src/main/java/io/prestosql/operator/scalar/MapConcatFunction.java:53:    public static final MapConcatFunction MAP_CONCAT_FUNCTION = new MapConcatFunction();
presto-main/src/main/java/io/prestosql/operator/scalar/MapConcatFunction.java:61:    private MapConcatFunction()
presto-main/src/main/java/io/prestosql/operator/scalar/ConcatFunction.java:71:    public static final ConcatFunction VARCHAR_CONCAT = new ConcatFunction(createUnboundedVarcharType().getTypeSignature(), "concatenates given strings");
presto-main/src/main/java/io/prestosql/operator/scalar/ConcatFunction.java:73:    public static final ConcatFunction VARBINARY_CONCAT = new ConcatFunction(VARBINARY.getTypeSignature(), "concatenates given varbinary values");
presto-main/src/main/java/io/prestosql/operator/scalar/ConcatFunction.java:75:    private ConcatFunction(TypeSignature type, String description)
presto-main/src/main/java/io/prestosql/operator/scalar/ArrayConcatFunction.java:48:    public static final ArrayConcatFunction ARRAY_CONCAT_FUNCTION = new ArrayConcatFunction();
presto-main/src/main/java/io/prestosql/operator/scalar/ArrayConcatFunction.java:56:    private ArrayConcatFunction()
presto-main/src/main/java/io/prestosql/operator/scalar/ElementToArrayConcatFunction.java:40:    public static final ElementToArrayConcatFunction ELEMENT_TO_ARRAY_CONCAT_FUNCTION = new ElementToArrayConcatFunction();
presto-main/src/main/java/io/prestosql/metadata/PolymorphicScalarFunctionBuilder.java:78:    public PolymorphicScalarFunctionBuilder description(String description)
        super(NAME,
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; grep -n super -A4 presto-main/src/main/java/io/prestosql/operator/aggregation/MinNAggregationFunction.java; grep -rn '\.description(' --include='*.java' . | grep -v /test/ | head
```

tool result:

```
25:        super(NAME,
26-                t -> ((leftBlock, leftIndex, rightBlock, rightIndex) -> -t.compareTo(leftBlock, leftIndex, rightBlock, rightIndex)),
27-                "Returns the minimum values of the argument");
28-    }
29-}
./presto-matching/src/main/java/io/prestosql/matching/DefaultPrinter.java:57:        appendLine("capturedAs(%s)", pattern.capture().description());
```

**assistant:** I'll script the annotation changes: capitalize the first character and remove a trailing period in every single-literal `@Description` outside test code.

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; cat > /tmp/fixdesc.py <<'EOF'
import re, subprocess, sys
files = subprocess.check_output(['git', 'ls-files', '*.java']).decode().split()
pat = re.compile(r'@Description\("((?:[^"\\]|\\.)*)"\)')
def fix(m):
    s = m.group(1)
    if s.endswith('.'):
        s = s[:-1]
    if s:
        s = s[0].upper() + s[1:]
    return '@Description("%s")' % s
for f in files:
    if '/src/test/' in f:
        continue
    src = open(f).read()
    new = pat.sub(fix, src)
    if new != src:
        open(f, 'w').write(new)
        print(f)
EOF
python3 /tmp/fixdesc.py | wc -l; git diff -U0 | grep '^+.*@Description' | sed 's/.*@Description("\([^ "]*\).*/\1/' | sort | uniq -c | sort -rn
```

tool result:

```
(eval):1: operation not permitted: /tmp/fixdesc.py
/Library/Developer/CommandLineTools/usr/bin/python3: can't open file '/tmp/fixdesc.py': [Errno 2] No such file or directory
       0
```

**assistant:** The sandbox won't let me write to `/tmp`, so I'll put the script in the repo for now and delete it afterwards.

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; cat > fixdesc.py <<'EOF'
import re, subprocess, sys
files = subprocess.check_output(['git', 'ls-files', '*.java']).decode().split()
pat = re.compile(r'@Description\("((?:[^"\\]|\\.)*)"\)')
def fix(m):
    s = m.group(1)
    if s.endswith('.'):
        s = s[:-1]
    if s:
        s = s[0].upper() + s[1:]
    return '@Description("%s")' % s
for f in files:
    if '/src/test/' in f:
        continue
    src = open(f).read()
    new = pat.sub(fix, src)
    if new != src:
        open(f, 'w').write(new)
        print(f)
EOF
python3 fixdesc.py | wc -l; git diff -U0 | grep '^+.*@Description' | sed 's/.*@Description("\([^ "]*\).*/\1/' | sort | uniq -c | sort -rn
```

tool result:

```
      35
  32 Round
  31 Returns
  10 Decode
  10 Day
   9 Compute
   8 Removes
   8 Converts
   7 Year
   7 Extract
   7 Encode
   7 Current
   7 Absolute
   6 Signum
   6 Remove
   6 Remainder
   5 Truncate
   5 Second
   5 Minute
   5 Millisecond
   5 Hour
   5 Difference
   5 Add
   5 A
   4 Suffix
   4 Substring
   4 Replaces
   4 Pads
   4 Month
   4 Convert
   4 Bitwise
   4 Arc
   3 Week
   3 Test
   3 Quarter
   3 Logarithm
   3 Last
   3 Given
   3 For
   3 Decodes
   3 Count
   3 Construct
   2 Time
   2 String(s)
   2 String
   2 Sorts
   2 Mongodb
   2 Inverse
   2 Hyperbolic
   2 Group(s)
   2 Greedily
   2 Generates
   2 Formats
   2 Creates
   2 Cosine
   2 Computes
   2 Binomial
   1 Value
   1 Unescape
   1 Transforms
   1 The
   1 Textual
   1 Tangent
   1 Square
   1 Splits
   1 Sine
   1 Reverse
   1 Return
   1 Retrieve
   1 Parses
   1 Normal
   1 Natural
   1 Length
   1 Internal
   1 Escape
   1 Encodes
   1 Cube
   1 Constant
   1 Concatenates
   1 An
```

**assistant:** All the new first words look right. Next, the plain-string descriptions found earlier and the one multi-line annotation in `BingTileFunctions`:

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; sed -n 199,201p presto-geospatial/src/main/java/io/prestosql/plugin/geospatial/BingTileFunctions.java
M=presto-main/src/main/java/io/prestosql/operator
sed -i '' \
 -e 's/"testing not thread safe function"/"Testing not thread safe function"/' presto-testing/src/main/java/io/prestosql/testing/StatefulSleepingSum.java
sed -i '' -e 's/^\( *\)"literal",$/\1"Literal",/' presto-main/src/main/java/io/prestosql/metadata/LiteralFunction.java
sed -i '' -e 's/"return an arbitrary non-null input value"/"Return an arbitrary non-null input value"/' $M/aggregation/ArbitraryAggregationFunction.java
sed -i '' -e 's/"return an array of values"/"Return an array of values"/' $M/aggregation/arrayagg/ArrayAggregationFunction.java
sed -i '' -e 's/"formats the input arguments using a format string"/"Formats the input arguments using a format string"/' $M/scalar/FormatFunction.java
sed -i '' -e 's/"apply lambda to each element of the array"/"Apply lambda to each element of the array"/' $M/scalar/ArrayTransformFunction.java
sed -i '' -e 's/"merge two maps into/"Merge two maps into/' $M/scalar/MapZipWithFunction.java
sed -i '' -e 's/"merge two arrays, element-wise/"Merge two arrays, element-wise/' $M/scalar/ZipWithFunction.java
sed -i '' -e 's/"return map containing entries/"Return map containing entries/' $M/scalar/MapFilterFunction.java
sed -i '' -e 's/"apply lambda to each entry of the map and transform the value"/"Apply lambda to each entry of the map and transform the value"/' $M/scalar/MapTransformValuesFunction.java
sed -i '' -e 's/"apply lambda to each entry of the map and transform the key"/"Apply lambda to each entry of the map and transform the key"/' $M/scalar/MapTransformKeysFunction.java
sed -i '' -e 's/"lambda apply function"/"Lambda apply function"/' $M/scalar/ApplyFunction.java
sed -i '' -e 's/"lambda invoke function"/"Lambda invoke function"/' $M/scalar/InvokeFunction.java
sed -i '' -e 's/"Merges the given arrays, element-wise, into a single array of rows\."/"Merges the given arrays, element-wise, into a single array of rows"/' $M/scalar/ZipFunction.java
sed -i '' -e 's/"get the largest of the given values"/"Get the largest of the given values"/' $M/scalar/Greatest.java
sed -i '' -e 's/"get the smallest of the given values"/"Get the smallest of the given values"/' $M/scalar/Least.java
sed -i '' -e 's/"concatenates given strings"/"Concatenates given strings"/' -e 's/"concatenates given varbinary values"/"Concatenates given varbinary values"/' $M/scalar/ConcatFunction.java
grep -n super -A3 $M/aggregation/minmaxby/MinByNAggregationFunction.java
```

tool result:

```
    @Description("Given a (latitude, longitude) point, a radius in kilometers and a zoom level, " +
            "returns a minimum set of Bing tiles at specified zoom level that cover a circle of " +
            "specified radius around the specified point.")
25:        super(NAME,
26-                t -> ((leftBlock, leftIndex, rightBlock, rightIndex) -> -t.compareTo(leftBlock, leftIndex, rightBlock, rightIndex)),
27-                "Returns the values of the first argument associated with the minimum values of the second argument");
28-    }
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; sed -i '' 's/"specified radius around the specified point\.")/"specified radius around the specified point")/' presto-geospatial/src/main/java/io/prestosql/plugin/geospatial/BingTileFunctions.java; rm fixdesc.py; git status --short | wc -l; git diff --stat | tail -1
# verify: remaining violations
grep -rn '@Description("[^"]*")' --include='*.java' . | grep -v /src/test/ | grep -E '@Description\("([^A-Z]|[^"]*\.")' ; echo "annotation check done"
```

tool result:

```
      54
 53 files changed, 335 insertions(+), 335 deletions(-)
annotation check done
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; git status --short | grep -v '^ M'
```

tool result:

```
?? Dockerfile
```

**thinking:**

```
I'll leave the existing Dockerfile untouched. Next, I'll run a temporary test that loads all registered functions and flags any description starting lowercase or ending with a period.


```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; grep -n 'public List<FunctionMetadata> listFunctions\|createTestMetadataManager()' presto-main/src/main/java/io/prestosql/metadata/{MetadataManager,Metadata}.java | head
```

tool result:

```
presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java:207:    public static MetadataManager createTestMetadataManager()
presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java:1329:    public List<FunctionMetadata> listFunctions()
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; cat > presto-main/src/test/java/io/prestosql/metadata/TmpDescriptionCheck.java <<'EOF'
package io.prestosql.metadata;

import org.testng.annotations.Test;

import java.util.List;
import java.util.stream.Collectors;

import static org.testng.Assert.assertEquals;

public class TmpDescriptionCheck
{
    @Test
    public void test()
    {
        List<String> bad = MetadataManager.createTestMetadataManager().listFunctions().stream()
                .filter(f -> !f.getDescription().isEmpty())
                .filter(f -> !Character.isUpperCase(f.getDescription().charAt(0)) || f.getDescription().endsWith("."))
                .map(f -> f.getSignature().getName() + ": " + f.getDescription())
                .collect(Collectors.toList());
        assertEquals(bad, List.of());
    }
}
EOF
/work/trinodb__trino-2707/bin/envrun 'git stash -q -- presto-main/src/main && ./mvnw -o -q -pl presto-main test -Dtest=TmpDescriptionCheck -DfailIfNoTests=false -Dair.check.skip-all=true 2>&1 | grep -E "expected|Tests run|ERROR" | head -5; git stash pop -q && git status --short | wc -l'
```

tool result:

```
55
```

**assistant:** The Maven run printed nothing, so I'll check which Maven setup the container actually has.

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; /work/trinodb__trino-2707/bin/envrun 'which mvn; ls ~/.m2/repository/io/prestosql 2>/dev/null | head -3; git stash -q -- presto-main/src/main && mvn -o -pl presto-main test -Dtest=TmpDescriptionCheck -DfailIfNoTests=false -Dair.check.skip-all=true 2>&1 | grep -E "expected|Tests run|ERROR|BUILD" | head -8; git stash pop -q; git status --short | wc -l'
```

tool result:

```
bash: line 1: which: command not found
[ERROR] Error executing Maven.
[ERROR] Extension io.takari.aether:takari-local-repository:0.11.3 or one of its dependencies could not be resolved: Plugin io.takari.aether:takari-local-repository:0.11.3 or one of its dependencies could not be resolved:
[ERROR] Caused by: Plugin io.takari.aether:takari-local-repository:0.11.3 or one of its dependencies could not be resolved:
55
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; cat .mvn/extensions.xml; /work/trinodb__trino-2707/bin/envrun 'ls ~/.m2 ~/.m2/repository | head; cat ~/.m2/settings.xml 2>/dev/null | head -20; ls ~/.m2/repository/io/ | head -30'
```

tool result:

```
<?xml version="1.0" encoding="UTF-8"?>
<extensions>
    <extension>
        <groupId>io.takari.aether</groupId>
        <artifactId>takari-local-repository</artifactId>
        <version>0.11.3</version>
    </extension>
</extensions>
ls: cannot access '/root/.m2': No such file or directory
ls: cannot access '/root/.m2/repository': No such file or directory
ls: cannot access '/root/.m2/repository/io/': No such file or directory
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; cat Dockerfile | head -40; /work/trinodb__trino-2707/bin/envrun 'echo $HOME; env | grep -i maven; find / -maxdepth 4 -name repository -path "*m2*" 2>/dev/null | head'
```

tool result:

```
FROM polybench_java_base 

WORKDIR /testbed
COPY . ./root
M2_HOME=/usr/local/apache-maven-3.9.11
MAVEN_HOME=/usr/local/apache-maven-3.9.11
PATH=/usr/local/apache-maven-3.9.11/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

**tool call: Bash**

```bash
/work/trinodb__trino-2707/bin/envrun 'find / -name "*.jar" -not -path "/proc/*" 2>/dev/null | grep -v jdk | wc -l; find / -name "guava*.jar" 2>/dev/null | head -2'
```

tool result:

```
105
/usr/local/apache-maven-3.9.11/lib/guava-33.4.8-jre.jar
```

**assistant:** The container has no Maven repository and no network, so the project can't be built or tested here. I'll delete the temporary test and check the changes statically instead.

**tool call: Bash**

```bash
cd /work/trinodb__trino-2707/repo; rm presto-main/src/test/java/io/prestosql/metadata/TmpDescriptionCheck.java
# every changed line must be identical to its original except for first-letter case of a string and a trailing period
paste -d'\n' <(git diff -U0 | grep '^-[^-]' | sed 's/^-//' | tr 'A-Z' 'a-z' | sed 's/\.")/")/; s/\.",$/",/') <(git diff -U0 | grep '^+[^+]' | sed 's/^+//' | tr 'A-Z' 'a-z') | paste - - | awk -F'\t' '$1!=$2' | head
git diff -U0 | grep -c '^-[^-]'; git diff -U0 | grep -c '^+[^+]'; git status --short | grep -v '^ M'
```

tool result:

```
335
335
?? Dockerfile
```

**assistant:** I've changed every function description outside test code to start with an uppercase letter and have no trailing period, but I couldn't build or run any tests to confirm it. The container has no Maven repository and no network, so even an offline build fails. Its first step can't load the Maven extension (`takari-local-repository`) the project requires.

Following the issue's examples, `word_stem` now reads "Returns the stem of a word in the given language" and `zip` reads "Merges the given arrays, element-wise, into a single array of rows". This matches what most descriptions already did, and what current Trino does.

**What changed (53 files, 335 lines):**
- **`@Description` annotations:** I fixed all of them with a short script. That included the multi-line one in `BingTileFunctions.java` and about 20 that ended in a period (in the geospatial functions, `ArraySortFunction`, `QuantileDigestFunctions` and others).
- **Descriptions passed as plain strings:** Some functions set their description in code rather than through the annotation, and those show up in `SHOW FUNCTIONS` too. I fixed the ones that broke the rule:
  - `ZipFunction`, `ZipWithFunction`, `MapZipWithFunction`
  - `ConcatFunction` (both versions), `Greatest`, `Least`
  - `FormatFunction`, `ApplyFunction`, `InvokeFunction`
  - `ArrayTransformFunction`, `MapFilterFunction`, `MapTransformKeysFunction`, `MapTransformValuesFunction`
  - `ArbitraryAggregationFunction`, `ArrayAggregationFunction`
  - `LiteralFunction`, plus the testing class `StatefulSleepingSum`

**How I checked it instead:**
- No description outside test code now starts with a lowercase letter or ends with a period.
- A line-by-line comparison shows every one of the 335 changed lines is identical to the original except for the first letter's case and the removed period. No code logic changed.
- I deleted the temporary script and test; only the fix remains. The untracked `Dockerfile` was already there and I left it alone.

The repository's copy of `TestShowQueries` still expects the old lowercase text for the `split_part`, `split_to_map` and `split_to_multimap` descriptions (e.g. 'splits a string by a delimiter…'). It will fail against this change unless your updated version of the test expects the capitalized wording.

_session end: success, turns 27, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 2.62 s: git stash -q -- presto-main/src/main && ./mvnw -o -q -pl presto-main test -Dtest=TmpDescriptionCheck -DfailIfNoTests=false -Dair.check.skip-all=true 2>&1 | grep -E "expected|Tests run|ERROR" | head -5; git stash pop -q && git status --short | wc -l
- `rc=0` 3.67 s: which mvn; ls ~/.m2/repository/io/prestosql 2>/dev/null | head -3; git stash -q -- presto-main/src/main && mvn -o -pl presto-main test -Dtest=TmpDescriptionCheck -DfailIfNoTests=false -Dair.check.skip-all=true 2>&1 | grep -E "expected|Tests run|ERROR|BUILD" | head -8; git stash pop -q; git status --short | wc -l
- `rc=0` 0.32 s: ls ~/.m2 ~/.m2/repository | head; cat ~/.m2/settings.xml 2>/dev/null | head -20; ls ~/.m2/repository/io/ | head -30
- `rc=0` 0.35 s: echo $HOME; env | grep -i maven; find / -maxdepth 4 -name repository -path "*m2*" 2>/dev/null | head
- `rc=0` 0.84 s: find / -name "*.jar" -not -path "/proc/*" 2>/dev/null | grep -v jdk | wc -l; find / -name "guava*.jar" 2>/dev/null | head -2
