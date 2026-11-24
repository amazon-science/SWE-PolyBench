# Instance: sveltejs__svelte-3314
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: True

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
Illegal property names aren't quoted for SSR
**Describe the bug**

A component can have a property like `<Foo x-y-z={42}/>`, and it will ordinarily be quoted by the compiler:

```js
var foo = new Foo({ props: { "x-y-z": 42 } });
```

In SSR mode, we get this instead:

```js
return `${validate_component(Foo, 'Foo').$$render($$result, { x-y-z: 42 }, {}, {})}`;
```

This is somewhat contrived (you can only access that property via `$$props['x-y-z']`), but it's a situation I've managed to encounter, and it's easily fixed.

**To Reproduce**

[Voila](https://svelte.dev/repl/07c5045a1d8044ccbba9989ea8198b05?version=3.6.9)

**Severity**

I mean... probably not the highest. But like I say, easy fix
````

## Operational trajectory

### Turn 1 — thinking

````text
The user is asking me to find where SSR component props get generated and quote the illegal property
````

### Turn 1 — tool call call_0001 (exec)

````json
{
 "command": "ls && git log --oneline -3"
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
 "stdout": "CHANGELOG.md\nDockerfile\nLICENSE\nREADME.md\nanimate\nappveyor.yml\nbanner.png\ncompiler.d.ts\ncompiler.js\ncompiler.js.map\neasing\nindex.js\nindex.mjs\ninternal\nmocha.coverage.opts\nmocha.opts\nmotion\nnode_modules\npackage-lock.json\npackage.json\nregister.js\nrollup.config.js\nsite\nsrc\nstore\ntest\ntmp\ntransition\ntsconfig.json\ntypes\ndbf503b9 Merge pull request #3305 from Conduitry/gh-3226\n620d26ca Merge pull request #3295 from sveltejs/gh-3286\ndf331871 Merge pull request #3294 from sveltejs/gh-3289\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 426,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [],
  "command_sha256": [
   "2fcf4d2090d1b2fbc9693dcdf5ef29cea50bd7f1e59b6ef2957da36b85a26be3"
  ]
 }
}
````

### Turn 2 — tool call call_0002 (rg)

````json
{
 "pattern": "\\$\\$render\\(",
 "output_mode": "files_with_matches"
}
````

Result:

````text
{
 "output_mode": "files_with_matches",
 "pattern": "\\$\\$render\\(",
 "search_path": "/testbed",
 "files": [],
 "stats": {
  "files_searched": 3504,
  "files_with_matches": 0,
  "matches_found": 0,
  "matches_returned": 0,
  "denied_skips": 0,
  "duration_ms": 1215,
  "timing": {
   "walk_ms": 0,
   "search_ms": 1215,
   "collect_ms": 0,
   "total_ms": 1215
  }
 },
 "truncated": false,
 "truncation_reason": "offset"
}
````

### Turn 3 — tool call call_0003 (read)

````json
{
 "file_path": "src/compiler/compile/render_ssr/handlers/InlineComponent.ts"
}
````

Result:

