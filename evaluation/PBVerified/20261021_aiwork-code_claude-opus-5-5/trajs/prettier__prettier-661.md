# Instance: prettier__prettier-661
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: True

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
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
````

## Operational trajectory

### Turn 1 — thinking

````text
This looks like an older Prettier version, and I recall there's a `jsxBracketSameLine` option that was added later. Let me check the repo to confirm.
````

### Turn 1 — tool call call_0001 (exec)

````json
{
 "command": "cd /testbed && git log --oneline -2 && grep -rn \"bracketSameLine\\|BracketSameLine\" src/ tests/ bin/ docs 2>/dev/null | head -30; ls; grep -n \"JSXOpeningElement\" -A40 src/printer.js | head -80"
}
````

Result:

````text
{
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "success",
  "exit_code": 0,
  "retryability": "not_needed",
  "open_work_at_failure": false
 },
 "stdout": "ec6ffbe Properly support member chains comments (#668)\nc4b83c7 Ensure that all comments are printed (#571)\nCHANGELOG.md\nDockerfile\nLICENSE\nREADME.md\nRationale.md\nbin\ncommands.md\ndocs\neditors\nindex.js\nnode_modules\npackage.json\nsrc\ntests\ntests_config\ntmp\nyarn.lock\n1190:    case \"JSXOpeningElement\": {\n1191-      const n = path.getValue();\n1192-\n1193-      // don't break up opening elements with a single long text attribute\n1194-      if (\n1195-        n.attributes.length === 1 &&\n1196-          n.attributes[0].value &&\n1197-          n.attributes[0].value.type === \"Literal\" &&\n1198-          typeof n.attributes[0].value.value === \"string\"\n1199-      ) {\n1200-        return group(\n1201-          concat([\n1202-            \"<\",\n1203-            path.call(print, \"name\"),\n1204-            \" \",\n1205-            concat(path.map(print, \"attributes\")),\n1206-            n.selfClosing ? \" />\" : \">\"\n1207-          ])\n1208-        );\n1209-      }\n1210-\n1211-      return group(\n1212-        concat([\n1213-          \"<\",\n1214-          path.call(print, \"name\"),\n1215-          concat([\n1216-            indent(\n1217-              options.tabWidth,\n1218-              concat(\n1219-                path.map(attr => concat([line, print(attr)]), \"attributes\")\n1220-              )\n1221-            ),\n1222-            n.selfClosing ? line : softline\n1223-          ]),\n1224-          n.selfClosing ? \"/>\" : \">\"\n1225-        ])\n1226-      );\n1227-    }\n1228-    case \"JSXClosingElement\":\n1229-      return concat([\"</\", path.call(print, \"name\"), \">\"]);\n1230-    case \"JSXText\":\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 290,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed",
   "bin/",
   "docs",
   "src/",
   "src/printer.js",
   "tests/"
  ],
  "command_sha256": [
   "5a990bc4bbda28e6929eeeb83321310ed861434d80b2542c02c46222f2a5b5a9"
  ]
 }
}
````

### Turn 2 — thinking

````text
I recall that an older prettier fix introduced the `jsxBracketSameLine` option, so I want to check options.js and its tests for references to that setting.
````

### Turn 2 — tool call call_0002 (exec)

````json
{
 "command": "cd /testbed && grep -rn \"SameLine\\|bracket\" --include=*.js -i src tests bin tests_config index.js | grep -v node_modules | head; cat src/options.js; grep -n \"bracket\\|Spacing\" bin/prettier.js README.md"
}
````

Result:

````text
{
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "success",
  "exit_code": 0,
  "retryability": "not_needed",
  "open_work_at_failure": false
 },
 "stdout": "src/util.js:268:function htmlEscapeInsideAngleBracket(str) {\nsrc/util.js:271:  // angle bracket context\nsrc/util.js:319:  htmlEscapeInsideAngleBracket\nsrc/options.js:16:  bracketSpacing: true,\nsrc/printer.js:477:                    options.bracketSpacing ? line : softline,\nsrc/printer.js:482:                options.bracketSpacing ? line : softline,\nsrc/printer.js:649:                options.bracketSpacing ? line : softline,\nsrc/printer.js:656:              concat([options.bracketSpacing ? line : softline, rightBrace])\nsrc/printer.js:687:        if (shouldPrintSameLine(n.value)) {\nsrc/printer.js:914:        const hasBraces = isCurlyBracket(con);\n\"use strict\";\n\nvar validate = require(\"jest-validate\").validate;\nvar deprecatedConfig = require(\"./deprecated\");\n\nvar defaults = {\n  // Number of spaces the pretty-printer should use per tab\n  tabWidth: 2,\n  // Fit code within this line limit\n  printWidth: 80,\n  // If true, will use single instead of double quotes\n  singleQuote: false,\n  // Controls the printing of trailing commas wherever possible\n  trailingComma: false,\n  // Controls the printing of spaces inside array and objects\n  bracketSpacing: true,\n  // Which parser to use. Valid options are 'flow' and 'babylon'\n  parser: \"babylon\"\n};\n\nvar exampleConfig = Object.assign({}, defaults, {\n  filename: \"testFilename\",\n  printWidth: 80,\n  originalText: \"text\"\n});\n\n// Copy options and fill in default values.\nfunction normalize(options) {\n  validate(options, { exampleConfig, deprecatedConfig });\n  const normalized = Object.assign({}, options || {});\n\n  // For backward compatibility. Deprecated in 0.0.10\n  if (\"useFlowParser\" in normalized) {\n    normalized.parser = normalized.useFlowParser ? \"flow\" : \"babylon\";\n    delete normalized.useFlowParser;\n  }\n\n  Object.keys(defaults).forEach(k => {\n    if (normalized[k] == null) {\n      normalized[k] = defaults[k];\n    }\n  });\n\n  return normalized;\n}\n\nmodule.exports = { normalize };\nbin/prettier.js:18:    \"bracket-spacing\",\nbin/prettier.js:32:  default: { color: true, \"bracket-spacing\": true, parser: \"babylon\" },\nbin/prettier.js:61:      \"  --bracket-spacing        Put spaces between brackets. Defaults to true.\\n\" +\nbin/prettier.js:67:      \"  --no-bracket-spacing\\n\" +\nbin/prettier.js:68:      \"  --bracket-spacing=false\"\nbin/prettier.js:125:  bracketSpacing: argv[\"bracket-spacing\"],\nREADME.md:149:  bracketSpacing: true,\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 145,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed",
   "README.md",
   "bin",
   "bin/prettier.js",
   "index.js",
   "src",
   "src/options.js",
   "tests",
   "tests_config"
  ],
  "command_sha256": [
   "84c78c04e069fc86e290f3da388687b467d331fc252f3ad0e877f4437f00335d"
  ]
 }
}
````

### Turn 3 — thinking

````text
I'm figuring out that prettier added a `jsxBracketSameLine` option and need to implement it in the JSX printing logic, modifying how the opening tag's closing bracket gets placed relative to the element name.
````

### Turn 4 — assistant text

The fix is to add a `jsxBracketSameLine` option (default `false`), in line with how prettier handles other style options.

### Turn 4 — tool call call_0003 (exec)

````json
{
 "command": "cd /testbed && sed -n 10,40p bin/prettier.js; sed -n 55,75p bin/prettier.js; sed -n 118,130p bin/prettier.js; sed -n 135,160p README.md"
}
````

Result:

````text
{
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "success",
  "exit_code": 0,
  "retryability": "not_needed",
  "open_work_at_failure": false
 },
 "stdout": "const prettier = require(\"../index\");\n\nconst argv = minimist(process.argv.slice(2), {\n  boolean: [\n    \"write\",\n    \"stdin\",\n    \"single-quote\",\n    \"trailing-comma\",\n    \"bracket-spacing\",\n    // The supports-color package (a sub sub dependency) looks directly at\n    // `process.argv` for `--no-color` and such-like options. The reason it is\n    // listed here is to avoid \"Ignored unknown option: --no-color\" warnings.\n    // See https://github.com/chalk/supports-color/#info for more information.\n    \"color\",\n    \"help\",\n    \"version\",\n    \"debug-print-doc\",\n    \"debug-check\",\n    // Deprecated in 0.0.10\n    \"flow-parser\"\n  ],\n  string: [\"print-width\", \"tab-width\", \"parser\"],\n  default: { color: true, \"bracket-spacing\": true, parser: \"babylon\" },\n  alias: { help: \"h\", version: \"v\" },\n  unknown: param => {\n    if (param.startsWith(\"-\")) {\n      console.warn(\"Ignored unknown option: \" + param + \"\\n\");\n      return false;\n    }\n  }\n});\n      \"  --write                  Edit the file in-place. (Beware!)\\n\" +\n      \"  --stdin                  Read input from stdin.\\n\" +\n      \"  --print-width <int>      Specify the length of line that the printer will wrap on. Defaults to 80.\\n\" +\n      \"  --tab-width <int>        Specify the number of spaces per indentation-level. Defaults to 2.\\n\" +\n      \"  --single-quote           Use single quotes instead of double.\\n\" +\n      \"  --trailing-comma         Print trailing commas wherever possible.\\n\" +\n      \"  --bracket-spacing        Put spaces between brackets. Defaults to true.\\n\" +\n      \"  --parser <flow|babylon>  Specify which parse to use. Defaults to babylon.\\n\" +\n      \"  --color                  Colorize error messages. Defaults to true.\\n\" +\n      \"  --version                Print prettier version.\\n\" +\n      \"\\n\" +\n      \"Boolean options can be turned off like this:\\n\" +\n      \"  --no-bracket-spacing\\n\" +\n      \"  --bracket-spacing=false\"\n  );\n  process.exit(argv[\"help\"] ? 0 : 1);\n}\n\nfunction getParserOption() {\n  const optionName = \"parser\";\n  const value = argv[optionName];\n  );\n  process.exit(1);\n}\n\nconst options = {\n  printWidth: getIntOption(\"print-width\"),\n  tabWidth: getIntOption(\"tab-width\"),\n  bracketSpacing: argv[\"bracket-spacing\"],\n  parser: getParserOption(),\n  singleQuote: argv[\"single-quote\"],\n  trailingComma: argv[\"trailing-comma\"]\n};\n\nprettier.format(source, {\n  // Fit code within this line limit\n  printWidth: 80,\n\n  // Number of spaces it should use per tab\n  tabWidth: 2,\n\n  // If true, will use single instead of double quotes\n  singleQuote: false,\n\n  // Controls the printing of trailing commas wherever possible\n  trailingComma: false,\n\n  // Controls the printing of spaces inside object literals\n  bracketSpacing: true,\n\n  // Which parser to use. Valid options are 'flow' and 'babylon'\n  parser: 'babylon'\n});\n```\n\n### Atom\n\nAtom users can simply install the `prettier-atom` package and use\nctrl+alt+f to format a file (or format on save if turned on).\n\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 96,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed",
   "README.md",
   "bin/prettier.js"
  ],
  "command_sha256": [
   "db854191cf61b7c346c1bbdb5496e01d5d3f04f9e6d4b184e7ca916d76f1e127"
  ]
 }
}
````

