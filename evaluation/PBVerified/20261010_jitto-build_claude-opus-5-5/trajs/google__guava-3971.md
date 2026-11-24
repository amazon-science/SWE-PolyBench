# Instance: google__guava-3971

- Final resolved (evaluator, logs/google__guava-3971_result.json): True
- Run state: DONE
- One attempt. Duration 158.4 s, turns 12, actor cost $0.4454904, container commands 3
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/google__guava-3971/repo
</uploaded_files>
I've uploaded a Java code repository in the directory /work/google__guava-3971/repo. Consider the following issue description:

<issue_description>
Add awaitTerminationUninterruptibly(..) for ExecutorService
_[Original issue](https://code.google.com/p/guava-libraries/issues/detail?id=1315) created by **chriss.dev** on 2013-03-02 at 12:05 PM_

---

The interface ExecutorService provides the method awaitTermination(long,TimeUnit), it would be nice to have "uninterruptibly" pendats in the Uninterruptibles-class like:

boolean awaitTerminationUninterruptibly(ExecutorService executor,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;long timeout,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TimeUnit unit)

//await the termination till the end of all days
void awaitTerminationUninterruptibly(ExecutorService executor)


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/google__guava-3971/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/google__guava-3971/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/google__guava-3971/bin/envrun 'git status --short && ls'
Edits you make under /work/google__guava-3971/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/google__guava-3971/repo; find . -name Uninterruptibles*.java; grep -n "awaitUninterruptibly\|^import\|Duration\|@Beta\|@GwtIncompatible\|joinUninterruptibly" guava/src/com/google/common/util/concurrent/Uninterruptibles.java; grep -rn "awaitTermination" guava-tests/test/com/google/common/util/concurrent/UninterruptiblesTest.java android/guava-tests/test/com/google/common/util/concurrent/UninterruptiblesTest.java | head
```

tool result:

```
(eval):1: no matches found: Uninterruptibles*.java
17:import static com.google.common.util.concurrent.Internal.toNanosSaturated;
18:import static java.util.concurrent.TimeUnit.NANOSECONDS;
20:import com.google.common.annotations.Beta;
21:import com.google.common.annotations.GwtCompatible;
22:import com.google.common.annotations.GwtIncompatible;
23:import com.google.common.base.Preconditions;
24:import com.google.errorprone.annotations.CanIgnoreReturnValue;
25:import java.time.Duration;
26:import java.util.concurrent.BlockingQueue;
27:import java.util.concurrent.CancellationException;
28:import java.util.concurrent.CountDownLatch;
29:import java.util.concurrent.ExecutionException;
30:import java.util.concurrent.Future;
31:import java.util.concurrent.Semaphore;
32:import java.util.concurrent.TimeUnit;
33:import java.util.concurrent.TimeoutException;
34:import java.util.concurrent.locks.Condition;
35:import java.util.concurrent.locks.Lock;
52:  @GwtIncompatible // concurrency
53:  public static void awaitUninterruptibly(CountDownLatch latch) {
78:  @GwtIncompatible // concurrency
79:  @Beta
80:  public static boolean awaitUninterruptibly(CountDownLatch latch, Duration timeout) {
81:    return awaitUninterruptibly(latch, toNanosSaturated(timeout), TimeUnit.NANOSECONDS);
89:  @GwtIncompatible // concurrency
90:  @SuppressWarnings("GoodTime") // should accept a java.time.Duration
91:  public static boolean awaitUninterruptibly(CountDownLatch latch, long timeout, TimeUnit unit) {
119:  @GwtIncompatible // concurrency
120:  @Beta
121:  public static boolean awaitUninterruptibly(Condition condition, Duration timeout) {
122:    return awaitUninterruptibly(condition, toNanosSaturated(timeout), TimeUnit.NANOSECONDS);
131:  @GwtIncompatible // concurrency
132:  @SuppressWarnings("GoodTime") // should accept a java.time.Duration
133:  public static boolean awaitUninterruptibly(Condition condition, long timeout, TimeUnit unit) {
155:  @GwtIncompatible // concurrency
156:  public static void joinUninterruptibly(Thread toJoin) {
180:  @GwtIncompatible // concurrency
181:  @Beta
182:  public static void joinUninterruptibly(Thread toJoin, Duration timeout) {
183:    joinUninterruptibly(toJoin, toNanosSaturated(timeout), TimeUnit.NANOSECONDS);
190:  @GwtIncompatible // concurrency
191:  @SuppressWarnings("GoodTime") // should accept a java.time.Duration
192:  public static void joinUninterruptibly(Thread toJoin, long timeout, TimeUnit unit) {
270:  @GwtIncompatible // java.time.Duration
271:  @Beta
272:  public static <V> V getUninterruptibly(Future<V> future, Duration timeout)
296:  @GwtIncompatible // TODO
297:  @SuppressWarnings("GoodTime") // should accept a java.time.Duration
322:  @GwtIncompatible // concurrency
348:  @GwtIncompatible // concurrency
373:  @GwtIncompatible // concurrency
374:  @Beta
375:  public static void sleepUninterruptibly(Duration sleepFor) {
381:  @GwtIncompatible // concurrency
382:  @SuppressWarnings("GoodTime") // should accept a java.time.Duration
411:  @GwtIncompatible // concurrency
412:  @Beta
413:  public static boolean tryAcquireUninterruptibly(Semaphore semaphore, Duration timeout) {
423:  @GwtIncompatible // concurrency
424:  @SuppressWarnings("GoodTime") // should accept a java.time.Duration
436:  @GwtIncompatible // concurrency
437:  @Beta
439:      Semaphore semaphore, int permits, Duration timeout) {
450:  @GwtIncompatible // concurrency
451:  @SuppressWarnings("GoodTime") // should accept a java.time.Duration
481:  @GwtIncompatible // concurrency
482:  @Beta
483:  public static boolean tryLockUninterruptibly(Lock lock, Duration timeout) {
493:  @GwtIncompatible // concurrency
494:  @SuppressWarnings("GoodTime") // should accept a java.time.Duration
```

**tool call: Bash**

```bash
cd /work/google__guava-3971/repo; sed -n 1,140p guava/src/com/google/common/util/concurrent/Uninterruptibles.java; diff guava/src/com/google/common/util/concurrent/Uninterruptibles.java android/guava/src/com/google/common/util/concurrent/Uninterruptibles.java
```

tool result:

```
/*
 * Copyright (C) 2011 The Guava Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */

package com.google.common.util.concurrent;

import static com.google.common.util.concurrent.Internal.toNanosSaturated;
import static java.util.concurrent.TimeUnit.NANOSECONDS;

import com.google.common.annotations.Beta;
import com.google.common.annotations.GwtCompatible;
import com.google.common.annotations.GwtIncompatible;
import com.google.common.base.Preconditions;
import com.google.errorprone.annotations.CanIgnoreReturnValue;
import java.time.Duration;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.CancellationException;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;
import java.util.concurrent.Semaphore;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;

/**
 * Utilities for treating interruptible operations as uninterruptible. In all cases, if a thread is
 * interrupted during such a call, the call continues to block until the result is available or the
 * timeout elapses, and only then re-interrupts the thread.
 *
 * @author Anthony Zana
 * @since 10.0
 */
@GwtCompatible(emulated = true)
public final class Uninterruptibles {

  // Implementation Note: As of 3-7-11, the logic for each blocking/timeout
  // methods is identical, save for method being invoked.

  /** Invokes {@code latch.}{@link CountDownLatch#await() await()} uninterruptibly. */
  @GwtIncompatible // concurrency
  public static void awaitUninterruptibly(CountDownLatch latch) {
    boolean interrupted = false;
    try {
      while (true) {
        try {
          latch.await();
          return;
        } catch (InterruptedException e) {
          interrupted = true;
        }
      }
    } finally {
      if (interrupted) {
        Thread.currentThread().interrupt();
      }
    }
  }

  /**
   * Invokes {@code latch.}{@link CountDownLatch#await(long, TimeUnit) await(timeout, unit)}
   * uninterruptibly.
   *
   * @since 28.0
   */
  @CanIgnoreReturnValue // TODO(cpovirk): Consider being more strict.
  @GwtIncompatible // concurrency
  @Beta
  public static boolean awaitUninterruptibly(CountDownLatch latch, Duration timeout) {
    return awaitUninterruptibly(latch, toNanosSaturated(timeout), TimeUnit.NANOSECONDS);
  }

  /**
   * Invokes {@code latch.}{@link CountDownLatch#await(long, TimeUnit) await(timeout, unit)}
   * uninterruptibly.
   */
  @CanIgnoreReturnValue // TODO(cpovirk): Consider being more strict.
  @GwtIncompatible // concurrency
  @SuppressWarnings("GoodTime") // should accept a java.time.Duration
  public static boolean awaitUninterruptibly(CountDownLatch latch, long timeout, TimeUnit unit) {
    boolean interrupted = false;
    try {
      long remainingNanos = unit.toNanos(timeout);
      long end = System.nanoTime() + remainingNanos;

      while (true) {
        try {
          // CountDownLatch treats negative timeouts just like zero.
          return latch.await(remainingNanos, NANOSECONDS);
        } catch (InterruptedException e) {
          interrupted = true;
          remainingNanos = end - System.nanoTime();
        }
      }
    } finally {
      if (interrupted) {
        Thread.currentThread().interrupt();
      }
    }
  }

  /**
   * Invokes {@code condition.}{@link Condition#await(long, TimeUnit) await(timeout, unit)}
   * uninterruptibly.
   *
   * @since 28.0
   */
  @GwtIncompatible // concurrency
  @Beta
  public static boolean awaitUninterruptibly(Condition condition, Duration timeout) {
    return awaitUninterruptibly(condition, toNanosSaturated(timeout), TimeUnit.NANOSECONDS);
  }

  /**
   * Invokes {@code condition.}{@link Condition#await(long, TimeUnit) await(timeout, unit)}
   * uninterruptibly.
   *
   * @since 23.6
   */
  @GwtIncompatible // concurrency
  @SuppressWarnings("GoodTime") // should accept a java.time.Duration
  public static boolean awaitUninterruptibly(Condition condition, long timeout, TimeUnit unit) {
    boolean interrupted = false;
    try {
      long remainingNanos = unit.toNanos(timeout);
      long end = System.nanoTime() + remainingNanos;

      while (true) {
        try {
17d16
< import static com.google.common.util.concurrent.Internal.toNanosSaturated;
20d18
< import com.google.common.annotations.Beta;
25d22
< import java.time.Duration;
74,75d70
<    *
<    * @since 28.0
79,89d73
<   @Beta
<   public static boolean awaitUninterruptibly(CountDownLatch latch, Duration timeout) {
<     return awaitUninterruptibly(latch, toNanosSaturated(timeout), TimeUnit.NANOSECONDS);
<   }
< 
<   /**
<    * Invokes {@code latch.}{@link CountDownLatch#await(long, TimeUnit) await(timeout, unit)}
<    * uninterruptibly.
<    */
<   @CanIgnoreReturnValue // TODO(cpovirk): Consider being more strict.
<   @GwtIncompatible // concurrency
117,128d100
<    * @since 28.0
<    */
<   @GwtIncompatible // concurrency
<   @Beta
<   public static boolean awaitUninterruptibly(Condition condition, Duration timeout) {
<     return awaitUninterruptibly(condition, toNanosSaturated(timeout), TimeUnit.NANOSECONDS);
<   }
< 
<   /**
<    * Invokes {@code condition.}{@link Condition#await(long, TimeUnit) await(timeout, unit)}
<    * uninterruptibly.
<    *
172,183d143
<   }
< 
<   /**
<    * Invokes {@code unit.}{@link TimeUnit#timedJoin(Thread, long) timedJoin(toJoin, timeout)
[... 3168 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/google__guava-3971/repo; sed -n 470,540p guava/src/com/google/common/util/concurrent/Uninterruptibles.java
```

tool result:

```
        Thread.currentThread().interrupt();
      }
    }
  }

  /**
   * Invokes {@code lock.}{@link Lock#tryLock(long, TimeUnit) tryLock(timeout, unit)}
   * uninterruptibly.
   *
   * @since NEXT
   */
  @GwtIncompatible // concurrency
  @Beta
  public static boolean tryLockUninterruptibly(Lock lock, Duration timeout) {
    return tryLockUninterruptibly(lock, toNanosSaturated(timeout), TimeUnit.NANOSECONDS);
  }

  /**
   * Invokes {@code lock.}{@link Lock#tryLock(long, TimeUnit) tryLock(timeout, unit)}
   * uninterruptibly.
   *
   * @since NEXT
   */
  @GwtIncompatible // concurrency
  @SuppressWarnings("GoodTime") // should accept a java.time.Duration
  public static boolean tryLockUninterruptibly(Lock lock, long timeout, TimeUnit unit) {
    boolean interrupted = false;
    try {
      long remainingNanos = unit.toNanos(timeout);
      long end = System.nanoTime() + remainingNanos;

      while (true) {
        try {
          return lock.tryLock(remainingNanos, NANOSECONDS);
        } catch (InterruptedException e) {
          interrupted = true;
          remainingNanos = end - System.nanoTime();
        }
      }
    } finally {
      if (interrupted) {
        Thread.currentThread().interrupt();
      }
    }
  }

  // TODO(user): Add support for waitUninterruptibly.

  private Uninterruptibles() {}
}
```

**tool call: Bash**

```bash
cd /work/google__guava-3971/repo; grep -rln "awaitTerminationUninterruptibly" . ; grep -n "awaitTermination" guava/src/com/google/common/util/concurrent/MoreExecutors.java | head
```

tool result:

```
./guava-tests/test/com/google/common/util/concurrent/FuturesTest.java
./android/guava-tests/test/com/google/common/util/concurrent/FuturesTest.java
275:                    service.awaitTermination(terminationTimeout, timeUnit);
359:    public boolean awaitTermination(long timeout, TimeUnit unit) throws InterruptedException {
586:    public final boolean awaitTermination(long timeout, TimeUnit unit) throws InterruptedException {
587:      return delegate.awaitTermination(timeout, unit);
1077:      if (!service.awaitTermination(halfTimeoutNanos, TimeUnit.NANOSECONDS)) {
1081:        service.awaitTermination(halfTimeoutNanos, TimeUnit.NANOSECONDS);
```

**tool call: Bash**

```bash
cd /work/google__guava-3971/repo; grep -n "awaitTerminationUninterruptibly\|^import static" guava-tests/test/com/google/common/util/concurrent/FuturesTest.java android/guava-tests/test/com/google/common/util/concurrent/FuturesTest.java
```

tool result:

```
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:19:import static com.google.common.base.Functions.constant;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:20:import static com.google.common.base.Functions.identity;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:21:import static com.google.common.base.Throwables.propagateIfInstanceOf;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:22:import static com.google.common.collect.Iterables.getOnlyElement;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:23:import static com.google.common.collect.Lists.newArrayList;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:24:import static com.google.common.collect.Sets.intersection;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:25:import static com.google.common.truth.Truth.assertThat;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:26:import static com.google.common.truth.Truth.assertWithMessage;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:27:import static com.google.common.util.concurrent.Futures.allAsList;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:28:import static com.google.common.util.concurrent.Futures.catching;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:29:import static com.google.common.util.concurrent.Futures.catchingAsync;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:30:import static com.google.common.util.concurrent.Futures.getDone;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:31:import static com.google.common.util.concurrent.Futures.immediateCancelledFuture;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:32:import static com.google.common.util.concurrent.Futures.immediateFailedFuture;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:33:import static com.google.common.util.concurrent.Futures.immediateFuture;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:34:import static com.google.common.util.concurrent.Futures.immediateVoidFuture;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:35:import static com.google.common.util.concurrent.Futures.inCompletionOrder;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:36:import static com.google.common.util.concurrent.Futures.lazyTransform;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:37:import static com.google.common.util.concurrent.Futures.nonCancellationPropagating;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:38:import static com.google.common.util.concurrent.Futures.scheduleAsync;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:39:import static com.google.common.util.concurrent.Futures.submit;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:40:import static com.google.common.util.concurrent.Futures.submitAsync;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:41:import static com.google.common.util.concurrent.Futures.successfulAsList;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:42:import static com.google.common.util.concurrent.Futures.transform;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:43:import static com.google.common.util.concurrent.Futures.transformAsync;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:44:import static com.google.common.util.concurrent.Futures.whenAllComplete;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:45:import static com.google.common.util.concurrent.Futures.whenAllSucceed;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:46:import static com.google.common.util.concurrent.MoreExecutors.directExecutor;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:47:import static com.google.common.util.concurrent.TestPlatform.clearInterrupt;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:48:import static com.google.common.util.concurrent.TestPlatform.getDoneFromTimeoutOverload;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:49:import static com.google.common.util.concurrent.Uninterruptibles.awaitUninterruptibly;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:50:import static com.google.common.util.concurrent.Uninterruptibles.getUninterruptibly;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:51:import static com.google.common.util.concurrent.testing.TestingExecutors.noOpScheduledExecutor;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:52:import static java.util.Arrays.asList;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:53:import static java.util.concurrent.Executors.newSingleThreadExecutor;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:54:import static java.util.concurrent.Executors.newSingleThreadScheduledExecutor;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:55:import static java.util.concurrent.TimeUnit.MILLISECONDS;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:56:import static java.util.concurrent.TimeUnit.SECONDS;
guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:3270:      // TODO(cpovirk: assertTrue(awaitTerminationUninterruptibly(executor, 10, SECONDS));
android/guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:19:import static com.google.common.base.Functions.constant;
android/guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:20:import static com.google.common.base.Functions.identity;
android/guava-tests/test/com/google/common/util/concurrent/FuturesTest.java:21:import static com.google.common.base.Throwables.propagateIfInstanceOf;
android/guava-tests/test/com/google/common/u
[... 5379 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/google__guava-3971/repo; python3 - <<'EOF'
def block(duration):
    s = '''  /**
   * Invokes {@code executor.}{@link ExecutorService#awaitTermination(long, TimeUnit)
   * awaitTermination(long, TimeUnit)} uninterruptibly with no timeout.
   *
   * @since NEXT
   */
  @Beta
  @GwtIncompatible // concurrency
  public static void awaitTerminationUninterruptibly(ExecutorService executor) {
    // TODO(cpovirk): We could optimize this to avoid calling nanoTime() at all.
    verify(awaitTerminationUninterruptibly(executor, Long.MAX_VALUE, NANOSECONDS));
  }

'''
    if duration:
        s += '''  /**
   * Invokes {@code executor.}{@link ExecutorService#awaitTermination(long, TimeUnit)
   * awaitTermination(long, TimeUnit)} uninterruptibly.
   *
   * @since NEXT
   */
  @Beta
  @GwtIncompatible // concurrency
  public static boolean awaitTerminationUninterruptibly(
      ExecutorService executor, Duration timeout) {
    return awaitTerminationUninterruptibly(executor, toNanosSaturated(timeout), NANOSECONDS);
  }

'''
    s += '''  /**
   * Invokes {@code executor.}{@link ExecutorService#awaitTermination(long, TimeUnit)
   * awaitTermination(long, TimeUnit)} uninterruptibly.
   *
   * @since NEXT
   */
  @Beta
  @GwtIncompatible // concurrency
  @SuppressWarnings("GoodTime") // should accept a java.time.Duration
  public static boolean awaitTerminationUninterruptibly(
      ExecutorService executor, long timeout, TimeUnit unit) {
    boolean interrupted = false;
    try {
      long remainingNanos = unit.toNanos(timeout);
      long end = System.nanoTime() + remainingNanos;

      while (true) {
        try {
          return executor.awaitTermination(remainingNanos, NANOSECONDS);
        } catch (InterruptedException e) {
          interrupted = true;
          remainingNanos = end - System.nanoTime();
        }
      }
    } finally {
      if (interrupted) {
        Thread.currentThread().interrupt();
      }
    }
  }

'''
    return s

for path, dur in [("guava/src/com/google/common/util/concurrent/Uninterruptibles.java", True),
                  ("android/guava/src/com/google/common/util/concurrent/Uninterruptibles.java", False)]:
    src = open(path).read()
    marker = "  // TODO(user): Add support for waitUninterruptibly."
    assert src.count(marker) == 1
    src = src.replace(marker, block(dur) + marker)
    src = src.replace("import static com.google.common.util.concurrent.Internal.toNanosSaturated;\n",
                      "import static com.google.common.base.Verify.verify;\nimport static com.google.common.util.concurrent.Internal.toNanosSaturated;\n") if dur else \
          src.replace("import static java.util.concurrent.TimeUnit.NANOSECONDS;\n",
                      "import static com.google.common.base.Verify.verify;\nimport static java.util.concurrent.TimeUnit.NANOSECONDS;\n")
    if not dur:
        src = src.replace("import com.google.common.annotations.GwtCompatible;\n",
                          "import com.google.common.annotations.Beta;\nimport com.google.common.annotations.GwtCompatible;\n")
    src = src.replace("import java.util.concurrent.ExecutionException;\n",
                      "import java.util.concurrent.ExecutionException;\nimport java.util.concurrent.ExecutorService;\n")
    open(path, "w").write(src)
EOF
git diff --stat; sed -n 15,40p android/guava/src/com/google/common/util/concurrent/Uninterruptibles.java
```

tool result:

```
 .../common/util/concurrent/Uninterruptibles.java   |   47 +
 guava-gwt/pom.xml                                  |  417 --
 .../common/base/ExtraObjectsMethodsForWeb.java     |   24 -
 .../super/com/google/common/base/Platform.java     |   95 -
 .../com/google/common/base/Platform.native.js      |   26 -
 .../super/com/google/common/cache/LocalCache.java  |  830 ---
 .../com/google/common/cache/LongAddables.java      |   28 -
 .../super/com/google/common/cache/LongAdder.java   |   39 -
 .../common/collect/AbstractSortedMultiset.java     |  143 -
 ...ayListMultimapGwtSerializationDependencies.java |   32 -
 .../google/common/collect/DescendingMultiset.java  |  153 -
 .../collect/ForwardingImmutableCollection.java     |   75 -
 .../common/collect/ForwardingImmutableList.java    |  100 -
 .../common/collect/ForwardingImmutableMap.java     |  135 -
 .../common/collect/ForwardingImmutableSet.java     |   84 -
 .../common/collect/ForwardingSortedMultiset.java   |  213 -
 .../HashMultimapGwtSerializationDependencies.java  |   31 -
 .../com/google/common/collect/ImmutableBiMap.java  |  165 -
 .../google/common/collect/ImmutableCollection.java |  170 -
 .../google/common/collect/ImmutableEnumMap.java    |   42 -
 .../google/common/collect/ImmutableEnumSet.java    |   42 -
 .../com/google/common/collect/ImmutableList.java   |  350 -
 .../com/google/common/collect/ImmutableMap.java    |  440 --
 ...utableMultisetGwtSerializationDependencies.java |   24 -
 .../com/google/common/collect/ImmutableSet.java    |  263 -
 .../google/common/collect/ImmutableSortedMap.java  |  390 --
 .../google/common/collect/ImmutableSortedSet.java  |  440 --
 .../common/collect/JdkBackedImmutableBiMap.java    |   26 -
 .../common/collect/JdkBackedImmutableMap.java      |   29 -
 ...edHashMultimapGwtSerializationDependencies.java |   32 -
 .../super/com/google/common/collect/MapMaker.java  |   53 -
 .../super/com/google/common/collect/Platform.java  |  114 -
 .../collect/RangeGwtSerializationDependencies.java |   25 -
 .../common/collect/RegularImmutableBiMap.java      |   61 -
 .../common/collect/RegularImmutableList.java       |   41 -
 .../google/common/collect/RegularImmutableMap.java |   35 -
 .../common/collect/RegularImmutableMultiset.java   |   57 -
 .../google/common/collect/RegularImmutableSet.java |   34 -
 .../common/collect/RegularImmutableSortedSet.java  |   44 -
 .../common/collect/SingletonImmutableBiMap.java    |   68 -
 .../common/collect/SingletonImmutableList.java     |   46 -
 .../common/collect/SingletonImmutableSet.java      |   53 -
 .../com/google/common/collect/SortedMultiset.java  |   57 -
 .../common/collect/UnmodifiableSortedMultiset.java |  106 -
 .../super/com/google/common/escape/Platform.java   |   33 -
 .../common/primitives/DoublesMethodsForWeb.java    |   28 -
 .../common/primitives/FloatsMethodsForWeb.java     |   28 -
 .../common/primitives/IntsMethodsForWeb.java       |   28 -
 .../com/google/common/primitives/Platform.java     |   32 -
 .../common/primitives/ShortsMethodsForWeb.java     |   28 -
 .../common/util/concurrent/AbstractFuture.java     |  423 --
 .../util/concurrent/AggregateFutureState.java      |   51 -
 .../GwtFluentFutureCatchingSpecialization.java     |   45 -
 .../GwtFuturesCatchingSpecialization.java          |   67 -
 .../common/util/concurrent/InterruptibleTask.java  |   46 -
 .../common/util/concurrent/ListenableFuture.java   |   69 -
 .../google/common/util/concurrent/Platform.java    |   30 -
 .../google/common/util/concurrent/Thenable.java    |   44 -
 .../common/util/concurrent/Uninterruptibles.java   |   35 -
 .../src/com/google/common/DummyJavadocClass.java   |   25 -
 .../google/common/ForceGuavaCompilation.gwt.xml    |   24 -
 .../common/ForceGuavaCompilationEntryPoint.java    |   29 -
 .../google/common/annotations/Annotations.gwt.xml  |   19 -
 .../common/base/Absent_CustomFieldSerializer.java  |   46 -
 guava-gwt/src/com/google/common/base/Base.gwt.xml  |   21 -
 .../common/base/GwtSerializationDependencies.java  |   98 -
 .../PairwiseEquivalence_CustomFieldSerializer.java |   52 -
 .../common/base/Present_CustomFieldSerializer.java |   46 -
 .../src/com/google/common/cache/Cache.gwt.xml      |   24 -
 .../AllEqualOrdering_CustomFieldSerializer.java    |   40 -
 .../ArrayListMultimap_CustomFieldSerializer.java   |   46 -
 .../ByFunctionOrdering_CustomFieldSerializer.java  |   50 -
 .../src/com/google/common/collect/Collect.gwt.xml  |   24 -
 .../ComparatorOrdering_CustomFieldSerializer.java  |   48 -
 .../CompoundOrdering_CustomFieldSerializer.java    |   57 -
 .../DenseImmutableTable_CustomFieldSerializer.java |   45 -
 ...mmutableListMultimap_CustomFieldSerializer.java |   43 -
 ...ImmutableSetMultimap_CustomFieldSerializer.java |   43 -
 .../ExplicitOrdering_CustomFieldSerializer.java    |   46 -
 ...wardingImmutableList_CustomFieldSerializer.java |   25 -
 ...rwardingImmutableSet_CustomFieldSerializer.java |   25 -
 .../collect/GwtSerializationDependencies.java      |  134 -
 .../HashBasedTable_CustomFieldSerializer.java      |   42 -
 .../HashMultimap_CustomFieldSerializer.java        |   46 -
 .../HashMultiset_CustomFieldSerializer.java        |   46 -
 .../ImmutableAsList_CustomFieldSerializer.java     |   25 -
 .../ImmutableBiMap_CustomFieldSerializer.java      |   25 -
 .../ImmutableEntry_CustomFieldSerializer.java      |   48 -
 .../ImmutableEnumMap_CustomFieldSerializer.java    |   55 -
 .../ImmutableEnumSet_CustomFieldSerializer.java    |   54 -
 ...mmutableListMultimap_CustomFieldSerializer.java |   48 -
 .../ImmutableList_CustomFieldSerializer.java       |   25 -
 .../ImmutableMultiset_CustomFieldSerializer.java   |   25 -
 ...ImmutableSetMultimap_CustomFieldSerializer.java |   57 -
 .../ImmutableSet_CustomFieldSerializer.java        |   25 -
 .../ImmutableSortedMap_CustomFieldSerializer.java  |   47 -
 ...mutableSortedMap_CustomFieldSerializerBase.java |   57 -
 .../ImmutableSortedSet_CustomFieldSerializer.java  |   25 -
 .../ImmutableT
[... 16121 more characters not shown]
```

**assistant:** My edits to both `Uninterruptibles.java` files are in. But `git diff --stat` also shows `guava-gwt/` deleted and `pom.xml` changed. I didn't touch those, so I'm checking where they came from.

**tool call: Bash**

```bash
cd /work/google__guava-3971/repo; git status --short | grep -v '^ D guava-gwt' ; git diff pom.xml; ls guava-gwt 2>&1 | head
```

tool result:

```
 M android/guava/src/com/google/common/util/concurrent/Uninterruptibles.java
 M guava/src/com/google/common/util/concurrent/Uninterruptibles.java
 M pom.xml
?? Dockerfile
diff --git a/pom.xml b/pom.xml
index 031be6836..ef9605b23 100644
--- a/pom.xml
+++ b/pom.xml
@@ -58,7 +58,7 @@
   <modules>
     <module>guava</module>
     <module>guava-bom</module>
-    <module>guava-gwt</module>
+     
     <module>guava-testlib</module>
     <module>guava-tests</module>
   </modules>
@@ -200,7 +200,7 @@
             <!-- By having our own entries here, we also override the default exclusion filter, which excludes all nested classes. -->
             <excludes>
               <!-- https://github.com/google/guava/issues/2840 -->
-              <exclude>%regex[.*PackageSanityTests.*.class]</exclude>
+<exclude>%regex[.*PackageSanityTests.*.class]</exclude><exclude>%regex[.*InetAddressesTest.*]</exclude><exclude>%regex[.*MoreFilesTest.*]</exclude>
               <!-- FeatureUtilTest.*ExampleDerivedInterfaceTester, com.google.common.io.*Tester, incidentally FeatureSpecificTestSuiteBuilderTest.MyAbstractTester (but we don't care either way because it's not meant to run on its own but works OK if it does)... but not NullPointerTesterTest, etc. -->
               <exclude>%regex[.*Tester.class]</exclude>
               <!-- Anonymous TestCase subclasses in GeneratedMonitorTest -->
ls: guava-gwt: No such file or directory
```

**thinking:**

```
The `guava-gwt` removal, pom.xml changes, and untracked Dockerfile are from the environment setup, not my edits, so I'll leave them as is. Now I'll compile and run a quick check.


```

**tool call: Bash**

```bash
cd /work/google__guava-3971/repo; mkdir -p /tmp/x; cat > Repro.java <<'EOF'
import static com.google.common.util.concurrent.Uninterruptibles.awaitTerminationUninterruptibly;
import java.time.Duration;
import java.util.concurrent.*;
public class Repro {
  public static void main(String[] a) throws Exception {
    ExecutorService e = Executors.newSingleThreadExecutor();
    CountDownLatch latch = new CountDownLatch(1);
    e.execute(() -> { try { latch.await(); } catch (InterruptedException ie) {} });
    e.shutdown();
    // timeout path, with interrupt
    Thread.currentThread().interrupt();
    long start = System.nanoTime();
    System.out.println("timed (expect false): " + awaitTerminationUninterruptibly(e, 200, TimeUnit.MILLISECONDS)
        + " elapsed>=200ms: " + ((System.nanoTime() - start) >= 200_000_000L)
        + " interrupted: " + Thread.interrupted());
    // interrupt from another thread during indefinite wait
    Thread main = Thread.currentThread();
    new Thread(() -> { try { Thread.sleep(100); main.interrupt(); Thread.sleep(100); } catch (InterruptedException ie) {} latch.countDown(); }).start();
    awaitTerminationUninterruptibly(e);
    System.out.println("terminated: " + e.isTerminated() + " interrupted: " + Thread.interrupted());
    System.out.println("duration (expect true): " + awaitTerminationUninterruptibly(e, Duration.ofSeconds(1)));
  }
}
EOF
../bin/envrun 'cd guava && mvn -o -q compile -DskipTests 2>&1 | tail -20; cd ../android/guava && mvn -o -q compile 2>&1 | tail -20; cd /testbed && javac -cp guava/target/classes -d /tmp/x Repro.java && java -cp guava/target/classes:/tmp/x Repro'
```

tool result:

```
Exit code 1
mkdir: /tmp/x: Operation not permitted
Error: A JNI error has occurred, please check your installation and try again
Exception in thread "main" java.lang.UnsupportedClassVersionError: Repro has been compiled by a more recent version of the Java Runtime (class file version 61.0), this version of the Java Runtime only recognizes class file versions up to 52.0
	at java.lang.ClassLoader.defineClass1(Native Method)
	at java.lang.ClassLoader.defineClass(ClassLoader.java:756)
	at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:142)
	at java.net.URLClassLoader.defineClass(URLClassLoader.java:473)
	at java.net.URLClassLoader.access$100(URLClassLoader.java:74)
	at java.net.URLClassLoader$1.run(URLClassLoader.java:369)
	at java.net.URLClassLoader$1.run(URLClassLoader.java:363)
	at java.security.AccessController.doPrivileged(Native Method)
	at java.net.URLClassLoader.findClass(URLClassLoader.java:362)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:418)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:352)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:351)
	at sun.launcher.LauncherHelper.checkAndLoadMain(LauncherHelper.java:621)
```

**assistant:** Both modules compiled. The container has mismatched `javac`/`java` versions, so I'll compile the check with `--release 8`.

**tool call: Bash**

```bash
cd /work/google__guava-3971/repo; ../bin/envrun 'mkdir -p /tmp/x && javac --release 8 -cp guava/target/classes -d /tmp/x Repro.java && java -cp guava/target/classes:/tmp/x Repro'
```

tool result:

```
timed (expect false): false elapsed>=200ms: true interrupted: true
terminated: true interrupted: true
duration (expect true): true
```

**thinking:**

```
All three overloads check out—timeout works, interrupts don't break the wait, and the interrupt flag gets reset properly. I'll clean up the check file now and run the nearby existing tests.


```

**tool call: Bash**

```bash
cd /work/google__guava-3971/repo; rm Repro.java; ../bin/envrun 'rm -rf /tmp/x; mvn -o -q test -pl guava,guava-testlib,guava-tests -Dtest="UninterruptiblesTest,FuturesTest" -DfailIfNoTests=false 2>&1 | grep -E "Tests run|FAIL|ERROR" | head -20'
```

tool result:

```
Tests run: 0, Failures: 0, Errors: 0, Skipped: 0
Tests run: 0, Failures: 0, Errors: 0, Skipped: 0
Tests run: 160, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 4.251 sec
Tests run: 44, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 7.789 sec
Tests run: 204, Failures: 0, Errors: 0, Skipped: 0
```

**tool call: Bash**

```bash
cd /work/google__guava-3971/repo; git status --short | grep -v guava-gwt
```

tool result:

```
 M android/guava/src/com/google/common/util/concurrent/Uninterruptibles.java
 M guava/src/com/google/common/util/concurrent/Uninterruptibles.java
 M pom.xml
?? Dockerfile
```

**assistant:** I added `awaitTerminationUninterruptibly` to `Uninterruptibles`, as the issue asks. A quick check showed it works, and `UninterruptiblesTest` and `FuturesTest` pass (204 tests, 0 failures).

**New methods in `guava/src/com/google/common/util/concurrent/Uninterruptibles.java`:**
- `boolean awaitTerminationUninterruptibly(ExecutorService executor, long timeout, TimeUnit unit)` waits for the executor to finish, up to the timeout. If the thread is interrupted, it keeps waiting until the deadline and then sets the interrupt flag again. It uses the same loop as the existing `awaitUninterruptibly(CountDownLatch, …)` methods.
- `boolean awaitTerminationUninterruptibly(ExecutorService executor, Duration timeout)` is a `java.time.Duration` version, matching the other Duration overloads in that file.
- `void awaitTerminationUninterruptibly(ExecutorService executor)` waits with no time limit (the "till the end of all days" case from the issue). It calls the timed version with `Long.MAX_VALUE` nanoseconds and uses `verify` to check that it returned `true`.

The Android copy (`android/guava/.../Uninterruptibles.java`) has the same methods except the `Duration` one, because that copy has no `Duration` overloads. The new methods are marked `@Beta`, `@GwtIncompatible` and `@since NEXT`, like the file's other recent additions.

**Check:** I compiled both modules and ran a throwaway program against the new methods (since deleted):
- The timed version returned `false` after the full 200 ms, even though the thread was interrupted beforehand, and the interrupt flag was set again afterwards.
- The no-timeout version kept waiting through an interrupt from another thread, returned once the executor had terminated, and set the interrupt flag again.
- The `Duration` version returned `true` for an executor that had already terminated.

`FuturesTest` has a commented-out TODO that would use the new method. I left it alone because you said the tests were already handled.

The working tree also shows `guava-gwt/` deleted, `pom.xml` modified and an untracked `Dockerfile`. Those changes were already there from the environment setup, not from me, and I didn't touch them.

_session end: success, turns 12, is_error False_

## Container commands (task container, no network; broker log)

- `rc=1` 52.37 s: cd guava && mvn -o -q compile -DskipTests 2>&1 | tail -20; cd ../android/guava && mvn -o -q compile 2>&1 | tail -20; cd /testbed && javac -cp guava/target/classes -d /tmp/x Repro.java && java -cp guava/target/classes:/tmp/x Repro
- `rc=0` 2.27 s: mkdir -p /tmp/x && javac --release 8 -cp guava/target/classes -d /tmp/x Repro.java && java -cp guava/target/classes:/tmp/x Repro
- `rc=0` 50.16 s: rm -rf /tmp/x; mvn -o -q test -pl guava,guava-testlib,guava-tests -Dtest="UninterruptiblesTest,FuturesTest" -DfailIfNoTests=false 2>&1 | grep -E "Tests run|FAIL|ERROR" | head -20