````text
{
 "type": "file",
 "path": "src/compiler/compile/render_ssr/handlers/InlineComponent.ts",
 "full_read": true,
 "output": "src/compiler/compile/render_ssr/handlers/InlineComponent.ts\n\n1: import { escape, escape_template, stringify } from '../../utils/stringify';\n2: import { quote_name_if_necessary } from '../../../utils/names';\n3: import { snip } from '../../utils/snip';\n4: import Renderer, { RenderOptions } from '../Renderer';\n5: import { stringify_props } from '../../utils/stringify_props';\n6: import { get_slot_scope } from './shared/get_slot_scope';\n7: import { AppendTarget } from '../../../interfaces';\n8: import InlineComponent from '../../nodes/InlineComponent';\n9: import { INode } from '../../nodes/interfaces';\n10: import Text from '../../nodes/Text';\n11: \n12: function stringify_attribute(chunk: INode) {\n13: \tif (chunk.type === 'Text') {\n14: \t\treturn escape_template(escape((chunk as Text).data));\n15: \t}\n16: \n17: \treturn '${@escape(' + snip(chunk) + ')}';\n18: }\n19: \n20: function get_attribute_value(attribute) {\n21: \tif (attribute.is_true) return `true`;\n22: \tif (attribute.chunks.length === 0) return `''`;\n23: \n24: \tif (attribute.chunks.length === 1) {\n25: \t\tconst chunk = attribute.chunks[0];\n26: \t\tif (chunk.type === 'Text') {\n27: \t\t\treturn stringify(chunk.data);\n28: \t\t}\n29: \n30: \t\treturn snip(chunk);\n31: \t}\n32: \n33: \treturn '`' + attribute.chunks.map(stringify_attribute).join('') + '`';\n34: }\n35: \n36: export default function(node: InlineComponent, renderer: Renderer, options: RenderOptions) {\n37: \tconst binding_props = [];\n38: \tconst binding_fns = [];\n39: \n40: \tnode.bindings.forEach(binding => {\n41: \t\trenderer.has_bindings = true;\n42: \n43: \t\t// TODO this probably won't work for contextual bindings\n44: \t\tconst snippet = snip(binding.expression);\n45: \n46: \t\tbinding_props.push(`${binding.name}: ${snippet}`);\n47: \t\tbinding_fns.push(`${binding.name}: $$value => { ${snippet} = $$value; $$settled = false }`);\n48: \t});\n49: \n50: \tconst uses_spread = node.attributes.find(attr => attr.is_spread);\n51: \n52: \tlet props;\n53: \n54: \tif (uses_spread) {\n55: \t\tprops = `@_Object.assign(${\n56: \t\t\tnode.attributes\n57: \t\t\t\t.map(attribute => {\n58: \t\t\t\t\tif (attribute.is_spread) {\n59: \t\t\t\t\t\treturn snip(attribute.expression);\n60: \t\t\t\t\t} else {\n61: \t\t\t\t\t\treturn `{ ${attribute.name}: ${get_attribute_value(attribute)} }`;\n62: \t\t\t\t\t}\n63: \t\t\t\t})\n64: \t\t\t\t.concat(binding_props.map(p => `{ ${p} }`))\n65: \t\t\t\t.join(', ')\n66: \t\t})`;\n67: \t} else {\n68: \t\tprops = stringify_props(\n69: \t\t\tnode.attributes\n70: \t\t\t\t.map(attribute => `${attribute.name}: ${get_attribute_value(attribute)}`)\n71: \t\t\t\t.concat(binding_props)\n72: \t\t);\n73: \t}\n74: \n75: \tconst bindings = stringify_props(binding_fns);\n76: \n77: \tconst expression = (\n78: \t\tnode.name === 'svelte:self'\n79: \t\t\t? '__svelte:self__' // TODO conflict-proof this\n80: \t\t\t: node.name === 'svelte:component'\n81: \t\t\t\t? `((${snip(node.expression)}) || @missing_component)`\n82: \t\t\t\t: node.name\n83: \t);\n84: \n85: \tconst slot_fns = [];\n86: \n87: \tif (node.children.length) {\n88: \t\tconst target: AppendTarget = {\n89: \t\t\tslots: { default: '' },\n90: \t\t\tslot_stack: ['default']\n91: \t\t};\n92: \n93: \t\trenderer.targets.push(target);\n94: \n95: \t\tconst slot_scopes = new Map();\n96: \t\tslot_scopes.set('default', get_slot_scope(node.lets));\n97: \n98: \t\trenderer.render(node.children, Object.assign({}, options, {\n99: \t\t\tslot_scopes\n100: \t\t}));\n101: \n102: \t\tObject.keys(target.slots).forEach(name => {\n103: \t\t\tconst slot_scope = slot_scopes.get(name);\n104: \n105: \t\t\tslot_fns.push(\n106: \t\t\t\t`${quote_name_if_necessary(name)}: (${slot_scope}) => \\`${target.slots[name]}\\``\n107: \t\t\t);\n108: \t\t});\n109: \n110: \t\trenderer.targets.pop();\n111: \t}\n112: \n113: \tconst slots = stringify_props(slot_fns);\n114: \n115: \trenderer.append(`\\${@validate_component(${expression}, '${node.name}').$$render($$result, ${props}, ${bindings}, ${slots})}`);\n116: }\n\n(End of file - total 116 lines)",
 "offset": 1,
 "lines_returned": 116,
 "total_lines": 116,
 "total_lines_exact": true,
 "truncated": false,
 "size_bytes": 3209
}
````

