# Instance: prettier__prettier-11637

- Final resolved (evaluator, logs/prettier__prettier-11637_result.json): True
- Run state: DONE
- One attempt. Duration 115.7 s, turns 22, actor cost $0.5111016, container commands 9
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/prettier__prettier-11637/repo
</uploaded_files>
I've uploaded a JavaScript code repository in the directory /work/prettier__prettier-11637/repo. Consider the following issue description:

<issue_description>
Weird wrapping for SCSS @use rules
<!--

BEFORE SUBMITTING AN ISSUE:

1.  Search for your issue on GitHub: https://github.com/prettier/prettier/issues
    A large number of opened issues are duplicates of existing issues.
    If someone has already opened an issue for what you are experiencing,
    you do not need to open a new issue — please add a 👍 reaction to the
    existing issue instead.

2.  We get a lot of requests for adding options, but Prettier is
    built on the principle of being opinionated about code formatting.
    This means we add options only in the case of strict technical necessity.
    Find out more: https://prettier.io/docs/en/option-philosophy.html

Don't fill the form below manually! Let a program create a report for you:

1. Go to https://prettier.io/playground
2. Paste your code and set options
3. Press the "Report issue" button in the lower right

-->

**Prettier 2.4.1**
[Playground link](https://prettier.io/playground/#N4Igxg9gdgLgprEAuEABArgZzgAgDpoBmAngDYDmAVgIYD0ARtdgTgO4CWMAFjgBR5QcQnABJC1ALbtSxALQTq7KEj4Dh6nACV09dgGsANGo1DNEehBgQjgkzkzFM8CbPTsbd+9SiZZ2AE7shB7CAJQhQmLQMLKscOzkXDAqAMwArAAMEaJcAIyyhNGx8YnJOJlZxpFcAEwFRXEJSSoV2SJcKfWwxU1lFQKhANwgBiAQAA4w7NCYyKDU-v4QrAAKCwizKNSkrNSOIyD0-tRgenAwAMqScAAySnDI4qTYo0cnZ5fjJ0rkyDD+6DgozgEnocAAJuCITdvOR0NRyHAAGIQfwKGBTKC-LboKwHJISUgAdS4nDgmC+YDgFw2nHYADdOMRkOBMLNRkoAjAVsdyApHtsXiBKJgAB4XH6kOAARXQlgeSCeQq+-gCLMwYDZB3GgVgRPY4O4yAAHFkQDqINgicdxiydeS4P56Q9RgBHOXwHkTTYgJiyKBwCEQg7+ODu9ihnkI-mKwVAkDYKR-AHxzCSmUehVK+Mwaj0fWGrjIGqjf6KUg-ADCEAkMZA5LSBywcAAKnnNtnRvTAQBJKBQ2AXMCBSYAQX7FxgZCzcYAvrOgA)

Not sure which version this was introduced.
Previously this did not happen.

But the current SCSS syntax using `@use` gets wrapped in a weird way.
The opening parentheses is wrapped with a indent, and also all of  the code inside it.

**Input:**

```scss
@use "@fylgja/base" with (
    $family-main: (
        Rubik,
        Roboto,
        system-ui,
        sans-serif,
    ),
    $font-weight: 350,
    $h1-font-weight: 500,
    $h2-font-weight: 500,
    $h3-font-weight: 500
);
```

**Output:**

```scss
@use "@fylgja/base" with
  (
    $family-main: (
      Rubik,
      Roboto,
      system-ui,
      sans-serif,
    ),
    $font-weight: 350,
    $h1-font-weight: 500,
    $h2-font-weight: 500,
    $h3-font-weight: 500
  );
```

**Expected behavior:**

```scss
@use "@fylgja/base" with (
    $family-main: (
        Rubik,
        Roboto,
        system-ui,
        sans-serif,
    ),
    $font-weight: 350,
    $h1-font-weight: 500,
    $h2-font-weight: 500,
    $h3-font-weight: 500
);
```


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/prettier__prettier-11637/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/prettier__prettier-11637/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/prettier__prettier-11637/bin/envrun 'git status --short && ls'
Edits you make under /work/prettier__prettier-11637/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/prettier__prettier-11637/repo; grep -n "isSCSSMapItemNode\|@use\|\"with\"\|isKeyInValuePairNode" src/language-css/*.js | head -50
```

tool result:

```
src/language-css/printer-postcss.js:61:  isKeyInValuePairNode,
src/language-css/printer-postcss.js:66:  isSCSSMapItemNode,
src/language-css/printer-postcss.js:870:      const isSCSSMapItem = isSCSSMapItemNode(path);
src/language-css/printer-postcss.js:874:      const isKey = isKeyInValuePairNode(node, parentNode);
src/language-css/utils.js:348:function isSCSSMapItemNode(path) {
src/language-css/utils.js:410:function isKeyInValuePairNode(node, parentNode) {
src/language-css/utils.js:528:  isKeyInValuePairNode,
src/language-css/utils.js:529:  isSCSSMapItemNode,
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-11637/repo; sed -n 340,410p src/language-css/utils.js; sed -n 860,940p src/language-css/printer-postcss.js
```

tool result:

```
  return (
    node.type === "value-paren_group" &&
    node.groups &&
    node.groups[0] &&
    isKeyValuePairNode(node.groups[0])
  );
}

function isSCSSMapItemNode(path) {
  const node = path.getValue();

  // Ignore empty item (i.e. `$key: ()`)
  if (node.groups.length === 0) {
    return false;
  }

  const parentParentNode = path.getParentNode(1);

  // Check open parens contain key/value pair (i.e. `(key: value)` and `(key: (value, other-value)`)
  if (
    !isKeyValuePairInParenGroupNode(node) &&
    !(parentParentNode && isKeyValuePairInParenGroupNode(parentParentNode))
  ) {
    return false;
  }

  const declNode = getAncestorNode(path, "css-decl");

  // SCSS map declaration (i.e. `$map: (key: value, other-key: other-value)`)
  if (declNode && declNode.prop && declNode.prop.startsWith("$")) {
    return true;
  }

  // List as value of key inside SCSS map (i.e. `$map: (key: (value other-value other-other-value))`)
  if (isKeyValuePairInParenGroupNode(parentParentNode)) {
    return true;
  }

  // SCSS Map is argument of function (i.e. `func((key: value, other-key: other-value))`)
  if (parentParentNode.type === "value-func") {
    return true;
  }

  return false;
}

function isInlineValueCommentNode(node) {
  return node.type === "value-comment" && node.inline;
}

function isHashNode(node) {
  return node.type === "value-word" && node.value === "#";
}

function isLeftCurlyBraceNode(node) {
  return node.type === "value-word" && node.value === "{";
}

function isRightCurlyBraceNode(node) {
  return node.type === "value-word" && node.value === "}";
}

function isWordNode(node) {
  return ["value-word", "value-atword"].includes(node.type);
}

function isColonNode(node) {
  return node && node.type === "value-colon";
}

function isKeyInValuePairNode(node, parentNode) {
        for (let i = 0; i < printed.length; i++) {
          if (i !== 0) {
            res.push([",", line]);
          }
          res.push(printed[i]);
        }

        return group(indent(fill(res)));
      }

      const isSCSSMapItem = isSCSSMapItemNode(path);

      const lastItem = getLast(node.groups);
      const isLastItemComment = lastItem && lastItem.type === "value-comment";
      const isKey = isKeyInValuePairNode(node, parentNode);

      const printed = group(
        [
          node.open ? print("open") : "",
          indent([
            softline,
            join(
              [",", line],
              path.map((childPath) => {
                const node = childPath.getValue();
                const printed = print();

                // Key/Value pair in open paren already indented
                if (
                  isKeyValuePairNode(node) &&
                  node.type === "value-comma_group" &&
                  node.groups &&
                  node.groups[0].type !== "value-paren_group" &&
                  node.groups[2] &&
                  node.groups[2].type === "value-paren_group"
                ) {
                  const parts = getDocParts(printed.contents.contents);
                  parts[1] = group(parts[1]);

                  return group(dedent(printed));
                }

                return printed;
              }, "groups")
            ),
          ]),
          ifBreak(
            !isLastItemComment &&
              isSCSS(options.parser, options.originalText) &&
              isSCSSMapItem &&
              shouldPrintComma(options)
              ? ","
              : ""
          ),
          softline,
          node.close ? print("close") : "",
        ],
        {
          shouldBreak: isSCSSMapItem && !isKey,
        }
      );

      return isKey ? dedent(printed) : printed;
    }
    case "value-func": {
      return [
        node.value,
        insideAtRuleNode(path, "supports") && isMediaAndSupportsKeywords(node)
          ? " "
          : "",
        print("group"),
      ];
    }
    case "value-paren": {
      return node.value;
    }
    case "value-number": {
      return [printCssNumber(node.value), maybeToLowerCase(node.unit)];
    }
    case "value-operator": {
      return node.value;
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-11637/repo; printf '@use "@fylgja/base" with (\n    $family-main: (\n        Rubik,\n        Roboto,\n        system-ui,\n        sans-serif,\n    ),\n    $font-weight: 350,\n    $h1-font-weight: 500,\n    $h2-font-weight: 500,\n    $h3-font-weight: 500\n);\n@use "library" with ($black: #222, $border-radius: 0.1rem);\n' > /tmp/repro.scss; cp /tmp/repro.scss repro.scss; ../bin/envrun './bin/prettier.js repro.scss'; ls tests/format/scss | grep -i use; git log --oneline -3
```

tool result:

```
(eval):1: operation not permitted: /tmp/repro.scss
cp: /tmp/repro.scss: No such file or directory
[error] No files matching the pattern were found: "repro.scss".

5909f5b3f Extract unified plugins (#11632)
580827020 Turn off trim_trailing_whitespace in Markdown in root or changelog_unreleased (#11605)
6106421f0 Remove unnecessary copy (#11602)
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-11637/repo; printf '@use "@fylgja/base" with (\n    $family-main: (\n        Rubik,\n        Roboto,\n        system-ui,\n        sans-serif,\n    ),\n    $font-weight: 350,\n    $h1-font-weight: 500,\n    $h2-font-weight: 500,\n    $h3-font-weight: 500\n);\n@use "library" with ($black: #222, $border-radius: 0.1rem);\n@use "library" with ($black: #222, $border-radius: 0.1rem, $font-family: "Helvetica, sans-serif");\n' > repro.scss; ../bin/envrun './bin/prettier.js repro.scss'; grep -rln "@use" tests/format/scss
```

tool result:

```
@use "@fylgja/base" with
  (
    $family-main: (
      Rubik,
      Roboto,
      system-ui,
      sans-serif,
    ),
    $font-weight: 350,
    $h1-font-weight: 500,
    $h2-font-weight: 500,
    $h3-font-weight: 500
  );
@use "library" with ($black: #222, $border-radius: 0.1rem);
@use "library" with
  ($black: #222, $border-radius: 0.1rem, $font-family: "Helvetica, sans-serif");

tests/format/scss/quotes/quotes.scss
tests/format/scss/quotes/__snapshots__/jsfmt.spec.js.snap
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-11637/repo; grep -n -B2 -A12 "with" tests/format/scss/quotes/__snapshots__/jsfmt.spec.js.snap | head -80; git status
```

tool result:

```
10-@use "library";
11-
12:@use "library" with (
13-  $black: #222,
14-  $border-radius: 0.1rem
15-  $font-family: "Helvetica, sans-serif"
16-);
17-
18-@use "library" as *;
19-
20-@use "library" as f;
21-
22-@use "sass:map";
23-
24-@forward "library";
--
35-@use 'library';
36-
37:@use 'library' with
38-  ($black: #222, $border-radius: 0.1rem $font-family: 'Helvetica, sans-serif');
39-
40-@use 'library' as *;
41-
42-@use 'library' as f;
43-
44-@use 'sass:map';
45-
46-@forward 'library';
47-
48-@forward 'library' show border, $border-color;
49-
--
65-@use "library";
66-
67:@use "library" with (
68-  $black: #222,
69-  $border-radius: 0.1rem
70-  $font-family: "Helvetica, sans-serif"
71-);
72-
73-@use "library" as *;
74-
75-@use "library" as f;
76-
77-@use "sass:map";
78-
79-@forward "library";
--
90-@use "library";
91-
92:@use "library" with
93-  ($black: #222, $border-radius: 0.1rem $font-family: "Helvetica, sans-serif");
94-
95-@use "library" as *;
96-
97-@use "library" as f;
98-
99-@use "sass:map";
100-
101-@forward "library";
102-
103-@forward "library" show border, $border-color;
104-
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   package.json

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Dockerfile
	repro.scss

no changes added to commit (use "git add" and/or "git commit -a")
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-11637/repo; git diff package.json | head; sed -n 560,860p src/language-css/printer-postcss.js
```

tool result:

```
diff --git a/package.json b/package.json
index d412831b0..81b9e57ac 100644
--- a/package.json
+++ b/package.json
@@ -149,7 +149,7 @@
     "perf:repeat": "yarn && yarn build && cross-env NODE_ENV=production node ./dist/bin-prettier.js --debug-repeat ${PERF_REPEAT:-1000} --loglevel debug ${PERF_FILE:-./index.js} > /dev/null",
     "perf:repeat-inspect": "yarn && yarn build && cross-env NODE_ENV=production node --inspect-brk ./dist/bin-prettier.js --debug-repeat ${PERF_REPEAT:-1000} --loglevel debug ${PERF_FILE:-./index.js} > /dev/null",
     "perf:benchmark": "yarn && yarn build && cross-env NODE_ENV=production node ./dist/bin-prettier.js --debug-benchmark --loglevel debug ${PERF_FILE:-./index.js} > /dev/null",
-    "lint": "run-p lint:*",
+    "lint": "echo noop",
          iNextNode.type === "value-operator" &&
          iNextNode.value === "*"
        ) {
          continue;
        }

        // Ignore after latest node (i.e. before semicolon)
        if (!iNextNode) {
          continue;
        }

        // styled.div` background: var(--${one}); `
        if (
          iNode.type === "value-word" &&
          iNode.value.endsWith("-") &&
          isAtWordPlaceholderNode(iNextNode)
        ) {
          continue;
        }

        // Ignore spaces before/after string interpolation (i.e. `"#{my-fn("_")}"`)
        const isStartSCSSInterpolationInString =
          iNode.type === "value-string" && iNode.value.startsWith("#{");
        const isEndingSCSSInterpolationInString =
          insideSCSSInterpolationInString &&
          iNextNode.type === "value-string" &&
          iNextNode.value.endsWith("}");

        if (
          isStartSCSSInterpolationInString ||
          isEndingSCSSInterpolationInString
        ) {
          insideSCSSInterpolationInString = !insideSCSSInterpolationInString;

          continue;
        }

        if (insideSCSSInterpolationInString) {
          continue;
        }

        // Ignore colon (i.e. `:`)
        if (isColonNode(iNode) || isColonNode(iNextNode)) {
          continue;
        }

        // Ignore `@` in Less (i.e. `@@var;`)
        if (iNode.type === "value-atword" && iNode.value === "") {
          continue;
        }

        // Ignore `~` in Less (i.e. `content: ~"^//* some horrible but needed css hack";`)
        if (iNode.value === "~") {
          continue;
        }

        // Ignore escape `\`
        if (
          iNode.value &&
          iNode.value.includes("\\") &&
          iNextNode &&
          iNextNode.type !== "value-comment"
        ) {
          continue;
        }

        // Ignore escaped `/`
        if (
          iPrevNode &&
          iPrevNode.value &&
          iPrevNode.value.indexOf("\\") === iPrevNode.value.length - 1 &&
          iNode.type === "value-operator" &&
          iNode.value === "/"
        ) {
          continue;
        }

        // Ignore `\` (i.e. `$variable: \@small;`)
        if (iNode.value === "\\") {
          continue;
        }

        // Ignore `$$` (i.e. `background-color: $$(style)Color;`)
        if (isPostcssSimpleVarNode(iNode, iNextNode)) {
          continue;
        }

        // Ignore spaces after `#` and after `{` and before `}` in SCSS interpolation (i.e. `#{variable}`)
        if (
          isHashNode(iNode) ||
          isLeftCurlyBraceNode(iNode) ||
          isRightCurlyBraceNode(iNextNode) ||
          (isLeftCurlyBraceNode(iNextNode) && hasEmptyRawBefore(iNextNode)) ||
          (isRightCurlyBraceNode(iNode) && hasEmptyRawBefore(iNextNode))
        ) {
          continue;
        }

        // Ignore css variables and interpolation in SCSS (i.e. `--#{$var}`)
        if (iNode.value === "--" && isHashNode(iNextNode)) {
          continue;
        }

        // Formatting math operations
        const isMathOperator = isMathOperatorNode(iNode);
        const isNextMathOperator = isMathOperatorNode(iNextNode);

        // Print spaces before and after math operators beside SCSS interpolation as is
        // (i.e. `#{$var}+5`, `#{$var} +5`, `#{$var}+ 5`, `#{$var} + 5`)
        // (i.e. `5+#{$var}`, `5 +#{$var}`, `5+ #{$var}`, `5 + #{$var}`)
        if (
          ((isMathOperator && isHashNode(iNextNode)) ||
            (isNextMathOperator && isRightCurlyBraceNode(iNode))) &&
          hasEmptyRawBefore(iNextNode)
        ) {
          continue;
        }

        // absolute paths are only parsed as one token if they are part of url(/abs/path) call
        // but if you have custom -fb-url(/abs/path/) then it is parsed as "division /" and rest
        // of the path. We don't want to put a space after that first division in this case.
        if (!iPrevNode && isDivisionNode(iNode)) {
          continue;
        }

        // Print spaces before and after addition and subtraction math operators as is in `calc` function
        // due to the fact that it is not valid syntax
        // (i.e. `calc(1px+1px)`, `calc(1px+ 1px)`, `calc(1px +1px)`, `calc(1px + 1px)`)
        if (
          insideValueFunctionNode(path, "calc") &&
          (isAdditionNode(iNode) ||
            isAdditionNode(iNextNode) ||
            isSubtractionNode(iNode) ||
            isSubtractionNode(iNextNode)) &&
          hasEmptyRawBefore(iNextNode)
        ) {
          continue;
        }

        // Print spaces after `+` and `-` in color adjuster functions as is (e.g. `color(red l(+ 20%))`)
        // Adjusters with signed numbers (e.g. `color(red l(+20%))`) output as-is.
        const isColorAdjusterNode =
          (isAdditionNode(iNode) || isSubtractionNode(iNode)) &&
          i === 0 &&
          (iNextNode.type === "value-number" || iNextNode.isHex) &&
          parentParentNode &&
          isColorAdjusterFuncNode(parentParentNode) &&
          !hasEmptyRawBefore(iNextNode);

        const requireSpaceBeforeOperator =
          (iNextNextNode && iNextNextNode.type === "value-func") ||
          (iNextNextNode && isWordNode(iNextNextNode)) ||
          iNode.type === "value-func
[... 4408 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-11637/repo; grep -rl "fylgja\|with (" tests/format/scss tests/format/less 2>/dev/null | head; grep -n "getAncestorNode\|insideAtRuleNode" src/language-css/utils.js | head
```

tool result:

```
tests/format/scss/quotes/quotes.scss
tests/format/scss/quotes/__snapshots__/jsfmt.spec.js.snap
48:function getAncestorNode(path, typeOrTypes) {
54:  const declAncestorNode = getAncestorNode(path, "css-decl");
110:  const atRuleAncestorNode = getAncestorNode(path, "css-atrule");
132:  const funcAncestorNode = getAncestorNode(path, "value-func");
141:  const ruleAncestorNode = getAncestorNode(path, "css-rule");
152:function insideAtRuleNode(path, atRuleNameOrAtRuleNames) {
156:  const atRuleAncestorNode = getAncestorNode(path, "css-atrule");
166:  const atRuleAncestorNode = getAncestorNode(path, "css-atrule");
366:  const declNode = getAncestorNode(path, "css-decl");
489:  getAncestorNode,
```

**thinking:**

```
Found that the `line` between `with` and `(` causes incorrect breaking, and the paren group isn't recognized as an SCSS map so it won't break per item. I'll fix both issues now.


```

**tool call: Bash**

```bash
cd /work/prettier__prettier-11637/repo; sed -n 40,60p src/language-css/utils.js; sed -n 150,175p src/language-css/utils.js; grep -n "atRuleAncestorNode =" src/language-css/printer-postcss.js
```

tool result:

```
    if (types.includes(ancestorNode.type)) {
      return counter;
    }
  }

  return -1;
}

function getAncestorNode(path, typeOrTypes) {
  const counter = getAncestorCounter(path, typeOrTypes);
  return counter === -1 ? null : path.getParentNode(counter);
}

function getPropOfDeclNode(path) {
  const declAncestorNode = getAncestorNode(path, "css-decl");

  return (
    declAncestorNode &&
    declAncestorNode.prop &&
    declAncestorNode.prop.toLowerCase()
  );
}

function insideAtRuleNode(path, atRuleNameOrAtRuleNames) {
  const atRuleNames = Array.isArray(atRuleNameOrAtRuleNames)
    ? atRuleNameOrAtRuleNames
    : [atRuleNameOrAtRuleNames];
  const atRuleAncestorNode = getAncestorNode(path, "css-atrule");

  return (
    atRuleAncestorNode &&
    atRuleNames.includes(atRuleAncestorNode.name.toLowerCase())
  );
}

function insideURLFunctionInImportAtRuleNode(path) {
  const node = path.getValue();
  const atRuleAncestorNode = getAncestorNode(path, "css-atrule");

  return (
    atRuleAncestorNode &&
    atRuleAncestorNode.name === "import" &&
    node.groups[0].value === "url" &&
    node.groups.length === 2
  );
}

522:      const atRuleAncestorNode = getAncestorNode(path, "css-atrule");
```

**assistant:** Now the edits.

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/prettier__prettier-11637/repo/src/language-css/utils.js",
 "old_string": "  if (parentParentNode.type === \"value-func\") {\n    return true;\n  }\n\n  return false;",
 "new_string": "  if (parentParentNode.type === \"value-func\") {\n    return true;\n  }\n\n  // SCSS Map is configuration of module (i.e. `@use \"library\" with ($key: value)`)\n  if (insideAtRuleNode(path, [\"use\", \"forward\"])) {\n    return true;\n  }\n\n  return false;"
}
```

tool result:

```
The file /work/prettier__prettier-11637/repo/src/language-css/utils.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/prettier__prettier-11637/repo/src/language-css/printer-postcss.js",
 "old_string": "        // Formatting `grid` property\n        if (isGridValue) {",
 "new_string": "        // Keep `with` and module configuration on the same line in SCSS (i.e. `@use \"library\" with ($key: value)`)\n        if (\n          atRuleAncestorNode &&\n          [\"use\", \"forward\"].includes(atRuleAncestorNode.name.toLowerCase()) &&\n          iNode.type === \"value-word\" &&\n          iNode.value === \"with\" &&\n          iNextNode.type === \"value-paren_group\"\n        ) {\n          parts.push(\" \");\n\n          continue;\n        }\n\n        // Formatting `grid` property\n        if (isGridValue) {"
}
```

tool result:

```
The file /work/prettier__prettier-11637/repo/src/language-css/printer-postcss.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-11637/repo; printf '@forward "library" with ($black: #222 !default, $border-radius: 0.1rem !default);\n@use "lib" with ($a: (b: c, d: e));\n@use "lib" with ($a: f(1, 2));\n' >> repro.scss; ../bin/envrun './bin/prettier.js repro.scss'
```

tool result:

```
Exit code 2
[error] repro.scss: TypeError: Cannot read properties of undefined (reading 'type')
[error]     at Object.genericPrint [as print] (/testbed/src/language-css/printer-postcss.js:558:21)
[error]     at callPluginPrintFunction (/testbed/src/main/ast-to-doc.js:133:21)
[error]     at mainPrintInternal (/testbed/src/main/ast-to-doc.js:76:17)
[error]     at mainPrint (/testbed/src/main/ast-to-doc.js:56:14)
[error]     at /testbed/src/language-css/printer-postcss.js:898:33
[error]     at /testbed/src/common/ast-path.js:108:23
[error]     at AstPath.each (/testbed/src/common/ast-path.js:95:7)
[error]     at AstPath.map (/testbed/src/common/ast-path.js:107:10)
[error]     at Object.genericPrint [as print] (/testbed/src/language-css/printer-postcss.js:896:20)
[error]     at callPluginPrintFunction (/testbed/src/main/ast-to-doc.js:133:21)
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-11637/repo; sed -n 550,562p src/language-css/printer-postcss.js; git stash -q; ../bin/envrun './bin/prettier.js repro.scss' 2>&1 | head -3; git stash pop -q; git status --short
```

tool result:

```
          continue;
        }

        // Ignore SCSS @forward wildcard suffix
        if (
          insideAtRuleNode(path, "forward") &&
          iNode.type === "value-word" &&
          iNode.value &&
          iPrevNode.type === "value-word" &&
          iPrevNode.value === "as" &&
          iNextNode.type === "value-operator" &&
          iNextNode.value === "*"
        ) {
[error] repro.scss: TypeError: Cannot read properties of undefined (reading 'type')
[error]     at Object.genericPrint [as print] (/testbed/src/language-css/printer-postcss.js:558:21)
[error]     at callPluginPrintFunction (/testbed/src/main/ast-to-doc.js:133:21)
 M package.json
 M src/language-css/printer-postcss.js
 M src/language-css/utils.js
?? Dockerfile
?? repro.scss
```

**thinking:**

```
That crash is a pre-existing, separate bug in the `@forward` wildcard check, unrelated to my change. I'll remove it from the repro and test the remaining cases.


```

**tool call: Bash**

```bash
cd /work/prettier__prettier-11637/repo; sed -i.bak '/@forward/d' repro.scss && rm repro.scss.bak; ../bin/envrun './bin/prettier.js repro.scss > out.scss; cat out.scss; ./bin/prettier.js out.scss | diff - out.scss && echo IDEMPOTENT'
```

tool result:

```
@use "@fylgja/base" with (
    $family-main: (
      Rubik,
      Roboto,
      system-ui,
      sans-serif,
    ),
    $font-weight: 350,
    $h1-font-weight: 500,
    $h2-font-weight: 500,
    $h3-font-weight: 500,
  );
@use "library" with (
    $black: #222,
    $border-radius: 0.1rem,
  );
@use "library" with (
    $black: #222,
    $border-radius: 0.1rem,
    $font-family: "Helvetica, sans-serif",
  );
@use "lib" with (
    $a: (
      b: c,
      d: e,
    ),
  );
@use "lib" with (
    $a: f(1, 2),
  );
IDEMPOTENT
```

**thinking:**

```
I found two remaining issues: an extra indent from nesting inside the comma group, and an unwanted trailing comma from treating it as a map item. I'll fix this by detecting `with (...)` configurations directly and forcing them to break/dedent, similar to how map keys are handled, instead of classifying them as map items.


```

**tool call: Bash**

```bash
cd /work/prettier__prettier-11637/repo; git checkout src/language-css/utils.js src/language-css/printer-postcss.js
```

tool result:

```
Updated 2 paths from the index
```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/prettier__prettier-11637/repo/src/language-css/utils.js",
 "old_string": "function isInlineValueCommentNode(node) {",
 "new_string": "// Module configuration in SCSS (i.e. `@use \"library\" with ($black: #222)`)\nfunction isSCSSModuleConfigurationNode(path) {\n  const node = path.getValue();\n  const parentNode = path.getParentNode();\n\n  if (\n    !node.open ||\n    node.open.value !== \"(\" ||\n    !node.close ||\n    node.close.value !== \")\" ||\n    !parentNode ||\n    parentNode.type !== \"value-comma_group\" ||\n    !insideAtRuleNode(path, [\"use\", \"forward\"])\n  ) {\n    return false;\n  }\n\n  const previousNode = parentNode.groups[parentNode.groups.indexOf(node) - 1];\n\n  return Boolean(\n    previousNode &&\n      previousNode.type === \"value-word\" &&\n      previousNode.value === \"with\"\n  );\n}\n\nfunction isInlineValueCommentNode(node) {"
}
```

tool result:

```
The file /work/prettier__prettier-11637/repo/src/language-css/utils.js has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-11637/repo; sed -i.bak 's/^  isSCSSMapItemNode,$/  isSCSSMapItemNode,\n  isSCSSModuleConfigurationNode,/' src/language-css/utils.js src/language-css/printer-postcss.js && rm src/language-css/*.bak; git diff --stat
```

tool result:

```
 package.json                        |  2 +-
 src/language-css/printer-postcss.js |  1 +
 src/language-css/utils.js           | 27 +++++++++++++++++++++++++++
 3 files changed, 29 insertions(+), 1 deletion(-)
```

**assistant:** Now I'll update the paren-group printing:

**tool call: Bash**

```bash
cd /work/prettier__prettier-11637/repo; python3 - <<'EOF'
p='src/language-css/printer-postcss.js'
s=open(p).read()
old='''      const isKey = isKeyInValuePairNode(node, parentNode);
'''
new='''      const isKey = isKeyInValuePairNode(node, parentNode);
      const isModuleConfiguration = isSCSSModuleConfigurationNode(path);
'''
assert s.count(old)==1; s=s.replace(old,new)
old='''          shouldBreak: isSCSSMapItem && !isKey,
        }
      );

      return isKey ? dedent(printed) : printed;'''
new='''          shouldBreak: isModuleConfiguration || (isSCSSMapItem && !isKey),
        }
      );

      return isKey || isModuleConfiguration ? dedent(printed) : printed;'''
assert s.count(old)==1; s=s.replace(old,new)
open(p,'w').write(s)
EOF
git diff src/language-css/printer-postcss.js; ../bin/envrun './bin/prettier.js repro.scss > out.scss; cat out.scss; ./bin/prettier.js out.scss | diff - out.scss && echo IDEMPOTENT'
```

tool result:

```
diff --git a/src/language-css/printer-postcss.js b/src/language-css/printer-postcss.js
index 0c326d6d2..6225a092d 100644
--- a/src/language-css/printer-postcss.js
+++ b/src/language-css/printer-postcss.js
@@ -64,6 +64,7 @@ const {
   isTemplatePropNode,
   isPostcssSimpleVarNode,
   isSCSSMapItemNode,
+  isSCSSModuleConfigurationNode,
   isInlineValueCommentNode,
   isHashNode,
   isLeftCurlyBraceNode,
@@ -872,6 +873,7 @@ function genericPrint(path, options, print) {
       const lastItem = getLast(node.groups);
       const isLastItemComment = lastItem && lastItem.type === "value-comment";
       const isKey = isKeyInValuePairNode(node, parentNode);
+      const isModuleConfiguration = isSCSSModuleConfigurationNode(path);
 
       const printed = group(
         [
@@ -915,11 +917,11 @@ function genericPrint(path, options, print) {
           node.close ? print("close") : "",
         ],
         {
-          shouldBreak: isSCSSMapItem && !isKey,
+          shouldBreak: isModuleConfiguration || (isSCSSMapItem && !isKey),
         }
       );
 
-      return isKey ? dedent(printed) : printed;
+      return isKey || isModuleConfiguration ? dedent(printed) : printed;
     }
     case "value-func": {
       return [
@use "@fylgja/base" with
  (
  $family-main: (
    Rubik,
    Roboto,
    system-ui,
    sans-serif,
  ),
  $font-weight: 350,
  $h1-font-weight: 500,
  $h2-font-weight: 500,
  $h3-font-weight: 500
);
@use "library" with
  (
  $black: #222,
  $border-radius: 0.1rem
);
@use "library" with
  (
  $black: #222,
  $border-radius: 0.1rem,
  $font-family: "Helvetica, sans-serif"
);
@use "lib" with
  (
  $a: (
    b: c,
    d: e,
  )
);
@use "lib" with
  (
  $a: f(1, 2)
);
IDEMPOTENT
```

**assistant:** Indentation and commas are fixed now. `fill` still puts a line break before `(` because it measures the next item as if it were flat, so I'm adding back the explicit space after `with`:

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/prettier__prettier-11637/repo/src/language-css/printer-postcss.js",
 "old_string": "        // Formatting `grid` property\n        if (isGridValue) {",
 "new_string": "        // Keep module configuration on the same line as `with` in SCSS (i.e. `@use \"library\" with ($black: #222)`)\n        if (\n          atRuleAncestorNode &&\n          [\"use\", \"forward\"].includes(atRuleAncestorNode.name.toLowerCase()) &&\n          iNode.type === \"value-word\" &&\n          iNode.value === \"with\" &&\n          iNextNode.type === \"value-paren_group\"\n        ) {\n          parts.push(\" \");\n\n          continue;\n        }\n\n        // Formatting `grid` property\n        if (isGridValue) {"
}
```

tool result:

```
The file /work/prettier__prettier-11637/repo/src/language-css/printer-postcss.js has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-11637/repo; printf '@use "lib" as x with ($a: 1);\n@use "lib" with ($a: 1) ;\n' >> repro.scss; ../bin/envrun './bin/prettier.js repro.scss > out.scss; cat out.scss; ./bin/prettier.js out.scss | diff - out.scss && echo IDEMPOTENT'
```

tool result:

```
@use "@fylgja/base" with (
  $family-main: (
    Rubik,
    Roboto,
    system-ui,
    sans-serif,
  ),
  $font-weight: 350,
  $h1-font-weight: 500,
  $h2-font-weight: 500,
  $h3-font-weight: 500
);
@use "library" with (
  $black: #222,
  $border-radius: 0.1rem
);
@use "library" with (
  $black: #222,
  $border-radius: 0.1rem,
  $font-family: "Helvetica, sans-serif"
);
@use "lib" with (
  $a: (
    b: c,
    d: e,
  )
);
@use "lib" with (
  $a: f(1, 2)
);
@use "lib" as x with (
  $a: 1
);
@use "lib" with (
  $a: 1
);
IDEMPOTENT
```

**assistant:** The output now matches the expected format from the issue (with Prettier's 2-space indent), and formatting it a second time gives the same result. Next I'll run the CSS/SCSS/Less tests:

**tool call: Bash**

```bash
cd /work/prettier__prettier-11637/repo; rm repro.scss out.scss; ../bin/envrun 'yarn jest tests/format/scss tests/format/less tests/format/css 2>&1 | tail -60'
```

tool result:

```
      ↵

      283 |         CURSOR_PLACEHOLDER,
      284 |       })
    > 285 |     ).toMatchSnapshot();
          |       ^
      286 |   });
      287 |
      288 |   if (!FULL_TEST) {

      at Object.<anonymous> (tests/config/format-test.js:285:7)

  ● quotes.scss - {"singleQuote":true} › format

    expect(received).toMatchSnapshot()

    Snapshot name: `quotes.scss - {"singleQuote":true} format 1`

    - Snapshot  - 2
    + Received  + 4

    @@ -29,12 +29,14 @@
      @forward "library" as btn*;

      =====================================output=====================================
      @use 'library';

    - @use 'library' with
    -   ($black: #222, $border-radius: 0.1rem $font-family: 'Helvetica, sans-serif');
    + @use 'library' with (
    +   $black: #222,
    +   $border-radius: 0.1rem $font-family: 'Helvetica, sans-serif'
    + );

      @use 'library' as *;

      @use 'library' as f;
      ↵

      283 |         CURSOR_PLACEHOLDER,
      284 |       })
    > 285 |     ).toMatchSnapshot();
          |       ^
      286 |   });
      287 |
      288 |   if (!FULL_TEST) {

      at Object.<anonymous> (tests/config/format-test.js:285:7)


Snapshot Summary
 › 2 snapshots failed from 1 test suite. Inspect your code changes or re-run jest with `-u` to update them.

Test Suites: 1 failed, 55 passed, 56 total
Tests:       2 failed, 182 passed, 184 total
Snapshots:   2 failed, 178 passed, 180 total
Time:        4.189 s
Ran all test suites matching /tests\/format\/scss|tests\/format\/less|tests\/format\/css/i.
error Command failed with exit code 1.
info Visit https://yarnpkg.com/en/docs/cli/run for documentation about this command.
```

**assistant:** Only the old `quotes.scss` snapshot fails, because it recorded the buggy `with\n  (...)` output. Last, a lint check on the changed files:

**tool call: Bash**

```bash
cd /work/prettier__prettier-11637/repo; ../bin/envrun 'npx eslint src/language-css/utils.js src/language-css/printer-postcss.js && npx prettier --check src/language-css/utils.js src/language-css/printer-postcss.js'; git status --short
```

tool result:

```
Browserslist: caniuse-lite is outdated. Please run:
  npx browserslist@latest --update-db
  Why you should do it regularly: https://github.com/browserslist/browserslist#browsers-data-updating
Checking formatting...
All matched files use Prettier code style!

 M package.json
 M src/language-css/printer-postcss.js
 M src/language-css/utils.js
?? Dockerfile
```

**assistant:** SCSS `@use ... with (...)` now formats the way the issue expects. The input from the issue comes out as:

```scss
@use "@fylgja/base" with (
  $family-main: (
    Rubik,
    Roboto,
    system-ui,
    sans-serif,
  ),
  $font-weight: 350,
  $h1-font-weight: 500,
  $h2-font-weight: 500,
  $h3-font-weight: 500
);
```

Indentation is Prettier's usual 2 spaces. Formatting the output again changes nothing.

**What was wrong:** there were two problems.
1. Prettier was allowed to break the line between `with` and `(`, and did whenever the rule was too long.
2. The `(...)` block sat inside the indentation of the surrounding rule, so it and everything in it got an extra indent.

**Changes:**
- **`src/language-css/utils.js`:** a new helper, `isSCSSModuleConfigurationNode`, recognises a `(...)` block that directly follows the word `with` inside `@use` or `@forward`.
- **`src/language-css/printer-postcss.js`:**
  - `with` and `(` are always separated by a plain space, so they stay on one line.
  - The configuration block always breaks onto one item per line and is un-indented, the same way SCSS map keys already are. No trailing comma is added after the last item.

Short configurations are also expanded one item per line, so `@use "lib" with ($a: 1);` becomes three lines. That matches how SCSS maps (`$map: (key: value)`) are already formatted.

**Tests:** I ran the CSS, SCSS and Less format tests: 182 pass and 2 fail. The failures are both versions of the existing `tests/format/scss/quotes` snapshot, which recorded the old broken output (`@use "library" with` followed by `(` on the next line). That is exactly what this fix changes, so those snapshots need regenerating; I didn't touch them since you said you're handling the tests. ESLint and Prettier's own style check pass on the changed files, and I deleted my scratch files.

**Separate bug, not fixed:** `@forward "lib" with ($a: 1)` crashes Prettier with `TypeError: Cannot read properties of undefined (reading 'type')`, and it did before my change too. The cause is the existing `@forward` wildcard check in `printer-postcss.js`, which reads `iPrevNode.type` when `iPrevNode` is undefined. Adding an `iPrevNode &&` guard there should fix it. I left it out to keep this change focused; once that crash is fixed, `@forward ... with (...)` will get the same formatting as `@use`.

`package.json` (the `lint` script set to `echo noop`) and the untracked `Dockerfile` were already like that before I started, and I left them alone.

_session end: success, turns 22, is_error False_

## Container commands (task container, no network; broker log)

- `rc=2` 0.91 s: ./bin/prettier.js repro.scss
- `rc=0` 0.93 s: ./bin/prettier.js repro.scss
- `rc=2` 0.88 s: ./bin/prettier.js repro.scss
- `rc=2` 0.75 s: ./bin/prettier.js repro.scss
- `rc=0` 1.79 s: ./bin/prettier.js repro.scss > out.scss; cat out.scss; ./bin/prettier.js out.scss | diff - out.scss && echo IDEMPOTENT
- `rc=0` 1.8 s: ./bin/prettier.js repro.scss > out.scss; cat out.scss; ./bin/prettier.js out.scss | diff - out.scss && echo IDEMPOTENT
- `rc=0` 1.83 s: ./bin/prettier.js repro.scss > out.scss; cat out.scss; ./bin/prettier.js out.scss | diff - out.scss && echo IDEMPOTENT
- `rc=0` 8.1 s: yarn jest tests/format/scss tests/format/less tests/format/css 2>&1 | tail -60
- `rc=0` 5.2 s: npx eslint src/language-css/utils.js src/language-css/printer-postcss.js && npx prettier --check src/language-css/utils.js src/language-css/printer-postcss.js
