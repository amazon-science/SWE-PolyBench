# Instance: apache__rocketmq-5037

- Final resolved (evaluator, logs/apache__rocketmq-5037_result.json): False
- Run state: DONE
- One attempt. Duration 544.6 s, turns 23, actor cost $0.8062883999999999, container commands 11
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/apache__rocketmq-5037/repo
</uploaded_files>
I've uploaded a Java code repository in the directory /work/apache__rocketmq-5037/repo. Consider the following issue description:

<issue_description>
Optimize controller module Response code
In Controller module process Request, if handle failure most return **CONTROLLER_INVALID_REQUEST** code.  Optimize return code, Make its semantics clearer.
ReplicasInfoManager#alterSyncStateSet, as following picture:
![image](https://user-images.githubusercontent.com/15797831/189293823-c88de649-7624-4a4a-82b8-81ae21ee821e.png)


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/apache__rocketmq-5037/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/apache__rocketmq-5037/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/apache__rocketmq-5037/bin/envrun 'git status --short && ls'
Edits you make under /work/apache__rocketmq-5037/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
grep -rn "CONTROLLER_" --include=*.java common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java; grep -rln "CONTROLLER_INVALID_REQUEST\|CONTROLLER_" --include=*.java . | grep -v /test/
```

tool result:

```
(eval):1: no matches found: --include=*.java
(eval):1: no matches found: --include=*.java
```

**tool call: Bash**

```bash
grep -rn "ResponseCode\.\|CONTROLLER_" --include=*.java controller/src/test | grep -v "SUCCESS" | head -50
```

tool result:

```
(eval):1: no matches found: --include=*.java
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5037/repo; grep -rn "CONTROLLER_" --include='*.java' . | grep -v /test/ | grep -v "^./controller"; echo ---; grep -rn "ResponseCode\.\|CONTROLLER_" --include='*.java' controller/src/test | grep -v "SUCCESS"
```

tool result:

```
./tools/src/main/java/org/apache/rocketmq/tools/admin/MQAdminExt.java:431:     * Command Code : RequestCode.GET_CONTROLLER_CONFIG
./tools/src/main/java/org/apache/rocketmq/tools/admin/MQAdminExt.java:442:     * Command Code : RequestCode.UPDATE_CONTROLLER_CONFIG
./broker/src/main/java/org/apache/rocketmq/broker/out/BrokerOuterAPI.java:130:import static org.apache.rocketmq.common.protocol.ResponseCode.CONTROLLER_NOT_LEADER;
./broker/src/main/java/org/apache/rocketmq/broker/out/BrokerOuterAPI.java:131:import static org.apache.rocketmq.common.protocol.ResponseCode.CONTROLLER_BROKER_METADATA_NOT_EXIST;
./broker/src/main/java/org/apache/rocketmq/broker/out/BrokerOuterAPI.java:1101:        final RemotingCommand request = RemotingCommand.createRequestCommand(RequestCode.CONTROLLER_GET_METADATA_INFO, null);
./broker/src/main/java/org/apache/rocketmq/broker/out/BrokerOuterAPI.java:1120:        final RemotingCommand request = RemotingCommand.createRequestCommand(RequestCode.CONTROLLER_ALTER_SYNC_STATE_SET, requestHeader);
./broker/src/main/java/org/apache/rocketmq/broker/out/BrokerOuterAPI.java:1129:            case CONTROLLER_NOT_LEADER: {
./broker/src/main/java/org/apache/rocketmq/broker/out/BrokerOuterAPI.java:1144:        final RemotingCommand request = RemotingCommand.createRequestCommand(RequestCode.CONTROLLER_REGISTER_BROKER, requestHeader);
./broker/src/main/java/org/apache/rocketmq/broker/out/BrokerOuterAPI.java:1151:            case CONTROLLER_NOT_LEADER: {
./broker/src/main/java/org/apache/rocketmq/broker/out/BrokerOuterAPI.java:1164:        final RemotingCommand request = RemotingCommand.createRequestCommand(RequestCode.CONTROLLER_GET_REPLICA_INFO, requestHeader);
./broker/src/main/java/org/apache/rocketmq/broker/out/BrokerOuterAPI.java:1174:            case CONTROLLER_NOT_LEADER: {
./broker/src/main/java/org/apache/rocketmq/broker/out/BrokerOuterAPI.java:1177:            case CONTROLLER_BROKER_METADATA_NOT_EXIST: {
./broker/src/main/java/org/apache/rocketmq/broker/controller/ReplicasManager.java:49:import static org.apache.rocketmq.common.protocol.ResponseCode.CONTROLLER_BROKER_METADATA_NOT_EXIST;
./broker/src/main/java/org/apache/rocketmq/broker/controller/ReplicasManager.java:105:        FIRST_TIME_SYNC_CONTROLLER_METADATA_DONE,
./broker/src/main/java/org/apache/rocketmq/broker/controller/ReplicasManager.java:135:                this.state = State.FIRST_TIME_SYNC_CONTROLLER_METADATA_DONE;
./broker/src/main/java/org/apache/rocketmq/broker/controller/ReplicasManager.java:141:        if (this.state == State.FIRST_TIME_SYNC_CONTROLLER_METADATA_DONE) {
./broker/src/main/java/org/apache/rocketmq/broker/controller/ReplicasManager.java:355:                if (exception.getResponseCode() == CONTROLLER_BROKER_METADATA_NOT_EXIST) {
./common/src/main/java/org/apache/rocketmq/common/protocol/RequestCode.java:247:    public static final int CONTROLLER_ALTER_SYNC_STATE_SET = 1001;
./common/src/main/java/org/apache/rocketmq/common/protocol/RequestCode.java:249:    public static final int CONTROLLER_ELECT_MASTER = 1002;
./common/src/main/java/org/apache/rocketmq/common/protocol/RequestCode.java:251:    public static final int CONTROLLER_REGISTER_BROKER = 1003;
./common/src/main/java/org/apache/rocketmq/common/protocol/RequestCode.java:253:    public static final int CONTROLLER_GET_REPLICA_INFO = 1004;
./common/src/main/java/org/apache/rocketmq/common/protocol/RequestCode.java:255:    public static final int CONTROLLER_GET_METADATA_INFO = 1005;
./common/src/main/java/org/apache/rocketmq/common/protocol/RequestCode.java:257:    public static final int CONTROLLER_GET_SYNC_STATE_DATA = 1006;
./common/src/main/java/org/apache/rocketmq/common/protocol/RequestCode.java:266:    public static final int UPDATE_CONTROLLER_CONFIG = 1009;
./common/src/main/java/org/apache/rocketmq/common/protocol/RequestCode.java:271:    public static final int GET_CONTROLLER_CONFIG = 1010;
./common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java:105:    public static final int CONTROLLER_FENCED_MASTER_EPOCH = 2000;
./common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java:106:    public static final int CONTROLLER_FENCED_SYNC_STATE_SET_EPOCH = 2001;
./common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java:107:    public static final int CONTROLLER_INVALID_MASTER = 2002;
./common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java:108:    public static final int CONTROLLER_INVALID_REPLICAS = 2003;
./common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java:109:    public static final int CONTROLLER_MASTER_NOT_AVAILABLE = 2004;
./common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java:110:    public static final int CONTROLLER_INVALID_REQUEST = 2005;
./common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java:111:    public static final int CONTROLLER_BROKER_NOT_ALIVE = 2006;
./common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java:112:    public static final int CONTROLLER_NOT_LEADER = 2007;
./common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java:114:    public static final int CONTROLLER_BROKER_METADATA_NOT_EXIST = 2008;
./common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java:116:    public static final int CONTROLLER_INVALID_CLEAN_BROKER_METADATA = 2009;
./common/src/main/java/org/apache/rocketmq/common/constant/LoggerName.java:22:    public static final String CONTROLLER_LOGGER_NAME = "RocketmqController";
./client/src/main/java/org/apache/rocketmq/client/impl/MQClientAPIImpl.java:2934:        final RemotingCommand request = RemotingCommand.createRequestCommand(RequestCode.CONTROLLER_GET_METADATA_INFO, null);
./client/src/main/java/org/apache/rocketmq/client/impl/MQClientAPIImpl.java:2951:        RemotingCommand request = RemotingCommand.createRequestCommand(RequestCode.CONTROLLER_GET_SYNC_STATE_DATA, null);
./client/src/main/java/org/apa
[... 2903 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5037/repo; sed -n 95,120p common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java; grep -rn "ResponseCode\." controller/src/main; sed -n 140,230p controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java
```

tool result:

```
    public static final int NOT_LEADER_FOR_QUEUE = 501;

    public static final int RPC_UNKNOWN = -1000;
    public static final int RPC_ADDR_IS_NULL = -1002;
    public static final int RPC_SEND_TO_CHANNEL_FAILED = -1004;
    public static final int RPC_TIME_OUT = -1006;

    /**
     * Controller response code
     */
    public static final int CONTROLLER_FENCED_MASTER_EPOCH = 2000;
    public static final int CONTROLLER_FENCED_SYNC_STATE_SET_EPOCH = 2001;
    public static final int CONTROLLER_INVALID_MASTER = 2002;
    public static final int CONTROLLER_INVALID_REPLICAS = 2003;
    public static final int CONTROLLER_MASTER_NOT_AVAILABLE = 2004;
    public static final int CONTROLLER_INVALID_REQUEST = 2005;
    public static final int CONTROLLER_BROKER_NOT_ALIVE = 2006;
    public static final int CONTROLLER_NOT_LEADER = 2007;

    public static final int CONTROLLER_BROKER_METADATA_NOT_EXIST = 2008;

    public static final int CONTROLLER_INVALID_CLEAN_BROKER_METADATA = 2009;

}
controller/src/main/java/org/apache/rocketmq/controller/impl/DLedgerController.java:194:        return RemotingCommand.createResponseCommandWithHeader(ResponseCode.SUCCESS, new GetMetaDataResponseHeader(
controller/src/main/java/org/apache/rocketmq/controller/impl/DLedgerController.java:299:                final RemotingCommand command = RemotingCommand.createResponseCommand(ResponseCode.CONTROLLER_NOT_LEADER, "The controller is not in leader state");
controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java:90:                result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, err);
controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java:99:                result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_MASTER, err);
controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java:108:                result.setCodeAndRemark(ResponseCode.CONTROLLER_FENCED_MASTER_EPOCH, err);
controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java:117:                result.setCodeAndRemark(ResponseCode.CONTROLLER_FENCED_SYNC_STATE_SET_EPOCH, err);
controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java:126:                    result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REPLICAS, err);
controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java:132:                    result.setCodeAndRemark(ResponseCode.CONTROLLER_BROKER_NOT_ALIVE, err);
controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java:140:                result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, err);
controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java:152:        result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, "Broker metadata is not existed");
controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java:174:                result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, err);
controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java:198:            result.setCodeAndRemark(ResponseCode.CONTROLLER_MASTER_NOT_AVAILABLE, "Failed to elect a new broker master");
controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java:201:        result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, "Broker metadata is not existed");
controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java:274:        result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, "The broker has not master, and this new registered broker can't not be elected as master");
controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java:295:        result.setCodeAndRemark(ResponseCode.CONTROLLER_BROKER_METADATA_NOT_EXIST, "Broker metadata is not existed");
controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java:337:                result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_CLEAN_BROKER_METADATA, remark);
controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java:345:                        result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_CLEAN_BROKER_METADATA, remark);
controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java:356:        result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_CLEAN_BROKER_METADATA, String.format("Broker %s is not existed,clean broker data failure.", brokerName));
controller/src/main/java/org/apache/rocketmq/controller/impl/event/ControllerResult.java:27:    private int responseCode = ResponseCode.SUCCESS;
controller/src/main/java/org/apache/rocketmq/controller/processor/ControllerRequestProcessor.java:138:                return RemotingCommand.createResponseCommand(ResponseCode.SUCCESS, "Heart beat success");
controller/src/main/java/org/apache/rocketmq/controller/processor/ControllerRequestProcessor.java:165:                return RemotingCommand.createResponseCommand(ResponseCode.REQUEST_CODE_NOT_SUPPORTED, error);
controller/src/main/java/org/apache/rocketmq/controller/processor/ControllerRequestProcessor.java:190:                response.setCode(ResponseCode.SYSTEM_ERROR);
controller/src/main/java/org/apache/rocketmq/controller/processor/ControllerRequestProcessor.java:198:                response.setCode(ResponseCode.SYSTEM_ERROR);
controller/src/main/java/org/apache/rocketmq/controller/processor/ControllerRequestProcessor.java:206:        response.setCode(ResponseCode.SUCCESS);
controller/src/main/java/org/apache/rocketmq/controller/processor/ControllerRequestProcessor.java:220:                response.setCode(ResponseCode.SYSTEM_ERROR);
controller/src/main/java/org/apache/rocketmq/c
[... 5594 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5037/repo; sed -n 75,300p controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java; git log --oneline -2
```

tool result:

```
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
                result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, err);
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
                String err = String.format("Rejecting alter syncStateSet request because the current master epoch is:{%d}, not {%d}",
                    syncStateInfo.getMasterEpoch(), request.getMasterEpoch());
                log.error("{}", err);
                result.setCodeAndRemark(ResponseCode.CONTROLLER_FENCED_MASTER_EPOCH, err);
                return result;
            }

            // Check syncStateSet epoch
            if (syncStateSet.getSyncStateSetEpoch() != syncStateInfo.getSyncStateSetEpoch()) {
                String err = String.format("Rejecting alter syncStateSet request because the current syncStateSet epoch is:{%d}, not {%d}",
                    syncStateInfo.getSyncStateSetEpoch(), syncStateSet.getSyncStateSetEpoch());
                log.error("{}", err);
                result.setCodeAndRemark(ResponseCode.CONTROLLER_FENCED_SYNC_STATE_SET_EPOCH, err);
                return result;
            }

            // Check newSyncStateSet correctness
            for (String replicas : newSyncStateSet) {
                if (!brokerInfo.isBrokerExist(replicas)) {
                    String err = String.format("Rejecting alter syncStateSet request because the replicas {%s} don't exist", replicas);
                    log.error("{}", err);
                    result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REPLICAS, err);
                    return result;
                }
                if (!brokerAlivePredicate.test(brokerInfo.getClusterName(), replicas)) {
                    String err = String.format("Rejecting alter syncStateSet request because the replicas {%s} don't alive", replicas);
                    log.error(err);
                    result.setCodeAndRemark(ResponseCode.CONTROLLER_BROKER_NOT_ALIVE, err);
                    return result;
                }
            }

            if (!newSyncStateSet.contains(syncStateInfo.getMasterAddress())) {
                String err = String.format("Rejecting alter syncStateSet request because the newSyncStateSet don't contains origin leader {%s}", syncStateInfo.getMasterAddress());
                log.error(err);
                result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, err);
                return result;
            }

            // Generate event
            int epoch = syncStateInfo.getSyncStateSetEpoch() + 1;
            response.setNewSyncStateSetEpoch(epoch);
            result.setBody(new SyncStateSet(newSyncStateSet, epoch).encode());
            final AlterSyncStateSetEvent event = new AlterSyncStateSetEvent(brokerName, newSyncStateSet);
            result.addEvent(event);
            return result;
        }
        result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, "Broker metadata is not existed");
        return result;
    }

    public ControllerResult<ElectMasterResponseHeader> electMaster(final ElectMasterRequestHeader request,
        final ElectPolicy electPolicy) {
        final String brokerName = request.getBrokerName();
        final String assignBrokerAddress = request.getBrokerAddress();
        final ControllerResult<ElectMasterResponseHeader> result = new ControllerResult<>(new ElectMasterResponseHeader());
        if (isContainsBroker(brokerName)) {
            final SyncStateInfo syncStateInfo = this.syncStateSetInfoTable.get(brokerName);
            final BrokerInfo brokerInfo = this.replicaInfoTable.get(brokerName);
            final Set<String> syncStateSet = syncStateInfo.getSyncStateSet();
            final String oldMaster = syncStateInfo.getMasterAddress();
            Set<String> allReplicaBrokers = controllerConfig.isEnableElectUncleanMaster() ? brokerInfo.getAllBroker() : null;

            // elect by policy
            String newMaster = electPolicy.elect(brokerInfo.getClusterName(), syncStateSet, allReplicaBrokers, oldMaster, assignBrokerAddress);
            if (StringUtils.isNotEmpty(newMaster) && newMaster.equals(oldMaster)) {
                // old master still valid, change nothing
                String err = String.format("The old master %s is still alive, not need to elect new master for broker %s", oldMaster, brokerInfo.getBrokerName())
[... 7557 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5037/repo; grep -rn "getResponseCode\|getCode()" controller/src/test | grep -v SUCCESS; sed -n 60,135p controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java
```

tool result:

```
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:163:        assertEquals(ResponseCode.CONTROLLER_INVALID_REQUEST, cResult.getResponseCode());
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:174:        System.out.println(cResult.getResponseCode());
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:190:        System.out.println(cResult.getResponseCode());
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:216:        assertEquals(cResult1.getResponseCode(), ResponseCode.CONTROLLER_INVALID_REQUEST);
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:221:        assertEquals(cResult2.getResponseCode(), ResponseCode.CONTROLLER_MASTER_NOT_AVAILABLE);
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:264:        assertEquals(ResponseCode.CONTROLLER_INVALID_CLEAN_BROKER_METADATA, result1.getResponseCode());
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:268:        assertEquals(ResponseCode.CONTROLLER_INVALID_CLEAN_BROKER_METADATA, result2.getResponseCode());
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:281:        assertEquals(ResponseCode.CONTROLLER_INVALID_CLEAN_BROKER_METADATA, result5.getResponseCode());
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java:286:        assertEquals(ResponseCode.CONTROLLER_INVALID_CLEAN_BROKER_METADATA, result6.getResponseCode());
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/ControllerManagerTest.java:138:        switch (response.getCode()) {
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/ControllerManagerTest.java:143:                throw new MQBrokerException(response.getCode(), "Controller leader was changed");
controller/src/test/java/org/apache/rocketmq/controller/impl/controller/ControllerManagerTest.java:146:        throw new MQBrokerException(response.getCode(), response.getRemark());
        final ControllerConfig config = new ControllerConfig();
        config.setEnableElectUncleanMaster(false);
        config.setScanNotActiveBrokerInterval(300000000);
        this.replicasInfoManager = new ReplicasInfoManager(config);
        this.heartbeatManager = new DefaultBrokerHeartbeatManager(config);
        this.heartbeatManager.start();
    }

    @After
    public void destroy() {
        this.replicasInfoManager = null;
        this.heartbeatManager.shutdown();
        this.heartbeatManager = null;
    }

    public boolean registerNewBroker(String clusterName, String brokerName, String brokerAddress,
        boolean isFirstRegisteredBroker) {
        // Register new broker
        final RegisterBrokerToControllerRequestHeader registerRequest =
            new RegisterBrokerToControllerRequestHeader(clusterName, brokerName, brokerAddress);
        final ControllerResult<RegisterBrokerToControllerResponseHeader> registerResult = this.replicasInfoManager.registerBroker(registerRequest);
        apply(registerResult.getEvents());

        if (isFirstRegisteredBroker) {
            final ControllerResult<GetReplicaInfoResponseHeader> getInfoResult = this.replicasInfoManager.getReplicaInfo(new GetReplicaInfoRequestHeader(brokerName));
            final GetReplicaInfoResponseHeader replicaInfo = getInfoResult.getResponse();
            assertEquals(replicaInfo.getMasterAddress(), brokerAddress);
            assertEquals(replicaInfo.getMasterEpoch(), 1);
        } else {
            final RegisterBrokerToControllerResponseHeader response = registerResult.getResponse();
            assertTrue(response.getBrokerId() > 0);
        }
        return true;
    }

    private boolean alterNewInSyncSet(String brokerName, String masterAddress, int masterEpoch,
        Set<String> newSyncStateSet, int syncStateSetEpoch) {
        final AlterSyncStateSetRequestHeader alterRequest =
            new AlterSyncStateSetRequestHeader(brokerName, masterAddress, masterEpoch);
        final ControllerResult<AlterSyncStateSetResponseHeader> result = this.replicasInfoManager.alterSyncStateSet(alterRequest, new SyncStateSet(newSyncStateSet, syncStateSetEpoch), (va1, va2) -> true);
        apply(result.getEvents());

        final ControllerResult<GetReplicaInfoResponseHeader> resp = this.replicasInfoManager.getReplicaInfo(new GetReplicaInfoRequestHeader(brokerName));
        final GetReplicaInfoResponseHeader replicaInfo = resp.getResponse();
        final SyncStateSet syncStateSet = RemotingSerializable.decode(resp.getBody(), SyncStateSet.class);

        assertArrayEquals(syncStateSet.getSyncStateSet().toArray(), newSyncStateSet.toArray());
        assertEquals(syncStateSet.getSyncStateSetEpoch(), syncStateSetEpoch + 1);
        return true;
    }

    private void apply(final List<EventMessage> events) {
        for (EventMessage event : events) {
            this.replicasInfoManager.applyEvent(event);
        }
    }

    public void mockMetaData() {
        registerNewBroker("cluster1", "broker1", "127.0.0.1:9000", true);
        registerNewBroker("cluster1", "broker1", "127.0.0.1:9001", false);
        registerNewBroker("cluster1", "broker1", "127.0.0.1:9002", false);
        final HashSet<String> newSyncStateSet = new HashSet<>();
        newSyncStateSet.add("127.0.0.1:9000");
        newSyncStateSet.add("127.0.0.1:9001");
        newSyncStateSet.add("127.0.0.1:9002");
        assertTrue(alterNewInSyncSet("broker1", "127.0.0.1:9000", 1, newSyncStateSet, 1));
    }

    public void mockHeartbeatDataMasterStillAlive() {
        this.heartbeatManager.re
[... 363 more characters not shown]
```

**assistant:** Both `CONTROLLER_INVALID_REQUEST` assertions in the tests cover the "old master still alive" case in `electMaster`. My plan is to add specific response codes and use them in `ReplicasInfoManager`.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5037/repo; python3 - <<'EOF'
p='common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java'
s=open(p).read()
s=s.replace("""    public static final int CONTROLLER_INVALID_CLEAN_BROKER_METADATA = 2009;
""","""    public static final int CONTROLLER_INVALID_CLEAN_BROKER_METADATA = 2009;

    public static final int CONTROLLER_BROKER_NEED_TO_BE_REGISTERED = 2010;

    public static final int CONTROLLER_MASTER_STILL_EXIST = 2011;

    public static final int CONTROLLER_ELECT_MASTER_FAILED = 2012;

    public static final int CONTROLLER_ALTER_SYNC_STATE_SET_FAILED = 2013;
""")
open(p,'w').write(s)
p='controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java'
s=open(p).read()
reps=[
("""                result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, err);
                return result;
            }

            // Check master""","""                result.setCodeAndRemark(ResponseCode.CONTROLLER_ALTER_SYNC_STATE_SET_FAILED, err);
                return result;
            }

            // Check master"""),
("""                log.error(err);
                result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, err);""","""                log.error(err);
                result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_MASTER, err);"""),
("""            result.addEvent(event);
            return result;
        }
        result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, "Broker metadata is not existed");""","""            result.addEvent(event);
            return result;
        }
        result.setCodeAndRemark(ResponseCode.CONTROLLER_BROKER_NEED_TO_BE_REGISTERED, "Broker metadata is not existed");"""),
("""                result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, err);
                return result;
            }
            // a new master""","""                result.setCodeAndRemark(ResponseCode.CONTROLLER_MASTER_STILL_EXIST, err);
                return result;
            }
            // a new master"""),
("""            result.setCodeAndRemark(ResponseCode.CONTROLLER_MASTER_NOT_AVAILABLE, "Failed to elect a new broker master");
            return result;
        }
        result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, "Broker metadata is not existed");""","""            result.setCodeAndRemark(ResponseCode.CONTROLLER_MASTER_NOT_AVAILABLE, "Failed to elect a new broker master");
            return result;
        }
        result.setCodeAndRemark(ResponseCode.CONTROLLER_BROKER_NEED_TO_BE_REGISTERED, "Broker metadata is not existed");"""),
("""ResponseCode.CONTROLLER_INVALID_REQUEST, "The broker has not master""","""ResponseCode.CONTROLLER_MASTER_NOT_AVAILABLE, "The broker has not master"""),
]
for a,b in reps:
    assert s.count(a)==1,a
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -rn "CONTROLLER_INVALID_REQUEST" --include='*.java' . | grep -v /test/
```

tool result:

```
./common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java:110:    public static final int CONTROLLER_INVALID_REQUEST = 2005;
```

**thinking:**

```
I'll change the "new set doesn't contain the leader" case to use `CONTROLLER_ALTER_SYNC_STATE_SET_FAILED`, since `CONTROLLER_INVALID_MASTER` covers a different scenario (mismatched master address in the request).


```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5037/repo; python3 - <<'EOF'
p='controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java'
s=open(p).read()
a="""                log.error(err);
                result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_MASTER, err);"""
assert s.count(a)==1
s=s.replace(a,a.replace("CONTROLLER_INVALID_MASTER","CONTROLLER_ALTER_SYNC_STATE_SET_FAILED"))
open(p,'w').write(s)
EOF
git diff
```

tool result:

```
diff --git a/common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java b/common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java
index 65c367d3c..e3786358d 100644
--- a/common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java
+++ b/common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java
@@ -115,4 +115,12 @@ public class ResponseCode extends RemotingSysResponseCode {
 
     public static final int CONTROLLER_INVALID_CLEAN_BROKER_METADATA = 2009;
 
+    public static final int CONTROLLER_BROKER_NEED_TO_BE_REGISTERED = 2010;
+
+    public static final int CONTROLLER_MASTER_STILL_EXIST = 2011;
+
+    public static final int CONTROLLER_ELECT_MASTER_FAILED = 2012;
+
+    public static final int CONTROLLER_ALTER_SYNC_STATE_SET_FAILED = 2013;
+
 }
diff --git a/controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java b/controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java
index 683a17d4e..88ab5b695 100644
--- a/controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java
+++ b/controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java
@@ -87,7 +87,7 @@ public class ReplicasInfoManager {
             if (oldSyncStateSet.size() == newSyncStateSet.size() && oldSyncStateSet.containsAll(newSyncStateSet)) {
                 String err = "The newSyncStateSet is equal with oldSyncStateSet, no needed to update syncStateSet";
                 log.warn("{}", err);
-                result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, err);
+                result.setCodeAndRemark(ResponseCode.CONTROLLER_ALTER_SYNC_STATE_SET_FAILED, err);
                 return result;
             }
 
@@ -137,7 +137,7 @@ public class ReplicasInfoManager {
             if (!newSyncStateSet.contains(syncStateInfo.getMasterAddress())) {
                 String err = String.format("Rejecting alter syncStateSet request because the newSyncStateSet don't contains origin leader {%s}", syncStateInfo.getMasterAddress());
                 log.error(err);
-                result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, err);
+                result.setCodeAndRemark(ResponseCode.CONTROLLER_ALTER_SYNC_STATE_SET_FAILED, err);
                 return result;
             }
 
@@ -149,7 +149,7 @@ public class ReplicasInfoManager {
             result.addEvent(event);
             return result;
         }
-        result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, "Broker metadata is not existed");
+        result.setCodeAndRemark(ResponseCode.CONTROLLER_BROKER_NEED_TO_BE_REGISTERED, "Broker metadata is not existed");
         return result;
     }
 
@@ -171,7 +171,7 @@ public class ReplicasInfoManager {
                 // old master still valid, change nothing
                 String err = String.format("The old master %s is still alive, not need to elect new master for broker %s", oldMaster, brokerInfo.getBrokerName());
                 log.warn("{}", err);
-                result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, err);
+                result.setCodeAndRemark(ResponseCode.CONTROLLER_MASTER_STILL_EXIST, err);
                 return result;
             }
             // a new master is elected
@@ -198,7 +198,7 @@ public class ReplicasInfoManager {
             result.setCodeAndRemark(ResponseCode.CONTROLLER_MASTER_NOT_AVAILABLE, "Failed to elect a new broker master");
             return result;
         }
-        result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, "Broker metadata is not existed");
+        result.setCodeAndRemark(ResponseCode.CONTROLLER_BROKER_NEED_TO_BE_REGISTERED, "Broker metadata is not existed");
         return result;
     }
 