### Turn 4 — tool call call_0004 (exec)

````json
{
 "command": "cd src/compiler/compile/render_ssr/handlers && sed -i 's/return `{ ${attribute.name}: ${get_attribute_value(attribute)} }`;/return `{ ${quote_name_if_necessary(attribute.name)}: ${get_attribute_value(attribute)} }`;/; s/\\.map(attribute => `${attribute.name}: ${get_attribute_value(attribute)}`)/.map(attribute => `${quote_name_if_necessary(attribute.name)}: ${get_attribute_value(attribute)}`)/' InlineComponent.ts && git diff"
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
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "write",
    "paths": [
     "InlineComponent.ts"
    ]
   }
  ],
  "reads": [
   "src/compiler/compile/render_ssr/handlers"
  ],
  "command_sha256": [
   "dffe4189bbc59336b349c99252f02be8f928257d88895901610b1b3782858575"
  ]
 },
 "_agent_context_projection": {
  "schema_version": "agent.exec_tool_result_receipt_preview.v1",
  "content_status": "partial_preview",
  "context_view_limit_bytes": 16384,
  "receipt": {
   "result_id": "tr_26b845c4c1354aefacfeb9787640499e",
   "total_bytes": 201378,
   "total_lines": 4957,
   "omitted_bytes": 177234,
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "artifact": {
   "result_id": "tr_26b845c4c1354aefacfeb9787640499e",
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "content_preview": "{\"tool_outcome\":{\"schema_version\":1,\"tool_name\":\"exec\",\"status\":\"success\",\"exit_code\":0,\"re\n...[agent-cli tool_result context preview: tool_result_delivery_status=delivered; content_status=partial_preview_not_failure; compatibility_marker=tool_result truncated; omitted_bytes=200144; total_bytes=200326; context_view_limit=512 bytes; context_view_strategy=head_tail_compact; guidance=preview_not_failure_outcome_neutral]...\ns\"],\"command_sha256\":[\"dffe4189bbc59336b349c99252f02be8f928257d88895901610b1b3782858575\"]}}",
  "stdout": {
   "total_bytes": 182094,
   "total_lines": 4957,
   "omitted_bytes": 177234,
   "preview": "diff --git a/package-lock.json b/package-lock.json\nindex bcde04de..a2671440 100644\n--- a/package-lock.json\n+++ b/package-lock.json\n@@ -1,8 +1,4841 @@\n {\n   \"name\": \"svelte\",\n-  \"version\": \"3.6.7\",\n-  \"lockfileVersion\": 1,\n+  \"version\": \"3.6.9\",\n+  \"lockfileVersion\": 2,\n   \"requires\": true,\n+  \"packages\": {\n+    \"\": {\n+      \"name\": \"svelte\",\n+      \"version\": \"3.6.9\",\n+      \"license\": \"MIT\",\n+      \"devDependencies\": {\n+        \"@types/mocha\": \"^5.2.7\",\n+        \"@types/node\": \"=8\",\n+        \"@typescript-eslint/eslint-plugin\": \"^1.11.0\",\n+        \"@typescript-eslint/parser\": \"^1.11.0\",\n+        \"acorn\": \"^6.2.0\",\n+        \"acorn-dynamic-import\": \"^4.0.0\",\n+        \"agadoo\": \"^1.0.1\",\n+        \"c8\": \"^5.0.1\",\n+        \"codecov\": \"^3.5.0\",\n+        \"css-tree\": \"1.0.0-alpha22\",\n+        \"eslint\": \"^6.0.1\",\n+        \"eslint-plugin-import\": \"^2.18.0\",\n+        \"eslint-plugin-svelte3\": \"^2.6.0\",\n+        \"estree-walker\": \"^0.6.1\",\n+        \"is-reference\": \"^1.1.3\",\n+        \"jsdom\": \"^15.1.1\",\n+        \"kleur\": \"^3.0.3\",\n+        \"locate-character\": \"^2.0.5\",\n+        \"magic-string\": \"^0.25.3\",\n+        \"mocha\": \"^6.1.4\",\n+        \"puppeteer\": \"^1.18.1\",\n+        \"rollup\": \"^1.16.6\",\n+        \"rollup-plugin-commonjs\": \"^10.0.1\",\n+        \"rollup-plugin-json\": \"^4.0.0\",\n+        \"rollup-plugin-node-resolve\": \"^5.2.0\",\n+        \"rollup-plugin-replace\": \"^2.2.0\",\n+        \"rollup-plugin-sucrase\": \"^2.1.0\",\n+        \"rollup-plugin-typescript\": \"^1.0.1\",\n+        \"rollup-plugin-virtual\": \"^1.0.1\",\n+        \"source-map\": \"^0.6.1\",\n+        \"source-map-support\": \"^0.5.12\",\n+        \"tiny-glob\": \"^0.2.6\",\n+        \"ts-node\": \"^8.3.0\",\n+        \"tslib\": \"^1.10.0\",\n+        \"typescript\": \"^3.5.2\"\n+      },\n+      \"engines\": {\n+        \"node\": \">= 8\"\n+      }\n+    },\n+    \"node_modules/@babel/code-frame\": {\n+      \"version\": \"7.0.0\",\n+      \"resolved\": \"https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.0.0.tgz\",\n+      \"integrity\": \"sha512-OfC2uemaknXr87bdLUkWog7nYuliM9Ij5HUcajsVcMCpQrcLmtxRbVFTIqmcSkSeYRBFBRxs2FiUqFJDLdiebA==\",\n+      \"dev\": true,\n+      \"dependencies\": {\n+        \"@babel/highlight\": \"^7.0.0\"\n+      }\n+    },\n+    \"node_modules/@babel/highlight\": {\n+      \"version\": \"7.5.0\",\n+      \"resolved\": \"https://registry.npmjs.org/@babel/highlight/-/highlight-7.5.0.tgz\",\n+      \"integrity\": \"sha512-7dV4eu9gBxoM0dAnj/BCFDW9LFU0zvTrkq0ugM7pnHEgguOEeOz1so2ZghEdzviYzQEED0r4EAgpsBChKy1TRQ==\n...[agent-cli tool_result context preview: tool_result_delivery_status=delivered; content_status=partial_preview_not_failure; compatibility_marker=tool_result truncated; omitted_bytes=177234; total_bytes=182094; context_view_limit=5461 bytes; context_view_strategy=head_tail_v2; preserved_ranges=0..2430,179664..182094; model_guidance=this tool result was delivered and the visible content is a bounded preview, not evidence by itself that the read or command failed; continuation_hint=use read/exec with explicit offset/limit or rerun the command with narrower filters to inspect the omitted range]...\n },\n     \"string_decoder\": {\n       \"version\": \"1.1.1\",\n       \"resolved\": \"https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz\",\n@@ -3281,6 +8106,17 @@\n         }\n       }\n     },\n+    \"string-width\": {\n+      \"version\": \"3.1.0\",\n+      \"resolved\": \"https://registry.npmjs.org/string-width/-/string-width-3.1.0.tgz\",\n+      \"integrity\": \"sha512-vafcv6KjVZKSgz06oM/H6GDBrAtz8vdhQakGjFIvNrHA6y3HCF1CInLy+QLq8dTJPQ1b+KDUqDFctkdRW44e1w==\",\n+      \"dev\": true,\n+      \"requires\": {\n+        \"emoji-regex\": \"^7.0.1\",\n+        \"is-fullwidth-code-point\": \"^2.0.0\",\n+        \"strip-ansi\": \"^5.1.0\"\n+      }\n+    },\n     \"strip-ansi\": {\n       \"version\": \"5.2.0\",\n       \"resolved\": \"https://registry.npmjs.org/strip-ansi/-/strip-ansi-5.2.0.tgz\",\ndiff --git a/package.json b/package.json\nindex 1f40d178..63f9a62f 100644\n--- a/package.json\n+++ b/package.json\n@@ -37,7 +37,7 @@\n     \"posttest\": \"agadoo internal/index.mjs\",\n     \"prepublishOnly\": \"npm run lint && PUBLISH=true npm test\",\n     \"tsd\": \"tsc -p src/compiler --emitDeclarationOnly && tsc -p src/runtime --emitDeclarationOnly\",\n-    \"lint\": \"eslint \\\"{src,test}/**/*.{ts,js}\\\"\"\n+    \"lint\": \"echo noop\"\n   },\n   \"repository\": {\n     \"type\": \"git\",\n@@ -99,6 +99,5 @@\n     ],\n     \"sourceMap\": true,\n     \"instrument\": true\n-  },\n-  \"dependencies\": {}\n+  }\n }\ndiff --git a/src/compiler/compile/render_ssr/handlers/InlineComponent.ts b/src/compiler/compile/render_ssr/handlers/InlineComponent.ts\nindex 320bf5e6..74d990a3 100644\n--- a/src/compiler/compile/render_ssr/handlers/InlineComponent.ts\n+++ b/src/compiler/compile/render_ssr/handlers/InlineComponent.ts\n@@ -58,7 +58,7 @@ export default function(node: InlineComponent, renderer: Renderer, options: Rend\n \t\t\t\t\tif (attribute.is_spread) {\n \t\t\t\t\t\treturn snip(attribute.expression);\n \t\t\t\t\t} else {\n-\t\t\t\t\t\treturn `{ ${attribute.name}: ${get_attribute_value(attribute)} }`;\n+\t\t\t\t\t\treturn `{ ${quote_name_if_necessary(attribute.name)}: ${get_attribute_value(attribute)} }`;\n \t\t\t\t\t}\n \t\t\t\t})\n \t\t\t\t.concat(binding_props.map(p => `{ ${p} }`))\n@@ -67,7 +67,7 @@ export default function(node: InlineComponent, renderer: Renderer, options: Rend\n \t} else {\n \t\tprops = stringify_props(\n \t\t\tnode.attributes\n-\t\t\t\t.map(attribute => `${attribute.name}: ${get_attribute_value(attribute)}`)\n+\t\t\t\t.map(attribute => `${quote_name_if_necessary(attribute.name)}: ${get_attribute_value(attribute)}`)\n \t\t\t\t.concat(binding_props)\n \t\t);\n \t}\n"
  }
 }
}
````

### Turn 5 — thinking

````text
The package.json and lock file changes were already there, so I'll leave those alone. Let me check if tests run through ts-node to verify things actually compile properly.
````

### Turn 5 — assistant text

Edit applied (package.json/lock diffs were already there and are not mine). Running a quick smoke check:

### Turn 5 — tool call call_0005 (exec)

````json
{
 "command": "cd /testbed && cat > /tmp/t.js <<'EOF'\nrequire('ts-node').register({transpileOnly:true, compilerOptions:{module:'commonjs'}});\nconst {compile}=require('/testbed/src/compiler/index.ts');\nfor (const src of ['<script>import Foo from \"./Foo.svelte\";</script><Foo x-y-z={42}/>','<script>import Foo from \"./Foo.svelte\";let o={};</script><Foo {...o} x-y-z={42}/>']) {\n const c=compile(src,{generate:'ssr'}).js.code; console.log(c.split('\\n').filter(l=>l.includes('$$render')).join('\\n')); new Function(c.replace(/import.*\\n/g,'').replace(/export default/,'return'));}\nEOF\nnode /tmp/t.js; rm /tmp/t.js"
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
 "duration_ms": 609,
 "stderr": "node:internal/modules/cjs/loader:1031\n  throw err;\n  ^\n\nError: Cannot find module 'ts-node'\nRequire stack:\n- /tmp/t.js\n    at Function.Module._resolveFilename (node:internal/modules/cjs/loader:1028:15)\n    at Function.Module._load (node:internal/modules/cjs/loader:873:27)\n    at Module.require (node:internal/modules/cjs/loader:1100:19)\n    at require (node:internal/modules/cjs/helpers:119:18)\n    at Object.<anonymous> (/tmp/t.js:1:1)\n    at Module._compile (node:internal/modules/cjs/loader:1198:14)\n    at Object.Module._extensions..js (node:internal/modules/cjs/loader:1252:10)\n    at Module.load (node:internal/modules/cjs/loader:1076:32)\n    at Function.Module._load (node:internal/modules/cjs/loader:911:12)\n    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:81:12) {\n  code: 'MODULE_NOT_FOUND',\n  requireStack: [ '/tmp/t.js' ]\n}\n",
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "guidance": "stderr contains error-like diagnostics while the final exit code is 0. Inspect stderr before treating this command as successful; shell control flow may have masked a failed subcommand.",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "write",
    "paths": [
     "/tmp/t.js"
    ]
   }
  ],
  "reads": [
   "/testbed",
   "/tmp/t.js"
  ],
  "command_sha256": [
   "283315c5394f986f7011c79a8cd0952733aabf7f895400e1f2f715c583d0c57e"
  ]
 },
 "device_targets": []
}
````

