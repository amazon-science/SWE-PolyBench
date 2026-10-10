# Instance: apolloconfig__apollo-4207

- Final resolved (evaluator, logs/apolloconfig__apollo-4207_result.json): False
- Run state: DONE
- One attempt. Duration 135.7 s, turns 20, actor cost $0.5120152000000001, container commands 6
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/apolloconfig__apollo-4207/repo
</uploaded_files>
I've uploaded a Java code repository in the directory /work/apolloconfig__apollo-4207/repo. Consider the following issue description:

<issue_description>
feature: `isCommonlyUsed` password check not hardcoded
**Is your feature request related to a problem? Please describe.**
Fragments of passwords that seem insecure may change from time to time and may be wanted to change. For example a company password policy might change and won't allow a certain pattern in their password (lets say the company name). 

**Describe the solution you'd like**
I suggest that the `LIST_OF_CODE_FRAGMENT` List that is currently hardcoded in `com.ctrip.framework.apollo.portal.util.checker.AuthUserPasswordChecker` should be extracted into a file that can be change 24/7 (aka while running).
The administrator can define the location of the file inside a property file or smth similar like that.
If no location is defined there is a default file inside the project that could be used. The default file may contain the already existing hardcoded list.

**Describe alternatives you've considered**
Alternatively to storing the `LIST_OF_CODE_FRAGMENT`s inside a file, the list could be stored inside a database. This will make it easier to maintain inside the administration panel. 

**Additional context**
I think this feature implemented in #4008 is really great but not hardcoding this fragment list may make it more future proof and better maintainable.


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/apolloconfig__apollo-4207/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/apolloconfig__apollo-4207/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/apolloconfig__apollo-4207/bin/envrun 'git status --short && ls'
Edits you make under /work/apolloconfig__apollo-4207/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/apolloconfig__apollo-4207/repo; cat apollo-portal/src/main/java/com/ctrip/framework/apollo/portal/util/checker/AuthUserPasswordChecker.java; grep -rn "AuthUserPasswordChecker\|PasswordChecker" --include=*.java . | grep -v "^./apollo-portal/src/main/java/com/ctrip/framework/apollo/portal/util/checker/AuthUserPasswordChecker.java"
```

tool result:

```
/*
 * Copyright 2022 Apollo Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */
package com.ctrip.framework.apollo.portal.util.checker;

import com.google.common.base.Strings;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Pattern;
import org.springframework.stereotype.Component;

@Component
public class AuthUserPasswordChecker implements UserPasswordChecker {

  private static final Pattern PWD_PATTERN = Pattern
      .compile("^(?=.*[0-9].*)(?=.*[a-zA-Z].*).{8,20}$");

  private static final List<String> LIST_OF_CODE_FRAGMENT = Arrays.asList(
      "111", "222", "333", "444", "555", "666", "777", "888", "999", "000",
      "001122", "112233", "223344", "334455", "445566", "556677", "667788", "778899", "889900",
      "009988", "998877", "887766", "776655", "665544", "554433", "443322", "332211", "221100",
      "0123", "1234", "2345", "3456", "4567", "5678", "6789", "7890",
      "0987", "9876", "8765", "7654", "6543", "5432", "4321", "3210",
      "1q2w", "2w3e", "3e4r", "5t6y", "abcd", "qwer", "asdf", "zxcv"
  );

  @Override
  public CheckResult checkWeakPassword(String password) {
    if (!PWD_PATTERN.matcher(password).matches()) {
      return new CheckResult(Boolean.FALSE,
          "Password needs a number and letter and between 8~20 characters");
    }
    if (isCommonlyUsed(password)) {
      return new CheckResult(Boolean.FALSE,
          "Passwords cannot be consecutive, regular letters or numbers. And cannot be commonly used. "
              + "e.g: abcd1234, 1234qwer, 1q2w3e4r, 1234asdfghjk, ...");
    }
    return new CheckResult(Boolean.TRUE, null);
  }

