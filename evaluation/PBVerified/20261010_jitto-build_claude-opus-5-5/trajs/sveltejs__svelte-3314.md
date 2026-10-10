# Instance: sveltejs__svelte-3314

- Final resolved (evaluator, logs/sveltejs__svelte-3314_result.json): True
- Run state: DONE
- One attempt. Duration 50.3 s, turns 7, actor cost $0.1425564, container commands 3
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/sveltejs__svelte-3314/repo
</uploaded_files>
I've uploaded a JavaScript code repository in the directory /work/sveltejs__svelte-3314/repo. Consider the following issue description:

<issue_description>
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

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/sveltejs__svelte-3314/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/sveltejs__svelte-3314/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/sveltejs__svelte-3314/bin/envrun 'git status --short && ls'
Edits you make under /work/sveltejs__svelte-3314/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cat src/compiler/compile/render_ssr/handlers/InlineComponent.ts && grep -rn "quote_name_if_necessary\|quote_prop_if_necessary" src | head
```

tool result:

```
import { escape, escape_template, stringify } from '../../utils/stringify';
import { quote_name_if_necessary } from '../../../utils/names';
import { snip } from '../../utils/snip';
import Renderer, { RenderOptions } from '../Renderer';
import { stringify_props } from '../../utils/stringify_props';
import { get_slot_scope } from './shared/get_slot_scope';
import { AppendTarget } from '../../../interfaces';
import InlineComponent from '../../nodes/InlineComponent';
import { INode } from '../../nodes/interfaces';
import Text from '../../nodes/Text';

function stringify_attribute(chunk: INode) {
	if (chunk.type === 'Text') {
		return escape_template(escape((chunk as Text).data));
	}

	return '${@escape(' + snip(chunk) + ')}';
}

function get_attribute_value(attribute) {
	if (attribute.is_true) return `true`;
	if (attribute.chunks.length === 0) return `''`;

	if (attribute.chunks.length === 1) {
		const chunk = attribute.chunks[0];
		if (chunk.type === 'Text') {
			return stringify(chunk.data);
		}

		return snip(chunk);
	}

	return '`' + attribute.chunks.map(stringify_attribute).join('') + '`';
}