### Turn 6 — tool call call_0006 (exec)

````json
{
 "command": "cd /testbed && cat > t_smoke.js <<'EOF'\nrequire('ts-node').register({transpileOnly:true, compilerOptions:{module:'commonjs'}});\nconst {compile}=require('./src/compiler/index.ts');\nfor (const src of ['<script>import Foo from \"./Foo.svelte\";</script><Foo x-y-z={42}/>','<script>import Foo from \"./Foo.svelte\";let o={};</script><Foo {...o} x-y-z={42}/>']) {\n const c=compile(src,{generate:'ssr'}).js.code; console.log(c.split('\\n').filter(l=>l.includes('$$render(')).join('\\n'));}\nEOF\ntimeout 60 node t_smoke.js; rm t_smoke.js"
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
 "duration_ms": 3112,
 "stderr": "\n/testbed/src/compiler/compile/utils/scope.ts:50\n\t\t\t} else if (node.type === 'Identifier' && is_reference(node as ESTreeNode, parent as ESTreeNode)) {\n                                                        ^\nTypeError: is_reference_1.default is not a function\n    at Object.enter (/testbed/src/compiler/compile/utils/scope.ts:50:57)\n    at visit (/testbed/node_modules/estree-walker/src/estree-walker.js:22:9)\n    at visit (/testbed/node_modules/estree-walker/src/estree-walker.js:44:4)\n    at visit (/testbed/node_modules/estree-walker/src/estree-walker.js:39:34)\n    at visit (/testbed/node_modules/estree-walker/src/estree-walker.js:39:34)\n    at Object.walk (/testbed/node_modules/estree-walker/src/estree-walker.js:2:2)\n    at Object.create_scopes (/testbed/src/compiler/compile/utils/scope.ts:13:2)\n    at Component.walk_instance_js_pre_template (/testbed/src/compiler/compile/Component.ts:643:51)\n    at new Component (/testbed/src/compiler/compile/Component.ts:172:8)\n    at compile (/testbed/src/compiler/compile/index.ts:72:20)\n",
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "guidance": "stderr contains error-like diagnostics while the final exit code is 0. Inspect stderr before treating this command as successful; shell control flow may have masked a failed subcommand.",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "write",
    "paths": [
     "t_smoke.js"
    ]
   }
  ],
  "reads": [
   "/testbed"
  ],
  "command_sha256": [
   "491cd8a6f526ba3ba8be20239657f9b33cf962f7cba25b8201ce0498e66aa95a"
  ]
 },
 "device_targets": []
}
````

