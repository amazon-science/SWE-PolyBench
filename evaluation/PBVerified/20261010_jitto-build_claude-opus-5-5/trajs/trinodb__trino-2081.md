# Instance: trinodb__trino-2081

- Final resolved (evaluator, logs/trinodb__trino-2081_result.json): False
- Run state: DONE
- One attempt. Duration 76.3 s, turns 14, actor cost $0.35595340000000003, container commands 4
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/trinodb__trino-2081/repo
</uploaded_files>
I've uploaded a Java code repository in the directory /work/trinodb__trino-2081/repo. Consider the following issue description:

<issue_description>
Using dot in ScalarFunctions name value cause failures
We are wring a custom functions like `@ScalarFunction(value = "pretradedate", alias = "default.pretradedate")`. When select on `default.pretradedate`, it throws error
```
io.prestosql.spi.PrestoException: line 1:1: Function default.pretradedate not registered

	at io.prestosql.sql.analyzer.ExpressionAnalyzer$Visitor.visitFunctionCall(ExpressionAnalyzer.java:878)
	at io.prestosql.sql.analyzer.ExpressionAnalyzer$Visitor.visitFunctionCall(ExpressionAnalyzer.java:316)
	at io.prestosql.sql.tree.FunctionCall.accept(FunctionCall.java:110)
	at io.prestosql.sql.tree.StackableAstVisitor.process(StackableAstVisitor.java:26)
	at io.prestosql.sql.analyzer.ExpressionAnalyzer$Visitor.process(ExpressionAnalyzer.java:339)
	at io.prestosql.sql.analyzer.ExpressionAnalyzer.analyze(ExpressionAnalyzer.java:276)
	at io.prestosql.sql.ExpressionTestUtils.planExpression(ExpressionTestUtils.java:92)
	at io.prestosql.operator.scalar.FunctionAssertions.createExpression(FunctionAssertions.java:641)
	at io.prestosql.operator.scalar.FunctionAssertions.executeProjectionWithAll(FunctionAssertions.java:480)
	at io.prestosql.operator.scalar.FunctionAssertions.selectUniqueValue(FunctionAssertions.java:295)
	at io.prestosql.operator.scalar.FunctionAssertions.selectSingleValue(FunctionAssertions.java:290)
	at io.prestosql.operator.scalar.FunctionAssertions.assertFunction(FunctionAssertions.java:253)
	at io.prestosql.operator.scalar.AbstractTestFunctions.assertFunction(AbstractTestFunctions.java:91)
	at cn.com.gf.bdp.presto.udf.tradingday.TradeDateFunctionTest.testPretradeDate(TradeDateFunctionTest.java:56)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.testng.internal.MethodInvocationHelper.invokeMethod(MethodInvocationHelper.java:104)
	at org.testng.internal.Invoker.invokeMethod(Invoker.java:645)
	at org.testng.internal.Invoker.invokeTestMethod(Invoker.java:851)
	at org.testng.internal.Invoker.invokeTestMethods(Invoker.java:1177)
	at org.testng.internal.TestMethodWorker.invokeTestMethods(TestMethodWorker.java:129)
	at org.testng.internal.TestMethodWorker.run(TestMethodWorker.java:112)
	at org.testng.TestRunner.privateRun(TestRunner.java:756)
	at org.testng.TestRunner.run(TestRunner.java:610)
	at org.testng.SuiteRunner.runTest(SuiteRunner.java:387)
	at org.testng.SuiteRunner.runSequentially(SuiteRunner.java:382)
	at org.testng.SuiteRunner.privateRun(SuiteRunner.java:340)
	at org.testng.SuiteRunner.run(SuiteRunner.java:289)
	at org.testng.SuiteRunnerWorker.runSuite(SuiteRunnerWorker.java:52)
	at org.testng.SuiteRunnerWorker.run(SuiteRunnerWorker.java:86)
	at org.testng.TestNG.runSuitesSequentially(TestNG.java:1293)
	at org.testng.TestNG.runSuitesLocally(TestNG.java:1218)
	at org.testng.TestNG.runSuites(TestNG.java:1133)
	at org.testng.TestNG.run(TestNG.java:1104)
	at org.testng.IDEARemoteTestNG.run(IDEARemoteTestNG.java:72)
	at org.testng.RemoteTestNGStarter.main(RemoteTestNGStarter.java:123)
Caused by: io.prestosql.spi.PrestoException: Function default.pretradedate not registered
	at io.prestosql.metadata.FunctionRegistry.resolveFunction(FunctionRegistry.java:706)
	at io.prestosql.metadata.MetadataManager.lambda$resolveFunction$19(MetadataManager.java:1312)
	at java.util.Optional.orElseGet(Optional.java:267)
	at io.prestosql.metadata.MetadataManager.resolveFunction(MetadataManager.java:1312)
	at io.prestosql.sql.analyzer.ExpressionAnalyzer$Visitor.visitFunctionCall(ExpressionAnalyzer.java:866)
	... 37 more
```
Presto version: 323

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/trinodb__trino-2081/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/trinodb__trino-2081/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/trinodb__trino-2081/bin/envrun 'git status --short && ls'
Edits you make under /work/trinodb__trino-2081/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/trinodb__trino-2081/repo; grep -rn "QualifiedName\|getSuffix\|\.toString()" presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java | head -30; git log --oneline -1
```

tool result:

```
presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java:168:import io.prestosql.sql.tree.QualifiedName;
presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java:692:    public boolean isAggregationFunction(QualifiedName name)
presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java:699:    ResolvedFunction resolveFunction(QualifiedName name, List<TypeSignatureProvider> parameterTypes)
presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java:776:        throw new PrestoException(AMBIGUOUS_FUNCTION_CALL, errorMessageBuilder.toString());
presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java:1028:            return resolveFunction(QualifiedName.of(mangleOperatorName(operatorType)), fromTypes(argumentTypes));
presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java:1057:    public ResolvedFunction getCoercion(QualifiedName name, Type fromType, Type toType)
presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java:1059:        ResolvedFunction resolvedFunction = resolveCoercion(new Signature(name.getSuffix(), toType.getTypeSignature(), ImmutableList.of(fromType.getTypeSignature())));
presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java:1066:        Collection<FunctionMetadata> allCandidates = functions.get(QualifiedName.of(signature.getName()));
presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java:1136:        private final Multimap<QualifiedName, FunctionMetadata> functionsByName;
presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java:1151:            ImmutableListMultimap.Builder<QualifiedName, FunctionMetadata> functionsByName = ImmutableListMultimap.<QualifiedName, FunctionMetadata>builder()
presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java:1155:                    .forEach(functionMetadata -> functionsByName.put(QualifiedName.of(functionMetadata.getSignature().getName()), functionMetadata));
presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java:1159:            for (Map.Entry<QualifiedName, Collection<FunctionMetadata>> entry : this.functionsByName.asMap().entrySet()) {
presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java:1174:        public Collection<FunctionMetadata> get(QualifiedName name)
presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java:1221:                    .toString();
14a301a6f7 Update constructor visibility in ReferenceAwareExpressionNodeInliner
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2081/repo; sed -n 690,720p presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java; sed -n 1130,1185p presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java; grep -n "of(\|equals\|hashCode\|parts\|originalParts" presto-parser/src/main/java/io/prestosql/sql/tree/QualifiedName.java
```

tool result:

```
    }

    public boolean isAggregationFunction(QualifiedName name)
    {
        return functions.get(name).stream()
                .map(FunctionMetadata::getKind)
                .anyMatch(AGGREGATE::equals);
    }

    ResolvedFunction resolveFunction(QualifiedName name, List<TypeSignatureProvider> parameterTypes)
    {
        Collection<FunctionMetadata> allCandidates = functions.get(name);
        List<FunctionMetadata> exactCandidates = allCandidates.stream()
                .filter(function -> function.getSignature().getTypeVariableConstraints().isEmpty())
                .collect(Collectors.toList());

        Optional<ResolvedFunction> match = matchFunctionExact(exactCandidates, parameterTypes);
        if (match.isPresent()) {
            return match.get();
        }

        List<FunctionMetadata> genericCandidates = allCandidates.stream()
                .filter(function -> !function.getSignature().getTypeVariableConstraints().isEmpty())
                .collect(Collectors.toList());

        match = matchFunctionExact(genericCandidates, parameterTypes);
        if (match.isPresent()) {
            return match.get();
        }

        match = matchFunctionWithCoercion(allCandidates, parameterTypes);
        return boundVariables.isPresent();
    }

    private static class FunctionMap
    {
        private final Map<FunctionId, SqlFunction> functions;
        private final Multimap<QualifiedName, FunctionMetadata> functionsByName;

        public FunctionMap()
        {
            functions = ImmutableMap.of();
            functionsByName = ImmutableListMultimap.of();
        }

        public FunctionMap(FunctionMap map, Collection<? extends SqlFunction> functions)
        {
            this.functions = ImmutableMap.<FunctionId, SqlFunction>builder()
                    .putAll(map.functions)
                    .putAll(Maps.uniqueIndex(functions, function -> function.getFunctionMetadata().getFunctionId()))
                    .build();

            ImmutableListMultimap.Builder<QualifiedName, FunctionMetadata> functionsByName = ImmutableListMultimap.<QualifiedName, FunctionMetadata>builder()
                    .putAll(map.functionsByName);
            functions.stream()
                    .map(SqlFunction::getFunctionMetadata)
                    .forEach(functionMetadata -> functionsByName.put(QualifiedName.of(functionMetadata.getSignature().getName()), functionMetadata));
            this.functionsByName = functionsByName.build();

            // Make sure all functions with the same name are aggregations or none of them are
            for (Map.Entry<QualifiedName, Collection<FunctionMetadata>> entry : this.functionsByName.asMap().entrySet()) {
                Collection<FunctionMetadata> values = entry.getValue();
                long aggregations = values.stream()
                        .map(FunctionMetadata::getKind)
                        .filter(kind -> kind == AGGREGATE)
                        .count();
                checkState(aggregations == 0 || aggregations == values.size(), "'%s' is both an aggregation and a scalar function", entry.getKey());
            }
        }

        public List<FunctionMetadata> list()
        {
            return ImmutableList.copyOf(functionsByName.values());
        }

        public Collection<FunctionMetadata> get(QualifiedName name)
        {
            return functionsByName.get(name);
        }

        public SqlFunction get(FunctionId functionId)
        {
            SqlFunction sqlFunction = functions.get(functionId);
            checkArgument(sqlFunction != null, "Unknown function implementation: " + functionId);
            return sqlFunction;
        }
    }
