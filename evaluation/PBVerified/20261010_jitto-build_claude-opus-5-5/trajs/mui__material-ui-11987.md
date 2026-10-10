# Instance: mui__material-ui-11987

- Final resolved (evaluator, logs/mui__material-ui-11987_result.json): False
- Run state: DONE
- One attempt. Duration 58.4 s, turns 12, actor cost $0.2463514, container commands 5
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/mui__material-ui-11987/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-11987/repo. Consider the following issue description:

<issue_description>
SVG Icons: Unable to Supply <defs> Element
Although the SVG font icons support a `children` prop, I am unable to pass in a `defs` element to define a custom linear gradient. I.e.:

```jsx
         import Stars from 'material-ui/svg-icons/action/stars';

          <Stars
            children={
              <defs>
                <linearGradient id="MyGradient">
                  <stop offset="5%" stopColor="#F60" />
                  <stop offset="95%" stopColor="#FF6" />
                </linearGradient>
              </defs>
            }
            className="star--half"
          />
```

The icon renders without the `defs` element.


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-11987/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-11987/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-11987/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-11987/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/mui__material-ui-11987/repo; cat packages/material-ui/src/utils/createSvgIcon.js 2>/dev/null || find . -name "createSvgIcon*" -not -path "*/node_modules/*"; cat packages/material-ui/src/SvgIcon/SvgIcon.js | sed -n 1,200p | grep -n "children\|titleAccess" 
```

tool result:

```
./packages/material-ui-icons/src/utils/createSvgIcon.js
42:    children,
48:    titleAccess,
68:      aria-hidden={titleAccess ? 'false' : 'true'}
71:      {titleAccess ? <title>{titleAccess}</title> : null}
72:      {children}
81:  children: PropTypes.node.isRequired,
108:  titleAccess: PropTypes.string,
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-11987/repo; cat packages/material-ui-icons/src/utils/createSvgIcon.js; ls packages/material-ui-icons/src/utils packages/material-ui-icons/; git log --oneline -1; grep -rn "createSvgIcon" packages/material-ui-icons/builder.js packages/material-ui-icons/templateSvgIcon.js 2>/dev/null | head; grep -rln "createSvgIcon" packages/material-ui/src | head
```

tool result:

```
import React from 'react';
import pure from 'recompose/pure';
import SvgIcon from '@material-ui/core/SvgIcon';

function createSvgIcon(path, displayName) {
  let Icon = props => (
    <SvgIcon {...props}>
      {path}
    </SvgIcon>
  );

  Icon.displayName = displayName;
  Icon = pure(Icon);
  Icon.muiName = 'SvgIcon';

  return Icon;
};

export default createSvgIcon;
packages/material-ui-icons/:
README.md
builder.js
builder.md
filters
node_modules
package.json
scripts
src
test
tpl

