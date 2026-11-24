# Instance: apache__rocketmq-7712

- Final resolved (evaluator, logs/apache__rocketmq-7712_result.json): True
- Run state: DONE
- One attempt. Duration 149.7 s, turns 17, actor cost $0.30423300000000003, container commands 10
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/apache__rocketmq-7712/repo
</uploaded_files>
I've uploaded a Java code repository in the directory /work/apache__rocketmq-7712/repo. Consider the following issue description:

<issue_description>
[Bug] Deleting the last item problem of the ACL topic/group perms or the global white list caused by the UtilAll#split func flaw
### Before Creating the Bug Report

- [X] I found a bug, not just asking a question, which should be created in [GitHub Discussions](https://github.com/apache/rocketmq/discussions).

- [X] I have searched the [GitHub Issues](https://github.com/apache/rocketmq/issues) and [GitHub Discussions](https://github.com/apache/rocketmq/discussions)  of this repository and believe that this is not a duplicate.

- [X] I have confirmed that this bug belongs to the current repository, not other repositories of RocketMQ.


### Runtime platform environment

OS(CentOS release 7.6.1810)

### RocketMQ version

branch(develop) version(5.1.5-SNAPSHOT)

### JDK Version

Compliler(Oracke JDK 1.8.0_361) OS(CentOS release 7.6.1810)

### Describe the Bug

I found an bug of ACL during my work on RocketMQ.
When I tried to delete the last item of the ACL topic/group perms, there was an error which indicates the resouce fomat is incrorrect. And there's also an similar problem of the global white list, which is always remain an empty data at last.

### Steps to Reproduce

**To reproduce you can use two ways:**
1. If you use the Dashboard(take the topic/group perms for example)
1.1 Create an ACL with mutiple topic perms and group perms.
1.2 Delete the topic perms or group perms one by one.
1.3 The error woud appear when delete the last one.

![AgAACF5zlnReY1XDkERMf6P-SgV5fqC1](https://github.com/apache/rocketmq/assets/29912051/10e0ddc4-84a9-4306-9f13-b29a26c2cddc)
![AgAACF5zlnR_G2hISrFGkp9IHvbLVnhw](https://github.com/apache/rocketmq/assets/29912051/641c7900-25ae-422f-b892-78725dba4fe3)
![AgAACF5zlnQIxRfBwMZA4odWFJ1KCjd_](https://github.com/apache/rocketmq/assets/29912051/64ca490f-838a-43da-b16a-92fc2995a509)

2. If you want to create an test method for reproduce
2.1 New an DefaultMQAdminExt and config it with namesrv and then start it.
2.2 New an PlainAccessConfig and setGroupPerms(Collections.EMPTY_LIST), setTopicPerms(Collections.EMPTY_LIST).
2.3 Then call DefaultMQAdminExt #createAndUpdatePlainAccessConfig.
2.4 Or to call DefaultMQAdminExt #updateGlobalWhiteAddrConfig with the second parmeter an empty string.

![图片](https://github.com/apache/rocketmq/assets/29912051/978d469c-a105-4109-bc9a-76491a5b7cbc)
![图片](https://github.com/apache/rocketmq/assets/29912051/f0c277ee-1e91-4c6e-a627-320c2ac59ec4)


### What Did You Expect to See?

For the topic/group perms, it should not be an error to delete the last item.
![图片](https://github.com/apache/rocketmq/assets/29912051/26cc5b3d-6b9f-455f-a1ba-5c67668dc20f)


For the global white list, it should not be an empty data

![图片](https://github.com/apache/rocketmq/assets/29912051/04377834-cdd7-4a6f-a929-c68bd00482ce)


### What Did You See Instead?

For the topic/group perms, it popup an error: 
org.apache.rocketmq.client.exception.MQClientException: CODE: 209  DESC: Parse Resource format error for .
The expected resource format is 'Res=Perm'. For example: topicA=SUB

![AgAACF5zlnReY1XDkERMf6P-SgV5fqC1](https://github.com/apache/rocketmq/assets/29912051/b06c98b8-852e-4227-9d13-dde47df42f03)

For the global white list, it remains an empty data

![AgAACF5zlnR_G2hISrFGkp9IHvbLVnhw](https://github.com/apache/rocketmq/assets/29912051/794828f0-6471-446c-a885-6e4cd4949803)


### Additional Context

**I've already found and fixed the bug, and I'll submit an PR later.**

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/apache__rocketmq-7712/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/apache__rocketmq-7712/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/apache__rocketmq-7712/bin/envrun 'git status --short && ls'
Edits you make under /work/apache__rocketmq-7712/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/apache__rocketmq-7712/repo; grep -n "split" -A25 common/src/main/java/org/apache/rocketmq/common/UtilAll.java | head -60; grep -rn "UtilAll.split" --include=*.java . | grep -v /test/
```

tool result:

```
119:        String[] whiles = when.split(";");
120-        if (whiles.length > 0) {
121-            Calendar now = Calendar.getInstance();
122-            for (String w : whiles) {
123-                int nowHour = Integer.parseInt(w);
124-                if (nowHour == now.get(Calendar.HOUR_OF_DAY)) {
125-                    return true;
126-                }
127-            }
128-        }
129-
130-        return false;
131-    }
132-
133-    public static String timeMillisToHumanString() {
134-        return timeMillisToHumanString(System.currentTimeMillis());
135-    }
136-
137-    public static String timeMillisToHumanString(final long t) {
138-        Calendar cal = Calendar.getInstance();
139-        cal.setTimeInMillis(t);
140-        return String.format("%04d%02d%02d%02d%02d%02d%03d", cal.get(Calendar.YEAR), cal.get(Calendar.MONTH) + 1,
141-            cal.get(Calendar.DAY_OF_MONTH), cal.get(Calendar.HOUR_OF_DAY), cal.get(Calendar.MINUTE), cal.get(Calendar.SECOND),
142-            cal.get(Calendar.MILLISECOND));
143-    }
144-
--
663:    public static String join(List<String> list, String splitter) {
664-        if (list == null) {
665-            return null;
666-        }
667-
668-        StringBuilder str = new StringBuilder();
669-        for (int i = 0; i < list.size(); i++) {
670-            str.append(list.get(i));
671-            if (i == list.size() - 1) {
672-                break;
673-            }
674:            str.append(splitter);
675-        }
676-        return str.toString();
677-    }
678-
679:    public static List<String> split(String str, String splitter) {
680-        if (str == null) {
681-            return null;
682-        }
683-
684:        String[] addrArray = str.split(splitter);
685-        return Arrays.asList(addrArray);
686-    }
687-
688-    public static void deleteEmptyDirectory(File file) {
689-        if (file == null || !file.exists()) {
690-            return;
691-        }
692-        if (!file.isDirectory()) {
693-            return;
694-        }
695-        File[] files = file.listFiles();
(eval):1: no matches found: --include=*.java
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-7712/repo; grep -rn "UtilAll.split\|testSplit" . --include='*.java' -A12 | grep -i "split\|assert" | head -40; grep -n "^import" common/src/main/java/org/apache/rocketmq/common/UtilAll.java
```

tool result:

```
./broker/src/main/java/org/apache/rocketmq/broker/processor/AdminBrokerProcessor.java:598:        accessConfig.setTopicPerms(UtilAll.split(requestHeader.getTopicPerms(), ","));
./broker/src/main/java/org/apache/rocketmq/broker/processor/AdminBrokerProcessor.java:599:        accessConfig.setGroupPerms(UtilAll.split(requestHeader.getGroupPerms(), ","));
./broker/src/main/java/org/apache/rocketmq/broker/processor/AdminBrokerProcessor.java:672:            if (accessValidator.updateGlobalWhiteAddrsConfig(UtilAll.split(requestHeader.getGlobalWhiteAddrs(), ","),
./tieredstore/src/test/java/org/apache/rocketmq/tieredstore/util/MessageBufferUtilTest.java:153:    public void testSplitMessages() {
19:import io.netty.util.internal.PlatformDependent;
20:import java.io.ByteArrayInputStream;
21:import java.io.ByteArrayOutputStream;
22:import java.io.File;
23:import java.io.IOException;
24:import java.lang.management.ManagementFactory;
25:import java.net.Inet4Address;
26:import java.net.Inet6Address;
27:import java.net.InetAddress;
28:import java.net.NetworkInterface;
29:import java.nio.ByteBuffer;
30:import java.nio.file.Files;
31:import java.text.NumberFormat;
32:import java.text.ParseException;
33:import java.text.SimpleDateFormat;
34:import java.util.Arrays;
35:import java.util.Calendar;
36:import java.util.Date;
37:import java.util.Enumeration;
38:import java.util.Iterator;
39:import java.util.List;
40:import java.util.Map;
41:import java.util.concurrent.TimeUnit;
42:import java.util.function.Supplier;
43:import java.util.zip.CRC32;
44:import java.util.zip.DeflaterOutputStream;
45:import java.util.zip.InflaterInputStream;
46:import org.apache.commons.lang3.StringUtils;
47:import org.apache.commons.validator.routines.InetAddressValidator;
48:import org.apache.rocketmq.common.constant.LoggerName;
49:import org.apache.rocketmq.logging.org.slf4j.Logger;
50:import org.apache.rocketmq.logging.org.slf4j.LoggerFactory;
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-7712/repo; grep -n "split" -B3 -A15 common/src/test/java/org/apache/rocketmq/common/UtilAllTest.java
```

tool result:

```
(Bash completed with no output)
```

**assistant:** Root cause: `"".split(",")` returns `[""]`, so an empty perms/white-list string becomes a one-element list containing an empty string. Let me reproduce first.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-7712/repo; mkdir -p /tmp/r && cat > /tmp/r/Repro.java <<'EOF'
public class Repro { public static void main(String[] a){
  System.out.println(org.apache.rocketmq.common.UtilAll.split("", ",").size());
  System.out.println(org.apache.rocketmq.common.UtilAll.split("a,b", ","));
  System.out.println(org.apache.rocketmq.common.UtilAll.split(null, ","));
}}
EOF
cp /tmp/r/Repro.java ./Repro.java
../bin/envrun 'mvn -q -o compile -pl common -am -DskipTests -Dcheckstyle.skip -Drat.skip -Dspotbugs.skip 2>&1 | tail -5; CP=$(cd common && mvn -q -o dependency:build-classpath -Dmdep.outputFile=/dev/stdout); javac -cp common/target/classes:$CP -d /tmp Repro.java && java -cp /tmp:common/target/classes:$CP Repro'
```

tool result:

```
Exit code 2
mkdir: /tmp/r: Operation not permitted
cp: /tmp/r/Repro.java: No such file or directory
error: invalid flag: for
Usage: javac <options> <source files>
use --help for a list of possible options
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-7712/repo; cat > Repro.java <<'EOF'
public class Repro { public static void main(String[] a){
  System.out.println(org.apache.rocketmq.common.UtilAll.split("", ",").size());
  System.out.println(org.apache.rocketmq.common.UtilAll.split("a,b", ","));
  System.out.println(org.apache.rocketmq.common.UtilAll.split(null, ","));
}}
EOF
../bin/envrun 'mvn -q -o compile -pl common -am -DskipTests -Dcheckstyle.skip -Drat.skip -Dspotbugs.skip 2>&1 | tail -5; (cd common && mvn -q -o dependency:build-classpath -Dmdep.outputFile=/tmp/cp.txt >/dev/null); CP=$(cat /tmp/cp.txt); javac -cp common/target/classes:$CP -d /tmp Repro.java && java -cp /tmp:common/target/classes:$CP Repro'
```

tool result:

```
Exit code 1
cat: /tmp/cp.txt: No such file or directory
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

**tool call: Bash**

```bash
cd /work/apache__rocketmq-7712/repo; ../bin/envrun 'CP=$(find ~/.m2 -name "commons-lang3*.jar" | head -1); javac --release 8 -cp common/target/classes -d /tmp Repro.java && java -cp /tmp:common/target/classes:$CP Repro'
```

tool result:

```
Exit code 1
Exception in thread "main" java.lang.NoClassDefFoundError: org/apache/rocketmq/logging/org/slf4j/LoggerFactory
	at org.apache.rocketmq.common.UtilAll.<clinit>(UtilAll.java:53)
	at Repro.main(Repro.java:2)
Caused by: java.lang.ClassNotFoundException: org.apache.rocketmq.logging.org.slf4j.LoggerFactory
	at java.net.URLClassLoader.findClass(URLClassLoader.java:387)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:418)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:352)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:351)
	... 2 more
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-7712/repo; ../bin/envrun 'CP=$(find ~/.m2 -name "commons-lang3*.jar" -o -name "rocketmq-logging-noop*.jar" -o -name "logback*.jar" -o -name "rocketmq-shaded-slf4j*.jar" -o -name "rocketmq-slf4j*.jar" | tr "\n" :); java -cp /tmp:common/target/classes:$CP Repro'
```

tool result:

```
SLF4J: No SLF4J providers were found.
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See https://www.slf4j.org/codes.html#noProviders for further details.
1
[a, b]
null
```

**assistant:** Reproduced: `split("", ",")` returns a list with one empty string. Now the fix:

**tool call: Bash**

```bash
cd /work/apache__rocketmq-7712/repo; python3 - <<'EOF'
p='common/src/main/java/org/apache/rocketmq/common/UtilAll.java'
s=open(p).read()
s=s.replace("""            return null;
        }

        String[] addrArray = str.split(splitter);""","""            return null;
        }

        if (StringUtils.isBlank(str)) {
            return Collections.EMPTY_LIST;
        }

        String[] addrArray = str.split(splitter);""",1)
s=s.replace("import java.util.Calendar;\n","import java.util.Calendar;\nimport java.util.Collections;\n",1)
open(p,'w').write(s)
EOF
git diff
```

tool result:

```
diff --git a/common/src/main/java/org/apache/rocketmq/common/UtilAll.java b/common/src/main/java/org/apache/rocketmq/common/UtilAll.java
index 19efa9aa9..8f4ca7504 100644
--- a/common/src/main/java/org/apache/rocketmq/common/UtilAll.java
+++ b/common/src/main/java/org/apache/rocketmq/common/UtilAll.java
@@ -33,6 +33,7 @@ import java.text.ParseException;
 import java.text.SimpleDateFormat;
 import java.util.Arrays;
 import java.util.Calendar;
+import java.util.Collections;
 import java.util.Date;
 import java.util.Enumeration;
 import java.util.Iterator;
@@ -681,6 +682,10 @@ public class UtilAll {
             return null;
         }
 
+        if (StringUtils.isBlank(str)) {
+            return Collections.EMPTY_LIST;
+        }
+
         String[] addrArray = str.split(splitter);
         return Arrays.asList(addrArray);
     }
diff --git a/pom.xml b/pom.xml
index 49c92d2fa..d73c13d83 100644
--- a/pom.xml
+++ b/pom.xml
@@ -390,7 +390,7 @@
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
I'll switch to the type-safe `Collections.emptyList()` instead of the raw `EMPTY_LIST`, then rebuild and rerun the repro, leaving the pre-existing `pom.xml` diff untouched.


```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-7712/repo; sed -i '' 's/return Collections.EMPTY_LIST;/return Collections.emptyList();/' common/src/main/java/org/apache/rocketmq/common/UtilAll.java; sed -i '' 's/split("", ",").size()/split("", ",").size() + " " + org.apache.rocketmq.common.UtilAll.split("  ", ",").size()/' Repro.java
../bin/envrun 'mvn -q -o compile -pl common -DskipTests -Dcheckstyle.skip -Drat.skip -Dspotbugs.skip 2>&1 | tail -5; CP=$(find ~/.m2 -name "commons-lang3*.jar" -o -name "rocketmq-slf4j*.jar" -o -name "rocketmq-shaded-slf4j*.jar" | tr "\n" :); javac --release 8 -cp common/target/classes -d /tmp Repro.java && java -cp /tmp:common/target/classes:$CP Repro 2>/dev/null'
```

tool result:

```
0 0
[a, b]
null
```

**assistant:** Fixed. Now let me check that the ACL code handles an empty list properly.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-7712/repo; grep -n "TopicPerms\|GroupPerms\|globalWhiteRemoteAddresses" acl/src/main/java/org/apache/rocketmq/acl/plain/PlainPermissionManager.java | head -30
```

tool result:

```
140:            List<String> globalWhiteRemoteAddressesList = plainAclConfData.getGlobalWhiteRemoteAddresses();
141:            if (globalWhiteRemoteAddressesList != null && !globalWhiteRemoteAddressesList.isEmpty()) {
142:                for (int j = 0; j < globalWhiteRemoteAddressesList.size(); j++) {
144:                        getRemoteAddressStrategy(globalWhiteRemoteAddressesList.get(j)));
220:        List<String> globalWhiteRemoteAddressesList = plainAclConfData.getGlobalWhiteRemoteAddresses();
221:        if (globalWhiteRemoteAddressesList != null && !globalWhiteRemoteAddressesList.isEmpty()) {
222:            for (int i = 0; i < globalWhiteRemoteAddressesList.size(); i++) {
224:                    getRemoteAddressStrategy(globalWhiteRemoteAddressesList.get(i)));
309:        Permission.checkResourcePerms(plainAccessConfig.getTopicPerms());
310:        Permission.checkResourcePerms(plainAccessConfig.getGroupPerms());
428:        if (plainAccessConfig.getTopicPerms() != null) {
429:            newAccountsMap.setTopicPerms(plainAccessConfig.getTopicPerms());
431:        if (plainAccessConfig.getGroupPerms() != null) {
432:            newAccountsMap.setGroupPerms(plainAccessConfig.getGroupPerms());
532:                        plainAccessConfig.setGroupPerms(plainAccessConfigs.get(j).getGroupPerms());
538:                        plainAccessConfig.setTopicPerms(plainAccessConfigs.get(j).getTopicPerms());
```

**assistant:** An empty list now passes `checkResourcePerms` and replaces the stored perms, which is what we want. Next I'll clean up and run the nearest tests.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-7712/repo; rm Repro.java; ../bin/envrun 'rm -f /tmp/Repro.class; mvn -o test -pl common -Dtest=UtilAllTest -DfailIfNoTests=false -Drat.skip -Dspotbugs.skip -Djacoco.skip 2>&1 | grep -E "Tests run|BUILD|ERROR" | tail -8'; git status --short
```

tool result:

```
[ERROR] 
[ERROR] -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoExecutionException

 M common/src/main/java/org/apache/rocketmq/common/UtilAll.java
 M pom.xml
?? Dockerfile
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-7712/repo; ../bin/envrun 'mvn -o test -pl common -Dtest=UtilAllTest -DfailIfNoTests=false -Drat.skip -Dspotbugs.skip -Djacoco.skip 2>&1 | grep -E "ERROR|Tests run|BUILD" | head -15'
```

tool result:

```
[INFO] BUILD FAILURE
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:2.19.1:test (default-test) on project rocketmq-common: Unable to generate classpath: org.apache.maven.artifact.resolver.MultipleArtifactsNotFoundException: Missing:
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
```

**assistant:** Surefire's JUnit4 provider isn't in the offline cache. I'll check which providers are available.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-7712/repo; ../bin/envrun 'ls ~/.m2/repository/org/apache/maven/surefire/; ls ~/.m2/repository/org/apache/maven/surefire/surefire-junit4* 2>/dev/null'
```

tool result:

```
Exit code 2
maven-surefire-common
surefire
surefire-api
surefire-booter
```

**assistant:** The surefire provider isn't installed, so I'll run `UtilAllTest` directly with JUnitCore.

**tool call: Bash**

```bash
cd /work/apache__rocketmq-7712/repo; ../bin/envrun 'cd common && mvn -q -o test-compile -Drat.skip -Dspotbugs.skip -Dcheckstyle.skip >/dev/null 2>&1; mvn -q -o dependency:build-classpath -Dmdep.outputFile=/testbed/common/cp.txt >/dev/null 2>&1; java -cp target/test-classes:target/classes:$(cat cp.txt) org.junit.runner.JUnitCore org.apache.rocketmq.common.UtilAllTest 2>&1 | tail -5; rm -f cp.txt'
```

tool result:

```
cat: cp.txt: No such file or directory
Error: Could not find or load main class org.junit.runner.JUnitCore
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-7712/repo; ../bin/envrun 'cd common && ls target/test-classes/org/apache/rocketmq/common/UtilAllTest.class; CP=$(find ~/.m2 -name "*.jar" | grep -E "junit-4|hamcrest|assertj|mockito|byte-buddy|objenesis|commons-lang3|commons-validator|netty-all|guava|rocketmq-slf4j|rocketmq-logback|logback|fastjson|commons-codec" | tr "\n" :); java -cp target/test-classes:target/classes:$CP org.junit.runner.JUnitCore org.apache.rocketmq.common.UtilAllTest 2>&1 | grep -vE "^\s+at " | tail -15'
```

tool result:

```
target/test-classes/org/apache/rocketmq/common/UtilAllTest.class
23:30:41,116 |-INFO in org.apache.rocketmq.logging.ch.qos.logback.classic.model.processor.LoggerModelHandler - Setting additivity of logger [org.apache.rocketmq] to false
23:30:41,116 |-INFO in org.apache.rocketmq.logging.ch.qos.logback.core.model.processor.AppenderRefModelHandler - Attaching appender named [CONSOLE] to Logger[org.apache.rocketmq]
23:30:41,117 |-INFO in org.apache.rocketmq.logging.ch.qos.logback.classic.model.processor.RootLoggerModelHandler - Setting level of ROOT logger to ERROR
23:30:41,117 |-INFO in org.apache.rocketmq.logging.ch.qos.logback.core.model.processor.AppenderRefModelHandler - Attaching appender named [CONSOLE] to Logger[ROOT]
23:30:41,117 |-INFO in org.apache.rocketmq.logging.ch.qos.logback.core.model.processor.DefaultProcessor@1990a65e - End of configuration.
23:30:41,117 |-INFO in org.apache.rocketmq.common.logging.JoranConfiguratorExt@64485a47 - Registering current configuration as safe fallback point

.......23:30:41.217 [main] ERROR RocketmqStore - Error when measuring disk space usage, path is null or empty, path : null
23:30:41.220 [main] ERROR RocketmqStore - Error when measuring disk space usage, path is null or empty, path : 
23:30:41.220 [main] ERROR RocketmqStore - Error when measuring disk space usage, file doesn't exist on this path: nonExistingPath
...
Time: 0.454

OK (11 tests)
```

**tool call: Bash**

```bash
cd /work/apache__rocketmq-7712/repo; git status --short; git diff common
```

tool result:

```
 M common/src/main/java/org/apache/rocketmq/common/UtilAll.java
 M pom.xml
?? Dockerfile
diff --git a/common/src/main/java/org/apache/rocketmq/common/UtilAll.java b/common/src/main/java/org/apache/rocketmq/common/UtilAll.java
index 19efa9aa9..f16bb88ff 100644
--- a/common/src/main/java/org/apache/rocketmq/common/UtilAll.java
+++ b/common/src/main/java/org/apache/rocketmq/common/UtilAll.java
@@ -33,6 +33,7 @@ import java.text.ParseException;
 import java.text.SimpleDateFormat;
 import java.util.Arrays;
 import java.util.Calendar;
+import java.util.Collections;
 import java.util.Date;
 import java.util.Enumeration;
 import java.util.Iterator;
@@ -681,6 +682,10 @@ public class UtilAll {
             return null;
         }
 
+        if (StringUtils.isBlank(str)) {
+            return Collections.emptyList();
+        }
+
         String[] addrArray = str.split(splitter);
         return Arrays.asList(addrArray);
     }
```

**assistant:** I fixed the bug in `UtilAll.split` (`common/src/main/java/org/apache/rocketmq/common/UtilAll.java`). An empty or whitespace-only input now returns an empty list.

**Cause:** when you delete the last topic/group perm or white-list entry, the client sends an empty string. The broker passes it to `UtilAll.split(str, ",")` in `AdminBrokerProcessor`, and in Java `"".split(",")` returns `[""]`, a list holding one empty string, not an empty list. That one `""` caused both symptoms:
- **Topic/group perms:** `Permission.checkResourcePerms` tried to parse `""` as `Res=Perm` and failed with `CODE: 209 Parse Resource format error for .`
- **Global white list:** `""` was saved as an entry, which is the empty data you saw left behind.

**Fix:**
```java
if (StringUtils.isBlank(str)) {
    return Collections.emptyList();
}
```
`null` still returns `null`. That matters because `PlainPermissionManager` treats a `null` perms list as "leave unchanged" and an empty list as "clear all". Non-empty input is split exactly as before.

**Checks:**
- **Reproduction:** before the fix, `split("", ",")` returned a list of size 1. After it, both `""` and `"  "` return size 0, `"a,b"` still gives `[a, b]`, and `null` still gives `null`.
- **ACL path:** an empty list passes `checkResourcePerms` and replaces the stored perms, so deleting the last item now clears them as expected.
- **Existing tests:** `UtilAllTest` passes (11 tests). I couldn't run it through `mvn test` because the surefire JUnit4 provider isn't in the offline Maven cache, so I ran it directly with JUnitCore.

I deleted my reproduction files afterwards. The `pom.xml` change and the untracked `Dockerfile` in `git status` were already there when I started, and I didn't touch them.

_session end: success, turns 17, is_error False_

## Container commands (task container, no network; broker log)

- `rc=2` 12.5 s: mvn -q -o compile -pl common -am -DskipTests -Dcheckstyle.skip -Drat.skip -Dspotbugs.skip 2>&1 | tail -5; CP=$(cd common && mvn -q -o dependency:build-classpath -Dmdep.outputFile=/dev/stdout); javac -cp common/target/classes:$CP -d /tmp Repro.java && java -cp /tmp:common/target/classes:$CP Repro
- `rc=1` 12.55 s: mvn -q -o compile -pl common -am -DskipTests -Dcheckstyle.skip -Drat.skip -Dspotbugs.skip 2>&1 | tail -5; (cd common && mvn -q -o dependency:build-classpath -Dmdep.outputFile=/tmp/cp.txt >/dev/null); CP=$(cat /tmp/cp.txt); javac -cp common/target/classes:$CP -d /tmp Repro.java && java -cp /tmp:common/target/classes:$CP Repro
- `rc=1` 1.6 s: CP=$(find ~/.m2 -name "commons-lang3*.jar" | head -1); javac --release 8 -cp common/target/classes -d /tmp Repro.java && java -cp /tmp:common/target/classes:$CP Repro
- `rc=0` 0.76 s: CP=$(find ~/.m2 -name "commons-lang3*.jar" -o -name "rocketmq-logging-noop*.jar" -o -name "logback*.jar" -o -name "rocketmq-shaded-slf4j*.jar" -o -name "rocketmq-slf4j*.jar" | tr "\n" :); java -cp /tmp:common/target/classes:$CP Repro
- `rc=0` 13.8 s: mvn -q -o compile -pl common -DskipTests -Dcheckstyle.skip -Drat.skip -Dspotbugs.skip 2>&1 | tail -5; CP=$(find ~/.m2 -name "commons-lang3*.jar" -o -name "rocketmq-slf4j*.jar" -o -name "rocketmq-shaded-slf4j*.jar" | tr "\n" :); javac --release 8 -cp common/target/classes -d /tmp Repro.java && java -cp /tmp:common/target/classes:$CP Repro 2>/dev/null
- `rc=0` 10.24 s: rm -f /tmp/Repro.class; mvn -o test -pl common -Dtest=UtilAllTest -DfailIfNoTests=false -Drat.skip -Dspotbugs.skip -Djacoco.skip 2>&1 | grep -E "Tests run|BUILD|ERROR" | tail -8
- `rc=0` 9.73 s: mvn -o test -pl common -Dtest=UtilAllTest -DfailIfNoTests=false -Drat.skip -Dspotbugs.skip -Djacoco.skip 2>&1 | grep -E "ERROR|Tests run|BUILD" | head -15
- `rc=2` 0.3 s: ls ~/.m2/repository/org/apache/maven/surefire/; ls ~/.m2/repository/org/apache/maven/surefire/surefire-junit4* 2>/dev/null
- `rc=0` 10.96 s: cd common && mvn -q -o test-compile -Drat.skip -Dspotbugs.skip -Dcheckstyle.skip >/dev/null 2>&1; mvn -q -o dependency:build-classpath -Dmdep.outputFile=/testbed/common/cp.txt >/dev/null 2>&1; java -cp target/test-classes:target/classes:$(cat cp.txt) org.junit.runner.JUnitCore org.apache.rocketmq.common.UtilAllTest 2>&1 | tail -5; rm -f cp.txt
- `rc=0` 1.27 s: cd common && ls target/test-classes/org/apache/rocketmq/common/UtilAllTest.class; CP=$(find ~/.m2 -name "*.jar" | grep -E "junit-4|hamcrest|assertj|mockito|byte-buddy|objenesis|commons-lang3|commons-validator|netty-all|guava|rocketmq-slf4j|rocketmq-logback|logback|fastjson|commons-codec" | tr "\n" :); java -cp target/test-classes:target/classes:$CP org.junit.runner.JUnitCore org.apache.rocketmq.common.UtilAllTest 2>&1 | grep -vE "^\s+at " | tail -15