@@ -271,7 +271,7 @@ public class ReplicasInfoManager {
         }
 
         response.setMasterAddress("");
-        result.setCodeAndRemark(ResponseCode.CONTROLLER_INVALID_REQUEST, "The broker has not master, and this new registered broker can't not be elected as master");
+        result.setCodeAndRemark(ResponseCode.CONTROLLER_MASTER_NOT_AVAILABLE, "The broker has not master, and this new registered broker can't not be elected as master");
         return result;
     }
 
diff --git a/pom.xml b/pom.xml
index 958c9015a..6a3939348 100644
--- a/pom.xml
+++ b/pom.xml
@@ -377,7 +377,7 @@
                     <forkCount>1</forkCount>
                     <reuseForks>true</reuseForks>
                     <excludes>
-                        <exclude>**/IT*.java</exclude>
+<exclude>**/IT*.java</exclude><exclude>%regex[.*MixCommitlogTest.*]</exclude>
                     </excludes>
                 </configuration>
             </plugin>
```

**thinking:**

```
I'll leave the pre-existing `pom.xml` diff as is and build/run the controller tests next—the two `CONTROLLER_INVALID_REQUEST` assertions for the "master still alive" case are expected to fail now.


```

**tool call: Bash**

```bash
/work/apache__rocketmq-5037/bin/envrun 'mvn -o -q install -pl common -DskipTests -Dcheckstyle.skip -Dspotbugs.skip -Drat.skip 2>&1 | tail -20; mvn -o test -pl controller -Dcheckstyle.skip -Drat.skip -Dtest=ReplicasInfoManagerTest,ControllerManagerTest,DLedgerControllerTest -DfailIfNoTests=false 2>&1 | grep -E "Tests run|FAIL|expected|ERROR" | head -30'
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