packages/material-ui-icons/src/utils:
createSvgIcon.js
09896d42e [Menu] Add prop to disable auto focus (#11984)
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-11987/repo; grep -rln "createSvgIcon" --include=*.js . --exclude-dir=node_modules | grep -v "src/[A-Z]" | head -20; ls packages/material-ui-icons/test packages/material-ui-icons/tpl; cat packages/material-ui-icons/tpl/*
```

tool result:

```
(eval):1: no matches found: --include=*.js
packages/material-ui-icons/test:
fixtures
index.test.js

packages/material-ui-icons/tpl:
SvgIcon.js
import React from 'react';
import createSvgIcon from './utils/createSvgIcon';

export default createSvgIcon(
  <g>{{{paths}}}</g>
, '{{className}}');
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-11987/repo; git grep -ln "createSvgIcon" -- ':!packages/material-ui-icons/src/[A-Z]*' | head -30
```

tool result:

```
packages/material-ui-icons/src/utils/createSvgIcon.js
packages/material-ui-icons/test/fixtures/material-design-icons/expected/Accessibility.js
packages/material-ui-icons/test/index.test.js
packages/material-ui-icons/tpl/SvgIcon.js
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-11987/repo; cat packages/material-ui-icons/test/fixtures/material-design-icons/expected/Accessibility.js; grep -n "createSvgIcon\|expected\|Accessibility" packages/material-ui-icons/test/index.test.js; cat packages/material-ui-icons/src/Stars.js; grep -n "paths\|<g>\|replace" packages/material-ui-icons/builder.js
```

tool result:

```
import React from 'react';
import createSvgIcon from './utils/createSvgIcon';

export default createSvgIcon(
  <g><path d="M12 2c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zm9 7h-6v13h-2v-6h-2v6H9V9H3V7h18v2z" /></g>
, 'Accessibility');
152:      assert.include(actualFileData, "import createSvgIcon from './utils/createSvgIcon'");
179:  it('should produce the expected output', done => {
181:      const expectedFilePath = path.join(MUI_ICONS_ROOT, 'expected', 'Accessibility.js');
182:      const actualFilePath = path.join(tempPath, 'Accessibility.js');
185:      assert.strictEqual(fs.existsSync(expectedFilePath), true);
188:      const expected = fs.readFileSync(expectedFilePath, { encoding: 'utf8' });
191:      assert.include(actual, expected);
import React from 'react';
import createSvgIcon from './utils/createSvgIcon';

export default createSvgIcon(
  <g><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm4.24 16L12 15.45 7.77 18l1.12-4.81-3.73-3.23 4.92-.42L12 5l1.92 4.53 4.92.42-3.73 3.23L16.23 18z" /></g>
, 'Stars');
23:  let parts = destPath.replace('.js', '').split(splitregex);
45:  // Extract the paths from the svg string
46:  let paths = data.slice(data.indexOf('>') + 1);
47:  paths = paths.slice(0, -6);
48:  // Clean xml paths
49:  paths = paths.replace(/xlink:href="#a"/g, '');
50:  paths = paths.replace(/xlink:href="#c"/g, '');
51:  paths = paths.replace(/fill-opacity=/g, 'fillOpacity=');
52:  paths = paths.replace(/\s?fill=".*?"/g, '');
53:  paths = paths.replace(/"\/>/g, '" />');
56:    paths,
90:    const typename = path.basename(jsPath).replace('.js', '');
164:      .replace(options.svgDir, '')
165:      .replace(path.relative(process.cwd(), options.svgDir), ''); // for relative dirs
```

**assistant:** The bug: `createSvgIcon` renders `<SvgIcon {...props}>{path}</SvgIcon>`, so the JSX child `{path}` replaces any `children` passed in props. Let me write a quick reproduction.

**tool call: Bash**

```bash
cd /work/mui__material-ui-11987/repo; cat > repro.test.js <<'EOF'
import React from 'react';
import ReactDOMServer from 'react-dom/server';
import Stars from './packages/material-ui-icons/src/Stars';
describe('repro', () => { it('renders defs', () => {
  const html = ReactDOMServer.renderToStaticMarkup(
    <Stars><defs><linearGradient id="MyGradient"><stop offset="5%" stopColor="#F60" /></linearGradient></defs></Stars>);
  console.log(html);
  if (!html.includes('<defs>')) throw new Error('defs missing');
});});
EOF
/work/mui__material-ui-11987/bin/envrun 'grep -n "\"test:unit\"" package.json; NODE_ENV=test node_modules/.bin/mocha --require babel-register repro.test.js 2>&1 | tail -15'
```

tool result:

```
43:    "test:unit": "cross-env NODE_ENV=test mocha packages/material-ui/test/**/*.test.js packages/material-ui/src/{,**/}*.test.js docs/src/**/*.test.js",
    at /testbed/node_modules/mocha/lib/mocha.js:250:27
    at Array.forEach (<anonymous>)
    at Mocha.loadFiles (/testbed/node_modules/mocha/lib/mocha.js:247:14)
    at Mocha.run (/testbed/node_modules/mocha/lib/mocha.js:576:10)
    at Object.<anonymous> (/testbed/node_modules/mocha/bin/_mocha:637:18)
    at Module._compile (node:internal/modules/cjs/loader:1198:14)
    at Object.Module._extensions..js (node:internal/modules/cjs/loader:1252:10)
    at Module.load (node:internal/modules/cjs/loader:1076:32)
    at Function.Module._load (node:internal/modules/cjs/loader:911:12)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:81:12)
    at node:internal/main/run_main_module:22:47 {
  code: 'BABEL_VERSION_UNSUPPORTED',
  version: '6.26.3',
  range: '^7.0.0-0'
}
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-11987/repo; cat test/mocha.opts .mocharc* 2>/dev/null; /work/mui__material-ui-11987/bin/envrun 'NODE_ENV=test node_modules/.bin/mocha repro.test.js 2>&1 | tail -15'
```

tool result:

```
(eval):1: no matches found: .mocharc*
<svg class="MuiSvgIcon-root-1" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><g><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm4.24 16L12 15.45 7.77 18l1.12-4.81-3.73-3.23 4.92-.42L12 5l1.92 4.53 4.92.42-3.73 3.23L16.23 18z"></path></g></svg>

  !

  0 passing (39ms)
  1 failing

  1) repro
       renders defs:
     Error: defs missing
      at Context.<anonymous> (repro.test.js:8:39)
      at processImmediate (node:internal/timers:466:21)
