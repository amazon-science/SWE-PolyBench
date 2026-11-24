# Instance: prettier__prettier-14400
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: True

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
Script in SVG is incorrectly formatted when using HTML parser
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

**Prettier 2.7.1**
[Playground link](https://prettier.io/playground/#N4Igxg9gdgLgprEAuEAeAzgNwOYAIAeAtgDZToC8AOiABYwwAOSA9MwO4cB0bAzJxACdszAEwAGCcyzZquNgEsAJjBpUQIgCxjZNOPOx01m7SFyZ5cNgCEI+NWNwPNuTdQB8lKJRiow8gWDEcLhgdtQAjCKyYACeajxRpgJqAGyyAGbyxMRqYACuAgIIMADCEMSC7p7e3qgAhlDyhHXwuC0wAvIARnnwAHJ1hHC5MbKYdcR5cBTUCQDckbKKBfacKegZWTnU6UVwAF5wssweXj7MfgFBp7V4mdlqUNBHpugdEADWw9T5hcVlFQEsjeAk+cAAtMR5FA4GA6gw1KC8lBFMD3l9wQplKpqIlcCCweDFHV0DQ6oU6nFcWjQRjiaSIOl0ug4DAjFUzrUGC0aLhFGoALIOEw3GA1HwNJotYLtTo9fqDb4gVGmcaTaaCyK4cIATkw4QFuu1IhoBq1AFZMOCDebjTRrXNDSIXOF9QKROE7WbnTwrQaeHbrbIunBsNDVgB2DamZbJahiTgiaO4e7bEC7OAHF64E7VMX5+qNZqtWXdXpwAZDNQEukkmiM5mssYTKYzdRzEy4ENhqCR5Ox1ZJzYPHZ7Q7HUW1ZjclSTnwz3n86hCxwc8W1SXFmX0OXlytKlVmFsa5fhCPaiPEBO26+G8+X6+4cG3+-EZ+cW3v80C89nt+P69HXCAAOD9tVA80rzA28QLA80Pygz9b3g20UP-MCvwFFDwIQr9HA-YNQ3DeNOB1fsVhIodTFTNQMyzCc83FQspRLHcywVKtqBrCF6XrJkWTFVVjzbEQO0IntVjIpYKJABMqJTLZaLHbMlDUYgSRgABldFs1zTlzgXOdmK3AAVAQGnQdJBEINo2PlCtFTUDoLKsgRCFkGAYgYJVQRgaVm3VNsHC1SI5h4FJgudRZTG7YiQHUt5tNpOBOAQQ8B1mMRkyKbyWjKZE2WoaFFDgTJGngBizlQZhsFFDAwE6BgYDnRQIHyIZYE4OpFEUABRTBigAGXkN4EDgAQAAoAHIABEAHkBTKWAhogbq4EUKaABpcAmgBKXByDcXBgEY-NIDIGBcCeEqDr5Nq8g6mBOGwVleqCR6rBiABJRRpoSrSdKm3a5lO7x5HSHbrrgfaTv08Ugku6RbqhzhuSKWA+ggErUfJYpMextG8axuAQbh-NwZ2qbuTyFkAEEixaeRoHQKbcGhfEcBh0H828BHcHrAaBFu9IJhZUn1x5mA+YqNbFGF0WSe58UUe6vqBtgYbRphSaprS-rii2nb9sO46lclmWSrl8hcA6KZxcliWKYmgBCAXxq5smJe8aQcZpuB6ZYpmyD2+2vfzABfM3vHD4Go5gH3Vf1jWRvgbXpsICA-eKcbDb2g6jthsPxTdoXrdtxXPcln3kWpumGZgIP0BDuOY9Dh345wLqeqTmBNdT8b08zlkgjqAbc+Ngu4+8Ev5eIMWp4biGJot9aPaLqvO9r-368b5vK-FSP95gVuzcPiWz4j2OxSqqQGvkJrTmq6RThATaQAgJrG+QUByVBNgAAVcZkGQCACYbBKToFfiALo5kwBfC0oqYaMJkAiznnAN+MC6hwNZJpbkfgoDYGQOXN+cBCAhh6utQaDRsB5DqC9AAYtZdo0JCEoDqL0CAUC6AkAAOo0HkPAdAeC4CaQQOgAR8hzCeRAWAdAkC37QhZAIGA-9zLYGaCghWb8ABW6B8CaRYUEAAinkCA8BNFoLfmjJRIDuHECgQwTosAeFKBUMgYCYgrGghZDw8yDAQGOOmONAaUCACOpj4CqI-pAth6BwQwnWutKBRRwn+DgKouhGikCoJZG-FkhB5BEIEFMPJhi4AmLMXACxuSQB+S6C47EyARBv2clkFhZRCBZJANMc0UC-YmTqF0GJOT0EgEwFML6KJiiaTvk1emihtIxCCNUuA4dw5AA)

```sh
# Options (if any):
--parser html
```

**Input:**

```html
<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 24 24">
	<script>
		document.addEventListener('DOMContentLoaded', () => {
			const node = document.getElementById('lastStroke');
			if (node) {
				let svg = node.parentNode.parentNode.parentNode;
				if ('pauseAnimations' in svg) {
					let hover = false;
					let loaded = false;
					node.addEventListener('endEvent', () => {
						loaded = true;
						if (!hover) {
							svg.pauseAnimations();
						}
					});
					svg.addEventListener('mouseenter', () => {
						hover = true;
						svg.unpauseAnimations();
					});
					svg.addEventListener('mouseleave', () => {
						hover = false;
						if (loaded) {
							svg.pauseAnimations();
						}
					});
				}
			}
		});	
	</script>
</svg>
```

**Output:**

```svg
<svg
  xmlns="http://www.w3.org/2000/svg"
  width="240"
  height="240"
  viewBox="0 0 24 24"
>
  <script>
    document.addEventListener('DOMContentLoaded', () => { const node =
    document.getElementById('lastStroke'); if (node) { let svg =
    node.parentNode.parentNode.parentNode; if ('pauseAnimations' in svg) { let
    hover = false; let loaded = false; node.addEventListener('endEvent', () => {
    loaded = true; if (!hover) { svg.pauseAnimations(); } });
    svg.addEventListener('mouseenter', () => { hover = true;
    svg.unpauseAnimations(); }); svg.addEventListener('mouseleave', () => {
    hover = false; if (loaded) { svg.pauseAnimations(); } }); } } });
  </script>
</svg>
```

**Expected behavior:**

Expected output to be readable.

There is no special parser for SVG, so using HTML parser to format it. However, something weird happens when there is a script inside SVG and Prettier turns it into unreadable mess.
````

## Operational trajectory

### Turn 1 — assistant text

I'll start by exploring the repository structure to understand the codebase.

### Turn 1 — tool call call_0001 (exec)

````json
{
 "command": "cd /testbed && ls && git log --oneline -3"
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
 "stdout": "CHANGELOG.md\nCODE_OF_CONDUCT.md\nCONTRIBUTING.md\nDockerfile\nLICENSE\nREADME.md\nbin\nchangelog_unreleased\ncommands.md\ncspell.json\ndocs\nindex.js\njest.config.mjs\nnetlify.toml\nnode_modules\npackage.json\nscripts\nsrc\nstandalone.js\ntests\ntmp\ntsconfig.json\ntypes\nwebsite\nyarn.lock\n6905b39ec Build(deps): Bump qs from 6.5.2 to 6.5.3 in /website (#14603)\na5a1f74d5 Build(deps): Bump minimist from 1.2.5 to 1.2.8 in /website (#14600)\n702e7b493 Build(deps): Bump async from 2.6.3 to 2.6.4 in /website (#14601)\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 887,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed"
  ],
  "command_sha256": [
   "b64bbfb39e063cc2530a7c0ae424e6fa7e568bcfa493b9fdf752c9ac669eb2e6"
  ]
 }
}
````