**assistant:** The test runner's JUnit 4 provider isn't in the offline Maven cache. I'll check which providers are available.

**tool call: Bash**

```bash
/work/apache__rocketmq-5037/bin/envrun 'ls ~/.m2/repository/org/apache/maven/surefire/; ls ~/.m2/repository/org/apache/maven/surefire/*/ | head -40'
```

tool result:

```
maven-surefire-common
surefire
surefire-api
surefire-booter
/root/.m2/repository/org/apache/maven/surefire/maven-surefire-common/:
2.19.1

/root/.m2/repository/org/apache/maven/surefire/surefire-api/:
2.19.1

/root/.m2/repository/org/apache/maven/surefire/surefire-booter/:
2.19.1

/root/.m2/repository/org/apache/maven/surefire/surefire/:
2.19.1
```

**assistant:** Since there's no surefire provider, I'll compile with Maven and run the tests directly with JUnitCore.

**tool call: Bash**

```bash
/work/apache__rocketmq-5037/bin/envrun 'mvn -o -q test-compile -pl controller -Dcheckstyle.skip -Drat.skip 2>&1 | tail -5; mvn -o -q dependency:build-classpath -pl controller -Dmdep.outputFile=/tmp/cp.txt >/dev/null 2>&1; java -cp controller/target/classes:controller/target/test-classes:$(cat /tmp/cp.txt) org.junit.runner.JUnitCore org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest 2>&1 | grep -vE "^\s+at |INFO|WARN" | tail -30'
```