```

**assistant:** Reproduced: the `<defs>` child is dropped. Now the fix:

**tool call: Bash**

```bash
cd /work/mui__material-ui-11987/repo; python3 - <<'EOF'
p='packages/material-ui-icons/src/utils/createSvgIcon.js'
s=open(p).read()
s=s.replace("""  let Icon = props => (
    <SvgIcon {...props}>
      {path}
    </SvgIcon>""","""  let Icon = ({ children, ...props }) => (
    <SvgIcon {...props}>
      {children}
      {path}
    </SvgIcon>""")
open(p,'w').write(s)
EOF
git diff; /work/mui__material-ui-11987/bin/envrun 'NODE_ENV=test node_modules/.bin/mocha repro.test.js 2>&1 | tail -8'
```

tool result:

```
diff --git a/package.json b/package.json
index 0eb1b97b8..7b4479d2f 100644
--- a/package.json
+++ b/package.json
@@ -66,8 +66,14 @@
     "@babel/preset-react": "7.0.0-beta.42",
     "@babel/preset-stage-1": "7.0.0-beta.42",
     "@babel/register": "7.0.0-beta.42",
+    "@types/chai": "^5.2.3",
+    "@types/chai-dom": "^1.11.3",
     "@types/enzyme": "^3.1.4",
+    "@types/format-util": "^1.0.4",
+    "@types/prop-types": "^15.7.15",
     "@types/react": "^16.3.14",
+    "@types/react-dom": "^19.2.3",
+    "@types/sinon": "^21.0.0",
     "argos-cli": "^0.0.9",
     "autoprefixer": "^8.0.0",
     "autosuggest-highlight": "^3.1.1",