### Turn 2 — tool call call_0002 (exec)

````json
{
 "command": "cd /testbed && ls src/language-html && ls src/language-html/embed"
}
````

Result:

````text
{
 "tool_diagnostic": {
  "schema_version": 1,
  "code": "exec.execution.nonzero_exit",
  "failure_stage": "execution",
  "cause_domain": "local_process",
  "owner": "exec",
  "classification_source": "producer_explicit",
  "failure_scope": "invocation",
  "action": "run"
 },
 "stdout": "ast.js\nclean.js\nconditional-comment.js\nconstants.evaluate.js\nembed.js\nget-node-content.js\nget-visitor-keys.js\nindex.js\nlanguages.evaluate.js\nloc.js\noptions.js\nparser-html.js\npragma.js\nprint\nprint-preprocess.js\nprinter-html.js\nsyntax-attribute.js\nsyntax-vue.js\nutils\nvisitor-keys.js\n",
 "stderr": "ls: cannot access 'src/language-html/embed': No such file or directory\n",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed",
   "src/language-html",
   "src/language-html/embed"
  ],
  "command_sha256": [
   "37f8c737197c4e37b87d41ca7e552fd29e5f26c0a066da710e96f0f38f6e0de5"
  ]
 },
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "failed",
  "exit_code": 2,
  "failure_class": "unknown",
  "retryability": "retry_after_change",
  "open_work_at_failure": false,
  "evidence_tail": "ls: cannot access 'src/language-html/embed': No such file or directory\n"
 },
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "device_targets": [],
 "duration_ms": 253
}
````

