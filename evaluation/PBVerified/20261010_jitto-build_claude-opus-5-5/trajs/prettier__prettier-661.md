# Instance: prettier__prettier-661

- Final resolved (evaluator, logs/prettier__prettier-661_result.json): True
- Run state: DONE
- One attempt. Duration 31.6 s, turns 6, actor cost $0.1383076, container commands 1
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/prettier__prettier-661/repo
</uploaded_files>
I've uploaded a JavaScript code repository in the directory /work/prettier__prettier-661/repo. Consider the following issue description:

<issue_description>
JSX opening element closing tag gets moved to a new line
If you have a line of JSX that is over printWidth, something like:

```js
const El = (<span width="1" height="2">x</span>)
```

For the sake of reproducing the issue assume the printWidth is set to 20 but this reproduces anytime the line needs to break for JSX. Then the code is formatted as:

```js
const El = (
    <span
        width="1"
        height="2"
    >
        x
    </span>
);
```

Notice the span `>` being placed on a new line by itself. 
Again this wastes lots of vertical space whenever you have many tags in a component. Instead a better option would be either to make it configurable or to place it on the same line as the last prop, eg:

```js
const El = (
    <span
        width="1"
        height="2" >
        x
    </span>
);
```

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/prettier__prettier-661/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/prettier__prettier-661/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/prettier__prettier-661/bin/envrun 'git status --short && ls'
Edits you make under /work/prettier__prettier-661/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
grep -n "JSXOpeningElement" -A40 src/printer.js | head -70; cat src/options.js; git log --oneline -1; ls tests | grep -i jsx; grep -rn "jsxBracket\|BracketSameLine" tests bin src README.md | head
```

tool result:

```
1190:    case "JSXOpeningElement": {
1191-      const n = path.getValue();
1192-
1193-      // don't break up opening elements with a single long text attribute
1194-      if (
1195-        n.attributes.length === 1 &&
1196-          n.attributes[0].value &&
1197-          n.attributes[0].value.type === "Literal" &&
1198-          typeof n.attributes[0].value.value === "string"
1199-      ) {
1200-        return group(
1201-          concat([
1202-            "<",
1203-            path.call(print, "name"),
1204-            " ",
1205-            concat(path.map(print, "attributes")),
1206-            n.selfClosing ? " />" : ">"
1207-          ])
1208-        );
1209-      }
1210-
1211-      return group(
1212-        concat([
1213-          "<",
1214-          path.call(print, "name"),
1215-          concat([
1216-            indent(
1217-              options.tabWidth,
1218-              concat(
1219-                path.map(attr => concat([line, print(attr)]), "attributes")
1220-              )
1221-            ),
1222-            n.selfClosing ? line : softline
1223-          ]),
1224-          n.selfClosing ? "/>" : ">"
1225-        ])
1226-      );
1227-    }
1228-    case "JSXClosingElement":
1229-      return concat(["</", path.call(print, "name"), ">"]);
1230-    case "JSXText":
"use strict";

var validate = require("jest-validate").validate;
var deprecatedConfig = require("./deprecated");

var defaults = {
  // Number of spaces the pretty-printer should use per tab
  tabWidth: 2,
  // Fit code within this line limit
  printWidth: 80,
  // If true, will use single instead of double quotes
  singleQuote: false,
  // Controls the printing of trailing commas wherever possible
  trailingComma: false,
  // Controls the printing of spaces inside array and objects
  bracketSpacing: true,
  // Which parser to use. Valid options are 'flow' and 'babylon'
  parser: "babylon"
};

var exampleConfig = Object.assign({}, defaults, {
  filename: "testFilename",
  printWidth: 80,
  originalText: "text"
});

// Copy options and fill in default values.
function normalize(options) {
  validate(options, { exampleConfig, deprecatedConfig });
  const normalized = Object.assign({}, options || {});

  // For backward compatibility. Deprecated in 0.0.10
  if ("useFlowParser" in normalized) {
    normalized.parser = normalized.useFlowParser ? "flow" : "babylon";
    delete normalized.useFlowParser;
  }

  Object.keys(defaults).forEach(k => {
    if (normalized[k] == null) {
      normalized[k] = defaults[k];
    }
  });

  return normalized;
}

