# Instance: serverless__serverless-8159

- Final resolved (evaluator, logs/serverless__serverless-8159_result.json): True
- Run state: DONE
- One attempt. Duration 59.5 s, turns 12, actor cost $0.29245340000000003, container commands 3
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/serverless__serverless-8159/repo
</uploaded_files>
I've uploaded a JavaScript code repository in the directory /work/serverless__serverless-8159/repo. Consider the following issue description:

<issue_description>
Allow for the removal of default request mapping templates
Currently [default request mapping templates are created ](https://github.com/serverless/serverless/blob/v1.58.0/lib/plugins/aws/package/compile/events/apiGateway/lib/method/integration.js#L189) both for application/json and application/x-www-form-urlencoded. There does not appear to be a simple method for overriding this default. In our application we only support the application/json content type however application/x-www-form-urlencoded is being automatically created even though it is not supported by our application. Even worse, when generating swagger documentation via the AWS API Gateway this forces us advertise that we consume both:

"consumes": [
          "application/json",
          "application/x-www-form-urlencoded"
        ],

IMO, there really should be a way of overriding defaults in any application. If you can suggest any workaround to this it would be great


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/serverless__serverless-8159/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/serverless__serverless-8159/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/serverless__serverless-8159/bin/envrun 'git status --short && ls'
Edits you make under /work/serverless__serverless-8159/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/serverless__serverless-8159/repo; cat lib/plugins/aws/package/compile/events/apiGateway/lib/method/integration.js; git log --oneline -1
```

tool result:

```
'use strict';

const _ = require('lodash');

const DEFAULT_COMMON_TEMPLATE = `
  #define( $loop )
    {
    #foreach($key in $map.keySet())
        #set( $k = $util.escapeJavaScript($key) )
        #set( $v = $util.escapeJavaScript($map.get($key)).replaceAll("\\\\'", "'") )
        "$k":
          "$v"
          #if( $foreach.hasNext ) , #end
    #end
    }
  #end

  {
    "body": $body,
    "method": "$context.httpMethod",
    "principalId": "$context.authorizer.principalId",
    "stage": "$context.stage",

    "cognitoPoolClaims" : {
       extraCognitoPoolClaims
       "sub": "$context.authorizer.claims.sub"
    },

    #set( $map = $context.authorizer )
    "enhancedAuthContext": $loop,

    #set( $map = $input.params().header )
    "headers": $loop,

    #set( $map = $input.params().querystring )
    "query": $loop,

    #set( $map = $input.params().path )
    "path": $loop,

    #set( $map = $context.identity )
    "identity": $loop,

    #set( $map = $stageVariables )
    "stageVariables": $loop,

    "requestPath": "$context.resourcePath"
  }
`;

module.exports = {
  getMethodIntegration(http, { lambdaLogicalId, lambdaAliasName }) {
    const type = http.integration || 'AWS_PROXY';
    const integration = {
      IntegrationHttpMethod: 'POST',
      Type: type,
    };

    // Valid integrations are:
    // * `HTTP` for integrating with an HTTP back end,
    // * `AWS` for any AWS service endpoints,
    // * `MOCK` for testing without actually invoking the back end,
    // * `HTTP_PROXY` for integrating with the HTTP proxy integration, or
    // * `AWS_PROXY` for integrating with the Lambda proxy integration type (the default)
    if (type === 'AWS' || type === 'AWS_PROXY') {
      Object.assign(integration, {
        Uri: {
          'Fn::Join': [
            '',
            [
              'arn:',
              { Ref: 'AWS::Partition' },
              ':apigateway:',
              { Ref: 'AWS::Region' },
              ':lambda:path/2015-03-31/functions/',
              ...[],
              { 'Fn::GetAtt': [lambdaLogicalId, 'Arn'] },
              ...(lambdaAliasName ? [':', lambdaAliasName] : []),
              '/invocations',
            ],
          ],
        },
      });
    } else if (type === 'HTTP' || type === 'HTTP_PROXY') {
      const integrationHttpMethod = (http.request && http.request.method) || http.method;
      Object.assign(integration, {
        Uri: http.request && http.request.uri,
        IntegrationHttpMethod: integrationHttpMethod.toUpperCase(),
      });
      if (http.connectionType) {
        Object.assign(integration, {
          ConnectionType: http.connectionType,
          ConnectionId: http.connectionId,
        });
      }
    } else if (type === 'MOCK') {
      // nothing to do but kept here for reference
    }

    if (type === 'AWS' || type === 'HTTP' || type === 'MOCK') {
      Object.assign(integration, {
        PassthroughBehavior: http.request && http.request.passThrough,
        ContentHandling: http.request && http.request.contentHandling,
        RequestTemplates: this.getIntegrationRequestTemplates(http, type === 'AWS'),
        IntegrationResponses: this.getIntegrationResponses(http),
      });
    }
    if (
      ((type === 'AWS' || type === 'HTTP' || type === 'HTTP_PROXY') &&
        http.request &&
        http.request.parameters &&
        Object.keys(http.request.parameters).length) ||
      http.async
    ) {
      Object.assign(integration, {
        RequestParameters: this.getIntegrationRequestParameters(http),
      });
    }

    return {
      Properties: {
        Integration: integration,
      },
    };
  },

  getIntegrationResponses(http) {
    const integrationResponses = [];

    if (http.response) {
      const integrationResponseHeaders = [];

      if (http.cors) {
        let origin = http.cors.origin;

        // TODO remove once "origins" config is deprecated
        if (http.cors.origins && http.cors.origins.length) {
          origin = http.cors.origins.join(',');
        }

        _.merge(integrationResponseHeaders, {
          'Access-Control-Allow-Origin': `'${origin}'`,
        });

        // Only set Access-Control-Allow-Credentials when explicitly allowed (omit if false)
        if (http.cors.allowCredentials) {
          integrationResponseHeaders['Access-Control-Allow-Credentials'] = 'true';
        }
      }

      if (http.response.headers) {
        _.merge(integrationResponseHeaders, http.response.headers);
      }

      _.forEach(http.response.statusCodes, (config, statusCode) => {
        const responseParameters = _.mapKeys(
          integrationResponseHeaders,
          (value, header) => `method.response.header.${header}`
        );

        const integrationResponse = {
          StatusCode: statusCode,
          SelectionPattern: config.pattern || '',
          ResponseParameters: responseParameters,
          ResponseTemplates: {},
          ContentHandling: statusCode.startsWith('2') ? http.response.contentHandling : undefined,
        };

        if (config.headers) {
          _.merge(
            integrationResponse.ResponseParameters,
            _.mapKeys(config.headers, (value, header) => `method.response.header.${header}`)
          );
        }

        if (http.response.template) {
          _.merge(integrationResponse.ResponseTemplates, {
            'application/json': http.response.template,
          });
        }

        if (config.template) {
          const template =
            typeof config.template === 'string'
              ? { 'application/json': config.template }
              : config.template;

          _.merge(integrationResponse.ResponseTemplates, template);
        }

        integrationResponses.push(integrationResponse);
      });
    }

    return integrationResponses;
  },

  getIntegrationRequestTemplates(http, useDefaults) {
    // default request templates
    const integrationRequestTemplates = {};

    // Only set defaults for AWS (lambda) integ
[... 1842 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/serverless__serverless-8159/repo; grep -rn "template" lib/plugins/aws/package/compile/events/apiGateway/index.js lib/plugins/aws/package/compile/events/apiGateway/lib/validate.js | head -40; grep -n "null\|ullish\|without.*template\|remov" lib/plugins/aws/package/compile/events/apiGateway/lib/method/index.test.js | head -30
```

tool result:

```
lib/plugins/aws/package/compile/events/apiGateway/lib/validate.js:502:      if (http.request.template && typeof http.request.template !== 'object') {
lib/plugins/aws/package/compile/events/apiGateway/lib/validate.js:552:    // for HTTP and MOCK integrations, where there is no default request template defined.
```

**tool call: Bash**

```bash
cd /work/serverless__serverless-8159/repo; sed -n 480,570p lib/plugins/aws/package/compile/events/apiGateway/lib/validate.js; grep -n "template" -A12 lib/plugins/aws/package/compile/events/apiGateway/index.js | head -60; grep -n -i "template" docs/providers/aws/events/apigateway.md | head -40
```

tool result:

```
          ' Supported connectionTyps are:',
          ' vpc-link.',
        ].join('');
        throw new this.serverless.classes.Error(errorMessage);
      }
      return normalizedConnectionType;
    }

    return null;
  },

  getRequest(http) {
    if (http.request) {
      const request = http.request;

      if (typeof http.request !== 'object') {
        const errorMessage = [
          'Request config must be provided as an object.',
          ' Please check the docs for more info.',
        ].join('');
        throw new this.serverless.classes.Error(errorMessage);
      }
      if (http.request.template && typeof http.request.template !== 'object') {
        const errorMessage = [
          'Template config must be provided as an object.',
          ' Please check the docs for more info.',
        ].join('');
        throw new this.serverless.classes.Error(errorMessage);
      }

      if (request.parameters) {
        request.parameters = this.getRequestParameters(request);
      }

      return request;
    }

    return {};
  },

  getRequestParameters(httpRequest) {
    const parameters = {};
    // only these locations are currently supported
    const locations = ['querystrings', 'paths', 'headers'];
    locations.forEach(location => {
      // strip the plural s
      const singular = location.substring(0, location.length - 1);
      _.forEach(httpRequest.parameters[location], (value, key) => {
        parameters[`method.request.${singular}.${key}`] = value;
      });
    });
    return parameters;
  },

  getRequestPassThrough(http) {
    const requestPassThroughBehaviors = ['NEVER', 'WHEN_NO_MATCH', 'WHEN_NO_TEMPLATES'];

    if (http.request.passThrough) {
      if (requestPassThroughBehaviors.indexOf(http.request.passThrough) === -1) {
        const errorMessage = [
          'Request passThrough "',
          http.request.passThrough,
          '" is not one of ',
          requestPassThroughBehaviors.join(', '),
        ].join('');
        throw new this.serverless.classes.Error(errorMessage);
      }

      return http.request.passThrough;
    }

    // Validate() sets the passThrough default to NEVER. This is inappropriate
    // for HTTP and MOCK integrations, where there is no default request template defined.
    const type = http.integration || 'AWS_PROXY';
    if (type === 'AWS') {
      return requestPassThroughBehaviors[0];
    } else if (type === 'HTTP' || type === 'MOCK') {
      return undefined;
    }

    return 'WHEN_NO_MATCH';
  },

  getResponse(http) {
    if (http.response) {
      const response = http.response;

      if (typeof response !== 'object') {
        const errorMessage = [
          'Response config must be provided as an object.',
          ' Please check the docs for more info.',
34:    - [Request templates](#request-templates)
35:      - [Default Request Templates](#default-request-templates)
36:      - [Custom Request Templates](#custom-request-templates)
40:      - [Custom Response Templates](#custom-response-templates)
280:Please note that since you can't send multiple values for [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin), this configuration uses a response template to check if the request origin matches one of your provided `origins` and overrides the header with the following code:
549:If you are creating the Cognito User Pool in the `resources` section of the same template, you can refer to the ARN using the `Fn::GetAtt` attribute from CloudFormation. To do so, you _must_ give your authorizer a name and specify a type of `COGNITO_USER_POOLS`:
931:### Request templates
933:#### Default Request Templates
935:Serverless ships with the following default request templates you can use out of the box:
940:Both templates give you access to the following properties you can access with the help of the `event` object:
953:#### Custom Request Templates
955:However you can define and use your own request templates as follows (you can even overwrite the default request templates
956:by defining a new request template for an existing content type):
968:            template:
973:**Note:** The templates are defined as plain text here. However you can also reference an external file with the help of the `${file(templatefile)}` syntax.
989:            template:
999:[API Gateway](https://serverless.com/amazon-api-gateway/) provides multiple ways to handle requests where the Content-Type header does not match any of the specified mapping templates. When this happens, the request payload will either be passed through the integration request _without transformation_ or rejected with a `415 - Unsupported Media Type`, depending on the configuration.
1020:| NEVER             | Never                                        | No templates defined or Content-Type does not match a defined template |
1021:| WHEN_NO_MATCH     | Content-Type does not match defined template | Never                                                                  |
1022:| WHEN_NO_TEMPLATES | No templates were defined                    | One or more templates defined, but Content-Type does not match         |
1029:- API Gateway docs refer to "WHEN_NO_TEMPLATE" (singular), but this will fail during creation as the actual value should be "WHEN_NO_TEMPLATES" (plural)
1033:Serverless lets you setup custom headers and a response template for your `http` event.
1058:#### Custom Response Templates
1060:Sometimes you'll want to define a custom response template API Gateway should use to transform your lambdas output.
1075:            template: $input.path('$')
1078:**Note:** The template is defined as plain text here. However you can also reference an external file with the help of
1079:the `${file(templatefile)}` syntax.
1122:You can override the defaults status codes supplied by Serverless. You can use this to change the default status code, add/remove status codes, or change the templates and headers used for
[... 1115 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/serverless__serverless-8159/repo; grep -rn -i "default.*template\|template.*default" lib test --include=*.js | grep -v node_modules | head -30
```

tool result:

```
(eval):1: no matches found: --include=*.js
```

**tool call: Grep**

```json
{
 "pattern": "(?i)default.*template|template.*default|request: \\{\\s*template",
 "path": "/work/serverless__serverless-8159/repo",
 "glob": "{lib,test}/**/*.js",
 "output_mode": "content"
}
```

tool result:

```
lib/plugins/aws/package/compile/events/apiGateway/lib/method/integration.js:5:const DEFAULT_COMMON_TEMPLATE = `
lib/plugins/aws/package/compile/events/apiGateway/lib/method/integration.js:198:  getIntegrationRequestTemplates(http, useDefaults) {
lib/plugins/aws/package/compile/events/apiGateway/lib/method/integration.js:199:    // default request templates
lib/plugins/aws/package/compile/events/apiGateway/lib/method/integration.js:205:        'application/json': this.DEFAULT_JSON_REQUEST_TEMPLATE,
lib/plugins/aws/package/compile/events/apiGateway/lib/method/integration.js:206:        'application/x-www-form-urlencoded': this.DEFAULT_FORM_URL_ENCODED_REQUEST_TEMPLATE,
lib/plugins/aws/package/compile/events/apiGateway/lib/method/integration.js:234:  DEFAULT_JSON_REQUEST_TEMPLATE: `
lib/plugins/aws/package/compile/events/apiGateway/lib/method/integration.js:237:    ${DEFAULT_COMMON_TEMPLATE}
lib/plugins/aws/package/compile/events/apiGateway/lib/method/integration.js:240:  DEFAULT_FORM_URL_ENCODED_REQUEST_TEMPLATE: `
lib/plugins/aws/package/compile/events/apiGateway/lib/method/integration.js:259:    ${DEFAULT_COMMON_TEMPLATE}
lib/plugins/aws/package/compile/events/apiGateway/lib/method/index.test.js:1251:    it('should setup a default "application/json" template', () => {
lib/plugins/aws/package/compile/events/apiGateway/lib/method/index.test.js:1279:    it('should setup a default "application/x-www-form-urlencoded" template', () => {
lib/plugins/aws/package/compile/events/apiGateway/lib/method/index.test.js:1438:    it('should be possible to overwrite default request templates', () => {
lib/plugins/aws/package/compile/events/apiGateway/lib/validate.js:552:    // for HTTP and MOCK integrations, where there is no default request template defined.
lib/plugins/aws/package/compile/functions/index.test.js:2878:            defaultIamRole = cfTemplate.Resources.IamRoleLambdaExecution;
lib/plugins/aws/package/compile/events/websockets/lib/api.js:34:    const defaultRoleResource = this.serverless.service.provider.compiledCloudFormationTemplate
test/integration-package/cloudformation.tests.js:54:  it('creates the correct default function resource in cfn template', () => {
test/integration-package/lambda-files.tests.js:23:  it('packages the default aws template correctly in the zip', () => {
test/integration-package/lambda-files.tests.js:31:  it('packages the default aws template with an npm dep correctly in the zip', () => {
```

**tool call: Bash**

```bash
cd /work/serverless__serverless-8159/repo; grep -rn "template" lib/plugins/aws/package/compile/events/apiGateway/index.js lib/plugins/aws/provider/*.js | head; sed -n 950,1000p docs/providers/aws/events/apigateway.md
```

tool result:

````
lib/plugins/aws/provider/awsProvider.js:541:  // to the cloudformation template for regions where acceleration is not supported (ie, govcloud)
- stageVariables
- requestPath

#### Custom Request Templates

However you can define and use your own request templates as follows (you can even overwrite the default request templates
by defining a new request template for an existing content type):

```yml
functions:
  create:
    handler: posts.create
    events:
      - http:
          method: get
          path: whatever
          integration: lambda
          request:
            template:
              text/xhtml: '{ "stage" : "$context.stage" }'
              application/json: '{ "httpMethod" : "$context.httpMethod" }'
```

**Note:** The templates are defined as plain text here. However you can also reference an external file with the help of the `${file(templatefile)}` syntax.

**Note 2:** In .yml, strings containing `:`, `{`, `}`, `[`, `]`, `,`, `&`, `*`, `#`, `?`, `|`, `-`, `<`, `>`, `=`, `!`, `%`, `@`, `` ` `` must be quoted.

If you want to map querystrings to the event object, you can use the `$input.params('hub.challenge')` syntax from API Gateway, as follows:

```yml
functions:
  create:
    handler: posts.create
    events:
      - http:
          method: get
          path: whatever
          integration: lambda
          request:
            template:
              application/json: '{ "foo" : "$input.params(''bar'')" }'
```

**Note:** Notice when using single-quoted strings, any single quote `'` inside its contents must be doubled (`''`) to escape it.
You can then access the query string `https://example.com/dev/whatever?bar=123` by `event.foo` in the lambda function.
If you want to spread a string into multiple lines, you can use the `>` or `|` syntax, but the following strings have to be all indented with the same amount, [read more about `>` syntax](http://stackoverflow.com/questions/3790454/in-yaml-how-do-i-break-a-string-over-multiple-lines).

#### Pass Through Behavior

[API Gateway](https://serverless.com/amazon-api-gateway/) provides multiple ways to handle requests where the Content-Type header does not match any of the specified mapping templates. When this happens, the request payload will either be passed through the integration request _without transformation_ or rejected with a `415 - Unsupported Media Type`, depending on the configuration.
````

**assistant:** I'll write a quick repro: an AWS integration where the user tries to drop the form-urlencoded template by setting it to `null`.

**tool call: Bash**

```bash
cd /work/serverless__serverless-8159/repo; cat > repro.js <<'EOF'
const m = require('./lib/plugins/aws/package/compile/events/apiGateway/lib/method/integration');
const r = m.getMethodIntegration({ integration: 'AWS', request: { template: { 'application/x-www-form-urlencoded': null } } }, { lambdaLogicalId: 'L' });
console.log(r.Properties.Integration.RequestTemplates);
const r2 = m.getMethodIntegration({ integration: 'AWS', request: { template: { 'application/json': null, 'application/x-www-form-urlencoded': null } } }, { lambdaLogicalId: 'L' });
console.log(r2.Properties.Integration.RequestTemplates);
EOF
../bin/envrun 'node repro.js' | grep -v '^ '
```

tool result:

```
{
}
{ 'application/json': null, 'application/x-www-form-urlencoded': null }
```

**assistant:** Confirmed: there's no way to drop a default — `null` just ends up emitted as a template value. Fix: treat `null` as "remove this content type".

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/serverless__serverless-8159/repo/lib/plugins/aws/package/compile/events/apiGateway/lib/method/integration.js",
 "old_string": "      Object.assign(integrationRequestTemplates, http.request.template);\n    }",
 "new_string": "      Object.assign(integrationRequestTemplates, http.request.template);\n    }\n\n    // remove templates explicitly set to null (allows removal of default templates)\n    for (const contentType of Object.keys(integrationRequestTemplates)) {\n      if (integrationRequestTemplates[contentType] == null) {\n        delete integrationRequestTemplates[contentType];\n      }\n    }"
}
```

tool result:

```
The file /work/serverless__serverless-8159/repo/lib/plugins/aws/package/compile/events/apiGateway/lib/method/integration.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Edit**

````json
{
 "replace_all": false,
 "file_path": "/work/serverless__serverless-8159/repo/docs/providers/aws/events/apigateway.md",
 "old_string": "**Note:** The templates are defined as plain text here. However you can also reference an external file with the help of the `${file(templatefile)}` syntax.\n\n**Note 2:**",
 "new_string": "**Note:** The templates are defined as plain text here. However you can also reference an external file with the help of the `${file(templatefile)}` syntax.\n\nYou can also remove a default request template by setting it to `null`:\n\n```yml\nfunctions:\n  create:\n    handler: posts.create\n    events:\n      - http:\n          method: post\n          path: whatever\n          integration: lambda\n          request:\n            template:\n              application/x-www-form-urlencoded: null\n```\n\n**Note 2:**"
}
````

tool result:

```
The file /work/serverless__serverless-8159/repo/docs/providers/aws/events/apigateway.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
cd /work/serverless__serverless-8159/repo; ../bin/envrun 'node repro.js' | grep -v '^ '; rm repro.js; ../bin/envrun 'npx mocha lib/plugins/aws/package/compile/events/apiGateway/lib/method/index.test.js lib/plugins/aws/package/compile/events/apiGateway/lib/validate.test.js 2>&1 | tail -15'; git status --short
```

tool result:

```
{
}
undefined

    ✓ should not show a warning message when using request.parameter with LAMBDA-PROXY
    ✓ should remove non-parameter request/response config with LAMBDA-PROXY
    ✓ should throw an error when an invalid integration type was provided
    ✓ should accept a valid passThrough
    ✓ should default pass through to NEVER for lambda
    ✓ should not set default pass through http
    ✓ should support HTTP_PROXY integration with VPC_LINK connection type
    ✓ should throw an error when connectionId is not provided with VPC_LINK
    ✓ should throw an error when connectionType is invalid
    ✓ should reject if http event is present and stage contains invalid chars
    ✓ should set default statusCodes to response for lambda by default


  131 passing (2s)


 M Dockerfile
 M docs/providers/aws/events/apigateway.md
 M lib/plugins/aws/package/compile/events/apiGateway/lib/method/integration.js
```

**tool call: Bash**

```bash
cd /work/serverless__serverless-8159/repo; git diff --stat Dockerfile
```

tool result:

```
 Dockerfile | 17 ++++-------------
 1 file changed, 4 insertions(+), 13 deletions(-)
```

**assistant:** You can now remove a default request mapping template by setting its content type to `null` under `request.template`:

```yml
request:
  template:
    application/x-www-form-urlencoded: null
```

With that config, only `application/json` gets a template, so API Gateway's generated swagger won't list `application/x-www-form-urlencoded` under `consumes`.

**What changed**
- In `lib/plugins/aws/package/compile/events/apiGateway/lib/method/integration.js`, `getIntegrationRequestTemplates` merges the user's templates over the defaults as before. Then it drops any content type whose value is `null`. If every template is removed, `RequestTemplates` is left off the integration entirely.
- In `docs/providers/aws/events/apigateway.md`, the "Custom Request Templates" section now has a short example of removing a default this way.

Existing configs behave the same: overriding or adding templates still works. I picked `null` as the way to opt out, rather than skipping the defaults whenever custom templates are given, because the second option would break existing setups that rely on merging.

**Verification**
- **Before the fix:** the `null` value was passed straight through as a template value.
- **After:** setting one content type to `null` leaves only the other. Setting both to `null` leaves no `RequestTemplates` at all.
- **Tests:** the existing method and validate tests for API Gateway pass (131 passing). I deleted the repro script afterwards.

`git status` also shows a modified `Dockerfile`. I didn't change it and left it alone; it was probably modified by the environment setup.

_session end: success, turns 12, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.37 s: node repro.js
- `rc=0` 0.49 s: node repro.js
- `rc=0` 6.61 s: npx mocha lib/plugins/aws/package/compile/events/apiGateway/lib/method/index.test.js lib/plugins/aws/package/compile/events/apiGateway/lib/validate.test.js 2>&1 | tail -15