### Turn 3 — tool call call_0003 (rg)

````json
{
 "pattern": "function (inferScriptParser|isScriptLikeTag|inferElementParser)|name === \"script\"|fullName === \"script\"",
 "path": "src/language-html",
 "context": 15
}
````

Result:

````text
{
 "output_mode": "content",
 "pattern": "function (inferScriptParser|isScriptLikeTag|inferElementParser)|name === \"script\"|fullName === \"script\"",
 "search_path": "/testbed/src/language-html",
 "matches": [
  {
   "path": "print/tag.js",
   "line_number": 251,
   "line": "    node.fullName === \"script\" &&",
   "context_before": [
    "      ? (attribute) => ignoreAttributeData.includes(attribute.rawName)",
    "      : () => false;",
    "",
    "  const printedAttributes = path.map(",
    "    ({ node: attribute }) =>",
    "      hasPrettierIgnoreAttribute(attribute)",
    "        ? replaceEndOfLine(",
    "            options.originalText.slice(locStart(attribute), locEnd(attribute))",
    "          )",
    "        : print(),",
    "    \"attrs\"",
    "  );",
    "",
    "  const forceNotToBreakAttrContent =",
    "    node.type === \"element\" &&"
   ],
   "context_after": [
    "    node.attrs.length === 1 &&",
    "    node.attrs[0].fullName === \"src\" &&",
    "    node.children.length === 0;",
    "",
    "  const shouldPrintAttributePerLine =",
    "    options.singleAttributePerLine &&",
    "    node.attrs.length > 1 &&",
    "    !isVueSfcBlock(node, options);",
    "  const attributeLine = shouldPrintAttributePerLine ? hardline : line;",
    "",
    "  /** @type {Doc[]} */",
    "  const parts = [",
    "    indent([",
    "      forceNotToBreakAttrContent ? \" \" : line,",
    "      join(attributeLine, printedAttributes),"
   ]
  },
  {
   "path": "utils/index.js",
   "line_number": 106,
   "line": "function isScriptLikeTag(node) {",
   "context_before": [
    "    return false;",
    "  }",
    "",
    "  return isPrettierIgnore(node.prev);",
    "}",
    "",
    "function isPrettierIgnore(node) {",
    "  return node.type === \"comment\" && node.value.trim() === \"prettier-ignore\";",
    "}",
    "",
    "/** there's no opening/closing tag or it's considered not breakable */",
    "function isTextLikeNode(node) {",
    "  return node.type === \"text\" || node.type === \"comment\";",
    "}",
    ""
   ],
   "context_after": [
    "  return (",
    "    node.type === \"element\" &&",
    "    (node.fullName === \"script\" ||",
    "      node.fullName === \"style\" ||",
    "      node.fullName === \"svg:style\" ||",
    "      (isUnknownNamespace(node) &&",
    "        (node.name === \"script\" || node.name === \"style\")))",
    "  );",
    "}",
    "",
    "function canHaveInterpolation(node) {",
    "  return node.children && !isScriptLikeTag(node);",
    "}",
    "",
    "function isWhitespaceSensitiveNode(node) {"
   ]
  },
  {
   "path": "utils/index.js",
   "line_number": 109,
   "line": "    (node.fullName === \"script\" ||",
   "context_before": [
    "  return isPrettierIgnore(node.prev);",
    "}",
    "",
    "function isPrettierIgnore(node) {",
    "  return node.type === \"comment\" && node.value.trim() === \"prettier-ignore\";",
    "}",
    "",
    "/** there's no opening/closing tag or it's considered not breakable */",
    "function isTextLikeNode(node) {",
    "  return node.type === \"text\" || node.type === \"comment\";",
    "}",
    "",
    "function isScriptLikeTag(node) {",
    "  return (",
    "    node.type === \"element\" &&"
   ],
   "context_after": [
    "      node.fullName === \"style\" ||",
    "      node.fullName === \"svg:style\" ||",
    "      (isUnknownNamespace(node) &&",
    "        (node.name === \"script\" || node.name === \"style\")))",
    "  );",
    "}",
    "",
    "function canHaveInterpolation(node) {",
    "  return node.children && !isScriptLikeTag(node);",
    "}",
    "",
    "function isWhitespaceSensitiveNode(node) {",
    "  return (",
    "    isScriptLikeTag(node) ||",
    "    node.type === \"interpolation\" ||"
   ]
  },
  {
   "path": "utils/index.js",
   "line_number": 113,
   "line": "        (node.name === \"script\" || node.name === \"style\")))",
   "context_before": [
    "  return node.type === \"comment\" && node.value.trim() === \"prettier-ignore\";",
    "}",
    "",
    "/** there's no opening/closing tag or it's considered not breakable */",
    "function isTextLikeNode(node) {",
    "  return node.type === \"text\" || node.type === \"comment\";",
    "}",
    "",
    "function isScriptLikeTag(node) {",
    "  return (",
    "    node.type === \"element\" &&",
    "    (node.fullName === \"script\" ||",
    "      node.fullName === \"style\" ||",
    "      node.fullName === \"svg:style\" ||",
    "      (isUnknownNamespace(node) &&"
   ],
   "context_after": [
    "  );",
    "}",
    "",
    "function canHaveInterpolation(node) {",
    "  return node.children && !isScriptLikeTag(node);",
    "}",
    "",
    "function isWhitespaceSensitiveNode(node) {",
    "  return (",
    "    isScriptLikeTag(node) ||",
    "    node.type === \"interpolation\" ||",
    "    isIndentationSensitiveNode(node)",
    "  );",
    "}",
    ""
   ]
  },
  {
   "path": "utils/index.js",
   "line_number": 370,
   "line": "function inferScriptParser(node, options) {",
   "context_before": [
    "",
    "    case \"text/x-handlebars-template\":",
    "      return \"glimmer\";",
    "",
    "    default:",
    "      if (",
    "        type.endsWith(\"json\") ||",
    "        type.endsWith(\"importmap\") ||",
    "        type === \"speculationrules\"",
    "      ) {",
    "        return \"json\";",
    "      }",
    "  }",
    "}",
    ""
   ],
   "context_after": [
    "  const { name, attrMap } = node;",
    "",
    "  if (name !== \"script\" || Object.hasOwn(attrMap, \"src\")) {",
    "    return;",
    "  }",
    "",
    "  const { type, lang } = node.attrMap;",
    "",
    "  if (!lang && !type) {",
    "    return \"babel\";",
    "  }",
    "",
    "  return (",
    "    inferParser(options, { language: lang }) ?? inferParserByTypeAttribute(type)",
    "  );"
   ]
  },
  {
   "path": "utils/index.js",
   "line_number": 413,
   "line": "function inferElementParser(node, options) {",
   "context_before": [
    "  const { type, lang } = attrMap;",
    "",
    "  return (",
    "    inferParser(options, { language: lang }) ?? inferParserByTypeAttribute(type)",
    "  );",
    "}",
    "",
    "function inferStyleParser(node, options) {",
    "  if (node.name !== \"style\") {",
    "    return;",
    "  }",
    "  const { lang } = node.attrMap;",
    "  return lang ? inferParser(options, { language: lang }) : \"css\";",
    "}",
    ""
   ],
   "context_after": [
    "  return (",
    "    inferScriptParser(node, options) ??",
    "    inferStyleParser(node, options) ??",
    "    inferVueSfcBlockParser(node, options)",
    "  );",
    "}",
    "",
    "function isBlockLikeCssDisplay(cssDisplay) {",
    "  return (",
    "    cssDisplay === \"block\" ||",
    "    cssDisplay === \"list-item\" ||",
    "    cssDisplay.startsWith(\"table\")",
    "  );",
    "}",
    ""
   ]
  },
  {
   "path": "utils/index.js",
   "line_number": 620,
   "line": "  return isVueSfcBlock(node, options) && node.name === \"script\";",
   "context_before": [
    "  );",
    "}",
    "",
    "function getTextValueParts(node, value = node.value) {",
    "  return node.parent.isWhitespaceSensitive",
    "    ? node.parent.isIndentationSensitive",
    "      ? replaceEndOfLine(value)",
    "      : replaceEndOfLine(",
    "          dedentString(htmlTrimPreserveIndentation(value)),",
    "          hardline",
    "        )",
    "    : join(line, htmlWhitespaceUtils.split(value));",
    "}",
    "",
    "function isVueScriptTag(node, options) {"
   ],
   "context_after": [
    "}",
    "",
    "export {",
    "  htmlTrimPreserveIndentation,",
    "  getLeadingAndTrailingHtmlWhitespace,",
    "  canHaveInterpolation,",
    "  dedentString,",
    "  forceBreakChildren,",
    "  forceBreakContent,",
    "  forceNextEmptyLine,",
    "  getLastDescendant,",
    "  getNodeCssStyleDisplay,",
    "  getNodeCssStyleWhiteSpace,",
    "  hasPrettierIgnore,",
    "  inferElementParser,"
   ]
  }
 ],
 "stats": {
  "files_searched": 26,
  "files_with_matches": 2,
  "matches_found": 7,
  "matches_returned": 7,
  "denied_skips": 0,
  "duration_ms": 16,
  "timing": {
   "walk_ms": 0,
   "search_ms": 13,
   "collect_ms": 0,
   "total_ms": 16
  }
 },
 "truncated": false
}
````