### Turn 7 — assistant text

Needs esModuleInterop; retrying with that option.

### Turn 7 — tool call call_0007 (exec)

````json
{
 "command": "cd /testbed && cat > t_smoke.js <<'EOF'\nrequire('ts-node').register({transpileOnly:true, compilerOptions:{module:'commonjs',esModuleInterop:true}});\nconst {compile}=require('./src/compiler/index.ts');\nfor (const src of ['<script>import Foo from \"./Foo.svelte\";</script><Foo x-y-z={42}/>','<script>import Foo from \"./Foo.svelte\";let o={};</script><Foo {...o} x-y-z={42}/>']) {\n const c=compile(src,{generate:'ssr'}).js.code; console.log(c.split('\\n').filter(l=>l.includes('$$render(')).join('\\n'));}\nEOF\ntimeout 60 node t_smoke.js; rm t_smoke.js"
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
 "stdout": "\treturn `${validate_component(Foo, 'Foo').$$render($$result, { \"x-y-z\": 42 }, {}, {})}`;\n\treturn `${validate_component(Foo, 'Foo').$$render($$result, Object.assign(o, { \"x-y-z\": 42 }), {}, {})}`;\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 3415,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "write",
    "paths": [
     "t_smoke.js"
    ]
   }
  ],
  "reads": [
   "/testbed"
  ],
  "command_sha256": [
   "69d212bb22473061d2b2315f63c76ea5d7f63f4c84468dcd599cb203aa100bbc"
  ]
 }
}
````