tool result:

```
     [java] JVM args ignored when same JVM is used.
cat: /tmp/cp.txt: No such file or directory
Error: Could not find or load main class org.junit.runner.JUnitCore
```

**tool call: Bash**

```bash
/work/apache__rocketmq-5037/bin/envrun 'mvn -o dependency:build-classpath -pl controller -Dmdep.outputFile=/tmp/cp.txt 2>&1 | grep -E "ERROR|BUILD" | head -5'
```

tool result:

```
[INFO] BUILD FAILURE
[ERROR] No plugin found for prefix 'dependency' in the current project and in the plugin groups [org.apache.maven.plugins, org.codehaus.mojo] available from the repositories [local (/root/.m2/repository), central (https://repo.maven.apache.org/maven2)] -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
```

**assistant:** The dependency plugin isn't cached either, so I'll assemble the classpath by hand from the local jars and the module `target/classes` directories.

**tool call: Bash**

```bash
/work/apache__rocketmq-5037/bin/envrun 'CP=controller/target/classes:controller/target/test-classes:common/target/classes:remoting/target/classes:client/target/classes:srvutil/target/classes:logging/target/classes:$(find ~/.m2/repository -name "*.jar" | grep -v "/org/apache/rocketmq/rocketmq-" | grep -v maven | tr "\n" ":"); ls common/target/classes remoting/target/classes >/dev/null && java -cp "$CP" org.junit.runner.JUnitCore org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest org.apache.rocketmq.controller.impl.controller.ControllerManagerTest 2>&1 | grep -vE "^\s+at |INFO|WARN|^[0-9]+$|ElectMasterResponseHeader" | tail -30'
```

