# Instance: serverless__serverless-6534

- Final resolved (evaluator, logs/serverless__serverless-6534_result.json): False
- Run state: DONE
- One attempt. Duration 43.1 s, turns 9, actor cost $0.2296712, container commands 2
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/serverless__serverless-6534/repo
</uploaded_files>
I've uploaded a JavaScript code repository in the directory /work/serverless__serverless-6534/repo. Consider the following issue description:

<issue_description>
Wider `logs:CreateLogStream`/`logs:PutLogEvents` permissions in policy for Lambda functions with manual names (v1.45.1)
<!--
1. If you have a question and not a bug report please ask first at http://forum.serverless.com
2. Please check if an issue already exists. This bug may have already been documented
3. Check out and follow our Guidelines: https://github.com/serverless/serverless/blob/master/CONTRIBUTING.md
4. Fill out the whole template so we have a good overview on the issue
5. Do not remove any section of the template. If something is not applicable leave it empty but leave it in the Issue
6. Please follow the template, otherwise we'll have to ask you to update it
-->

# This is a Bug Report

## Description

* What went wrong?

   When a service contains only custom named functions, the policies for `logs:CreateLogStream` and `logs:PutLogEvents` created using v1.45.1 have a wider set of permissions than they previously did with v1.44.1.

   ### Resource access allowed when using v1.44.1

   * `logs:CreateLogStream`:
      * `arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/lambda/log-group-policy-custom-named-fn:*`
   * `logs:PutLogEvents`:
      * `arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/lambda/log-group-policy-custom-named-fn:*:*`


   ### Resource access allowed when using v1.45.1

   * `logs:CreateLogStream`:
      * `arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/lambda/log-group-policy-dev*:*`
      * `arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/lambda/log-group-policy-custom-named-fn:*`
   * `logs:PutLogEvents`:
      * `arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/lambda/log-group-policy-dev*:*:*`
      * `arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/lambda/log-group-policy-custom-named-fn:*:*`

* What did you expect should have happened?

   Based on the principle of least privilege, the additional permissions for `/aws/lambda/log-group-policy-dev*` should not have been added to the IAM policy.