### Turn 8 — assistant text

I fixed the bug: in SSR mode, component props with names that aren't valid JavaScript identifiers are now quoted. `<Foo x-y-z={42}/>` now compiles to:

```js
$$render($$result, { "x-y-z": 42 }, {}, {})
```

The change is in `src/compiler/compile/render_ssr/handlers/InlineComponent.ts`. When that file builds the props object, it now passes each prop name through `quote_name_if_necessary`. That helper was already imported there and already used for slot names. It quotes only names that need it, so ordinary names are unchanged. The fix is applied in both places props are built:
- **Without a spread:** gives `{ "x-y-z": 42 }`
- **With a spread** (`<Foo {...o} x-y-z={42}/>`): gives `Object.assign(o, { "x-y-z": 42 })`

I checked this by compiling both cases in SSR mode from the source and reading the generated code, which matched the output above. I did not run the project's test suite.

`package.json` and `package-lock.json` already had uncommitted changes before I started (including `lint` set to `echo noop`). I didn't touch them.

### Turn 9 — assistant text

SSR output now quotes illegal component property names, so `<Foo x-y-z={42}/>` compiles to `{ "x-y-z": 42 }` instead of `{ x-y-z: 42 }`.

The fix is in `src/compiler/compile/render_ssr/handlers/InlineComponent.ts`. Attribute names now go through `quote_name_if_necessary`, which was already imported there and used for slot names. Both places that build props use it: the plain props object and the spread (`Object.assign`) case.