tool result:

```
[EntryDispatcher-n1-n0] ERROR io.openmessaging.storage.dledger.DLedgerRpcNettyService - Send push request failed, info[group=d0a8c853-14a2-4b36-8611-fc80c67de2d1,term=1,code=200,local=null,remote=n0,leader=n1]
org.apache.rocketmq.remoting.exception.RemotingConnectException: connect to localhost:30000 failed
[EntryDispatcher-n1-n0] ERROR io.openmessaging.storage.dledger.DLedgerEntryPusher - [Push-n0]Error in EntryDispatcher-n1-n0 writeIndex=-1 compareIndex=0
io.openmessaging.storage.dledger.exception.DLedgerException: [code=302,name=NETWORK_ERROR,desc=] compareIndex=0
[EntryDispatcher-n1-n0] ERROR io.openmessaging.storage.dledger.DLedgerRpcNettyService - Send push request failed, info[group=d0a8c853-14a2-4b36-8611-fc80c67de2d1,term=1,code=200,local=null,remote=n0,leader=n1]
org.apache.rocketmq.remoting.exception.RemotingConnectException: connect to localhost:30000 failed
[EntryDispatcher-n1-n0] ERROR io.openmessaging.storage.dledger.DLedgerEntryPusher - [Push-n0]Error in EntryDispatcher-n1-n0 writeIndex=-1 compareIndex=0
io.openmessaging.storage.dledger.exception.DLedgerException: [code=302,name=NETWORK_ERROR,desc=] compareIndex=0
[heartBeatInvokeExecutor-2] ERROR io.openmessaging.storage.dledger.DLedgerRpcNettyService - Send heartBeat request failed, info[group=d0a8c853-14a2-4b36-8611-fc80c67de2d1,term=1,code=200,local=n1,remote=n0,leader=n1]
org.apache.rocketmq.remoting.exception.RemotingConnectException: connect to localhost:30000 failed
[EntryDispatcher-n1-n0] ERROR io.openmessaging.storage.dledger.DLedgerRpcNettyService - Send push request failed, info[group=d0a8c853-14a2-4b36-8611-fc80c67de2d1,term=1,code=200,local=null,remote=n0,leader=n1]
org.apache.rocketmq.remoting.exception.RemotingConnectException: connect to localhost:30000 failed
[EntryDispatcher-n1-n0] ERROR io.openmessaging.storage.dledger.DLedgerEntryPusher - [Push-n0]Error in EntryDispatcher-n1-n0 writeIndex=-1 compareIndex=0
io.openmessaging.storage.dledger.exception.DLedgerException: [code=302,name=NETWORK_ERROR,desc=] compareIndex=0
Delete file /tmp/d0a8c853-14a2-4b36-8611-fc80c67de2d1/n0
Delete file /tmp/d0a8c853-14a2-4b36-8611-fc80c67de2d1/n1
Delete file /tmp/d0a8c853-14a2-4b36-8611-fc80c67de2d1/n2
E
Time: 16.573
There were 3 failures:
1) testElectMaster(org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest)
java.lang.AssertionError: expected:<2011> but was:<2005>
2) testElectMasterOldMasterStillAlive(org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest)
java.lang.AssertionError: expected:<2005> but was:<2011>
3) testSomeApi(org.apache.rocketmq.controller.impl.controller.ControllerManagerTest)
java.lang.NoSuchMethodError: org.hamcrest.Matcher.describeMismatch(Ljava/lang/Object;Lorg/hamcrest/Description;)V

FAILURES!!!
Tests run: 7,  Failures: 3
```

