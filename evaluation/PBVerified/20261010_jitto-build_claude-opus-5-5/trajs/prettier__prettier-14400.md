# Instance: prettier__prettier-14400

- Final resolved (evaluator, logs/prettier__prettier-14400_result.json): True
- Run state: DONE
- One attempt. Duration 70.4 s, turns 10, actor cost $0.17954720000000002, container commands 4
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/prettier__prettier-14400/repo
</uploaded_files>
I've uploaded a JavaScript code repository in the directory /work/prettier__prettier-14400/repo. Consider the following issue description:

<issue_description>
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

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/prettier__prettier-14400/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/prettier__prettier-14400/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/prettier__prettier-14400/bin/envrun 'git status --short && ls'
Edits you make under /work/prettier__prettier-14400/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/prettier__prettier-14400/repo; grep -rn "script" src/language-html/utils/index.js | head -40; grep -rn "getNodeContent\|isScriptLikeTag\|inferScriptParser" src/language-html/*.js | head -30
```

tool result:

```
src/language-html/utils/index.js:109:    (node.fullName === "script" ||
src/language-html/utils/index.js:113:        (node.name === "script" || node.name === "style")))
src/language-html/utils/index.js:253:      (["body", "script", "style"].includes(node.name) ||
src/language-html/utils/index.js:322:      return ["script", "select"].includes(node.name);
src/language-html/utils/index.js:342:    case "text/javascript":
src/language-html/utils/index.js:344:    case "application/javascript":
src/language-html/utils/index.js:347:    case "application/x-typescript":
src/language-html/utils/index.js:348:      return "typescript";
src/language-html/utils/index.js:373:  if (name !== "script" || Object.hasOwn(attrMap, "src")) {
src/language-html/utils/index.js:558:// top-level elements (excluding <template>, <style> and <script>) in Vue SFC are considered custom block
src/language-html/utils/index.js:560:const vueRootElementsSet = new Set(["template", "style", "script"]);
src/language-html/utils/index.js:601:    // https://github.com/vuejs/rfcs/blob/sfc-improvements/active-rfcs/0000-sfc-script-setup.md
src/language-html/utils/index.js:602:    (tagName === "script" && attributeName === "setup") ||
src/language-html/utils/index.js:620:  return isVueSfcBlock(node, options) && node.name === "script";
src/language-html/embed.js:26:  isScriptLikeTag,
src/language-html/embed.js:37:import getNodeContent from "./get-node-content.js";
src/language-html/embed.js:263:      if (isScriptLikeTag(node) || node.type === "interpolation") {
src/language-html/embed.js:275:          const content = getNodeContent(node, options);
src/language-html/embed.js:300:      if (isScriptLikeTag(node.parent)) {
src/language-html/get-node-content.js:10:function getNodeContent(node, options) {
src/language-html/get-node-content.js:36:export default getNodeContent;
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-14400/repo; sed -n 100,120p src/language-html/utils/index.js; sed -n 330,440p src/language-html/utils/index.js
```

tool result:

```
/** there's no opening/closing tag or it's considered not breakable */
function isTextLikeNode(node) {
  return node.type === "text" || node.type === "comment";
}

function isScriptLikeTag(node) {
  return (
    node.type === "element" &&
    (node.fullName === "script" ||
      node.fullName === "style" ||
      node.fullName === "svg:style" ||
      (isUnknownNamespace(node) &&
        (node.name === "script" || node.name === "style")))
  );
}

function canHaveInterpolation(node) {
  return node.children && !isScriptLikeTag(node);
}


function hasNonTextChild(node) {
  return node.children?.some((child) => child.type !== "text");
}

function inferParserByTypeAttribute(type) {
  if (!type) {
    return;
  }

  switch (type) {
    case "module":
    case "text/javascript":
    case "text/babel":
    case "application/javascript":
      return "babel";

    case "application/x-typescript":
      return "typescript";

    case "text/markdown":
      return "markdown";

    case "text/html":
      return "html";

    case "text/x-handlebars-template":
      return "glimmer";

    default:
      if (
        type.endsWith("json") ||
        type.endsWith("importmap") ||
        type === "speculationrules"
      ) {
        return "json";
      }
  }
}

function inferScriptParser(node, options) {
  const { name, attrMap } = node;

  if (name !== "script" || Object.hasOwn(attrMap, "src")) {
    return;
  }

  const { type, lang } = node.attrMap;

  if (!lang && !type) {
    return "babel";
  }

  return (
    inferParser(options, { language: lang }) ?? inferParserByTypeAttribute(type)
  );
}

function inferVueSfcBlockParser(node, options) {
  if (!isVueNonHtmlBlock(node, options)) {
    return;
  }
  const { attrMap } = node;

  if (Object.hasOwn(attrMap, "src")) {
    return;
  }

  const { type, lang } = attrMap;

  return (
    inferParser(options, { language: lang }) ?? inferParserByTypeAttribute(type)
  );
}