* What was the config you used?

   Full source: [log-group-policy.zip](https://github.com/serverless/serverless/files/3296986/log-group-policy.zip)

   ```yaml
   service: log-group-policy

   provider:
      name: aws
      runtime: nodejs8.10

   functions:
      testFunction:
         name: ${self:service}-custom-named-fn
         handler: index.handler
   ```

   #### To compare output between v1.44.1 and v1.45.1

   ```
   unzip log-group-policy.zip
   cd log-group-policy
   echo '{}' > package.json
   npm i serverless@1.44.1
   ./node_modules/.bin/sls package
   cp .serverless/cloudformation-template-update-stack.json cf-update-stack-v1.44.1.json
   npm i serverless@1.45.1
   ./node_modules/.bin/sls package
   cp .serverless/cloudformation-template-update-stack.json cf-update-stack-v1.45.1.json
   diff cf-update-stack-v1.44.1.json cf-update-stack-v1.45.1.json
   ```

Similar or dependent issues:
* #6236 (PR #6240)
* #6212

## Additional Data

* ***Serverless Framework Version you're using***: 1.45.1
* ***Operating System***: macOS 10.14
* ***Stack Trace***: n/a
* ***Provider Error messages***: none


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/serverless__serverless-6534/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/serverless__serverless-6534/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/serverless__serverless-6534/bin/envrun 'git status --short && ls'
Edits you make under /work/serverless__serverless-6534/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
grep -rn "log-group" lib/plugins/aws/package/lib/mergeIamTemplates.js; cat lib/plugins/aws/package/lib/mergeIamTemplates.js | head -150
```

tool result:

```
lib/plugins/aws/package/lib/mergeIamTemplates.js:97:        `:log-group:${logGroupsPrefix}*:*`,
lib/plugins/aws/package/lib/mergeIamTemplates.js:103:        `:log-group:${logGroupsPrefix}*:*:*`,
lib/plugins/aws/package/lib/mergeIamTemplates.js:120:          `:log-group:${customFunctionNamelogGroupsPrefix}:*`,
lib/plugins/aws/package/lib/mergeIamTemplates.js:126:          `:log-group:${customFunctionNamelogGroupsPrefix}:*:*`,
'use strict';

const _ = require('lodash');
const BbPromise = require('bluebird');
const path = require('path');

module.exports = {
  mergeIamTemplates() {
    this.validateStatements(this.serverless.service.provider.iamRoleStatements);
    this.validateManagedPolicies(this.serverless.service.provider.iamManagedPolicies);
    return this.merge();
  },

  merge() {
    // resolve early if no functions are provided
    if (!this.serverless.service.getAllFunctions().length) {
      return BbPromise.resolve();
    }

    // create log group resources
    this.serverless.service.getAllFunctions().forEach(functionName => {
      const functionObject = this.serverless.service.getFunction(functionName);
      const logGroupLogicalId = this.provider.naming.getLogGroupLogicalId(functionName);
      const newLogGroup = {
        [logGroupLogicalId]: {
          Type: 'AWS::Logs::LogGroup',
          Properties: {
            LogGroupName: this.provider.naming.getLogGroupName(functionObject.name),
          },
        },
      };

      if (_.has(this.serverless.service.provider, 'logRetentionInDays')) {
        const rawRetentionInDays = this.serverless.service.provider.logRetentionInDays;
        const retentionInDays = parseInt(rawRetentionInDays, 10);
        if (_.isInteger(retentionInDays) && retentionInDays > 0) {
          newLogGroup[logGroupLogicalId].Properties.RetentionInDays = retentionInDays;
        } else {
          const errorMessage = `logRetentionInDays should be an integer over 0 but ${rawRetentionInDays}`;
          throw new this.serverless.classes.Error(errorMessage);
        }
      }

      _.merge(
        this.serverless.service.provider.compiledCloudFormationTemplate.Resources,
        newLogGroup
      );
    });

    // resolve early if provider level role is provided
    if ('role' in this.serverless.service.provider) {
      return BbPromise.resolve();
    }

    // resolve early if all functions contain a custom role
    const customRolesProvided = [];
    this.serverless.service.getAllFunctions().forEach(functionName => {
      const functionObject = this.serverless.service.getFunction(functionName);
      customRolesProvided.push('role' in functionObject);
    });
    if (_.isEqual(_.uniq(customRolesProvided), [true])) {
      return BbPromise.resolve();
    }

    // merge in the iamRoleLambdaTemplate
    const iamRoleLambdaExecutionTemplate = this.serverless.utils.readFileSync(
      path.join(
        this.serverless.config.serverlessPath,
        'plugins',
        'aws',
        'package',
        'lib',
        'iam-role-lambda-execution-template.json'
      )
    );
    iamRoleLambdaExecutionTemplate.Properties.Path = this.provider.naming.getRolePath();
    iamRoleLambdaExecutionTemplate.Properties.RoleName = this.provider.naming.getRoleName();
    iamRoleLambdaExecutionTemplate.Properties.Policies[0].PolicyName = this.provider.naming.getPolicyName();

    _.merge(this.serverless.service.provider.compiledCloudFormationTemplate.Resources, {
      [this.provider.naming.getRoleLogicalId()]: iamRoleLambdaExecutionTemplate,
    });

    const canonicalFunctionNamePrefix = `${
      this.provider.serverless.service.service
    }-${this.provider.getStage()}`;
    const logGroupsPrefix = this.provider.naming.getLogGroupName(canonicalFunctionNamePrefix);

    const policyDocumentStatements = this.serverless.service.provider.compiledCloudFormationTemplate
      .Resources[this.provider.naming.getRoleLogicalId()].Properties.Policies[0].PolicyDocument
      .Statement;

    // Ensure general polices for functions with default name resolution
    policyDocumentStatements[0].Resource.push({
      'Fn::Sub':
        'arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}' +
        `:log-group:${logGroupsPrefix}*:*`,
    });

    policyDocumentStatements[1].Resource.push({
      'Fn::Sub':
        'arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}' +
        `:log-group:${logGroupsPrefix}*:*:*`,
    });

    // Ensure policies for functions with custom name resolution
    this.serverless.service.getAllFunctions().forEach(functionName => {
      const { name: resolvedFunctionName } = this.serverless.service.getFunction(functionName);
      if (!resolvedFunctionName || resolvedFunctionName.startsWith(canonicalFunctionNamePrefix)) {
        return;
      }

      const customFunctionNamelogGroupsPrefix = this.provider.naming.getLogGroupName(
        resolvedFunctionName
      );

      policyDocumentStatements[0].Resource.push({
        'Fn::Sub':
          'arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}' +
          `:log-group:${customFunctionNamelogGroupsPrefix}:*`,
      });

      policyDocumentStatements[1].Resource.push({
        'Fn::Sub':
          'arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}' +
          `:log-group:${customFunctionNamelogGroupsPrefix}:*:*`,
      });
    });

    if (this.serverless.service.provider.iamRoleStatements) {
      // add custom iam role statements
      this.serverless.service.provider.compiledCloudFormationTemplate.Resources[
        this.provider.naming.getRoleLogicalId()
      ].Properties.Policies[0].PolicyDocument.Statement = policyDocumentStatements.concat(
        this.serverless.service.provider.iamRoleStatements
      );
    }

    if (this.serverless.service.provider.iamManagedPolicies) {
      // add iam managed policies
      const iamManagedPolicies = this.serverless.service.provider.iamManagedPolicies;
      if (iamManagedPolicies.length > 0) {
        this
[... 307 more characters not shown]
```

**tool call: Bash**

```bash
grep -n "custom\|canonical\|log-group" lib/plugins/aws/package/lib/mergeIamTemplates.test.js | head -50
```

tool result:

```
52:      const canonicalFunctionsPrefix = `${
94:                          `log-group:/aws/lambda/${canonicalFunctionsPrefix}*:*`,
105:                          `log-group:/aws/lambda/${canonicalFunctionsPrefix}*:*:*`,
130:  it('should ensure IAM policies for custom named functions', () => {
131:    const customFunctionName = 'foo-bar';
134:        name: customFunctionName,
142:      const canonicalFunctionsPrefix = `${
184:                          `log-group:/aws/lambda/${canonicalFunctionsPrefix}*:*`,
189:                          `log-group:/aws/lambda/${customFunctionName}:*`,
200:                          `log-group:/aws/lambda/${canonicalFunctionsPrefix}*:*:*`,
205:                          `log-group:/aws/lambda/${customFunctionName}:*:*`,
231:  it('should add custom IAM policy statements', () => {
299:  it('should throw error if custom IAM policy statements is not an array', () => {
314:  it('should throw error if a custom IAM policy statement does not have an Effect field', () => {
327:  it('should throw error if a custom IAM policy statement does not have an Action field', () => {
340:  it('should throw error if a custom IAM policy statement does not have a Resource field', () => {
353:  it('should throw an error describing all problematics custom IAM policy statements', () => {
433:  it('should add a CloudWatch LogGroup resource if all functions use custom roles', () => {
```

**tool call: Bash**

```bash
sed -n 20,60p lib/plugins/aws/package/lib/mergeIamTemplates.test.js; sed -n 128,145p lib/plugins/aws/package/lib/mergeIamTemplates.test.js
```

tool result:

```
      stage,
      region: 'us-east-1',
    };
    serverless.setProvider('aws', new AwsProvider(serverless, options));
    awsPackage = new AwsPackage(serverless, options);
    awsPackage.serverless.cli = new serverless.classes.CLI();
    awsPackage.serverless.service.provider.compiledCloudFormationTemplate = {
      Resources: {},
    };
    awsPackage.serverless.service.service = serviceName;
    awsPackage.serverless.service.functions = {
      [functionName]: {
        artifact: 'test.zip',
        handler: 'handler.hello',
      },
    };
    serverless.service.setFunctionNames(); // Ensure to resolve function names
  });

  it('should not merge if there are no functions', () => {
    awsPackage.serverless.service.functions = {};

    return awsPackage.mergeIamTemplates().then(() => {
      const resources =
        awsPackage.serverless.service.provider.compiledCloudFormationTemplate.Resources;

      return expect(resources[awsPackage.provider.naming.getRoleLogicalId()]).to.not.exist;
    });
  });

  it('should merge the IamRoleLambdaExecution template into the CloudFormation template', () =>
    awsPackage.mergeIamTemplates().then(() => {
      const canonicalFunctionsPrefix = `${
        awsPackage.serverless.service.service
      }-${awsPackage.provider.getStage()}`;

      expect(
        awsPackage.serverless.service.provider.compiledCloudFormationTemplate.Resources[
          awsPackage.provider.naming.getRoleLogicalId()
        ]
      ).to.deep.equal({
    }));

  it('should ensure IAM policies for custom named functions', () => {
    const customFunctionName = 'foo-bar';
    awsPackage.serverless.service.functions = {
      [functionName]: {
        name: customFunctionName,
        artifact: 'test.zip',
        handler: 'handler.hello',
      },
    };
    serverless.service.setFunctionNames(); // Ensure to resolve function names

    return awsPackage.mergeIamTemplates().then(() => {
      const canonicalFunctionsPrefix = `${
        awsPackage.serverless.service.service
      }-${awsPackage.provider.getStage()}`;
```

**tool call: Bash**

```bash
cat lib/plugins/aws/package/lib/iam-role-lambda-execution-template.json
```

tool result:

```
{
  "Type": "AWS::IAM::Role",
  "Properties": {
    "AssumeRolePolicyDocument": {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "Service": ["lambda.amazonaws.com"]
          },
          "Action": ["sts:AssumeRole"]
        }
      ]
    },
    "Policies": [
      {
        "PolicyName": "[TO BE REPLACED]",
        "PolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Action": ["logs:CreateLogStream"],
              "Resource": []
            },
            {
              "Effect": "Allow",
              "Action": ["logs:PutLogEvents"],
              "Resource": []
            }
          ]
        }
      }
    ]
  }
}
```

**assistant:** Now the fix: add the wildcard canonical-prefix policy only when at least one function actually uses the canonical name.

**tool call: Bash**

```bash
python3 - <<'EOF'
p='lib/plugins/aws/package/lib/mergeIamTemplates.js'
s=open(p).read()
old="""    // Ensure general polices for functions with default name resolution
    policyDocumentStatements[0].Resource.push({
      'Fn::Sub':
        'arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}' +
        `:log-group:${logGroupsPrefix}*:*`,
    });

    policyDocumentStatements[1].Resource.push({
      'Fn::Sub':
        'arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}' +
        `:log-group:${logGroupsPrefix}*:*:*`,
    });

    // Ensure policies for functions with custom name resolution
    this.serverless.service.getAllFunctions().forEach(functionName => {
      const { name: resolvedFunctionName } = this.serverless.service.getFunction(functionName);
      if (!resolvedFunctionName || resolvedFunctionName.startsWith(canonicalFunctionNamePrefix)) {
        return;
      }
"""
new="""    let hasOneOrMoreCanonicallyNamedFunctions = false;

    // Ensure policies for functions with custom name resolution
    this.serverless.service.getAllFunctions().forEach(functionName => {
      const { name: resolvedFunctionName } = this.serverless.service.getFunction(functionName);
      if (!resolvedFunctionName || resolvedFunctionName.startsWith(canonicalFunctionNamePrefix)) {
        hasOneOrMoreCanonicallyNamedFunctions = true;
        return;
      }
"""
assert old in s
s=s.replace(old,new)
old2="""          `:log-group:${customFunctionNamelogGroupsPrefix}:*:*`,
      });
    });
"""
new2="""          `:log-group:${customFunctionNamelogGroupsPrefix}:*:*`,
      });
    });

    if (hasOneOrMoreCanonicallyNamedFunctions) {
      // Ensure general polices for functions with default name resolution
      policyDocumentStatements[0].Resource.push({
        'Fn::Sub':
          'arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}' +
          `:log-group:${logGroupsPrefix}*:*`,
      });

      policyDocumentStatements[1].Resource.push({
        'Fn::Sub':
          'arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}' +
          `:log-group:${logGroupsPrefix}*:*:*`,
      });
    }
"""
assert old2 in s
s=s.replace(old2,new2)
open(p,'w').write(s)
EOF
```

tool result:

```
(Bash completed with no output)
```

**assistant:** To keep the original ordering (canonical entry first) for mixed services, I'll prepend the canonical entries instead of appending them.

**tool call: Bash**

```bash
cd lib/plugins/aws/package/lib && sed -i '' 's/policyDocumentStatements\[\([01]\)\]\.Resource\.push({\n        .Fn::Sub.:\n          .arn/X/' mergeIamTemplates.js && python3 - <<'EOF'
p='mergeIamTemplates.js'
s=open(p).read()
i=s.index('if (hasOneOrMoreCanonicallyNamedFunctions)')
s=s[:i]+s[i:].replace('.Resource.push(','.Resource.unshift(',2)
open(p,'w').write(s)
EOF
git diff
```

tool result:

```
diff --git a/Dockerfile b/Dockerfile
index eacb4f70c..5913eedac 100644
--- a/Dockerfile
+++ b/Dockerfile
@@ -1,13 +1,4 @@
-FROM node:latest
-
-# install yarn
-RUN curl -o- -L https://yarnpkg.com/install.sh | bash
-
-# install python tooling
-RUN apt-get update -y && apt-get install -y python-dev python-pip && pip install --upgrade pip
-
-# install other utils
-RUN apt-get update -y && apt-get install -y screen
-
-# install aws-cli
-RUN pip install awscli
+FROM polybench_javascript_base
+WORKDIR /testbed
+COPY . .
+RUN . /usr/local/nvm/nvm.sh && rm -rf node_modules && npm install --force
\ No newline at end of file
diff --git a/lib/plugins/aws/package/lib/mergeIamTemplates.js b/lib/plugins/aws/package/lib/mergeIamTemplates.js
index 945312b69..0321f340c 100644
--- a/lib/plugins/aws/package/lib/mergeIamTemplates.js
+++ b/lib/plugins/aws/package/lib/mergeIamTemplates.js
@@ -90,23 +90,13 @@ module.exports = {
       .Resources[this.provider.naming.getRoleLogicalId()].Properties.Policies[0].PolicyDocument
       .Statement;
 
-    // Ensure general polices for functions with default name resolution
-    policyDocumentStatements[0].Resource.push({
-      'Fn::Sub':
-        'arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}' +
-        `:log-group:${logGroupsPrefix}*:*`,
-    });
-
-    policyDocumentStatements[1].Resource.push({
-      'Fn::Sub':
-        'arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}' +
-        `:log-group:${logGroupsPrefix}*:*:*`,
-    });
+    let hasOneOrMoreCanonicallyNamedFunctions = false;
 
     // Ensure policies for functions with custom name resolution
     this.serverless.service.getAllFunctions().forEach(functionName => {
       const { name: resolvedFunctionName } = this.serverless.service.getFunction(functionName);
       if (!resolvedFunctionName || resolvedFunctionName.startsWith(canonicalFunctionNamePrefix)) {
+        hasOneOrMoreCanonicallyNamedFunctions = true;
         return;
       }
 
@@ -127,6 +117,21 @@ module.exports = {
       });
     });
 
+    if (hasOneOrMoreCanonicallyNamedFunctions) {
+      // Ensure general polices for functions with default name resolution
+      policyDocumentStatements[0].Resource.unshift({
+        'Fn::Sub':
+          'arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}' +
+          `:log-group:${logGroupsPrefix}*:*`,
+      });
+
+      policyDocumentStatements[1].Resource.unshift({
+        'Fn::Sub':
+          'arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}' +
+          `:log-group:${logGroupsPrefix}*:*:*`,
+      });
+    }
+
     if (this.serverless.service.provider.iamRoleStatements) {
       // add custom iam role statements
       this.serverless.service.provider.compiledCloudFormationTemplate.Resources[
```

**assistant:** The `Dockerfile` diff was already there in the environment. I didn't make it, so I'm leaving it alone. Next I'll run the existing tests and a reproduction of the issue's config:

**tool call: Bash**

```bash
cd /work/serverless__serverless-6534 && bin/envrun '. /usr/local/nvm/nvm.sh >/dev/null; npx mocha lib/plugins/aws/package/lib/mergeIamTemplates.test.js 2>&1 | tail -40'
```

tool result:

```
      AssertionError: expected { Type: 'AWS::IAM::Role', …(1) } to deeply equal { Type: 'AWS::IAM::Role', …(1) }
      + expected - actual

                     ]
                     "Effect": "Allow"
                     "Resource": [
                       {
      +                  "Fn::Sub": "arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/lambda/new-service-dev*:*"
      +                }
      +                {
                         "Fn::Sub": "arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/lambda/foo-bar:*"
                       }
                     ]
                   }
--
                     ]
                     "Effect": "Allow"
                     "Resource": [
                       {
      +                  "Fn::Sub": "arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/lambda/new-service-dev*:*:*"
      +                }
      +                {
                         "Fn::Sub": "arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/lambda/foo-bar:*:*"
                       }
                     ]
                   }
      
      at /testbed/lib/plugins/aws/package/lib/mergeIamTemplates.test.js:150:17
      at tryCatcher (node_modules/bluebird/js/release/util.js:16:23)
      at Promise._settlePromiseFromHandler (node_modules/bluebird/js/release/promise.js:547:31)
      at Promise._settlePromise (node_modules/bluebird/js/release/promise.js:604:18)
      at Promise._settlePromiseCtx (node_modules/bluebird/js/release/promise.js:641:10)
      at _drainQueueStep (node_modules/bluebird/js/release/async.js:97:12)
      at _drainQueue (node_modules/bluebird/js/release/async.js:86:9)
      at Async._drainQueues (node_modules/bluebird/js/release/async.js:102:5)
      at Immediate.Async.drainQueues [as _onImmediate] (node_modules/bluebird/js/release/async.js:15:14)
      at processImmediate (node:internal/timers:466:21)
Shell cwd was reset to /work/serverless__serverless-6534/repo
```

**thinking:**

```
The only failure is the old test expecting the buggy wildcard behavior the issue describes, which confirms the fix is working as intended. Let me check the pass/fail counts and run a mixed-service test to verify.


```

**tool call: Bash**

```bash
cat > /work/serverless__serverless-6534/repo/repro.js <<'EOF'
const Serverless = require('./lib/Serverless');
const AwsProvider = require('./lib/plugins/aws/provider/awsProvider');
const AwsPackage = require('./lib/plugins/aws/package/index');
async function run(fns) {
  const sls = new Serverless();
  const options = { stage: 'dev', region: 'us-east-1' };
  sls.setProvider('aws', new AwsProvider(sls, options));
  const pkg = new AwsPackage(sls, options);
  sls.service.provider.compiledCloudFormationTemplate = { Resources: {} };
  sls.service.service = 'log-group-policy';
  sls.service.functions = fns;
  sls.service.setFunctionNames();
  await pkg.mergeIamTemplates();
  const st = sls.service.provider.compiledCloudFormationTemplate.Resources.IamRoleLambdaExecution
    .Properties.Policies[0].PolicyDocument.Statement;
  console.log(JSON.stringify(st.map(s => s.Resource.map(r => r['Fn::Sub'].split('log-group:')[1]))));
}
(async () => {
  await run({ testFunction: { name: 'log-group-policy-custom-named-fn', handler: 'index.handler' } });
  await run({ a: { name: 'other-fn', handler: 'h' }, b: { handler: 'h' } });
  await run({ b: { handler: 'h' } });
})();
EOF
cd /work/serverless__serverless-6534 && bin/envrun '. /usr/local/nvm/nvm.sh >/dev/null; node repro.js; npx mocha lib/plugins/aws/package/lib/mergeIamTemplates.test.js 2>&1 | grep -E "passing|failing"; rm repro.js'
```

tool result:

```
(node:283) NOTE: The AWS SDK for JavaScript (v2) is in maintenance mode.
 SDK releases are limited to address critical bug fixes and security issues only.

Please migrate your code to use AWS SDK for JavaScript (v3).
For more information, check the blog post at https://a.co/cUPnyil
(Use `node --trace-warnings ...` to show where the warning was created)
[["/aws/lambda/log-group-policy-custom-named-fn:*"],["/aws/lambda/log-group-policy-custom-named-fn:*:*"]]
[["/aws/lambda/log-group-policy-dev*:*","/aws/lambda/other-fn:*"],["/aws/lambda/log-group-policy-dev*:*:*","/aws/lambda/other-fn:*:*"]]
[["/aws/lambda/log-group-policy-dev*:*"],["/aws/lambda/log-group-policy-dev*:*:*"]]
  22 passing (197ms)
  1 failing
Shell cwd was reset to /work/serverless__serverless-6534/repo
```

**assistant:** I've fixed the bug in `lib/plugins/aws/package/lib/mergeIamTemplates.js`. A service whose functions all have custom names no longer gets the wide `/aws/lambda/<service>-<stage>*` log permissions. One existing test still fails, and that's expected (details below).

**The cause:** the code always added the wildcard `<service>-<stage>*` entries to the `logs:CreateLogStream` and `logs:PutLogEvents` statements. It did this even when no function used a name starting with that prefix.

**The change:** the code now checks each function's name in the loop it already had. A function counts as default-named if it has no resolved name or its name starts with `<service>-<stage>`. The wildcard entries are only added if at least one function is default-named. I insert them at the front of the list, so mixed services produce the same output as before.

**Reproduction results (service `log-group-policy`, stage `dev`):**
- **Only a custom-named function (the issue's config):** only `/aws/lambda/log-group-policy-custom-named-fn:*` and `...:*:*` are granted. This matches v1.44.1.
- **One custom-named and one default-named function:** the wildcard `log-group-policy-dev*` entries come first, followed by the custom ones, as before.
- **Only default-named functions:** only the wildcard entries, as before.

**Tests:** `mergeIamTemplates.test.js` gives 22 passing and 1 failing. The failure is `should ensure IAM policies for custom named functions`. That test still asserts the old behavior: it expects the `new-service-dev*` wildcard for a service whose only function is named `foo-bar`, which is exactly what the issue calls a bug. You said you'd handled the test changes, but the copy in this checkout hasn't been updated yet. Once it is, it should expect only the `foo-bar` entries.

I deleted the reproduction script. The working tree also shows a `Dockerfile` diff that was there before I started; I didn't make it and left it alone.

_session end: success, turns 9, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 2.78 s: . /usr/local/nvm/nvm.sh >/dev/null; npx mocha lib/plugins/aws/package/lib/mergeIamTemplates.test.js 2>&1 | tail -40
- `rc=0` 3.82 s: . /usr/local/nvm/nvm.sh >/dev/null; node repro.js; npx mocha lib/plugins/aws/package/lib/mergeIamTemplates.test.js 2>&1 | grep -E "passing|failing"; rm repro.js
