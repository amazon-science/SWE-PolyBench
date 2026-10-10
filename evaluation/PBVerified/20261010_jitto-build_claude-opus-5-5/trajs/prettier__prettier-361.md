# Instance: prettier__prettier-361

- Final resolved (evaluator, logs/prettier__prettier-361_result.json): True
- Run state: DONE
- One attempt. Duration 36.0 s, turns 9, actor cost $0.1504924, container commands 3
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/prettier__prettier-361/repo
</uploaded_files>
I've uploaded a JavaScript code repository in the directory /work/prettier__prettier-361/repo. Consider the following issue description:

<issue_description>
Export extension syntax not formatted correctly
Code using the [export extensions transform](https://babeljs.io/docs/plugins/transform-export-extensions/) is not formatted correctly.

When running prettier on one of my projects, the following:

```js
export reducer from './reducer'
```

was formatted as:

```js
export { reducer } from './reducer';
```

Note the addition of the curly braces, which changes the semantics of the `export` statement.

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/prettier__prettier-361/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/prettier__prettier-361/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/prettier__prettier-361/bin/envrun 'git status --short && ls'
Edits you make under /work/prettier__prettier-361/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
grep -n "ExportNamespaceSpecifier\|ExportDefaultSpecifier\|function printExportDeclaration" -A3 src/printer.js | head -60
```

tool result:

```
387:    case "ExportNamespaceSpecifier":
388-      return concat([ "* as ", path.call(print, "exported") ]);
389:    case "ExportDefaultSpecifier":
390-      return path.call(print, "exported");
391-    case "ImportDeclaration":
392-      parts.push("import ");
--
1815:function printExportDeclaration(path, options, print) {
1816-  var decl = path.getValue();
1817-  var parts = [ "export " ];
1818-
```

**tool call: Bash**

```bash
sed -n 1815,1880p src/printer.js; sed -n 391,440p src/printer.js
```

tool result:

```
function printExportDeclaration(path, options, print) {
  var decl = path.getValue();
  var parts = [ "export " ];

  namedTypes.Declaration.assert(decl);

  if (decl["default"] || decl.type === "ExportDefaultDeclaration") {
    parts.push("default ");
  }

  if (decl.declaration) {
    parts.push(path.call(print, "declaration"));

    if (
      decl.type === "ExportDefaultDeclaration" &&
        (decl.declaration.type !== "ClassDeclaration" &&
          decl.declaration.type !== "FunctionDeclaration" &&
          decl.declaration.type !== "FunctionExpression")
    ) {
      parts.push(";");
    }
  } else {
    if (decl.specifiers && decl.specifiers.length > 0) {
      if (
        decl.specifiers.length === 1 &&
          decl.specifiers[0].type === "ExportBatchSpecifier"
      ) {
        parts.push("*");
      } else {
        parts.push(
          decl.exportKind === "type" ? "type " : "",
          multilineGroup(
            concat([
              "{",
              indent(
                options.tabWidth,
                concat([
                  options.bracketSpacing ? line : softline,
                  join(concat([ ",", line ]), path.map(print, "specifiers"))
                ])
              ),
              ifBreak(options.trailingComma ? "," : ""),
              options.bracketSpacing ? line : softline,
              "}"
            ])
          )
        );
      }
    } else {
      parts.push("{}");
    }

    if (decl.source) {
      parts.push(" from ", path.call(print, "source"));
    }

    parts.push(";");
  }

  return concat(parts);
}

function printFlowDeclaration(path, parts) {
  var parentExportDecl = util.getParentExportDeclaration(path);

  if (parentExportDecl) {
    case "ImportDeclaration":
      parts.push("import ");

      if (n.importKind && n.importKind !== "value") {
        parts.push(n.importKind + " ");
      }

      if (n.specifiers && n.specifiers.length > 0) {
        var standalones = [];
        var grouped = [];

        path.each(
          function(specifierPath) {
            var value = specifierPath.getValue();
            if (
              namedTypes.ImportDefaultSpecifier.check(value) ||
                namedTypes.ImportNamespaceSpecifier.check(value)
            ) {
              standalones.push(print(specifierPath));
            } else {
              grouped.push(print(specifierPath));
            }
          },
          "specifiers"
        );

        assert.ok(standalones.length <= 1);

        if (standalones.length > 0) {
          parts.push(standalones[0]);
        }

        if (standalones.length > 0 && grouped.length > 0) {
          parts.push(", ");
        }

        if (grouped.length > 0) {
          parts.push(
            multilineGroup(
              concat([
                "{",
                indent(
                  options.tabWidth,
                  concat([
                    options.bracketSpacing ? line : softline,
                    join(concat([ ",", line ]), grouped)
                  ])
                ),
                ifBreak(options.trailingComma ? "," : ""),
                options.bracketSpacing ? line : softline,
```

**tool call: Bash**

```bash
grep -rln "export .* from\b" tests --include=*.snap | head; ls tests | grep -i export; git log --oneline -1
```

tool result:

```
(eval):1: no matches found: --include=*.snap
declare_export
declare_module_exports
esproposal_export_star_as.enable
esproposal_export_star_as.ignore
export
export_default
export_type
poly_class_export
237e6f4 Use a Symbol instead of the private dep (#359)
```

**tool call: Bash**

```bash
ls tests/export tests/esproposal_export_star_as.enable; cat tests/esproposal_export_star_as.enable/*.js tests/export/*.js 2>/dev/null | head -40; cat tests/export/jsfmt.spec.js 2>/dev/null
```

tool result:

```
tests/esproposal_export_star_as.enable:
__snapshots__
dest.js
jsfmt.spec.js
source.js

tests/export:
__snapshots__
bracket.js
empty.js
jsfmt.spec.js
// @flow

import {source} from "./test";

var a: number = source.num;
var b: string = source.num; // Error: num ~> string

var c: string = source.str;
var d: number = source.str; // Error: num ~> string
run_spec(__dirname);
// @flow

export var str = 'asdf';
export var num = 42;
export {
  runTaskForChanged,
  description,
  someOtherLabel,
  thatMakes,
  itGo,
  multiLine,
  andMore,
  soWeCanGetItTo80Columns
};
export {fitsIn, oneLine};
export {};
export {} from ".";
run_spec(__dirname);
run_spec(__dirname, {bracketSpacing: false});
run_spec(__dirname);
run_spec(__dirname, {bracketSpacing: false});
```

**assistant:** Reproduce:

**tool call: Bash**

```bash
cd /tmp && cat > /work/prettier__prettier-361/repo/repro.js <<'EOF'
const p = require("./");
for (const s of [
  "export reducer from './reducer'",
  "export * as ns from 'mod'",
  "export a, * as b from 'mod'",
  "export a, { b, c } from 'mod'",
  "export * as a, { b } from 'mod'",
  "export * from 'mod'",
  "export { a, b } from 'mod'",
]) {
  try { console.log(JSON.stringify(s), "=>", p.format(s, {useFlowParser: false})); } catch (e) { console.log(s, "ERR", e.message); }
  try { console.log("  flow:", p.format(s, {useFlowParser: true})); } catch (e) { console.log("  flow ERR", e.message); }
}
EOF
/work/prettier__prettier-361/bin/envrun 'node repro.js'
```

tool result:

```
"export reducer from './reducer'" => export { reducer } from "./reducer";

  flow ERR Unexpected identifier on line 1
"export * as ns from 'mod'" => export { * as ns } from "mod";

  flow: export { * as ns } from "mod";

"export a, * as b from 'mod'" => export { a, * as b } from "mod";

  flow ERR Unexpected identifier on line 1
"export a, { b, c } from 'mod'" => export { a, b, c } from "mod";

  flow ERR Unexpected identifier on line 1
"export * as a, { b } from 'mod'" => export { * as a, b } from "mod";

  flow ERR Unexpected token , on line 1
"export * from 'mod'" => export * from "mod";

  flow: export * from "mod";

"export { a, b } from 'mod'" => export { a, b } from "mod";

  flow: export { a, b } from "mod";
Shell cwd was reset to /work/prettier__prettier-361/repo
```

**assistant:** Fix: print `ExportDefaultSpecifier`/`ExportNamespaceSpecifier` outside the braces, like the import printer does.

**tool call: Bash**

```bash
python3 - <<'EOF'
p='src/printer.js'
s=open(p).read()
old='''      } else {
        parts.push(
          decl.exportKind === "type" ? "type " : "",
          multilineGroup(
            concat([
              "{",
              indent(
                options.tabWidth,
                concat([
                  options.bracketSpacing ? line : softline,
                  join(concat([ ",", line ]), path.map(print, "specifiers"))
                ])
              ),
              ifBreak(options.trailingComma ? "," : ""),
              options.bracketSpacing ? line : softline,
              "}"
            ])
          )
        );
      }'''
new='''      } else {
        var standalones = [];
        var grouped = [];

        path.each(
          function(specifierPath) {
            var value = specifierPath.getValue();
            if (
              value.type === "ExportDefaultSpecifier" ||
                value.type === "ExportNamespaceSpecifier"
            ) {
              standalones.push(print(specifierPath));
            } else {
              grouped.push(print(specifierPath));
            }
          },
          "specifiers"
        );

        parts.push(decl.exportKind === "type" ? "type " : "");

        parts.push(join(", ", standalones));

        if (standalones.length > 0 && grouped.length > 0) {
          parts.push(", ");
        }

        if (grouped.length > 0) {
          parts.push(
            multilineGroup(
              concat([
                "{",
                indent(
                  options.tabWidth,
                  concat([
                    options.bracketSpacing ? line : softline,
                    join(concat([ ",", line ]), grouped)
                  ])
                ),
                ifBreak(options.trailingComma ? "," : ""),
                options.bracketSpacing ? line : softline,
                "}"
              ])
            )
          );
        }
      }'''
assert s.count(old)==1
open(p,'w').write(s.replace(old,new))
EOF
/work/prettier__prettier-361/bin/envrun 'node repro.js'
```

tool result:

```
"export reducer from './reducer'" => export reducer from "./reducer";

  flow ERR Unexpected identifier on line 1
"export * as ns from 'mod'" => export * as ns from "mod";

  flow: export * as ns from "mod";

"export a, * as b from 'mod'" => export a, * as b from "mod";

  flow ERR Unexpected identifier on line 1
"export a, { b, c } from 'mod'" => export a, { b, c } from "mod";

  flow ERR Unexpected identifier on line 1
"export * as a, { b } from 'mod'" => export * as a, { b } from "mod";

  flow ERR Unexpected token , on line 1
"export * from 'mod'" => export * from "mod";

  flow: export * from "mod";

"export { a, b } from 'mod'" => export { a, b } from "mod";

  flow: export { a, b } from "mod";
```

**assistant:** All forms now print correctly (the Flow parser simply doesn't support most of this syntax). Running the test suite:

**tool call: Bash**

```bash
rm repro.js; /work/prettier__prettier-361/bin/envrun 'npm test 2>&1 | tail -30'; git status --short
```

tool result:

```
 PASS  tests/contents/ignore/jsfmt.spec.js
 PASS  tests/jsx_intrinsics.custom/jsfmt.spec.js
 PASS  tests/shebang/jsfmt.spec.js
 PASS  tests/config_file_extensions/jsfmt.spec.js
 PASS  tests/jsx_intrinsics.custom/lib/jsfmt.spec.js
 PASS  tests/tagged-unions/jsfmt.spec.js
 PASS  tests/const_params/jsfmt.spec.js
 PASS  tests/immutable_methods/jsfmt.spec.js
 PASS  tests/interface/jsfmt.spec.js
 PASS  tests/object_assign/jsfmt.spec.js
 PASS  tests/lib_interfaces/declarations/jsfmt.spec.js
 PASS  tests/incremental_json/jsfmt.spec.js
 PASS  tests/generics/jsfmt.spec.js
 PASS  tests/closure/jsfmt.spec.js
 PASS  tests/arraylib/jsfmt.spec.js
 PASS  tests/return_new/jsfmt.spec.js
 PASS  tests/demo/2/jsfmt.spec.js
 PASS  tests/misc/jsfmt.spec.js
 PASS  tests/demo/1/jsfmt.spec.js
 PASS  tests/class_subtyping/jsfmt.spec.js
 PASS  tests/config_all_weak/jsfmt.spec.js
 PASS  tests/suggest/jsfmt.spec.js
 PASS  tests/import_typeof/jsfmt.spec.js
 PASS  tests/init/jsfmt.spec.js

Test Suites: 382 passed, 382 total
Tests:       1095 passed, 1095 total
Snapshots:   1095 passed, 1095 total
Time:        3.534s
Ran all test suites.

 M package.json
 M src/printer.js
?? Dockerfile
```

**assistant:** `package.json` and `Dockerfile` show up as changed, but I didn't touch them. Checking:

**tool call: Bash**

```bash
git diff package.json; ls -la Dockerfile
```

tool result:

```
diff --git a/package.json b/package.json
index b28bbda..b97d475 100644
--- a/package.json
+++ b/package.json
@@ -37,7 +37,8 @@
     "format": "./bin/prettier.js --write",
     "format:single": "npm run format -- src/printer.js",
     "format:all": "npm run format -- index.js src/*.js bin/*.js",
-    "build:docs": "rollup -c docs/rollup.config.js"
+    "build:docs": "rollup -c docs/rollup.config.js",
+    "lint": "echo noop"
   },
   "jest": {
     "setupFiles": [
-rw-r--r--  1 user  staff  308 Aug 27  2025 Dockerfile
```

**assistant:** Prettier now keeps the export extension syntax intact: `export reducer from './reducer'` stays as `export reducer from "./reducer";` instead of gaining curly braces. The full test suite passes (382 suites, 1095 tests).

**Cause:** In `printExportDeclaration` (`src/printer.js`), every export specifier was put inside `{ ... }`. That included the default form (`export reducer`) and the namespace form (`export * as ns`), which are valid only outside braces.

**Fix:** The export printer now handles specifiers the same way the import printer already did. Default and namespace specifiers are printed on their own, and any named ones follow in braces, separated by `, `. I checked these cases with the Babylon parser:

| Input | Before | After |
|---|---|---|
| `export reducer from './reducer'` | `export { reducer } from "./reducer";` | `export reducer from "./reducer";` |
| `export * as ns from 'mod'` | `export { * as ns } from "mod";` | `export * as ns from "mod";` |
| `export a, * as b from 'mod'` | `export { a, * as b } from "mod";` | `export a, * as b from "mod";` |
| `export a, { b, c } from 'mod'` | `export { a, b, c } from "mod";` | `export a, { b, c } from "mod";` |
| `export * as a, { b } from 'mod'` | `export { * as a, b } from "mod";` | `export * as a, { b } from "mod";` |

`export * from`, `export { a, b } from` and `export {}` print the same as before. The Flow parser can't parse most of the new forms (only `export * as ns`), so those only work with the default parser.

I deleted my reproduction script. Two other files show as changed in git that I didn't edit: `package.json` (adds a `"lint": "echo noop"` script) and an untracked `Dockerfile`. They look like leftovers from setting up the test environment, so I left them alone.

_session end: success, turns 9, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.5 s: node repro.js
- `rc=0` 0.48 s: node repro.js
- `rc=0` 5.75 s: npm test 2>&1 | tail -30