function inferStyleParser(node, options) {
  if (node.name !== "style") {
    return;
  }
  const { lang } = node.attrMap;
  return lang ? inferParser(options, { language: lang }) : "css";
}

function inferElementParser(node, options) {
  return (
    inferScriptParser(node, options) ??
    inferStyleParser(node, options) ??
    inferVueSfcBlockParser(node, options)
  );
}

function isBlockLikeCssDisplay(cssDisplay) {
  return (
    cssDisplay === "block" ||
    cssDisplay === "list-item" ||
    cssDisplay.startsWith("table")
  );
}

function isFirstChildLeadingSpaceSensitiveCssDisplay(cssDisplay) {
  return !isBlockLikeCssDisplay(cssDisplay) && cssDisplay !== "inline-block";
}

function isLastChildTrailingSpaceSensitiveCssDisplay(cssDisplay) {
  return !isBlockLikeCssDisplay(cssDisplay) && cssDisplay !== "inline-block";
}

function isPrevTrailingSpaceSensitiveCssDisplay(cssDisplay) {
  return !isBlockLikeCssDisplay(cssDisplay);
}
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-14400/repo; grep -rn "svg:style\|svg:" src/language-html | head; ls tests/format/html/svg 2>/dev/null; git log --oneline -1
```

tool result:

```
src/language-html/utils/index.js:111:      node.fullName === "svg:style" ||
src/language-html/utils/index.js:483:    if (hasParent(node, (parent) => parent.fullName === "svg:foreignObject")) {
__snapshots__
jsfmt.spec.js
svg.html
6905b39ec Build(deps): Bump qs from 6.5.2 to 6.5.3 in /website (#14603)
```

**assistant:** Reproduce first:

**tool call: Bash**

```bash
cd /work/prettier__prettier-14400/repo; cat > /tmp/repro.html <<'EOF'
<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 24 24">
	<script>
		document.addEventListener('DOMContentLoaded', () => {
			const node = document.getElementById('lastStroke');
			if (node) { svg.pauseAnimations(); }
		});	
	</script>
</svg>
EOF
cp /tmp/repro.html repro-tmp.html; ../bin/envrun './bin/prettier.js repro-tmp.html'
```

tool result:

```
Exit code 2
(eval):1: operation not permitted: /tmp/repro.html
cp: /tmp/repro.html: No such file or directory
[error] No files matching the pattern were found: "repro-tmp.html".
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-14400/repo; cat > repro-tmp.html <<'EOF'
<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 24 24">
	<script>
		document.addEventListener('DOMContentLoaded', () => {
			const node = document.getElementById('lastStroke');
			if (node) { svg.pauseAnimations(); }
		});	
	</script>
</svg>
EOF
../bin/envrun './bin/prettier.js repro-tmp.html'
```

tool result:

```
<svg
  xmlns="http://www.w3.org/2000/svg"
  width="240"
  height="240"
  viewBox="0 0 24 24"
>
  <script>
    document.addEventListener('DOMContentLoaded', () => { const node =
    document.getElementById('lastStroke'); if (node) { svg.pauseAnimations(); }
    });
  </script>
</svg>
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-14400/repo; sed -i '' 's/      node.fullName === "svg:style" ||/      node.fullName === "svg:style" ||\n      node.fullName === "svg:script" ||/' src/language-html/utils/index.js; sed -n 105,116p src/language-html/utils/index.js
```

tool result:

```
function isScriptLikeTag(node) {
  return (
    node.type === "element" &&
    (node.fullName === "script" ||
      node.fullName === "style" ||
      node.fullName === "svg:style" ||
      node.fullName === "svg:script" ||
      (isUnknownNamespace(node) &&
        (node.name === "script" || node.name === "style")))
  );
}
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-14400/repo; cat > repro-tmp.html <<'EOF'
<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 24 24">
	<script>
		document.addEventListener('DOMContentLoaded', () => {
			const node = document.getElementById('lastStroke');
			if (node && a < b && c > d) { svg.pauseAnimations(); }
		});	
	</script>
	<script type="text/x-unknown">
	  foo   bar
	</script>
</svg>
EOF
../bin/envrun './bin/prettier.js repro-tmp.html'
```

tool result:

```
<svg
  xmlns="http://www.w3.org/2000/svg"
  width="240"
  height="240"
  viewBox="0 0 24 24"
>
  <script>
    document.addEventListener("DOMContentLoaded", () => {
      const node = document.getElementById("lastStroke");
      if (node && a < b && c > d) {
        svg.pauseAnimations();
      }
    });
  </script>
  <script type="text/x-unknown">
    foo   bar
  </script>
</svg>
```

**assistant:** Fixed. Now run the HTML tests:

**tool call: Bash**

```bash
cd /work/prettier__prettier-14400/repo; rm repro-tmp.html; ../bin/envrun 'yarn jest tests/format/html tests/format/vue 2>&1 | tail -40'; git status --short
```

tool result:

```
PASS tests/format/html/yaml/jsfmt.spec.js
PASS tests/format/html/srcset/jsfmt.spec.js
PASS tests/format/html/svg/jsfmt.spec.js
PASS tests/format/html/next_empty_line/jsfmt.spec.js
PASS tests/format/html/magic_comments/jsfmt.spec.js
PASS tests/format/html/interpolation/jsfmt.spec.js
PASS tests/format/html/prettier_ignore/jsfmt.spec.js
PASS tests/format/html/tags/jsfmt.spec.js
PASS tests/format/html/front-matter/jsfmt.spec.js
PASS tests/format/vue/bracket-same-line/jsfmt.spec.js
PASS tests/format/html/whitespace/jsfmt.spec.js
PASS tests/format/html/case/jsfmt.spec.js
PASS tests/format/html/aurelia/jsfmt.spec.js
PASS tests/format/html/doctype_declarations/jsfmt.spec.js
PASS tests/format/html/comments/jsfmt.spec.js
PASS tests/format/html/cdata/jsfmt.spec.js
PASS tests/format/html/script/jsfmt.spec.js
PASS tests/format/vue/vue-3/jsfmt.spec.js
PASS tests/format/vue/range/jsfmt.spec.js
PASS tests/format/html/multiparser/ts/jsfmt.spec.js
PASS tests/format/vue/single-attribute-per-line/jsfmt.spec.js
PASS tests/format/vue/interpolation/jsfmt.spec.js
PASS tests/format/vue/invalid/jsfmt.spec.js
PASS tests/format/html/css/jsfmt.spec.js
PASS tests/format/html/attributes/jsfmt.spec.js
PASS tests/format/vue/v-for/jsfmt.spec.js
PASS tests/format/vue/custom_block/jsfmt.spec.js (5.069 s)
PASS tests/format/vue/ts-expression/jsfmt.spec.js
PASS tests/format/html/basics/jsfmt.spec.js
PASS tests/format/vue/event-binding/jsfmt.spec.js
PASS tests/format/vue/html-vue/jsfmt.spec.js
PASS tests/format/vue/multiparser/jsfmt.spec.js (5.825 s)
PASS tests/format/html/js/jsfmt.spec.js
PASS tests/format/vue/vue/jsfmt.spec.js (6.242 s)

Test Suites: 50 passed, 50 total
Tests:       415 passed, 415 total
Snapshots:   397 passed, 397 total
Time:        11.238 s
Ran all test suites matching /tests\/format\/html|tests\/format\/vue/i.

 M package.json
 M src/language-html/utils/index.js
?? Dockerfile
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-14400/repo; git diff package.json
```

tool result:

```
diff --git a/package.json b/package.json
index c3d075e45..3235a6daa 100644
--- a/package.json
+++ b/package.json
@@ -165,7 +165,7 @@
     "perf:inspect": "yarn && yarn build && cross-env NODE_ENV=production node --inspect-brk ./dist/bin/prettier.cjs",
     "perf:benchmark": "yarn perf --debug-benchmark",
     "perf:compare": "./scripts/benchmark/compare.sh",
-    "lint": "run-p \"lint:*\"",
+    "lint": "echo noop",
     "lint:typecheck": "tsc",
     "lint:eslint": "cross-env EFF_NO_LINK_RULES=true eslint . --format friendly",
     "lint:changelog": "node ./scripts/lint-changelog.mjs",
```

**assistant:** I fixed the bug: JavaScript inside `<script>` tags within `<svg>` is now formatted as JavaScript when using the HTML parser.

**Cause:** Inside an `<svg>`, the parser names a `<script>` element `svg:script`. The function that decides which tags hold embedded code, `isScriptLikeTag` in `src/language-html/utils/index.js`, already recognised `svg:style` but not `svg:script`. So the script was treated as ordinary text and its words were rewrapped to fit the line width, which produced the unreadable output in the issue.

**Fix:** I added one line to that check:

```js
      node.fullName === "svg:style" ||
      node.fullName === "svg:script" ||
```

The script's language is then picked the same way as for a normal HTML `<script>`.

**Checks:**
- **Before the fix:** I reproduced the issue's output with a cut-down version of its example.
- **After the fix:** the script inside `<svg>` comes out as properly formatted JavaScript, and code containing `<` and `>` comparisons is formatted correctly.
- **Unknown script types:** a script with an unrecognised type (`text/x-unknown`) keeps its original content untouched, the same as in plain HTML.
- **Existing tests:** all HTML and Vue format tests pass (50 suites, 415 tests). I deleted my reproduction file afterwards.

`git status` also shows a changed `package.json` (the `lint` script replaced with `echo noop`) and an untracked `Dockerfile`. I didn't make either change; they look like part of the container setup, so I left them alone.

_session end: success, turns 10, is_error False_

## Container commands (task container, no network; broker log)

- `rc=2` 1.22 s: ./bin/prettier.js repro-tmp.html
- `rc=0` 1.23 s: ./bin/prettier.js repro-tmp.html
- `rc=0` 1.3 s: ./bin/prettier.js repro-tmp.html
- `rc=0` 16.07 s: yarn jest tests/format/html tests/format/vue 2>&1 | tail -40
