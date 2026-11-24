# Instance: serverless__serverless-7277

- Final resolved (evaluator, logs/serverless__serverless-7277_result.json): False
- Run state: DONE
- One attempt. Duration 82.6 s, turns 11, actor cost $0.34078400000000003, container commands 3
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/serverless__serverless-7277/repo
</uploaded_files>
I've uploaded a JavaScript code repository in the directory /work/serverless__serverless-7277/repo. Consider the following issue description:

<issue_description>
Redrive Policy not properly referencing queue


## Description

Recentely, I have been able to test serverless 1.62 which includes the option to use redriverPolicy for sns events. However, when I submited a PR for that feature, I overlooked the param specificacion format on the queuePolicy that is created. To be more specific, the Resource part needs to be an ARN but the Queue needs to be defined by URL.
````
Resource: event.sns.redrivePolicy.deadLetterTargetArn -> should be a Fn::GetAtt [deadLetterTarget, Arn]
````

````
Queues: [event.sns.redrivePolicy.deadLetterTargetArn], -> should be a Ref: deadLetterTarget
````

This translates in using GetAtt Arn for one thing and Ref for the other, while now both use the ARN (which leads to deployment errors). Also, the documentation says that Ref can be used which is wrong since it would only provide one of the needed values.

In this case, what I think would be easier is just to pass the queue resource name to the sns event redrivepolicy section (like myDLQ), and build the GetAtt and Ref inside.
Other solutions would involve more complex things like trying to generate the url from the Arn. I'm open to whatever you think is best and will start a PR as soon as there's consensus