I compiled two components in SSR mode as a quick check, and both came out quoted:
- Without a spread: `$$render($$result, { "x-y-z": 42 }, {}, {})`
- With a spread: `$$render($$result, Object.assign(o, { "x-y-z": 42 }), {}, {})`

I didn't run the project's full test suite.

Binding names are still output unquoted. Normal bindings are valid identifiers, so I left them alone.

`package.json` and `package-lock.json` were already modified before I started, and I didn't touch them.

## Final answer

SSR output now quotes illegal component property names, so `<Foo x-y-z={42}/>` compiles to `{ "x-y-z": 42 }` instead of `{ x-y-z: 42 }`.

The fix is in `src/compiler/compile/render_ssr/handlers/InlineComponent.ts`. Attribute names now go through `quote_name_if_necessary`, which was already imported there and used for slot names. Both places that build props use it: the plain props object and the spread (`Object.assign`) case.

I compiled two components in SSR mode as a quick check, and both came out quoted:
- Without a spread: `$$render($$result, { "x-y-z": 42 }, {}, {})`
- With a spread: `$$render($$result, Object.assign(o, { "x-y-z": 42 }), {}, {})`

I didn't run the project's full test suite.

Binding names are still output unquoted. Normal bindings are valid identifiers, so I left them alone.

`package.json` and `package-lock.json` were already modified before I started, and I didn't touch them.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 146555 | 2315 | 134370 | 12167 | 148870 |