### Turn 4 — thinking

````text
I need to check whether the fullName for svg script elements is "svg:script" - since "svg:style" is already handled in isScriptLikeTag, I should add "svg:script" there too and verify it works.
````

### Turn 4 — tool call call_0004 (exec)

````json
{
 "command": "cd /testbed && printf '<svg xmlns=\"http://www.w3.org/2000/svg\">\\n<script>\\nconst a = 1; if (a) { foo() }\\n</script>\\n<style>a{color:red}</style>\\n</svg>\\n' > /tmp/t.html && ./bin/prettier.js /tmp/t.html"
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
 "stdout": "<svg xmlns=\"http://www.w3.org/2000/svg\">\n  <script>\n    const a = 1; if (a) { foo() }\n  </script>\n  <style>\n    a {\n      color: red;\n    }\n  </style>\n</svg>\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 1153,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "write",
    "paths": [
     "/tmp/t.html"
    ]
   }
  ],
  "reads": [
   "/testbed",
   "/tmp/t.html"
  ],
  "command_sha256": [
   "4b0c9efdabcd635e69909dede3c8c09909c1748ee33d012640b7491627dfddbb"
  ]
 }
}
````

### Turn 5 — tool call call_0005 (edit)

````json
{
 "file_path": "src/language-html/utils/index.js",
 "old_string": "    (node.fullName === \"script\" ||\n      node.fullName === \"style\" ||\n      node.fullName === \"svg:style\" ||",
 "new_string": "    (node.fullName === \"script\" ||\n      node.fullName === \"style\" ||\n      node.fullName === \"svg:style\" ||\n      node.fullName === \"svg:script\" ||"
}
````