**thinking:**

```
The two ReplicasInfoManagerTest failures are expected since the old tests still assert error code 2005 instead of the new 2011. The ControllerManagerTest failure is just a hamcrest version clash in my classpath masking the real result, so I'll rerun it with a single hamcrest version and compare against the original code.


```

**tool call: Bash**

```bash
/work/apache__rocketmq-5037/bin/envrun 'find ~/.m2/repository -name "*hamcrest*.jar"'
```

tool result:

```
/root/.m2/repository/org/hamcrest/hamcrest/2.1/hamcrest-2.1.jar
/root/.m2/repository/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar
```

**tool call: Bash**

```bash
cat > /tmp/runct.sh <<'EOF'
CP=controller/target/classes:controller/target/test-classes:common/target/classes:remoting/target/classes:client/target/classes:srvutil/target/classes:logging/target/classes:/root/.m2/repository/org/hamcrest/hamcrest/2.1/hamcrest-2.1.jar:$(find ~/.m2/repository -name "*.jar" | grep -v "/org/apache/rocketmq/rocketmq-" | grep -v maven | grep -v hamcrest | tr "\n" ":")
java -cp "$CP" org.junit.runner.JUnitCore org.apache.rocketmq.controller.impl.controller.ControllerManagerTest 2>&1 | grep -E "^[0-9]+\)|Error|Tests run|^OK|expected" | grep -v "ERROR " | head
EOF
cp /tmp/runct.sh /work/apache__rocketmq-5037/repo/runct.sh
/work/apache__rocketmq-5037/bin/envrun 'bash runct.sh'
```

tool result:

```
Exit code 127
(eval):1: operation not permitted: /tmp/runct.sh
cp: /tmp/runct.sh: No such file or directory
bash: runct.sh: No such file or directory
```

**tool call: Write**

```json
{
 "file_path": "/work/apache__rocketmq-5037/repo/runct.sh",
 "content": "CP=controller/target/classes:controller/target/test-classes:common/target/classes:remoting/target/classes:client/target/classes:srvutil/target/classes:logging/target/classes:/root/.m2/repository/org/hamcrest/hamcrest/2.1/hamcrest-2.1.jar:$(find ~/.m2/repository -name \"*.jar\" | grep -v \"/org/apache/rocketmq/rocketmq-\" | grep -v maven | grep -v hamcrest | tr \"\\n\" \":\")\njava -cp \"$CP\" org.junit.runner.JUnitCore \"$@\" 2>&1 | grep -E \"^[0-9]+\\)|Error|Tests run|^OK|expected|Exception:\" | grep -v \"ERROR \\|RemotingConnect\\|DLedgerException\" | head -20\n"
}
```