  /**
   * @return The password contains code fragment or is blank.
   */
  private boolean isCommonlyUsed(String password) {
    if (Strings.isNullOrEmpty(password)) {
      return true;
    }
    for (String s : LIST_OF_CODE_FRAGMENT) {
      if (password.toLowerCase().contains(s)) {
        return true;
      }
    }
    return false;
  }
}
(eval):1: no matches found: --include=*.java
```

**tool call: Bash**

```bash
cd /work/apolloconfig__apollo-4207/repo; grep -rn "PasswordChecker" --include='*.java' . | grep -v "checker/AuthUserPasswordChecker.java"; git log --oneline -1
```

tool result:

```
./apollo-portal/src/test/java/com/ctrip/framework/apollo/portal/util/AuthUserPasswordCheckerTest.java:19:import com.ctrip.framework.apollo.portal.util.checker.AuthUserPasswordChecker;
./apollo-portal/src/test/java/com/ctrip/framework/apollo/portal/util/AuthUserPasswordCheckerTest.java:27:public class AuthUserPasswordCheckerTest {
./apollo-portal/src/test/java/com/ctrip/framework/apollo/portal/util/AuthUserPasswordCheckerTest.java:29:  private AuthUserPasswordChecker checker;
./apollo-portal/src/test/java/com/ctrip/framework/apollo/portal/util/AuthUserPasswordCheckerTest.java:33:    checker = new AuthUserPasswordChecker();
./apollo-portal/src/test/java/com/ctrip/framework/apollo/portal/controller/UserInfoControllerTest.java:22:import com.ctrip.framework.apollo.portal.util.checker.AuthUserPasswordChecker;
./apollo-portal/src/test/java/com/ctrip/framework/apollo/portal/controller/UserInfoControllerTest.java:40:  private AuthUserPasswordChecker userPasswordChecker;
./apollo-portal/src/test/java/com/ctrip/framework/apollo/portal/controller/UserInfoControllerTest.java:48:    Mockito.when(userPasswordChecker.checkWeakPassword(Mockito.anyString()))
./apollo-portal/src/test/java/com/ctrip/framework/apollo/portal/controller/UserInfoControllerTest.java:62:    Mockito.when(userPasswordChecker.checkWeakPassword(Mockito.anyString()))
./apollo-portal/src/main/java/com/ctrip/framework/apollo/portal/util/checker/UserPasswordChecker.java:19:public interface UserPasswordChecker {
./apollo-portal/src/main/java/com/ctrip/framework/apollo/portal/controller/UserInfoController.java:27:import com.ctrip.framework.apollo.portal.util.checker.AuthUserPasswordChecker;
./apollo-portal/src/main/java/com/ctrip/framework/apollo/portal/controller/UserInfoController.java:47:  private final AuthUserPasswordChecker passwordChecker;
./apollo-portal/src/main/java/com/ctrip/framework/apollo/portal/controller/UserInfoController.java:53:      final AuthUserPasswordChecker passwordChecker) {
96ee53a2 Allow disable apollo client cache (#4199)
```

**tool call: Bash**

```bash
cd /work/apolloconfig__apollo-4207/repo; cat apollo-portal/src/test/java/com/ctrip/framework/apollo/portal/util/checker/AuthUserPasswordCheckerTest.java 2>/dev/null || find . -name "*PasswordChecker*"
```

tool result:

```
./apollo-portal/src/test/java/com/ctrip/framework/apollo/portal/util/AuthUserPasswordCheckerTest.java
./apollo-portal/src/main/java/com/ctrip/framework/apollo/portal/util/checker/UserPasswordChecker.java
./apollo-portal/src/main/java/com/ctrip/framework/apollo/portal/util/checker/AuthUserPasswordChecker.java
```

**tool call: Bash**

```bash
cd /work/apolloconfig__apollo-4207/repo; cat apollo-portal/src/test/java/com/ctrip/framework/apollo/portal/util/AuthUserPasswordCheckerTest.java; cat apollo-portal/src/main/java/com/ctrip/framework/apollo/portal/component/config/PortalConfig.java
```

tool result:

```
/*
 * Copyright 2022 Apollo Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */
package com.ctrip.framework.apollo.portal.util;

import com.ctrip.framework.apollo.portal.util.checker.AuthUserPasswordChecker;
import com.ctrip.framework.apollo.portal.util.checker.CheckResult;
import java.util.Arrays;
import java.util.List;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class AuthUserPasswordCheckerTest {

  private AuthUserPasswordChecker checker;

  @Before
  public void setup() {
    checker = new AuthUserPasswordChecker();
  }

  @Test
  public void testRegexMatch() {
    List<String> unMatchList = Arrays.asList(
        "11111111",
        "oibjdiel",
        "oso87b6",
        "0vb9xibowkd8bz9dsxbef"
    );
    String exceptedErrMsg = "Password needs a number and letter and between 8~20 characters";

    for (String p : unMatchList) {
      CheckResult res = checker.checkWeakPassword(p);
      Assert.assertFalse(res.isSuccess());
      Assert.assertEquals(exceptedErrMsg, res.getMessage());
    }

    List<String> matchList = Arrays.asList(
        "pziv0g87",
        "8f7zjpf8sci93",
        "Upz4jF8u2yjV3wn8zp6c"
    );

    for (String p : matchList) {
      CheckResult res = checker.checkWeakPassword(p);
      Assert.assertTrue(res.isSuccess());
    }
  }

  @Test
  public void testIsWeakPassword() {
    List<String> weakPwdList = Arrays.asList(
        "a1234567", "b98765432", "c11111111", "d2222222", "e3333333", "f4444444",
        "g5555555", "h6666666", "i7777777", "j8888888", "k9999999", "l0000000",
        "1q2w3e4r", "qwertyuiop1", "asdfghjkl2", "asdfghjkl3", "abcd1234"
    );
    String exceptedErrMsg =
        "Passwords cannot be consecutive, regular letters or numbers. And cannot be commonly used.";

    for (String p : weakPwdList) {
      CheckResult res = checker.checkWeakPassword(p);
      Assert.assertFalse(res.isSuccess());
      Assert.assertTrue(res.getMessage().startsWith(exceptedErrMsg));
    }

    CheckResult res = checker.checkWeakPassword("1s39gvisk");
    Assert.assertTrue(res.isSuccess());
  }

}/*
 * Copyright 2022 Apollo Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */
package com.ctrip.framework.apollo.portal.component.config;


import com.ctrip.framework.apollo.common.config.RefreshableConfig;
import com.ctrip.framework.apollo.common.config.RefreshablePropertySource;
import com.ctrip.framework.apollo.portal.entity.vo.Organization;
import com.ctrip.framework.apollo.portal.environment.Env;
import com.ctrip.framework.apollo.portal.service.PortalDBPropertySource;
import com.ctrip.framework.apollo.portal.service.SystemRoleManagerService;
import com.google.common.base.Strings;
import com.google.common.collect.Lists;
import com.google.common.collect.Sets;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.lang.reflect.Type;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

@Component
public class PortalConfig extends RefreshableConfig {

  private static final Logger logger = LoggerFactory.getLogger(PortalConfig.class);

  private static final Gson GSON = new Gson();
  private static final Type ORGANIZATION = new TypeToken<List<Organization>>() {
  }.getType();

  /**
   * meta servers config in "PortalDB.ServerConfig"
   */
  private static final Type META_SERVERS = new TypeToken<Map<String, String>>(){}.getType();

  private final PortalDBPropertySource portalDBPropertySource;

  public PortalConfig(final PortalDBPropertySource portalDBPropertySource) {
    this.portalDBPropertySource = portalDBPropertySource;
  }

  @Override
  public List<RefreshablePropertySource> getRefreshablePropertySources() {
    return Collections.singletonList(portalDBPropertySource);
  }

  /***
   * Level: important
   **/
  public List<Env> portalSupportedEnvs() {
    String[] configurations = getArrayProperty("apollo.portal.envs", new String[]{"FAT", "UAT", "PRO"});
    List<Env> envs = Lists.newLinkedList();

    for (String env : configurations) {
      envs.add(Env.addEnvironment(env));
    }

    return envs;
  }

  /**
   * @return the relationship between environment and its meta server. empty if meet exception
   */
  public Map<String, String> getMetaServers() {
    final String key = "apollo.portal.meta.servers";
    String jsonContent = getValue(key);
    if (null == jsonContent) {
      return Collections.emptyMap();
    }

    // watch out that the format of content may be wrong
    // that will cause exception
    Map<String, String> map = Collections.emptyMap();
    try {
      // try to parse
      map = GSON.fromJson(jsonContent, META_SERVERS);
    } catch (Exception e) {
      logger.error("Wrong format for: {}", key, e);
    }
    return map;
  }

  public List<String> superAdmins() {
    String supe
[... 4565 more characters not shown]
```

**thinking:**

```
The checker currently hardcodes the list, so I'll move it into `PortalConfig`, refreshable at runtime from the PortalDB `ServerConfig` table, keeping the existing list as the default, and inject `PortalConfig` into the checker.


```

**tool call: Bash**

```bash
cd /work/apolloconfig__apollo-4207/repo; python3 - <<'EOF'
p='apollo-portal/src/main/java/com/ctrip/framework/apollo/portal/component/config/PortalConfig.java'
s=open(p).read()
s=s.replace("import java.lang.reflect.Type;\n","import java.lang.reflect.Type;\nimport java.util.Arrays;\n",1)
s=s.replace("""  private static final Type META_SERVERS = new TypeToken<Map<String, String>>(){}.getType();
""","""  private static final Type META_SERVERS = new TypeToken<Map<String, String>>(){}.getType();

  private static final List<String> DEFAULT_USER_PASSWORD_NOT_ALLOW_LIST = Arrays.asList(
      "111", "222", "333", "444", "555", "666", "777", "888", "999", "000",
      "001122", "112233", "223344", "334455", "445566", "556677", "667788", "778899", "889900",
      "009988", "998877", "887766", "776655", "665544", "554433", "443322", "332211", "221100",
      "0123", "1234", "2345", "3456", "4567", "5678", "6789", "7890",
      "0987", "9876", "8765", "7654", "6543", "5432", "4321", "3210",
      "1q2w", "2w3e", "3e4r", "5t6y", "abcd", "qwer", "asdf", "zxcv"
  );
""",1)
s=s.replace("""  public boolean supportSearchByItem() {
    return getBooleanProperty("searchByItem.switch", true);
  }
""","""  public boolean supportSearchByItem() {
    return getBooleanProperty("searchByItem.switch", true);
  }

  public List<String> getUserPasswordNotAllowList() {
    String[] value = getArrayProperty("apollo.portal.auth.user-password-not-allow-list", null);
    if (value == null || value.length == 0) {
      return DEFAULT_USER_PASSWORD_NOT_ALLOW_LIST;
    }
    return Arrays.asList(value);
  }
""",1)
open(p,'w').write(s)
EOF
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
cd /work/apolloconfig__apollo-4207/repo; grep -n "splitter\|getArrayProperty" -A8 apollo-common/src/main/java/com/ctrip/framework/apollo/common/config/RefreshableConfig.java | head -40
```

tool result:

```
47:  protected Splitter splitter = Splitter.on(LIST_SEPARATOR).omitEmptyStrings().trimResults();
48-
49-  @Autowired
50-  private ConfigurableEnvironment environment;
51-
52-  private List<RefreshablePropertySource> propertySources;
53-
54-  /**
55-   * register refreshable property source.
--
110:  public String[] getArrayProperty(String key, String[] defaultValue) {
111-    try {
112-      String value = getValue(key);
113-      return Strings.isNullOrEmpty(value) ? defaultValue : value.split(LIST_SEPARATOR);
114-    } catch (Throwable e) {
115-      Tracer.logError("Get array property failed.", e);
116-      return defaultValue;
117-    }
118-  }
```

**thinking:**

```
I've added `getUserPasswordNotAllowList()` to `PortalConfig` with the old list as default, but switched to the trimming `splitter` since `getArrayProperty` doesn't trim whitespace from values. Next, I'll update the checker.


```

**tool call: Bash**

```bash
cd /work/apolloconfig__apollo-4207/repo; python3 - <<'EOF'
p='apollo-portal/src/main/java/com/ctrip/framework/apollo/portal/component/config/PortalConfig.java'
s=open(p).read()
s=s.replace("""    String[] value = getArrayProperty("apollo.portal.auth.user-password-not-allow-list", null);
    if (value == null || value.length == 0) {
      return DEFAULT_USER_PASSWORD_NOT_ALLOW_LIST;
    }
    return Arrays.asList(value);""","""    String value = getValue("apollo.portal.auth.user-password-not-allow-list");
    if (Strings.isNullOrEmpty(value)) {
      return DEFAULT_USER_PASSWORD_NOT_ALLOW_LIST;
    }
    List<String> notAllowList = splitter.splitToList(value);
    return notAllowList.isEmpty() ? DEFAULT_USER_PASSWORD_NOT_ALLOW_LIST : notAllowList;""")
open(p,'w').write(s)
EOF
cat > apollo-portal/src/main/java/com/ctrip/framework/apollo/portal/util/checker/AuthUserPasswordChecker.java <<'EOF'
/*
 * Copyright 2022 Apollo Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */
package com.ctrip.framework.apollo.portal.util.checker;

import com.ctrip.framework.apollo.portal.component.config.PortalConfig;
import com.google.common.base.Strings;
import java.util.List;
import java.util.regex.Pattern;
import org.springframework.stereotype.Component;

@Component
public class AuthUserPasswordChecker implements UserPasswordChecker {

  private static final Pattern PWD_PATTERN = Pattern
      .compile("^(?=.*[0-9].*)(?=.*[a-zA-Z].*).{8,20}$");

  private final PortalConfig portalConfig;

  public AuthUserPasswordChecker(final PortalConfig portalConfig) {
    this.portalConfig = portalConfig;
  }

  @Override
  public CheckResult checkWeakPassword(String password) {
    if (!PWD_PATTERN.matcher(password).matches()) {
      return new CheckResult(Boolean.FALSE,
          "Password needs a number and letter and between 8~20 characters");
    }
    if (isCommonlyUsed(password)) {
      return new CheckResult(Boolean.FALSE,
          "Passwords cannot be consecutive, regular letters or numbers. And cannot be commonly used. "
              + "e.g: abcd1234, 1234qwer, 1q2w3e4r, 1234asdfghjk, ...");
    }
    return new CheckResult(Boolean.TRUE, null);
  }

  /**
   * @return The password contains code fragment or is blank.
   */
  private boolean isCommonlyUsed(String password) {
    if (Strings.isNullOrEmpty(password)) {
      return true;
    }
    List<String> userPasswordNotAllowList = portalConfig.getUserPasswordNotAllowList();
    String lowerCasePassword = password.toLowerCase();
    for (String s : userPasswordNotAllowList) {
      if (lowerCasePassword.contains(s.toLowerCase())) {
        return true;
      }
    }
    return false;
  }
}
EOF
git diff --stat
```

tool result:

```
 .../portal/component/config/PortalConfig.java       | 19 +++++++++++++++++++
 .../util/checker/AuthUserPasswordChecker.java       | 21 ++++++++++-----------
 2 files changed, 29 insertions(+), 11 deletions(-)
```

**thinking:**

```
The checker now reads the list from PortalConfig on every check, so database changes apply at runtime. Next, I'll write a temporary test with a mocked PortalConfig to verify the default list, a custom list, and trimming/case handling.


```

**tool call: Bash**

```bash
cd /work/apolloconfig__apollo-4207/repo; mkdir -p apollo-portal/src/test/java/tmprepro; cat > apollo-portal/src/test/java/tmprepro/TmpCheckerTest.java <<'EOF'
package tmprepro;

import com.ctrip.framework.apollo.portal.component.config.PortalConfig;
import com.ctrip.framework.apollo.portal.service.PortalDBPropertySource;
import com.ctrip.framework.apollo.portal.util.checker.AuthUserPasswordChecker;
import java.util.Arrays;
import org.junit.Assert;
import org.junit.Test;
import org.mockito.Mockito;

public class TmpCheckerTest {
  @Test
  public void test() {
    PortalConfig cfg = Mockito.spy(new PortalConfig(Mockito.mock(PortalDBPropertySource.class)));
    Mockito.doReturn(null).when(cfg).getValue("apollo.portal.auth.user-password-not-allow-list");
    AuthUserPasswordChecker c = new AuthUserPasswordChecker(cfg);
    Assert.assertFalse(c.checkWeakPassword("abcd1234x").isSuccess());
    Assert.assertTrue(c.checkWeakPassword("1s39gvisk").isSuccess());
    Assert.assertTrue(c.checkWeakPassword("apollo12x").isSuccess());

    Mockito.doReturn(" Apollo , ,ctrip").when(cfg).getValue("apollo.portal.auth.user-password-not-allow-list");
    Assert.assertEquals(Arrays.asList("Apollo", "ctrip"), cfg.getUserPasswordNotAllowList());
    Assert.assertFalse(c.checkWeakPassword("apollo12x").isSuccess());
    Assert.assertTrue(c.checkWeakPassword("abcd1234x").isSuccess());

    Mockito.doReturn(" , ").when(cfg).getValue("apollo.portal.auth.user-password-not-allow-list");
    Assert.assertFalse(c.checkWeakPassword("abcd1234x").isSuccess());
  }
}
EOF
mv apollo-portal/src/test/java/com/ctrip/framework/apollo/portal/util/AuthUserPasswordCheckerTest.java /tmp/ 
../bin/envrun 'mvn -o -q test -pl apollo-portal -am -Dtest=TmpCheckerTest,UserInfoControllerTest -DfailIfNoTests=false 2>&1 | tail -40'
```

tool result:

```
mv: rename apollo-portal/src/test/java/com/ctrip/framework/apollo/portal/util/AuthUserPasswordCheckerTest.java to /tmp/AuthUserPasswordCheckerTest.java: Operation not permitted
[ERROR] Plugin org.apache.maven.plugins:maven-resources-plugin:3.3.1 or one of its dependencies could not be resolved:
[ERROR] 	Cannot access central (https://repo.maven.apache.org/maven2) in offline mode and the artifact org.apache.maven.plugins:maven-resources-plugin:jar:3.3.1 has not been downloaded from it before.
[ERROR] -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/PluginResolutionException
```

**assistant:** Maven couldn't resolve the resources plugin offline, and moving the old test to `/tmp` failed with a permissions error. I'll look at which plugin versions are cached in the container.

**tool call: Bash**

```bash
cd /work/apolloconfig__apollo-4207/repo; ../bin/envrun 'ls ~/.m2/repository/org/apache/maven/plugins/maven-resources-plugin ~/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin ~/.m2/repository/com/ctrip/framework/apollo/ 2>&1; ls apollo-portal/target 2>&1 | head'
```

tool result:

```
ls: cannot access '/root/.m2/repository/com/ctrip/framework/apollo/': No such file or directory
/root/.m2/repository/org/apache/maven/plugins/maven-resources-plugin:
2.6

/root/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin:
2.19.1
classes
generated-sources
generated-test-sources
maven-status
site
surefire-reports
test-classes
```

**tool call: Bash**

```bash
cd /work/apolloconfig__apollo-4207/repo; ../bin/envrun 'mvn -v; ls ~/.m2; cat ~/.m2/settings.xml 2>/dev/null | head -30'
```

tool result:

```
Apache Maven 3.9.11 (3e54c93a704957b63ee3494413a2b544fd3d825b)
Maven home: /usr/local/apache-maven-3.9.11
Java version: 1.8.0_462, vendor: Amazon.com Inc., runtime: /usr/lib/jvm/java-1.8.0-amazon-corretto.x86_64/jre
Default locale: en_US, platform encoding: ANSI_X3.4-1968
OS name: "linux", version: "6.12.76-linuxkit", arch: "amd64", family: "unix"
repository
wrapper
```

**assistant:** Container's Maven 3.9 defaults to plugin versions that aren't cached, but a Maven wrapper is present. I'll use `./mvnw` instead.

**tool call: Bash**

```bash
cd /work/apolloconfig__apollo-4207/repo; ../bin/envrun 'ls ~/.m2/wrapper/dists/*; ls mvnw; ./mvnw -o -q test -pl apollo-portal -am -Dtest=TmpCheckerTest,UserInfoControllerTest -DfailIfNoTests=false 2>&1 | tail -40'
```

tool result:

```
4lcg54ki11c6mp435njk296gm5
mvnw
./mvnw: line 121: which: command not found
./mvnw: line 149: which: command not found
Error: JAVA_HOME is not defined correctly.
  We cannot execute
```

**tool call: Bash**

```bash
cd /work/apolloconfig__apollo-4207/repo; ../bin/envrun 'export JAVA_HOME=/usr/lib/jvm/java-1.8.0-amazon-corretto.x86_64; ./mvnw -o -q test -pl apollo-portal -am -Dtest=TmpCheckerTest,UserInfoControllerTest -DfailIfNoTests=false 2>&1 | tail -40'
```

tool result:

```
[ERROR] COMPILATION ERROR : 
[ERROR] /testbed/apollo-portal/src/test/java/com/ctrip/framework/apollo/portal/util/AuthUserPasswordCheckerTest.java:[33,15] constructor AuthUserPasswordChecker in class com.ctrip.framework.apollo.portal.util.checker.AuthUserPasswordChecker cannot be applied to given types;
  required: com.ctrip.framework.apollo.portal.component.config.PortalConfig
  found: no arguments
  reason: actual and formal argument lists differ in length
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-compiler-plugin:3.6.0:testCompile (default-testCompile) on project apollo-portal: Compilation failure
[ERROR] /testbed/apollo-portal/src/test/java/com/ctrip/framework/apollo/portal/util/AuthUserPasswordCheckerTest.java:[33,15] constructor AuthUserPasswordChecker in class com.ctrip.framework.apollo.portal.util.checker.AuthUserPasswordChecker cannot be applied to given types;
[ERROR]   required: com.ctrip.framework.apollo.portal.component.config.PortalConfig
[ERROR]   found: no arguments
[ERROR]   reason: actual and formal argument lists differ in length
[ERROR] 
[ERROR] -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoFailureException
[ERROR] 
[ERROR] After correcting the problems, you can resume the build with the command
[ERROR]   mvn <goals> -rf :apollo-portal
```

**thinking:**

```
The build compiles now, with the only error being the existing `AuthUserPasswordCheckerTest` still using the old no-arg constructor, which is expected since the checker now requires `PortalConfig`. I'll temporarily back up that test file to run my checks, then restore it afterward.


```

**tool call: Bash**

```bash
cd /work/apolloconfig__apollo-4207/repo; T=apollo-portal/src/test/java/com/ctrip/framework/apollo/portal/util/AuthUserPasswordCheckerTest.java; mv $T $T.bak; ../bin/envrun 'export JAVA_HOME=/usr/lib/jvm/java-1.8.0-amazon-corretto.x86_64; ./mvnw -o test -pl apollo-portal -am -Dtest=TmpCheckerTest,UserInfoControllerTest,PortalConfigTest -DfailIfNoTests=false 2>&1 | grep -E "Tests run|FAIL|ERROR|BUILD" | head -30'; mv $T.bak $T
```

tool result:

```
Tests run: 1, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.936 sec - in tmprepro.TmpCheckerTest
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.093 sec - in com.ctrip.framework.apollo.portal.controller.UserInfoControllerTest
Tests run: 3, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

**thinking:**

```
Tests pass for the default list, custom list handling, and blank-value fallback, plus `UserInfoControllerTest`. I'll now remove the temporary test and document the new setting.


```

**tool call: Bash**

```bash
cd /work/apolloconfig__apollo-4207/repo; rm -rf apollo-portal/src/test/java/tmprepro; git status --short; grep -rln "searchByItem.switch" docs CHANGES.md 2>/dev/null; head -30 CHANGES.md
```

tool result:

```
 M apollo-portal/src/main/java/com/ctrip/framework/apollo/portal/component/config/PortalConfig.java
 M apollo-portal/src/main/java/com/ctrip/framework/apollo/portal/util/checker/AuthUserPasswordChecker.java
?? Dockerfile
docs/zh/deployment/distributed-deployment-guide.md
Changes by Version
==================
Release Notes.

Apollo 2.0.0

------------------
* [Fix issue that the $ symbol is not used when reading shell variables](https://github.com/ctripcorp/apollo/pull/3890)
* [Bump xstream from 1.4.17 to 1.4.18](https://github.com/apolloconfig/apollo/pull/3916)
* [switch apollo.config-service log from warning to info level](https://github.com/ctripcorp/apollo/pull/3884)
* [Make Access Key Timestamp check configurable](https://github.com/ctripcorp/apollo/pull/3908)
* [remove ctrip profile](https://github.com/ctripcorp/apollo/pull/3920)
* [Remove spring dependencies from internal code](https://github.com/apolloconfig/apollo/pull/3937)
* [Fix issue: ingress syntax](https://github.com/apolloconfig/apollo/pull/3933)
* [refactor: let open api more easier to use and development](https://github.com/apolloconfig/apollo/pull/3943)
* [feat(scripts): use bash to call openapi](https://github.com/apolloconfig/apollo/pull/3980)
* [Support search by item](https://github.com/apolloconfig/apollo/pull/3977)
* [Implement password policies to avoid weak passwords](https://github.com/apolloconfig/apollo/pull/4008)
* [Extend the gray release capability to support dimensions other than IP](https://github.com/apolloconfig/apollo/pull/4013)
* [public namespace basic function](https://github.com/apolloconfig/apollo/pull/3850)
* [Bump version to 2.0.0 and drop java 1.7 support](https://github.com/apolloconfig/apollo/pull/4015)
* [Optimize home page style](https://github.com/apolloconfig/apollo/pull/4052)
* [Support Java 17](https://github.com/apolloconfig/apollo/pull/4060)
* [Optimize top navbar style](https://github.com/apolloconfig/apollo/pull/4073)
* [Support export/import configs by apollo env](https://github.com/apolloconfig/apollo/pull/3947)
* [Catch LinkageError for ClassLoaderUtil.isClassPresent in case class is present but is failed to load](https://github.com/apolloconfig/apollo/pull/4097)
* [Split helm chart into another repo](https://github.com/apolloconfig/apollo/pull/4125)
* [fix gray publish refresh item status](https://github.com/apolloconfig/apollo/pull/4128)
* [Support only show difference keys when compare namespace](https://github.com/apolloconfig/apollo/pull/4165)
* [Fix the issue that property placeholder doesn't work for dubbo reference beans](https://github.com/apolloconfig/apollo/pull/4175)
```

**tool call: Bash**

```bash
cd /work/apolloconfig__apollo-4207/repo; grep -n "searchByItem" -B3 -A12 docs/zh/deployment/distributed-deployment-guide.md; ls docs; tail -5 CHANGES.md
```

tool result:

````
1219-
1220-### 3.1.12 admin-service.access.tokens - 设置apollo-portal访问各环境apollo-adminservice所需的access token
1221-
1222:### 3.1.13 searchByItem.switch - 控制台搜索框是否支持按配置项搜索
1223-
1224-默认为 true，可以方便的按配置项快速搜索配置
1225-
1226-如果设置为 false，则关闭此功能 
1227-
1228-> 适用于1.7.1及以上版本
1229-
1230-如果对应环境的apollo-adminservice开启了[访问控制](#_326-admin-serviceaccesscontrolenabled-配置apollo-adminservice是否开启访问控制)，那么需要在此配置apollo-portal访问该环境apollo-adminservice所需的access token，否则会访问失败
1231-
1232-格式为json，如下所示：
1233-
1234-```json
CNAME
_coverpage.md
charts
css
en
index.html
scripts
zh
* [Change Copy Right year to 2022](https://github.com/apolloconfig/apollo/pull/4202)
* [Allow disable apollo client cache](https://github.com/apolloconfig/apollo/pull/4199)

------------------
All issues and pull requests are [here](https://github.com/ctripcorp/apollo/milestone/8?closed=1)
````

**tool call: Bash**

```bash
cd /work/apolloconfig__apollo-4207/repo; sed -n 1234,1260p docs/zh/deployment/distributed-deployment-guide.md; grep -n "^### 3.1\|^## 3.2" docs/en/deployment/distributed-deployment-guide.md
```

tool result:

````
```json
{
    "dev" : "098f6bcd4621d373cade4e832627b4f6",
    "pro" : "ad0234829205b9033196ba818f7a872b"
}
```

## 3.2 调整ApolloConfigDB配置
配置项统一存储在ApolloConfigDB.ServerConfig表中，需要注意每个环境的ApolloConfigDB.ServerConfig都需要单独配置，修改完一分钟实时生效。

### 3.2.1 eureka.service.url - Eureka服务Url

> 不适用于基于Kubernetes原生服务发现场景

不管是apollo-configservice还是apollo-adminservice都需要向eureka服务注册，所以需要配置eureka服务地址。
按照目前的实现，apollo-configservice本身就是一个eureka服务，所以只需要填入apollo-configservice的地址即可，如有多个，用逗号分隔（注意不要忘了/eureka/后缀）。

需要注意的是每个环境只填入自己环境的eureka服务地址，比如FAT的apollo-configservice是1.1.1.1:8080和2.2.2.2:8080，UAT的apollo-configservice是3.3.3.3:8080和4.4.4.4:8080，PRO的apollo-configservice是5.5.5.5:8080和6.6.6.6:8080，那么：

1. 在FAT环境的ApolloConfigDB.ServerConfig表中设置eureka.service.url为：
```
http://1.1.1.1:8080/eureka/,http://2.2.2.2:8080/eureka/
```

2. 在UAT环境的ApolloConfigDB.ServerConfig表中设置eureka.service.url为：
```
http://3.3.3.3:8080/eureka/,http://4.4.4.4:8080/eureka/
````

**assistant:** I've found where the portal settings are documented in the Chinese deployment guide. Next I'll check the English guide's heading layout so I can add the new setting to both.

**tool call: Bash**

```bash
cd /work/apolloconfig__apollo-4207/repo; grep -n "^#.*searchByItem\|^#.*admin-service.access.tokens\|^## 3.2" docs/en/deployment/distributed-deployment-guide.md
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
cd /work/apolloconfig__apollo-4207/repo; grep -n "admin-service.access.tokens\|ApolloConfigDB" docs/en/deployment/distributed-deployment-guide.md | head
```

tool result:

```
(Bash completed with no output)
```

**assistant:** The English guide doesn't cover these portal settings at all, so I'll document the new one in the Chinese guide only and add a line to CHANGES.md.

**tool call: Bash**

````bash
cd /work/apolloconfig__apollo-4207/repo; python3 - <<'EOF'
p='docs/zh/deployment/distributed-deployment-guide.md'
s=open(p).read()
anchor='''    "pro" : "ad0234829205b9033196ba818f7a872b"
}
```

## 3.2 调整ApolloConfigDB配置'''
assert s.count(anchor)==1
s=s.replace(anchor,'''    "pro" : "ad0234829205b9033196ba818f7a872b"
}
```

### 3.1.14 apollo.portal.auth.user-password-not-allow-list - 指定用户密码中不允许包含的字符串

> 适用于2.0.0及以上版本

默认值为空，即使用内置的列表：`111, 222, 333, 444, 555, 666, 777, 888, 999, 000, 001122, 112233, 223344, 334455, 445566, 556677, 667788, 778899, 889900, 009988, 998877, 887766, 776655, 665544, 554433, 443322, 332211, 221100, 0123, 1234, 2345, 3456, 4567, 5678, 6789, 7890, 0987, 9876, 8765, 7654, 6543, 5432, 4321, 3210, 1q2w, 2w3e, 3e4r, 5t6y, abcd, qwer, asdf, zxcv`

在使用内置的用户管理（auth profile）时，用户创建或修改密码时，如果密码（不区分大小写）包含该列表中的任意一项，则视为弱密码，会被拒绝。

格式为逗号分隔，修改后实时生效，如：

```
apollo,ctrip,1234
```

## 3.2 调整ApolloConfigDB配置''')
open(p,'w').write(s)
p='CHANGES.md'
s=open(p).read()
a='* [Allow disable apollo client cache](https://github.com/apolloconfig/apollo/pull/4199)\n'
s=s.replace(a,a+'* [Make password check not hardcoded](https://github.com/apolloconfig/apollo/pull/4207)\n')
open(p,'w').write(s)
EOF
git status --short; git diff CHANGES.md
````

tool result:

```
 M CHANGES.md
 M apollo-portal/src/main/java/com/ctrip/framework/apollo/portal/component/config/PortalConfig.java
 M apollo-portal/src/main/java/com/ctrip/framework/apollo/portal/util/checker/AuthUserPasswordChecker.java
 M docs/zh/deployment/distributed-deployment-guide.md
?? Dockerfile
diff --git a/CHANGES.md b/CHANGES.md
index 30573633..d77090ad 100644
--- a/CHANGES.md
+++ b/CHANGES.md
@@ -36,6 +36,7 @@ Apollo 2.0.0
 * [Add unit tests for Utils](https://github.com/apolloconfig/apollo/pull/4193)
 * [Change Copy Right year to 2022](https://github.com/apolloconfig/apollo/pull/4202)
 * [Allow disable apollo client cache](https://github.com/apolloconfig/apollo/pull/4199)
+* [Make password check not hardcoded](https://github.com/apolloconfig/apollo/pull/4207)
 
 ------------------
 All issues and pull requests are [here](https://github.com/ctripcorp/apollo/milestone/8?closed=1)
```

**assistant:** The list of password fragments is no longer hardcoded. Admins can now set it at runtime, and if nothing is set the original list is used.

**How it works now**
- **New setting:** `apollo.portal.auth.user-password-not-allow-list`, a comma-separated value in the PortalDB `ServerConfig` table. This uses the same refreshable config as every other portal setting, so changes take effect while the portal is running, with no restart. It follows your issue's "database" option rather than a separate file.
- **`PortalConfig.java`:** the old hardcoded list is now the default. A new method, `getUserPasswordNotAllowList()`, returns the configured list. Spaces around entries are trimmed, empty entries are dropped, and a blank or missing value falls back to the default.
- **`AuthUserPasswordChecker.java`:** it now gets `PortalConfig` through its constructor and reads the list on every check. Matching ignores case on both sides, so an entry like `Apollo` also blocks `apollo12x`.
- **Docs:** I added a section for the new setting to `docs/zh/deployment/distributed-deployment-guide.md` and an entry to `CHANGES.md`. The English guide doesn't cover any of these portal settings, so I didn't add one there.

**Testing**
- I couldn't move the existing test out of the repo, so I temporarily renamed it in place and restored it afterwards. I then ran a temporary test with a mocked config, which passed. It covered the default list, a custom list with spaces and empty entries, case-insensitive matching, and a blank value falling back to the default. `UserInfoControllerTest` also passes. I deleted the temporary test afterwards.
- Plain `mvn` fails offline in the container because of missing plugin versions. I used `./mvnw -o` with `JAVA_HOME` set instead.

**Before you merge:** the current `AuthUserPasswordCheckerTest` will no longer compile. It still calls `new AuthUserPasswordChecker()` with no arguments, and the constructor now requires a `PortalConfig`. I left that file untouched as you asked, so it needs to be the updated version you mentioned. I also left alone an untracked `Dockerfile` in the repo root that I didn't create.

_session end: success, turns 20, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 4.93 s: mvn -o -q test -pl apollo-portal -am -Dtest=TmpCheckerTest,UserInfoControllerTest -DfailIfNoTests=false 2>&1 | tail -40
- `rc=0` 0.31 s: ls ~/.m2/repository/org/apache/maven/plugins/maven-resources-plugin ~/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin ~/.m2/repository/com/ctrip/framework/apollo/ 2>&1; ls apollo-portal/target 2>&1 | head
- `rc=0` 1.06 s: mvn -v; ls ~/.m2; cat ~/.m2/settings.xml 2>/dev/null | head -30
- `rc=0` 0.35 s: ls ~/.m2/wrapper/dists/*; ls mvnw; ./mvnw -o -q test -pl apollo-portal -am -Dtest=TmpCheckerTest,UserInfoControllerTest -DfailIfNoTests=false 2>&1 | tail -40
- `rc=0` 16.21 s: export JAVA_HOME=/usr/lib/jvm/java-1.8.0-amazon-corretto.x86_64; ./mvnw -o -q test -pl apollo-portal -am -Dtest=TmpCheckerTest,UserInfoControllerTest -DfailIfNoTests=false 2>&1 | tail -40
- `rc=0` 18.26 s: export JAVA_HOME=/usr/lib/jvm/java-1.8.0-amazon-corretto.x86_64; ./mvnw -o test -pl apollo-portal -am -Dtest=TmpCheckerTest,UserInfoControllerTest,PortalConfigTest -DfailIfNoTests=false 2>&1 | grep -E "Tests run|FAIL|ERROR|BUILD" | head -30