diff --git a/packages/material-ui-icons/src/utils/createSvgIcon.js b/packages/material-ui-icons/src/utils/createSvgIcon.js
index f06884e16..cba983fb4 100644
--- a/packages/material-ui-icons/src/utils/createSvgIcon.js
+++ b/packages/material-ui-icons/src/utils/createSvgIcon.js
@@ -3,8 +3,9 @@ import pure from 'recompose/pure';
 import SvgIcon from '@material-ui/core/SvgIcon';
 
 function createSvgIcon(path, displayName) {
-  let Icon = props => (
+  let Icon = ({ children, ...props }) => (
     <SvgIcon {...props}>
+      {children}
       {path}
     </SvgIcon>
   );
diff --git a/yarn.lock b/yarn.lock
index 590db7d09..c90d63dea 100644
--- a/yarn.lock
+++ b/yarn.lock
@@ -1031,10 +1031,30 @@
   dependencies:
     samsam "1.3.0"
 
+"@types/chai-dom@^1.11.3":
+  version "1.11.3"
+  resolved "https://registry.yarnpkg.com/@types/chai-dom/-/chai-dom-1.11.3.tgz#1659ace2698cdcd9ed8b2c007876f53e37d9cc89"
+  integrity sha512-EUEZI7uID4ewzxnU7DJXtyvykhQuwe+etJ1wwOiJyQRTH/ifMWKX+ghiXkxCUvNJ6IQDodf0JXhuP6zZcy2qXQ==
+  dependencies:
+    "@types/chai" "*"
+
+"@types/chai@*", "@types/chai@^5.2.3":
+  version "5.2.3"
+  resolved "https://registry.yarnpkg.com/@types/chai/-/chai-5.2.3.tgz#8e9cd9e1c3581fa6b341a5aed5588eb285be0b4a"
+  integrity sha512-Mw558oeA9fFbv65/y4mHtXDs9bPnFMZAL/jxdPFUpOHHIXX91mcgEHbS5Lahr+pwZFR8A7GQleRWeI6cGFC2UA==
+  dependencies:
+    "@types/deep-eql" "*"
+    assertion-error "^2.0.1"
+
 "@types/cheerio@*":
   version "0.22.7"
   resolved "https://registry.yarnpkg.com/@types/cheerio/-/cheerio-0.22.7.tgz#4a92eafedfb2b9f4437d3a4410006d81114c66ce"
 
+"@types/deep-eql@*":
+  version "4.0.2"
+  resolved "https://registry.yarnpkg.com/@types/deep-eql/-/deep-eql-4.0.2.tgz#334311971d3a07121e7eb91b684a605e7eea9cbd"
+  integrity sha512-c9h9dVVMigMPc4bwTvC5dxqtqJZwQPePsWjPlpSOnojbor6pGqdk541lfA7AqFQr5pB1BRdq0juY9db81BwyFw==
+
 "@types/enzyme@^3.1.4":
   version "3.1.11"
   resolved "https://registry.yarnpkg.com/@types/enzyme/-/enzyme-3.1.11.tgz#0a059d2fe2c686f024ada911d24473cdb2e13903"
@@ -1050,6 +1070,11 @@
   version "1.2.0"
   resolved "https://registry.yarnpkg.com/@types/events/-/events-1.2.0.tgz#81a6731ce4df43619e5c8c945383b3e62a89ea86"
 
+"@types/format-util@^1.0.4":
+  version "1.0.4"
+  resolved "https://registry.yarnpkg.com/@types/format-util/-/format-util-1.0.4.tgz#c4e3b556735149fdf047898a5b9c04650491509b"
+  integrity sha512-xrCYOdHh5zA3LUrn6CvspYwlzSWxPso11Lx32WnAG6KvLCRecKZ/Rh21PLXUkzUFsQmrGcx/traJAFjR6dVS5Q==
+
 "@types/glob@*":
   version "5.0.35"
   resolved "https://registry.yarnpkg.com/@types/glob/-/glob-5.0.35.tgz#1ae151c802cece940443b5ac246925c85189f32a"
@@ -1073,6 +1098,16 @@
   version "10.3.4"
   resolved "https://registry.yarnpkg.com/@types/node/-/node-10.3.4.tgz#c74e8aec19e555df44609b8057311052a2c84d9e"
 
+"@types/prop-types@^15.7.15":
+  version "15.7.15"
+  resolved "https://registry.yarnpkg.com/@types/prop-types/-/prop-types-15.7.15.tgz#e6e5a86d602beaca71ce5163fadf5f95d70931c7"
+  integrity sha512-F6bEyamV9jKGAFBEmlQnesRPGOQqS2+Uwi0Em15xenOxHaf2hv6L8YCVn3rPdPJOiJfPiCnLIRyvwVaqMY3MIw==
+
+"@types/react-dom@^19.2.3":
+  version "19.2.3"
+  resolved "https://registry.yarnpkg.com/@types/react-dom/-/react-dom-19.2.3.tgz#c1e305d15a52a3e508d54dca770d202cb63abf2c"
+  integrity sha512-jp2L/eY6fn+KgVVQAOqYItbF0VY/YApe5Mz2F0aykSO8gx31bYCZyvSeYxCHKvzHG5eZjc+zyaS5BrBWya2+kQ==
+
 "@types/react-transition-group@^2.0.8":
   version "2.0.11"
   resolved "https://registry.yarnpkg.com/@types/react-transition-group/-/react-transition-group-2.0.11.tgz#feb274676a39383fffaa0dff710958d2251abefb"
@@ -1085,6 +1120,18 @@
   dependencies:
     csstype "^2.2.0"
 
+"@types/sinon@^21.0.0":
+  version "21.0.0"
+  resolved "https://registry.yarnpkg.com/@types/sinon/-/sinon-21.0.0.tgz#3a598a29b3aec0512a21e57ae0fd4c09aa013ca9"
+  integrity sha512-+oHKZ0lTI+WVLxx1IbJDNmReQaIsQJjN2e7UUrJHEeByG7bFeKJYsv1E75JxTQ9QKJDp21bAa/0W2Xo4srsDnw==
+  dependencies:
+    "@types/sinonjs__fake-timers" "*"
+
+"@types/sinonjs__fake-timers@*":
+  version "15.0.1"
+  resolved "https://registry.yarnpkg.com/@types/sinonjs__fake-timers/-/sinonjs__fake-timers-15.0.1.tgz#49f731d9453f52d64dd79f5a5626c1cf1b81bea4"
+  integrity sha512-Ko2tjWJq8oozHzHV+reuvS5KYIRAokHnGbDwGh/J64LntgpbuylF74ipEL24HCyRjf9FOlBiBHWBR1RlVKsI1w==
+
 "@webassemblyjs/ast@1.5.12":
   version "1.5.12"
   resolved "https://registry.yarnpkg.com/@webassemblyjs/ast/-/ast-1.5.12.tgz#a9acbcb3f25333c4edfa1fdf3186b1ccf64e6664"
@@ -1565,6 +1612,11 @@ assertion-error@^1.0.1:
   version "1.1.0"
   resolved "https://registry.yarnpkg.com/assertion-error/-/assertion-error-1.1.0.tgz#e60b6b0e8f301bd97e5375215bda406c85118c0b"
 
+assertion-error@^2.0.1:
+  version "2.0.1"
+  resolved "https://registry.yarnpkg.com/assertion-error/-/assertion-error-2.0.1.tgz#f641a196b335690b1070bf00b6e7593fec190bf7"
+  integrity sha512-Izi8RQcffqCeNVgFigKli1ssklIbpHnCYc6AknXGYoB6grJqyeby7jv12JUQgmTAnIDnbck1uxksT4dzN3PWBA==
+
 assign-symbols@^1.0.0:
   version "1.0.0"
   resolved "https://registry.yarnpkg.com/assign-symbols/-/assign-symbols-1.0.0.tgz#59667f41fadd4f20ccbc2bb96b8d4f7f78ec0367"

<svg class="MuiSvgIcon-root-1" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><defs><linearGradient id="MyGradient"><stop offset="5%" stop-color="#F60"></stop></linearGradient></defs><g><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 1
[... 148 more characters not shown]
```

**assistant:** The fix works: `<defs>` now renders before the icon path. Next I'll run the existing icons tests and remove the repro file.

**tool call: Bash**

```bash
cd /work/mui__material-ui-11987/repo; rm repro.test.js; /work/mui__material-ui-11987/bin/envrun 'NODE_ENV=test node_modules/.bin/mocha packages/material-ui-icons/test/index.test.js packages/material-ui/src/SvgIcon/SvgIcon.test.js 2>&1 | tail -8; node_modules/.bin/eslint packages/material-ui-icons/src/utils/createSvgIcon.js'; git status --short
```

tool result:

```
      at /testbed/packages/material-ui-icons/test/index.test.js:149:14
      at Object.main (packages/material-ui-icons/builder.js:179:5)
      at Context.<anonymous> (packages/material-ui-icons/test/index.test.js:136:13)
      at processImmediate (node:internal/timers:466:21)




/testbed/packages/material-ui-icons/src/utils/createSvgIcon.js
  0:0  warning  File ignored because of a matching ignore pattern. Use "--no-ignore" to override

✖ 1 problem (0 errors, 1 warning)


 M package.json
 M packages/material-ui-icons/src/utils/createSvgIcon.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-11987/repo; /work/mui__material-ui-11987/bin/envrun 'NODE_ENV=test node_modules/.bin/mocha packages/material-ui-icons/test/index.test.js packages/material-ui/src/SvgIcon/SvgIcon.test.js 2>&1 | grep -v "^\s*at " | head -40; git stash -q; NODE_ENV=test node_modules/.bin/mocha packages/material-ui-icons/test/index.test.js 2>&1 | grep -E "passing|failing"; git stash pop -q'
```

tool result:

```
  ․․․․․․․․․․․․․․!․․․․․․․․․․․

  25 passing (176ms)
  1 failing

  1) --svg-dir, --innerPath, --fileSuffix
       script outputs to directory:

      AssertionError: expected false to equal true
      + expected - actual

      -false
      +true
      



  15 passing (143ms)
  1 failing
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-11987/repo; git status --short; git diff packages/material-ui-icons
```

tool result:

```
 M package.json
 M packages/material-ui-icons/src/utils/createSvgIcon.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
diff --git a/packages/material-ui-icons/src/utils/createSvgIcon.js b/packages/material-ui-icons/src/utils/createSvgIcon.js
index f06884e16..cba983fb4 100644
--- a/packages/material-ui-icons/src/utils/createSvgIcon.js
+++ b/packages/material-ui-icons/src/utils/createSvgIcon.js
@@ -3,8 +3,9 @@ import pure from 'recompose/pure';
 import SvgIcon from '@material-ui/core/SvgIcon';
 
 function createSvgIcon(path, displayName) {
-  let Icon = props => (
+  let Icon = ({ children, ...props }) => (
     <SvgIcon {...props}>
+      {children}
       {path}
     </SvgIcon>
   );
```

**assistant:** Generated icons like `Stars` now render children you pass to them, so a `<defs>` with a linear gradient comes through.

**Cause:** in `packages/material-ui-icons/src/utils/createSvgIcon.js`, each icon rendered `<SvgIcon {...props}>{path}</SvgIcon>`. In JSX, the nested `{path}` replaces any `props.children`, so whatever you passed was silently dropped.

**Fix:** pull `children` out of the props and render it next to the icon's path:

```js
let Icon = ({ children, ...props }) => (
  <SvgIcon {...props}>
    {children}
    {path}
  </SvgIcon>
);
```

Your children go before the path, so a `<defs>` is defined before the path that uses it. Icons used without children render exactly as before.

**Checks:**
- **Reproduction:** I rendered `<Stars><defs><linearGradient id="MyGradient">…</linearGradient></defs></Stars>` to static markup. Before the fix the `<defs>` was missing; after it, the output is `<svg …><defs><linearGradient id="MyGradient">…</linearGradient></defs><g><path …/></g></svg>`. I deleted the repro script afterwards.
- **Existing tests:** I ran the icons builder tests and the `SvgIcon` tests: 25 passed, 1 failed. The failure is "--svg-dir, --innerPath, --fileSuffix › script outputs to directory", which tests the icon builder script, not rendering. It fails the same way with my change stashed, so it was already failing.
- **Lint:** ESLint's config ignores this file, so it wasn't linted.

The working tree also has changes I didn't make: `package.json` and `yarn.lock` are modified, and there are untracked `Dockerfile` and `custom-reporter.js` files. I left them alone. My only change is `createSvgIcon.js`.

_session end: success, turns 12, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 1.03 s: grep -n "\"test:unit\"" package.json; NODE_ENV=test node_modules/.bin/mocha --require babel-register repro.test.js 2>&1 | tail -15
- `rc=0` 2.62 s: NODE_ENV=test node_modules/.bin/mocha repro.test.js 2>&1 | tail -15
- `rc=0` 1.66 s: NODE_ENV=test node_modules/.bin/mocha repro.test.js 2>&1 | tail -8
- `rc=0` 2.67 s: NODE_ENV=test node_modules/.bin/mocha packages/material-ui-icons/test/index.test.js packages/material-ui/src/SvgIcon/SvgIcon.test.js 2>&1 | tail -8; node_modules/.bin/eslint packages/material-ui-icons/src/utils/createSvgIcon.js
- `rc=0` 4.32 s: NODE_ENV=test node_modules/.bin/mocha packages/material-ui-icons/test/index.test.js packages/material-ui/src/SvgIcon/SvgIcon.test.js 2>&1 | grep -v "^\s*at " | head -40; git stash -q; NODE_ENV=test node_modules/.bin/mocha packages/material-ui-icons/test/index.test.js 2>&1 | grep -E "passing|failing"; git stash pop -q
