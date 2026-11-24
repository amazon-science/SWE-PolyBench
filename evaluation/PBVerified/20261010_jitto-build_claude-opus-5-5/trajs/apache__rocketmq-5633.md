# Instance: apache__rocketmq-5633

- Final resolved (evaluator, logs/apache__rocketmq-5633_result.json): False
- Run state: DONE
- One attempt. Duration 445.5 s, turns 21, actor cost $0.6657854000000001, container commands 13
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/apache__rocketmq-5633/repo
</uploaded_files>
I've uploaded a Java code repository in the directory /work/apache__rocketmq-5633/repo. Consider the following issue description:

<issue_description>
ReplicasInfoManager#registerBroker not check master is alive
The issue tracker is used for bug reporting purposes **ONLY** whereas feature request needs to follow the [RIP process](https://github.com/apache/rocketmq/wiki/RocketMQ-Improvement-Proposal). To avoid unnecessary duplication, please check whether there is a previous issue before filing a new one.

It is recommended to start a discussion thread in the [mailing lists](http://rocketmq.apache.org/about/contact/) in cases of discussing your deployment plan, API clarification, and other non-bug-reporting issues.
We welcome any friendly suggestions, bug fixes, collaboration, and other improvements.

Please ensure that your bug report is clear and self-contained. Otherwise, it would take additional rounds of communication, thus more time, to understand the problem itself.

Generally, fixing an issue goes through the following steps:
1. Understand the issue reported;
1. Reproduce the unexpected behavior locally;
1. Perform root cause analysis to identify the underlying problem;
1. Create test cases to cover the identified problem;
1. Work out a solution to rectify the behavior and make the newly created test cases pass;
1. Make a pull request and go through peer review;

As a result, it would be very helpful yet challenging if you could provide an isolated project reproducing your reported issue. Anyway, please ensure your issue report is informative enough for the community to pick up. At a minimum, include the following hints:

**BUG REPORT**

1. Please describe the issue you observed:

1. start controller embedded namesrv
2. start broker with controller model （172.30.42.116:30931）
3. shutdown namesrv
4.  shutdown broker (172.30.42.116:30931)
5. start controller embedded namesrv again, 
6.  start broker with controller model(172.30.42.116:30911). SyncStateInfo value as following:
![image](https://user-images.githubusercontent.com/15797831/205018953-c0e219ab-2f88-4ced-8de5-805f8b6b1499.png)
ReplicasInfoManager#registerBroker not check this master is alive.
```java
            if (syncStateInfo.isMasterExist()) {
                // If the master is alive, just return master info.
                final String masterAddress = syncStateInfo.getMasterAddress();
                response.setMasterAddress(masterAddress);
                return result;
            } else {
                // If the master is not alive, we should elect a new master:
                // Case1: This replicas was in sync state set list
                // Case2: The option {EnableElectUncleanMaster} is true
                canBeElectedAsMaster = syncStateInfo.getSyncStateSet().contains(brokerAddress)
                    || this.controllerConfig.isEnableElectUncleanMaster();
            }
```

7. Please tell us about your environment:
env: develop
8. Other information (e.g. detailed explanation, logs, related issues, suggestions on how to fix, etc):

**FEATURE REQUEST**

1. Please describe the feature you are requesting.

2. Provide any additional detail on your proposed use case for this feature.

2. Indicate the importance of this issue to you (blocker, must-have, should-have, nice-to-have). Are you currently using any workarounds to address this issue?

9. If there are some sub-tasks involved, use -[] for each sub-task and create a corresponding issue to map to the sub-task:

- [sub-task1-issue-number](example_sub_issue1_link_here): sub-task1 description here, 
- [sub-task2-issue-number](example_sub_issue2_link_here): sub-task2 description here,
- ...


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/apache__rocketmq-5633/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/apache__rocketmq-5633/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/apache__rocketmq-5633/bin/envrun 'git status --short && ls'
Edits you make under /work/apache__rocketmq-5633/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/apache__rocketmq-5633/repo; f=$(find . -name ReplicasInfoManager.java); echo $f; cat $f; grep -rn "registerBroker(" --include=*.java controller | grep -v "^.*test"
```

tool result:

```
./controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.rocketmq.controller.impl.manager;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.function.BiPredicate;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import org.apache.commons.lang3.StringUtils;
import org.apache.rocketmq.common.ControllerConfig;
import org.apache.rocketmq.common.MixAll;
import org.apache.rocketmq.common.constant.LoggerName;
import org.apache.rocketmq.controller.elect.ElectPolicy;
import org.apache.rocketmq.controller.impl.event.AlterSyncStateSetEvent;
import org.apache.rocketmq.controller.impl.event.ApplyBrokerIdEvent;
import org.apache.rocketmq.controller.impl.event.CleanBrokerDataEvent;
import org.apache.rocketmq.controller.impl.event.ControllerResult;
import org.apache.rocketmq.controller.impl.event.ElectMasterEvent;
import org.apache.rocketmq.controller.impl.event.EventMessage;
import org.apache.rocketmq.controller.impl.event.EventType;
import org.apache.rocketmq.logging.org.slf4j.Logger;
import org.apache.rocketmq.logging.org.slf4j.LoggerFactory;
import org.apache.rocketmq.remoting.protocol.ResponseCode;
import org.apache.rocketmq.remoting.protocol.body.BrokerMemberGroup;
import org.apache.rocketmq.remoting.protocol.body.InSyncStateData;
import org.apache.rocketmq.remoting.protocol.body.SyncStateSet;
import org.apache.rocketmq.remoting.protocol.header.controller.AlterSyncStateSetRequestHeader;
import org.apache.rocketmq.remoting.protocol.header.controller.AlterSyncStateSetResponseHeader;
import org.apache.rocketmq.remoting.protocol.header.controller.CleanControllerBrokerDataRequestHeader;
import org.apache.rocketmq.remoting.protocol.header.controller.ElectMasterRequestHeader;
import org.apache.rocketmq.remoting.protocol.header.controller.ElectMasterResponseHeader;
import org.apache.rocketmq.remoting.protocol.header.controller.GetReplicaInfoRequestHeader;
import org.apache.rocketmq.remoting.protocol.header.controller.GetReplicaInfoResponseHeader;
import org.apache.rocketmq.remoting.protocol.header.controller.RegisterBrokerToControllerRequestHeader;
import org.apache.rocketmq.remoting.protocol.header.controller.RegisterBrokerToControllerResponseHeader;

/**
 * The manager that manages the replicas info for all brokers. We can think of this class as the controller's memory
 * state machine It should be noted that this class is not thread safe, and the upper layer needs to ensure that it can
 * be called sequentially
 */
public class ReplicasInfoManager {
    private static final Logger log = LoggerFactory.getLogger(LoggerName.CONTROLLER_LOGGER_NAME);
    private final ControllerConfig controllerConfig;
    private final Map<String/* brokerName */, BrokerInfo> replicaInfoTable;
    private final Map<String/* brokerName */, SyncStateInfo> syncStateSetInfoTable;

    public ReplicasInfoManager(final ControllerConfig config) {
        this.controllerConfig = config;
        this.replicaInfoTable = new HashMap<>();
        this.syncStateSetInfoTable = new HashMap<>();
    }

    public ControllerResult<AlterSyncStateSetResponseHeader> alterSyncStateSet(
        final AlterSyncStateSetRequestHeader request, final SyncStateSet syncStateSet,
        final BiPredicate<String, String> brokerAlivePredicate) {
        final String brokerName = request.getBrokerName();
        final ControllerResult<AlterSyncStateSetResponseHeader> result = new ControllerResult<>(new AlterSyncStateSetResponseHeader());
        final AlterSyncStateSetResponseHeader response = result.getResponse();

        if (isContainsBroker(brokerName)) {
            final Set<String> newSyncStateSet = syncStateSet.getSyncStateSet();
            final SyncStateInfo syncStateInfo = this.syncStateSetInfoTable.get(brokerName);
            final BrokerInfo brokerInfo = this.replicaInfoTable.get(brokerName);

            // Check whether the oldSyncStateSet is equal with newSyncStateSet
            final Set<String> oldSyncStateSet = syncStateInfo.getSyncStateSet();
            if (oldSyncStateSet.size() == newSyncStateSet.size() && oldSyncStateSet.containsAll(newSyncStateSet)) {
                String err = "The newSyncStateSet is equal with oldSyncStateSet, no needed to update syncStateSet";
                log.warn("{}", err);
                result.setCodeAndRemark(ResponseCode.CONTROLLER_ALTER_SYNC_STATE_SET_FAILED, err);
                return result;
            }

            // Check master
            if (!syncStateInfo.getMasterAddress().equals(request.getMasterAddress())) {
                String err = String.format("Rejecting alter syncStateSet request because the current leader is:{%s}, not {%s}",
                    syncStateInfo.getMasterAddress(), request.getMasterAddress());
                log.error("{}", err);
                result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_MASTER, err);
                return result;
            }

            // Check master epoch
            if (request.getMasterEpoch() != syncStateInfo.getMasterEpoch()) {
            
[... 19932 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; grep -rn "registerBroker(" controller/src | grep -v "^\S*namesrv"; grep -rn "registerBroker\|DefaultBrokerHeartbeatManager\|isBrokerActive\|brokerAlivePredicate" controller/src/main/java/org/apache/rocketmq/controller/impl/DLedgerController.java | head -30
```

tool result:

```
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:79:        final ControllerResult<RegisterBrokerToControllerResponseHeader> registerResult = this.replicasInfoManager.registerBroker(registerRequest);
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:128:        this.heartbeatManager.registerBroker("cluster1", "broker1", "127.0.0.1:9000", 1L, 10000000000L, null,
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:130:        this.heartbeatManager.registerBroker("cluster1", "broker1", "127.0.0.1:9001", 1L, 10000000000L, null,
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:132:        this.heartbeatManager.registerBroker("cluster1", "broker1", "127.0.0.1:9002", 1L, 10000000000L, null,
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:137:        this.heartbeatManager.registerBroker("cluster1", "broker1", "127.0.0.1:9000", 1L, -10000L, null,
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:139:        this.heartbeatManager.registerBroker("cluster1", "broker1", "127.0.0.1:9001", 1L, 10000000000L, null,
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:141:        this.heartbeatManager.registerBroker("cluster1", "broker1", "127.0.0.1:9002", 1L, 10000000000L, null,
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:146:        this.heartbeatManager.registerBroker("cluster1", "broker1", "127.0.0.1:9000", 1L, -10000L, null,
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:148:        this.heartbeatManager.registerBroker("cluster1", "broker1", "127.0.0.1:9001", 1L, 10000000000L, null,
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:150:        this.heartbeatManager.registerBroker("cluster1", "broker1", "127.0.0.1:9002", 1L, 10000000000L, null,
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:155:        this.heartbeatManager.registerBroker("cluster1", "broker1", "127.0.0.1:9000", 1L, -10000L, null,
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:157:        this.heartbeatManager.registerBroker("cluster1", "broker1", "127.0.0.1:9001", 1L, 10000000000L, null,
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:159:        this.heartbeatManager.registerBroker("cluster1", "broker1", "127.0.0.1:9002", 1L, 10000000000L, null,
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/DefaultBrokerHeartbeatManagerTest.java:46:        this.heartbeatManager.registerBroker("cluster1", "broker1", "127.0.0.1:7000", 1L, 3000L, null, 1, 1L, 0);
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/DLedgerControllerTest.java:103:                final RemotingCommand responseInner = leader.registerBroker(registerRequest).get(2, TimeUnit.SECONDS);
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/DLedgerControllerTest.java:246:        final RegisterBrokerToControllerResponseHeader r1 = (RegisterBrokerToControllerResponseHeader) leader.registerBroker(request1).get(10, TimeUnit.SECONDS).readCustomHeader();
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/DLedgerControllerTest.java:254:        final RegisterBrokerToControllerResponseHeader r2 = (RegisterBrokerToControllerResponseHeader) leader.registerBroker(request2).get(10, TimeUnit.SECONDS).readCustomHeader();
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/ControllerManagerTest.java:126:    public RegisterBrokerToControllerResponseHeader registerBroker(
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/ControllerManagerTest.java:155:        final RegisterBrokerToControllerResponseHeader responseHeader1 = registerBroker(leaderAddr, "cluster1", "broker1", "127.0.0.1:8000", this.remotingClient, 1000L);
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/ControllerManagerTest.java:159:        final RegisterBrokerToControllerResponseHeader responseHeader2 = registerBroker(leaderAddr, "cluster1", "broker1", "127.0.0.1:8001", this.remotingClient1, 4000L);
controller/src/main/java/org/apache/rocketmq/controller/impl/DLedgerController.java:167:    public CompletableFuture<RemotingCommand> registerBroker(RegisterBrokerToControllerRequestHeader request) {
controller/src/main/java/org/apache/rocketmq/controller/impl/DLedgerController.java:169:            () -> this.replicasInfoManager.registerBroker(request), true);
controller/src/main/java/org/apache/rocketmq/controller/impl/DefaultBrokerHeartbeatManager.java:103:    public void registerBroker(String clusterName, String brokerName, String brokerAddr,
controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java:218:    public ControllerResult<RegisterBrokerToControllerResponseHeader> registerBroker(
controller/src/main/java/org/apache/rocketmq/controller/processor/ControllerRequestProcessor.java:111:                final CompletableFuture<RemotingCommand> future = this.controllerManager.getController().registerBroker(controllerRequest);
controller/src/main/java/org/apache/rocketmq/controller/processor/ControllerRequestProcessor.java:116:                        this.heartbeatManager.registerBroker(controllerRequest.getClusterName(), controllerRequest.getBrokerName(), controllerRequest.getBrokerAddress(),
controll
[... 2473 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; sed -n 60,130p controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/DLedgerControllerTest.java; sed -n 225,275p controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/DLedgerControllerTest.java
```

tool result:

```
    public DLedgerController launchController(final String group, final String peers, final String selfId,
        String storeType, final boolean isEnableElectUncleanMaster) {
        String tmpdir = System.getProperty("java.io.tmpdir");
        final String path = (StringUtils.endsWith(tmpdir, File.separator) ? tmpdir : tmpdir + File.separator) + group + File.separator + selfId;
        baseDirs.add(path);

        final ControllerConfig config = new ControllerConfig();
        config.setControllerDLegerGroup(group);
        config.setControllerDLegerPeers(peers);
        config.setControllerDLegerSelfId(selfId);
        config.setControllerStorePath(path);
        config.setMappedFileSize(10 * 1024 * 1024);
        config.setEnableElectUncleanMaster(isEnableElectUncleanMaster);

        final DLedgerController controller = new DLedgerController(config, (str1, str2) -> true);

        controller.startup();
        return controller;
    }

    @Before
    public void startup() {
        this.baseDirs = new ArrayList<>();
        this.controllers = new ArrayList<>();
    }

    @After
    public void tearDown() {
        for (Controller controller : this.controllers) {
            controller.shutdown();
        }
        for (String dir : this.baseDirs) {
            new File(dir).delete();
        }
    }

    public boolean registerNewBroker(Controller leader, String clusterName, String brokerName, String brokerAddress,
        boolean isFirstRegisteredBroker) throws Exception {
        // Register new broker
        final RegisterBrokerToControllerRequestHeader registerRequest = new RegisterBrokerToControllerRequestHeader(clusterName, brokerName, brokerAddress);
        RemotingCommand response = await().atMost(Duration.ofSeconds(20)).until(() -> {
            try {
                final RemotingCommand responseInner = leader.registerBroker(registerRequest).get(2, TimeUnit.SECONDS);
                if (responseInner == null || responseInner.getCode() != ResponseCode.SUCCESS) {
                    return null;
                }
                return responseInner;
            } catch (Exception e) {
                e.printStackTrace();
                return null;
            }
        }, item -> item != null);

        final RegisterBrokerToControllerResponseHeader registerResult = (RegisterBrokerToControllerResponseHeader) response.readCustomHeader();

        if (!isFirstRegisteredBroker) {
            assertTrue(registerResult.getBrokerId() > 0);
        }
        return true;
    }

    private boolean alterNewInSyncSet(Controller leader, String brokerName, String masterAddress, int masterEpoch,
        Set<String> newSyncStateSet, int syncStateSetEpoch) throws Exception {
        final AlterSyncStateSetRequestHeader alterRequest =
            new AlterSyncStateSetRequestHeader(brokerName, masterAddress, masterEpoch);
        final RemotingCommand response = leader.alterSyncStateSet(alterRequest, new SyncStateSet(newSyncStateSet, syncStateSetEpoch)).get(10, TimeUnit.SECONDS);
        if (null == response || response.getCode() != ResponseCode.SUCCESS) {
            return false;
        }
        final RemotingCommand getInfoResponse = leader.getReplicaInfo(new GetReplicaInfoRequestHeader(brokerName)).get(10, TimeUnit.SECONDS);
        newSyncStateSet.add("127.0.0.1:9000");

        assertTrue(alterNewInSyncSet(leader, "broker1", "127.0.0.1:9000", 1, newSyncStateSet, 2));

        // Now we trigger electMaster api, which means the old master is shutdown and want to elect a new master.
        // However, the syncStateSet in statemachine is {"127.0.0.1:9000"}, not more replicas can be elected as master, it will be failed.
        final ElectMasterRequestHeader electRequest = new ElectMasterRequestHeader("broker1");
        setBrokerElectPolicy(leader, "127.0.0.1:9000");
        leader.electMaster(electRequest).get(10, TimeUnit.SECONDS);

        final RemotingCommand resp = leader.getReplicaInfo(new GetReplicaInfoRequestHeader("broker1")).
            get(10, TimeUnit.SECONDS);
        final GetReplicaInfoResponseHeader replicaInfo = (GetReplicaInfoResponseHeader) resp.readCustomHeader();
        final SyncStateSet syncStateSet = RemotingSerializable.decode(resp.getBody(), SyncStateSet.class);
        assertEquals(syncStateSet.getSyncStateSet(), newSyncStateSet);
        assertEquals(replicaInfo.getMasterAddress(), "");
        assertEquals(replicaInfo.getMasterEpoch(), 2);

        // Now, we start broker1 - 127.0.0.1:9001, but it was not in syncStateSet, so it will not be elected as master.
        final RegisterBrokerToControllerRequestHeader request1 =
            new RegisterBrokerToControllerRequestHeader("cluster1", "broker1", "127.0.0.1:9001");
        final RegisterBrokerToControllerResponseHeader r1 = (RegisterBrokerToControllerResponseHeader) leader.registerBroker(request1).get(10, TimeUnit.SECONDS).readCustomHeader();
        assertEquals(r1.getBrokerId(), 2);
        assertEquals(r1.getMasterAddress(), "");
        assertEquals(r1.getMasterEpoch(), 2);

        // Now, we start broker1 - 127.0.0.1:9000, it will be elected as master
        final RegisterBrokerToControllerRequestHeader request2 =
            new RegisterBrokerToControllerRequestHeader("cluster1", "broker1", "127.0.0.1:9000");
        final RegisterBrokerToControllerResponseHeader r2 = (RegisterBrokerToControllerResponseHeader) leader.registerBroker(request2).get(10, TimeUnit.SECONDS).readCustomHeader();
        assertEquals(r2.getBrokerId(), 0);
        assertEquals(r2.getMasterAddress(), "127.0.0.1:9000");
        assertEquals(r2.getMasterEpoch(), 3);
    }

    @Test
    public void testEnableElectUnCleanMaster() throws Exception {
        final DLedgerController leader = mockMetaData(true);
        final HashSet<String> newSyncStateSet = new HashSet<>();
        newSyncStateSet.add("127.0.0.1:9000");

        assertTrue(alterNewInSyncSet(leader, "broker1", "127.0.0.1:9000", 1, newSyncStateSet, 2));

[... 586 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; python3 - <<'EOF'
p='controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java'
s=open(p).read()
s=s.replace("""    public ControllerResult<RegisterBrokerToControllerResponseHeader> registerBroker(
        final RegisterBrokerToControllerRequestHeader request) {
""","""    public ControllerResult<RegisterBrokerToControllerResponseHeader> registerBroker(
        final RegisterBrokerToControllerRequestHeader request) {
        return registerBroker(request, (clusterName, brokerAddress) -> true);
    }

    public ControllerResult<RegisterBrokerToControllerResponseHeader> registerBroker(
        final RegisterBrokerToControllerRequestHeader request, final BiPredicate<String, String> brokerAlivePredicate) {
""",1)
s=s.replace("""            if (syncStateInfo.isMasterExist()) {
                // If the master is alive, just return master info.""","""            if (syncStateInfo.isMasterExist() && brokerAlivePredicate.test(brokerInfo.getClusterName(), syncStateInfo.getMasterAddress())) {
                // If the master is alive, just return master info.""",1)
open(p,'w').write(s)
p='controller/src/main/java/org/apache/rocketmq/controller/impl/DLedgerController.java'
s=open(p).read()
s=s.replace("this.replicasInfoManager.registerBroker(request)","this.replicasInfoManager.registerBroker(request, this.brokerAlivePredicate)")
open(p,'w').write(s)
EOF
git diff
```

tool result:

```
diff --git a/controller/src/main/java/org/apache/rocketmq/controller/impl/DLedgerController.java b/controller/src/main/java/org/apache/rocketmq/controller/impl/DLedgerController.java
index 71e8e465c..fab4f6005 100644
--- a/controller/src/main/java/org/apache/rocketmq/controller/impl/DLedgerController.java
+++ b/controller/src/main/java/org/apache/rocketmq/controller/impl/DLedgerController.java
@@ -166,7 +166,7 @@ public class DLedgerController implements Controller {
     @Override
     public CompletableFuture<RemotingCommand> registerBroker(RegisterBrokerToControllerRequestHeader request) {
         return this.scheduler.appendEvent("registerBroker",
-            () -> this.replicasInfoManager.registerBroker(request), true);
+            () -> this.replicasInfoManager.registerBroker(request, this.brokerAlivePredicate), true);
     }
 
     @Override
diff --git a/controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java b/controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java
index 02ea9a6b6..0bda63e71 100644
--- a/controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java
+++ b/controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java
@@ -217,6 +217,11 @@ public class ReplicasInfoManager {
 
     public ControllerResult<RegisterBrokerToControllerResponseHeader> registerBroker(
         final RegisterBrokerToControllerRequestHeader request) {
+        return registerBroker(request, (clusterName, brokerAddress) -> true);
+    }
+
+    public ControllerResult<RegisterBrokerToControllerResponseHeader> registerBroker(
+        final RegisterBrokerToControllerRequestHeader request, final BiPredicate<String, String> brokerAlivePredicate) {
         final String brokerName = request.getBrokerName();
         final String brokerAddress = request.getBrokerAddress();
         final ControllerResult<RegisterBrokerToControllerResponseHeader> result = new ControllerResult<>(new RegisterBrokerToControllerResponseHeader());
@@ -240,7 +245,7 @@ public class ReplicasInfoManager {
             response.setMasterEpoch(syncStateInfo.getMasterEpoch());
             response.setSyncStateSetEpoch(syncStateInfo.getSyncStateSetEpoch());
 
-            if (syncStateInfo.isMasterExist()) {
+            if (syncStateInfo.isMasterExist() && brokerAlivePredicate.test(brokerInfo.getClusterName(), syncStateInfo.getMasterAddress())) {
                 // If the master is alive, just return master info.
                 final String masterAddress = syncStateInfo.getMasterAddress();
                 response.setMasterAddress(masterAddress);
diff --git a/pom.xml b/pom.xml
index 197cea783..fa8cce2b9 100644
--- a/pom.xml
+++ b/pom.xml
@@ -383,7 +383,7 @@
                     <forkCount>1</forkCount>
                     <reuseForks>true</reuseForks>
                     <excludes>
-                        <exclude>**/IT*.java</exclude>
+<exclude>**/IT*.java</exclude><exclude>%regex[.*MixCommitlogTest.*]</exclude>
                     </excludes>
                 </configuration>
             </plugin>
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; sed -n 100,130p controller/src/main/java/org/apache/rocketmq/controller/processor/ControllerRequestProcessor.java
```

tool result:

```
                        }
                        if (this.controllerManager.getControllerConfig().isNotifyBrokerRoleChanged()) {
                            this.controllerManager.notifyBrokerRoleChanged(responseHeader, electMasterRequest.getClusterName());
                        }
                    }
                    return response;
                }
                break;
            }
            case CONTROLLER_REGISTER_BROKER: {
                final RegisterBrokerToControllerRequestHeader controllerRequest = (RegisterBrokerToControllerRequestHeader) request.decodeCommandCustomHeader(RegisterBrokerToControllerRequestHeader.class);
                final CompletableFuture<RemotingCommand> future = this.controllerManager.getController().registerBroker(controllerRequest);
                if (future != null) {
                    final RemotingCommand response = future.get(WAIT_TIMEOUT_OUT, TimeUnit.SECONDS);
                    final RegisterBrokerToControllerResponseHeader responseHeader = (RegisterBrokerToControllerResponseHeader) response.readCustomHeader();
                    if (responseHeader != null && responseHeader.getBrokerId() >= 0) {
                        this.heartbeatManager.registerBroker(controllerRequest.getClusterName(), controllerRequest.getBrokerName(), controllerRequest.getBrokerAddress(),
                                                             responseHeader.getBrokerId(), controllerRequest.getHeartbeatTimeoutMillis(), ctx.channel(),
                                                             controllerRequest.getEpoch(), controllerRequest.getMaxOffset(), controllerRequest.getElectionPriority());
                    }
                    return response;
                }
                break;
            }
            case CONTROLLER_GET_REPLICA_INFO: {
                final GetReplicaInfoRequestHeader controllerRequest = (GetReplicaInfoRequestHeader) request.decodeCommandCustomHeader(GetReplicaInfoRequestHeader.class);
                final CompletableFuture<RemotingCommand> future = this.controllerManager.getController().getReplicaInfo(controllerRequest);
                if (future != null) {
                    return future.get(WAIT_TIMEOUT_OUT, TimeUnit.SECONDS);
                }
                break;
```

**thinking:**

```
I've updated `registerBroker` to take a broker-alive predicate and wired it into `DLedgerController`. Now I'll write a temporary test reproducing the issue's scenario and run the controller module's tests.


```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; cat > controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/TmpReproTest.java <<'EOF'
package org.apache.rocketmq.controller.impl.controller.impl.manager;

import org.apache.rocketmq.common.ControllerConfig;
import org.apache.rocketmq.controller.impl.event.ControllerResult;
import org.apache.rocketmq.controller.impl.manager.ReplicasInfoManager;
import org.apache.rocketmq.remoting.protocol.header.controller.RegisterBrokerToControllerRequestHeader;
import org.apache.rocketmq.remoting.protocol.header.controller.RegisterBrokerToControllerResponseHeader;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TmpReproTest {
    @Test
    public void test() {
        ControllerConfig config = new ControllerConfig();
        ReplicasInfoManager m = new ReplicasInfoManager(config);
        ControllerResult<RegisterBrokerToControllerResponseHeader> r = m.registerBroker(new RegisterBrokerToControllerRequestHeader("c", "b", "a:30931"), (c, a) -> true);
        r.getEvents().forEach(m::applyEvent);
        // old master a:30931 is dead now; register a:30911
        r = m.registerBroker(new RegisterBrokerToControllerRequestHeader("c", "b", "a:30911"), (c, a) -> a.equals("a:30911"));
        assertEquals("", r.getResponse().getMasterAddress());
        config.setEnableElectUncleanMaster(true);
        r = m.registerBroker(new RegisterBrokerToControllerRequestHeader("c", "b", "a:30911"), (c, a) -> a.equals("a:30911"));
        assertEquals("a:30911", r.getResponse().getMasterAddress());
        r.getEvents().forEach(m::applyEvent);
        r = m.registerBroker(new RegisterBrokerToControllerRequestHeader("c", "b", "a:30931"), (c, a) -> true);
        assertEquals("a:30911", r.getResponse().getMasterAddress());
    }
}
EOF
../bin/envrun 'mvn -o -q install -DskipTests -pl controller -am > /tmp/b.log 2>&1; tail -20 /tmp/b.log; mvn -o test -pl controller -Dtest="TmpReproTest,ReplicasInfoManagerTest,DLedgerControllerTest,ControllerManagerTest" -DfailIfNoTests=false 2>&1 | grep -E "Tests run|FAIL|ERROR" | head -30'
```

tool result:

```
     [java] JVM args ignored when same JVM is used.
     [java] JVM args ignored when same JVM is used.
     [java] JVM args ignored when same JVM is used.
     [java] JVM args ignored when same JVM is used.
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-checkstyle-plugin:3.2.0:check (validate) on project rocketmq-controller: Failed during checkstyle execution: There is 1 error reported by Checkstyle 9.3 with style/rmq_checkstyle.xml ruleset. -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoExecutionException
[ERROR] 
[ERROR] After correcting the problems, you can resume the build with the command
[ERROR]   mvn <args> -rf :rocketmq-controller
[ERROR] /testbed/controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/TmpReproTest.java:1: Line does not match expected header line of '/\*'. [RegexpHeader]
[INFO] BUILD FAILURE
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-checkstyle-plugin:3.2.0:check (validate) on project rocketmq-controller: Failed during checkstyle execution: There is 1 error reported by Checkstyle 9.3 with style/rmq_checkstyle.xml ruleset. -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoExecutionException
```

**assistant:** Checkstyle rejected the temp test because it has no license header. I'll skip checkstyle for this run.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; ../bin/envrun 'mvn -o -q install -DskipTests -Dcheckstyle.skip -pl controller -am > /tmp/b.log 2>&1; grep ERROR /tmp/b.log | head; mvn -o test -Dcheckstyle.skip -pl controller -Dtest="TmpReproTest,ReplicasInfoManagerTest,DLedgerControllerTest,ControllerManagerTest" -DfailIfNoTests=false 2>&1 | grep -E "Tests run|FAIL|ERROR" | head -30'
```

tool result:

```
[INFO] BUILD FAILURE
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:2.19.1:test (default-test) on project rocketmq-controller: Unable to generate classpath: org.apache.maven.artifact.resolver.MultipleArtifactsNotFoundException: Missing:
[ERROR] ----------
[ERROR] 1) org.apache.maven.surefire:surefire-junit4:jar:2.19.1
[ERROR] 
[ERROR]   Try downloading the file manually from the project website.
[ERROR] 
[ERROR]   Then, install it using the command: 
[ERROR]       mvn install:install-file -DgroupId=org.apache.maven.surefire -DartifactId=surefire-junit4 -Dversion=2.19.1 -Dpackaging=jar -Dfile=/path/to/file
[ERROR] 
[ERROR]   Alternatively, if you host your own repository you can deploy the file there: 
[ERROR]       mvn deploy:deploy-file -DgroupId=org.apache.maven.surefire -DartifactId=surefire-junit4 -Dversion=2.19.1 -Dpackaging=jar -Dfile=/path/to/file -Durl=[url] -DrepositoryId=[id]
[ERROR] 
[ERROR]   Path to dependency: 
[ERROR]   	1) dummy:dummy:jar:1.0
[ERROR]   	2) org.apache.maven.surefire:surefire-junit4:jar:2.19.1
[ERROR] 
[ERROR] ----------
[ERROR] 1 required artifact is missing.
[ERROR] 
[ERROR] for artifact: 
[ERROR]   dummy:dummy:jar:1.0
[ERROR] 
[ERROR] from the specified remote repositories:
[ERROR]   central (https://repo.maven.apache.org/maven2, releases=true, snapshots=false)
[ERROR] 
[ERROR] -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
```

**assistant:** The build works, but the offline Maven cache is missing the JUnit 4 test runner plugin. I'll check which test runners are cached.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; ../bin/envrun 'ls ~/.m2/repository/org/apache/maven/surefire/; ls ~/.m2/repository/org/apache/maven/surefire/surefire-junit*/ 2>/dev/null'
```

tool result:

```
Exit code 2
maven-surefire-common
surefire
surefire-api
surefire-booter
```

**assistant:** Maven can't run the tests offline, so I'll run JUnit directly with the module's test classpath.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; ../bin/envrun 'cd controller && mvn -o -q dependency:build-classpath -Dmdep.outputFile=/tmp/cp.txt >/dev/null 2>&1; mvn -o -q test-compile -Dcheckstyle.skip 2>&1 | grep ERROR | head; CP=target/classes:target/test-classes:$(cat /tmp/cp.txt); timeout 500 java -cp $CP org.junit.runner.JUnitCore org.apache.rocketmq.controller.impl.controller.impl.manager.TmpReproTest org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest org.apache.rocketmq.controller.impl.controller.ControllerManagerTest 2>&1 | grep -vE "^\s+at |INFO|WARN|DEBUG" | tail -30'
```

tool result:

```
cat: /tmp/cp.txt: No such file or directory
Error: Could not find or load main class org.junit.runner.JUnitCore
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; ../bin/envrun 'cd controller && mvn -o dependency:build-classpath -Dmdep.outputFile=/tmp/cp.txt 2>&1 | grep -E "ERROR|BUILD" | head -5'
```

tool result:

```
[INFO] BUILD FAILURE
[ERROR] No plugin found for prefix 'dependency' in the current project and in the plugin groups [org.apache.maven.plugins, org.codehaus.mojo] available from the repositories [local (/root/.m2/repository), central (https://repo.maven.apache.org/maven2)] -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
```

**assistant:** The dependency plugin isn't cached either. I'll build the classpath from every jar in the local Maven repo instead.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; ../bin/envrun 'cd controller && CP=target/classes:target/test-classes:$(for m in common remoting srvutil client tools logging namesrv; do printf "../$m/target/classes:"; done)$(find ~/.m2/repository -name "*.jar" ! -path "*rocketmq*" ! -path "*maven*" ! -path "*plexus*" | tr "\n" ":"); timeout 550 java -cp $CP org.junit.runner.JUnitCore org.apache.rocketmq.controller.impl.controller.impl.manager.TmpReproTest org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest org.apache.rocketmq.controller.impl.controller.ControllerManagerTest 2>&1 | grep -vE "^\s+at |INFO|WARN|DEBUG" | tail -30'
```

tool result:

```
12) testElectMasterOldMasterStillAlive(org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest)
java.lang.NoClassDefFoundError: Could not initialize class org.apache.rocketmq.controller.impl.manager.ReplicasInfoManager
13) testElectMasterOldMasterStillAlive(org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest)
java.lang.NullPointerException
14) testElectMasterPreferHigherPriorityWhenEpochAndOffsetEquals(org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest)
java.lang.NoClassDefFoundError: Could not initialize class org.apache.rocketmq.controller.impl.manager.ReplicasInfoManager
15) testElectMasterPreferHigherPriorityWhenEpochAndOffsetEquals(org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest)
java.lang.NullPointerException
16) testEnableElectUnCleanMaster(org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest)
java.lang.NoClassDefFoundError: org/apache/rocketmq/logging/org/slf4j/LoggerFactory
	... 34 trimmed
Caused by: java.lang.ClassNotFoundException: org.apache.rocketmq.logging.org.slf4j.LoggerFactory
	... 39 more
17) testElectMaster(org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest)
java.lang.NoClassDefFoundError: Could not initialize class org.apache.rocketmq.controller.impl.DLedgerController
18) testChangeControllerLeader(org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest)
java.lang.NoClassDefFoundError: Could not initialize class org.apache.rocketmq.controller.impl.DLedgerController
19) testAllReplicasShutdownAndRestartWithUnEnableElectUnCleanMaster(org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest)
java.lang.NoClassDefFoundError: Could not initialize class org.apache.rocketmq.controller.impl.DLedgerController
20) testSomeApi(org.apache.rocketmq.controller.impl.controller.ControllerManagerTest)
java.lang.NoClassDefFoundError: org/apache/rocketmq/logging/org/slf4j/LoggerFactory
	... 34 trimmed
Caused by: java.lang.ClassNotFoundException: org.apache.rocketmq.logging.org.slf4j.LoggerFactory
	... 37 more
21) testSomeApi(org.apache.rocketmq.controller.impl.controller.ControllerManagerTest)
java.lang.NullPointerException

FAILURES!!!
Tests run: 13,  Failures: 21
```

**assistant:** The shaded logging jar is still missing. I'll add the `rocketmq-logger` and `dledger` jars back.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; ../bin/envrun 'cd controller && CP=target/classes:target/test-classes:$(for m in common remoting srvutil client tools logging namesrv; do printf "../$m/target/classes:"; done)$(find ~/.m2/repository -name "*.jar" \( ! -path "*rocketmq*" -o -path "*rocketmq-shaded*" -o -path "*logger*" -o -path "*dledger*" \) ! -path "*/rocketmq/rocketmq-*5.*" ! -path "*maven*" ! -path "*plexus*" | tr "\n" ":"); timeout 550 java -cp $CP org.junit.runner.JUnitCore org.apache.rocketmq.controller.impl.controller.impl.manager.TmpReproTest org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest org.apache.rocketmq.controller.impl.controller.ControllerManagerTest 2>&1 | grep -vE "^\s+at |INFO|WARN|DEBUG" | tail -30'
```

tool result:

```
12) testElectMasterOldMasterStillAlive(org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest)
java.lang.NoClassDefFoundError: Could not initialize class org.apache.rocketmq.controller.impl.manager.ReplicasInfoManager
13) testElectMasterOldMasterStillAlive(org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest)
java.lang.NullPointerException
14) testElectMasterPreferHigherPriorityWhenEpochAndOffsetEquals(org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest)
java.lang.NoClassDefFoundError: Could not initialize class org.apache.rocketmq.controller.impl.manager.ReplicasInfoManager
15) testElectMasterPreferHigherPriorityWhenEpochAndOffsetEquals(org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest)
java.lang.NullPointerException
16) testEnableElectUnCleanMaster(org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest)
java.lang.NoClassDefFoundError: org/apache/rocketmq/logging/org/slf4j/LoggerFactory
	... 34 trimmed
Caused by: java.lang.ClassNotFoundException: org.apache.rocketmq.logging.org.slf4j.LoggerFactory
	... 39 more
17) testElectMaster(org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest)
java.lang.NoClassDefFoundError: Could not initialize class org.apache.rocketmq.controller.impl.DLedgerController
18) testChangeControllerLeader(org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest)
java.lang.NoClassDefFoundError: Could not initialize class org.apache.rocketmq.controller.impl.DLedgerController
19) testAllReplicasShutdownAndRestartWithUnEnableElectUnCleanMaster(org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest)
java.lang.NoClassDefFoundError: Could not initialize class org.apache.rocketmq.controller.impl.DLedgerController
20) testSomeApi(org.apache.rocketmq.controller.impl.controller.ControllerManagerTest)
java.lang.NoClassDefFoundError: org/apache/rocketmq/logging/org/slf4j/LoggerFactory
	... 34 trimmed
Caused by: java.lang.ClassNotFoundException: org.apache.rocketmq.logging.org.slf4j.LoggerFactory
	... 37 more
21) testSomeApi(org.apache.rocketmq.controller.impl.controller.ControllerManagerTest)
java.lang.NullPointerException

FAILURES!!!
Tests run: 13,  Failures: 21
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; ../bin/envrun 'grep -rl "org/apache/rocketmq/logging/org/slf4j/LoggerFactory" ~/.m2/repository --include=*.jar 2>/dev/null | head; for j in $(find ~/.m2/repository -path "*rocketmq*" -name "*.jar"); do unzip -l $j 2>/dev/null | grep -q "logging/org/slf4j/LoggerFactory.class" && echo $j; done'
```

tool result:

```
Exit code 1
/root/.m2/repository/io/github/aliyunmq/rocketmq-logback-classic/1.0.0/rocketmq-logback-classic-1.0.0.jar
/root/.m2/repository/io/github/aliyunmq/rocketmq-slf4j-api/1.0.0/rocketmq-slf4j-api-1.0.0.jar
/root/.m2/repository/io/github/aliyunmq/rocketmq-logback-classic/1.0.0/rocketmq-logback-classic-1.0.0.jar
/root/.m2/repository/io/github/aliyunmq/rocketmq-slf4j-api/1.0.0/rocketmq-slf4j-api-1.0.0.jar
```

**assistant:** My filter excluded the `io/github/aliyunmq` logging jars by mistake. I'll exclude only the project's own `org/apache/rocketmq/rocketmq-*` artifacts and run again.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; ../bin/envrun 'cd controller && CP=target/classes:target/test-classes:$(for m in common remoting srvutil client tools logging namesrv; do printf "../$m/target/classes:"; done)$(find ~/.m2/repository -name "*.jar" ! -path "*/org/apache/rocketmq/rocketmq-*" ! -path "*maven*" ! -path "*plexus*" | tr "\n" ":"); timeout 550 java -cp $CP org.junit.runner.JUnitCore org.apache.rocketmq.controller.impl.controller.impl.manager.TmpReproTest org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest org.apache.rocketmq.controller.impl.controller.ControllerManagerTest 2>&1 | grep -vE "^\s+at |INFO|WARN|DEBUG" | tail -30'
```

tool result:

```
JUnit version 4.13.2

........SLF4J: The requested version 1.5.6 by your slf4j binding is not compatible with [1.6, 1.7]
SLF4J: See http://www.slf4j.org/codes.html#version_mismatch for further details.
E.E.E.E.E
Time: 2.598
There were 5 failures:
1) testEnableElectUnCleanMaster(org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest)
java.lang.NoSuchMethodError: org.slf4j.helpers.MessageFormatter.format(Ljava/lang/String;Ljava/lang/Object;)Ljava/lang/String;
2) testElectMaster(org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest)
java.lang.IllegalStateException: Failed to bind to 0.0.0.0:30000
	... 34 trimmed
Caused by: java.net.BindException: Address already in use
3) testChangeControllerLeader(org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest)
java.lang.IllegalStateException: Failed to bind to 0.0.0.0:30000
	... 34 trimmed
Caused by: java.net.BindException: Address already in use
4) testAllReplicasShutdownAndRestartWithUnEnableElectUnCleanMaster(org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest)
java.lang.IllegalStateException: Failed to bind to 0.0.0.0:30000
	... 34 trimmed
Caused by: java.net.BindException: Address already in use
5) testSomeApi(org.apache.rocketmq.controller.impl.controller.ControllerManagerTest)
java.lang.IllegalStateException: Failed to bind to 0.0.0.0:30000
	... 34 trimmed
Caused by: java.net.BindException: Address already in use

FAILURES!!!
Tests run: 13,  Failures: 5
```

**thinking:**

```
My reproduction test and ReplicasInfoManagerTest pass, but DLedgerControllerTest fails due to conflicting slf4j versions in my hand-built classpath, which also triggers the port-binding errors. I'll trim the classpath to one slf4j version and rerun.


```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; ../bin/envrun 'ls ~/.m2/repository/org/slf4j/*/'
```

tool result:

```
/root/.m2/repository/org/slf4j/jcl-over-slf4j/:
1.5.6
2.0.0-alpha1

/root/.m2/repository/org/slf4j/slf4j-api/:
1.5.6
1.7.32
1.7.5
1.8.0-beta4
2.0.0-alpha1
2.0.3

/root/.m2/repository/org/slf4j/slf4j-jdk14/:
1.5.6

/root/.m2/repository/org/slf4j/slf4j-parent/:
1.5.6
1.7.32
1.7.5
1.8.0-beta4
2.0.0-alpha1
2.0.3

/root/.m2/repository/org/slf4j/slf4j-simple/:
2.0.0-alpha1
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; ../bin/envrun 'cd controller && CP=target/classes:target/test-classes:$(for m in common remoting srvutil client tools logging namesrv; do printf "../$m/target/classes:"; done)$(find ~/.m2/repository -name "*.jar" ! -path "*/org/apache/rocketmq/rocketmq-*" ! -path "*maven*" ! -path "*plexus*" ! -path "*/org/slf4j/*" | tr "\n" ":")$HOME/.m2/repository/org/slf4j/slf4j-api/1.7.32/slf4j-api-1.7.32.jar; timeout 550 java -cp $CP org.junit.runner.JUnitCore org.apache.rocketmq.controller.impl.controller.impl.manager.TmpReproTest org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest org.apache.rocketmq.controller.impl.controller.ControllerManagerTest 2>&1 | grep -vE "^\s+at |INFO|WARN|DEBUG" | tail -30'
```

tool result:

```
JUnit version 4.13.2

........SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
E.E.E.E.E
Time: 75.696
There were 5 failures:
1) testEnableElectUnCleanMaster(org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest)
java.lang.NoSuchMethodError: org.hamcrest.Matcher.describeMismatch(Ljava/lang/Object;Lorg/hamcrest/Description;)V
2) testElectMaster(org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest)
java.lang.NoSuchMethodError: org.hamcrest.Matcher.describeMismatch(Ljava/lang/Object;Lorg/hamcrest/Description;)V
3) testChangeControllerLeader(org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest)
java.lang.NoSuchMethodError: org.hamcrest.Matcher.describeMismatch(Ljava/lang/Object;Lorg/hamcrest/Description;)V
4) testAllReplicasShutdownAndRestartWithUnEnableElectUnCleanMaster(org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest)
java.lang.NoSuchMethodError: org.hamcrest.Matcher.describeMismatch(Ljava/lang/Object;Lorg/hamcrest/Description;)V
5) testSomeApi(org.apache.rocketmq.controller.impl.controller.ControllerManagerTest)
java.lang.NoSuchMethodError: org.hamcrest.Matcher.describeMismatch(Ljava/lang/Object;Lorg/hamcrest/Description;)V

FAILURES!!!
Tests run: 13,  Failures: 5
```

**thinking:**

```
The slf4j conflict is resolved, but a hamcrest version conflict is masking the real issue—an awaitility condition that timed out after 75s. I'll pin hamcrest to one version and print the full trace to confirm whether this is a genuine failure.


```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; ../bin/envrun 'ls ~/.m2/repository/org/hamcrest/*/'
```

tool result:

```
/root/.m2/repository/org/hamcrest/hamcrest-core/:
1.3

/root/.m2/repository/org/hamcrest/hamcrest-parent/:
1.3

/root/.m2/repository/org/hamcrest/hamcrest/:
2.1
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; git stash -q; git stash apply -q; git status --short
```

tool result:

```
 M controller/src/main/java/org/apache/rocketmq/controller/impl/DLedgerController.java
 M controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java
 M pom.xml
?? Dockerfile
?? controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/TmpReproTest.java
```

**assistant:** The working tree is unchanged. (`Dockerfile` and the `pom.xml` edit were there before I started.) Now I'll rerun with hamcrest 2.1 first on the classpath.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; ../bin/envrun 'cd controller && CP=$HOME/.m2/repository/org/hamcrest/hamcrest/2.1/hamcrest-2.1.jar:target/classes:target/test-classes:$(for m in common remoting srvutil client tools logging namesrv; do printf "../$m/target/classes:"; done)$(find ~/.m2/repository -name "*.jar" ! -path "*/org/apache/rocketmq/rocketmq-*" ! -path "*maven*" ! -path "*plexus*" ! -path "*/org/slf4j/*" ! -path "*hamcrest*" | tr "\n" ":")$HOME/.m2/repository/org/slf4j/slf4j-api/1.7.32/slf4j-api-1.7.32.jar; timeout 550 java -cp $CP org.junit.runner.JUnitCore org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest org.apache.rocketmq.controller.impl.controller.ControllerManagerTest 2>&1 | grep -vE "INFO|WARN|DEBUG" | grep -v "^\s*at org.junit\|reflect" | head -60'
```

tool result:

```
JUnit version 4.13.2

SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
....
Time: 82.907

OK (5 tests)
```

**assistant:** All 5 tests pass, so the earlier failures were only classpath conflicts. Now I'll remove the temporary test and its compiled classes.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5633/repo; rm controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/TmpReproTest.java; find controller/target -name "TmpReproTest*" -delete; git status --short
```

tool result:

```
 M controller/src/main/java/org/apache/rocketmq/controller/impl/DLedgerController.java
 M controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java
 M pom.xml
?? Dockerfile
```

**assistant:** I fixed the bug: when a broker registers, the controller now checks whether the recorded master is actually alive. If it isn't, the controller elects a new master instead of returning the dead one.

**Root cause:** `ReplicasInfoManager#registerBroker` only checked whether a master address was recorded in its metadata. After the namesrv/controller restart in the issue, the metadata still pointed to the old master (`172.30.42.116:30931`). That broker was gone, but the controller handed its address to the new broker anyway, so no new master was ever elected.

**Changes:**
- **`ReplicasInfoManager.java`**: added a `registerBroker(request, brokerAlivePredicate)` overload. It returns the existing master only if the master is recorded **and** the predicate says it is alive. Otherwise it uses the existing election rules: the registering broker can become master if it's in the sync state set, or if `enableElectUncleanMaster` is on. If neither applies, registration fails with an empty master address, as before.
- **`DLedgerController.java`**: `registerBroker` now passes its broker-alive predicate (the same one already used by `alterSyncStateSet` and `cleanBrokerData`).
- I kept the old one-argument `registerBroker(request)` because the current `ReplicasInfoManagerTest` still calls it. It treats every master as alive, so it keeps the old behaviour; the real controller path doesn't use it.

**Verification:**
- A temporary test reproduced the issue's scenario. With the old master dead, a new broker outside the sync state set got an empty master. With `enableElectUncleanMaster` on, it was elected master. With the master alive, the existing master was returned.
- That test, `ReplicasInfoManagerTest`, `DLedgerControllerTest` and `ControllerManagerTest` all pass. I didn't run the rest of the controller module's tests.
- Maven can't run tests offline here because the JUnit runner plugin isn't in the local cache. I ran JUnit directly with a classpath I built by hand. The first attempts failed only from slf4j and hamcrest version conflicts in that classpath; once I fixed those, everything passed.

**Behaviour change:** if a master restarts and re-registers before its heartbeat is recorded, the controller may not see it as alive. If it's in the sync state set, it gets re-elected with a higher master epoch rather than simply being returned as master. It still ends up master.

I deleted the temporary test. The diff touches only the two controller files above. The `pom.xml` change and the untracked `Dockerfile` were there before I started, and I left them alone.

_session end: success, turns 21, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 67.26 s: mvn -o -q install -DskipTests -pl controller -am > /tmp/b.log 2>&1; tail -20 /tmp/b.log; mvn -o test -pl controller -Dtest="TmpReproTest,ReplicasInfoManagerTest,DLedgerControllerTest,ControllerManagerTest" -DfailIfNoTests=false 2>&1 | grep -E "Tests run|FAIL|ERROR" | head -30
- `rc=0` 89.68 s: mvn -o -q install -DskipTests -Dcheckstyle.skip -pl controller -am > /tmp/b.log 2>&1; grep ERROR /tmp/b.log | head; mvn -o test -Dcheckstyle.skip -pl controller -Dtest="TmpReproTest,ReplicasInfoManagerTest,DLedgerControllerTest,ControllerManagerTest" -DfailIfNoTests=false 2>&1 | grep -E "Tests run|FAIL|ERROR" | head -30
- `rc=2` 0.31 s: ls ~/.m2/repository/org/apache/maven/surefire/; ls ~/.m2/repository/org/apache/maven/surefire/surefire-junit*/ 2>/dev/null
- `rc=0` 21.36 s: cd controller && mvn -o -q dependency:build-classpath -Dmdep.outputFile=/tmp/cp.txt >/dev/null 2>&1; mvn -o -q test-compile -Dcheckstyle.skip 2>&1 | grep ERROR | head; CP=target/classes:target/test-classes:$(cat /tmp/cp.txt); timeout 500 java -cp $CP org.junit.runner.JUnitCore org.apache.rocketmq.controller.impl.controller.impl.manager.TmpReproTest org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest org.apache.rocketmq.controller.impl.controller.ControllerManagerTest 2>&1 | grep -vE "^\s+a
- `rc=0` 3.36 s: cd controller && mvn -o dependency:build-classpath -Dmdep.outputFile=/tmp/cp.txt 2>&1 | grep -E "ERROR|BUILD" | head -5
- `rc=0` 1.19 s: cd controller && CP=target/classes:target/test-classes:$(for m in common remoting srvutil client tools logging namesrv; do printf "../$m/target/classes:"; done)$(find ~/.m2/repository -name "*.jar" ! -path "*rocketmq*" ! -path "*maven*" ! -path "*plexus*" | tr "\n" ":"); timeout 550 java -cp $CP org.junit.runner.JUnitCore org.apache.rocketmq.controller.impl.controller.impl.manager.TmpReproTest org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest org.apache.rocketmq.controller.impl.controlle
- `rc=0` 1.13 s: cd controller && CP=target/classes:target/test-classes:$(for m in common remoting srvutil client tools logging namesrv; do printf "../$m/target/classes:"; done)$(find ~/.m2/repository -name "*.jar" \( ! -path "*rocketmq*" -o -path "*rocketmq-shaded*" -o -path "*logger*" -o -path "*dledger*" \) ! -path "*/rocketmq/rocketmq-*5.*" ! -path "*maven*" ! -path "*plexus*" | tr "\n" ":"); timeout 550 java -cp $CP org.junit.runner.JUnitCore org.apache.rocketmq.controller.impl.controller.impl.manager.TmpReproTest org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest org.apac
- `rc=1` 1.07 s: grep -rl "org/apache/rocketmq/logging/org/slf4j/LoggerFactory" ~/.m2/repository --include=*.jar 2>/dev/null | head; for j in $(find ~/.m2/repository -path "*rocketmq*" -name "*.jar"); do unzip -l $j 2>/dev/null | grep -q "logging/org/slf4j/LoggerFactory.class" && echo $j; done
- `rc=0` 3.91 s: cd controller && CP=target/classes:target/test-classes:$(for m in common remoting srvutil client tools logging namesrv; do printf "../$m/target/classes:"; done)$(find ~/.m2/repository -name "*.jar" ! -path "*/org/apache/rocketmq/rocketmq-*" ! -path "*maven*" ! -path "*plexus*" | tr "\n" ":"); timeout 550 java -cp $CP org.junit.runner.JUnitCore org.apache.rocketmq.controller.impl.controller.impl.manager.TmpReproTest org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest org.apache.rocketmq.con
- `rc=0` 0.28 s: ls ~/.m2/repository/org/slf4j/*/
- `rc=0` 76.68 s: cd controller && CP=target/classes:target/test-classes:$(for m in common remoting srvutil client tools logging namesrv; do printf "../$m/target/classes:"; done)$(find ~/.m2/repository -name "*.jar" ! -path "*/org/apache/rocketmq/rocketmq-*" ! -path "*maven*" ! -path "*plexus*" ! -path "*/org/slf4j/*" | tr "\n" ":")$HOME/.m2/repository/org/slf4j/slf4j-api/1.7.32/slf4j-api-1.7.32.jar; timeout 550 java -cp $CP org.junit.runner.JUnitCore org.apache.rocketmq.controller.impl.controller.impl.manager.TmpReproTest org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest org.a
- `rc=0` 0.29 s: ls ~/.m2/repository/org/hamcrest/*/
- `rc=0` 83.8 s: cd controller && CP=$HOME/.m2/repository/org/hamcrest/hamcrest/2.1/hamcrest-2.1.jar:target/classes:target/test-classes:$(for m in common remoting srvutil client tools logging namesrv; do printf "../$m/target/classes:"; done)$(find ~/.m2/repository -name "*.jar" ! -path "*/org/apache/rocketmq/rocketmq-*" ! -path "*maven*" ! -path "*plexus*" ! -path "*/org/slf4j/*" ! -path "*hamcrest*" | tr "\n" ":")$HOME/.m2/repository/org/slf4j/slf4j-api/1.7.32/slf4j-api-1.7.32.jar; timeout 550 java -cp $CP org.junit.runner.JUnitCore org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest org
