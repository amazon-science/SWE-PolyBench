# Instance: sveltejs__svelte-1095

- Final resolved (evaluator, logs/sveltejs__svelte-1095_result.json): True
- Run state: DONE
- One attempt. Duration 324.0 s, turns 12, actor cost $0.368705, container commands 4
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/sveltejs__svelte-1095/repo
</uploaded_files>
I've uploaded a JavaScript code repository in the directory /work/sveltejs__svelte-1095/repo. Consider the following issue description:

<issue_description>
case-sensitivity of SVG viewBox likely to cause silent errors
In most 'try online' tools, the SVG `viewBox` attribute is handled the same whether properly camel-cased or not (`viewbox`). Svelte only recognizes `viewBox`. This can make it difficult for developers new to SVG - especially when they are starting with random sample code from blogs/tutorials - as improper use simply doesn't show up. Either an compile-time warning or acceptance of both variants would be helpful.

Example:
When I try to render `<svg viewbox="-250 -250 500 500">` with the [Svelte](https://svelte.technology/repl?version=1.50.0&gist=3547a556f7fcdf284516a39d24fbff24), my image is cutoff. Whereas on W3Schools or [CodePen](https://codepen.io/anon/pen/opWRbY), it renders fine, indicating that `width` and `height` aren't inherently mandatory. I had the same results testing locally and with REPL.

When I try `<svg width=500 height=500 viewbox="-250 -250 500 500">` it will adjust the size correctly, but doesn't respect the viewbox.

Since I started with pasting a blog example, I mistakenly thought svelte couldn't handle viewbox. 

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/sveltejs__svelte-1095/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/sveltejs__svelte-1095/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/sveltejs__svelte-1095/bin/envrun 'git status --short && ls'
Edits you make under /work/sveltejs__svelte-1095/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

Follow these steps to resolve the issue:
1. As a first step, explore the repo to find and read the code relevant to the <issue_description>.
2. Create a script or a small test to reproduce the error and execute it with envrun, to confirm the error.
3. Edit the source code of the repo to resolve the issue.
4. Rerun your reproduction and confirm that the error is fixed.
5. Think about edge cases and make sure your fix handles them as well; run the existing tests closest to the code you changed.
6. Delete any scripts or files you created only for reproduction or checking, so that only the fix remains in the repository.

```

## Trajectory

_session start: model claude-opus-5-5, tools ['Bash', 'Edit', 'Glob', 'Grep', 'Read', 'Write'], MCP servers []_

**tool call: Bash**

```bash
ls src src/validate/html && cat package.json | grep '"version"' && grep -rn "viewBox\|svg" src --include=*.ts | head -30; git log --oneline -1; git status
```

tool result:

```
src:
config.ts
css
generators
index.ts
interfaces.ts
parse
server-side-rendering
shared
utils
validate

src/validate/html:
a11y.ts
index.ts
validateElement.ts
validateEventHandler.ts
validateHead.ts
validateWindow.ts
  "version": "1.51.1",
(eval):1: no matches found: --include=*.ts
9cfa1747 -> v1.51.1
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
```

**tool call: Bash**

```bash
grep -rn "viewBox\|svg\|namespace" src | grep -v "^src/shared" | head -40; cat src/validate/html/validateElement.ts; ls test/validator/samples | grep -i -E "svg|attr|case|namespace"
```

tool result:

```
src/validate/js/propValidators/namespace.ts:1:import * as namespaces from '../../../utils/namespaces';
src/validate/js/propValidators/namespace.ts:6:const valid = new Set(namespaces.validNamespaces);
src/validate/js/propValidators/namespace.ts:8:export default function namespace(validator: Validator, prop: Node) {
src/validate/js/propValidators/namespace.ts:13:			`The 'namespace' property must be a string literal representing a valid namespace`,
src/validate/js/propValidators/namespace.ts:19:		const match = fuzzymatch(ns, namespaces.validNamespaces);
src/validate/js/propValidators/namespace.ts:22:				`Invalid namespace '${ns}' (did you mean '${match}'?)`,
src/validate/js/propValidators/namespace.ts:26:			validator.error(`Invalid namespace '${ns}'`, prop.start);
src/validate/js/propValidators/index.ts:11:import namespace from './namespace';
src/validate/js/propValidators/index.ts:30:	namespace,
src/validate/js/index.ts:5:import namespaces from '../../utils/namespaces';
src/validate/js/index.ts:79:			if (props.has('namespace')) {
src/validate/js/index.ts:80:				const ns = props.get('namespace').value.value;
src/validate/js/index.ts:81:				validator.namespace = namespaces[ns] || ns;
src/validate/html/a11y.ts:1:import * as namespaces from '../../utils/namespaces';
src/validate/html/a11y.ts:122:			// anchor-in-svg-is-valid
src/validate/html/validateElement.ts:1:import * as namespaces from '../../utils/namespaces';
src/validate/html/validateElement.ts:6:const svg = /^(?:altGlyph|altGlyphDef|altGlyphItem|animate|animateColor|animateMotion|animateTransform|circle|clipPath|color-profile|cursor|defs|desc|discard|ellipse|feBlend|feColorMatrix|feComponentTransfer|feComposite|feConvolveMatrix|feDiffuseLighting|feDisplacementMap|feDistantLight|feDropShadow|feFlood|feFuncA|feFuncB|feFuncG|feFuncR|feGaussianBlur|feImage|feMerge|feMergeNode|feMorphology|feOffset|fePointLight|feSpecularLighting|feSpotLight|feTile|feTurbulence|filter|font|font-face|font-face-format|font-face-name|font-face-src|font-face-uri|foreignObject|g|glyph|glyphRef|hatch|hatchpath|hkern|image|line|linearGradient|marker|mask|mesh|meshgradient|meshpatch|meshrow|metadata|missing-glyph|mpath|path|pattern|polygon|polyline|radialGradient|rect|set|solidcolor|stop|switch|symbol|text|textPath|tref|tspan|unknown|use|view|vkern)$/;
src/validate/html/validateElement.ts:28:	if (elementStack.length === 0 && validator.namespace !== namespaces.svg && svg.test(node.name)) {
src/validate/html/validateElement.ts:30:			`<${node.name}> is an SVG element – did you forget to add { namespace: 'svg' } ?`,
src/validate/index.ts:29:	namespace: string;
src/validate/index.ts:51:		this.namespace = null;
src/utils/namespaces.ts:3:export const svg = 'http://www.w3.org/2000/svg';
src/utils/namespaces.ts:5:export const xml = 'http://www.w3.org/XML/1998/namespace';
src/utils/namespaces.ts:11:	'svg',
src/utils/namespaces.ts:17:	svg,
src/utils/namespaces.ts:23:const namespaces: Record<string, string> = { html, mathml, svg, xlink, xml, xmlns };
src/utils/namespaces.ts:25:export default namespaces;
src/generators/nodes/Text.ts:28:	return parentElement.namespace || elementsWithoutText.has(parentElement.name);
src/generators/nodes/Element.ts:15:import * as namespaces from '../../utils/namespaces';
src/generators/nodes/Element.ts:33:		this.namespace = this.name === 'svg' ?
src/generators/nodes/Element.ts:34:			namespaces.svg :
src/generators/nodes/Element.ts:35:			parentElement ? parentElement.namespace : this.generator.namespace;
src/generators/nodes/Element.ts:42:					this.namespace = attribute.value[0].data;
src/generators/nodes/Element.ts:178:		const renderStatement = getRenderStatement(this.generator, this.namespace, this.name);
src/generators/nodes/Element.ts:186:					${name} = ${getClaimStatement(generator, this.namespace, parentNodes, this)};
src/generators/nodes/Element.ts:227:		if (!this.namespace && this.canUseInnerHTML && this.children.length > 0) {
src/generators/nodes/Element.ts:671:	namespace: string,
src/generators/nodes/Element.ts:674:	if (namespace === 'http://www.w3.org/2000/svg') {
src/generators/nodes/Element.ts:678:	if (namespace) {
src/generators/nodes/Element.ts:679:		return `document.createElementNS("${namespace}", "${name}")`;
import * as namespaces from '../../utils/namespaces';
import validateEventHandler from './validateEventHandler';
import validate, { Validator } from '../index';
import { Node } from '../../interfaces';

const svg = /^(?:altGlyph|altGlyphDef|altGlyphItem|animate|animateColor|animateMotion|animateTransform|circle|clipPath|color-profile|cursor|defs|desc|discard|ellipse|feBlend|feColorMatrix|feComponentTransfer|feComposite|feConvolveMatrix|feDiffuseLighting|feDisplacementMap|feDistantLight|feDropShadow|feFlood|feFuncA|feFuncB|feFuncG|feFuncR|feGaussianBlur|feImage|feMerge|feMergeNode|feMorphology|feOffset|fePointLight|feSpecularLighting|feSpotLight|feTile|feTurbulence|filter|font|font-face|font-face-format|font-face-name|font-face-src|font-face-uri|foreignObject|g|glyph|glyphRef|hatch|hatchpath|hkern|image|line|linearGradient|marker|mask|mesh|meshgradient|meshpatch|meshrow|metadata|missing-glyph|mpath|path|pattern|polygon|polyline|radialGradient|rect|set|solidcolor|stop|switch|symbol|text|textPath|tref|tspan|unknown|use|view|vkern)$/;

export default function validateElement(
	validator: Validator,
	node: Node,
	refs: Map<string, Node[]>,
	refCallees: Node[],
	stack: Node[],
	elementStack: Node[]
) {
	const isComponent =
		node.name === ':Self' || node.name === ':Component' || validator.components.has(node.name);

	if (isComponent) {
		validator.used.components.add(node.name);
	}

	if (!isComponent && /^[A-Z]/.test(node.name[0])) {
		// TODO upgrade to validator.error in v2
		validator.warn(`${node.name} component is not defined`, node.start);
	}

	if (elementStack.length === 0 && validator.namespace !== namespaces.svg && svg.test(node.name)) {
		validator.warn(
			`<${node.name}> is an SVG element – did you forget to add { namesp
[... 7058 more characters not shown]
```

**tool call: Bash**

```bash
grep -rli "viewbox" test | head; grep -rn "attribute.name\|\.name" src/generators/nodes/Attribute.ts | head -20; grep -rn "Attribute" src/server-side-rendering/visitors/Element.ts | head
```

tool result:

```
src/generators/nodes/Attribute.ts:40:		this.name = name;
src/generators/nodes/Attribute.ts:46:		const name = this.name;
src/generators/nodes/Attribute.ts:56:		let metadata = node.namespace ? null : attributeLookup[name];
src/generators/nodes/Attribute.ts:57:		if (metadata && metadata.appliesTo && !~metadata.appliesTo.indexOf(node.name))
src/generators/nodes/Attribute.ts:62:			(node.name === 'option' || // TODO check it's actually bound
src/generators/nodes/Attribute.ts:63:				(node.name === 'input' &&
src/generators/nodes/Attribute.ts:66:							attribute.type === 'Binding' && /checked|group/.test(attribute.name)
src/generators/nodes/Attribute.ts:81:		const isLegacyInputType = this.generator.legacy && name === 'type' && this.parent.name === 'input';
src/generators/nodes/Attribute.ts:83:		const isDataSet = /^data-/.test(name) && !this.generator.legacy && !node.namespace;
src/generators/nodes/Attribute.ts:112:					block.contexts.has(expression.name) ||
src/generators/nodes/Attribute.ts:144:				name === 'value' && node.name === 'select';
grep: src/server-side-rendering/visitors/Element.ts: No such file or directory
```

**tool call: Bash**

```bash
sed -n 1,60p src/generators/nodes/Attribute.ts; ls src/generators/server-side-rendering/visitors 2>/dev/null; grep -rn "attribute.name" src/generators/server-side-rendering/visitors/Element.ts; git diff --stat; ls test/runtime/samples | grep -i svg
```

tool result:

```
import deindent from '../../utils/deindent';
import { stringify } from '../../utils/stringify';
import getExpressionPrecedence from '../../utils/getExpressionPrecedence';
import { DomGenerator } from '../dom/index';
import Node from './shared/Node';
import Element from './Element';
import Block from '../dom/Block';

export interface StyleProp {
	key: string;
	value: Node[];
}

export default class Attribute {
	type: 'Attribute';
	start: number;
	end: number;

	generator: DomGenerator;
	parent: Element;
	name: string;
	value: true | Node[]
	expression: Node;

	constructor({
		generator,
		name,
		value,
		parent
	}: {
		generator: DomGenerator,
		name: string,
		value: Node[],
		parent: Element
	}) {
		this.type = 'Attribute';
		this.generator = generator;
		this.parent = parent;

		this.name = name;
		this.value = value;
	}

	render(block: Block) {
		const node = this.parent;
		const name = this.name;

		if (name === 'style') {
			const styleProps = optimizeStyle(this.value);
			if (styleProps) {
				this.renderStyle(block, styleProps);
				return;
			}
		}

		let metadata = node.namespace ? null : attributeLookup[name];
		if (metadata && metadata.appliesTo && !~metadata.appliesTo.indexOf(node.name))
			metadata = null;

		const isIndirectlyBoundValue =
AwaitBlock.ts
Comment.ts
Component.ts
EachBlock.ts
Element.ts
Head.ts
IfBlock.ts
MustacheTag.ts
RawMustacheTag.ts
Slot.ts
Text.ts
Title.ts
Window.ts
index.ts
shared
src/generators/server-side-rendering/visitors/Element.ts:26:		const slot = node.attributes.find((attribute: Node) => attribute.name === 'slot');
src/generators/server-side-rendering/visitors/Element.ts:36:		if (attribute.name === 'value' && node.name === 'textarea') {
src/generators/server-side-rendering/visitors/Element.ts:39:			let str = ` ${attribute.name}`;
 package.json |    2 +-
 yarn.lock    | 7154 ++++++++++++++++++++++++++++++----------------------------
 2 files changed, 3748 insertions(+), 3408 deletions(-)
attribute-empty-svg
svg
svg-attributes
svg-child-component-declared-namespace
svg-child-component-declared-namespace-shorthand
svg-class
svg-each-block-anchor
svg-each-block-namespace
svg-multiple
svg-no-whitespace
svg-xlink
svg-xmlns
```

**tool call: Bash**

```bash
sed -n 1,80p src/generators/nodes/Element.ts; sed -n 1,70p src/generators/server-side-rendering/visitors/Element.ts
```

tool result:

```
import deindent from '../../utils/deindent';
import { stringify, escapeHTML } from '../../utils/stringify';
import flattenReference from '../../utils/flattenReference';
import isVoidElementName from '../../utils/isVoidElementName';
import validCalleeObjects from '../../utils/validCalleeObjects';
import reservedNames from '../../utils/reservedNames';
import Node from './shared/Node';
import Block from '../dom/Block';
import Attribute from './Attribute';
import Binding from './Binding';
import EventHandler from './EventHandler';
import Ref from './Ref';
import Transition from './Transition';
import Text from './Text';
import * as namespaces from '../../utils/namespaces';

export default class Element extends Node {
	type: 'Element';
	name: string;
	attributes: (Attribute | Binding | EventHandler | Ref | Transition)[]; // TODO split these up sooner
	children: Node[];

	init(
		block: Block,
		stripWhitespace: boolean,
		nextSibling: Node
	) {
		if (this.name === 'slot' || this.name === 'option') {
			this.cannotUseInnerHTML();
		}

		const parentElement = this.parent && this.parent.findNearest(/^Element/);
		this.namespace = this.name === 'svg' ?
			namespaces.svg :
			parentElement ? parentElement.namespace : this.generator.namespace;

		this.attributes.forEach(attribute => {
			if (attribute.type === 'Attribute' && attribute.value !== true) {
				// special case — xmlns
				if (attribute.name === 'xmlns') {
					// TODO this attribute must be static – enforce at compile time
					this.namespace = attribute.value[0].data;
				}

				attribute.value.forEach((chunk: Node) => {
					if (chunk.type !== 'Text') {
						if (this.parent) this.parent.cannotUseInnerHTML();

						const dependencies = chunk.metadata.dependencies;
						block.addDependencies(dependencies);

						// special case — <option value='{{foo}}'> — see below
						if (
							this.name === 'option' &&
							attribute.name === 'value'
						) {
							let select = this.parent;
							while (select && (select.type !== 'Element' || select.name !== 'select')) select = select.parent;

							if (select && select.selectBindingDependencies) {
								select.selectBindingDependencies.forEach(prop => {
									dependencies.forEach((dependency: string) => {
										this.generator.indirectDependencies.get(prop).add(dependency);
									});
								});
							}
						}
					}
				});
			} else {
				if (this.parent) this.parent.cannotUseInnerHTML();

				if (attribute.type === 'EventHandler' && attribute.expression) {
					attribute.expression.arguments.forEach((arg: Node) => {
						block.addDependencies(arg.metadata.dependencies);
					});
				} else if (attribute.type === 'Binding') {
					block.addDependencies(attribute.metadata.dependencies);
				} else if (attribute.type === 'Transition') {
					if (attribute.intro)
import visitComponent from './Component';
import visitSlot from './Slot';
import isVoidElementName from '../../../utils/isVoidElementName';
import visit from '../visit';
import { SsrGenerator } from '../index';
import Element from '../../nodes/Element';
import Block from '../Block';
import { Node } from '../../../interfaces';
import stringifyAttributeValue from './shared/stringifyAttributeValue';

export default function visitElement(
	generator: SsrGenerator,
	block: Block,
	node: Element
) {
	if (node.name === 'slot') {
		visitSlot(generator, block, node);
		return;
	}

	let openingTag = `<${node.name}`;
	let textareaContents; // awkward special case

	const slot = node.getStaticAttributeValue('slot');
	if (slot && node.hasAncestor('Component')) {
		const slot = node.attributes.find((attribute: Node) => attribute.name === 'slot');
		const slotName = slot.value[0].data;
		const appendTarget = generator.appendTargets[generator.appendTargets.length - 1];
		appendTarget.slotStack.push(slotName);
		appendTarget.slots[slotName] = '';
	}

	node.attributes.forEach((attribute: Node) => {
		if (attribute.type !== 'Attribute') return;

		if (attribute.name === 'value' && node.name === 'textarea') {
			textareaContents = stringifyAttributeValue(block, attribute.value);
		} else {
			let str = ` ${attribute.name}`;

			if (attribute.value !== true) {
				str += `="${stringifyAttributeValue(block, attribute.value)}"`;
			}

			openingTag += str;
		}
	});

	if (node._needsCssAttribute) {
		openingTag += ` ${generator.stylesheet.id}`;

		if (node._cssRefAttribute) {
			openingTag += ` svelte-ref-${node._cssRefAttribute}`;
		}
	}

	openingTag += '>';

	generator.append(openingTag);

	if (node.name === 'textarea' && textareaContents !== undefined) {
		generator.append(textareaContents);
	} else if (node.name === 'script' || node.name === 'style') {
		generator.append(node.data);
	} else {
		node.children.forEach((child: Node) => {
			visit(generator, block, child);
		});
	}
```

**assistant:** I'll look at how the compiler is built/tested so I can reproduce.

**tool call: Bash**

```bash
grep -n '"scripts"' -A20 package.json; cat test/runtime/samples/svg-attributes/*; ls compiler 2>/dev/null
```

tool result:

```
14:  "scripts": {
15-    "test": "mocha --opts mocha.opts",
16-    "quicktest": "mocha --opts mocha.opts",
17-    "precoverage": "export COVERAGE=true && nyc mocha --opts mocha.coverage.opts",
18-    "coverage": "nyc report --reporter=text-lcov > coverage.lcov",
19-    "codecov": "codecov",
20-    "precodecov": "npm run coverage",
21-    "lint": "echo noop",
22-    "build": "node src/shared/_build.js && rollup -c && rollup -c rollup.store.config.js",
23-    "prepare": "npm run build",
24-    "dev": "node src/shared/_build.js && rollup -c -w",
25-    "pretest": "npm run build",
26-    "prepublishOnly": "npm run lint && npm test",
27-    "prettier": "prettier --write \"src/**/*.ts\""
28-  },
29-  "repository": {
30-    "type": "git",
31-    "url": "https://github.com/sveltejs/svelte.git"
32-  },
33-  "keywords": [
34-    "UI",
export default {
	html: `
		<svg>
			<g>
				<circle class='red'/>
			</g>
		</svg>
	`,

	test ( assert, component, target ) {
		const circle = target.querySelector( 'circle' );
		assert.equal( circle.getAttribute( 'class' ), 'red' );
		component.destroy();
	}
};
<svg>
	<g>
		<circle class='red'/>
	</g>
</svg>
```

**assistant:** Now a reproduction: compile `<svg viewbox=...>` and inspect the generated DOM code.

**tool call: Bash**

```bash
cat > repro.js <<'EOF'
const svelte = require('./compiler/svelte.js');
const src = `<svg viewbox="0 0 10 10" preserveaspectratio="none" data-Foo="x"><rect width='{{w}}' viewbox='{{v}}'/></svg><div contenteditable="true"></div>`;
const dom = svelte.compile(src, {}).code;
console.log(dom.split('\n').filter(l => /Attribute|\.(viewBox|contentEditable)/i.test(l)).join('\n'));
console.log(svelte.compile(src, {generate:'ssr'}).code.split('\n').filter(l=>/svg/.test(l)).join('\n'));
EOF
../bin/envrun 'npm run build >/dev/null 2>&1; node repro.js'
```

tool result:

```
			setAttribute(rect, "width", state.w);
			setAttribute(rect, "viewbox", state.v);
			setAttribute(svg, "viewbox", "0 0 10 10");
			setAttribute(svg, "preserveaspectratio", "none");
			setAttribute(svg, "data-Foo", "x");
			div.contentEditable = "true";
				setAttribute(rect, "width", state.w);
				setAttribute(rect, "viewbox", state.v);
function setAttribute(node, attribute, value) {
	node.setAttribute(attribute, value);
	return `<svg viewbox="0 0 10 10" preserveaspectratio="none" data-Foo="x"><rect width="${state.w}" viewbox="${state.v}"></rect></svg><div contenteditable="true"></div>`;
```

**thinking:**

```
Confirmed the issue: `setAttribute` keeps lowercase SVG attribute names like "viewbox", which SVG ignores (SSR works only because browsers auto-correct case). I'll fix the DOM generator to normalize SVG attribute casing, scoped to the SVG namespace so other attributes stay untouched.


```

**tool call: Bash**

```bash
cat > src/utils/fixAttributeCasing.ts <<'EOF'
// SVG attributes are case-sensitive when set via setAttribute, so
// e.g. `viewbox` must be corrected to `viewBox` (as the HTML parser does)
const svgAttributes = 'attributeName attributeType baseFrequency baseProfile calcMode clipPathUnits contentScriptType contentStyleType diffuseConstant edgeMode externalResourcesRequired filterRes filterUnits glyphRef gradientTransform gradientUnits kernelMatrix kernelUnitLength keyPoints keySplines keyTimes lengthAdjust limitingConeAngle markerHeight markerUnits markerWidth maskContentUnits maskUnits numOctaves pathLength patternContentUnits patternTransform patternUnits pointsAtX pointsAtY pointsAtZ preserveAlpha preserveAspectRatio primitiveUnits refX refY repeatCount repeatDur requiredExtensions requiredFeatures specularConstant specularExponent spreadMethod startOffset stdDeviation stitchTiles surfaceScale systemLanguage tableValues targetX targetY textLength viewBox viewTarget xChannelSelector yChannelSelector zoomAndPan'.split(' ');

const svgAttributeLookup = new Map();
svgAttributes.forEach(name => {
	svgAttributeLookup.set(name.toLowerCase(), name);
});

export default function fixAttributeCasing(name: string) {
	return svgAttributeLookup.get(name.toLowerCase()) || name;
}
EOF
python3 - <<'EOF'
p='src/generators/nodes/Attribute.ts'
s=open(p).read()
s=s.replace("import Block from '../dom/Block';\n","import Block from '../dom/Block';\nimport fixAttributeCasing from '../../utils/fixAttributeCasing';\nimport * as namespaces from '../../utils/namespaces';\n",1)
s=s.replace("""		const node = this.parent;
		const name = this.name;
""","""		const node = this.parent;
		const name = node.namespace === namespaces.svg ? fixAttributeCasing(this.name) : this.name;
""",1)
open(p,'w').write(s)
EOF
git diff src; ../bin/envrun 'npm run build >/dev/null 2>&1; node repro.js'
```

tool result:

```
diff --git a/src/generators/nodes/Attribute.ts b/src/generators/nodes/Attribute.ts
index 63987053..c2cbb017 100644
--- a/src/generators/nodes/Attribute.ts
+++ b/src/generators/nodes/Attribute.ts
@@ -5,6 +5,8 @@ import { DomGenerator } from '../dom/index';
 import Node from './shared/Node';
 import Element from './Element';
 import Block from '../dom/Block';
+import fixAttributeCasing from '../../utils/fixAttributeCasing';
+import * as namespaces from '../../utils/namespaces';
 
 export interface StyleProp {
 	key: string;
@@ -43,7 +45,7 @@ export default class Attribute {
 
 	render(block: Block) {
 		const node = this.parent;
-		const name = this.name;
+		const name = node.namespace === namespaces.svg ? fixAttributeCasing(this.name) : this.name;
 
 		if (name === 'style') {
 			const styleProps = optimizeStyle(this.value);
			setAttribute(rect, "width", state.w);
			setAttribute(rect, "viewBox", state.v);
			setAttribute(svg, "viewBox", "0 0 10 10");
			setAttribute(svg, "preserveAspectRatio", "none");
			setAttribute(svg, "data-Foo", "x");
			div.contentEditable = "true";
				setAttribute(rect, "width", state.w);
				setAttribute(rect, "viewBox", state.v);
function setAttribute(node, attribute, value) {
	node.setAttribute(attribute, value);
	return `<svg viewbox="0 0 10 10" preserveaspectratio="none" data-Foo="x"><rect width="${state.w}" viewbox="${state.v}"></rect></svg><div contenteditable="true"></div>`;
```

**assistant:** The generated DOM code now uses `viewBox` and `preserveAspectRatio`, and leaves unrelated attributes alone. Next I'll check it in the DOM at runtime and run the test suite.

**tool call: Bash**

```bash
mkdir -p /tmp/x; cat > repro2.js <<'EOF'
require('./register')||0;
EOF
rm repro2.js
cat > repro.js <<'EOF'
const svelte = require('./compiler/svelte.js');
const { JSDOM } = require('jsdom');
const window = new JSDOM('<main></main>').window;
const code = svelte.compile(`<svg viewbox="0 0 10 10"><rect viewbox="{{v}}"/></svg>`, { format: 'cjs', name: 'C' }).code;
const m = { exports: {} };
global.document = window.document;
new Function('module', 'exports', 'require', code)(m, m.exports, require);
const C = m.exports;
const target = window.document.querySelector('main');
const c = new C({ target, data: { v: '1 2 3 4' } });
console.log(target.querySelector('svg').getAttribute('viewBox'), target.querySelector('rect').getAttribute('viewBox'));
EOF
../bin/envrun 'node repro.js; npx mocha --opts mocha.opts 2>&1 | tail -30'
```

tool result:

```
mkdir: /tmp/x: Operation not permitted
0 0 10 10 1 2 3 4
    [Symbol(SameObject caches)]: [Object: null prototype] {
      attributes: NamedNodeMap {},
      childNodes: NodeList {}
    },
    __value: 'two'
  },
  HTMLOptionElement {
    [Symbol(SameObject caches)]: [Object: null prototype] {
      attributes: NamedNodeMap {},
      childNodes: NodeList {}
    ...

should loosely deep-equal

HTMLOptionsCollection {}
      at Object.test (test/runtime/samples/binding-select/_config.js:22:10)
      at test/runtime/index.js:187:37

  8) runtime binding-select (shared helpers , hydration):
     Error: skipping test, already failed
      at Context.<anonymous> (test/runtime/index.js:58:11)
      at processImmediate (node:internal/timers:466:21)

  9) runtime binding-select (inline helpers):
     Error: skipping test, already failed
      at Context.<anonymous> (test/runtime/index.js:58:11)
      at processImmediate (node:internal/timers:466:21)
```

**assistant:** At runtime, both the static and dynamic `viewBox` are now set. There are some test failures; I'll compare them against a run without my change.

**tool call: Bash**

```bash
../bin/envrun 'npx mocha --opts mocha.opts 2>&1 | grep -E "passing|failing|pending|^  [0-9]+\)" > /testbed/after.txt; git stash -q; npm run build >/dev/null 2>&1; npx mocha --opts mocha.opts 2>&1 | grep -E "passing|failing|pending|^  [0-9]+\)" > /testbed/before.txt; git stash pop -q; npm run build >/dev/null 2>&1; diff before.txt after.txt && echo SAME; cat after.txt'
```

tool result:

```
SAME
  1548 passing (1m)
  53 pending
  9 failing
  1) custom-elements escaped-css:
  2) custom-elements html:
  3) custom-elements html-slots:
  4) custom-elements nested:
  5) custom-elements new:
  6) custom-elements new-styled:
  7) runtime binding-select (shared helpers):
  8) runtime binding-select (shared helpers , hydration):
  9) runtime binding-select (inline helpers):
```

**assistant:** The same 9 tests fail with and without my change (the custom-elements tests and `binding-select`, which look like environment problems), so the fix introduces no regressions. Cleaning up:

**tool call: Bash**

```bash
rm repro.js before.txt after.txt; git status --short
```

tool result:

```
 M package.json
 M src/generators/nodes/Attribute.ts
 M yarn.lock
?? Dockerfile
?? src/utils/fixAttributeCasing.ts
```

**assistant:** Svelte now accepts `viewbox` as well as `viewBox` on SVG elements. The compiled code sets the correctly cased attribute, so the browser respects it.

**Cause:** Inside SVG, Svelte creates elements with `createElementNS` and calls `setAttribute(svg, "viewbox", ...)`. Unlike the browser's HTML parser, `setAttribute` on SVG elements keeps the name exactly as written. SVG attribute names are case-sensitive, so `viewbox` was silently ignored. Server-side rendering wasn't affected, because there the browser's HTML parser fixes the case itself.

**Fix:**
- **`src/utils/fixAttributeCasing.ts`** (new): a lookup of the SVG attributes whose names mix upper and lower case (`viewBox`, `preserveAspectRatio`, `gradientUnits`, `stdDeviation`, etc.). It is based on the list the HTML parser itself corrects. Matching ignores case and returns the proper name. Anything not on the list, such as `data-Foo`, is left exactly as written.
- **`src/generators/nodes/Attribute.ts`**: when the element is in the SVG namespace, the attribute name goes through this lookup before code is generated. HTML elements and custom namespaces are unchanged.

**Checks:**
- **Reproduction:** before the fix, the generated code had `setAttribute(svg, "viewbox", ...)`; after it, `setAttribute(svg, "viewBox", ...)`. That holds for static and dynamic values, and `preserveaspectratio` is corrected the same way. In jsdom, `getAttribute('viewBox')` now returns the values for both. HTML attributes like `contenteditable` produce the same code as before.
- **Full test suite:** 1548 passing and 9 failing, with exactly the same failures with and without my change, so nothing new broke. The failures are the 6 custom-elements tests and `binding-select`, and they look like problems with the container rather than the code.

I deleted my reproduction script and temporary files. The changes to `package.json`, `yarn.lock` and the `Dockerfile` were already there before I started, and I didn't touch them.

_session end: success, turns 12, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 6.7 s: npm run build >/dev/null 2>&1; node repro.js
- `rc=0` 7.04 s: npm run build >/dev/null 2>&1; node repro.js
- `rc=0` 77.23 s: node repro.js; npx mocha --opts mocha.opts 2>&1 | tail -30
- `rc=0` 164.03 s: npx mocha --opts mocha.opts 2>&1 | grep -E "passing|failing|pending|^  [0-9]+\)" > /testbed/after.txt; git stash -q; npm run build >/dev/null 2>&1; npx mocha --opts mocha.opts 2>&1 | grep -E "passing|failing|pending|^  [0-9]+\)" > /testbed/before.txt; git stash pop -q; npm run build >/dev/null 2>&1; diff before.txt after.txt && echo SAME; cat after.txt