Result:

````text
{
 "path": "src/language-html/utils/index.js",
 "edited": true,
 "replacements": 1,
 "total_file_lines": 659,
 "total_file_size_bytes": 16186,
 "diff": "+       node.fullName === \"svg:script\" ||",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "edit",
    "paths": [
     "src/language-html/utils/index.js"
    ]
   }
  ]
 },
 "file_change": {
  "kind": "diff",
  "operation": "update",
  "path": "src/language-html/utils/index.js",
  "patch": "+       node.fullName === \"svg:script\" ||",
  "additions": 1,
  "deletions": 0,
  "truncated": false,
  "omitted_lines": 0
 }
}
````

### Turn 6 — tool call call_0006 (exec)

````json
{
 "command": "cd /testbed && ./bin/prettier.js /tmp/t.html"
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
 "stdout": "<svg xmlns=\"http://www.w3.org/2000/svg\">\n  <script>\n    const a = 1;\n    if (a) {\n      foo();\n    }\n  </script>\n  <style>\n    a {\n      color: red;\n    }\n  </style>\n</svg>\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 2112,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed",
   "/tmp/t.html"
  ],
  "command_sha256": [
   "0ac4a9cba4eba2e0385b10b2ef933178578b36df1595e2a3073ac277d11f0468"
  ]
 }
}
````

### Turn 7 — assistant text