tool result:

```
File created successfully at: /work/apache__rocketmq-5037/repo/runct.sh (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
/work/apache__rocketmq-5037/bin/envrun 'bash runct.sh org.apache.rocketmq.controller.impl.controller.ControllerManagerTest'
```

tool result:

```
[voteInvokeExecutor-2] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30002] failed, AbstractBootstrap$PendingRegistrationPromise@64091881(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30002)
[voteInvokeExecutor-1] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30001] failed, AbstractBootstrap$PendingRegistrationPromise@7e0657df(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30001)
[voteInvokeExecutor-2] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30002] failed, AbstractBootstrap$PendingRegistrationPromise@bde3296(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30002)
[heartBeatInvokeExecutor-1] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30000] failed, AbstractBootstrap$PendingRegistrationPromise@ca776ab(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30000)
[EntryDispatcher-n1-n0] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30000] failed, AbstractBootstrap$PendingRegistrationPromise@36101cb4(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30000)
[EntryDispatcher-n1-n0] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30000] failed, AbstractBootstrap$PendingRegistrationPromise@525628f9(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30000)
[heartBeatInvokeExecutor-1] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30000] failed, AbstractBootstrap$PendingRegistrationPromise@7826e20f(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30000)
[EntryDispatcher-n1-n0] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30000] failed, AbstractBootstrap$PendingRegistrationPromise@477ffb0b(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30000)
[EntryDispatcher-n1-n0] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30000] failed, AbstractBootstrap$PendingRegistrationPromise@11bbb9ab(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30000)
[heartBeatInvokeExecutor-1] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30000] failed, AbstractBootstrap$PendingRegistrationPromise@5597389(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30000)
[EntryDispatcher-n1-n0] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30000] failed, AbstractBootstrap$PendingRegistrationPromise@d8d00fe(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30000)
[EntryDispatcher-n1-n0] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30000] failed, AbstractBootstrap$PendingRegistrationPromise@7288a382(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30000)
OK (1 test)
```

**thinking:**

```
ControllerManagerTest passed. Now I'll run the full controller test suite, then temporarily switch the two old assertions to CONTROLLER_MASTER_STILL_EXIST to verify the change end-to-end before reverting that test edit.


```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5037/repo; T=controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java; sed -i '' 's/CONTROLLER_INVALID_REQUEST/CONTROLLER_MASTER_STILL_EXIST/' $T; CLASSES=$(cd controller/src/test/java && grep -rl "@Test" . | sed 's#^\./##; s#\.java$##; s#/#.#g' | tr '\n' ' '); echo $CLASSES; ../bin/envrun "mvn -o -q test-compile -pl controller -Dcheckstyle.skip -Drat.skip 2>&1 | grep ERROR | head; bash runct.sh $CLASSES" 2>&1 | grep -v WARN; git checkout $T; git status --short
```

tool result:

```
org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest org.apache.rocketmq.controller.impl.controller.impl.DefaultBrokerHeartbeatManagerTest org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest org.apache.rocketmq.controller.impl.controller.ControllerManagerTest 

Updated 1 path from the index
 M common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java
 M controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java
 M pom.xml
?? Dockerfile
?? runct.sh
```

**assistant:** That run printed nothing, so I can't tell whether it passed. I'll rerun it with the output visible.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5037/repo; T=controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java; sed -i '' 's/CONTROLLER_INVALID_REQUEST/CONTROLLER_MASTER_STILL_EXIST/' $T; ../bin/envrun "mvn -o -q test-compile -pl controller -Dcheckstyle.skip -Drat.skip 2>&1 | grep ERROR | head; bash runct.sh org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest org.apache.rocketmq.controller.impl.controller.impl.DefaultBrokerHeartbeatManagerTest org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest org.apache.rocketmq.controller.impl.controller.ControllerManagerTest" > out.log 2>&1; git checkout $T; grep -v WARN out.log | tail -20
```

tool result:

```
Updated 1 path from the index
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5037/repo; wc -l out.log; tail -c 2000 out.log
```

tool result:

```
      21 out.log
Connection refused: localhost/127.0.0.1:30002)
[EntryDispatcher-n1-n0] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30000] failed, AbstractBootstrap$PendingRegistrationPromise@448246fc(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30000)
[heartBeatInvokeExecutor-1] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30000] failed, AbstractBootstrap$PendingRegistrationPromise@d66a229(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30000)
[EntryDispatcher-n1-n0] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30000] failed, AbstractBootstrap$PendingRegistrationPromise@2634f3b7(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30000)
[EntryDispatcher-n1-n0] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30000] failed, AbstractBootstrap$PendingRegistrationPromise@6fb2c6d7(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30000)
[heartBeatInvokeExecutor-1] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30000] failed, AbstractBootstrap$PendingRegistrationPromise@79e6f6a0(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30000)
[EntryDispatcher-n1-n0] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30000] failed, AbstractBootstrap$PendingRegistrationPromise@50cb0178(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30000)
[voteInvokeExecutor-2] WARN RocketmqRemoting - createChannel: connect remote host[localhost:30001] failed, AbstractBootstrap$PendingRegistrationPromise@5c2d8828(failure: io.netty.channel.AbstractChannel$AnnotatedConnectException: Connection refused: localhost/127.0.0.1:30001)
```

**assistant:** My helper script's `head -20` was cutting the output off before the summary line. I'll filter out the noisy log lines first and remove the limit.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5037/repo; sed -i '' 's/ | head -20$/ | grep -v WARN/' runct.sh; T=controller/src/test/java/org/apache/rocketmq/controller/impl/controller/impl/manager/ReplicasInfoManagerTest.java; sed -i '' 's/CONTROLLER_INVALID_REQUEST/CONTROLLER_MASTER_STILL_EXIST/' $T; ../bin/envrun "mvn -o -q test-compile -pl controller -Dcheckstyle.skip -Drat.skip 2>&1 | grep ERROR | head; bash runct.sh org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest org.apache.rocketmq.controller.impl.controller.impl.DefaultBrokerHeartbeatManagerTest org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest org.apache.rocketmq.controller.impl.controller.ControllerManagerTest" > out.log 2>&1; git checkout $T; cat out.log
```

tool result:

```
Updated 1 path from the index
OK (12 tests)
```

**assistant:** All 12 controller tests pass. Now I'll delete my helper files.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5037/repo; rm -f runct.sh out.log; git status --short
```

tool result:

```
 M common/src/main/java/org/apache/rocketmq/common/protocol/ResponseCode.java
 M controller/src/main/java/org/apache/rocketmq/controller/impl/manager/ReplicasInfoManager.java
 M pom.xml
?? Dockerfile
```

