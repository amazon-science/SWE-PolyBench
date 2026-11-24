# Instance: apache__rocketmq-5062

- Final resolved (evaluator, logs/apache__rocketmq-5062_result.json): True
- Run state: DONE
- One attempt. Duration 359.1 s, turns 25, actor cost $1.14013, container commands 8
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/apache__rocketmq-5062/repo
</uploaded_files>
I've uploaded a Java code repository in the directory /work/apache__rocketmq-5062/repo. Consider the following issue description:

<issue_description>
Support escaping transactional messages in slave-acting-master mode
**FEATURE REQUEST**

In [RIP-32](https://github.com/apache/rocketmq/wiki/RIP-32-Slave-Acting-Master-Mode), Slave Acting Master Mode is supported and the escape of the transactional messages need to be supported. 

Below is a simple implementation of escaping transactional messages:

If a slave node is acting as master,
- EndTransaction requests (including commit and rollback) are denied.
- When checking status of half messages, escape half messages to an available master directly, without checking transaction status actually. There is a small trick: If a half message is sent to a local master, just append it to half topic; if sent to a remote master, the half message should be restored to original real message, because sending messages to a system topic is forbidden.

This implemetation keeps read-only sematics of slaves, so that no new half messages or op messages will be created in slave acting as master, all actual checking processes of half messages are delivered to master.

Previously there are several proposals, such as #4427, #4477, etc. They do provide good references and I truly appreciate the authors.



</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/apache__rocketmq-5062/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/apache__rocketmq-5062/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/apache__rocketmq-5062/bin/envrun 'git status --short && ls'
Edits you make under /work/apache__rocketmq-5062/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
git log --oneline -2 && ls broker/src/main/java/org/apache/rocketmq/broker/transaction/ broker/src/main/java/org/apache/rocketmq/broker/transaction/queue && grep -rn "escape\|Escape" --include=*.java broker/src/main | head -40
```

tool result:

```
613d483a1 fix-ysc：修复文件预热 (#4903)
d40765db4 [ISSUE #5138] Do not throw exception in order producer demo (#5185)
broker/src/main/java/org/apache/rocketmq/broker/transaction/:
AbstractTransactionalMessageCheckListener.java
OperationResult.java
TransactionalMessageCheckService.java
TransactionalMessageService.java
queue

broker/src/main/java/org/apache/rocketmq/broker/transaction/queue:
DefaultTransactionalMessageCheckListener.java
GetResult.java
TransactionalMessageBridge.java
TransactionalMessageServiceImpl.java
TransactionalMessageUtil.java
(eval):1: no matches found: --include=*.java
```

**tool call: Bash**

```bash
grep -rn "escape\|Escape" broker/src/main --include='*.java' | head -40; cat broker/src/main/java/org/apache/rocketmq/broker/transaction/AbstractTransactionalMessageCheckListener.java
```

tool result:

```
broker/src/main/java/org/apache/rocketmq/broker/BrokerController.java:55:import org.apache.rocketmq.broker.failover.EscapeBridge;
broker/src/main/java/org/apache/rocketmq/broker/BrokerController.java:253:    protected EscapeBridge escapeBridge;
broker/src/main/java/org/apache/rocketmq/broker/BrokerController.java:386:        this.escapeBridge = new EscapeBridge(this);
broker/src/main/java/org/apache/rocketmq/broker/BrokerController.java:742:                    this.timerMessageStore.registerEscapeBridgeHook(msg -> escapeBridge.putMessage(msg));
broker/src/main/java/org/apache/rocketmq/broker/BrokerController.java:1355:        if (this.escapeBridge != null) {
broker/src/main/java/org/apache/rocketmq/broker/BrokerController.java:1356:            escapeBridge.shutdown();
broker/src/main/java/org/apache/rocketmq/broker/BrokerController.java:1493:        if (this.escapeBridge != null) {
broker/src/main/java/org/apache/rocketmq/broker/BrokerController.java:1494:            this.escapeBridge.start();
broker/src/main/java/org/apache/rocketmq/broker/BrokerController.java:2208:    public EscapeBridge getEscapeBridge() {
broker/src/main/java/org/apache/rocketmq/broker/BrokerController.java:2209:        return escapeBridge;
broker/src/main/java/org/apache/rocketmq/broker/schedule/ScheduleMessageService.java:557:                brokerController.getEscapeBridge().asyncPutMessage(msgInner);
broker/src/main/java/org/apache/rocketmq/broker/schedule/ScheduleMessageService.java:789:                PutMessageResult result = ScheduleMessageService.this.brokerController.getEscapeBridge().putMessage(msgInner);
broker/src/main/java/org/apache/rocketmq/broker/processor/PopReviveService.java:109:        PutMessageResult putMessageResult = brokerController.getEscapeBridge().putMessageToSpecificQueue(msgInner);
broker/src/main/java/org/apache/rocketmq/broker/processor/PopReviveService.java:180:        return this.brokerController.getEscapeBridge().getMessage(topic, offset, queueId, brokerName);
broker/src/main/java/org/apache/rocketmq/broker/processor/PopBufferMergeService.java:542:        PutMessageResult putMessageResult = brokerController.getEscapeBridge().putMessageToSpecificQueue(msgInner);
broker/src/main/java/org/apache/rocketmq/broker/processor/PopBufferMergeService.java:586:        PutMessageResult putMessageResult = brokerController.getEscapeBridge().putMessageToSpecificQueue(msgInner);
broker/src/main/java/org/apache/rocketmq/broker/processor/PopBufferMergeService.java:618:        PutMessageResult putMessageResult = brokerController.getEscapeBridge().putMessageToSpecificQueue(msgInner);
broker/src/main/java/org/apache/rocketmq/broker/processor/AckMessageProcessor.java:204:        PutMessageResult putMessageResult = this.brokerController.getEscapeBridge().putMessageToSpecificQueue(msgInner);
broker/src/main/java/org/apache/rocketmq/broker/processor/ChangeInvisibleTimeProcessor.java:157:        PutMessageResult putMessageResult = this.brokerController.getEscapeBridge().putMessageToSpecificQueue(msgInner);
broker/src/main/java/org/apache/rocketmq/broker/processor/ChangeInvisibleTimeProcessor.java:192:        PutMessageResult putMessageResult = this.brokerController.getEscapeBridge().putMessageToSpecificQueue(msgInner);
broker/src/main/java/org/apache/rocketmq/broker/topic/TopicRouteInfoManager.java:88:        final Set<String> topicSetForEscapeBridge = this.topicRouteTable.keySet();
broker/src/main/java/org/apache/rocketmq/broker/topic/TopicRouteInfoManager.java:89:        final Set<String> topicsAll = Sets.union(topicSetForPopAssignment, topicSetForEscapeBridge);
broker/src/main/java/org/apache/rocketmq/broker/topic/TopicRouteInfoManager.java:92:            boolean isNeedUpdatePublishInfo = topicSetForEscapeBridge.contains(topic);
broker/src/main/java/org/apache/rocketmq/broker/failover/EscapeBridge.java:54:public class EscapeBridge {
broker/src/main/java/org/apache/rocketmq/broker/failover/EscapeBridge.java:65:    public EscapeBridge(BrokerController brokerController) {
broker/src/main/java/org/apache/rocketmq/broker/failover/EscapeBridge.java:72:        if (brokerController.getBrokerConfig().isEnableSlaveActingMaster() && brokerController.getBrokerConfig().isEnableRemoteEscape()) {
broker/src/main/java/org/apache/rocketmq/broker/failover/EscapeBridge.java:80:                new ThreadFactoryImpl("AsyncEscapeBridgeExecutor_", this.brokerController.getBrokerIdentity())
broker/src/main/java/org/apache/rocketmq/broker/failover/EscapeBridge.java:97:            && this.brokerController.getBrokerConfig().isEnableRemoteEscape()) {
broker/src/main/java/org/apache/rocketmq/broker/failover/EscapeBridge.java:108:            LOG.warn("Put message failed, enableSlaveActingMaster={}, enableRemoteEscape={}.",
broker/src/main/java/org/apache/rocketmq/broker/failover/EscapeBridge.java:109:                this.brokerController.getBrokerConfig().isEnableSlaveActingMaster(), this.brokerController.getBrokerConfig().isEnableRemoteEscape());
broker/src/main/java/org/apache/rocketmq/broker/failover/EscapeBridge.java:157:            && this.brokerController.getBrokerConfig().isEnableRemoteEscape()) {
broker/src/main/java/org/apache/rocketmq/broker/failover/EscapeBridge.java:182:            LOG.warn("Put message failed, enableSlaveActingMaster={}, enableRemoteEscape={}.",
broker/src/main/java/org/apache/rocketmq/broker/failover/EscapeBridge.java:183:                this.brokerController.getBrokerConfig().isEnableSlaveActingMaster(), this.brokerController.getBrokerConfig().isEnableRemoteEscape());
broker/src/main/java/org/apache/rocketmq/broker/failover/EscapeBridge.java:206:            && this.brokerController.getBrokerConfig().isEnableRemoteEscape()) {
broker/src/main/java/org/apache/rocketmq/broker/failover/EscapeBridge.java:235:            LOG.warn("Put message to specific queue failed, enableSlaveActingMaster={}, enableRemoteEscape={}.",
broker/src/main/java/org/apache/rocketmq/broker/failover/EscapeBridge.java:236:           
[... 5420 more characters not shown]
```

**tool call: Bash**

```bash
git status; grep -rln "Transaction" broker/src/test | head; 
```

tool result:

```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   pom.xml

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Dockerfile

no changes added to commit (use "git add" and/or "git commit -a")
broker/src/test/resources/META-INF/service/org.apache.rocketmq.broker.transaction.AbstractTransactionalMessageCheckListener
broker/src/test/resources/META-INF/service/org.apache.rocketmq.broker.transaction.TransactionalMessageService
broker/src/test/java/org/apache/rocketmq/broker/transaction/queue/TransactionalMessageServiceImplTest.java
broker/src/test/java/org/apache/rocketmq/broker/transaction/queue/TransactionalMessageBridgeTest.java
broker/src/test/java/org/apache/rocketmq/broker/transaction/queue/DefaultTransactionalMessageCheckListenerTest.java
broker/src/test/java/org/apache/rocketmq/broker/util/ServiceProviderTest.java
broker/src/test/java/org/apache/rocketmq/broker/util/LogTransactionalMessageCheckListener.java
broker/src/test/java/org/apache/rocketmq/broker/util/TransactionalMessageServiceImpl.java
broker/src/test/java/org/apache/rocketmq/broker/processor/SendMessageProcessorTest.java
broker/src/test/java/org/apache/rocketmq/broker/processor/EndTransactionProcessorTest.java
```

**tool call: Bash**

```bash
cd broker/src/test/java/org/apache/rocketmq/broker; grep -n "escape\|Escape\|SlaveActing\|MinBrokerId\|renew\|buildTransactionalMessage" -r . | head -40; cat ../../../../../main/java/org/apache/rocketmq/broker/failover/EscapeBridge.java
```

tool result:

```
Exit code 1
./transaction/queue/TransactionalMessageServiceImplTest.java:136:        when(bridge.renewHalfMessageInner(any(MessageExtBrokerInner.class))).thenReturn(createMessageBrokerInner());
./transaction/queue/TransactionalMessageBridgeTest.java:154:        MessageExtBrokerInner msgInner = transactionBridge.renewImmunityHalfMessageInner(messageExt);
./transaction/queue/TransactionalMessageBridgeTest.java:168:        MessageExt messageExtRes = transactionBridge.renewHalfMessageInner(messageExt);
./schedule/ScheduleMessageServiceTest.java:36:import org.apache.rocketmq.broker.failover.EscapeBridge;
./schedule/ScheduleMessageServiceTest.java:132:        EscapeBridge escapeBridge = new EscapeBridge(brokerController);
./schedule/ScheduleMessageServiceTest.java:133:        Mockito.when(brokerController.getEscapeBridge()).thenReturn(escapeBridge);
./processor/ChangeInvisibleTimeProcessorTest.java:25:import org.apache.rocketmq.broker.failover.EscapeBridge;
./processor/ChangeInvisibleTimeProcessorTest.java:80:    private EscapeBridge escapeBridge = new EscapeBridge(this.brokerController);
./processor/ChangeInvisibleTimeProcessorTest.java:89:        Field ebField = BrokerController.class.getDeclaredField("escapeBridge");
./processor/ChangeInvisibleTimeProcessorTest.java:91:        ebField.set(brokerController, this.escapeBridge);
./processor/ChangeInvisibleTimeProcessorTest.java:111:        when(escapeBridge.putMessageToSpecificQueue(any(MessageExtBrokerInner.class))).thenReturn(new PutMessageResult(PutMessageStatus.PUT_OK, new AppendMessageResult(AppendMessageStatus.PUT_OK)));
./processor/AckMessageProcessorTest.java:25:import org.apache.rocketmq.broker.failover.EscapeBridge;
./processor/AckMessageProcessorTest.java:87:        EscapeBridge escapeBridge = new EscapeBridge(brokerController);
./processor/AckMessageProcessorTest.java:88:        Mockito.when(brokerController.getEscapeBridge()).thenReturn(escapeBridge);
./failover/EscapeBridgeTest.java:45:public class EscapeBridgeTest {
./failover/EscapeBridgeTest.java:47:    private EscapeBridge escapeBridge;
./failover/EscapeBridgeTest.java:79:        escapeBridge = new EscapeBridge(brokerController);
./failover/EscapeBridgeTest.java:82:        brokerConfig.setEnableSlaveActingMaster(true);
./failover/EscapeBridgeTest.java:83:        brokerConfig.setEnableRemoteEscape(true);
./failover/EscapeBridgeTest.java:84:        escapeBridge.start();
./failover/EscapeBridgeTest.java:90:        escapeBridge.shutdown();
./failover/EscapeBridgeTest.java:101:        final PutMessageResult result1 = escapeBridge.putMessage(messageExtBrokerInner);
./failover/EscapeBridgeTest.java:108:        Assertions.assertThatCode(() -> escapeBridge.putMessage(messageExtBrokerInner)).doesNotThrowAnyException();
./failover/EscapeBridgeTest.java:111:        final PutMessageResult result3 = escapeBridge.putMessage(messageExtBrokerInner);
./failover/EscapeBridgeTest.java:120:        Assertions.assertThatCode(() -> escapeBridge.asyncPutMessage(messageExtBrokerInner)).doesNotThrowAnyException();
./failover/EscapeBridgeTest.java:124:        Assertions.assertThatCode(() -> escapeBridge.asyncPutMessage(messageExtBrokerInner)).doesNotThrowAnyException();
./failover/EscapeBridgeTest.java:127:        Assertions.assertThatCode(() -> escapeBridge.asyncPutMessage(messageExtBrokerInner)).doesNotThrowAnyException();
./failover/EscapeBridgeTest.java:133:        final PutMessageResult result1 = escapeBridge.putMessageToSpecificQueue(messageExtBrokerInner);
./failover/EscapeBridgeTest.java:139:        Assertions.assertThatCode(() -> escapeBridge.putMessageToSpecificQueue(messageExtBrokerInner)).doesNotThrowAnyException();
./failover/EscapeBridgeTest.java:146:        Assertions.assertThatCode(() -> escapeBridge.putMessage(messageExtBrokerInner)).doesNotThrowAnyException();
./failover/EscapeBridgeTest.java:148:        Assertions.assertThatCode(() -> escapeBridge.getMessage(TEST_TOPIC, 0, DEFAULT_QUEUE_ID, BROKER_NAME)).doesNotThrowAnyException();
./failover/EscapeBridgeTest.java:153:        Assertions.assertThatCode(() -> escapeBridge.getMessageFromRemote(TEST_TOPIC, 1, DEFAULT_QUEUE_ID, BROKER_NAME)).doesNotThrowAnyException();
./failover/EscapeBridgeTest.java:163:        Assertions.assertThatCode(() -> escapeBridge.decodeMsgList(getMessageResult)).doesNotThrowAnyException();
cat: ../../../../../main/java/org/apache/rocketmq/broker/failover/EscapeBridge.java: No such file or directory
```

**tool call: Bash**

```bash
cd broker/src/main/java/org/apache/rocketmq/broker; cat failover/EscapeBridge.java | sed -n 1,260p
```

tool result:

```
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

package org.apache.rocketmq.broker.failover;

import java.nio.ByteBuffer;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;

import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;
import org.apache.commons.lang3.StringUtils;
import org.apache.rocketmq.broker.BrokerController;
import org.apache.rocketmq.client.consumer.PullResult;
import org.apache.rocketmq.client.consumer.PullStatus;
import org.apache.rocketmq.client.exception.MQBrokerException;
import org.apache.rocketmq.client.impl.producer.TopicPublishInfo;
import org.apache.rocketmq.client.producer.SendResult;
import org.apache.rocketmq.client.producer.SendStatus;
import org.apache.rocketmq.common.MixAll;
import org.apache.rocketmq.common.ThreadFactoryImpl;
import org.apache.rocketmq.common.constant.LoggerName;
import org.apache.rocketmq.common.message.MessageConst;
import org.apache.rocketmq.common.message.MessageDecoder;
import org.apache.rocketmq.common.message.MessageExt;
import org.apache.rocketmq.common.message.MessageExtBrokerInner;
import org.apache.rocketmq.common.message.MessageQueue;
import org.apache.rocketmq.logging.InternalLogger;
import org.apache.rocketmq.logging.InternalLoggerFactory;
import org.apache.rocketmq.remoting.exception.RemotingException;
import org.apache.rocketmq.store.GetMessageResult;
import org.apache.rocketmq.store.MessageStore;
import org.apache.rocketmq.store.PutMessageResult;
import org.apache.rocketmq.store.PutMessageStatus;

public class EscapeBridge {
    protected static final InternalLogger LOG = InternalLoggerFactory.getLogger(LoggerName.BROKER_LOGGER_NAME);
    private static final long SEND_TIMEOUT = 3000L;
    private static final long DEFAULT_PULL_TIMEOUT_MILLIS = 1000 * 10L;
    private final String innerProducerGroupName;
    private final String innerConsumerGroupName;

    private final BrokerController brokerController;

    private ExecutorService defaultAsyncSenderExecutor;

    public EscapeBridge(BrokerController brokerController) {
        this.brokerController = brokerController;
        this.innerProducerGroupName = "InnerProducerGroup_" + brokerController.getBrokerConfig().getBrokerName() + "_" + brokerController.getBrokerConfig().getBrokerId();
        this.innerConsumerGroupName = "InnerConsumerGroup_" + brokerController.getBrokerConfig().getBrokerName() + "_" + brokerController.getBrokerConfig().getBrokerId();
    }

    public void start() throws Exception {
        if (brokerController.getBrokerConfig().isEnableSlaveActingMaster() && brokerController.getBrokerConfig().isEnableRemoteEscape()) {
            final BlockingQueue<Runnable> asyncSenderThreadPoolQueue = new LinkedBlockingQueue<>(50000);
            this.defaultAsyncSenderExecutor = new ThreadPoolExecutor(
                Runtime.getRuntime().availableProcessors(),
                Runtime.getRuntime().availableProcessors(),
                1000 * 60,
                TimeUnit.MILLISECONDS,
                asyncSenderThreadPoolQueue,
                new ThreadFactoryImpl("AsyncEscapeBridgeExecutor_", this.brokerController.getBrokerIdentity())
            );
            LOG.info("init executor for escaping messages asynchronously success.");
        }
    }

    public void shutdown() {
        if (null != this.defaultAsyncSenderExecutor) {
            this.defaultAsyncSenderExecutor.shutdown();
        }
    }

    public PutMessageResult putMessage(MessageExtBrokerInner messageExt) {
        BrokerController masterBroker = this.brokerController.peekMasterBroker();
        if (masterBroker != null) {
            return masterBroker.getMessageStore().putMessage(messageExt);
        } else if (this.brokerController.getBrokerConfig().isEnableSlaveActingMaster()
            && this.brokerController.getBrokerConfig().isEnableRemoteEscape()) {

            try {
                messageExt.setWaitStoreMsgOK(false);
                final SendResult sendResult = putMessageToRemoteBroker(messageExt);
                return transformSendResult2PutResult(sendResult);
            } catch (Exception e) {
                LOG.error("sendMessageInFailover to remote failed", e);
                return new PutMessageResult(PutMessageStatus.PUT_TO_REMOTE_BROKER_FAIL, null, true);
            }
        } else {
            LOG.warn("Put message failed, enableSlaveActingMaster={}, enableRemoteEscape={}.",
                this.brokerController.getBrokerConfig().isEnableSlaveActingMaster(), this.brokerController.getBrokerConfig().isEnableRemoteEscape());
            return new PutMessageResult(PutMessageStatus.SERVICE_NOT_AVAILABLE, null);
        }
    }

    private SendResult putMessageToRemoteBroker(MessageExtBrokerInner messageExt) {
        final TopicPublishInfo topicPublishInfo = this.brokerController.getTopicRouteInfoManager().tryToFindTopicPublishInfo(messageExt.getTopic());
        if (null == topicPublishInfo || !topicPublishInfo.ok()) {
            LOG.warn("putMessageToRemoteBroker: no route info of topic {} when escaping me
[... 7970 more characters not shown]
```

**tool call: Bash**

```bash
cd broker/src/main/java/org/apache/rocketmq/broker 2>/dev/null; pwd; cat transaction/queue/TransactionalMessageServiceImpl.java | sed -n 1,330p; cat transaction/queue/TransactionalMessageUtil.java
```

tool result:

```
/work/apache__rocketmq-5062/repo/broker/src/main/java/org/apache/rocketmq/broker
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
package org.apache.rocketmq.broker.transaction.queue;

import org.apache.rocketmq.broker.transaction.AbstractTransactionalMessageCheckListener;
import org.apache.rocketmq.broker.transaction.OperationResult;
import org.apache.rocketmq.broker.transaction.TransactionalMessageService;
import org.apache.rocketmq.client.consumer.PullResult;
import org.apache.rocketmq.client.consumer.PullStatus;
import org.apache.rocketmq.common.constant.LoggerName;
import org.apache.rocketmq.common.message.MessageConst;
import org.apache.rocketmq.common.message.MessageExt;
import org.apache.rocketmq.common.message.MessageQueue;
import org.apache.rocketmq.common.protocol.ResponseCode;
import org.apache.rocketmq.common.protocol.header.EndTransactionRequestHeader;
import org.apache.rocketmq.common.topic.TopicValidator;
import org.apache.rocketmq.logging.InternalLogger;
import org.apache.rocketmq.logging.InternalLoggerFactory;
import org.apache.rocketmq.common.message.MessageExtBrokerInner;
import org.apache.rocketmq.store.PutMessageResult;
import org.apache.rocketmq.store.PutMessageStatus;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Set;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ConcurrentHashMap;

public class TransactionalMessageServiceImpl implements TransactionalMessageService {
    private static final InternalLogger log = InternalLoggerFactory.getLogger(LoggerName.TRANSACTION_LOGGER_NAME);

    private TransactionalMessageBridge transactionalMessageBridge;

    private static final int PULL_MSG_RETRY_NUMBER = 1;

    private static final int MAX_PROCESS_TIME_LIMIT = 60000;

    private static final int MAX_RETRY_COUNT_WHEN_HALF_NULL = 1;

    public TransactionalMessageServiceImpl(TransactionalMessageBridge transactionBridge) {
        this.transactionalMessageBridge = transactionBridge;
    }

    private ConcurrentHashMap<MessageQueue, MessageQueue> opQueueMap = new ConcurrentHashMap<>();

    @Override
    public CompletableFuture<PutMessageResult> asyncPrepareMessage(MessageExtBrokerInner messageInner) {
        return transactionalMessageBridge.asyncPutHalfMessage(messageInner);
    }

    @Override
    public PutMessageResult prepareMessage(MessageExtBrokerInner messageInner) {
        return transactionalMessageBridge.putHalfMessage(messageInner);
    }

    private boolean needDiscard(MessageExt msgExt, int transactionCheckMax) {
        String checkTimes = msgExt.getProperty(MessageConst.PROPERTY_TRANSACTION_CHECK_TIMES);
        int checkTime = 1;
        if (null != checkTimes) {
            checkTime = getInt(checkTimes);
            if (checkTime >= transactionCheckMax) {
                return true;
            } else {
                checkTime++;
            }
        }
        msgExt.putUserProperty(MessageConst.PROPERTY_TRANSACTION_CHECK_TIMES, String.valueOf(checkTime));
        return false;
    }

    private boolean needSkip(MessageExt msgExt) {
        long valueOfCurrentMinusBorn = System.currentTimeMillis() - msgExt.getBornTimestamp();
        if (valueOfCurrentMinusBorn
            > transactionalMessageBridge.getBrokerController().getMessageStoreConfig().getFileReservedTime()
            * 3600L * 1000) {
            log.info("Half message exceed file reserved time ,so skip it.messageId {},bornTime {}",
                msgExt.getMsgId(), msgExt.getBornTimestamp());
            return true;
        }
        return false;
    }

    private boolean putBackHalfMsgQueue(MessageExt msgExt, long offset) {
        PutMessageResult putMessageResult = putBackToHalfQueueReturnResult(msgExt);
        if (putMessageResult != null
            && putMessageResult.getPutMessageStatus() == PutMessageStatus.PUT_OK) {
            msgExt.setQueueOffset(
                putMessageResult.getAppendMessageResult().getLogicsOffset());
            msgExt.setCommitLogOffset(
                putMessageResult.getAppendMessageResult().getWroteOffset());
            msgExt.setMsgId(putMessageResult.getAppendMessageResult().getMsgId());
            log.debug(
                "Send check message, the offset={} restored in queueOffset={} "
                    + "commitLogOffset={} "
                    + "newMsgId={} realMsgId={} topic={}",
                offset, msgExt.getQueueOffset(), msgExt.getCommitLogOffset(), msgExt.getMsgId(),
                msgExt.getUserProperty(MessageConst.PROPERTY_UNIQ_CLIENT_MESSAGE_ID_KEYIDX),
                msgExt.getTopic());
            return true;
        } else {
            log.error(
                "PutBackToHalfQueueReturnResult write failed, topic: {}, queueId: {}, "
                    + "msgId: {}",
                msgExt.getTopic(), msgExt.getQueueId(), msgExt.getMsgId());
            return false;
        }
    }

    @Override
    public void check(long transactionTimeout, int transactionCheckMax,
        AbstractTransactionalMessageCheckListener listener) {
        try {
            String
[... 12291 more characters not shown]
```

**assistant:** Now let me look at the end-transaction processor and the bridge.

**tool call: Bash**

```bash
cd broker/src/main/java/org/apache/rocketmq/broker; sed -n 1,140p processor/EndTransactionProcessor.java; grep -n "public\|LOGGER\|^import" transaction/queue/TransactionalMessageBridge.java; grep -n "MinBrokerId\|isSpecialServiceRunning\|peekMasterBroker\|getBrokerIdentity()" BrokerController.java | head
```

tool result:

```
(eval):cd:1: no such file or directory: broker/src/main/java/org/apache/rocketmq/broker
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
package org.apache.rocketmq.broker.processor;

import io.netty.channel.ChannelHandlerContext;
import org.apache.rocketmq.broker.BrokerController;
import org.apache.rocketmq.broker.transaction.OperationResult;
import org.apache.rocketmq.common.TopicFilterType;
import org.apache.rocketmq.common.constant.LoggerName;
import org.apache.rocketmq.common.message.MessageAccessor;
import org.apache.rocketmq.common.message.MessageConst;
import org.apache.rocketmq.common.message.MessageDecoder;
import org.apache.rocketmq.common.message.MessageExt;
import org.apache.rocketmq.common.protocol.ResponseCode;
import org.apache.rocketmq.common.protocol.header.EndTransactionRequestHeader;
import org.apache.rocketmq.common.sysflag.MessageSysFlag;
import org.apache.rocketmq.logging.InternalLogger;
import org.apache.rocketmq.logging.InternalLoggerFactory;
import org.apache.rocketmq.remoting.common.RemotingHelper;
import org.apache.rocketmq.remoting.exception.RemotingCommandException;
import org.apache.rocketmq.remoting.netty.NettyRequestProcessor;
import org.apache.rocketmq.remoting.protocol.RemotingCommand;
import org.apache.rocketmq.common.message.MessageExtBrokerInner;
import org.apache.rocketmq.store.PutMessageResult;
import org.apache.rocketmq.store.config.BrokerRole;

/**
 * EndTransaction processor: process commit and rollback message
 */
public class EndTransactionProcessor implements NettyRequestProcessor {
    private static final InternalLogger LOGGER = InternalLoggerFactory.getLogger(LoggerName.TRANSACTION_LOGGER_NAME);
    private final BrokerController brokerController;

    public EndTransactionProcessor(final BrokerController brokerController) {
        this.brokerController = brokerController;
    }

    @Override
    public RemotingCommand processRequest(ChannelHandlerContext ctx, RemotingCommand request) throws
        RemotingCommandException {
        final RemotingCommand response = RemotingCommand.createResponseCommand(null);
        final EndTransactionRequestHeader requestHeader =
            (EndTransactionRequestHeader) request.decodeCommandCustomHeader(EndTransactionRequestHeader.class);
        LOGGER.debug("Transaction request:{}", requestHeader);
        if (BrokerRole.SLAVE == brokerController.getMessageStoreConfig().getBrokerRole()) {
            response.setCode(ResponseCode.SLAVE_NOT_AVAILABLE);
            LOGGER.warn("Message store is slave mode, so end transaction is forbidden. ");
            return response;
        }

        if (requestHeader.getFromTransactionCheck()) {
            switch (requestHeader.getCommitOrRollback()) {
                case MessageSysFlag.TRANSACTION_NOT_TYPE: {
                    LOGGER.warn("Check producer[{}] transaction state, but it's pending status."
                            + "RequestHeader: {} Remark: {}",
                        RemotingHelper.parseChannelRemoteAddr(ctx.channel()),
                        requestHeader.toString(),
                        request.getRemark());
                    return null;
                }

                case MessageSysFlag.TRANSACTION_COMMIT_TYPE: {
                    LOGGER.warn("Check producer[{}] transaction state, the producer commit the message."
                            + "RequestHeader: {} Remark: {}",
                        RemotingHelper.parseChannelRemoteAddr(ctx.channel()),
                        requestHeader.toString(),
                        request.getRemark());

                    break;
                }

                case MessageSysFlag.TRANSACTION_ROLLBACK_TYPE: {
                    LOGGER.warn("Check producer[{}] transaction state, the producer rollback the message."
                            + "RequestHeader: {} Remark: {}",
                        RemotingHelper.parseChannelRemoteAddr(ctx.channel()),
                        requestHeader.toString(),
                        request.getRemark());
                    break;
                }
                default:
                    return null;
            }
        } else {
            switch (requestHeader.getCommitOrRollback()) {
                case MessageSysFlag.TRANSACTION_NOT_TYPE: {
                    LOGGER.warn("The producer[{}] end transaction in sending message,  and it's pending status."
                            + "RequestHeader: {} Remark: {}",
                        RemotingHelper.parseChannelRemoteAddr(ctx.channel()),
                        requestHeader.toString(),
                        request.getRemark());
                    return null;
                }

                case MessageSysFlag.TRANSACTION_COMMIT_TYPE: {
                    break;
                }

                case MessageSysFlag.TRANSACTION_ROLLBACK_TYPE: {
                    LOGGER.warn("The producer[{}] end transaction in sending message, rollback the message."
                            + "RequestHeader: {} Remark: {}",
                        RemotingHelper.parseChannelRemoteAddr(ctx.channel()),
                        requestHeader.toString(),
                        request.getRemark());
                    break;
            
[... 6140 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5062/repo/broker/src/main/java/org/apache/rocketmq/broker; grep -n "transactionalMessageCheckService\|MinBrokerId\|isIsolated\|SpecialService\|changeTransaction" BrokerController.java | head -40; sed -n 190,270p transaction/queue/TransactionalMessageBridge.java
```

tool result:

```
244:    protected TransactionalMessageCheckService transactionalMessageCheckService;
257:    protected volatile boolean isIsolated = false;
900:        this.transactionalMessageCheckService = new TransactionalMessageCheckService(this);
1347:        if (this.transactionalMessageCheckService != null) {
1348:            this.transactionalMessageCheckService.shutdown(false);
1514:            isIsolated = true;
1523:        if (!isIsolated && !this.messageStoreConfig.isEnableDLegerCommitLog() && !this.messageStoreConfig.isDuplicationEnable()) {
1524:            changeSpecialServiceStatus(this.brokerConfig.getBrokerId() == MixAll.MASTER_ID);
1536:                    if (isIsolated) {
1575:                if (isIsolated) {
1746:        if (!this.isIsolated) {
1802:        this.changeSpecialServiceStatus(this.brokerConfig.getBrokerId() == minBrokerId);
1805:        isIsolated = false;
1811:        this.changeSpecialServiceStatus(this.brokerConfig.getBrokerId() == MixAll.MASTER_ID);
1814:        isIsolated = false;
1819:        isIsolated = true;
1820:        this.changeSpecialServiceStatus(false);
1823:    public boolean isSpecialServiceRunning() {
1881:        this.changeSpecialServiceStatus(this.brokerConfig.getBrokerId() == this.minBrokerIdInGroup);
1937:    public void changeSpecialServiceStatus(boolean shouldStart) {
1947:        changeTransactionCheckServiceStatus(shouldStart);
1955:    private synchronized void changeTransactionCheckServiceStatus(boolean shouldStart) {
1959:                this.transactionalMessageCheckService.start();
1961:                this.transactionalMessageCheckService.shutdown(true);
2122:        return transactionalMessageCheckService;
2126:        TransactionalMessageCheckService transactionalMessageCheckService) {
2127:        this.transactionalMessageCheckService = transactionalMessageCheckService;
2188:    public long getMinBrokerIdInGroup() {
2241:        isIsolated = isolated;
2244:    public boolean isIsolated() {
2245:        return this.isIsolated;
        }

        return foundList;
    }

    public PutMessageResult putHalfMessage(MessageExtBrokerInner messageInner) {
        return store.putMessage(parseHalfMessageInner(messageInner));
    }

    public CompletableFuture<PutMessageResult> asyncPutHalfMessage(MessageExtBrokerInner messageInner) {
        return store.asyncPutMessage(parseHalfMessageInner(messageInner));
    }

    private MessageExtBrokerInner parseHalfMessageInner(MessageExtBrokerInner msgInner) {
        MessageAccessor.putProperty(msgInner, MessageConst.PROPERTY_REAL_TOPIC, msgInner.getTopic());
        MessageAccessor.putProperty(msgInner, MessageConst.PROPERTY_REAL_QUEUE_ID,
            String.valueOf(msgInner.getQueueId()));
        msgInner.setSysFlag(
            MessageSysFlag.resetTransactionValue(msgInner.getSysFlag(), MessageSysFlag.TRANSACTION_NOT_TYPE));
        msgInner.setTopic(TransactionalMessageUtil.buildHalfTopic());
        msgInner.setQueueId(0);
        msgInner.setPropertiesString(MessageDecoder.messageProperties2String(msgInner.getProperties()));
        return msgInner;
    }

    public boolean putOpMessage(MessageExt messageExt, String opType) {
        MessageQueue messageQueue = new MessageQueue(messageExt.getTopic(),
            this.brokerController.getBrokerConfig().getBrokerName(), messageExt.getQueueId());
        if (TransactionalMessageUtil.REMOVETAG.equals(opType)) {
            return addRemoveTagInTransactionOp(messageExt, messageQueue);
        }
        return true;
    }

    public PutMessageResult putMessageReturnResult(MessageExtBrokerInner messageInner) {
        LOGGER.debug("[BUG-TO-FIX] Thread:{} msgID:{}", Thread.currentThread().getName(), messageInner.getMsgId());
        return store.putMessage(messageInner);
    }

    public boolean putMessage(MessageExtBrokerInner messageInner) {
        PutMessageResult putMessageResult = store.putMessage(messageInner);
        if (putMessageResult != null
            && putMessageResult.getPutMessageStatus() == PutMessageStatus.PUT_OK) {
            return true;
        } else {
            LOGGER.error("Put message failed, topic: {}, queueId: {}, msgId: {}",
                messageInner.getTopic(), messageInner.getQueueId(), messageInner.getMsgId());
            return false;
        }
    }

    public MessageExtBrokerInner renewImmunityHalfMessageInner(MessageExt msgExt) {
        MessageExtBrokerInner msgInner = renewHalfMessageInner(msgExt);
        String queueOffsetFromPrepare = msgExt.getUserProperty(MessageConst.PROPERTY_TRANSACTION_PREPARED_QUEUE_OFFSET);
        if (null != queueOffsetFromPrepare) {
            MessageAccessor.putProperty(msgInner, MessageConst.PROPERTY_TRANSACTION_PREPARED_QUEUE_OFFSET,
                String.valueOf(queueOffsetFromPrepare));
        } else {
            MessageAccessor.putProperty(msgInner, MessageConst.PROPERTY_TRANSACTION_PREPARED_QUEUE_OFFSET,
                String.valueOf(msgExt.getQueueOffset()));
        }

        msgInner.setPropertiesString(MessageDecoder.messageProperties2String(msgInner.getProperties()));

        return msgInner;
    }

    public MessageExtBrokerInner renewHalfMessageInner(MessageExt msgExt) {
        MessageExtBrokerInner msgInner = new MessageExtBrokerInner();
        msgInner.setTopic(msgExt.getTopic());
        msgInner.setBody(msgExt.getBody());
        msgInner.setQueueId(msgExt.getQueueId());
        msgInner.setMsgId(msgExt.getMsgId());
        msgInner.setSysFlag(msgExt.getSysFlag());
        msgInner.setTags(msgExt.getTags());
        msgInner.setTagsCode(MessageExtBrokerInner.tagsString2tagsCode(msgInner.getTags()));
        MessageAccessor.setProperties(msgInner, msgExt.getProperties());
        msgInner.setPropertiesString(MessageDecoder.messageProperties2String(msgExt.getProperties()));
        msgInner.setBornTimestamp(msgExt.getBornTimestamp());
        msgInner.setBornHost(msgExt.getBornHost());
        msgInner.setStoreHost(msgExt.getStoreHost());
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5062/repo; grep -n "sendMessageToSpecificBroker\b" -A40 broker/src/main/java/org/apache/rocketmq/broker/out/BrokerOuterAPI.java | head -60; grep -n "TRANSACTION_PREPARED\|isTransHalf\|rejectTrans" -i broker/src/main/java/org/apache/rocketmq/broker/processor/SendMessageProcessor.java; grep -n "clearProperty" common/src/main/java/org/apache/rocketmq/common/message/MessageAccessor.java
```

tool result:

```
876:    public SendResult sendMessageToSpecificBroker(String brokerAddr, final String brokerName,
877-                                                  final MessageExt msg, String group,
878-                                                  long timeoutMillis) throws RemotingException, MQBrokerException, InterruptedException {
879-
880-        RemotingCommand request = buildSendMessageRequest(msg, group);
881-        RemotingCommand response = this.remotingClient.invokeSync(brokerAddr, request, timeoutMillis);
882-        return this.processSendResponse(brokerName, msg, response);
883-    }
884-
885-    public CompletableFuture<SendResult> sendMessageToSpecificBrokerAsync(String brokerAddr, final String brokerName,
886-                                                                          final MessageExt msg, String group,
887-                                                                          long timeoutMillis) {
888-        RemotingCommand request = buildSendMessageRequest(msg, group);
889-
890-        CompletableFuture<SendResult> cf = new CompletableFuture<>();
891-        final String msgId = msg.getMsgId();
892-        try {
893-            this.remotingClient.invokeAsync(brokerAddr, request, timeoutMillis, responseFuture -> {
894-                RemotingCommand response = responseFuture.getResponseCommand();
895-                if (null != response) {
896-                    SendResult sendResult = null;
897-                    try {
898-                        sendResult = this.processSendResponse(brokerName, msg, response);
899-                        cf.complete(sendResult);
900-                    } catch (MQBrokerException | RemotingCommandException e) {
901-                        LOGGER.error("processSendResponse in sendMessageToSpecificBrokerAsync failed, msgId=" + msgId, e);
902-                        cf.completeExceptionally(e);
903-                    }
904-                } else {
905-                    cf.complete(null);
906-                }
907-
908-            });
909-        } catch (Throwable t) {
910-            LOGGER.error("invokeAsync failed in sendMessageToSpecificBrokerAsync, msgId=" + msgId, t);
911-            cf.completeExceptionally(t);
912-        }
913-        return cf;
914-    }
915-
916-    private static RemotingCommand buildSendMessageRequest(MessageExt msg, String group) {
259:        String traFlag = oriProps.get(MessageConst.PROPERTY_TRANSACTION_PREPARED);
263:            if (this.brokerController.getBrokerConfig().isRejectTransactionMessage()) {
24:    public static void clearProperty(final Message msg, final String name) {
25:        msg.clearProperty(name);
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5062/repo; sed -n 916,945p broker/src/main/java/org/apache/rocketmq/broker/out/BrokerOuterAPI.java; sed -n 100,180p broker/src/test/java/org/apache/rocketmq/broker/transaction/queue/TransactionalMessageServiceImplTest.java
```

tool result:

```
    private static RemotingCommand buildSendMessageRequest(MessageExt msg, String group) {
        SendMessageRequestHeaderV2 requestHeaderV2 = buildSendMessageRequestHeaderV2(msg, group);
        RemotingCommand request = RemotingCommand.createRequestCommand(RequestCode.SEND_MESSAGE_V2, requestHeaderV2);

        request.setBody(msg.getBody());
        return request;
    }

    private static SendMessageRequestHeaderV2 buildSendMessageRequestHeaderV2(MessageExt msg, String group) {
        SendMessageRequestHeader requestHeader = new SendMessageRequestHeader();
        requestHeader.setProducerGroup(group);
        requestHeader.setTopic(msg.getTopic());
        requestHeader.setDefaultTopic(TopicValidator.AUTO_CREATE_TOPIC_KEY_TOPIC);
        requestHeader.setDefaultTopicQueueNums(8);
        requestHeader.setQueueId(msg.getQueueId());
        requestHeader.setSysFlag(msg.getSysFlag());
        requestHeader.setBornTimestamp(msg.getBornTimestamp());
        requestHeader.setFlag(msg.getFlag());
        requestHeader.setProperties(MessageDecoder.messageProperties2String(msg.getProperties()));
        requestHeader.setReconsumeTimes(msg.getReconsumeTimes());
        requestHeader.setBatch(false);

        SendMessageRequestHeaderV2 requestHeaderV2 = SendMessageRequestHeaderV2.createSendMessageRequestHeaderV2(requestHeader);
        return requestHeaderV2;
    }

    private SendResult processSendResponse(
            final String brokerName,
            final Message msg,
            final RemotingCommand response
    }

    @Test
    public void testRollbackMessage() {
        when(bridge.lookMessageByOffset(anyLong())).thenReturn(createMessageBrokerInner());
        OperationResult result = queueTransactionMsgService.commitMessage(createEndTransactionRequestHeader(MessageSysFlag.TRANSACTION_ROLLBACK_TYPE));
        assertThat(result.getResponseCode()).isEqualTo(ResponseCode.SUCCESS);
    }

    @Test
    public void testCheck_withDiscard() {
        when(bridge.fetchMessageQueues(TopicValidator.RMQ_SYS_TRANS_HALF_TOPIC)).thenReturn(createMessageQueueSet(TopicValidator.RMQ_SYS_TRANS_HALF_TOPIC));
        when(bridge.getHalfMessage(0, 0, 1)).thenReturn(createDiscardPullResult(TopicValidator.RMQ_SYS_TRANS_HALF_TOPIC, 5, "hellp", 1));
        when(bridge.getHalfMessage(0, 1, 1)).thenReturn(createPullResult(TopicValidator.RMQ_SYS_TRANS_HALF_TOPIC, 6, "hellp", 0));
        when(bridge.getOpMessage(anyInt(), anyLong(), anyInt())).thenReturn(createOpPulResult(TopicValidator.RMQ_SYS_TRANS_OP_HALF_TOPIC, 1, "10", 1));
        long timeOut = this.brokerController.getBrokerConfig().getTransactionTimeOut();
        int checkMax = this.brokerController.getBrokerConfig().getTransactionCheckMax();
        final AtomicInteger checkMessage = new AtomicInteger(0);
        doAnswer(new Answer() {
            @Override
            public Object answer(InvocationOnMock invocation) {
                checkMessage.addAndGet(1);
                return null;
            }
        }).when(listener).resolveDiscardMsg(any(MessageExt.class));
        queueTransactionMsgService.check(timeOut, checkMax, listener);
        assertThat(checkMessage.get()).isEqualTo(1);
    }

    @Test
    public void testCheck_withCheck() {
        when(bridge.fetchMessageQueues(TopicValidator.RMQ_SYS_TRANS_HALF_TOPIC)).thenReturn(createMessageQueueSet(TopicValidator.RMQ_SYS_TRANS_HALF_TOPIC));
        when(bridge.getHalfMessage(0, 0, 1)).thenReturn(createPullResult(TopicValidator.RMQ_SYS_TRANS_HALF_TOPIC, 5, "hello", 1));
        when(bridge.getHalfMessage(0, 1, 1)).thenReturn(createPullResult(TopicValidator.RMQ_SYS_TRANS_HALF_TOPIC, 6, "hellp", 0));
        when(bridge.getOpMessage(anyInt(), anyLong(), anyInt())).thenReturn(createPullResult(TopicValidator.RMQ_SYS_TRANS_OP_HALF_TOPIC, 1, "5", 0));
        when(bridge.getBrokerController()).thenReturn(this.brokerController);
        when(bridge.renewHalfMessageInner(any(MessageExtBrokerInner.class))).thenReturn(createMessageBrokerInner());
        when(bridge.putMessageReturnResult(any(MessageExtBrokerInner.class))).thenReturn(new PutMessageResult
            (PutMessageStatus.PUT_OK, new AppendMessageResult(AppendMessageStatus.PUT_OK)));
        long timeOut = this.brokerController.getBrokerConfig().getTransactionTimeOut();
        final int checkMax = this.brokerController.getBrokerConfig().getTransactionCheckMax();
        final AtomicInteger checkMessage = new AtomicInteger(0);
        doAnswer(new Answer() {
            @Override
            public Object answer(InvocationOnMock invocation) {
                checkMessage.addAndGet(1);
                return checkMessage;
            }
        }).when(listener).resolveHalfMsg(any(MessageExt.class));
        queueTransactionMsgService.check(timeOut, checkMax, listener);
        assertThat(checkMessage.get()).isEqualTo(1);
    }

    @Test
    public void testDeletePrepareMessage() {
        when(bridge.putOpMessage(any(MessageExt.class), anyString())).thenReturn(true);
        boolean res = queueTransactionMsgService.deletePrepareMessage(createMessageBrokerInner());
        assertThat(res).isTrue();
    }

    @Test
    public void testOpen() {
        boolean isOpen = queueTransactionMsgService.open();
        assertThat(isOpen).isTrue();
    }

    private PullResult createDiscardPullResult(String topic, long queueOffset, String body, int size) {
        PullResult result = createPullResult(topic, queueOffset, body, size);
        List<MessageExt> msgs = result.getMsgFoundList();
        for (MessageExt msg : msgs) {
            msg.putUserProperty(MessageConst.PROPERTY_TRANSACTION_CHECK_TIMES, "100000");
        }
        return result;
    }

    private PullResult createPullResult(String topic, long queueOffset, String body, int size) {
        PullResult result = null;
        if (0 == size) {
            result = new PullResult(PullStatus.NO_NEW_MSG, 1, 0, 1,
                null);
        } else {
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5062/repo; sed -n 250,285p broker/src/main/java/org/apache/rocketmq/broker/processor/SendMessageProcessor.java; sed -n 270,290p broker/src/main/java/org/apache/rocketmq/broker/transaction/queue/TransactionalMessageBridge.java; sed -n 1,60p broker/src/test/java/org/apache/rocketmq/broker/transaction/queue/TransactionalMessageServiceImplTest.java | grep -n "brokerController\|Mock\|Spy"
```

tool result:

```
        msgInner.setBornHost(ctx.channel().remoteAddress());
        msgInner.setStoreHost(this.getStoreHost());
        msgInner.setReconsumeTimes(requestHeader.getReconsumeTimes() == null ? 0 : requestHeader.getReconsumeTimes());
        String clusterName = this.brokerController.getBrokerConfig().getBrokerClusterName();
        MessageAccessor.putProperty(msgInner, MessageConst.PROPERTY_CLUSTER, clusterName);

        msgInner.setPropertiesString(MessageDecoder.messageProperties2String(msgInner.getProperties()));

        // Map<String, String> oriProps = MessageDecoder.string2messageProperties(requestHeader.getProperties());
        String traFlag = oriProps.get(MessageConst.PROPERTY_TRANSACTION_PREPARED);
        boolean sendTransactionPrepareMessage = false;
        if (Boolean.parseBoolean(traFlag)
            && !(msgInner.getReconsumeTimes() > 0 && msgInner.getDelayTimeLevel() > 0)) { //For client under version 4.6.1
            if (this.brokerController.getBrokerConfig().isRejectTransactionMessage()) {
                response.setCode(ResponseCode.NO_PERMISSION);
                response.setRemark(
                    "the broker[" + this.brokerController.getBrokerConfig().getBrokerIP1()
                        + "] sending transaction message is forbidden");
                return response;
            }
            sendTransactionPrepareMessage = true;
        }

        long beginTimeMillis = this.brokerController.getMessageStore().now();

        if (brokerController.getBrokerConfig().isAsyncSendEnable()) {
            CompletableFuture<PutMessageResult> asyncPutMessageFuture;
            if (sendTransactionPrepareMessage) {
                asyncPutMessageFuture = this.brokerController.getTransactionalMessageService().asyncPrepareMessage(msgInner);
            } else {
                asyncPutMessageFuture = this.brokerController.getMessageStore().asyncPutMessage(msgInner);
            }

            final int finalQueueIdInt = queueIdInt;
            final MessageExtBrokerInner finalMsgInner = msgInner;
            asyncPutMessageFuture.thenAcceptAsync(putMessageResult -> {
        msgInner.setStoreHost(msgExt.getStoreHost());
        msgInner.setWaitStoreMsgOK(false);
        return msgInner;
    }

    private MessageExtBrokerInner makeOpMessageInner(Message message, MessageQueue messageQueue) {
        MessageExtBrokerInner msgInner = new MessageExtBrokerInner();
        msgInner.setTopic(message.getTopic());
        msgInner.setBody(message.getBody());
        msgInner.setQueueId(messageQueue.getQueueId());
        msgInner.setTags(message.getTags());
        msgInner.setTagsCode(MessageExtBrokerInner.tagsString2tagsCode(msgInner.getTags()));
        msgInner.setSysFlag(0);
        MessageAccessor.setProperties(msgInner, message.getProperties());
        msgInner.setPropertiesString(MessageDecoder.messageProperties2String(message.getProperties()));
        msgInner.setBornTimestamp(System.currentTimeMillis());
        msgInner.setBornHost(this.storeHost);
        msgInner.setStoreHost(this.storeHost);
        msgInner.setWaitStoreMsgOK(false);
        MessageClientIDSetter.setUniqID(msgInner);
        return msgInner;
44:import org.mockito.Mock;
45:import org.mockito.Spy;
46:import org.mockito.invocation.InvocationOnMock;
47:import org.mockito.junit.MockitoJUnitRunner;
```

**assistant:** Now implementing. First, the half-message → real-message converter in `TransactionalMessageUtil`:

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5062/repo/broker/src/main/java/org/apache/rocketmq/broker/transaction/queue; python3 - <<'EOF'
p='TransactionalMessageUtil.java'
s=open(p).read()
s=s.replace("""import org.apache.rocketmq.common.MixAll;
import org.apache.rocketmq.common.topic.TopicValidator;
""","""import org.apache.commons.lang3.StringUtils;
import org.apache.rocketmq.common.MixAll;
import org.apache.rocketmq.common.message.MessageAccessor;
import org.apache.rocketmq.common.message.MessageConst;
import org.apache.rocketmq.common.message.MessageDecoder;
import org.apache.rocketmq.common.message.MessageExt;
import org.apache.rocketmq.common.message.MessageExtBrokerInner;
import org.apache.rocketmq.common.sysflag.MessageSysFlag;
import org.apache.rocketmq.common.topic.TopicValidator;
""")
s=s.replace("""        return MixAll.CID_SYS_RMQ_TRANS;
    }
""","""        return MixAll.CID_SYS_RMQ_TRANS;
    }

    /**
     * Restore a half message to the original transactional (prepared) message, so that it could be sent to
     * another broker, as sending messages to the half topic, which is a system topic, is forbidden.
     *
     * @param msgExt half message
     * @return transactional message with real topic and queue id
     */
    public static MessageExtBrokerInner buildTransactionalMessageFromHalfMessage(MessageExt msgExt) {
        final MessageExtBrokerInner msgInner = new MessageExtBrokerInner();
        msgInner.setWaitStoreMsgOK(false);
        msgInner.setMsgId(msgExt.getMsgId());
        msgInner.setTopic(msgExt.getProperty(MessageConst.PROPERTY_REAL_TOPIC));
        msgInner.setBody(msgExt.getBody());
        final String realQueueIdStr = msgExt.getProperty(MessageConst.PROPERTY_REAL_QUEUE_ID);
        if (StringUtils.isNumeric(realQueueIdStr)) {
            msgInner.setQueueId(Integer.parseInt(realQueueIdStr));
        }
        msgInner.setFlag(msgExt.getFlag());
        msgInner.setBornTimestamp(msgExt.getBornTimestamp());
        msgInner.setBornHost(msgExt.getBornHost());
        msgInner.setStoreHost(msgExt.getStoreHost());
        msgInner.setTransactionId(msgExt.getProperty(MessageConst.PROPERTY_UNIQ_CLIENT_MESSAGE_ID_KEYIDX));

        MessageAccessor.setProperties(msgInner, msgExt.getProperties());
        MessageAccessor.putProperty(msgInner, MessageConst.PROPERTY_TRANSACTION_PREPARED, "true");
        MessageAccessor.clearProperty(msgInner, MessageConst.PROPERTY_TRANSACTION_PREPARED_QUEUE_OFFSET);
        MessageAccessor.clearProperty(msgInner, MessageConst.PROPERTY_REAL_TOPIC);
        MessageAccessor.clearProperty(msgInner, MessageConst.PROPERTY_REAL_QUEUE_ID);
        msgInner.setPropertiesString(MessageDecoder.messageProperties2String(msgInner.getProperties()));
        msgInner.setTagsCode(MessageExtBrokerInner.tagsString2tagsCode(msgInner.getTags()));

        msgInner.setSysFlag(MessageSysFlag.resetTransactionValue(msgExt.getSysFlag(), MessageSysFlag.TRANSACTION_PREPARED_TYPE));

        return msgInner;
    }
""")
open(p,'w').write(s)
EOF
grep -n "setProperties\b\|static.*setProperties" /work/apache__rocketmq-5062/repo/common/src/main/java/org/apache/rocketmq/common/message/MessageAccessor.java
```

tool result:

```
28:    public static void setProperties(final Message msg, Map<String, String> properties) {
29:        msg.setProperties(properties);
95:        newMsg.setProperties(msg.getProperties());
```

**assistant:** `setProperties` shares the map reference, so clearing properties would mutate the source half message. I'll copy the map instead.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5062/repo/broker/src/main/java/org/apache/rocketmq/broker/transaction/queue; python3 - <<'EOF'
p='TransactionalMessageUtil.java'
s=open(p).read()
s=s.replace("MessageAccessor.setProperties(msgInner, msgExt.getProperties());","MessageAccessor.setProperties(msgInner, new HashMap<>(msgExt.getProperties()));")
s=s.replace("import java.nio.charset.StandardCharsets;\n","import java.nio.charset.StandardCharsets;\nimport java.util.HashMap;\n")
open(p,'w').write(s)

p='TransactionalMessageBridge.java'
s=open(p).read()
s=s.replace("""    public MessageExtBrokerInner renewImmunityHalfMessageInner(""","""    public boolean escapeMessage(MessageExtBrokerInner messageInner) {
        PutMessageResult putMessageResult = this.brokerController.getEscapeBridge().putMessage(messageInner);
        if (putMessageResult != null && putMessageResult.isOk()) {
            return true;
        } else {
            LOGGER.error("Escaping message failed, topic: {}, queueId: {}, msgId: {}",
                messageInner.getTopic(), messageInner.getQueueId(), messageInner.getMsgId());
            return false;
        }
    }

    public MessageExtBrokerInner renewImmunityHalfMessageInner(""")
open(p,'w').write(s)
EOF
grep -n "isOk" -A4 /work/apache__rocketmq-5062/repo/store/src/main/java/org/apache/rocketmq/store/PutMessageResult.java
```

tool result:

```
36:    public boolean isOk() {
37-        if (remotePut) {
38-            return putMessageStatus == PutMessageStatus.PUT_OK || putMessageStatus == PutMessageStatus.FLUSH_DISK_TIMEOUT
39-                || putMessageStatus == PutMessageStatus.FLUSH_SLAVE_TIMEOUT || putMessageStatus == PutMessageStatus.SLAVE_NOT_AVAILABLE;
40-        } else {
41:            return this.appendMessageResult != null && this.appendMessageResult.isOk();
42-        }
43-
44-    }
45-
```

**assistant:** Now the `EscapeBridge`: convert half messages back to real messages when sending to a remote master.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5062/repo/broker/src/main/java/org/apache/rocketmq/broker/failover; python3 - <<'EOF'
p='EscapeBridge.java'
s=open(p).read()
old="""    private SendResult putMessageToRemoteBroker(MessageExtBrokerInner messageExt) {
        final TopicPublishInfo"""
new="""    private SendResult putMessageToRemoteBroker(MessageExtBrokerInner messageExt) {
        if (TransactionalMessageUtil.buildHalfTopic().equals(messageExt.getTopic())) {
            // Sending messages to system topics is forbidden, so restore half message to the original one.
            messageExt = TransactionalMessageUtil.buildTransactionalMessageFromHalfMessage(messageExt);
        }
        final TopicPublishInfo"""
assert old in s
s=s.replace(old,new)
s=s.replace("import org.apache.rocketmq.broker.BrokerController;\n","import org.apache.rocketmq.broker.BrokerController;\nimport org.apache.rocketmq.broker.transaction.queue.TransactionalMessageUtil;\n")
open(p,'w').write(s)
EOF
```

tool result:

```
(Bash completed with no output)
```

**assistant:** Now the check loop in `TransactionalMessageServiceImpl`: when acting as master, escape each pending half message instead of checking it.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5062/repo/broker/src/main/java/org/apache/rocketmq/broker/transaction/queue; python3 - <<'EOF'
p='TransactionalMessageServiceImpl.java'
s=open(p).read()
old="""                        if (needDiscard(msgExt, transactionCheckMax) || needSkip(msgExt)) {"""
new="""                        if (isSlaveActingMaster()) {
                            // Keep read-only semantics of slave: escape half message to master instead of checking.
                            final MessageExtBrokerInner msgInner = this.transactionalMessageBridge.renewHalfMessageInner(msgExt);
                            if (this.transactionalMessageBridge.escapeMessage(msgInner)) {
                                escapeFailCnt = 0;
                                newOffset = i + 1;
                                i++;
                                continue;
                            }
                            log.warn("Escaping transactional message failed {} times! msgId(offsetId)={}, UNIQ_KEY(transactionId)={}",
                                escapeFailCnt + 1, msgExt.getMsgId(),
                                msgExt.getUserProperty(MessageConst.PROPERTY_UNIQ_CLIENT_MESSAGE_ID_KEYIDX));
                            if (++escapeFailCnt > MAX_RETRY_TIMES_FOR_ESCAPE) {
                                // Retry in next round of check, rather than skipping the message.
                                break;
                            }
                            Thread.sleep(100L * escapeFailCnt);
                            continue;
                        }

                        if (needDiscard(msgExt, transactionCheckMax) || needSkip(msgExt)) {"""
assert old in s
s=s.replace(old,new)
old="""                int getMessageNullCount = 1;
"""
assert old in s
s=s.replace(old, old+"                int escapeFailCnt = 0;\n")
old="""    private static final int MAX_RETRY_COUNT_WHEN_HALF_NULL = 1;
"""
s=s.replace(old, old+"\n    private static final int MAX_RETRY_TIMES_FOR_ESCAPE = 10;\n")
old="""    private boolean needDiscard("""
s=s.replace(old,"""    private boolean isSlaveActingMaster() {
        final BrokerController brokerController = this.transactionalMessageBridge.getBrokerController();
        return brokerController != null
            && brokerController.getBrokerConfig().isEnableSlaveActingMaster()
            && BrokerRole.SLAVE == brokerController.getMessageStoreConfig().getBrokerRole()
            && brokerController.getMinBrokerIdInGroup() == brokerController.getBrokerConfig().getBrokerId();
    }

"""+old,1)
s=s.replace("import org.apache.rocketmq.broker.transaction.AbstractTransactionalMessageCheckListener;\n","import org.apache.rocketmq.broker.BrokerController;\nimport org.apache.rocketmq.broker.transaction.AbstractTransactionalMessageCheckListener;\n")
s=s.replace("import org.apache.rocketmq.store.PutMessageStatus;\n","import org.apache.rocketmq.store.PutMessageStatus;\nimport org.apache.rocketmq.store.config.BrokerRole;\n")
open(p,'w').write(s)
EOF
git diff --stat
```

tool result:

```
 .../rocketmq/broker/failover/EscapeBridge.java     |  5 +++
 .../queue/TransactionalMessageBridge.java          | 11 ++++++
 .../queue/TransactionalMessageServiceImpl.java     | 33 ++++++++++++++++
 .../queue/TransactionalMessageUtil.java            | 44 ++++++++++++++++++++++
 pom.xml                                            |  2 +-
 5 files changed, 94 insertions(+), 1 deletion(-)
```

**thinking:**

```
The end-transaction denial logic is already in place—`EndTransactionProcessor` rejects with `SLAVE_NOT_AVAILABLE` for the `SLAVE` role, including acting master. I'll now write a temporary test to confirm this works as expected.


```

**tool call: Bash**

```bash
mkdir -p /work/apache__rocketmq-5062/repo/broker/src/test/java/org/apache/rocketmq/broker/tmprepro && cat > /work/apache__rocketmq-5062/repo/broker/src/test/java/org/apache/rocketmq/broker/tmprepro/EscapeReproTest.java <<'EOF'
package org.apache.rocketmq.broker.tmprepro;

import java.net.InetSocketAddress;
import java.util.Collections;
import org.apache.rocketmq.broker.BrokerController;
import org.apache.rocketmq.broker.transaction.AbstractTransactionalMessageCheckListener;
import org.apache.rocketmq.broker.transaction.queue.TransactionalMessageBridge;
import org.apache.rocketmq.broker.transaction.queue.TransactionalMessageServiceImpl;
import org.apache.rocketmq.broker.transaction.queue.TransactionalMessageUtil;
import org.apache.rocketmq.client.consumer.PullResult;
import org.apache.rocketmq.client.consumer.PullStatus;
import org.apache.rocketmq.common.BrokerConfig;
import org.apache.rocketmq.common.message.*;
import org.apache.rocketmq.common.sysflag.MessageSysFlag;
import org.apache.rocketmq.common.topic.TopicValidator;
import org.apache.rocketmq.store.config.BrokerRole;
import org.apache.rocketmq.store.config.MessageStoreConfig;
import org.junit.Test;

import static org.junit.Assert.*;
import static org.mockito.ArgumentMatchers.*;
import static org.mockito.Mockito.*;

public class EscapeReproTest {
    @Test
    public void testBuild() {
        MessageExt half = new MessageExt();
        half.setTopic(TransactionalMessageUtil.buildHalfTopic());
        MessageAccessor.putProperty(half, MessageConst.PROPERTY_REAL_TOPIC, "real-topic");
        MessageAccessor.putProperty(half, MessageConst.PROPERTY_REAL_QUEUE_ID, "3");
        half.setMsgId("msgId");
        MessageAccessor.putProperty(half, MessageConst.PROPERTY_UNIQ_CLIENT_MESSAGE_ID_KEYIDX, "tranId");
        MessageAccessor.putProperty(half, MessageConst.PROPERTY_PRODUCER_GROUP, "grp");
        MessageExtBrokerInner inner = TransactionalMessageUtil.buildTransactionalMessageFromHalfMessage(half);
        assertEquals("real-topic", inner.getTopic());
        assertEquals(3, inner.getQueueId());
        assertEquals("true", inner.getProperty(MessageConst.PROPERTY_TRANSACTION_PREPARED));
        assertEquals("tranId", inner.getTransactionId());
        assertEquals("grp", inner.getProperty(MessageConst.PROPERTY_PRODUCER_GROUP));
        assertTrue(MessageSysFlag.check(inner.getSysFlag(), MessageSysFlag.TRANSACTION_PREPARED_TYPE));
        assertNull(inner.getProperty(MessageConst.PROPERTY_REAL_TOPIC));
        assertEquals("real-topic", half.getProperty(MessageConst.PROPERTY_REAL_TOPIC));
    }

    @Test
    public void testCheckEscapes() {
        BrokerController bc = mock(BrokerController.class);
        BrokerConfig cfg = new BrokerConfig();
        cfg.setEnableSlaveActingMaster(true);
        cfg.setBrokerId(1);
        MessageStoreConfig msc = new MessageStoreConfig();
        msc.setBrokerRole(BrokerRole.SLAVE);
        when(bc.getBrokerConfig()).thenReturn(cfg);
        when(bc.getMessageStoreConfig()).thenReturn(msc);
        when(bc.getMinBrokerIdInGroup()).thenReturn(1L);
        TransactionalMessageBridge bridge = mock(TransactionalMessageBridge.class);
        when(bridge.getBrokerController()).thenReturn(bc);
        MessageQueue mq = new MessageQueue(TopicValidator.RMQ_SYS_TRANS_HALF_TOPIC, "b", 0);
        when(bridge.fetchMessageQueues(anyString())).thenReturn(Collections.singleton(mq));
        when(bridge.fetchConsumeOffset(any())).thenReturn(0L);
        when(bridge.getOpMessage(anyInt(), anyLong(), anyInt())).thenReturn(new PullResult(PullStatus.NO_NEW_MSG, 0, 0, 0, null));
        MessageExt m = new MessageExt();
        m.setTopic(TopicValidator.RMQ_SYS_TRANS_HALF_TOPIC);
        m.setBornHost(new InetSocketAddress(1));
        m.setStoreHost(new InetSocketAddress(1));
        when(bridge.getHalfMessage(0, 0, 1)).thenReturn(new PullResult(PullStatus.FOUND, 1, 0, 1, Collections.singletonList(m)));
        when(bridge.getHalfMessage(0, 1, 1)).thenReturn(new PullResult(PullStatus.NO_NEW_MSG, 1, 0, 1, null));
        when(bridge.renewHalfMessageInner(any())).thenReturn(new MessageExtBrokerInner());
        when(bridge.escapeMessage(any())).thenReturn(true);
        AbstractTransactionalMessageCheckListener l = mock(AbstractTransactionalMessageCheckListener.class);
        new TransactionalMessageServiceImpl(bridge).check(1, 15, l);
        verify(bridge, times(1)).escapeMessage(any());
        verify(l, never()).resolveHalfMsg(any());
        verify(l, never()).resolveDiscardMsg(any());
        verify(bridge).updateConsumeOffset(mq, 1L);
    }
}
EOF
/work/apache__rocketmq-5062/bin/envrun 'mvn -o -q install -DskipTests -Dcheckstyle.skip -Drat.skip -Dspotbugs.skip -pl broker -am 2>&1 | tail -20; cd broker && mvn -o test -Dcheckstyle.skip -Drat.skip -Dtest="EscapeReproTest,TransactionalMessage*Test,EscapeBridgeTest,EndTransactionProcessorTest,DefaultTransactionalMessageCheckListenerTest" -DfailIfNoTests=false 2>&1 | grep -E "Tests run|FAIL|ERROR" | head -30'
```

tool result:

```
[INFO] BUILD FAILURE
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:2.19.1:test (default-test) on project rocketmq-broker: Unable to generate classpath: org.apache.maven.artifact.resolver.MultipleArtifactsNotFoundException: Missing:
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

**assistant:** The build compiled, but surefire's JUnit4 provider isn't cached offline. Checking which providers are available:

**tool call: Bash**

```bash
/work/apache__rocketmq-5062/bin/envrun 'git diff pom.xml; ls ~/.m2/repository/org/apache/maven/surefire/; ls ~/.m2/repository/org/apache/maven/surefire/surefire-junit4* 2>/dev/null'
```

tool result:

```
Exit code 2
diff --git a/pom.xml b/pom.xml
index c82e89b7f..5861b9ba4 100644
--- a/pom.xml
+++ b/pom.xml
@@ -378,7 +378,7 @@
                     <forkCount>1</forkCount>
                     <reuseForks>true</reuseForks>
                     <excludes>
-                        <exclude>**/IT*.java</exclude>
+<exclude>**/IT*.java</exclude><exclude>%regex[.*MixCommitlogTest.*]</exclude>
                     </excludes>
                 </configuration>
             </plugin>
maven-surefire-common
surefire
surefire-api
surefire-booter
```

**tool call: Bash**

```bash
/work/apache__rocketmq-5062/bin/envrun 'find / -name "surefire-junit*" -not -path "/proc/*" 2>/dev/null | head; find / -name "settings.xml" -path "*m2*" 2>/dev/null | head; cat Dockerfile | tail -20'
```

tool result:

```
FROM polybench_java_base 

WORKDIR /testbed
COPY . .
RUN export JAVA_HOME=/usr/lib/jvm/java-1.8.0-amazon-corretto.x86_64/ && sed -i 's/^.*\*\*\/IT\*\.java.*$/<exclude>**\/IT*.java<\/exclude><exclude>%regex[.*MixCommitlogTest.*]<\/exclude>/' pom.xml && update-alternatives --set java /usr/lib/jvm/java-1.8.0-amazon-corretto.x86_64/jre/bin/java && mvn clean install -am -Dtest=TransactionalMessageServiceImplTest,TransactionListenerImpl,TransactionMessageIT,TransactionalMessageUtilTest,ContainerIntegrationTestBase -DfailIfNoTests=false -fae -DskipTests

ENV JAVA_HOME=/usr/lib/jvm/java-1.8.0-amazon-corretto.x86_64/
RUN update-alternatives --set java /usr/lib/jvm/java-1.8.0-amazon-corretto.x86_64/jre/bin/java
```

**assistant:** Surefire's JUnit provider was never downloaded (the image was built with `-DskipTests`), so I'll compile the tests with Maven and run JUnit directly on the test classpath.

**tool call: Bash**

```bash
/work/apache__rocketmq-5062/bin/envrun 'cd broker && mvn -o -q test-compile -Dcheckstyle.skip -Drat.skip 2>&1 | tail -5; mvn -o -q dependency:build-classpath -Dmdep.outputFile=/tmp/cp.txt 2>&1 | tail -3; ls -la /tmp/cp.txt'
```

tool result:

```
Exit code 2
     [java] JVM args ignored when same JVM is used.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/NoPluginFoundForPrefixException
ls: cannot access '/tmp/cp.txt': No such file or directory
```

**assistant:** No dependency plugin either; I'll pull the test classpath from Maven's debug output.

**tool call: Bash**

```bash
/work/apache__rocketmq-5062/bin/envrun 'cd broker && mvn -o -X test-compile -Dcheckstyle.skip -Drat.skip 2>&1 | grep -A1 "\[DEBUG\] -d /testbed/broker/target/test-classes -classpath" | tail -1 > /tmp/raw.txt; wc -c /tmp/raw.txt; CP=$(sed -E "s/^.*-classpath ([^ ]+) .*$/\1/" /tmp/raw.txt); [ -z "$CP" ] && head -c 600 /tmp/raw.txt; echo "$CP" > /tmp/cp.txt; tr ":" "\n" < /tmp/cp.txt | grep -c jar'
```

tool result:

```
Exit code 1
0 /tmp/raw.txt
0
```

**tool call: Bash**

```bash
/work/apache__rocketmq-5062/bin/envrun 'cd broker && mvn -o -X test-compile -Dcheckstyle.skip -Drat.skip 2>&1 | grep -n "classpath\|Classpath" | cut -c1-200 | tail -8'
```

tool result:

```
2474:[DEBUG]   Adding to AuxClasspath ->/root/.m2/repository/org/slf4j/slf4j-api/1.7.7/slf4j-api-1.7.7.jar
2475:[DEBUG]   Adding to AuxClasspath ->/root/.m2/repository/com/googlecode/concurrentlinkedhashmap/concurrentlinkedhashmap-lru/1.4.2/concurrentlinkedhashmap-lru-1.4.2.jar
2476:[DEBUG]   Adding to AuxClasspath ->/root/.m2/repository/org/awaitility/awaitility/4.1.0/awaitility-4.1.0.jar
2477:[DEBUG]   Adding to AuxClasspath ->/root/.m2/repository/org/hamcrest/hamcrest/2.1/hamcrest-2.1.jar
2478:[DEBUG]   AuxClasspath is ->:/root/.m2/repository/org/apache/rocketmq/rocketmq-common/5.0.1-SNAPSHOT/rocketmq-common-5.0.1-SNAPSHOT.jar:/root/.m2/repository/org/apache/commons/commons-lang3/3.12.
2573:[DEBUG] Spotbugs arg is -auxclasspathFromInput
123981:[DEBUG]   (f) classpathElements = [/testbed/broker/target/test-classes, /testbed/broker/target/classes, /root/.m2/repository/org/apache/rocketmq/rocketmq-common/5.0.1-SNAPSHOT/rocketmq-common-5
124008:[DEBUG] Classpath: [/testbed/broker/target/test-classes
```

**tool call: Bash**

```bash
/work/apache__rocketmq-5062/bin/envrun 'cd broker && mvn -o -X test-compile -Dcheckstyle.skip -Drat.skip -Dspotbugs.skip 2>&1 | grep "(f) classpathElements = \[/testbed/broker/target/test-classes" | head -1 | sed -E "s/.*= \[(.*)\]$/\1/; s/, /:/g" > /tmp/cp.txt; java -cp $(cat /tmp/cp.txt) org.junit.runner.JUnitCore org.apache.rocketmq.broker.tmprepro.EscapeReproTest org.apache.rocketmq.broker.transaction.queue.TransactionalMessageServiceImplTest org.apache.rocketmq.broker.transaction.queue.TransactionalMessageBridgeTest org.apache.rocketmq.broker.transaction.queue.DefaultTransactionalMessageCheckListenerTest org.apache.rocketmq.broker.failover.EscapeBridgeTest org.apache.rocketmq.broker.processor.EndTransactionProcessorTest 2>&1 | grep -v "^\s*at \|^\[\|DEBUG\|INFO" | tail -30'
```

tool result:

```
JUnit version 4.13.2
......................................
Time: 2.68

OK (38 tests)
```

**thinking:**

```
All 38 tests pass, including my repro, which couldn't even compile before the fix since those methods didn't exist yet. Running checkstyle next, then cleaning up.


```

**tool call: Bash**

```bash
rm -rf /work/apache__rocketmq-5062/repo/broker/src/test/java/org/apache/rocketmq/broker/tmprepro; /work/apache__rocketmq-5062/bin/envrun 'cd broker && mvn -o -q checkstyle:check 2>&1 | tail -10; rm -f /tmp/cp.txt /tmp/raw.txt; rm -rf target/test-classes/org/apache/rocketmq/broker/tmprepro; cd .. && git status --short'
```

tool result:

```
[ERROR] src/main/java/org/apache/rocketmq/broker/BrokerStartup.java:[304,36] (coding) HiddenField: 'file' hides a field.
[ERROR] src/main/java/org/apache/rocketmq/broker/BrokerStartup.java:[308,9] (design) DesignForExtension: Class 'SystemConfigFileHelper' looks like designed for extension (can be subclassed), but the method 'getFile' does not have javadoc that explains how to do that safely. If class is not designed for extension consider making the class 'SystemConfigFileHelper' final or making the method 'getFile' static/final/abstract/empty, or adding allowed annotation for the method.
[ERROR] src/main/java/org/apache/rocketmq/broker/BrokerStartup.java:[308,9] (javadoc) MissingJavadocMethod: Missing a Javadoc comment.
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-checkstyle-plugin:3.2.0:check (default-cli) on project rocketmq-broker: You have 8014 Checkstyle violations. -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoFailureException
 M broker/src/main/java/org/apache/rocketmq/broker/failover/EscapeBridge.java
 M broker/src/main/java/org/apache/rocketmq/broker/transaction/queue/TransactionalMessageBridge.java
 M broker/src/main/java/org/apache/rocketmq/broker/transaction/queue/TransactionalMessageServiceImpl.java
 M broker/src/main/java/org/apache/rocketmq/broker/transaction/queue/TransactionalMessageUtil.java
 M pom.xml
?? Dockerfile
```

**thinking:**

```
The checkstyle run used the plugin's default Sun ruleset rather than the project's actual config, so its 8014 violations aren't relevant to this change—I left the pre-existing `pom.xml` and `Dockerfile` changes untouched. Here's the final diff.


```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-5062/repo && git diff broker/src/main/java/org/apache/rocketmq/broker/transaction/queue/TransactionalMessageServiceImpl.java
```

tool result:

```
diff --git a/broker/src/main/java/org/apache/rocketmq/broker/transaction/queue/TransactionalMessageServiceImpl.java b/broker/src/main/java/org/apache/rocketmq/broker/transaction/queue/TransactionalMessageServiceImpl.java
index 63b188e64..9af92f5ea 100644
--- a/broker/src/main/java/org/apache/rocketmq/broker/transaction/queue/TransactionalMessageServiceImpl.java
+++ b/broker/src/main/java/org/apache/rocketmq/broker/transaction/queue/TransactionalMessageServiceImpl.java
@@ -16,6 +16,7 @@
  */
 package org.apache.rocketmq.broker.transaction.queue;
 
+import org.apache.rocketmq.broker.BrokerController;
 import org.apache.rocketmq.broker.transaction.AbstractTransactionalMessageCheckListener;
 import org.apache.rocketmq.broker.transaction.OperationResult;
 import org.apache.rocketmq.broker.transaction.TransactionalMessageService;
@@ -33,6 +34,7 @@ import org.apache.rocketmq.logging.InternalLoggerFactory;
 import org.apache.rocketmq.common.message.MessageExtBrokerInner;
 import org.apache.rocketmq.store.PutMessageResult;
 import org.apache.rocketmq.store.PutMessageStatus;
+import org.apache.rocketmq.store.config.BrokerRole;
 
 import java.util.ArrayList;
 import java.util.Collections;
@@ -54,6 +56,8 @@ public class TransactionalMessageServiceImpl implements TransactionalMessageServ
 
     private static final int MAX_RETRY_COUNT_WHEN_HALF_NULL = 1;
 
+    private static final int MAX_RETRY_TIMES_FOR_ESCAPE = 10;
+
     public TransactionalMessageServiceImpl(TransactionalMessageBridge transactionBridge) {
         this.transactionalMessageBridge = transactionBridge;
     }
@@ -70,6 +74,14 @@ public class TransactionalMessageServiceImpl implements TransactionalMessageServ
         return transactionalMessageBridge.putHalfMessage(messageInner);
     }
 
+    private boolean isSlaveActingMaster() {
+        final BrokerController brokerController = this.transactionalMessageBridge.getBrokerController();
+        return brokerController != null
+            && brokerController.getBrokerConfig().isEnableSlaveActingMaster()
+            && BrokerRole.SLAVE == brokerController.getMessageStoreConfig().getBrokerRole()
+            && brokerController.getMinBrokerIdInGroup() == brokerController.getBrokerConfig().getBrokerId();
+    }
+
     private boolean needDiscard(MessageExt msgExt, int transactionCheckMax) {
         String checkTimes = msgExt.getProperty(MessageConst.PROPERTY_TRANSACTION_CHECK_TIMES);
         int checkTime = 1;
@@ -156,6 +168,7 @@ public class TransactionalMessageServiceImpl implements TransactionalMessageServ
                 }
                 // single thread
                 int getMessageNullCount = 1;
+                int escapeFailCnt = 0;
                 long newOffset = halfOffset;
                 long i = halfOffset;
                 while (true) {
@@ -187,6 +200,26 @@ public class TransactionalMessageServiceImpl implements TransactionalMessageServ
                             }
                         }
 
+                        if (isSlaveActingMaster()) {
+                            // Keep read-only semantics of slave: escape half message to master instead of checking.
+                            final MessageExtBrokerInner msgInner = this.transactionalMessageBridge.renewHalfMessageInner(msgExt);
+                            if (this.transactionalMessageBridge.escapeMessage(msgInner)) {
+                                escapeFailCnt = 0;
+                                newOffset = i + 1;
+                                i++;
+                                continue;
+                            }
+                            log.warn("Escaping transactional message failed {} times! msgId(offsetId)={}, UNIQ_KEY(transactionId)={}",
+                                escapeFailCnt + 1, msgExt.getMsgId(),
+                                msgExt.getUserProperty(MessageConst.PROPERTY_UNIQ_CLIENT_MESSAGE_ID_KEYIDX));
+                            if (++escapeFailCnt > MAX_RETRY_TIMES_FOR_ESCAPE) {
+                                // Retry in next round of check, rather than skipping the message.
+                                break;
+                            }
+                            Thread.sleep(100L * escapeFailCnt);
+                            continue;
+                        }
+
                         if (needDiscard(msgExt, transactionCheckMax) || needSkip(msgExt)) {
                             listener.resolveDiscardMsg(msgExt);
                             newOffset = i + 1;
```

**assistant:** A slave acting as master no longer checks half messages itself. It now hands each pending half message to an available master, and the targeted tests pass.

**What changed (4 files in `broker/`)**

1. **End-transaction denial** needed no change. `EndTransactionProcessor` already rejects commit and rollback with `SLAVE_NOT_AVAILABLE` whenever the role is `SLAVE`, and an acting master still has that role.

2. **Escaping during the check** (`TransactionalMessageServiceImpl.check`): a new `isSlaveActingMaster()` test is true when slave-acting-master is enabled, the role is `SLAVE`, and this broker has the lowest broker ID in its group. In that case each pending half message is rebuilt with `renewHalfMessageInner` and escaped, with no call to the producer. This happens before the discard step, so the slave never writes discard, op or re-queued half messages; the master does all the real checking.
   - If escaping fails, it retries up to 10 times with a short, growing pause, then stops and leaves the offset where it was. The next check round tries that message again, so nothing is skipped or lost.

3. **`TransactionalMessageBridge.escapeMessage`**: sends the message through `EscapeBridge.putMessage`. A master in the same process gets the half message added straight to its half topic.

4. **Remote masters** (`EscapeBridge.putMessageToRemoteBroker`): because sending to the system half topic is forbidden, a half message is first turned back into the original transactional message by the new `TransactionalMessageUtil.buildTransactionalMessageFromHalfMessage`. That method:
   - restores the real topic and queue ID;
   - sets the `TRAN_MSG=true` property and the prepared sys-flag, so the remote broker stores it as a new half message;
   - keeps the producer group and transaction ID, and drops the half-queue-only properties;
   - copies the property map, so the source message isn't changed.

**Testing**
- The image never downloaded surefire's JUnit provider, so `mvn test` can't run offline. I compiled with Maven and ran JUnit directly on the test classpath.
- A temporary test checked the message conversion and the acting-master check: the message is escaped, the producer is never called, nothing is discarded, and the offset moves forward. It passed.
- These existing tests also pass, 38 tests in total with the temporary one: `TransactionalMessageServiceImplTest`, `TransactionalMessageBridgeTest`, `DefaultTransactionalMessageCheckListenerTest`, `EscapeBridgeTest` and `EndTransactionProcessorTest`.
- I deleted the temporary test afterwards.
- I couldn't run the project's own checkstyle rules: calling the plugin directly used its default ruleset, which reports about 8,000 existing violations across the repo.

I left the `pom.xml` edit and the `Dockerfile` alone; they were already there before I started.

_session end: success, turns 25, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 56.23 s: mvn -o -q install -DskipTests -Dcheckstyle.skip -Drat.skip -Dspotbugs.skip -pl broker -am 2>&1 | tail -20; cd broker && mvn -o test -Dcheckstyle.skip -Drat.skip -Dtest="EscapeReproTest,TransactionalMessage*Test,EscapeBridgeTest,EndTransactionProcessorTest,DefaultTransactionalMessageCheckListenerTest" -DfailIfNoTests=false 2>&1 | grep -E "Tests run|FAIL|ERROR" | head -30
- `rc=2` 0.36 s: git diff pom.xml; ls ~/.m2/repository/org/apache/maven/surefire/; ls ~/.m2/repository/org/apache/maven/surefire/surefire-junit4* 2>/dev/null
- `rc=0` 0.77 s: find / -name "surefire-junit*" -not -path "/proc/*" 2>/dev/null | head; find / -name "settings.xml" -path "*m2*" 2>/dev/null | head; cat Dockerfile | tail -20
- `rc=2` 30.55 s: cd broker && mvn -o -q test-compile -Dcheckstyle.skip -Drat.skip 2>&1 | tail -5; mvn -o -q dependency:build-classpath -Dmdep.outputFile=/tmp/cp.txt 2>&1 | tail -3; ls -la /tmp/cp.txt
- `rc=1` 28.28 s: cd broker && mvn -o -X test-compile -Dcheckstyle.skip -Drat.skip 2>&1 | grep -A1 "\[DEBUG\] -d /testbed/broker/target/test-classes -classpath" | tail -1 > /tmp/raw.txt; wc -c /tmp/raw.txt; CP=$(sed -E "s/^.*-classpath ([^ ]+) .*$/\1/" /tmp/raw.txt); [ -z "$CP" ] && head -c 600 /tmp/raw.txt; echo "$CP" > /tmp/cp.txt; tr ":" "\n" < /tmp/cp.txt | grep -c jar
- `rc=0` 28.1 s: cd broker && mvn -o -X test-compile -Dcheckstyle.skip -Drat.skip 2>&1 | grep -n "classpath\|Classpath" | cut -c1-200 | tail -8
- `rc=0` 11.54 s: cd broker && mvn -o -X test-compile -Dcheckstyle.skip -Drat.skip -Dspotbugs.skip 2>&1 | grep "(f) classpathElements = \[/testbed/broker/target/test-classes" | head -1 | sed -E "s/.*= \[(.*)\]$/\1/; s/, /:/g" > /tmp/cp.txt; java -cp $(cat /tmp/cp.txt) org.junit.runner.JUnitCore org.apache.rocketmq.broker.tmprepro.EscapeReproTest org.apache.rocketmq.broker.transaction.queue.TransactionalMessageServiceImplTest org.apache.rocketmq.broker.transaction.queue.TransactionalMessageBridgeTest org.apache.rocketmq.broker.transaction.queue.DefaultTransactionalMessageCheckListenerTest org.apache.rocketmq.bro
- `rc=0` 10.61 s: cd broker && mvn -o -q checkstyle:check 2>&1 | tail -10; rm -f /tmp/cp.txt /tmp/raw.txt; rm -rf target/test-classes/org/apache/rocketmq/broker/tmprepro; cd .. && git status --short