Fixed. Let me run the HTML tests.

### Turn 7 — tool call call_0007 (exec)

````json
{
 "command": "cd /testbed && rm /tmp/t.html && yarn jest tests/format/html 2>&1 | tail -15",
 "timeout_secs": 600
}
````

Result:

````text
{
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "backgrounded",
  "retryability": "retry_after_wait",
  "open_work_at_failure": false
 },
 "background_exec": {
  "tool_action": "run",
  "task": {
   "task_id": "bg_1_49272884adc84bf88485ce4cf745c01f",
   "session_id": "cli:default:s7084c00e",
   "root_session_id": "cli:default:s7084c00e",
   "origin_session_id": "cli:default:s7084c00e",
   "status": "running",
   "controls": {
    "list": {
     "method": "background_exec.list",
     "params": {
      "sessionId": "cli:default:s7084c00e"
     }
    },
    "logs": {
     "method": "background_exec.logs",
     "params": {
      "sessionId": "cli:default:s7084c00e",
      "task_id": "bg_1_49272884adc84bf88485ce4cf745c01f"
     }
    },
    "wait": {
     "method": "background_exec.wait",
     "params": {
      "sessionId": "cli:default:s7084c00e",
      "task_id": "bg_1_49272884adc84bf88485ce4cf745c01f"
     }
    },
    "stop": {
     "method": "background_exec.stop",
     "params": {
      "sessionId": "cli:default:s7084c00e",
      "task_id": "bg_1_49272884adc84bf88485ce4cf745c01f"
     }
    }
   },
   "title": null,
   "cwd": "/testbed",
   "pid": 832,
   "pgid": 832,
   "runtime_identity_kind": "process",
   "lifecycle_intent": "session_bound",
   "operation_descriptor": {
    "schema_id": "agent.background-exec.operation.v1",
    "requested_type": "auto",
    "session_effective_type": "native",
    "operation_family": "native",
    "isolation_tier": "none",
    "lifecycle_mode": "host-process-group",
    "policy": "transitional-native",
    "reason": {
     "code": "session-native-fallback"
    }
   },
   "process_start_time_ticks": 38565623,
   "started_at_unix_secs": 1792244654,
   "updated_at_unix_secs": 1792244654,
   "finished_at_unix_secs": null,
   "duration_ms": 1,
   "exit_code": null,
   "requested_foreground_timeout_secs": 600,
   "effective_background_timeout_secs": 14400,
   "lease_mode": "renewable",
   "lease_source": "daemon_default",
   "timeout_secs": 14400,
   "output_bytes": 0,
   "last_output_at_unix_secs": null
  },
  "work_id": "bg_1_49272884adc84bf88485ce4cf745c01f",
  "work_terminal_revision": 1792244654,
  "controls": {
   "list": {
    "method": "background_exec.list",
    "params": {
     "sessionId": "cli:default:s7084c00e"
    }
   },
   "logs": {
    "method": "background_exec.logs",
    "params": {
     "sessionId": "cli:default:s7084c00e",
     "task_id": "bg_1_49272884adc84bf88485ce4cf745c01f"
    }
   },
   "wait": {
    "method": "background_exec.wait",
    "params": {
     "sessionId": "cli:default:s7084c00e",
     "task_id": "bg_1_49272884adc84bf88485ce4cf745c01f"
    }
   },
   "stop": {
    "method": "background_exec.stop",
    "params": {
     "sessionId": "cli:default:s7084c00e",
     "task_id": "bg_1_49272884adc84bf88485ce4cf745c01f"
    }
   }
  },
  "_meta": {
   "agent": {
    "background_exec_v1": {
     "controls": {
      "list": {
       "method": "background_exec.list",
       "params": {
        "sessionId": "cli:default:s7084c00e"
       }
      },
      "logs": {
       "method": "background_exec.logs",
       "params": {
        "sessionId": "cli:default:s7084c00e",
        "task_id": "bg_1_49272884adc84bf88485ce4cf745c01f"
       }
      },
      "wait": {
       "method": "background_exec.wait",
       "params": {
        "sessionId": "cli:default:s7084c00e",
        "task_id": "bg_1_49272884adc84bf88485ce4cf745c01f"
       }
      },
      "stop": {
       "method": "background_exec.stop",
       "params": {
        "sessionId": "cli:default:s7084c00e",
        "task_id": "bg_1_49272884adc84bf88485ce4cf745c01f"
       }
      }
     },
     "task": {
      "task_id": "bg_1_49272884adc84bf88485ce4cf745c01f",
      "session_id": "cli:default:s7084c00e",
      "root_session_id": "cli:default:s7084c00e",
      "origin_session_id": "cli:default:s7084c00e",
      "status": "running",
      "controls": {
       "list": {
        "method": "background_exec.list",
        "params": {
         "sessionId": "cli:default:s7084c00e"
        }
       },
       "logs": {
        "method": "background_exec.logs",
        "params": {
         "sessionId": "cli:default:s7084c00e",
         "task_id": "bg_1_49272884adc84bf88485ce4cf745c01f"
        }
       },
       "wait": {
        "method": "background_exec.wait",
        "params": {
         "sessionId": "cli:default:s7084c00e",
         "task_id": "bg_1_49272884adc84bf88485ce4cf745c01f"
        }
       },
       "stop": {
        "method": "background_exec.stop",
        "params": {
         "sessionId": "cli:default:s7084c00e",
         "task_id": "bg_1_49272884adc84bf88485ce4cf745c01f"
        }
       }
      },
      "title": null,
      "cwd": "/testbed",
      "pid": 832,
      "pgid": 832,
      "runtime_identity_kind": "process",
      "lifecycle_intent": "session_bound",
      "operation_descriptor": {
       "schema_id": "agent.background-exec.operation.v1",
       "requested_type": "auto",
       "session_effective_type": "native",
       "operation_family": "native",
       "isolation_tier": "none",
       "lifecycle_mode": "host-process-group",
       "policy": "transitional-native",
       "reason": {
        "code": "session-native-fallback"
       }
      },
      "process_start_time_ticks": 38565623,
      "started_at_unix_secs": 1792244654,
      "updated_at_unix_secs": 1792244654,
      "finished_at_unix_secs": null,
      "duration_ms": 1,
      "exit_code": null,
      "requested_foreground_timeout_secs": 600,
      "effective_background_timeout_secs": 14400,
      "lease_mode": "renewable",
      "lease_source": "daemon_default",
      "timeout_secs": 14400,
      "output_bytes": 0,
      "last_output_at_unix_secs": null
     },
     "status": "running",
     "terminal": false
    }
   }
  },
  "tool_outcome": {
   "schema_version": 1,
   "tool_name": "background_exec",
   "status": "backgrounded",
   "retryability": "retry_after_wait",
   "open_work_at_failure": false
  }
 },
 "_agent_context_projection": {
  "schema_version": "agent.exec_tool_result_receipt_preview.v1",
  "content_status": "partial_preview",
  "context_view_limit_bytes": 16384,
  "receipt": {
   "result_id": "tr_1530592db9054bc0a8559feea71b170c",
   "total_bytes": 5210,
   "total_lines": 0,
   "omitted_bytes": 0,
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "artifact": {
   "result_id": "tr_1530592db9054bc0a8559feea71b170c",
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "content_preview": "{\"backgrounded\":true,\"background_exec\":{\"tool_action\":\"run\",\"task\":{\"task_id\":\"bg_1_49272884a\n...[agent-cli tool_result context preview: tool_result_delivery_status=delivered; content_status=partial_preview_not_failure; compatibility_marker=tool_result truncated; omitted_bytes=4752; total_bytes=4938; context_view_limit=512 bytes; context_view_strategy=head_tail_compact; guidance=preview_not_failure_outcome_neutral]...\nait timeouts do not kill the task; background_exec.stop is the explicit termination action.\"}"
 }
}
````

### Turn 8 — tool call call_0008 (background_exec)

````json
{
 "action": "wait",
 "task_id": "bg_1_49272884adc84bf88485ce4cf745c01f",
 "until": "terminal"
}
````

Result:

````text
{
 "tool_action": "wait",
 "task_id": "bg_1_49272884adc84bf88485ce4cf745c01f",
 "work_id": "bg_1_49272884adc84bf88485ce4cf745c01f",
 "work_terminal_revision": 1792244678,
 "status": "completed",
 "terminal": true,
 "lease_mode": "renewable",
 "last_output_at_unix_secs": 1792244678,
 "duration_ms": 24721,
 "stdout_delta": "PASS tests/format/html/comments/jsfmt.spec.js (11.11 s)\nPASS tests/format/html/whitespace/jsfmt.spec.js (11.519 s)\nPASS tests/format/html/css/jsfmt.spec.js (9.325 s)\nPASS tests/format/html/bracket-same-line/jsfmt.spec.js (9.628 s)\nPASS tests/format/html/attributes/jsfmt.spec.js (8.3 s)\nPASS tests/format/html/basics/jsfmt.spec.js (9.028 s)\nPASS tests/format/html/multiparser/ts/jsfmt.spec.js (10.016 s)\nPASS tests/format/html/tags/jsfmt.spec.js (11.036 s)\nPASS tests/format/html/js/jsfmt.spec.js (11.301 s)\n\nTest Suites: 31 passed, 31 total\nTests:       229 passed, 229 total\nSnapshots:   211 passed, 211 total\nTime:        19.483 s\nRan all test suites matching /tests\\/format\\/html/i.\n",
 "stderr_delta": "",
 "from_cursor": {
  "stdout": 0,
  "stderr": 0
 },
 "next_cursor": {
  "stdout": 687,
  "stderr": 0
 },
 "truncated": false,
 "omitted_bytes": 0,
 "has_more": false,
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "background_exec",
  "status": "success",
  "exit_code": 0,
  "retryability": "not_needed",
  "open_work_at_failure": false
 },
 "wait_timed_out": false,
 "progress_state": "terminal"
}
````