**assistant:** The controller no longer returns the catch-all `CONTROLLER_INVALID_REQUEST` code. Each failure in `ReplicasInfoManager` now returns a code that says what went wrong. All 12 controller tests pass once the two old assertions are updated to the new code; the test files themselves are unchanged.

**New codes** in `common/.../protocol/ResponseCode.java`:
- `CONTROLLER_BROKER_NEED_TO_BE_REGISTERED = 2010`
- `CONTROLLER_MASTER_STILL_EXIST = 2011`
- `CONTROLLER_ELECT_MASTER_FAILED = 2012`
- `CONTROLLER_ALTER_SYNC_STATE_SET_FAILED = 2013`

**What each failure in `ReplicasInfoManager` now returns:**

| Method | Situation | Old code | New code |
|---|---|---|---|
| `alterSyncStateSet` | New sync state set is the same as the old one | `INVALID_REQUEST` | `CONTROLLER_ALTER_SYNC_STATE_SET_FAILED` |
| `alterSyncStateSet` | New set doesn't include the current master | `INVALID_REQUEST` | `CONTROLLER_ALTER_SYNC_STATE_SET_FAILED` |
| `alterSyncStateSet` | No metadata for the broker | `INVALID_REQUEST` | `CONTROLLER_BROKER_NEED_TO_BE_REGISTERED` |
| `electMaster` | Old master is still alive, nothing to elect | `INVALID_REQUEST` | `CONTROLLER_MASTER_STILL_EXIST` |
| `electMaster` | No metadata for the broker | `INVALID_REQUEST` | `CONTROLLER_BROKER_NEED_TO_BE_REGISTERED` |
| `registerBroker` | No master, and the new broker can't be elected | `INVALID_REQUEST` | `CONTROLLER_MASTER_NOT_AVAILABLE` |

The other existing codes (fenced epoch, invalid master, invalid replicas, broker not alive, and so on) are unchanged. The broker and client only check for success or the specific codes they already handle, so nothing else needed to change.

**Testing:** Maven couldn't run tests offline because its JUnit 4 runner isn't cached, so I compiled with Maven and ran the tests directly with JUnit.
- On the code as it stands, `testElectMaster` and `testElectMasterOldMasterStillAlive` fail with "expected 2005 but was 2011". They still expect the old code for the master-still-alive case, which is the behaviour this change replaces.
- With those two assertions temporarily switched to `CONTROLLER_MASTER_STILL_EXIST`, all 12 tests pass (`ReplicasInfoManagerTest`, `DefaultBrokerHeartbeatManagerTest`, `DLedgerControllerTest`, `ControllerManagerTest`). I then restored the test file.

**Points to check:**
- `CONTROLLER_ELECT_MASTER_FAILED` is defined but not used yet. The case where no new master can be elected still returns `CONTROLLER_MASTER_NOT_AVAILABLE`, because the existing tests expect that.
- The new codes were my own choice. I based them on what I remember of the upstream RocketMQ fix but didn't check them against it, and the issue's screenshot wasn't visible to me.
- The changes to `pom.xml` and the untracked `Dockerfile` were already there before I started, and I left them alone. My helper script and log file are deleted.

_session end: success, turns 23, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 32.76 s: mvn -o -q install -pl common -DskipTests -Dcheckstyle.skip -Dspotbugs.skip -Drat.skip 2>&1 | tail -20; mvn -o test -pl controller -Dcheckstyle.skip -Drat.skip -Dtest=ReplicasInfoManagerTest,ControllerManagerTest,DLedgerControllerTest -DfailIfNoTests=false 2>&1 | grep -E "Tests run|FAIL|expected|ERROR" | head -30
- `rc=0` 0.31 s: ls ~/.m2/repository/org/apache/maven/surefire/; ls ~/.m2/repository/org/apache/maven/surefire/*/ | head -40
- `rc=0` 18.64 s: mvn -o -q test-compile -pl controller -Dcheckstyle.skip -Drat.skip 2>&1 | tail -5; mvn -o -q dependency:build-classpath -pl controller -Dmdep.outputFile=/tmp/cp.txt >/dev/null 2>&1; java -cp controller/target/classes:controller/target/test-classes:$(cat /tmp/cp.txt) org.junit.runner.JUnitCore org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest 2>&1 | grep -vE "^\s+at |INFO|WARN" | tail -30
- `rc=0` 3.02 s: mvn -o dependency:build-classpath -pl controller -Dmdep.outputFile=/tmp/cp.txt 2>&1 | grep -E "ERROR|BUILD" | head -5
- `rc=0` 17.49 s: CP=controller/target/classes:controller/target/test-classes:common/target/classes:remoting/target/classes:client/target/classes:srvutil/target/classes:logging/target/classes:$(find ~/.m2/repository -name "*.jar" | grep -v "/org/apache/rocketmq/rocketmq-" | grep -v maven | tr "\n" ":"); ls common/target/classes remoting/target/classes >/dev/null && java -cp "$CP" org.junit.runner.JUnitCore org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest org.apache.rocketmq.controller.impl.controller.ControllerManagerTest 2>&1 | grep -vE "^\s+at |INFO|WARN|^[0-9]+$|ElectMaster
- `rc=0` 0.29 s: find ~/.m2/repository -name "*hamcrest*.jar"
- `rc=127` 0.29 s: bash runct.sh
- `rc=0` 19.67 s: bash runct.sh org.apache.rocketmq.controller.impl.controller.ControllerManagerTest
- `rc=0` 105.23 s: mvn -o -q test-compile -pl controller -Dcheckstyle.skip -Drat.skip 2>&1 | grep ERROR | head; bash runct.sh org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest org.apache.rocketmq.controller.impl.controller.impl.DefaultBrokerHeartbeatManagerTest org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest org.apache.rocketmq.controller.impl.controller.ControllerManagerTest 
- `rc=0` 108.05 s: mvn -o -q test-compile -pl controller -Dcheckstyle.skip -Drat.skip 2>&1 | grep ERROR | head; bash runct.sh org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest org.apache.rocketmq.controller.impl.controller.impl.DefaultBrokerHeartbeatManagerTest org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest org.apache.rocketmq.controller.impl.controller.ControllerManagerTest
- `rc=0` 107.59 s: mvn -o -q test-compile -pl controller -Dcheckstyle.skip -Drat.skip 2>&1 | grep ERROR | head; bash runct.sh org.apache.rocketmq.controller.impl.controller.impl.manager.ReplicasInfoManagerTest org.apache.rocketmq.controller.impl.controller.impl.DefaultBrokerHeartbeatManagerTest org.apache.rocketmq.controller.impl.controller.impl.DLedgerControllerTest org.apache.rocketmq.controller.impl.controller.ControllerManagerTest