### Turn 5 — tool call call_0004 (apply_patch)

````json
{
 "patch_text": "*** Begin Patch\n*** Update File: src/printer.js\n@@\n-            n.selfClosing ? line : softline\n+            n.selfClosing ? line : options.jsxBracketSameLine ? \">\" : softline\n           ]),\n-          n.selfClosing ? \"/>\" : \">\"\n+          n.selfClosing ? \"/>\" : options.jsxBracketSameLine ? \"\" : \">\"\n         ])\n*** Update File: src/options.js\n@@\n   bracketSpacing: true,\n+  // Puts the `>` of a multi-line jsx element at the end of the last line\n+  jsxBracketSameLine: false,\n*** Update File: bin/prettier.js\n@@\n     \"bracket-spacing\",\n+    \"jsx-bracket-same-line\",\n@@\n       \"  --bracket-spacing        Put spaces between brackets. Defaults to true.\\n\" +\n+      \"  --jsx-bracket-same-line  Put > on the last line instead of at a new line.\\n\" +\n@@\n   bracketSpacing: argv[\"bracket-spacing\"],\n+  jsxBracketSameLine: argv[\"jsx-bracket-same-line\"],\n*** Update File: README.md\n@@\n   bracketSpacing: true,\n \n+  // If true, puts the `>` of a multi-line jsx element at the end of\n+  // the last line instead of being alone on the next line\n+  jsxBracketSameLine: false,\n+\n*** End Patch"
}
````

Result:

````text
{
 "plan_id": "da25e6027d0fd75f755aba6c4607571cc92b5383c7d07297a4bbd130ecf59b54",
 "applied": true,
 "files_modified": [
  "src/printer.js",
  "src/options.js",
  "bin/prettier.js",
  "README.md"
 ],
 "conflicts": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "apply_patch",
    "paths": [
     "src/printer.js",
     "src/options.js",
     "bin/prettier.js",
     "README.md"
    ]
   }
  ]
 }
}
````

### Turn 6 — tool call call_0005 (exec)

````json
{
 "command": "cd /testbed && node -e '\nconst p=require(\"./\");const s=\"const El = (<span width=\\\"1\\\" height=\\\"2\\\">x</span>);\\nconst B = <img width=\\\"1\\\" height=\\\"2\\\" />;\";\nconsole.log(p.format(s,{printWidth:20,jsxBracketSameLine:true}));console.log(p.format(s,{printWidth:20}));' && echo '<span width=\"1\" height=\"2\">x</span>' | node bin/prettier.js --stdin --print-width 20 --jsx-bracket-same-line && npx jest 2>&1 | tail -5"
}
````

Result:

````text
{
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "success",
  "exit_code": 0,
  "retryability": "not_needed",
  "open_work_at_failure": false
 },
 "stdout": "const El = (\n  <span\n    width=\"1\"\n    height=\"2\">\n    x\n  </span>\n);\nconst B = (\n  <img\n    width=\"1\"\n    height=\"2\"\n  />\n);\n\nconst El = (\n  <span\n    width=\"1\"\n    height=\"2\"\n  >\n    x\n  </span>\n);\nconst B = (\n  <img\n    width=\"1\"\n    height=\"2\"\n  />\n);\n\n<span\n  width=\"1\"\n  height=\"2\">\n  x\n</span>;\nTest Suites: 431 passed, 431 total\nTests:       1214 passed, 1214 total\nSnapshots:   1214 passed, 1214 total\nTime:        66.771s\nRan all test suites.\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 70566,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed"
  ],
  "command_sha256": [
   "9b0e96d72e2004acb4d1e2bb9b3782a1a752e914cfafe17ee5ff333b9ad03773"
  ]
 }
}
````

### Turn 7 — thinking

````text
I notice the suggested formatting had a space before the closing bracket, but the standard style omits it, so I'll go with no space there.

I made this fix configurable as an option rather than changing default behavior, keeping existing users unaffected. I also noticed a minor formatting difference—my output omits the space before the closing bracket that the issue's example showed, but that shouldn't matter functionally.
````

### Turn 7 — assistant text

I added a `jsxBracketSameLine` option, off by default. When it's turned on and a JSX opening tag has to break across lines, the closing `>` now goes at the end of the last prop instead of on its own line. Self-closing tags like `<img />` keep `/>` on its own line either way.

With `printWidth: 20` and `jsxBracketSameLine: true`, the example now prints:

```js
const El = (
  <span
    width="1"
    height="2">
    x
  </span>
);
```

There's no space before the `>`. The issue showed `height="2" >` as one possibility, but `height="2">` matches how the tag is printed when it fits on one line.

**Changes:**
- `src/printer.js`: the `JSXOpeningElement` case places `>` after the last prop when the option is on.
- `src/options.js`: adds the `jsxBracketSameLine` option, defaulting to `false`.
- `bin/prettier.js`: adds a `--jsx-bracket-same-line` command-line flag and its help text.
- `README.md`: documents the new option.

**Checks:**
- I formatted the example with the option on and off, both through the API and through the command-line flag, and the output was correct each time.
- The full jest suite passes: 431 suites, 1214 tests.

Because the default is off, existing output doesn't change. If you'd rather this be how JSX always prints, the fix is simply to drop the option.

### Turn 8 — assistant text

I fixed this by adding a `jsxBracketSameLine` option, which defaults to `false`. When it's turned on, the `>` of a multi-line JSX opening tag stays on the line with the last attribute. When it's off, output is the same as before.

With `printWidth: 20, jsxBracketSameLine: true`, your example now prints as:

```js
const El = (
  <span
    width="1"
    height="2">
    x
  </span>
);
```

There's no space before the `>`, unlike the `height="2" >` sketch in the issue. Self-closing tags still put `/>` on its own line in both modes.

The issue offered two options: make it configurable, or always do this. I went with configurable so existing output stays the same, which is what the current snapshot tests expect. If you'd rather make this the default, the change in `src/printer.js` is small but some snapshots would need updating.

Changes:
- **`src/printer.js`:** the `JSXOpeningElement` case puts `>` at the end of the attribute block when the option is on.
- **`src/options.js`:** adds the default `jsxBracketSameLine: false`.
- **`bin/prettier.js`:** adds a `--jsx-bracket-same-line` flag and help text.
- **`README.md`:** documents the option.

Checks:
- I ran your example through `prettier.format` with the option on and off, and got the outputs described above.
- The CLI flag gave the same result.
- The full Jest suite passes: 431 suites, 1214 tests and snapshots.

I didn't add a test for the new option.

## Final answer

I fixed this by adding a `jsxBracketSameLine` option, which defaults to `false`. When it's turned on, the `>` of a multi-line JSX opening tag stays on the line with the last attribute. When it's off, output is the same as before.

With `printWidth: 20, jsxBracketSameLine: true`, your example now prints as:

```js
const El = (
  <span
    width="1"
    height="2">
    x
  </span>
);
```

There's no space before the `>`, unlike the `height="2" >` sketch in the issue. Self-closing tags still put `/>` on its own line in both modes.

The issue offered two options: make it configurable, or always do this. I went with configurable so existing output stays the same, which is what the current snapshot tests expect. If you'd rather make this the default, the change in `src/printer.js` is small but some snapshots would need updating.

Changes:
- **`src/printer.js`:** the `JSXOpeningElement` case puts `>` at the end of the attribute block when the option is on.
- **`src/options.js`:** adds the default `jsxBracketSameLine: false`.
- **`bin/prettier.js`:** adds a `--jsx-bracket-same-line` flag and help text.
- **`README.md`:** documents the option.

Checks:
- I ran your example through `prettier.format` with the option on and off, and got the outputs described above.
- The CLI flag gave the same result.
- The full Jest suite passes: 431 suites, 1214 tests and snapshots.

I didn't add a test for the new option.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 110652 | 2714 | 80222 | 30412 | 113366 |