### Turn 9 — thinking

````text
I could also consider Vue or Angular-specific tests, but that should be sufficient for now.
````

### Turn 9 — assistant text

I fixed it: a `<script>` inside an `<svg>` is now formatted as JavaScript, just like a normal `<script>` tag.

**Cause:** inside `<svg>`, the HTML parser names the script element `svg:script`. The check in `isScriptLikeTag` (`src/language-html/utils/index.js`) already allowed for `svg:style`, but not `svg:script`. So the script's content was treated as plain text and its lines were joined and re-wrapped, which is the mess shown in the issue.

**Fix:** I added one condition to that check, `node.fullName === "svg:script"`, so the content is kept as-is and sent to the JavaScript formatter.

**Checks:**
- I ran a small SVG with a `<script>` and a `<style>` through `./bin/prettier.js`. Before the fix, the script came out on one line as `const a = 1; if (a) { foo() }`. After it, the output is properly indented JavaScript.
- `yarn jest tests/format/html` passed: 31 suites, 229 tests, 211 snapshots.

I only changed source code; no tests were touched.

### Turn 10 — assistant text

I fixed it: JavaScript in a `<script>` inside `<svg>` now gets formatted properly with the HTML parser.

**Cause:** Inside `<svg>`, the parser names the script element `svg:script`, not `script`. `isScriptLikeTag` in `src/language-html/utils/index.js` already handled `svg:style` but not `svg:script`. So the script was treated as ordinary text, and its contents got wrapped like words in a paragraph.