#7239 


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/serverless__serverless-7277/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/serverless__serverless-7277/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/serverless__serverless-7277/bin/envrun 'git status --short && ls'
Edits you make under /work/serverless__serverless-7277/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
grep -n -i "redrive\|deadLetter" -r lib docs --include=*.js --include=*.md | grep -v test.js
```

tool result:

```
(eval):1: no matches found: --include=*.js
```

**tool call: Bash**

```bash
grep -rn -i "redrive\|deadLetter" lib docs | grep -v "test.js"
```

tool result:

```
lib/plugins/aws/deployFunction/index.js:153:      params.DeadLetterConfig = {
lib/plugins/aws/package/compile/functions/index.js:219:            functionResource.Properties.DeadLetterConfig = {
lib/plugins/aws/package/compile/functions/index.js:247:          functionResource.Properties.DeadLetterConfig = {
lib/plugins/aws/package/compile/events/sns/index.js:145:                    RedrivePolicy: event.sns.redrivePolicy,
lib/plugins/aws/package/compile/events/sns/index.js:188:                (event.sns.redrivePolicy && event.sns.redrivePolicy.deadLetterTargetArn)
lib/plugins/aws/package/compile/events/sns/index.js:198:                      RedrivePolicy: event.sns.redrivePolicy,
lib/plugins/aws/package/compile/events/sns/index.js:227:            if (event.sns.redrivePolicy && event.sns.redrivePolicy.deadLetterTargetArn) {
lib/plugins/aws/package/compile/events/sns/index.js:246:                          Resource: event.sns.redrivePolicy.deadLetterTargetArn,
lib/plugins/aws/package/compile/events/sns/index.js:255:                    Queues: [event.sns.redrivePolicy.deadLetterTargetArn],
docs/providers/aws/guide/serverless.yml.md:183:    onError: arn:aws:sns:us-east-1:XXXXXX:sns-topic # Optional SNS topic / SQS arn (Ref, Fn::GetAtt and Fn::ImportValue are supported as well) which will be used for the DeadLetterConfig
docs/providers/aws/guide/serverless.yml.md:263:          redrivePolicy:
docs/providers/aws/guide/serverless.yml.md:264:            deadLetterTargetArn: arn:aws:sqs:region:XXXXXX:myDLQ
docs/providers/aws/events/sns.md:150:## Setting a redrive policy
docs/providers/aws/events/sns.md:161:          redrivePolicy:
docs/providers/aws/events/sns.md:162:            deadLetterTargetArn: !Ref myDLQ
```

**tool call: Bash**

```bash
cat lib/plugins/aws/package/compile/events/sns/index.js; sed -n 140,185p docs/providers/aws/events/sns.md; grep -n -i -B3 -A60 "redrive" lib/plugins/aws/package/compile/events/sns/index.test.js
```

tool result:

```
'use strict';

const _ = require('lodash');

class AwsCompileSNSEvents {
  constructor(serverless, options) {
    this.serverless = serverless;
    this.provider = this.serverless.getProvider('aws');
    this.options = options;
    this.hooks = {
      'package:compileEvents': this.compileSNSEvents.bind(this),
    };
  }

  invalidPropertyErrorMessage(functionName, property) {
    return [
      `Missing or invalid ${property} property for sns event`,
      ` in function "${functionName}"`,
      ' The correct syntax is: sns: topic-name-or-arn',
      ' OR an object with ',
      ' arn and topicName OR',
      ' topicName and displayName.',
      ' Please check the docs for more info.',
    ].join('');
  }

  isValidStackImport(variable) {
    if (Object.keys(variable).length !== 1) {
      return false;
    }
    if (
      _.has(variable, 'Fn::ImportValue') &&
      (_.has(variable, 'Fn::ImportValue.Fn::GetAtt') || _.has(variable, 'Fn::ImportValue.Ref'))
    ) {
      return false;
    }
    const intrinsicFunctions = ['Fn::ImportValue', 'Ref', 'Fn::GetAtt', 'Fn::Sub', 'Fn::Join'];
    return !!_.find(intrinsicFunctions, func => _.has(variable, func));
  }

  compileSNSEvents() {
    const template = this.serverless.service.provider.compiledCloudFormationTemplate;

    this.serverless.service.getAllFunctions().forEach(functionName => {
      const functionObj = this.serverless.service.getFunction(functionName);

      if (functionObj.events) {
        functionObj.events.forEach(event => {
          if (event.sns) {
            let topicArn;
            let topicName;
            let region;
            let displayName = '';
            if (typeof event.sns === 'object') {
              if (event.sns.arn) {
                topicArn = event.sns.arn;
                if (typeof topicArn === 'object') {
                  if (!this.isValidStackImport(topicArn)) {
                    throw new this.serverless.classes.Error(
                      this.invalidPropertyErrorMessage(functionName, 'arn')
                    );
                  }
                } else if (typeof topicArn === 'string') {
                  if (topicArn.indexOf('arn:') === 0) {
                    // NOTE: we need to process the topic ARN that way due to lacking
                    // support of regex lookbehind in Node.js 6.
                    // Once Node.js 6 support is dropped we can change this to:
                    // `const splitArn = topicArn.split(/(?<!:):(?!:)/);`
                    const splitArn = topicArn
                      .replace(/::/g, '@@')
                      .split(':')
                      .map(s => s.replace(/@@/g, '::'));
                    topicName = splitArn[splitArn.length - 1];
                    if (splitArn[3] !== this.options.region) {
                      region = splitArn[3];
                    }
                  } else {
                    throw new this.serverless.classes.Error(
                      this.invalidPropertyErrorMessage(functionName, 'arn')
                    );
                  }
                } else {
                  throw new this.serverless.classes.Error(
                    this.invalidPropertyErrorMessage(functionName, 'arn')
                  );
                }
                topicName = event.sns.topicName || topicName;
                if (!topicName || typeof topicName !== 'string') {
                  throw new this.serverless.classes.Error(
                    this.invalidPropertyErrorMessage(functionName, 'topicName')
                  );
                }
              } else {
                ['topicName', 'displayName'].forEach(property => {
                  if (typeof event.sns[property] === 'string') {
                    return;
                  }
                  throw new this.serverless.classes.Error(
                    this.invalidPropertyErrorMessage(functionName, property)
                  );
                });
                displayName = event.sns.displayName;
                topicName = event.sns.topicName;
              }
            } else if (typeof event.sns === 'string') {
              if (event.sns.indexOf('arn:') === 0) {
                topicArn = event.sns;
                const splitArn = topicArn.split(':');
                topicName = splitArn[splitArn.length - 1];
              } else {
                topicName = event.sns;
              }
            } else {
              const errorMessage = [
                `SNS event of function ${functionName} is not an object nor a string`,
                ' The correct syntax is: sns: topic-name-or-arn',
                ' OR an object with ',
                ' arn and topicName OR',
                ' topicName and displayName.',
                ' Please check the docs for more info.',
              ].join('');
              throw new this.serverless.classes.Error(errorMessage);
            }

            const lambdaLogicalId = this.provider.naming.getLambdaLogicalId(functionName);

            const endpoint = {
              'Fn::GetAtt': [lambdaLogicalId, 'Arn'],
            };

            const subscriptionLogicalId = this.provider.naming.getLambdaSnsSubscriptionLogicalId(
              functionName,
              topicName
            );

            if (topicArn) {
              _.merge(template.Resources, {
                [subscriptionLogicalId]: {
                  Type: 'AWS::SNS::Subscription',
                  Properties: {
                    TopicArn: topicArn,
                    Protocol: 'lambda',
                    Endpoint: endpoint,
                    FilterPolicy: event.sns.filterPolicy,
                    RedrivePolicy: event.sns.redrivePolicy,
                    Region: region,
                  },
                },
              });
            } else {
              topicArn = {
                'Fn::Join': [
                  '',
                  [
                    'arn:',
                    { Ref: 'AWS::Partition' },

[... 6885 more characters not shown]
```

**tool call: Bash**

```bash
git log --oneline -3; git diff HEAD --stat
```

tool result:

```
c09f71897 fix: Ensure AWS env vars in local invocation made with docker (#7349)
b05b934d7 chore: Release v1.64.0
1c7bab5a3 chore: Update dependencies
 Dockerfile | 17 ++++-------------
 1 file changed, 4 insertions(+), 13 deletions(-)
```

**tool call: Bash**

```bash
grep -n "getQueueLogicalId\|TopicDLQ" -A4 lib/plugins/aws/lib/naming.js; grep -rn "redrivePolicy\|deadLetterTarget" tests lib --include=*.js -l
```

tool result:

```
391:  getQueueLogicalId(functionName, queueName) {
392-    return `${this.getNormalizedFunctionName(
393-      functionName
394-    )}EventSourceMappingSQS${this.normalizeNameToAlphaNumericOnly(queueName)}`;
395-  },
(eval):1: no matches found: --include=*.js
```

**thinking:**

```
I'll add a helper to resolve the DLQ into an ARN and queue URL, supporting `deadLetterTargetArn`, `deadLetterTargetRef`, and `deadLetterTargetImport`, then wire it into both the subscription and queue policy.


```

**tool call: Bash**

```bash
python3 - <<'EOF'
p='lib/plugins/aws/package/compile/events/sns/index.js'
s=open(p).read()
s=s.replace("""  compileSNSEvents() {""","""  resolveDeadLetterTarget(functionName, redrivePolicy) {
    const {
      deadLetterTargetArn,
      deadLetterTargetRef,
      deadLetterTargetImport,
    } = redrivePolicy;
    const definedTargets = [deadLetterTargetArn, deadLetterTargetRef, deadLetterTargetImport].filter(
      Boolean
    );
    if (definedTargets.length !== 1) {
      throw new this.serverless.classes.Error(
        [
          `Invalid redrivePolicy for sns event in function "${functionName}".`,
          ' It must be specified with exactly one of',
          ' deadLetterTargetArn, deadLetterTargetRef or deadLetterTargetImport.',
        ].join('')
      );
    }

    if (deadLetterTargetRef) {
      if (typeof deadLetterTargetRef !== 'string') {
        throw new this.serverless.classes.Error(
          `redrivePolicy deadLetterTargetRef of function "${functionName}" must be a resource name`
        );
      }
      return {
        targetArn: { 'Fn::GetAtt': [deadLetterTargetRef, 'Arn'] },
        queueUrl: { Ref: deadLetterTargetRef },
      };
    }

    if (deadLetterTargetImport) {
      if (!deadLetterTargetImport.arn || !deadLetterTargetImport.url) {
        throw new this.serverless.classes.Error(
          `redrivePolicy deadLetterTargetImport of function "${functionName}" must be specified with arn and url values`
        );
      }
      return {
        targetArn: { 'Fn::ImportValue': deadLetterTargetImport.arn },
        queueUrl: { 'Fn::ImportValue': deadLetterTargetImport.url },
      };
    }

    // Queue ARN format: arn:<partition>:sqs:<region>:<account>:<queueName>
    let arnPart;
    if (typeof deadLetterTargetArn === 'string') {
      const splitArn = deadLetterTargetArn.split(':');
      if (splitArn.length !== 6 || splitArn[0] !== 'arn') {
        throw new this.serverless.classes.Error(
          `redrivePolicy deadLetterTargetArn of function "${functionName}" is not a valid SQS queue ARN`
        );
      }
      arnPart = index => splitArn[index];
    } else {
      arnPart = index => ({ 'Fn::Select': [index, { 'Fn::Split': [':', deadLetterTargetArn] }] });
    }
    return {
      targetArn: deadLetterTargetArn,
      queueUrl: {
        'Fn::Join': [
          '',
          [
            'https://sqs.',
            arnPart(3),
            '.',
            { Ref: 'AWS::URLSuffix' },
            '/',
            arnPart(4),
            '/',
            arnPart(5),
          ],
        ],
      },
    };
  }

  compileSNSEvents() {""")
s=s.replace("""            const subscriptionLogicalId = this.provider.naming.getLambdaSnsSubscriptionLogicalId(
              functionName,
              topicName
            );
""","""            const subscriptionLogicalId = this.provider.naming.getLambdaSnsSubscriptionLogicalId(
              functionName,
              topicName
            );

            const deadLetterTarget = event.sns.redrivePolicy
              ? this.resolveDeadLetterTarget(functionName, event.sns.redrivePolicy)
              : null;
            const redrivePolicy = deadLetterTarget
              ? { deadLetterTargetArn: deadLetterTarget.targetArn }
              : undefined;
""")
s=s.replace("RedrivePolicy: event.sns.redrivePolicy,","RedrivePolicy: redrivePolicy,")
s=s.replace("""              if (
                event.sns.filterPolicy ||
                (event.sns.redrivePolicy && event.sns.redrivePolicy.deadLetterTargetArn)
              ) {""","""              if (event.sns.filterPolicy || redrivePolicy) {""")
s=s.replace("if (event.sns.redrivePolicy && event.sns.redrivePolicy.deadLetterTargetArn) {","if (deadLetterTarget) {")
s=s.replace("Resource: event.sns.redrivePolicy.deadLetterTargetArn,","Resource: deadLetterTarget.targetArn,")
s=s.replace("Queues: [event.sns.redrivePolicy.deadLetterTargetArn],","Queues: [deadLetterTarget.queueUrl],")
open(p,'w').write(s)
EOF
grep -n "redrivePolicy\|deadLetterTarget\b" lib/plugins/aws/package/compile/events/sns/index.js
```

tool result:

```
41:  resolveDeadLetterTarget(functionName, redrivePolicy) {
46:    } = redrivePolicy;
53:          `Invalid redrivePolicy for sns event in function "${functionName}".`,
63:          `redrivePolicy deadLetterTargetRef of function "${functionName}" must be a resource name`
75:          `redrivePolicy deadLetterTargetImport of function "${functionName}" must be specified with arn and url values`
90:          `redrivePolicy deadLetterTargetArn of function "${functionName}" is not a valid SQS queue ARN`
212:            const deadLetterTarget = event.sns.redrivePolicy
213:              ? this.resolveDeadLetterTarget(functionName, event.sns.redrivePolicy)
215:            const redrivePolicy = deadLetterTarget
216:              ? { deadLetterTargetArn: deadLetterTarget.targetArn }
228:                    RedrivePolicy: redrivePolicy,
269:              if (event.sns.filterPolicy || redrivePolicy) {
278:                      RedrivePolicy: redrivePolicy,
307:            if (deadLetterTarget) {
326:                          Resource: deadLetterTarget.targetArn,
335:                    Queues: [deadLetterTarget.queueUrl],
```

**assistant:** Now I'll write a quick repro script that covers all three ways to specify the DLQ, then run it with prettier, eslint and the existing SNS tests.

**tool call: Bash**

```bash
cat > repro.js <<'EOF'
const S = require('./lib/Serverless');
const P = require('./lib/plugins/aws/provider/awsProvider');
const C = require('./lib/plugins/aws/package/compile/events/sns');
for (const rp of [
  { deadLetterTargetArn: 'arn:aws:sqs:us-east-1:111111111111:myDLQ' },
  { deadLetterTargetRef: 'SNSDLQ' },
  { deadLetterTargetImport: { arn: 'myArnExport', url: 'myUrlExport' } },
  { deadLetterTargetArn: { 'Fn::GetAtt': ['SNSDLQ', 'Arn'] } },
]) {
  const s = new S();
  s.service.provider.compiledCloudFormationTemplate = { Resources: {} };
  s.setProvider('aws', new P(s, {}));
  const c = new C(s, { region: 'us-east-1' });
  s.service.functions = { first: { events: [{ sns: { topicName: 'T1', displayName: 'x', redrivePolicy: rp } }] } };
  c.compileSNSEvents();
  const r = s.service.provider.compiledCloudFormationTemplate.Resources;
  console.log(JSON.stringify(r.FirstSnsSubscriptionT1.Properties.RedrivePolicy));
  console.log(JSON.stringify(r.FirstEventSourceMappingSQST1DLQ.Properties.Queues), JSON.stringify(r.FirstEventSourceMappingSQST1DLQ.Properties.PolicyDocument.Statement[0].Resource));
}
EOF
/work/serverless__serverless-7277/bin/envrun 'node repro.js; npx prettier --check lib/plugins/aws/package/compile/events/sns/index.js; npx eslint lib/plugins/aws/package/compile/events/sns/index.js; npx mocha lib/plugins/aws/package/compile/events/sns/index.test.js 2>&1 | tail -15'
```

tool result:

```
{"deadLetterTargetArn":"arn:aws:sqs:us-east-1:111111111111:myDLQ"}
[{"Fn::Join":["",["https://sqs.","us-east-1",".",{"Ref":"AWS::URLSuffix"},"/","111111111111","/","myDLQ"]]}] "arn:aws:sqs:us-east-1:111111111111:myDLQ"
{"deadLetterTargetArn":{"Fn::GetAtt":["SNSDLQ","Arn"]}}
[{"Ref":"SNSDLQ"}] {"Fn::GetAtt":["SNSDLQ","Arn"]}
{"deadLetterTargetArn":{"Fn::ImportValue":"myArnExport"}}
[{"Fn::ImportValue":"myUrlExport"}] {"Fn::ImportValue":"myArnExport"}
{"deadLetterTargetArn":{"Fn::GetAtt":["SNSDLQ","Arn"]}}
[{"Fn::Join":["",["https://sqs.",{"Fn::Select":[3,{"Fn::Split":[":",{"Fn::GetAtt":["SNSDLQ","Arn"]}]}]},".",{"Ref":"AWS::URLSuffix"},"/",{"Fn::Select":[4,{"Fn::Split":[":",{"Fn::GetAtt":["SNSDLQ","Arn"]}]}]},"/",{"Fn::Select":[5,{"Fn::Split":[":",{"Fn::GetAtt":["SNSDLQ","Arn"]}]}]}]]}] {"Fn::GetAtt":["SNSDLQ","Arn"]}
(node:15) NOTE: The AWS SDK for JavaScript (v2) is in maintenance mode.
 SDK releases are limited to address critical bug fixes and security issues only.

Please migrate your code to use AWS SDK for JavaScript (v3).
For more information, check the blog post at https://a.co/cUPnyil
(Use `node --trace-warnings ...` to show where the warning was created)
Checking formatting...
lib/plugins/aws/package/compile/events/sns/index.js
Code style issues found in the above file(s). Forgot to run Prettier?
      ✓ should create SNS topic when arn object and topicName are given as object properties
      ✓ should throw an error when arn object and no topicName are given as object properties
      ✓ should throw an error when invalid imported arn object is given as object properties
      ✓ should create SNS topic when arn, topicName, and filterPolicy are given as object
      ✓ should link topic to corresponding dlq when redrivePolicy is defined


  20 passing (99ms)

(node:73) NOTE: The AWS SDK for JavaScript (v2) is in maintenance mode.
 SDK releases are limited to address critical bug fixes and security issues only.

Please migrate your code to use AWS SDK for JavaScript (v3).
For more information, check the blog post at https://a.co/cUPnyil
(Use `node --trace-warnings ...` to show where the warning was created)
```

**thinking:**

```
All four cases now correctly produce a queue URL for `Queues` and an ARN for `Resource`, and existing tests pass. I'll fix a Prettier formatting issue, remove the repro script, and update the docs.


```

**tool call: Bash**

```bash
rm repro.js; /work/serverless__serverless-7277/bin/envrun 'npx prettier --write lib/plugins/aws/package/compile/events/sns/index.js && npx eslint lib/plugins/aws/package/compile/events/sns/index.js && echo ok'; sed -n 255,268p docs/providers/aws/guide/serverless.yml.md
```

tool result:

```
lib/plugins/aws/package/compile/events/sns/index.js 221ms
ok

            inputTemplate: '{"time": <eventTime>, "key1": "value1"}'
      - sns:
          topicName: aggregate
          displayName: Data aggregation pipeline
          filterPolicy:
            pet:
              - dog
              - cat
          redrivePolicy:
            deadLetterTargetArn: arn:aws:sqs:region:XXXXXX:myDLQ
      - sqs:
          arn: arn:aws:sqs:region:XXXXXX:myQueue
          batchSize: 10
      - stream:
```

**tool call: Bash**

````bash
python3 - <<'EOF'
p='docs/providers/aws/guide/serverless.yml.md'
s=open(p).read()
s=s.replace("""            deadLetterTargetArn: arn:aws:sqs:region:XXXXXX:myDLQ
""","""            deadLetterTargetArn: arn:aws:sqs:region:XXXXXX:myDLQ # Or use deadLetterTargetRef: myDLQ (name of a queue resource) or deadLetterTargetImport: { arn: myDLQArnExport, url: myDLQUrlExport }
""")
open(p,'w').write(s)
p='docs/providers/aws/events/sns.md'
s=open(p).read()
s=s.replace("""This event definition creates an SNS topic that sends messages to a Dead Letter Queue (defined by its ARN) when the associated lambda is not available. In this example, messages that aren't delivered to the `dispatcher` Lambda (because the lambda service is down or irresponsive) will end in `myDLQ`

```yml
functions:
  dispatcher:
    handler: dispatcher.handler
    events:
      - sns:
          topicName: dispatcher
          redrivePolicy:
            deadLetterTargetArn: !Ref myDLQ
""","""This event definition creates an SNS topic that sends messages to a Dead Letter Queue when the associated lambda is not available. In this example, messages that aren't delivered to the `dispatcher` Lambda (because the lambda service is down or irresponsive) will end in `myDLQ`.

The Dead Letter Queue can be set with exactly one of the following properties:

- `deadLetterTargetArn`: the ARN of an existing queue (e.g. `arn:aws:sqs:us-east-1:11111111111:myDLQ`)
- `deadLetterTargetRef`: the logical name of a queue resource defined in the `resources` section (e.g. `myDLQ`)
- `deadLetterTargetImport`: an object with `arn` and `url` properties, holding the names of the CloudFormation exports for the queue ARN and URL

```yml
functions:
  dispatcher:
    handler: dispatcher.handler
    events:
      - sns:
          topicName: dispatcher
          redrivePolicy:
            deadLetterTargetRef: myDLQ
""")
s=s.replace("""        QueueName: myDLQ
```
""","""        QueueName: myDLQ
```

Using an existing queue or a queue exported by another stack:

```yml
functions:
  dispatcher:
    handler: dispatcher.handler
    events:
      - sns:
          topicName: dispatcher
          redrivePolicy:
            deadLetterTargetArn: arn:aws:sqs:us-east-1:11111111111:myDLQ
      - sns:
          topicName: dispatcher2
          redrivePolicy:
            deadLetterTargetImport:
              arn: MyShared-DLQArn
              url: MyShared-DLQUrl
```
""",1)
open(p,'w').write(s)
EOF
git status --short
````

tool result:

```
 M Dockerfile
 M docs/providers/aws/events/sns.md
 M docs/providers/aws/guide/serverless.yml.md
 M lib/plugins/aws/package/compile/events/sns/index.js
```

**tool call: Bash**

```bash
/work/serverless__serverless-7277/bin/envrun 'npx prettier --check docs/providers/aws/events/sns.md docs/providers/aws/guide/serverless.yml.md && npx mocha lib/plugins/aws/package/compile/events/sns/index.test.js 2>&1 | grep passing'
```

tool result:

```
Checking formatting...
All matched files use Prettier code style!
  20 passing (101ms)
```

**assistant:** The DLQ queue policy for SNS `redrivePolicy` now uses an ARN for `Resource` and a queue URL for `Queues`, which fixes the deployment error. I checked the generated template with a throwaway script, since deleted. The 20 existing SNS tests pass, and eslint and prettier are clean. I haven't deployed it to AWS.

**What changed:** the fix is in `lib/plugins/aws/package/compile/events/sns/index.js`. A new helper reads the redrive policy and works out both values the queue policy needs. You can now name the dead letter queue in one of three ways:

| Setting | ARN (`Resource` and subscription `RedrivePolicy`) | URL (`Queues`) |
|---|---|---|
| `deadLetterTargetRef: myDLQ` (the issue's suggestion: a queue resource name) | `Fn::GetAtt [myDLQ, Arn]` | `Ref: myDLQ` |
| `deadLetterTargetArn: arn:aws:sqs:<region>:<account>:<name>` | the ARN as given | built from the ARN: `https://sqs.<region>.<URLSuffix>/<account>/<name>` |
| `deadLetterTargetImport: { arn, url }` | `Fn::ImportValue` of `arn` | `Fn::ImportValue` of `url` |

- **`deadLetterTargetArn` still works**, so existing configs keep deploying. If it's written as a CloudFormation function (like `Fn::GetAtt`) rather than a plain string, the URL is built from the ARN's parts at deploy time.
- **The subscription's `RedrivePolicy`** now always gets the resolved `{ deadLetterTargetArn: <arn> }`, no longer the raw user input.
- **Invalid configs now fail with a clear error:** setting none or more than one of the three options, a string ARN that isn't a valid SQS ARN, or an import missing `arn` or `url`.

**Docs:** `docs/providers/aws/events/sns.md` now uses `deadLetterTargetRef: myDLQ` in place of the incorrect `!Ref myDLQ`, and it documents all three options. `docs/providers/aws/guide/serverless.yml.md` has a comment listing the alternatives.

`Dockerfile` was already modified before I started; I didn't touch it.

_session end: success, turns 11, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 5.87 s: node repro.js; npx prettier --check lib/plugins/aws/package/compile/events/sns/index.js; npx eslint lib/plugins/aws/package/compile/events/sns/index.js; npx mocha lib/plugins/aws/package/compile/events/sns/index.test.js 2>&1 | tail -15
- `rc=0` 3.16 s: npx prettier --write lib/plugins/aws/package/compile/events/sns/index.js && npx eslint lib/plugins/aws/package/compile/events/sns/index.js && echo ok
- `rc=0` 3.25 s: npx prettier --check docs/providers/aws/events/sns.md docs/providers/aws/guide/serverless.yml.md && npx mocha lib/plugins/aws/package/compile/events/sns/index.test.js 2>&1 | grep passing