33:    private final List<String> parts;
34:    private final List<Identifier> originalParts;
36:    public static QualifiedName of(String first, String... rest)
39:        return of(ImmutableList.copyOf(Lists.asList(first, rest).stream().map(Identifier::new).collect(Collectors.toList())));
42:    public static QualifiedName of(String name)
45:        return of(ImmutableList.of(new Identifier(name)));
48:    public static QualifiedName of(Iterable<Identifier> originalParts)
50:        requireNonNull(originalParts, "originalParts is null");
51:        checkArgument(!isEmpty(originalParts), "originalParts is empty");
53:        return new QualifiedName(ImmutableList.copyOf(originalParts));
56:    private QualifiedName(List<Identifier> originalParts)
58:        this.originalParts = originalParts;
59:        this.parts = originalParts.stream().map(identifier -> identifier.getValue().toLowerCase(ENGLISH)).collect(toImmutableList());
64:        return parts;
69:        return originalParts;
75:        return Joiner.on('.').join(parts);
84:        if (parts.size() == 1) {
88:        List<Identifier> subList = originalParts.subList(0, originalParts.size() - 1);
89:        return Optional.of(new QualifiedName(subList));
94:        if (parts.size() < suffix.getParts().size()) {
98:        int start = parts.size() - suffix.getParts().size();
100:        return parts.subList(start, parts.size()).equals(suffix.getParts());
105:        return Iterables.getLast(parts);
109:    public boolean equals(Object o)
117:        return parts.equals(((QualifiedName) o).parts);
121:    public int hashCode()
123:        return parts.hashCode();
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2081/repo; grep -n "QualifiedName.of\|public void test" presto-main/src/test/java/io/prestosql/metadata/TestFunctionRegistry.java | head -30; ls presto-main/target 2>/dev/null | head
```

tool result:

```
61:    public void testIdentityCast()
74:    public void testExactMatchBeforeCoercion()
100:    public void testDuplicateFunctions()
115:    public void testConflictingScalarAggregation()
125:    public void testResolveFunctionByExactMatch()
134:    public void testResolveTypeParametrizedFunction()
143:    public void testResolveFunctionWithCoercion()
155:    public void testAmbiguousCallWithNoCoercion()
166:    public void testAmbiguousCallWithCoercion()
177:    public void testResolveFunctionWithCoercionInTypes()
189:    public void testResolveFunctionWithVariableArity()
207:    public void testResolveFunctionWithVariadicBound()
223:    public void testResolveFunctionForUnknown()
352:            return metadata.resolveFunction(QualifiedName.of(TEST_FUNCTION_NAME), fromTypeSignatures(parameterTypes)).getSignature();
```

**assistant:** Let me write a reproduction test.

**tool call: Bash**

```bash
cd /work/trinodb__trino-2081/repo; grep -n "registerScalar\|protected\|public" presto-main/src/test/java/io/prestosql/operator/scalar/AbstractTestFunctions.java | head -30
```

tool result:

```
48:public abstract class AbstractTestFunctions
50:    protected final Session session;
52:    protected FunctionAssertions functionAssertions;
54:    protected AbstractTestFunctions()
59:    protected AbstractTestFunctions(Session session)
64:    protected AbstractTestFunctions(FeaturesConfig config)
69:    protected AbstractTestFunctions(Session session, FeaturesConfig config)
76:    public final void initTestFunctions()
82:    public final void destroyTestFunctions()
88:    protected void assertFunction(String projection, Type expectedType, Object expected)
93:    protected void assertOperator(OperatorType operator, String value, Type expectedType, Object expected)
98:    protected void assertDecimalFunction(String statement, SqlDecimal expectedResult)
108:    protected void assertInvalidFunction(String projection)
113:    protected void assertInvalidFunction(String projection, ErrorCodeSupplier errorCode, String message)
118:    protected void assertInvalidFunction(String projection, String message)
123:    protected void assertInvalidFunction(String projection, ErrorCodeSupplier expectedErrorCode)
128:    protected void assertNumericOverflow(String projection, String message)
133:    protected void assertInvalidCast(String projection)
138:    protected void assertInvalidCast(String projection, String message)
143:    protected void assertCachedInstanceHasBoundedRetainedSize(String projection)
148:    protected void assertNotSupported(String projection, String message)
155:    protected void tryEvaluateWithAll(String projection, Type expectedType)
160:    protected void registerScalarFunction(SqlScalarFunction sqlScalarFunction)
165:    protected void registerScalar(Class<?> clazz)
172:    protected void registerParametricScalar(Class<?> clazz)
179:    protected void installPlugin(Plugin plugin)
184:    protected static SqlDecimal decimal(String decimalString)
197:    protected static SqlDecimal maxPrecisionDecimal(long value)
205:    protected static <K, V> Map<K, V> asMap(List<K> keyList, List<V> valueList)
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2081/repo; cat > presto-main/src/test/java/io/prestosql/operator/scalar/TestReproDotName.java <<'EOF'
package io.prestosql.operator.scalar;

import io.prestosql.spi.function.ScalarFunction;
import io.prestosql.spi.function.SqlType;
import io.prestosql.spi.type.StandardTypes;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import static io.prestosql.spi.type.BigintType.BIGINT;

public class TestReproDotName
        extends AbstractTestFunctions
{
    @BeforeClass
    public void setUp()
    {
        registerScalar(TestReproDotName.class);
    }

    @ScalarFunction(value = "repro_dot", alias = "default.repro_dot")
    @SqlType(StandardTypes.BIGINT)
    public static long reproDot()
    {
        return 42;
    }

    @Test
    public void test()
    {
        assertFunction("repro_dot()", BIGINT, 42L);
        assertFunction("default.repro_dot()", BIGINT, 42L);
        assertFunction("\"default\".\"repro_dot\"()", BIGINT, 42L);
    }
}
EOF
../bin/envrun 'ls ~/.m2/repository/io/prestosql/presto-main 2>/dev/null; mvn -v | head -1'
```

tool result:

```
Apache Maven 3.9.11 (3e54c93a704957b63ee3494413a2b544fd3d825b)
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2081/repo; ../bin/envrun 'mvn -o -q test -pl presto-main -Dtest=TestReproDotName -DfailIfNoTests=false -Dair.check.skip-all=true 2>&1 | tail -40'
```

tool result:

```
[ERROR] Error executing Maven.
[ERROR] Extension io.takari.aether:takari-local-repository:0.11.2 or one of its dependencies could not be resolved: Plugin io.takari.aether:takari-local-repository:0.11.2 or one of its dependencies could not be resolved:
	Cannot access central (https://repo.maven.apache.org/maven2) in offline mode and the artifact io.takari.aether:takari-local-repository:jar:0.11.2 has not been downloaded from it before.

[ERROR] Caused by: Plugin io.takari.aether:takari-local-repository:0.11.2 or one of its dependencies could not be resolved:
	Cannot access central (https://repo.maven.apache.org/maven2) in offline mode and the artifact io.takari.aether:takari-local-repository:jar:0.11.2 has not been downloaded from it before.
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2081/repo; cat .mvn/extensions.xml; ../bin/envrun 'ls ~/.m2 ~/.m2/repository | head; cat ~/.m2/settings.xml 2>/dev/null; ls presto-main/target 2>/dev/null | head; ls /root/.m2/repository/io/prestosql 2>/dev/null | head'
```

tool result:

```
<?xml version="1.0" encoding="UTF-8"?>
<extensions>
    <extension>
        <groupId>io.takari.aether</groupId>
        <artifactId>takari-local-repository</artifactId>
        <version>0.11.2</version>
    </extension>
</extensions>
ls: cannot access '/root/.m2': No such file or directory
ls: cannot access '/root/.m2/repository': No such file or directory
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2081/repo; ../bin/envrun 'echo $HOME; env | grep -i -E "maven|m2|java"; find / -maxdepth 4 -type d -name repository 2>/dev/null | head; find / -name "guava-*.jar" 2>/dev/null | head -3'
```

tool result:

```
/root
JAVA_HOME=/usr/lib/jvm/java-11-amazon-corretto.x86_64/
M2_HOME=/usr/local/apache-maven-3.9.11
MAVEN_HOME=/usr/local/apache-maven-3.9.11
PATH=/usr/local/apache-maven-3.9.11/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
/usr/local/apache-maven-3.9.11/lib/guava-33.4.8-jre.jar
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2081/repo; ls presto-docs/src/main/sphinx/release | tail -3; grep -n "addFunctions" -A12 presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java | head -30
```

tool result:

```
release-324.rst
release-325.rst
release-326.rst
671:        addFunctions(builder.getFunctions());
672-    }
673-
674:    public final synchronized void addFunctions(List<? extends SqlFunction> functions)
675-    {
676-        for (SqlFunction function : functions) {
677-            FunctionMetadata functionMetadata = function.getFunctionMetadata();
678-            checkArgument(!functionMetadata.getSignature().getName().contains("|"), "Function name can not contain '|' character: %s", functionMetadata.getSignature());
679-            for (FunctionMetadata existingFunction : this.functions.list()) {
680-                checkArgument(!functionMetadata.getFunctionId().equals(existingFunction.getFunctionId()), "Function already registered: %s", functionMetadata.getFunctionId());
681-                checkArgument(!functionMetadata.getSignature().equals(existingFunction.getSignature()), "Function already registered: %s", functionMetadata.getSignature());
682-            }
683-        }
684-        this.functions = new FunctionMap(this.functions, functions);
685-    }
686-
```

**thinking:**

```
Maven isn't usable in this environment, so I'll trace the fix by reading code directly. I found the bug: `FunctionMap` registers functions under a single-part `QualifiedName.of("default.pretradedate")`, but the parser produces a two-part `QualifiedName.of("default", "pretradedate")`, causing lookups to fail—next I'll check how `MetadataManager` calls this.


```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2081/repo; grep -n "public ResolvedFunction resolveFunction" -A20 presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java
```

tool result:

```
1320:    public ResolvedFunction resolveFunction(QualifiedName name, List<TypeSignatureProvider> parameterTypes)
1321-    {
1322-        return ResolvedFunction.fromQualifiedName(name)
1323-                .orElseGet(() -> functions.resolveFunction(name, parameterTypes));
1324-    }
1325-
1326-    @Override
1327-    public ResolvedFunction resolveOperator(OperatorType operatorType, List<? extends Type> argumentTypes)
1328-            throws OperatorNotFoundException
1329-    {
1330-        return functions.resolveOperator(operatorType, argumentTypes);
1331-    }
1332-
1333-    @Override
1334-    public ResolvedFunction getCoercion(OperatorType operatorType, Type fromType, Type toType)
1335-    {
1336-        return functions.getCoercion(operatorType, fromType, toType);
1337-    }
1338-
1339-    @Override
1340-    public ResolvedFunction getCoercion(QualifiedName name, Type fromType, Type toType)
```

**assistant:** Changing `FunctionMap` to index by the normalized dotted name string so both forms resolve the same way:

**tool call: Bash**

```bash
cd /work/trinodb__trino-2081/repo; python3 - <<'EOF'
p='presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java'
s=open(p).read()
reps=[
("""        private final Multimap<QualifiedName, FunctionMetadata> functionsByName;
""","""        // keyed by the lower case, dot separated name, so a function registered with a dot
        // in the name (e.g. "a.b") can be resolved by the equivalent qualified name (a.b)
        private final Multimap<String, FunctionMetadata> functionsByName;
"""),
("""            ImmutableListMultimap.Builder<QualifiedName, FunctionMetadata> functionsByName = ImmutableListMultimap.<QualifiedName, FunctionMetadata>builder()""",
"""            ImmutableListMultimap.Builder<String, FunctionMetadata> functionsByName = ImmutableListMultimap.<String, FunctionMetadata>builder()"""),
("""functionsByName.put(QualifiedName.of(functionMetadata.getSignature().getName()), functionMetadata));""",
"""functionsByName.put(QualifiedName.of(functionMetadata.getSignature().getName()).toString(), functionMetadata));"""),
("""            for (Map.Entry<QualifiedName, Collection<FunctionMetadata>> entry : this.functionsByName.asMap().entrySet()) {""",
"""            for (Map.Entry<String, Collection<FunctionMetadata>> entry : this.functionsByName.asMap().entrySet()) {"""),
("""            return functionsByName.get(name);
""","""            return functionsByName.get(name.toString());
"""),
]
for a,b in reps:
    assert s.count(a)==1,a
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
git diff
```

tool result:

```
diff --git a/presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java b/presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java
index e5ea57abd3..a99cae21b3 100644
--- a/presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java
+++ b/presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java
@@ -1133,7 +1133,9 @@ public class FunctionRegistry
     private static class FunctionMap
     {
         private final Map<FunctionId, SqlFunction> functions;
-        private final Multimap<QualifiedName, FunctionMetadata> functionsByName;
+        // keyed by the lower case, dot separated name, so a function registered with a dot
+        // in the name (e.g. "a.b") can be resolved by the equivalent qualified name (a.b)
+        private final Multimap<String, FunctionMetadata> functionsByName;
 
         public FunctionMap()
         {
@@ -1148,15 +1150,15 @@ public class FunctionRegistry
                     .putAll(Maps.uniqueIndex(functions, function -> function.getFunctionMetadata().getFunctionId()))
                     .build();
 
-            ImmutableListMultimap.Builder<QualifiedName, FunctionMetadata> functionsByName = ImmutableListMultimap.<QualifiedName, FunctionMetadata>builder()
+            ImmutableListMultimap.Builder<String, FunctionMetadata> functionsByName = ImmutableListMultimap.<String, FunctionMetadata>builder()
                     .putAll(map.functionsByName);
             functions.stream()
                     .map(SqlFunction::getFunctionMetadata)
-                    .forEach(functionMetadata -> functionsByName.put(QualifiedName.of(functionMetadata.getSignature().getName()), functionMetadata));
+                    .forEach(functionMetadata -> functionsByName.put(QualifiedName.of(functionMetadata.getSignature().getName()).toString(), functionMetadata));
             this.functionsByName = functionsByName.build();
 
             // Make sure all functions with the same name are aggregations or none of them are
-            for (Map.Entry<QualifiedName, Collection<FunctionMetadata>> entry : this.functionsByName.asMap().entrySet()) {
+            for (Map.Entry<String, Collection<FunctionMetadata>> entry : this.functionsByName.asMap().entrySet()) {
                 Collection<FunctionMetadata> values = entry.getValue();
                 long aggregations = values.stream()
                         .map(FunctionMetadata::getKind)
@@ -1173,7 +1175,7 @@ public class FunctionRegistry
 
         public Collection<FunctionMetadata> get(QualifiedName name)
         {
-            return functionsByName.get(name);
+            return functionsByName.get(name.toString());
         }
 
         public SqlFunction get(FunctionId functionId)
```

**assistant:** Now checking whether anything else rejects qualified (multi-part) function names before or after lookup:

**tool call: Bash**

```bash
cd /work/trinodb__trino-2081/repo; grep -rn "getName().getPrefix()\|getName().getParts().size()\|getName().getSuffix()" presto-main/src/main/java/io/prestosql/sql | head -20
```

tool result:

```
presto-main/src/main/java/io/prestosql/sql/planner/SymbolAllocator.java:117:                    .orElse(functionCall.getName().getSuffix());
presto-main/src/main/java/io/prestosql/sql/analyzer/StatementAnalyzer.java:888:            if (!table.getName().getPrefix().isPresent()) {
presto-main/src/main/java/io/prestosql/sql/analyzer/StatementAnalyzer.java:890:                Optional<WithQuery> withQuery = createScope(scope).getNamedQuery(table.getName().getSuffix());
presto-main/src/main/java/io/prestosql/sql/analyzer/StatementAnalyzer.java:958:                            QualifiedName.of(table.getName().getSuffix()),
presto-main/src/main/java/io/prestosql/sql/analyzer/StatementAnalyzer.java:974:                                QualifiedName.of(table.getName().getSuffix()),
```

**assistant:** Nothing else blocks qualified names. I'll delete the reproduction test, since I couldn't run it.

**tool call: Bash**

```bash
cd /work/trinodb__trino-2081/repo; rm presto-main/src/test/java/io/prestosql/operator/scalar/TestReproDotName.java; git status --short
```

tool result:

```
 M presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java
?? Dockerfile
```

**assistant:** I made the fix, but I couldn't compile or test it. The container has no local Maven repository and no network access, so Maven fails before building anything: it can't even resolve the `takari-local-repository` build extension. The reproduction test I wrote (a scalar function with `alias = "default.repro_dot"`, called as `default.repro_dot()`) never ran, and I've deleted it.

**Cause:** `FunctionRegistry.FunctionMap` stored each function under `QualifiedName.of(signature.getName())`. For the alias `default.pretradedate`, that produces a name with one part, `"default.pretradedate"`. When a query calls `default.pretradedate(...)`, the parser produces a name with two parts, `default` and `pretradedate`. `QualifiedName` compares names part by part, so the lookup in `resolveFunction` never matched and threw "Function … not registered".

**Fix** (only `presto-main/src/main/java/io/prestosql/metadata/FunctionRegistry.java` changed): `FunctionMap` now stores functions under a plain string, the lowercased dot-joined name (`QualifiedName.toString()`). `get(QualifiedName)` looks up `name.toString()`. A function registered as `default.pretradedate` now resolves whether the name arrives as one part or two. The other code that looks functions up by name in this registry goes through the same `get`, so it behaves the same way. That includes `isAggregationFunction`, the coercion lookup and the check that a name isn't both an aggregation and a scalar function.

**Edge cases, by reading the code:**
- Ordinary names without dots resolve exactly as before, because a single part's string is just the lowercased name.
- Matching is still case-insensitive, since both sides are lowercased.
- The error message `'sum' is both an aggregation and a scalar function` is unchanged.
- A quoted single identifier like `"default.pretradedate"()` would now also resolve to this function. That seems acceptable.
- Nothing in the analyzer rejects multi-part function names before or after the lookup.

To confirm, run `TestFunctionRegistry` and the new tests in an environment where Maven can resolve dependencies.

There's an untracked `Dockerfile` at the repository root that was there before I started; I didn't touch it.

_session end: success, turns 14, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 1.01 s: ls ~/.m2/repository/io/prestosql/presto-main 2>/dev/null; mvn -v | head -1
- `rc=0` 2.34 s: mvn -o -q test -pl presto-main -Dtest=TestReproDotName -DfailIfNoTests=false -Dair.check.skip-all=true 2>&1 | tail -40
- `rc=0` 0.34 s: ls ~/.m2 ~/.m2/repository | head; cat ~/.m2/settings.xml 2>/dev/null; ls presto-main/target 2>/dev/null | head; ls /root/.m2/repository/io/prestosql 2>/dev/null | head
- `rc=0` 1.01 s: echo $HOME; env | grep -i -E "maven|m2|java"; find / -maxdepth 4 -type d -name repository 2>/dev/null | head; find / -name "guava-*.jar" 2>/dev/null | head -3