**Fix:** I added one condition to that function:

```js
node.fullName === "svg:script" ||
```

**Checks:**
- I wrote a smaller test file than the one in the issue: an SVG with a script containing an `if` block, plus a style. Before the change, the script printed as one line (`const a = 1; if (a) { foo() }`). After it, the script is split into proper statements with indentation, and the style still formats as before.
- The existing HTML tests (`yarn jest tests/format/html`) pass: 31 suites, 229 tests and 211 snapshots, with no snapshot changes.

I didn't run the full example from the issue or the rest of the test suite, and I didn't add a new test.

## Final answer

I fixed it: JavaScript in a `<script>` inside `<svg>` now gets formatted properly with the HTML parser.

**Cause:** Inside `<svg>`, the parser names the script element `svg:script`, not `script`. `isScriptLikeTag` in `src/language-html/utils/index.js` already handled `svg:style` but not `svg:script`. So the script was treated as ordinary text, and its contents got wrapped like words in a paragraph.

**Fix:** I added one condition to that function:

```js
node.fullName === "svg:script" ||
```

**Checks:**
- I wrote a smaller test file than the one in the issue: an SVG with a script containing an `if` block, plus a style. Before the change, the script printed as one line (`const a = 1; if (a) { foo() }`). After it, the script is split into proper statements with indentation, and the style still formats as before.
- The existing HTML tests (`yarn jest tests/format/html`) pass: 31 suites, 229 tests and 211 snapshots, with no snapshot changes.

I didn't run the full example from the issue or the rest of the test suite, and I didn't add a new test.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 160426 | 1819 | 118980 | 41428 | 162245 |
