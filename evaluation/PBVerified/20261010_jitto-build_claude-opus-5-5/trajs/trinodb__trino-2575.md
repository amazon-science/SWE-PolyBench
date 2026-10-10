# Instance: trinodb__trino-2575

- Final resolved (evaluator, logs/trinodb__trino-2575_result.json): True
- Run state: DONE
- One attempt. Duration 147.9 s, turns 17, actor cost $0.49810099999999996, container commands 5
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/trinodb__trino-2575/repo
</uploaded_files>
I've uploaded a Java code repository in the directory /work/trinodb__trino-2575/repo. Consider the following issue description:

<issue_description>
Error when querying information schema with empty table_name predicate
```
select * from "hive"."information_schema"."tables" WHERE table_schema='tpch' AND table_name=''
```

Is causing:
```
java.lang.IllegalArgumentException: tableName is empty
	at io.prestosql.spi.connector.SchemaUtil.checkNotEmpty(SchemaUtil.java:28)
	at io.prestosql.spi.connector.SchemaTableName.<init>(SchemaTableName.java:33)
	at io.prestosql.metadata.QualifiedObjectName.asSchemaTableName(QualifiedObjectName.java:75)
	at io.prestosql.metadata.CatalogMetadata.getConnectorId(CatalogMetadata.java:115)
	at io.prestosql.metadata.MetadataManager.getTableHandle(MetadataManager.java:285)
	at io.prestosql.metadata.MetadataManager.listTables(MetadataManager.java:507)
	at io.prestosql.metadata.MetadataListing.listTables(MetadataListing.java:64)
	at io.prestosql.connector.informationschema.InformationSchemaPageSource.addTablesRecords(InformationSchemaPageSource.java:268)
	at io.prestosql.connector.informationschema.InformationSchemaPageSource.buildPages(InformationSchemaPageSource.java:210)
	at io.prestosql.connector.informationschema.InformationSchemaPageSource.getNextPage(InformationSchemaPageSource.java:173)
	at io.prestosql.operator.ScanFilterAndProjectOperator$ConnectorPageSourceToPages.process(ScanFilterAndProjectOperator.java:362)
	at io.prestosql.operator.WorkProcessorUtils$ProcessWorkProcessor.process(WorkProcessorUtils.java:372)
	at io.prestosql.operator.WorkProcessorUtils.getNextState(WorkProcessorUtils.java:221)
	at io.prestosql.operator.WorkProcessorUtils.access$000(WorkProcessorUtils.java:37)
	at io.prestosql.operator.WorkProcessorUtils$YieldingProcess.process(WorkProcessorUtils.java:181)
	at io.prestosql.operator.WorkProcessorUtils$ProcessWorkProcessor.process(WorkProcessorUtils.java:372)
	at io.prestosql.operator.WorkProcessorUtils$3.process(WorkProcessorUtils.java:306)
	at io.prestosql.operator.WorkProcessorUtils$ProcessWorkProcessor.process(WorkProcessorUtils.java:372)
	at io.prestosql.operator.WorkProcessorUtils$3.process(WorkProcessorUtils.java:306)
	at io.prestosql.operator.WorkProcessorUtils$ProcessWorkProcessor.process(WorkProcessorUtils.java:372)
	at io.prestosql.operator.WorkProcessorUtils$3.process(WorkProcessorUtils.java:306)
	at io.prestosql.operator.WorkProcessorUtils$ProcessWorkProcessor.process(WorkProcessorUtils.java:372)
	at io.prestosql.operator.WorkProcessorUtils.getNextState(WorkProcessorUtils.java:221)
	at io.prestosql.operator.WorkProcessorUtils.lambda$processStateMonitor$2(WorkProcessorUtils.java:200)
	at io.prestosql.operator.WorkProcessorUtils$ProcessWorkProcessor.process(WorkProcessorUtils.java:372)
	at io.prestosql.operator.WorkProcessorUtils.lambda$flatten$6(WorkProcessorUtils.java:277)
	at io.prestosql.operator.WorkProcessorUtils$3.process(WorkProcessorUtils.java:319)
	at io.prestosql.operator.WorkProcessorUtils$ProcessWorkProcessor.process(WorkProcessorUtils.java:372)
	at io.prestosql.operator.WorkProcessorUtils$3.process(WorkProcessorUtils.java:306)
	at io.prestosql.operator.WorkProcessorUtils$ProcessWorkProcessor.process(WorkProcessorUtils.java:372)
	at io.prestosql.operator.WorkProcessorUtils.getNextState(WorkProcessorUtils.java:221)
	at io.prestosql.operator.WorkProcessorUtils.lambda$processStateMonitor$2(WorkProcessorUtils.java:200)
	at io.prestosql.operator.WorkProcessorUtils$ProcessWorkProcessor.process(WorkProcessorUtils.java:372)
	at io.prestosql.operator.WorkProcessorUtils.getNextState(WorkProcessorUtils.java:221)
	at io.prestosql.operator.WorkProcessorUtils.lambda$finishWhen$3(WorkProcessorUtils.java:215)
	at io.prestosql.operator.WorkProcessorUtils$ProcessWorkProcessor.process(WorkProcessorUtils.java:372)
	at io.prestosql.operator.WorkProcessorSourceOperatorAdapter.getOutput(WorkProcessorSourceOperatorAdapter.java:148)
	at io.prestosql.operator.Driver.processInternal(Driver.java:379)
	at io.prestosql.operator.Driver.lambda$processFor$8(Driver.java:283)
	at io.prestosql.operator.Driver.tryWithLock(Driver.java:675)
	at io.prestosql.operator.Driver.processFor(Driver.java:276)
	at io.prestosql.execution.SqlTaskExecution$DriverSplitRunner.processFor(SqlTaskExecution.java:1075)
	at io.prestosql.execution.executor.PrioritizedSplitRunner.process(PrioritizedSplitRunner.java:163)
	at io.prestosql.execution.executor.TaskExecutor$TaskRunner.run(TaskExecutor.java:484)
	at io.prestosql.$gen.Presto_null__testversion____20200116_131217_4.run(Unknown Source)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
	at java.lang.Thread.run(Thread.java:748)
```

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/trinodb__trino-2575/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/trinodb__trino-2575/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/trinodb__trino-2575/bin/envrun 'git status --short && ls'
Edits you make under /work/trinodb__trino-2575/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/trinodb__trino-2575/repo; sed -n 480,530p presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java; sed -n 30,110p presto-main/src/main/java/io/prestosql/metadata/MetadataListing.java
```

tool result:

```
        ConnectorMetadata metadata = getMetadata(session, catalogName);
        ConnectorTableMetadata tableMetadata = metadata.getTableMetadata(session.toConnectorSession(catalogName), tableHandle.getConnectorHandle());
        if (tableMetadata.getColumns().isEmpty()) {
            throw new PrestoException(NOT_SUPPORTED, "Table has no columns: " + tableHandle);
        }

        return new TableMetadata(catalogName, tableMetadata);
    }

    @Override
    public TableStatistics getTableStatistics(Session session, TableHandle tableHandle, Constraint constraint)
    {
        CatalogName catalogName = tableHandle.getCatalogName();
        ConnectorMetadata metadata = getMetadata(session, catalogName);
        return metadata.getTableStatistics(session.toConnectorSession(catalogName), tableHandle.getConnectorHandle(), constraint);
    }

    @Override
    public Map<String, ColumnHandle> getColumnHandles(Session session, TableHandle tableHandle)
    {
        CatalogName catalogName = tableHandle.getCatalogName();
        ConnectorMetadata metadata = getMetadata(session, catalogName);
        Map<String, ColumnHandle> handles = metadata.getColumnHandles(session.toConnectorSession(catalogName), tableHandle.getConnectorHandle());

        ImmutableMap.Builder<String, ColumnHandle> map = ImmutableMap.builder();
        for (Entry<String, ColumnHandle> mapEntry : handles.entrySet()) {
            map.put(mapEntry.getKey().toLowerCase(ENGLISH), mapEntry.getValue());
        }
        return map.build();
    }

    @Override
    public ColumnMetadata getColumnMetadata(Session session, TableHandle tableHandle, ColumnHandle columnHandle)
    {
        requireNonNull(tableHandle, "tableHandle is null");
        requireNonNull(columnHandle, "columnHandle is null");

        CatalogName catalogName = tableHandle.getCatalogName();
        ConnectorMetadata metadata = getMetadata(session, catalogName);
        return metadata.getColumnMetadata(session.toConnectorSession(catalogName), tableHandle.getConnectorHandle(), columnHandle);
    }

    @Override
    public List<QualifiedObjectName> listTables(Session session, QualifiedTablePrefix prefix)
    {
        requireNonNull(prefix, "prefix is null");

        Optional<QualifiedObjectName> objectName = prefix.asQualifiedObjectName();
        if (objectName.isPresent()) {
            return getTableHandle(session, objectName.get())
                    .map(handle -> ImmutableList.of(objectName.get()))
import java.util.Map.Entry;
import java.util.Set;
import java.util.SortedMap;
import java.util.SortedSet;

import static com.google.common.collect.ImmutableMap.toImmutableMap;
import static com.google.common.collect.ImmutableSet.toImmutableSet;

public final class MetadataListing
{
    private MetadataListing() {}

    public static SortedMap<String, CatalogName> listCatalogs(Session session, Metadata metadata, AccessControl accessControl)
    {
        Map<String, CatalogName> catalogNames = metadata.getCatalogNames(session);
        Set<String> allowedCatalogs = accessControl.filterCatalogs(session.getIdentity(), catalogNames.keySet());

        ImmutableSortedMap.Builder<String, CatalogName> result = ImmutableSortedMap.naturalOrder();
        for (Map.Entry<String, CatalogName> entry : catalogNames.entrySet()) {
            if (allowedCatalogs.contains(entry.getKey())) {
                result.put(entry);
            }
        }
        return result.build();
    }

    public static SortedSet<String> listSchemas(Session session, Metadata metadata, AccessControl accessControl, String catalogName)
    {
        Set<String> schemaNames = ImmutableSet.copyOf(metadata.listSchemaNames(session, catalogName));
        return ImmutableSortedSet.copyOf(accessControl.filterSchemas(session.toSecurityContext(), catalogName, schemaNames));
    }

    public static Set<SchemaTableName> listTables(Session session, Metadata metadata, AccessControl accessControl, QualifiedTablePrefix prefix)
    {
        Set<SchemaTableName> tableNames = metadata.listTables(session, prefix).stream()
                .map(QualifiedObjectName::asSchemaTableName)
                .collect(toImmutableSet());
        return accessControl.filterTables(session.toSecurityContext(), prefix.getCatalogName(), tableNames);
    }

    public static Set<SchemaTableName> listViews(Session session, Metadata metadata, AccessControl accessControl, QualifiedTablePrefix prefix)
    {
        Set<SchemaTableName> tableNames = metadata.listViews(session, prefix).stream()
                .map(QualifiedObjectName::asSchemaTableName)
                .collect(toImmutableSet());
        return accessControl.filterTables(session.toSecurityContext(), prefix.getCatalogName(), tableNames);
    }

    public static Set<GrantInfo> listTablePrivileges(Session session, Metadata metadata, AccessControl accessControl, QualifiedTablePrefix prefix)
    {
        List<GrantInfo> grants = metadata.listTablePrivileges(session, prefix);
        Set<SchemaTableName> allowedTables = accessControl.filterTables(
                session.toSecurityContext(),
                prefix.getCatalogName(),
                grants.stream().map(GrantInfo::getSchemaTableName).collect(toImmutableSet()));

        return grants.stream()
                .filter(grantInfo -> allowedTables.contains(grantInfo.getSchemaTableName()))
                .collect(toImmutableSet());
    }

    public static Map<SchemaTableName, List<ColumnMetadata>> listTableColumns(Session session, Metadata metadata, AccessControl accessControl, QualifiedTablePrefix prefix)
    {
        Map<SchemaTableName, List<ColumnMetadata>> tableColumns = metadata.listTableColumns(session, prefix).entrySet().stream()
                .collect(toImmutableMap(entry -> entry.getKey().asSchemaTableName(), Entry::getValue));
        Set<SchemaTableName> allowedTables = accessControl.filterTables(
                session.toSecurityContext(),
                prefix.getCatalogName(),
          
[... 605 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2575/repo; sed -n 1,140p presto-main/src/main/java/io/prestosql/metadata/QualifiedTablePrefix.java; sed -n 270,300p presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java
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
package io.prestosql.metadata;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import io.prestosql.spi.connector.SchemaTablePrefix;

import javax.annotation.concurrent.Immutable;

import java.util.Objects;
import java.util.Optional;

import static com.google.common.base.Verify.verify;
import static io.prestosql.metadata.MetadataUtil.checkCatalogName;
import static io.prestosql.metadata.MetadataUtil.checkSchemaName;
import static io.prestosql.metadata.MetadataUtil.checkTableName;

@Immutable
public class QualifiedTablePrefix
{
    private final String catalogName;
    private final Optional<String> schemaName;
    private final Optional<String> tableName;

    public QualifiedTablePrefix(String catalogName)
    {
        this.catalogName = checkCatalogName(catalogName);
        this.schemaName = Optional.empty();
        this.tableName = Optional.empty();
    }

    public QualifiedTablePrefix(String catalogName, String schemaName)
    {
        this.catalogName = checkCatalogName(catalogName);
        this.schemaName = Optional.of(checkSchemaName(schemaName));
        this.tableName = Optional.empty();
    }

    public QualifiedTablePrefix(String catalogName, String schemaName, String tableName)
    {
        this.catalogName = checkCatalogName(catalogName);
        this.schemaName = Optional.of(checkSchemaName(schemaName));
        this.tableName = Optional.of(checkTableName(tableName));
    }

    @JsonCreator
    public QualifiedTablePrefix(
            @JsonProperty("catalogName") String catalogName,
            @JsonProperty("schemaName") Optional<String> schemaName,
            @JsonProperty("tableName") Optional<String> tableName)
    {
        checkTableName(catalogName, schemaName, tableName);
        this.catalogName = catalogName;
        this.schemaName = schemaName;
        this.tableName = tableName;
    }

    @JsonProperty
    public String getCatalogName()
    {
        return catalogName;
    }

    @JsonProperty
    public Optional<String> getSchemaName()
    {
        return schemaName;
    }

    @JsonProperty
    public Optional<String> getTableName()
    {
        return tableName;
    }

    public boolean hasSchemaName()
    {
        return schemaName.isPresent();
    }

    public boolean hasTableName()
    {
        return tableName.isPresent();
    }

    public SchemaTablePrefix asSchemaTablePrefix()
    {
        if (!schemaName.isPresent()) {
            return new SchemaTablePrefix();
        }
        else if (!tableName.isPresent()) {
            return new SchemaTablePrefix(schemaName.get());
        }
        else {
            return new SchemaTablePrefix(schemaName.get(), tableName.get());
        }
    }

    public Optional<QualifiedObjectName> asQualifiedObjectName()
    {
        if (tableName.isPresent()) {
            verify(schemaName.isPresent());
            return Optional.of(new QualifiedObjectName(catalogName, schemaName.get(), tableName.get()));
        }

        return Optional.empty();
    }

    public boolean matches(QualifiedObjectName objectName)
    {
        return Objects.equals(catalogName, objectName.getCatalogName())
                && schemaName.map(schema -> Objects.equals(schema, objectName.getSchemaName())).orElse(true)
                && tableName.map(table -> Objects.equals(table, objectName.getObjectName())).orElse(true);
    }

    @Override
    public boolean equals(Object obj)
    {
        if (obj == this) {
            return true;
        }
        if ((obj == null) || (getClass() != obj.getClass())) {
            return false;
        }
        QualifiedTablePrefix o = (QualifiedTablePrefix) obj;
        return Objects.equals(catalogName, o.catalogName) &&
                Objects.equals(schemaName, o.schemaName) &&
                Objects.equals(tableName, o.tableName);
        if (!catalog.isPresent()) {
            return false;
        }
        CatalogMetadata catalogMetadata = catalog.get();
        ConnectorSession connectorSession = session.toConnectorSession(catalogMetadata.getCatalogName());
        return catalogMetadata.listConnectorIds().stream()
                .map(catalogMetadata::getMetadataFor)
                .anyMatch(metadata -> metadata.schemaExists(connectorSession, schema.getSchemaName()));
    }

    @Override
    public List<String> listSchemaNames(Session session, String catalogName)
    {
        Optional<CatalogMetadata> catalog = getOptionalCatalogMetadata(session, catalogName);

        ImmutableSet.Builder<String> schemaNames = ImmutableSet.builder();
        if (catalog.isPresent()) {
            CatalogMetadata catalogMetadata = catalog.get();
            ConnectorSession connectorSession = session.toConnectorSession(catalogMetadata.getCatalogName());
            for (CatalogName connectorId : catalogMetadata.listConnectorIds()) {
                ConnectorMetadata metadata = catalogMetadata.getMetadataFor(connectorId);
                metadata.listSchemaNames(connectorSession).stream()
                        .map(schema -> schema.toLowerCase(Locale.ENGLISH))
                        .forEach(schemaNames::add);
            }
        }
        return ImmutableList.copyOf(schemaNames.build());
    }

    @Override
    public Optional<TableHandle> getTableHandle(Session session, QualifiedObjectName table)
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2575/repo; sed -n 298,330p presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java; grep -n "asSchemaTableName\|isEmpty()" presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java presto-main/src/main/java/io/prestosql/metadata/CatalogMetadata.java; grep -rn "table_name = ''\|table_name=''\|\"\"" --include=*.java presto-tests/src/main/java/io/prestosql/tests/AbstractTestDistributedQueries.java presto-main/src/test/java/io/prestosql/connector/informationschema 2>/dev/null | head
```

tool result:

```
    @Override
    public Optional<TableHandle> getTableHandle(Session session, QualifiedObjectName table)
    {
        requireNonNull(table, "table is null");

        Optional<CatalogMetadata> catalog = getOptionalCatalogMetadata(session, table.getCatalogName());
        if (catalog.isPresent()) {
            CatalogMetadata catalogMetadata = catalog.get();
            CatalogName catalogName = catalogMetadata.getConnectorId(session, table);
            ConnectorMetadata metadata = catalogMetadata.getMetadataFor(catalogName);

            ConnectorSession connectorSession = session.toConnectorSession(catalogName);
            ConnectorTableHandle tableHandle = metadata.getTableHandle(connectorSession, table.asSchemaTableName());
            if (tableHandle != null) {
                return Optional.of(new TableHandle(
                        catalogName,
                        tableHandle,
                        catalogMetadata.getTransactionHandleFor(catalogName),
                        Optional.empty()));
            }
        }
        return Optional.empty();
    }

    @Override
    public Optional<TableHandle> getTableHandleForStatisticsCollection(Session session, QualifiedObjectName table, Map<String, Object> analyzeProperties)
    {
        requireNonNull(table, "table is null");

        Optional<CatalogMetadata> catalog = getOptionalCatalogMetadata(session, table.getCatalogName());
        if (catalog.isPresent()) {
            CatalogMetadata catalogMetadata = catalog.get();
presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java:311:            ConnectorTableHandle tableHandle = metadata.getTableHandle(connectorSession, table.asSchemaTableName());
presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java:334:            ConnectorTableHandle tableHandle = metadata.getTableHandleForStatisticsCollection(session.toConnectorSession(catalogName), table.asSchemaTableName(), analyzeProperties);
presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java:360:            return metadata.getSystemTable(session.toConnectorSession(catalogName), tableName.asSchemaTableName());
presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java:383:        if (layouts.isEmpty()) {
presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java:482:        if (tableMetadata.getColumns().isEmpty()) {
presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java:639:        metadata.renameTable(session.toConnectorSession(catalog), tableHandle.getConnectorHandle(), newTableName.asSchemaTableName());
presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java:963:            return metadata.getView(connectorSession, viewName.asSchemaTableName());
presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java:975:        metadata.createView(session.toConnectorSession(catalogName), viewName.asSchemaTableName(), definition, replace);
presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java:988:        metadata.renameView(session.toConnectorSession(catalogName), source.asSchemaTableName(), target.asSchemaTableName());
presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java:998:        metadata.dropView(session.toConnectorSession(catalogName), viewName.asSchemaTableName());
presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java:1195:        metadata.grantTablePrivileges(session.toConnectorSession(catalogName), tableName.asSchemaTableName(), privileges, grantee, grantOption);
presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java:1205:        metadata.revokeTablePrivileges(session.toConnectorSession(catalogName), tableName.asSchemaTableName(), privileges, grantee, grantOption);
presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java:1309:        if (!missingOperators.isEmpty()) {
presto-main/src/main/java/io/prestosql/metadata/CatalogMetadata.java:115:        if (systemTables.getTableHandle(session.toConnectorSession(systemTablesId), table.asSchemaTableName()) != null) {
(eval):1: no matches found: --include=*.java
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2575/repo; grep -n "asQualifiedObjectName\|getTableHandle(session\|getView(session\|getSystemTable(session" presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java; sed -n 340,365p presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java; sed -n 945,970p presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java; grep -n "checkSchemaName\|checkTableName\|checkLowerCase" -A6 presto-main/src/main/java/io/prestosql/metadata/MetadataUtil.java | head -60
```

tool result:

```
360:            return metadata.getSystemTable(session.toConnectorSession(catalogName), tableName.asSchemaTableName());
527:        Optional<QualifiedObjectName> objectName = prefix.asQualifiedObjectName();
529:            return getTableHandle(session, objectName.get())
890:        Optional<QualifiedObjectName> objectName = prefix.asQualifiedObjectName();
892:            return getView(session, objectName.get())
1220:            List<CatalogName> connectorIds = prefix.asQualifiedObjectName()
                        Optional.empty()));
            }
        }
        return Optional.empty();
    }

    @Override
    public Optional<SystemTable> getSystemTable(Session session, QualifiedObjectName tableName)
    {
        requireNonNull(session, "session is null");
        requireNonNull(tableName, "table is null");

        Optional<CatalogMetadata> catalog = getOptionalCatalogMetadata(session, tableName.getCatalogName());
        if (catalog.isPresent()) {
            CatalogMetadata catalogMetadata = catalog.get();

            // we query only main connector for runtime system tables
            CatalogName catalogName = catalogMetadata.getCatalogName();
            ConnectorMetadata metadata = catalogMetadata.getMetadataFor(catalogName);

            return metadata.getSystemTable(session.toConnectorSession(catalogName), tableName.asSchemaTableName());
        }
        return Optional.empty();
    }

    @Override
                            entry.getKey().getTableName());
                    views.put(viewName, entry.getValue());
                }
            }
        }
        return ImmutableMap.copyOf(views);
    }

    @Override
    public Optional<ConnectorViewDefinition> getView(Session session, QualifiedObjectName viewName)
    {
        Optional<CatalogMetadata> catalog = getOptionalCatalogMetadata(session, viewName.getCatalogName());
        if (catalog.isPresent()) {
            CatalogMetadata catalogMetadata = catalog.get();
            CatalogName catalogName = catalogMetadata.getConnectorId(session, viewName);
            ConnectorMetadata metadata = catalogMetadata.getMetadataFor(catalogName);

            ConnectorSession connectorSession = session.toConnectorSession(catalogName);
            return metadata.getView(connectorSession, viewName.asSchemaTableName());
        }
        return Optional.empty();
    }

    @Override
    public void createView(Session session, QualifiedObjectName viewName, ConnectorViewDefinition definition, boolean replace)
    {
50:    public static void checkTableName(String catalogName, Optional<String> schemaName, Optional<String> tableName)
51-    {
52-        checkCatalogName(catalogName);
53:        schemaName.ifPresent(name -> checkLowerCase(name, "schemaName"));
54:        tableName.ifPresent(name -> checkLowerCase(name, "tableName"));
55-
56-        checkArgument(schemaName.isPresent() || !tableName.isPresent(), "tableName specified but schemaName is missing");
57-    }
58-
59-    public static String checkCatalogName(String catalogName)
60-    {
61:        return checkLowerCase(catalogName, "catalogName");
62-    }
63-
64:    public static String checkSchemaName(String schemaName)
65-    {
66:        return checkLowerCase(schemaName, "schemaName");
67-    }
68-
69:    public static String checkTableName(String tableName)
70-    {
71:        return checkLowerCase(tableName, "tableName");
72-    }
73-
74-    public static void checkObjectName(String catalogName, String schemaName, String objectName)
75-    {
76:        checkLowerCase(catalogName, "catalogName");
77:        checkLowerCase(schemaName, "schemaName");
78:        checkLowerCase(objectName, "objectName");
79-    }
80-
81:    public static String checkLowerCase(String value, String name)
82-    {
83-        if (value == null) {
84-            throw new NullPointerException(format("%s is null", name));
85-        }
86-        checkArgument(value.equals(value.toLowerCase(ENGLISH)), "%s is not lowercase: %s", name, value);
87-        return value;
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2575/repo; cat presto-spi/src/main/java/io/prestosql/spi/connector/SchemaTablePrefix.java | sed -n 20,60p; sed -n 1210,1240p presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java; grep -rln "information_schema" --include=*.java presto-tests/src/test | head
```

tool result:

```
public class SchemaTablePrefix
{
    private final Optional<String> schemaName;
    private final Optional<String> tableName;

    public SchemaTablePrefix()
    {
        this.schemaName = Optional.empty();
        this.tableName = Optional.empty();
    }

    public SchemaTablePrefix(String schemaName)
    {
        this.schemaName = Optional.of(checkNotEmpty(schemaName, "schemaName"));
        this.tableName = Optional.empty();
    }

    public SchemaTablePrefix(String schemaName, String tableName)
    {
        this.schemaName = Optional.of(checkNotEmpty(schemaName, "schemaName"));
        this.tableName = Optional.of(checkNotEmpty(tableName, "tableName"));
    }

    public Optional<String> getSchema()
    {
        return schemaName;
    }

    public Optional<String> getTable()
    {
        return tableName;
    }

    public boolean matches(SchemaTableName schemaTableName)
    {
        // empty prefix matches everything
        if (isEmpty()) {
            return true;
        }

    {
        requireNonNull(prefix, "prefix is null");

        Optional<CatalogMetadata> catalog = getOptionalCatalogMetadata(session, prefix.getCatalogName());

        ImmutableSet.Builder<GrantInfo> grantInfos = ImmutableSet.builder();
        if (catalog.isPresent()) {
            CatalogMetadata catalogMetadata = catalog.get();
            ConnectorSession connectorSession = session.toConnectorSession(catalogMetadata.getCatalogName());

            List<CatalogName> connectorIds = prefix.asQualifiedObjectName()
                    .map(qualifiedTableName -> singletonList(catalogMetadata.getConnectorId(session, qualifiedTableName)))
                    .orElseGet(catalogMetadata::listConnectorIds);
            for (CatalogName catalogName : connectorIds) {
                ConnectorMetadata metadata = catalogMetadata.getMetadataFor(catalogName);
                grantInfos.addAll(metadata.listTablePrivileges(connectorSession, prefix.asSchemaTablePrefix()));
            }
        }
        return ImmutableList.copyOf(grantInfos.build());
    }

    //
    // Types
    //

    @Override
    public Type getType(TypeSignature signature)
    {
        return typeRegistry.getType(new InternalTypeManager(this), signature);
    }

(eval):1: no matches found: --include=*.java
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2575/repo; grep -n "QualifiedTablePrefix\|isEmpty\|private .*(" presto-main/src/main/java/io/prestosql/connector/informationschema/InformationSchemaMetadata.java
```

tool result:

```
24:import io.prestosql.metadata.QualifiedTablePrefix;
76:    private static final InformationSchemaColumnHandle CATALOG_COLUMN_HANDLE = new InformationSchemaColumnHandle("table_catalog");
77:    private static final InformationSchemaColumnHandle SCHEMA_COLUMN_HANDLE = new InformationSchemaColumnHandle("table_schema");
78:    private static final InformationSchemaColumnHandle TABLE_NAME_COLUMN_HANDLE = new InformationSchemaColumnHandle("table_name");
193:        Set<QualifiedTablePrefix> prefixes = getPrefixes(session, table, constraint);
204:    public static Set<QualifiedTablePrefix> defaultPrefixes(String catalogName)
206:        return ImmutableSet.of(new QualifiedTablePrefix(catalogName));
209:    private Set<QualifiedTablePrefix> getPrefixes(ConnectorSession session, InformationSchemaTableHandle table, Constraint constraint)
221:        Set<QualifiedTablePrefix> prefixes = calculatePrefixesWithSchemaName(session, constraint.getSummary(), constraint.predicate());
222:        Set<QualifiedTablePrefix> tablePrefixes = calculatePrefixesWithTableName(informationSchemaTable, session, prefixes, constraint.getSummary(), constraint.predicate());
240:    private Set<QualifiedTablePrefix> calculatePrefixesWithSchemaName(
250:                    .map(schema -> new QualifiedTablePrefix(catalogName, schema))
255:            return ImmutableSet.of(new QualifiedTablePrefix(catalogName));
264:    private Set<QualifiedTablePrefix> calculatePrefixesWithTableName(
267:            Set<QualifiedTablePrefix> prefixes,
285:                    .map(QualifiedObjectName::asQualifiedTablePrefix)
298:                .map(QualifiedObjectName::asQualifiedTablePrefix)
302:    private boolean isColumnsEnumeratingTable(InformationSchemaTable table)
307:    private Stream<QualifiedTablePrefix> listSchemaNames(Session session)
310:                .map(schema -> new QualifiedTablePrefix(catalogName, schema));
313:    private <T> Optional<Set<String>> filterString(TupleDomain<T> constraint, T column)
350:    private Map<ColumnHandle, NullableValue> schemaAsFixedValues(String schema)
355:    private Map<ColumnHandle, NullableValue> asFixedValues(QualifiedObjectName objectName)
363:    private boolean isLowerCase(String value)
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2575/repo; sed -n 185,370p presto-main/src/main/java/io/prestosql/connector/informationschema/InformationSchemaMetadata.java
```

tool result:

```
    public Optional<ConstraintApplicationResult<ConnectorTableHandle>> applyFilter(ConnectorSession session, ConnectorTableHandle handle, Constraint constraint)
    {
        InformationSchemaTableHandle table = (InformationSchemaTableHandle) handle;

        if (!isTablesEnumeratingTable(table.getTable()) || !table.getPrefixes().equals(defaultPrefixes(catalogName))) {
            return Optional.empty();
        }

        Set<QualifiedTablePrefix> prefixes = getPrefixes(session, table, constraint);

        if (prefixes.equals(table.getPrefixes())) {
            return Optional.empty();
        }

        table = new InformationSchemaTableHandle(table.getCatalogName(), table.getTable(), prefixes, table.getLimit());

        return Optional.of(new ConstraintApplicationResult<>(table, constraint.getSummary()));
    }

    public static Set<QualifiedTablePrefix> defaultPrefixes(String catalogName)
    {
        return ImmutableSet.of(new QualifiedTablePrefix(catalogName));
    }

    private Set<QualifiedTablePrefix> getPrefixes(ConnectorSession session, InformationSchemaTableHandle table, Constraint constraint)
    {
        if (constraint.getSummary().isNone()) {
            return ImmutableSet.of();
        }

        Optional<Set<String>> catalogs = filterString(constraint.getSummary(), CATALOG_COLUMN_HANDLE);
        if (catalogs.isPresent() && !catalogs.get().contains(table.getCatalogName())) {
            return ImmutableSet.of();
        }

        InformationSchemaTable informationSchemaTable = table.getTable();
        Set<QualifiedTablePrefix> prefixes = calculatePrefixesWithSchemaName(session, constraint.getSummary(), constraint.predicate());
        Set<QualifiedTablePrefix> tablePrefixes = calculatePrefixesWithTableName(informationSchemaTable, session, prefixes, constraint.getSummary(), constraint.predicate());
        // in case of high number of prefixes it is better to populate all data and then filter
        if (tablePrefixes.size() <= MAX_PREFIXES_COUNT) {
            prefixes = tablePrefixes;
        }
        if (prefixes.size() > MAX_PREFIXES_COUNT) {
            // in case of high number of prefixes it is better to populate all data and then filter
            prefixes = defaultPrefixes(catalogName);
        }

        return prefixes;
    }

    public static boolean isTablesEnumeratingTable(InformationSchemaTable table)
    {
        return ImmutableSet.of(COLUMNS, VIEWS, TABLES, TABLE_PRIVILEGES).contains(table);
    }

    private Set<QualifiedTablePrefix> calculatePrefixesWithSchemaName(
            ConnectorSession connectorSession,
            TupleDomain<ColumnHandle> constraint,
            Optional<Predicate<Map<ColumnHandle, NullableValue>>> predicate)
    {
        Optional<Set<String>> schemas = filterString(constraint, SCHEMA_COLUMN_HANDLE);
        if (schemas.isPresent()) {
            return schemas.get().stream()
                    .filter(this::isLowerCase)
                    .filter(schema -> !predicate.isPresent() || predicate.get().test(schemaAsFixedValues(schema)))
                    .map(schema -> new QualifiedTablePrefix(catalogName, schema))
                    .collect(toImmutableSet());
        }

        if (!predicate.isPresent()) {
            return ImmutableSet.of(new QualifiedTablePrefix(catalogName));
        }

        Session session = ((FullConnectorSession) connectorSession).getSession();
        return listSchemaNames(session)
                .filter(prefix -> predicate.get().test(schemaAsFixedValues(prefix.getSchemaName().get())))
                .collect(toImmutableSet());
    }

    private Set<QualifiedTablePrefix> calculatePrefixesWithTableName(
            InformationSchemaTable informationSchemaTable,
            ConnectorSession connectorSession,
            Set<QualifiedTablePrefix> prefixes,
            TupleDomain<ColumnHandle> constraint,
            Optional<Predicate<Map<ColumnHandle, NullableValue>>> predicate)
    {
        Session session = ((FullConnectorSession) connectorSession).getSession();

        Optional<Set<String>> tables = filterString(constraint, TABLE_NAME_COLUMN_HANDLE);
        if (tables.isPresent()) {
            return prefixes.stream()
                    .peek(prefix -> verify(!prefix.asQualifiedObjectName().isPresent()))
                    .flatMap(prefix -> prefix.getSchemaName()
                            .map(schemaName -> Stream.of(prefix))
                            .orElseGet(() -> listSchemaNames(session)))
                    .flatMap(prefix -> tables.get().stream()
                            .filter(this::isLowerCase)
                            .map(table -> new QualifiedObjectName(catalogName, prefix.getSchemaName().get(), table)))
                    .filter(objectName -> !isColumnsEnumeratingTable(informationSchemaTable) || metadata.getTableHandle(session, objectName).isPresent() || metadata.getView(session, objectName).isPresent())
                    .filter(objectName -> !predicate.isPresent() || predicate.get().test(asFixedValues(objectName)))
                    .map(QualifiedObjectName::asQualifiedTablePrefix)
                    .collect(toImmutableSet());
        }

        if (!predicate.isPresent() || !isColumnsEnumeratingTable(informationSchemaTable)) {
            return prefixes;
        }

        return prefixes.stream()
                .flatMap(prefix -> Stream.concat(
                        metadata.listTables(session, prefix).stream(),
                        metadata.listViews(session, prefix).stream()))
                .filter(objectName -> predicate.get().test(asFixedValues(objectName)))
                .map(QualifiedObjectName::asQualifiedTablePrefix)
                .collect(toImmutableSet());
    }

    private boolean isColumnsEnumeratingTable(InformationSchemaTable table)
    {
        return COLUMNS.equals(table);
    }

    private Stream<QualifiedTablePrefix> listSchemaNames(Session session)
    {
        return metadata.listSchemaNames(s
[... 2385 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2575/repo; grep -rl "information_schema" presto-tests/src/test presto-main/src/test | head -20; ls ~/.m2 2>/dev/null; ../bin/envrun 'ls ~/.m2/repository | head; ls presto-main/target presto-tests/target 2>/dev/null | head'
```

tool result:

```
presto-tests/src/test/java/io/prestosql/tests/TestLocalQueries.java
presto-tests/src/test/java/io/prestosql/tests/TestMetadataManager.java
presto-tests/src/test/java/io/prestosql/tests/TestInformationSchemaConnector.java
presto-tests/src/test/java/io/prestosql/connector/informationschema/BenchmarkInformationSchema.java
presto-main/src/test/java/io/prestosql/metadata/TestInformationSchemaTableHandle.java
presto-main/src/test/java/io/prestosql/metadata/TestInformationSchemaMetadata.java
ls: cannot access '/root/.m2/repository': No such file or directory
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2575/repo; ../bin/envrun 'which mvn java; ls -a ~; ls /testbed; cat ~/.m2/settings.xml 2>/dev/null; ls / ' ; sed -n 1,80p presto-tests/src/test/java/io/prestosql/tests/TestInformationSchemaConnector.java
```

tool result:

```
bash: line 1: which: command not found
.
..
.cache
.ssh
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
docker
mvnw
pom.xml
presto-accumulo
presto-array
presto-atop
presto-base-jdbc
presto-benchmark
presto-benchmark-driver
presto-benchto-benchmarks
presto-blackhole
presto-cassandra
presto-cli
presto-client
presto-docs
presto-elasticsearch
presto-example-http
presto-geospatial
presto-geospatial-toolkit
presto-google-sheets
presto-hive
presto-hive-hadoop2
presto-iceberg
presto-jdbc
presto-jmx
presto-kafka
presto-kinesis
presto-kudu
presto-local-file
presto-main
presto-matching
presto-memory
presto-memory-context
presto-memsql
presto-ml
presto-mongodb
presto-mysql
presto-orc
presto-parquet
presto-parser
presto-password-authenticators
presto-phoenix
presto-plugin-toolkit
presto-postgresql
presto-product-tests
presto-product-tests-launcher
presto-proxy
presto-raptor-legacy
presto-rcfile
presto-record-decoder
presto-redis
presto-redshift
presto-resource-group-managers
presto-server
presto-server-rpm
presto-session-property-managers
presto-spi
presto-sqlserver
presto-teradata-functions
presto-testing
presto-testing-server-launcher
presto-tests
presto-thrift
presto-thrift-api
presto-thrift-testing-server
presto-tpcds
presto-tpch
presto-verifier
src
bin
boot
dev
etc
home
lib
lib64
local
media
mnt
opt
proc
root
run
sbin
srv
sys
testbed
tmp
usr
var

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
package io.prestosql.tests;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableMap;
import io.prestosql.Session;
import io.prestosql.connector.MockConnectorFactory;
import io.prestosql.plugin.tpch.TpchPlugin;
import io.prestosql.spi.Plugin;
import io.prestosql.spi.connector.ConnectorFactory;
import io.prestosql.spi.connector.SchemaTableName;
import io.prestosql.testing.AbstractTestQueryFramework;
import io.prestosql.testing.DistributedQueryRunner;
import org.testng.annotations.Test;

import java.util.List;
import java.util.Objects;
import java.util.concurrent.atomic.AtomicLong;
import java.util.stream.IntStream;

import static com.google.common.base.MoreObjects.toStringHelper;
import static com.google.common.collect.ImmutableList.toImmutableList;
import static io.prestosql.connector.MockConnectorFactory.Builder.defaultGetColumns;
import static io.prestosql.testing.TestingSession.testSessionBuilder;
import static org.testng.Assert.assertEquals;

@Test(singleThreaded = true)
public class TestInformationSchemaConnector
        extends AbstractTestQueryFramework
{
    private static final AtomicLong LIST_SCHEMAS_CALLS_COUNTER = new AtomicLong();
    private static final AtomicLong LIST_TABLES_CALLS_COUNTER = new AtomicLong();
    private static final AtomicLong GET_COLUMNS_CALLS_COUNTER = new AtomicLong();

    @Test
    public void testBasic()
    {
        assertQuery("SELECT count(*) FROM tpch.information_schema.schemata", "VALUES 10");
        assertQuery("SELECT count(*) FROM tpch.information_schema.tables", "VALUES 80");
        assertQuery("SELECT count(*) FROM tpch.information_schema.columns", "VALUES 583");
        assertQuery("SELECT * FROM tpch.information_schema.schemata ORDER BY 1 DESC, 2 DESC LIMIT 1", "VALUES ('tpch', 'tiny')");
        assertQuery("SELECT * FROM tpch.information_schema.tables ORDER BY 1 DESC, 2 DESC, 3 DESC, 4 DESC LIMIT 1", "VALUES ('tpch', 'tiny', 'supplier', 'BASE TABLE')");
        assertQuery("SELECT * FROM tpch.information_schema.columns ORDER BY 1 DESC, 2 DESC, 3 DESC, 4 DESC LIMIT 1", "VALUES ('tpch', 'tiny', 'supplier', 'suppkey', 1, NULL, 'YES', 'bigint')");
        assertQuery("SELECT count(*) FROM test_catalog.information_schema.columns", "VALUES 3000034");
    }

    @Test
    public void testSchemaNamePredicate()
    {
        assertQuery("SELECT count(*) FROM tpch.information_schema.schemata WHERE schema_name = 'sf1'", "VALUES 1");
        assertQuery("SELECT count(*) FROM tpch.information_schema.tables WHERE table_schema = 'sf1'", "VALUES 8");
        assertQuery("SELECT count(*) FROM tpch.information_schema.columns WHERE table_schema = 'sf1'", "VALUES 61");
        assertQuery("SELECT count(*) FROM tpch.information_schema.columns WHERE table_schema = 'information_schema'", "VALUES 34");
        assertQuery("SELECT count(*) FROM tpch.information_schema.columns WHERE table_schema > 'sf100'", "VALUES 427");
        assertQuery("SELECT count(*) FROM tpch.information_schema.columns WHERE table_schema != 'sf100'", "VALUES 522");
        assertQuery("SELECT count(*) FROM tpch.information_schema.columns WHERE table_schema LIKE 'sf100'", "VALUES 61");
        assertQuery("SELECT count(*) FROM tpch.information_schema.columns WHERE table_schema LIKE 'sf%'", "VALUES 488");
    }

    @Test
    public void testTableNamePredicate()
    {
        assertQuery("SELECT count(*) FROM tpch.information_schema.tables WHERE table_name = 'orders'", "VALUES 9");
        assertQuery("SELECT count(*) FROM tpch.information_schema.tables WHERE table_name = 'ORDERS'", "VALUES 0");
        assertQuery("SELECT count(*) FROM tpch.information_schema.tables WHERE table_name LIKE 'orders'", "VALUES 9");
        assertQuery("SELECT count(*) FROM tpch.information_schema.tables WHERE table_name < 'orders'", "VALUES 30");
        assertQuery("SELECT count(*) FROM tpch.information_schema.tables WHERE table_name LIKE 'part'", "VALUES 9");
        assertQuery("SELECT count(*) FROM tpch.information_schema.tables WHERE table_name LIKE 'part%'", "VALUES 18");
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2575/repo; ../bin/envrun 'command -v mvn java; java -version 2>&1; ls ~/.cache; ls /testbed/presto-main/target 2>&1 | head -3; env | grep -i maven'
```

tool result:

```
/usr/local/apache-maven-3.9.11/bin/mvn
/usr/bin/java
openjdk version "11.0.28" 2025-07-15 LTS
OpenJDK Runtime Environment Corretto-11.0.28.6.1 (build 11.0.28+6-LTS)
OpenJDK 64-Bit Server VM Corretto-11.0.28.6.1 (build 11.0.28+6-LTS, mixed mode)
rosetta
ls: cannot access '/testbed/presto-main/target': No such file or directory
M2_HOME=/usr/local/apache-maven-3.9.11
MAVEN_HOME=/usr/local/apache-maven-3.9.11
PATH=/usr/local/apache-maven-3.9.11/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2575/repo; ../bin/envrun 'cat /usr/local/apache-maven-3.9.11/conf/settings.xml | grep -i localRepo; find / -maxdepth 4 -name "repository" -type d 2>/dev/null | head'
```

tool result:

```
  <!-- localRepository
  <localRepository>/path/to/local/repo</localRepository>
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2575/repo; ../bin/envrun 'find / -name "guava*.jar" -not -path "/proc/*" 2>/dev/null | head; df -h / | tail -1'
```

tool result:

```
/usr/local/apache-maven-3.9.11/lib/guava-33.4.8-jre.jar
overlay         911G   68G  798G   8% /
```

**thinking:**

```
Since I can't build or run tests here, I'll fix this by tracing the code manually: the empty name originates from predicate pushdown in `InformationSchemaMetadata` and flows into `MetadataManager.getTableHandle`, and an empty `table_schema` would break the same way via `SchemaTablePrefix`. I'll fix both spots.


```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2575/repo; python3 - <<'EOF'
p='presto-main/src/main/java/io/prestosql/connector/informationschema/InformationSchemaMetadata.java'
s=open(p).read()
old1="""                    .filter(this::isLowerCase)
                    .filter(schema -> !predicate"""
new1="""                    .filter(this::isLowerCase)
                    .filter(schema -> !schema.isEmpty())
                    .filter(schema -> !predicate"""
old2="""                            .filter(this::isLowerCase)
                            .map(table ->"""
new2="""                            .filter(this::isLowerCase)
                            .filter(table -> !table.isEmpty())
                            .map(table ->"""
assert s.count(old1)==1 and s.count(old2)==1
s=s.replace(old1,new1).replace(old2,new2)
open(p,'w').write(s)

p='presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java'
s=open(p).read()
old="""        requireNonNull(table, "table is null");

        Optional<CatalogMetadata> catalog = getOptionalCatalogMetadata(session, table.getCatalogName());
        if (catalog.isPresent()) {
            CatalogMetadata catalogMetadata = catalog.get();
            CatalogName catalogName = catalogMetadata.getConnectorId(session, table);
            ConnectorMetadata metadata = catalogMetadata.getMetadataFor(catalogName);

            ConnectorSession connectorSession = session.toConnectorSession(catalogName);
            ConnectorTableHandle tableHandle = metadata.getTableHandle(connectorSession, table.asSchemaTableName());"""
new="""        requireNonNull(table, "table is null");

        if (cannotExist(table)) {
            return Optional.empty();
        }

        Optional<CatalogMetadata> catalog = getOptionalCatalogMetadata(session, table.getCatalogName());
        if (catalog.isPresent()) {
            CatalogMetadata catalogMetadata = catalog.get();
            CatalogName catalogName = catalogMetadata.getConnectorId(session, table);
            ConnectorMetadata metadata = catalogMetadata.getMetadataFor(catalogName);

            ConnectorSession connectorSession = session.toConnectorSession(catalogName);
            ConnectorTableHandle tableHandle = metadata.getTableHandle(connectorSession, table.asSchemaTableName());"""
assert s.count(old)==1
s=s.replace(old,new)
old="""    public Optional<ConnectorViewDefinition> getView(Session session, QualifiedObjectName viewName)
    {
"""
new="""    public Optional<ConnectorViewDefinition> getView(Session session, QualifiedObjectName viewName)
    {
        if (cannotExist(viewName)) {
            return Optional.empty();
        }

"""
assert s.count(old)==1
s=s.replace(old,new)
open(p,'w').write(s)
EOF
grep -n "^    private static\|^    private .*(" presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java | tail -5; tail -30 presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java
```

tool result:

```
1546:    private CatalogMetadata getCatalogMetadataForWrite(Session session, CatalogName catalogName)
1553:    private ConnectorMetadata getMetadata(Session session, CatalogName catalogName)
1558:    private ConnectorMetadata getMetadataForWrite(Session session, CatalogName catalogName)
1563:    private void registerCatalogForQuery(Session session, CatalogMetadata catalogMetadata)
1575:    private static class QueryCatalogs
        public QueryCatalogs(Session session)
        {
            this.session = requireNonNull(session, "session is null");
        }

        private synchronized void registerCatalog(CatalogMetadata catalogMetadata)
        {
            checkState(!finished, "Query is already finished");
            if (catalogs.putIfAbsent(catalogMetadata.getCatalogName(), catalogMetadata) == null) {
                ConnectorSession connectorSession = session.toConnectorSession(catalogMetadata.getCatalogName());
                catalogMetadata.getMetadata().beginQuery(connectorSession);
            }
        }

        private synchronized void finish()
        {
            List<CatalogMetadata> catalogs;
            synchronized (this) {
                checkState(!finished, "Query is already finished");
                finished = true;
                catalogs = new ArrayList<>(this.catalogs.values());
            }

            for (CatalogMetadata catalogMetadata : catalogs) {
                ConnectorSession connectorSession = session.toConnectorSession(catalogMetadata.getCatalogName());
                catalogMetadata.getMetadata().cleanupQuery(connectorSession);
            }
        }
    }
}
```

**tool call: Bash**

```bash
cd /work/trinodb__trino-2575/repo; sed -n 1560,1575p presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java
```

tool result:

```
        return getCatalogMetadataForWrite(session, catalogName).getMetadata();
    }

    private void registerCatalogForQuery(Session session, CatalogMetadata catalogMetadata)
    {
        catalogsByQueryId.computeIfAbsent(session.getQueryId(), queryId -> new QueryCatalogs(session))
                .registerCatalog(catalogMetadata);
    }

    @VisibleForTesting
    public Set<QueryId> getActiveQueryIds()
    {
        return ImmutableSet.copyOf(catalogsByQueryId.keySet());
    }

    private static class QueryCatalogs
```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/trinodb__trino-2575/repo/presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java",
 "old_string": "    @VisibleForTesting\n    public Set<QueryId> getActiveQueryIds()",
 "new_string": "    private static boolean cannotExist(QualifiedObjectName name)\n    {\n        return name.getCatalogName().isEmpty() || name.getSchemaName().isEmpty() || name.getObjectName().isEmpty();\n    }\n\n    @VisibleForTesting\n    public Set<QueryId> getActiveQueryIds()"
}
```

tool result:

```
The file /work/trinodb__trino-2575/repo/presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java has been updated successfully. (file state is current in your context — no need to Read it back)
```

**assistant:** Both edits are in. Let me check the diff, since I can't compile it:

**tool call: Bash**

```bash
cd /work/trinodb__trino-2575/repo; git diff; git status --short
```

tool result:

```
diff --git a/presto-main/src/main/java/io/prestosql/connector/informationschema/InformationSchemaMetadata.java b/presto-main/src/main/java/io/prestosql/connector/informationschema/InformationSchemaMetadata.java
index 1981e3092f..ea87c7fd37 100644
--- a/presto-main/src/main/java/io/prestosql/connector/informationschema/InformationSchemaMetadata.java
+++ b/presto-main/src/main/java/io/prestosql/connector/informationschema/InformationSchemaMetadata.java
@@ -246,6 +246,7 @@ public class InformationSchemaMetadata
         if (schemas.isPresent()) {
             return schemas.get().stream()
                     .filter(this::isLowerCase)
+                    .filter(schema -> !schema.isEmpty())
                     .filter(schema -> !predicate.isPresent() || predicate.get().test(schemaAsFixedValues(schema)))
                     .map(schema -> new QualifiedTablePrefix(catalogName, schema))
                     .collect(toImmutableSet());
@@ -279,6 +280,7 @@ public class InformationSchemaMetadata
                             .orElseGet(() -> listSchemaNames(session)))
                     .flatMap(prefix -> tables.get().stream()
                             .filter(this::isLowerCase)
+                            .filter(table -> !table.isEmpty())
                             .map(table -> new QualifiedObjectName(catalogName, prefix.getSchemaName().get(), table)))
                     .filter(objectName -> !isColumnsEnumeratingTable(informationSchemaTable) || metadata.getTableHandle(session, objectName).isPresent() || metadata.getView(session, objectName).isPresent())
                     .filter(objectName -> !predicate.isPresent() || predicate.get().test(asFixedValues(objectName)))
diff --git a/presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java b/presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java
index 50d26c1e42..ce93caa1aa 100644
--- a/presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java
+++ b/presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java
@@ -301,6 +301,10 @@ public final class MetadataManager
     {
         requireNonNull(table, "table is null");
 
+        if (cannotExist(table)) {
+            return Optional.empty();
+        }
+
         Optional<CatalogMetadata> catalog = getOptionalCatalogMetadata(session, table.getCatalogName());
         if (catalog.isPresent()) {
             CatalogMetadata catalogMetadata = catalog.get();
@@ -953,6 +957,10 @@ public final class MetadataManager
     @Override
     public Optional<ConnectorViewDefinition> getView(Session session, QualifiedObjectName viewName)
     {
+        if (cannotExist(viewName)) {
+            return Optional.empty();
+        }
+
         Optional<CatalogMetadata> catalog = getOptionalCatalogMetadata(session, viewName.getCatalogName());
         if (catalog.isPresent()) {
             CatalogMetadata catalogMetadata = catalog.get();
@@ -1558,6 +1566,11 @@ public final class MetadataManager
                 .registerCatalog(catalogMetadata);
     }
 
+    private static boolean cannotExist(QualifiedObjectName name)
+    {
+        return name.getCatalogName().isEmpty() || name.getSchemaName().isEmpty() || name.getObjectName().isEmpty();
+    }
+
     @VisibleForTesting
     public Set<QueryId> getActiveQueryIds()
     {
 M presto-main/src/main/java/io/prestosql/connector/informationschema/InformationSchemaMetadata.java
 M presto-main/src/main/java/io/prestosql/metadata/MetadataManager.java
?? Dockerfile
```

**assistant:** I've made the fix, but I haven't compiled it, reproduced the error or run any tests. The container has no Maven local repository and no network, so the project's dependencies can't be resolved and nothing builds. Everything below comes from reading the code.

**Cause:** For a filter like `table_name = ''`, `InformationSchemaMetadata.applyFilter` turned `''` into a table-name prefix. That prefix ended up in `MetadataManager.listTables`, then `getTableHandle`, where `QualifiedObjectName.asSchemaTableName()` builds a `SchemaTableName` and fails with `tableName is empty`. `table_schema = ''` would fail the same way, inside `SchemaTablePrefix`.

**Changes:**
1. `presto-main/.../connector/informationschema/InformationSchemaMetadata.java`: when the filter values are turned into prefixes, empty schema and table names are now dropped. This is the same thing already done for names that aren't lowercase. No schema or table can have an empty name, so such a predicate now returns no rows instead of failing. This covers `tables`, `views`, `columns` and `table_privileges`, and both `=` and `IN (...)`.
2. `presto-main/.../metadata/MetadataManager.java`: I added a `cannotExist(QualifiedObjectName)` helper. `getTableHandle` and `getView` now return `Optional.empty()` when the catalog, schema or object name is empty, rather than throwing. This also protects other callers, including the `columns` path, which calls these methods directly.

**Expected results:**
- The query from the issue should return an empty result.
- `table_schema = ''` should also return nothing.
- Mixed lists like `table_name IN ('', 'orders')` should still return `orders`.
- When the filter isn't pushed down, all rows are listed and filtered afterwards, which was never affected.

**To verify,** in an environment with dependencies, run `TestInformationSchemaConnector` (in presto-tests) and `TestInformationSchemaMetadata` (in presto-main), plus the issue's query. I didn't create any reproduction files, so there was nothing to clean up. The untracked `Dockerfile` was already in the repository and I left it alone.

_session end: success, turns 17, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.29 s: ls ~/.m2/repository | head; ls presto-main/target presto-tests/target 2>/dev/null | head
- `rc=0` 0.33 s: which mvn java; ls -a ~; ls /testbed; cat ~/.m2/settings.xml 2>/dev/null; ls / 
- `rc=0` 0.57 s: command -v mvn java; java -version 2>&1; ls ~/.cache; ls /testbed/presto-main/target 2>&1 | head -3; env | grep -i maven
- `rc=0` 0.34 s: cat /usr/local/apache-maven-3.9.11/conf/settings.xml | grep -i localRepo; find / -maxdepth 4 -name "repository" -type d 2>/dev/null | head
- `rc=0` 0.75 s: find / -name "guava*.jar" -not -path "/proc/*" 2>/dev/null | head; df -h / | tail -1