module.exports = { normalize };
ec6ffbe Properly support member chains comments (#668)
jsx
jsx-multiline-assign
jsx-newlines
jsx-significant-space
jsx-split-attrs
jsx-stateless-arrow-fn
jsx_escape
```

**tool call: Bash**

```bash
cat tests/jsx-split-attrs/jsfmt.spec.js tests/jsx/jsfmt.spec.js; git status; grep -rln "jsx" tests/*/jsfmt.spec.js; grep -n "bracket" README.md bin/prettier.js
```

tool result:

```
run_spec(__dirname);
run_spec(__dirname);
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   package.json
	modified:   yarn.lock

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Dockerfile

no changes added to commit (use "git add" and/or "git commit -a")
README.md:149:  bracketSpacing: true,
bin/prettier.js:18:    "bracket-spacing",
bin/prettier.js:32:  default: { color: true, "bracket-spacing": true, parser: "babylon" },
bin/prettier.js:61:      "  --bracket-spacing        Put spaces between brackets. Defaults to true.\n" +
bin/prettier.js:67:      "  --no-bracket-spacing\n" +
bin/prettier.js:68:      "  --bracket-spacing=false"
bin/prettier.js:125:  bracketSpacing: argv["bracket-spacing"],
```

**tool call: Bash**

```bash
sed -n 10,40p bin/prettier.js; sed -n 55,75p bin/prettier.js; sed -n 115,135p bin/prettier.js; sed -n 130,160p README.md
```

tool result:

````
const prettier = require("../index");

const argv = minimist(process.argv.slice(2), {
  boolean: [
    "write",
    "stdin",
    "single-quote",
    "trailing-comma",
    "bracket-spacing",
    // The supports-color package (a sub sub dependency) looks directly at
    // `process.argv` for `--no-color` and such-like options. The reason it is
    // listed here is to avoid "Ignored unknown option: --no-color" warnings.
    // See https://github.com/chalk/supports-color/#info for more information.
    "color",
    "help",
    "version",
    "debug-print-doc",
    "debug-check",
    // Deprecated in 0.0.10
    "flow-parser"
  ],
  string: ["print-width", "tab-width", "parser"],
  default: { color: true, "bracket-spacing": true, parser: "babylon" },
  alias: { help: "h", version: "v" },
  unknown: param => {
    if (param.startsWith("-")) {
      console.warn("Ignored unknown option: " + param + "\n");
      return false;
    }
  }
});
      "  --write                  Edit the file in-place. (Beware!)\n" +
      "  --stdin                  Read input from stdin.\n" +
      "  --print-width <int>      Specify the length of line that the printer will wrap on. Defaults to 80.\n" +
      "  --tab-width <int>        Specify the number of spaces per indentation-level. Defaults to 2.\n" +
      "  --single-quote           Use single quotes instead of double.\n" +
      "  --trailing-comma         Print trailing commas wherever possible.\n" +
      "  --bracket-spacing        Put spaces between brackets. Defaults to true.\n" +
      "  --parser <flow|babylon>  Specify which parse to use. Defaults to babylon.\n" +
      "  --color                  Colorize error messages. Defaults to true.\n" +
      "  --version                Print prettier version.\n" +
      "\n" +
      "Boolean options can be turned off like this:\n" +
      "  --no-bracket-spacing\n" +
      "  --bracket-spacing=false"
  );
  process.exit(argv["help"] ? 0 : 1);
}

function getParserOption() {
  const optionName = "parser";
  const value = argv[optionName];
      optionName +
      " value. Expected an integer, but received: " +
      JSON.stringify(value)
  );
  process.exit(1);
}

const options = {
  printWidth: getIntOption("print-width"),
  tabWidth: getIntOption("tab-width"),
  bracketSpacing: argv["bracket-spacing"],
  parser: getParserOption(),
  singleQuote: argv["single-quote"],
  trailingComma: argv["trailing-comma"]
};

function format(input) {
  if (argv["debug-print-doc"]) {
    const doc = prettier.__debug.printToDoc(input, options);
    return prettier.__debug.formatDoc(doc);
  }
argument is optional, and all of the defaults are shown below:

```js
const prettier = require("prettier");

prettier.format(source, {
  // Fit code within this line limit
  printWidth: 80,

  // Number of spaces it should use per tab
  tabWidth: 2,

  // If true, will use single instead of double quotes
  singleQuote: false,

  // Controls the printing of trailing commas wherever possible
  trailingComma: false,

  // Controls the printing of spaces inside object literals
  bracketSpacing: true,

  // Which parser to use. Valid options are 'flow' and 'babylon'
  parser: 'babylon'
});
```

### Atom

Atom users can simply install the `prettier-atom` package and use
ctrl+alt+f to format a file (or format on save if turned on).
````

**assistant:** I'll add a `jsxBracketSameLine` option (default `false`, preserving existing behavior) and wire it through the printer, options, CLI, and README.

**tool call: Bash**

```bash
python3 - <<'EOF'
import re
def sub(path, old, new):
    s=open(path).read(); assert old in s, (path, old); open(path,'w').write(s.replace(old,new,1))
sub('src/printer.js', '''      return group(
        concat([
          "<",
          path.call(print, "name"),
          concat([
            indent(
              options.tabWidth,
              concat(
                path.map(attr => concat([line, print(attr)]), "attributes")
              )
            ),
            n.selfClosing ? line : softline
          ]),
          n.selfClosing ? "/>" : ">"
        ])
      );''', '''      const bracketSameLine = options.jsxBracketSameLine;

      return group(
        concat([
          "<",
          path.call(print, "name"),
          concat([
            indent(
              options.tabWidth,
              concat(
                path.map(attr => concat([line, print(attr)]), "attributes")
              )
            ),
            n.selfClosing ? line : bracketSameLine ? ">" : softline
          ]),
          n.selfClosing ? "/>" : bracketSameLine ? "" : ">"
        ])
      );''')
sub('src/options.js', '''  bracketSpacing: true,
''', '''  bracketSpacing: true,
  // Puts the `>` of a multi-line jsx element at the end of the last line
  jsxBracketSameLine: false,
''')
sub('bin/prettier.js', '''    "bracket-spacing",
''', '''    "bracket-spacing",
    "jsx-bracket-same-line",
''')
sub('bin/prettier.js', '''Defaults to true.\\n" +
''', '''Defaults to true.\\n" +
      "  --jsx-bracket-same-line  Put > on the last line instead of at a new line.\\n" +
''')
sub('bin/prettier.js', '''  bracketSpacing: argv["bracket-spacing"],
''', '''  bracketSpacing: argv["bracket-spacing"],
  jsxBracketSameLine: argv["jsx-bracket-same-line"],
''')
sub('README.md', '''  bracketSpacing: true,
''', '''  bracketSpacing: true,

  // If true, puts the `>` of a multi-line jsx element at the end of
  // the last line instead of being alone on the next line
  jsxBracketSameLine: false,
''')
EOF
git diff --stat
```

tool result:

```
 README.md       | 4 ++++
 bin/prettier.js | 3 +++
 package.json    | 7 ++++---
 src/options.js  | 2 ++
 src/printer.js  | 6 ++++--
 yarn.lock       | 3 ++-
 6 files changed, 19 insertions(+), 6 deletions(-)
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-661 && bin/envrun 'printf "const El = (<span width=\"1\" height=\"2\">x</span>);\nconst B = <img width=\"1\" height=\"2\" />;\n" > /tmp/a.js && node bin/prettier.js --print-width 20 /tmp/a.js && echo ---- && node bin/prettier.js --print-width 20 --jsx-bracket-same-line /tmp/a.js && yarn test 2>&1 | tail -8'
```

tool result:

```
const El = (
  <span
    width="1"
    height="2"
  >
    x
  </span>
);
const B = (
  <img
    width="1"
    height="2"
  />
);
----
const El = (
  <span
    width="1"
    height="2">
    x
  </span>
);
const B = (
  <img
    width="1"
    height="2"
  />
);
 PASS  tests/jsx-newlines/jsfmt.spec.js

Test Suites: 431 passed, 431 total
Tests:       1214 passed, 1214 total
Snapshots:   1214 passed, 1214 total
Time:        3.749s
Ran all test suites.
Done in 5.27s.
Shell cwd was reset to /work/prettier__prettier-661/repo
```

**assistant:** I added a new option, `jsxBracketSameLine`. When it's on and a JSX opening tag has to break across lines, the `>` goes at the end of the last attribute line instead of on its own line. It's off by default, so existing output doesn't change.

With `--print-width 20 --jsx-bracket-same-line`, the issue's example now prints:

```js
const El = (
  <span
    width="1"
    height="2">
    x
  </span>
);
```

Without the flag it still prints the old way. Two things differ from what the issue sketched:
- **No space before `>`:** you get `height="2">`, not `height="2" >`.
- **Self-closing tags are unchanged:** a broken `<img ... />` still puts `/>` on its own line, even with the option on.

**Changes:**
- `src/printer.js` (JSX opening element): with the option on, the `>` is printed right after the attributes instead of after a line break.
- `src/options.js`: the new option, defaulting to `false`.
- `bin/prettier.js`: a `--jsx-bracket-same-line` flag, with a line in the help text.
- `README.md`: the option added to the documented defaults.

**Testing:** I ran the example above with and without the flag, and the full test suite passed (431 suites, 1214 tests). I made the default "off" so the existing snapshots stay the same; I don't know exactly how the tests you added set the option. The only reproduction file I made was in the container's `/tmp`, so the repo has nothing extra in it.

`package.json` and `yarn.lock` were already modified before I started, and I didn't touch them.

_session end: success, turns 6, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 6.51 s: printf "const El = (<span width=\"1\" height=\"2\">x</span>);\nconst B = <img width=\"1\" height=\"2\" />;\n" > /tmp/a.js && node bin/prettier.js --print-width 20 /tmp/a.js && echo ---- && node bin/prettier.js --print-width 20 --jsx-bracket-same-line /tmp/a.js && yarn test 2>&1 | tail -8