export default function(node: InlineComponent, renderer: Renderer, options: RenderOptions) {
	const binding_props = [];
	const binding_fns = [];

	node.bindings.forEach(binding => {
		renderer.has_bindings = true;

		// TODO this probably won't work for contextual bindings
		const snippet = snip(binding.expression);

		binding_props.push(`${binding.name}: ${snippet}`);
		binding_fns.push(`${binding.name}: $$value => { ${snippet} = $$value; $$settled = false }`);
	});

	const uses_spread = node.attributes.find(attr => attr.is_spread);

	let props;

	if (uses_spread) {
		props = `@_Object.assign(${
			node.attributes
				.map(attribute => {
					if (attribute.is_spread) {
						return snip(attribute.expression);
					} else {
						return `{ ${attribute.name}: ${get_attribute_value(attribute)} }`;
					}
				})
				.concat(binding_props.map(p => `{ ${p} }`))
				.join(', ')
		})`;
	} else {
		props = stringify_props(
			node.attributes
				.map(attribute => `${attribute.name}: ${get_attribute_value(attribute)}`)
				.concat(binding_props)
		);
	}

	const bindings = stringify_props(binding_fns);

	const expression = (
		node.name === 'svelte:self'
			? '__svelte:self__' // TODO conflict-proof this
			: node.name === 'svelte:component'
				? `((${snip(node.expression)}) || @missing_component)`
				: node.name
	);

	const slot_fns = [];

	if (node.children.length) {
		const target: AppendTarget = {
			slots: { default: '' },
			slot_stack: ['default']
		};

		renderer.targets.push(target);

		const slot_scopes = new Map();
		slot_scopes.set('default', get_slot_scope(node.lets));

		renderer.render(node.children, Object.assign({}, options, {
			slot_scopes
		}));

		Object.keys(target.slots).forEach(name => {
			const slot_scope = slot_scopes.get(name);

			slot_fns.push(
				`${quote_name_if_necessary(name)}: (${slot_scope}) => \`${target.slots[name]}\``
			);
		});

		renderer.targets.pop();
	}

	const slots = stringify_props(slot_fns);

	renderer.append(`\${@validate_component(${expression}, '${node.name}').$$render($$result, ${props}, ${bindings}, ${slots})}`);
}
src/compiler/utils/names.ts:116:export function quote_name_if_necessary(name: string) {
src/compiler/utils/names.ts:121:export function quote_prop_if_necessary(name: string) {
src/compiler/compile/render_ssr/handlers/InlineComponent.ts:2:import { quote_name_if_necessary } from '../../../utils/names';
src/compiler/compile/render_ssr/handlers/InlineComponent.ts:106:				`${quote_name_if_necessary(name)}: (${slot_scope}) => \`${target.slots[name]}\``
src/compiler/compile/render_ssr/handlers/Element.ts:1:import { is_void, quote_prop_if_necessary, quote_name_if_necessary } from '../../../utils/names';
src/compiler/compile/render_ssr/handlers/Element.ts:88:		const snippet = expression ? snip(expression) : `ctx${quote_prop_if_necessary(name)}`;
src/compiler/compile/render_ssr/handlers/Element.ts:104:					args.push(`{ ${quote_name_if_necessary(attribute.name)}: true }`);
src/compiler/compile/render_ssr/handlers/Element.ts:111:					args.push(`{ ${quote_name_if_necessary(attribute.name)}: ${snip(attribute.chunks[0])} }`);
src/compiler/compile/render_ssr/handlers/Element.ts:114:					args.push(`{ ${quote_name_if_necessary(attribute.name)}: [\`${stringify_attribute(attribute, true)}\`, \`\${${class_expression}}\`].join(' ').trim() }`);
src/compiler/compile/render_ssr/handlers/Element.ts:116:					args.push(`{ ${quote_name_if_necessary(attribute.name)}: \`${stringify_attribute(attribute, true)}\` }`);
```

**assistant:** Let me reproduce first.

**tool call: Bash**

```bash
cat > /work/sveltejs__svelte-3314/repo/repro.js <<'EOF'
const svelte = require('./compiler.js');
const src = `<script>import Foo from './Foo.svelte';</script><Foo x-y-z={42} a-b="c"/><Foo {...{}} x-y-z={42}/>`;
const { js } = svelte.compile(src, { generate: 'ssr' });
console.log(js.code.split('\n').filter(l => l.includes('$$render')).join('\n'));
new Function(js.code.replace(/^import.*$/mg, '').replace(/export default/, 'return'));
console.log('parses OK');
EOF
/work/sveltejs__svelte-3314/bin/envrun 'ls compiler.js; node repro.js'
```

tool result:

```
Exit code 1
compiler.js
	return `${validate_component(Foo, 'Foo').$$render($$result, { x-y-z: 42, a-b: "c" }, {}, {})}${validate_component(Foo, 'Foo').$$render($$result, Object.assign({}, { x-y-z: 42 }), {}, {})}`;
undefined:8
	return `${validate_component(Foo, 'Foo').$$render($$result, { x-y-z: 42, a-b: "c" }, {}, {})}${validate_component(Foo, 'Foo').$$render($$result, Object.assign({}, { x-y-z: 42 }), {}, {})}`;
	                                                               ^

SyntaxError: Unexpected token '-'
    at new Function (<anonymous>)
    at Object.<anonymous> (/testbed/repro.js:5:1)
    at Module._compile (node:internal/modules/cjs/loader:1198:14)
    at Object.Module._extensions..js (node:internal/modules/cjs/loader:1252:10)
    at Module.load (node:internal/modules/cjs/loader:1076:32)
    at Function.Module._load (node:internal/modules/cjs/loader:911:12)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:81:12)
    at node:internal/main/run_main_module:22:47
```

**assistant:** Reproduced. Now the fix:

**tool call: Bash**

```bash
f=src/compiler/compile/render_ssr/handlers/InlineComponent.ts && sed -i '' \
 -e 's/return `{ \${attribute.name}: \${get_attribute_value(attribute)} }`;/return `{ ${quote_name_if_necessary(attribute.name)}: ${get_attribute_value(attribute)} }`;/' \
 -e 's/\.map(attribute => `\${attribute.name}: \${get_attribute_value(attribute)}`)/.map(attribute => `${quote_name_if_necessary(attribute.name)}: ${get_attribute_value(attribute)}`)/' $f && git diff
```

tool result:

```
<persisted-output>
Output too large (177.8KB). Full output saved to: <actor-session-dir>

Preview (first 2KB):
diff --git a/package-lock.json b/package-lock.json
index bcde04de..a2671440 100644
--- a/package-lock.json
+++ b/package-lock.json
@@ -1,8 +1,4841 @@
 {
   "name": "svelte",
-  "version": "3.6.7",
-  "lockfileVersion": 1,
+  "version": "3.6.9",
+  "lockfileVersion": 2,
   "requires": true,
+  "packages": {
+    "": {
+      "name": "svelte",
+      "version": "3.6.9",
+      "license": "MIT",
+      "devDependencies": {
+        "@types/mocha": "^5.2.7",
+        "@types/node": "=8",
+        "@typescript-eslint/eslint-plugin": "^1.11.0",
+        "@typescript-eslint/parser": "^1.11.0",
+        "acorn": "^6.2.0",
+        "acorn-dynamic-import": "^4.0.0",
+        "agadoo": "^1.0.1",
+        "c8": "^5.0.1",
+        "codecov": "^3.5.0",
+        "css-tree": "1.0.0-alpha22",
+        "eslint": "^6.0.1",
+        "eslint-plugin-import": "^2.18.0",
+        "eslint-plugin-svelte3": "^2.6.0",
+        "estree-walker": "^0.6.1",
+        "is-reference": "^1.1.3",
+        "jsdom": "^15.1.1",
+        "kleur": "^3.0.3",
+        "locate-character": "^2.0.5",
+        "magic-string": "^0.25.3",
+        "mocha": "^6.1.4",
+        "puppeteer": "^1.18.1",
+        "rollup": "^1.16.6",
+        "rollup-plugin-commonjs": "^10.0.1",
+        "rollup-plugin-json": "^4.0.0",
+        "rollup-plugin-node-resolve": "^5.2.0",
+        "rollup-plugin-replace": "^2.2.0",
+        "rollup-plugin-sucrase": "^2.1.0",
+        "rollup-plugin-typescript": "^1.0.1",
+        "rollup-plugin-virtual": "^1.0.1",
+        "source-map": "^0.6.1",
+        "source-map-support": "^0.5.12",
+        "tiny-glob": "^0.2.6",
+        "ts-node": "^8.3.0",
+        "tslib": "^1.10.0",
+        "typescript": "^3.5.2"
+      },
+      "engines": {
+        "node": ">= 8"
+      }
+    },
+    "node_modules/@babel/code-frame": {
+      "version": "7.0.0",
+      "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.0.0.tgz",
...
</persisted-output>
```

**assistant:** `package-lock.json` shows as modified, but I didn't change it. Let me check what's actually changed.

**tool call: Bash**

```bash
git status --short; git diff -- src
```

tool result:

```
 M package-lock.json
 M package.json
 M src/compiler/compile/render_ssr/handlers/InlineComponent.ts
?? Dockerfile
?? repro.js
diff --git a/src/compiler/compile/render_ssr/handlers/InlineComponent.ts b/src/compiler/compile/render_ssr/handlers/InlineComponent.ts
index 320bf5e6..74d990a3 100644
--- a/src/compiler/compile/render_ssr/handlers/InlineComponent.ts
+++ b/src/compiler/compile/render_ssr/handlers/InlineComponent.ts
@@ -58,7 +58,7 @@ export default function(node: InlineComponent, renderer: Renderer, options: Rend
 					if (attribute.is_spread) {
 						return snip(attribute.expression);
 					} else {
-						return `{ ${attribute.name}: ${get_attribute_value(attribute)} }`;
+						return `{ ${quote_name_if_necessary(attribute.name)}: ${get_attribute_value(attribute)} }`;
 					}
 				})
 				.concat(binding_props.map(p => `{ ${p} }`))
@@ -67,7 +67,7 @@ export default function(node: InlineComponent, renderer: Renderer, options: Rend
 	} else {
 		props = stringify_props(
 			node.attributes
-				.map(attribute => `${attribute.name}: ${get_attribute_value(attribute)}`)
+				.map(attribute => `${quote_name_if_necessary(attribute.name)}: ${get_attribute_value(attribute)}`)
 				.concat(binding_props)
 		);
 	}
```

**assistant:** The `package.json`/`package-lock.json`/`Dockerfile` changes come from the environment setup, not from me, so I'll leave them alone. Next I'll rebuild the compiler and rerun the repro.

**tool call: Bash**

```bash
/work/sveltejs__svelte-3314/bin/envrun 'npx rollup -c 2>&1 | tail -5; node repro.js'
```

tool result:

```
(!) Circular dependency: src/compiler/compile/nodes/shared/map_children.ts -> src/compiler/compile/nodes/Head.ts -> src/compiler/compile/nodes/shared/map_children.ts
(!) Circular dependency: src/compiler/compile/nodes/shared/map_children.ts -> src/compiler/compile/nodes/IfBlock.ts -> src/compiler/compile/nodes/shared/map_children.ts
(!) Circular dependency: src/compiler/compile/nodes/shared/map_children.ts -> src/compiler/compile/nodes/InlineComponent.ts -> src/compiler/compile/nodes/shared/map_children.ts
(!) Circular dependency: src/compiler/compile/nodes/shared/map_children.ts -> src/compiler/compile/nodes/Title.ts -> src/compiler/compile/nodes/shared/map_children.ts
created compiler.js in 1.3s
	return `${validate_component(Foo, 'Foo').$$render($$result, { "x-y-z": 42, "a-b": "c" }, {}, {})}${validate_component(Foo, 'Foo').$$render($$result, Object.assign({}, { "x-y-z": 42 }), {}, {})}`;
parses OK
```

**assistant:** Fixed, covering both the spread and non-spread cases. Now the SSR and runtime tests:

**tool call: Bash**

```bash
rm repro.js; /work/sveltejs__svelte-3314/bin/envrun 'npx mocha --opts mocha.opts --grep "ssr|runtime|js " 2>&1 | tail -30'
```

tool result:

```
    ✓ whitespace-normal
    - window-bind-scroll-update
    ✓ window-binding-multiple-handlers
    ✓ window-event-custom

  vars
    ✓ $$props, generate: ssr
    ✓ $$props-logicless, generate: ssr
    ✓ actions, generate: ssr
    ✓ animations, generate: ssr
    ✓ assumed-global, generate: ssr
    ✓ component-namespaced, generate: ssr
    ✓ duplicate-globals, generate: ssr
    ✓ duplicate-non-hoistable, generate: ssr
    ✓ duplicate-vars, generate: ssr
    ✓ implicit-reactive, generate: ssr
    ✓ imports, generate: ssr
    ✓ mutated-vs-reassigned, generate: ssr
    ✓ mutated-vs-reassigned-bindings, generate: ssr
    ✓ props, generate: ssr
    ✓ store-referenced, generate: ssr
    ✓ store-unreferenced, generate: ssr
    ✓ template-references, generate: ssr
    ✓ transitions, generate: ssr
    ✓ undeclared, generate: ssr


  1899 passing (12s)
  35 pending
```

**assistant:** SSR now quotes property names that aren't valid JavaScript identifiers when it passes props to a component, so `<Foo x-y-z={42}/>` compiles to `$$render($$result, { "x-y-z": 42 }, {}, {})`.

**The fix** is in `src/compiler/compile/render_ssr/handlers/InlineComponent.ts`. Component attribute names now go through the existing `quote_name_if_necessary` helper, which the same file already used for slot names. There were two places that built the props object, and both are fixed:
- the normal case: `{ x-y-z: 42 }` becomes `{ "x-y-z": 42 }`
- the spread case (`<Foo {...obj} x-y-z={42}/>`): `Object.assign({}, { x-y-z: 42 })` now quotes the name too

Normal names like `foo` stay unquoted, so output for existing components doesn't change.

**Verification:**
- Before the fix, compiling a test component in SSR mode produced code that failed with `SyntaxError: Unexpected token '-'`. After rebuilding the compiler, the generated code has quoted keys and parses cleanly.
- The SSR, runtime and JS-output tests pass: 1899 passing, 0 failing, 35 pending (skipped).

I deleted the reproduction script. Git also shows changes to `package.json` and `package-lock.json` and an untracked `Dockerfile`. They were already there from the environment setup, not from me, so I left them alone.

_session end: success, turns 7, is_error False_

## Container commands (task container, no network; broker log)

- `rc=1` 0.46 s: ls compiler.js; node repro.js
- `rc=0` 3.57 s: npx rollup -c 2>&1 | tail -5; node repro.js
- `rc=0` 15.69 s: npx mocha --opts mocha.opts --grep "ssr|runtime|js " 2>&1 | tail -30
