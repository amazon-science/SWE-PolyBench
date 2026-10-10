# Instance: prettier__prettier-12930

- Final resolved (evaluator, logs/prettier__prettier-12930_result.json): True
- Run state: DONE
- One attempt. Duration 37.9 s, turns 7, actor cost $0.1071572, container commands 4
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/prettier__prettier-12930/repo
</uploaded_files>
I've uploaded a JavaScript code repository in the directory /work/prettier__prettier-12930/repo. Consider the following issue description:

<issue_description>
Syntax error after formatting when using computed key in TypeScript enum
**Prettier 2.6.2**
[Playground link](https://prettier.io/playground/#N4Igxg9gdgLgprEAuECCuBbABAQS8AHSiywG0BLAakoF0iBfEAGhAgAcZzoBnZUAQwBOgiAHcACkIS8U-ADaj+AT14sARoP5gA1nBgBlfhjgAZclDjIAZvO5x1mnXv1st5gObIYgtPdQY1OAATIOCTfih3NH53OAAxCEEMfhhOSOQQfjQYCGYQAAsYDDkAdXzyeG5XMDh9aQryADcKpQywblUQcztBGHFNd2TrWz8AK24AD30POTgARTQIeGG5OxZXQR6MmCU2OG4wQXIOPLYj2BLyIJh85AAOAAZ1kTsSzTYMs-24QUbLFgAjot4P12DJMtwALQWYLBPKCOBA8gI-oxIZIGyrPx2DDkLw+bEzebAywYkYsGD8NSXa63JAAJgpmnIcg8AGEIBh0ahuABWPJoOwAFSpMkxaxAjV8AEkoKFYPpDscYDg5fodrMVnZ6PQgA)
<!-- prettier-ignore -->
```sh
--parser typescript
```

**Input 1:**
<!-- prettier-ignore -->
```tsx
enum A {
  [i++]
}
```

**Output 1:**
<!-- prettier-ignore -->
```tsx
enum A {
  i++,
}

```
**Input 2:**
<!-- prettier-ignore -->
```tsx
const a = "b"
enum A {
  [a] = 2
}
```

**Output 2:**
<!-- prettier-ignore -->
```tsx
const a = "b";
enum A {
  a = 2,
}

```

**Expected behavior:**
The output should be valid syntax. Although TypeScript will error during compiling that computed keys are not allowed in enums, they are valid syntax and parse correctly. Prettier should still support formatting this. Note that TypeScript still produces emit even when erroring, meaning the code would be able to run.

**Actual behavior:**
The output incorrectly removes the brackets, producing a syntax error on example 1, or modifying the runtime behaviour in example 2.



</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/prettier__prettier-12930/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/prettier__prettier-12930/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/prettier__prettier-12930/bin/envrun 'git status --short && ls'
Edits you make under /work/prettier__prettier-12930/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/prettier__prettier-12930/repo; grep -n "TSEnumMember" -A15 src/language-js/print/typescript.js; grep -rn "computed" src/language-js/print/property.js | head
```

tool result:

```
416:    case "TSEnumMember":
417-      parts.push(print("id"));
418-      if (node.initializer) {
419-        parts.push(" = ", print("initializer"));
420-      }
421-      return parts;
422-    case "TSImportEqualsDeclaration":
423-      if (node.isExport) {
424-        parts.push("export ");
425-      }
426-
427-      parts.push("import ");
428-
429-      if (node.importKind && node.importKind !== "value") {
430-        parts.push(node.importKind, " ");
431-      }
src/language-js/print/property.js:19:  if (node.computed) {
src/language-js/print/property.js:38:        !prop.computed &&
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-12930/repo; git status; grep -rln "i++\]" tests/format/typescript | head; cat > /tmp/r.ts <<'EOF'
enum A {
  [i++],
  ["a"] = 1,
  [a] = 2,
  "b" = 3,
}
EOF
cp /tmp/r.ts repro.ts; ../bin/envrun 'for p in typescript babel-ts; do ./bin/prettier.js --parser $p repro.ts; done; node -e "console.log(JSON.stringify(require(\"@typescript-eslint/typescript-estree\").parse(\"enum A {[a]=1}\").body[0].members[0]))"'
```

tool result:

```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   package.json

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Dockerfile

no changes added to commit (use "git add" and/or "git commit -a")
(eval):1: operation not permitted: /tmp/r.ts
cp: /tmp/r.ts: No such file or directory
[error] No files matching the pattern were found: "repro.ts".
[error] No files matching the pattern were found: "repro.ts".
{"type":"TSEnumMember","id":{"type":"Identifier","name":"a"},"initializer":{"type":"Literal","value":1,"raw":"1"},"computed":true}
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-12930/repo; printf 'enum A {\n  [i++],\n  ["a"] = 1,\n  [a] = 2,\n  "b" = 3,\n}\n' > repro.ts; ../bin/envrun 'for p in typescript babel-ts; do ./bin/prettier.js --parser $p repro.ts; done'
```

tool result:

```
Exit code 2
enum A {
  i++,
  "a" = 1,
  a = 2,
  "b" = 3,
}
[error] repro.ts: SyntaxError: Unexpected token (2:3)
[error]   1 | enum A {
[error] > 2 |   [i++],
[error]     |   ^
[error]   3 |   ["a"] = 1,
[error]   4 |   [a] = 2,
[error]   5 |   "b" = 3,
```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/prettier__prettier-12930/repo/src/language-js/print/typescript.js",
 "old_string": "      parts.push(print(\"id\"));\n      if (node.initializer) {",
 "new_string": "      if (node.computed) {\n        parts.push(\"[\", print(\"id\"), \"]\");\n      } else {\n        parts.push(print(\"id\"));\n      }\n      if (node.initializer) {"
}
```

tool result:

```
The file /work/prettier__prettier-12930/repo/src/language-js/print/typescript.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-12930/repo; ../bin/envrun './bin/prettier.js --parser typescript repro.ts; ./bin/prettier.js --parser typescript repro.ts | ./bin/prettier.js --parser typescript --stdin-filepath x.ts'; ls tests/format/typescript | grep -i enum; git status --short tests
```

tool result:

```
enum A {
  [i++],
  ["a"] = 1,
  [a] = 2,
  "b" = 3,
}
enum A {
  [i++],
  ["a"] = 1,
  [a] = 2,
  "b" = 3,
}

enum
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-12930/repo; rm repro.ts; grep -rn "TSEnumMember" src/ | grep -v "print/typescript.js"; ../bin/envrun 'yarn jest tests/format/typescript/enum tests/format/typescript/conformance 2>&1 | tail -8'
```

tool result:

```
PASS tests/format/typescript/enum/jsfmt.spec.js

Test Suites: 47 passed, 47 total
Tests:       262 passed, 262 total
Snapshots:   138 passed, 138 total
Time:        6.031 s
Ran all test suites matching /tests\/format\/typescript\/enum|tests\/format\/typescript\/conformance/i.
Done in 9.86s.
```

**assistant:** I fixed the bug: Prettier now keeps the brackets on computed enum keys like `[i++]` and `[a] = 2` when using the `typescript` parser.

**Cause:** The TypeScript parser does record that a key is computed (it sets `computed: true` on the enum member). But the enum member printer in `src/language-js/print/typescript.js` ignored that flag and printed only the key itself, which dropped the brackets.

**Fix:** In that same printer, if the member is computed, the key is now wrapped in `[` `]`. It's a few lines, and no other files changed.

**Verification:** I ran this input through `--parser typescript`:
```ts
enum A {
  [i++],
  ["a"] = 1,
  [a] = 2,
  "b" = 3,
}
```
- **Before:** the output was `i++,`, `"a" = 1` and `a = 2`. The first is a syntax error and the third changes what the code does at runtime.
- **After:** the output matches the input exactly, and formatting that output a second time gives the same result.
- **Tests:** the `tests/format/typescript/enum` and `tests/format/typescript/conformance` suites pass (47 suites, 262 tests).

**`babel-ts` parser:** this input still fails there, with `SyntaxError: Unexpected token`, because Babel's parser doesn't accept computed enum keys at all. That's a parser limitation the printer can't fix, so I left it alone.

I deleted my reproduction file. The `package.json` change and the untracked `Dockerfile` were already there before I started, and I didn't touch them.

_session end: success, turns 7, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 2.05 s: for p in typescript babel-ts; do ./bin/prettier.js --parser $p repro.ts; done; node -e "console.log(JSON.stringify(require(\"@typescript-eslint/typescript-estree\").parse(\"enum A {[a]=1}\").body[0].members[0]))"
- `rc=2` 1.54 s: for p in typescript babel-ts; do ./bin/prettier.js --parser $p repro.ts; done
- `rc=0` 2.46 s: ./bin/prettier.js --parser typescript repro.ts; ./bin/prettier.js --parser typescript repro.ts | ./bin/prettier.js --parser typescript --stdin-filepath x.ts
- `rc=0` 10.52 s: yarn jest tests/format/typescript/enum tests/format/typescript/conformance 2>&1 | tail -8
