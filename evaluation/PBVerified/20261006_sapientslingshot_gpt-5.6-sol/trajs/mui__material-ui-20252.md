# SWE-material-ui-20252 Trajectory

---

**Exported:** 2026-09-24T23:59:05.046Z

---

## SWE Benchmark Metadata

- **instanceId:** mui__material-ui-20252
- **repo:** mui/material-ui
- **baseCommit:** 5a794bd4974b02536b59d09029b12b4e76824301
- **taskIndex:** 28
- **status:** completed

---

## Execution Metrics
| Metric | Value |
|---|---:|
| Prompt tokens | 0 |
| Completion tokens | 0 |
| Total tokens | 3011760 |
| Credits consumed | 1.420662 |
| Total execution time | 2m 33s |

---

## Complete Raw Conversation

# Chat Session Export

**Exported:** 2026-09-24T23:59:05.043Z

## 👤 **User**

The current working directory is already provisioned by the benchmark host at exactly the task base commit, with one reachable commit and no Git remotes. Work only in this isolated local source tree.

Do not add Git remotes, clone, fetch, or pull. Do not access GitHub, GitHub APIs, upstream pull requests, commits, patches, or issue solutions. Do not use curl/wget or web-search tools. The benchmark runtime blocks outbound tools and commands.

Fix the issue using only the problem statement and the isolated local source tree. Generate mui__material-ui-20252.patch from the git diff,verify that git diff mui__material-ui-20252.patch contains only implementation or production files and no test files or test artifacts and then place it at this exact path: /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-20252.patch.

Repository: mui/material-ui
Base Commit: 5a794bd4974b02536b59d09029b12b4e76824301
Problem: [Tooltip] onFocus does not work on TextField if using a Tooltip with it
- [x] The issue is present in the latest release.
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Current Behavior 😯

`onFocus` does not work if using a `Tooltip` with `TextField`:
```

   {console.log("This cannot work!")}} />

```
This problem does not exist in Material-UI version ` The function works well.
3. Add a `Tooltip` to the `TextField` to show some hint for user.
   -> The `onFocus` function does not work any more.

## Context 🔦

I found this issue after I upgrade Material-UI to latest version. Now I have to use native `input` instead of `TextField` to avoid this problem.
Please correct me if I'm using the component wrongly. Thanks in advance!

Checked the source code, I think the problem is caused by this commit: https://github.com/mui-org/material-ui/commit/c98b9c47c5df2c94a72d5ce2b5169c1c53a1d842

## Your Environment 🌎

| Tech        | Version |
| ----------- | ------- |
| Material-UI | v4.9.4  |
| React       |  v16.13.0 |
| Browser     |    Chrome 80     |

---

## 🤖 **Slingshot**

*9/24/2026, 6:56:33 PM*

## Agent Execution Steps

1. **Tool call: register_tools**
Input:
```json
{
  "tool_names": [
    "get_agent_memory",
    "get_skill_details",
    "get_enriched_prompt",
    "get_workspace_files_list",
    "find_files",
    "grep",
    "read_file",
    "edit_file",
    "write_file",
    "run_terminal_command",
    "add_agent_memory"
  ],
  "toolPurpose": "- Load the workspace inspection, accessibility guidance, file editing, validation, patch generation, and session-memory tools needed to diagnose and fix the Tooltip/TextField focus regression entirely within the isolated repository."
}
```
Output:
```
Tools [get_agent_memory, get_skill_details, get_enriched_prompt, get_workspace_files_list, find_files, grep, read_file, edit_file, write_file, run_terminal_command, add_agent_memory] are now registered and immediately available for usage.
```

2. **Tool call: get_agent_memory**
Input:
```json
{
  "toolPurpose": "- I want to read previous agent summaries and persistent workspace conventions before inspecting or changing the repository, so I can avoid duplicate work and honor established project patterns."
}
```
Output:
```
Successfully read agent memory content:
Learnings from previous agent sessions: Successfully loaded 246 memory entries. Use these to inform your work and avoid creating duplicate memories when calling `add_agent_memory` tool.
Loaded memories:
* Gson JsonReader reports malformed Unicode escapes through syntaxError, yielding MalformedJsonException with line, column, and JSON path context.
* Gson Excluder handles anonymous/non-static local classes directionally: serialization delegates normally, while deserialization remains excluded.
* RocketMQ consumer lag, inflight, and available-message aggregates must iterate TopicConfig read queues to match consumer progress semantics.
* Dubbo's MulticastRegistry.java uses CRLF; validate its diffs with Git core.whitespace=cr-at-eol to avoid false trailing-whitespace failures.
* Gson tests on JDK 26 need -Pjdk15, release 8, ProGuard skipped, and ReflectionAccessTest excluded due removed SecurityManager support.
* Apollo namespace validation rejects URI-reserved names `.` and `..` while allowing ordinary dotted names.
* Gson production links to repository documentation should use the `main` branch in GitHub blob URLs.
* Gson ISO8601Utils uses a separate date-only GregorianCalendar path; it must disable leniency just like the date-time path to reject impossible dates.
* Apollo Portal password fragments are configured by apollo.portal.auth.password-checker.commonly-used-passwords-file and re-read on each check.
* Gson JsonWriter.name must immediately reject calls outside EMPTY_OBJECT or NONEMPTY_OBJECT with IllegalStateException("Nesting problem.").
* Dubbo RpcUtils priority is method-specific invocation attachment, generic attachment, URL method config, then URL global config.
* Gson ConstructorConstructor special-cases EnumMap, constructing it from a parameterized Class key and rejecting invalid raw/non-Class key types.
* Gson's unsafe opt-out API is disableJdkUnsafe(); its state must survive Gson.newBuilder() and fail lazily with JsonIOException when no constructor exists.
* Gson's JsonAdapter annotation factory must precede collection and map factories so unregistered annotation factories can obtain those delegates.
* Gson Streams.AppendableWriter.CurrentWrite must override toString() to return its full backing char array for CharSequence-compliant Appendables.
* Gson FormattingStyle separator spacing uses withSpaceAfterSeparators(boolean) and usesSpaceAfterSeparators(); commas are spaced only when newline is empty.
* Dubbo ClassHelper.convertPrimitive returns null for null or empty string input before primitive parsing.
* Gson Maven on JDK 26 fails -Werror on $Gson$Types dangling doc comments; direct javac --release 8 can validate production compilation locally.
* Gson serializes LazilyParsedNumber via an exact built-in adapter registered before reflective fallback, preserving its numeric lexeme.
* Guava concurrency production changes often require mirrored edits in guava/src and android/guava/src.
* Gson JsonObject backs members with LinkedTreeMap configured to reject Java null values, including through Map.Entry.setValue.
* Gson ProtoTypeAdapter supports opt-in explicit protobuf json_name via setShouldUseJsonNameFieldOption; custom serialized-name extensions take precedence.
* Apollo Portal forbids creating a private AppNamespace when the same name is already a globally public AppNamespace.
* Gson primitive numeric adapters must call the matching Number conversion method before serialization, including float/double and long-string policy wrappers.
* Dubbo compatibility tests on JDK 26 need JaCoCo skipped and java.lang opened; full tests may still fail when sandbox socket binding is denied.
* RocketMQ broker send ingress must strip PROPERTY_POP_CK so forwarded POP messages receive a fresh destination-broker receipt handle.
* Guava TopKSelector's trim fallback sorts an inclusive [left, right] range, so Arrays.sort must receive right + 1 as its exclusive bound.
* Gson DefaultDateTypeAdapter must restore each cached DateFormat timezone in a finally block after every parse attempt.
* Dubbo MockInvoker caches must include the service interface in the key; shorthand mock values like true/default are shared across references.
* At Gson base fe30b85, Gson.newJsonWriter must call setHtmlSafe(htmlSafe) so adapter-driven integrations inherit default or disabled HTML escaping.
* Gson's Troubleshooting.md uses CRLF; run Git whitespace checks with core.whitespace=cr-at-eol.
* Apollo Portal local user administration uses a super-admin /users/admin endpoint and UserInfo.enabled; edits preserve blank passwords and persist enabled status.
* RocketMQ POP retry topic v2 uses `%RETRY%group+topic`; `+` is forbidden in topic/group names, while v1 uses `_`.
* Dubbo CompatibleTypeUtils parses LocalDateTime as yyyy-MM-dd HH:mm:ss, LocalDate as yyyy-MM-dd, and LocalTime as HH:mm:ss.
* Dubbo Bytes char[] Base64 decoding must decrement full quartets and set remainder to 2/3 when the final quartet contains padding.
* Dubbo Triple Connection must assign the successful ChannelFuture channel in ConnectionListener before immediate availability checks.
* This Dubbo base contains multiple CRLF Java files; use git -c core.whitespace=cr-at-eol diff --check for rename-only patches.
* RocketMQ TieredFlatFile LOWER time lookup selects earliest segment with maxTimestamp >= target; UPPER selects latest with minTimestamp  instances, from shadowing it.
* Three.js Quaternion and Euler rotation-matrix conversion uses a 3-column stride for Matrix3 and 4-column stride for Matrix4 column-major elements.
* Svelte 1.17 static each-else teardown must set the destroyed else block reference to null so later empty states recreate it.
* Svelte v1 input value generation may tolerate dynamic type attributes, while binding semantics still require a compile-time static input type.
* At Svelte 1.14.1 base ec543cf, missing expected data properties are emitted by src/generators/dom/index.js as dev-only generated constructor diagnostics.
* Svelte v1 CSS attribute-presence selectors must return true once the attribute exists, before looking up a matcher operator.
* Svelte v1 component binding observers in keyed each blocks must reconstruct used contextual values from the child component's current _context before setting parent state.
* Svelte 1.27 CSS preprocessing is centralized in Stylesheet.apply for both DOM and SSR native elements, before selector matching and code generation.
* Svelte v1 Generator.parseJs must preserve node.async when lifting function expressions and arrow functions into named declarations.
* RocketMQ QueueOffsetAssigner uses get-before-computeIfAbsent fast paths to avoid Java 8 JDK-8161372 contention for established queue keys.
* Dubbo AbstractConfig metadata must prefer getX over duplicate isX accessors because Class.getMethods order is unspecified.
* Trino AddLocalExchanges should propagate parent stream preferences through identity projects to avoid redundant local repartition/gather exchanges around pruning.
* This benchmark workspace has no locally installed Java runtime, so Maven tests cannot run.
* In this Trino base, ProjectNode.isIdentity also identifies symbol-preserving pruning because Assignments checks only retained output assignments.
* Svelte v1 SSR must initialize a component-defined store inside `_render`, because nested components bypass the public `render` wrapper.
* Svelte v1 event handlers must serialize await contexts directly; each contexts instead serialize list/index pairs for reconstruction.
* Svelte v1 SVG attribute casing warnings are implemented in src/validate/html/validateElement.ts and scoped to SVG elements, descendants, and SVG namespace builds.
* Svelte v1 oncreate callbacks use unshift registration with LIFO callAll draining to preserve component/template preorder.
* Svelte v1 CSS scoping must merge the generated scope class into static and dynamic class values across DOM, innerHTML, and SSR output.
* Svelte v1 await then/catch context aliases must use Block.getUniqueName so names like children cannot shadow hydration helpers.
* Svelte v1 static innerHTML attribute serialization must join all text chunks so appended scoped CSS classes are not dropped on nested elements.
* Svelte v1 CSS DCE must treat Spread attributes as potential sources of any missing class, ID, or attribute during selector matching.
* Svelte v2 custom DOM event handlers must rewrite a direct `this.method()` callee to the associated element variable; native events retain runtime `this` binding.
* Svelte v3 alpha native element binding handlers emitted in component.partly_hoisted must use component.getUniqueName, not block.getUniqueName.
* Svelte v3 alpha rewrite_props must add a semicolon when exported prop declarations rely on ASI, while preserving an existing declaration semicolon.
* Svelte assignment instrumentation must ignore member roots that are not Identifiers; ThisExpression roots otherwise emit $$invalidate('undefined', undefined).
* Svelte v3 file-input bindings should listen to `change`, not `input`, because Safari does not reliably emit `input` when files are selected.
* Svelte v3 Expression.render must prefix hoisted object-method replacements with `: ` when the parent Property has method=true.
* Svelte v3 SSR inline-component attributes must use quote_name_if_necessary in both direct props and Object.assign spread fragments.
* Svelte mutation tracking must classify UpdateExpression member targets as mutated, not reassigned, in scripts and inline template functions.
* Svelte v3 Element namespace inference must stop at InlineComponent boundaries so slotted SVG tags do not inherit an outer HTML element namespace.
* Svelte inline !important styles are compiled by stripping the priority token and passing true as set_style's optional fourth argument.
* Svelte DebugTag DOM generation must omit its update block when expression dependencies are empty, or it emits invalid `if ()` code.
* Svelte v3 reassigned function declarations must remain unhoisted and count as dynamic reactive dependencies via Var.reassigned.
* In Svelte 3.9.1, reactive extraction and DOM dirty-check filtering must both include reassigned bindings; reassigned functions must not be hoisted.
* At Svelte base 64c56edd, reassigned function declarations must not hoist and must be included in reactive dependency and DOM dirty filters.
* Svelte v3 outro-capable compound if blocks must avoid changed([]); cached call conditions without dependencies use only a null initialization guard.
* Svelte 3.14 add_resize_listener creates an object resize sensor; set aria-hidden=true so this implementation detail is excluded from the accessibility tree.
* Svelte hydration must iterate a live NamedNodeMap backwards when removing unexpected attributes, or forward deletion skips alternating entries.
* Svelte CSS matching must distinguish unknown dynamic attributes from definite matches so leading :global descendants are not spuriously scoped.
* Svelte 3 keyed each updates must reassign the outer each_block_value so {:else} observes the current list length.
* Svelte v3 dev unknown-prop allowlists must include all instance exports, not only writable exports, because exported functions participate in component bindings.
* Svelte store-first destructuring must pass tail invalidations as extra set_store_value arguments so all store setters are evaluated while preserving the assignment result.
* Svelte await outros must clear info.blocks[i] only if the slot still references the outgoing block, so delayed callbacks cannot erase newer branches.
* Svelte v3 actions are repeatable directives; parser uniqueness checks exempt both EventHandler and Action while retaining other directive checks.
* Svelte 3 slot spreads require ordered Object.assign slot data and a wildcard dirty flag so arbitrary added, changed, or removed slot props update consumers.
* Svelte v3 SSR bound attributes must use boolean_attributes metadata; hard-coding boolean=true causes bind:value={0} to be omitted.
* Svelte hydratable builds map append, insert, and HtmlTag to hydration-specific helpers so plain bundles tree-shake hydration reordering.
* Svelte slot revival after an outro must pass an all-dirty mask to slot helpers; overflow contexts need one -1 per 31-member group.
* Svelte 3 await shorthand supports omitted resolve context by closing `then` with `}`, leaving the parsed await value null while activating the then branch.
* Svelte component initialization must prefer explicit options.context over ambient parent context, while cloning the selected map.
* Svelte text-like input update guards must include type=search in Attribute, Binding, and spread-attribute Element compiler paths.
* Prettier HTML embedded parsing depends on isScriptLikeTag; SVG script elements use fullName "svg:script" and must be included alongside "svg:style".
* Svelte 3 KeyBlock DOM wrappers must register key expression dependencies on the containing Block so slot-owned keyed fragments receive dirty updates.
* Prettier's TypeScript TSEnumMember printer must wrap `id` with brackets when `node.computed` is true.
* Prettier CLI directory globs must reuse an existing trailing slash; adding another slash causes fast-glob to return no supported files.
* Prettier SCSS @use/@forward `with (` spacing is handled in the value-comma_group branch of src/language-css/printer-postcss.js.
* Prettier ignored-node printing preserves relative indentation by comparing the node's leading whitespace with its nearest leading comment.
* Prettier ignored-node raw printing must mark only comments within the node range; file-wide prettier-ignore exemptions hide unrelated dropped comments.
* Prettier nested TSParenthesizedType keeps one pair in TSConditionalType check/extends and TSIndexedAccessType object positions.
* Prettier babel-ts must rethrow selected Babel recovered errors inside tryCombinations so invalid AST nodes do not reach the printer and fallback still runs.
* Prettier Markdown footnote definitions must flatten the initial paragraph with removeLines so long content remains attached to the `[^id]:` marker.
* Prettier config resolves string plugins and pluginSearchDirs relative to the discovered config file, including selected override options.
* Prettier's PostCSS root printer must return an empty string when css-root.nodes is empty; hardline is only for non-empty CSS/SCSS/Less roots.
* Prettier base 69f6ee7 is provisioned without node_modules; local CLI/tests fail on missing minimist unless dependencies are supplied.
* Prettier v1 CLI write status is emitted in src/cli-util.js formatFiles; silent loglevel must gate TTY progress, duration lines, and separators.
* Prettier 0.16 JSX opening tags keep `>` with the final prop by using an empty doc after non-self-closing attributes; self-closing tags retain `line` before `/>`.
* This Prettier 0.16 workspace lacks node_modules; full formatter and Jest tests are blocked by missing babel-code-frame and jest.
* Prettier 0.16 stabilizes standalone ternary boundary comments by attaching them as trailing comments to the preceding conditional child.
* Prettier v0.11 prints ClassProperty, ClassMethod, and MethodDefinition decorators with spaces; class decorators remain line-separated.
* Prettier 0.0.10 must print ExportDefaultSpecifier and ExportNamespaceSpecifier outside braces to preserve export-extension semantics.
* This Prettier workspace has no node_modules; Jest and formatter smoke tests are blocked by missing local dependencies.
* Serverless API Gateway custom request templates use null values to remove matching default content-type templates during compilation.
* Serverless v1.68 REST API http event properties pass through validation; AWS::ApiGateway::Method properties are built in apiGateway/lib/method/index.js.
* Serverless `.serverlessrc` may be symlinked; file detection must follow valid symlinks to avoid recreating the config and resetting tracking preferences.
* This Serverless workspace is provisioned without node_modules, so Mocha and ESLint quality gates cannot run locally.
* Serverless AWS info resource counts must paginate listStackResources via NextToken and accumulate StackResourceSummaries across all pages.
* SNS redrive queue policies need Fn::GetAtt for the queue ARN and Ref for the queue URL; the config may identify the queue by logical resource name.
* This Serverless benchmark tree has no installed npm dependencies, so unit tests and lint are blocked; Node syntax checks remain available.
* Serverless provisioned concurrency should live on a `provisioned` Lambda alias targeting the content-hashed version; API Gateway must invoke and permit that alias ARN.
* Serverless v1.54 IAM statements are validated in mergeIamTemplates.js and then concatenated unchanged into the generated execution-role policy.
* Serverless REST API logging treats exact SSM string "false" as disabled at stage compilation and post-deploy stage updates.
* Serverless CloudWatch Logs events need indexed Lambda permission IDs and each permission SourceArn scoped to its event's exact log group.
* Serverless IAM logging adds the service-stage wildcard only when a resolved function name uses that canonical prefix; manual-only services get exact log ARNs.
* Serverless AWS package cleanup must not spawn aws:common:validate; deploy's before:deploy:deploy hook retains credential validation.
* Serverless service plugins beginning with ./ or ../ resolve from serverless.config.servicePath; package names retain normal Node resolution.
* Serverless SNS existing-topic subscriptions derive CloudFormation Region from literal topic ARN segment 3; dynamic ARN intrinsics leave Region unset.
* Serverless v1.38 Lambda function compilation maps function-level `tracing` to CloudFormation `TracingConfig.Mode`.
* Serverless variable fallback cleaning must recognize both single- and double-quoted literals so embedded spaces are preserved.
* Serverless v1.39 default variableSyntax is synchronized across Service.js, print.js, and Utils.js telemetry comparison.
* Serverless v1.37 SSM variable resolution should parse valid JSON values while preserving non-JSON parameter values as strings.
* Serverless v1.34 Variables.cleanVariable removes whitespace outside quotes but preserves whitespace inside single- or double-quoted fallback literals.
* Serverless v1.21 maps top-level `deploy` plus `-f` or `--function` to the existing `deploy function` lifecycle in CLI.processInput.
* Serverless Cognito user pools must depend on invoke permissions; permissions use SourceAccount to avoid a circular dependency on the pool ARN.
* Serverless v1.15 supports SSE deployment buckets by normalizing object config and forwarding S3 PutObject encryption fields; KMS requires signature v4.
* Serverless stream event mappings must depend on custom IAM role logical IDs, not the absent generated IamRoleLambdaExecution resource.
* Serverless v1.12 API Gateway HTTP proxies use `integration: http-proxy` with a non-empty `request.uri`, compiled as CloudFormation `HTTP_PROXY`.
* Serverless API Gateway authorizer claim fragments must use join('') because implicit array coercion inserts extra commas into mapping templates.
* Serverless v1.3 deployment validation warnings are emitted through this.serverless.cli.log from compiler modules.
* Serverless v1 stream IAM permissions should group all event-source ARNs by DynamoDB/Kinesis into one policy statement per type.
* Serverless monitorStack must guard null stackStatus before suffix checks because an event page may contain no in-range AWS::CloudFormation::Stack event.
* Serverless v1.2 custom Resources may be an array of maps; entries merge left-to-right before merging into the compiled CloudFormation template.
* Serverless v1.1 function event validation must allow whole-property unresolved variables while still rejecting direct non-array event values.
* Serverless same-path API Gateway CORS aggregation unions methods, origins, and headers before generating one OPTIONS response.
* Serverless create --name explicitly overrides the generated service name; when absent, --path basename remains the naming fallback.
* VS Code snippet placeholder transforms use replace semantics so adjacent inactive tab-stop decorations honor edge stickiness and do not absorb transformed text.
* This VS Code benchmark tree has no node_modules; focused Mocha tests and Gulp compilation are unavailable without dependencies.
* VS Code language-specific configurationDefaults must shallow-merge by override key so later extensions do not erase built-in editor defaults.
* This VS Code benchmark tree has no node_modules or local tsc/eslint, so offline build, lint, and unit tests are unavailable.
* This VS Code benchmark tree has no node_modules or global tsc, so Mocha, lint, and TypeScript compilation cannot run locally.
* VS Code multi-word completions must preserve normalized edit ranges when providers are retriggered after a space.
* VS Code fuzzy completion highlighting treats '
  More info

```

### Clickable Tooltip (Icon Button)

```html

  i

```

### Focusable Tooltip (Input Field)

```html
Field Label

```

## JavaScript Implementation

The tooltip script handles:

1. **Initialization**: Create tooltip DOM element with proper ARIA attributes
2. **Event listeners**: Click, hover, focus, blur, keyboard events
3. **Show/hide logic**: Display tooltip with proper positioning
4. **Keyboard support**: Tab tracking and Escape key dismissal
5. **Viewport detection**: Reposition if tooltip overflows viewport
6. **ARIA management**: Dynamic `aria-describedby` connections

### Core Methods

- `init()`: Set up event listeners and create tooltip element
- `create()`: Build tooltip DOM with `role="tooltip"` and `aria-live="assertive"`
- `show(e)`: Display tooltip, position it, connect via `aria-describedby`
- `hide(e)`: Remove tooltip, clean up ARIA attributes
- `onKeyup(e)`: Handle Escape key to dismiss tooltip

### Key Features

**Tab tracking**: Distinguish between mouse and keyboard navigation to prevent tooltips from appearing unexpectedly when tabbing through buttons.

**Viewport awareness**: If tooltip extends beyond viewport, automatically reposition it (flip from top to bottom or vice versa).

**ARIA live region**: Tooltip has `aria-live="assertive"` so content is announced to screen readers when shown.

**Dynamic aria-describedby**: For INPUT elements, dynamically add/remove `aria-describedby="tooltip"` to ensure screen readers announce the tooltip content on focus.

## CSS Styling Guidelines

### Functional Styling (Required)

Provide minimal CSS for functionality:

```css
.tooltip {
  position: absolute;
  z-index: 2147483647; /* Maximum z-index */
  
  /* High Contrast Mode support */
  border: 1px solid transparent;
}

/* Visually hide when not shown */
.tooltip--hidden {
  clip: rect(1px, 1px, 1px, 1px);
  clip-path: inset(50%);
  height: 1px;
  overflow: hidden;
  position: absolute;
  white-space: nowrap;
  width: 1px;
  margin: -1px;
}

/* Arrow positioning */
.tooltip::before {
  content: "";
  position: absolute;
  /* High Contrast Mode support */
  border-top: 1px solid transparent;
  border-left: 1px solid transparent;
}

.tooltip--top::before {
  top: -0.5rem;
  transform: rotate(45deg);
}

.tooltip--bottom::before {
  bottom: -0.5rem;
  transform: rotate(-135deg);
}
```

### User Customization

Allow users to customize:
- Colors (background, text, border)
- Typography (font-family, font-size, line-height)
- Spacing (padding, margin)
- Border radius
- Arrow size and style
- Max-width
- Animations/transitions

Provide placeholder CSS variables or comments indicating customization points:

```css
.tooltip {
  /* Customize these properties */
  background: black; /* Change tooltip background */
  color: white;      /* Change text color */
  padding: 0.5rem;   /* Adjust padding */
  max-width: 20rem;  /* Adjust max width */
  border-radius: 0.5rem; /* Adjust corner radius */
}
```

## Accessibility Requirements (WCAG 2.2 Level AA)

### Keyboard Support
- ✅ Tooltip appears on focus of trigger element
- ✅ Tooltip dismisses with Escape key
- ✅ Tooltip dismisses on blur
- ✅ Tab key moves focus (doesn't get trapped)

### Screen Reader Support
- ✅ `role="tooltip"` identifies the element
- ✅ `aria-live="assertive"` announces content changes
- ✅ `aria-describedby` connects tooltip to trigger
- ✅ Tooltip content is meaningful and concise

### Visual Requirements
- ✅ High contrast mode support (transparent borders)
- ✅ Visible focus indicators on trigger elements
- ✅ Tooltip doesn't obscure critical content
- ✅ Repositions if it overflows viewport

### Touch Support
- ✅ Clickable tooltips work on touch devices
- ✅ Adequate touch target size (minimum 44×44px for buttons)

## Why Not Use Native `title` Attribute?

Avoid the native HTML `title` attribute for tooltips because:

- ❌ Only works for mouse users (not keyboard)
- ❌ Cannot be styled with CSS
- ❌ Has uncontrollable delay before appearing
- ❌ Inherits z-index (can be obscured)
- ❌ Not consistently announced by screen readers

**Exception**: `title` is still appropriate for:
- Expanding abbreviations with `` tag
- Providing titles to iframes (not for tooltip functionality)

## Code Generation Workflow

When generating tooltip code:

1. **Understand the context**: What type of tooltip is needed? (clickable button, icon, or focusable input)

2. **Generate HTML**: Use appropriate markup pattern with `data-tooltip` attribute

3. **Include JavaScript**: Provide the complete tooltip.js module from references (or simplified version)

4. **Provide functional CSS**: Include required styles for positioning, hiding, and high contrast mode

5. **Add customization guidance**: Comment CSS to show what users can safely customize

6. **Include initialization**: Show how to call `tooltip.init()` when DOM is ready

7. **Explain ARIA**: Document why each ARIA attribute is used

## Testing Checklist

Ensure generated tooltips meet these criteria:

- [ ] Tooltip appears on hover (mouse users)
- [ ] Tooltip appears on focus (keyboard users)
- [ ] Tooltip dismisses with Escape key
- [ ] Tooltip repositions if it overflows viewport
- [ ] Screen reader announces tooltip content
- [ ] High contrast mode shows tooltip clearly
- [ ] Touch/click works on mobile devices
- [ ] Focus indicators are visible
- [ ] No JavaScript errors in console

## Reference Implementation

For complete reference code, see:
- `references/tooltip.js` - Full JavaScript implementation
- `references/tooltip.css` - Complete CSS with functional and example styling

These files contain the proven Enable project implementation that can be adapted or used directly.

## Common Pitfalls to Avoid

❌ **Don't** put interactive elements inside tooltips (use popovers instead)

❌ **Don't** use tooltips for critical information (should be visible by default)

❌ **Don't** forget the Escape key handler

❌ **Don't** use fixed positioning without viewport detection

❌ **Don't** forget transparent borders (breaks high contrast mode)

❌ **Don't** use `title` attribute when custom styling is needed

✅ **Do** keep tooltip content concise and text-only

✅ **Do** ensure tooltips are supplemental, not essential

✅ **Do** test with keyboard, screen reader, and high contrast mode

✅ **Do** provide adequate touch targets for mobile

## Example Usage Scenarios

**Form field help**:
```html
VIN

  More info

```

**Icon button help**:
```html
Body style

  i

```

**Input with tooltip**:
```html
Termination date

```
```

4. **Tool call: get_enriched_prompt**
Input:
```json
{
  "programming_language": "javascript",
  "framework": "react",
  "platform": "",
  "toolPurpose": "I want to retrieve enriched React code-generation guidance so the Tooltip event-handler fix follows appropriate React composition, accessibility, maintainability, and testing best practices."
}
```
Output:
```

      **While we have below best practices, you must also enhance them based on your expertise**:
      - Use modern JavaScript (ES6+) features.
- Prefer functional programming principles where appropriate: favor pure functions, immutability, and avoid unnecessary side effects.
- Follow DRY (Don't Repeat Yourself), KISS (Keep It Simple), and YAGNI (You Aren't Gonna Need It) principles to maintain clarity and reduce complexity.
- Write modular, reusable, and testable code with single-responsibility functions and clear module boundaries.
- Implement comprehensive error handling using try/catch for both synchronous and asynchronous code; never silently ignore errors.
- Validate and sanitize all external inputs (e.g., user data, API payloads, URL parameters) to prevent runtime errors and security vulnerabilities like XSS or injection attacks.
- Never hardcode secrets or sensitive configuration—always use environment variables and ensure they are excluded from version control.
- Prevent memory leaks by cleaning up event listeners, timers (setTimeout/setInterval), DOM references, and framework-specific resources (e.g., useEffect cleanup in React).
- Use proper asynchronous patterns: prefer async/await over callbacks, always handle promise rejections, and avoid unhandled 'fire-and-forget' promises.
- Apply design patterns (e.g., Observer, Factory, Module) only when they solve a real problem—avoid over-engineering.
- Ensure compatibility across target environments (browsers or Node.js versions); use transpilation or polyfills if necessary.
- Write self-documenting code with clear naming conventions; supplement with JSDoc comments for public APIs or complex logic.
- Enforce consistent code style and formatting using tools like Prettier and ESLint (e.g., Airbnb or StandardJS conventions).
- Avoid polluting the global scope—encapsulate state within modules or classes.
- Optimize performance thoughtfully: avoid redundant computations, debounce/throttle expensive operations, and profile bottlenecks when needed.
- Adopt security-by-default practices: use HTTPS, set secure HTTP headers (e.g., CSP), validate CORS origins, and follow OWASP guidelines.
- Include structured logging for observability in production, but never log sensitive data like passwords, tokens, or PII.
- Ensure all interactive UI elements built with JavaScript are accessible: support keyboard navigation, focus management, ARIA roles/states, and screen reader announcements where needed.
- Design code to be testable: minimize side effects, use dependency injection where practical, and structure logic to support unit/integration tests.
- Favor component composition over inheritance; build small, focused, single-responsibility components.
- Minimize component re-renders by memoizing props with React.memo, useMemo, and useCallback where performance bottlenecks exist.
- Derive UI state from minimal source of truth; avoid duplicating or mirroring state unnecessarily.
- Clean up side effects properly in useEffect: return cleanup functions for subscriptions, timers, or event listeners to prevent memory leaks.
- Validate and sanitize all dynamic content rendered in JSX to prevent XSS—never dangerously set innerHTML unless explicitly escaped/sanitized.
- Treat props as immutable; never mutate received props or state directly—always use state setters or reducer actions.
- Structure state logic outside components when complex or reusable (e.g., custom hooks), keeping components declarative and testable.
- Avoid prop drilling by lifting shared state to the nearest common ancestor or using a scalable state propagation strategy—but only when necessary.
- Use environment variables for configuration (API endpoints, feature flags) and never embed secrets or environment-specific values in source code.
- Handle loading, error, and empty states explicitly in UI to improve resilience and user experience.
- Ensure accessibility (a11y) by using semantic HTML, proper ARIA attributes, and keyboard navigability—even when using agnostic UI primitives.
- Write components that are testable in isolation: avoid tight coupling to global state, side effects, or external services without abstraction.
- Prevent unnecessary client-side data fetching or computation—fetch only required data at appropriate component levels.
- Secure client-side routing: validate route parameters and implement authorization checks before rendering protected views.
- Optimize bundle size by code-splitting routes and heavy components using React.lazy and Suspense.
- Avoid inline function or object definitions in render if they break referential equality and cause unwanted re-renders.
      
```

5. **Tool call: find_files**
Input:
```json
{
  "globPatterns": [
    "**/[tT][oO][oO][lL][tT][iI][pP].*",
    "**/trajs/angular__angular-37561.md"
  ],
  "toolPurpose": "- I want to locate the Tooltip implementation and the exact user-attached context file within the isolated workspace before reading source or making changes."
}
```
Output:
```
Below are the 16 files found for the specified glob patterns (**/[tT][oO][oO][lL][tT][iI][pP].*, **/trajs/angular__angular-37561.md):

mui__material-ui-15526/pages/api/tooltip.md
mui__material-ui-15526/pages/api/tooltip.js
mui__material-ui-20232/docs/pages/api-docs/tooltip.md
mui__material-ui-20232/docs/pages/api-docs/tooltip.js
mui__material-ui-15526/packages/material-ui/src/Tooltip/Tooltip.d.ts
mui__material-ui-15526/packages/material-ui/src/Tooltip/Tooltip.js
mui__material-ui-15526/packages/material-ui/src/Tooltip/Tooltip.test.js
mui__material-ui-20252/docs/pages/api-docs/tooltip.md
mui__material-ui-20252/docs/pages/api-docs/tooltip.js
mui__material-ui-20252/packages/material-ui/src/Tooltip/Tooltip.d.ts
mui__material-ui-20252/packages/material-ui/src/Tooltip/Tooltip.js
mui__material-ui-20252/packages/material-ui/src/Tooltip/Tooltip.test.js
mui__material-ui-20232/packages/material-ui/src/Tooltip/Tooltip.d.ts
mui__material-ui-20232/packages/material-ui/src/Tooltip/Tooltip.js
mui__material-ui-20232/packages/material-ui/src/Tooltip/Tooltip.test.js
trajs/angular__angular-37561.md

Multiple matches were found. Use the request_user_input tool to specify which file should be referred to for the use case you are trying to implement.

```

6. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git --no-pager status --short --branch",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git --no-pager log -1 --format=%H",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- I want to verify the isolated repository is clean and exactly at the specified base commit before making any implementation changes."
}
```
Output:
```
I ran all provided commands and below are the outcomes for each command with their status. Please analyze each output carefully and run the commands again for which you see errors to get their output by correcting the command and other parameters.

=== EXECUTION SUMMARY ===
Total Commands: 2
Number of Successful Commands: 2
Number of Failed Commands: 0
Number of Timed Out Commands: 0
========================

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 1 of 2                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk git --no-pager status --short --branch'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
## HEAD (no branch)

__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 2 of 2                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk git --no-pager log -1 --format=%H'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
5a794bd4974b02536b59d09029b12b4e76824301
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

```

7. **Tool call: read_file**
Input:
```json
{
  "fileNames": [
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252/packages/material-ui/src/Tooltip/Tooltip.js",
      "startLine": 1
    },
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252/packages/material-ui/src/Tooltip/Tooltip.test.js",
      "startLine": 1
    },
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252/package.json",
      "startLine": 1
    },
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252/trajs/angular__angular-37561.md",
      "startLine": 1,
      "endLine": 316239
    }
  ],
  "toolPurpose": "- I want to read the exact Tooltip implementation and tests, project scripts, and the full user-attached context range to establish the regression contract and identify the smallest production-only fix."
}
```

8. **Tool call: read_file**
Input:
```json
{
  "fileNames": [
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252/packages/material-ui/src/TextField/TextField.js",
      "startLine": 1
    },
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252/packages/material-ui/src/FormControl/FormControl.js",
      "startLine": 1
    },
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252/packages/material-ui/src/InputBase/InputBase.js",
      "startLine": 1
    }
  ],
  "toolPurpose": "- I want to trace how TextField forwards refs and focus handlers through FormControl and InputBase, so the Tooltip fix composes the original callback without re-triggering it from interactive tooltip events."
}
```

9. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk ls node_modules/.bin/mocha node_modules/.bin/eslint node_modules/.bin/prettier",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --check",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- I want to establish available local quality gates and reconfirm there are no pre-existing whitespace errors before applying the focused Tooltip implementation change."
}
```
Output:
```
I ran all provided commands and below are the outcomes for each command with their status. Please analyze each output carefully and run the commands again for which you see errors to get their output by correcting the command and other parameters.

=== EXECUTION SUMMARY ===
Total Commands: 2
Number of Successful Commands: 1
Number of Failed Commands: 1
Number of Timed Out Commands: 0
========================

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 1 of 2                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk ls node_modules/.bin/mocha node_modules/.bin/eslint node_modules/.bin/prettier'
Status: ERROR
─────────────────────────────────────────────────────────────────────────
Output:
Command failed with exit code 1.

--- Full Output ---
ls: node_modules/.bin/eslint: No such file or directory
ls: node_modules/.bin/mocha: No such file or directory
ls: node_modules/.bin/prettier: No such file or directory
__CMD_FINISHED__ 1
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 2 of 2                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --check'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

```

10. **Tool call: grep**
Input:
```json
{
  "pattern": "contains\\(document\\.activeElement\\)|document\\.activeElement.*contains|onFocus &&.*childNode",
  "searchPath": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252/packages",
  "glob": [
    "**/*.js"
  ],
  "context": 3,
  "outputMode": "matches",
  "headLimit": 100,
  "toolPurpose": "- I need to inspect existing repository conventions for composite-focus containment checks before implementing the Tooltip event forwarding condition."
}
```
Output:
```
{"success":true,"mode":"content","numFiles":3,"numLines":3,"pagination":{"offset":0,"limit":100,"returned":3,"total":3,"hasMore":false},"matches":[{"file":"material-ui/src/Tooltip/Tooltip.js","line":343,"content":"if (childrenProps.onFocus && event.currentTarget === childNode) {","contextBefore":[{"line":340,"content":"}"},{"line":341,"content":""},{"line":342,"content":"const childrenProps = children.props;"}],"contextAfter":[{"line":344,"content":"childrenProps.onFocus(event);"},{"line":345,"content":"}"},{"line":346,"content":"};"}],"matches":["onFocus && event.currentTarget === childNode"]},{"file":"material-ui/src/Slider/Slider.js","line":100,"content":"!sliderRef.current.contains(document.activeElement) ||","contextBefore":[{"line":97,"content":""},{"line":98,"content":"function focusThumb({ sliderRef, activeIndex, setActive }) {"},{"line":99,"content":"if ("}],"contextAfter":[{"line":101,"content":"Number(document.activeElement.getAttribute('data-index')) !== activeIndex"},{"line":102,"content":") {"},{"line":103,"content":"sliderRef.current.querySelector(`[data-index=\"${activeIndex}\"]`).focus();"}],"matches":["contains(document.activeElement)"]},{"file":"material-ui/src/Menu/Menu.test.js","line":171,"content":"assert.strictEqual(false, menuEl.contains(document.activeElement));","contextBefore":[{"line":168,"content":"assert.strictEqual(popover.props().open, true);"},{"line":169,"content":"const menuEl = document.querySelector('[data-mui-test=\"Menu\"]');"},{"line":170,"content":"assert.notStrictEqual(document.activeElement, menuEl);"}],"contextAfter":[{"line":172,"content":"});"},{"line":173,"content":""},{"line":174,"content":"it('should call props.onEntering with element if exists', () => {"}],"matches":["contains(document.activeElement)"]}]}
```

11. **Tool call: edit_file**
Input:
```json
{
  "operations": [
    {
      "filePath": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252/packages/material-ui/src/Tooltip/Tooltip.js",
      "originalContent": "  const handleFocus = (event) => {\n    // Workaround for https://github.com/facebook/react/issues/7769\n    // The autoFocus of React might trigger the event before the componentDidMount.\n    // We need to account for this eventuality.\n    if (!childNode) {\n      setChildNode(event.currentTarget);\n    }\n\n    if (isFocusVisible(event)) {\n      setChildIsFocusVisible(true);\n      handleEnter(event);\n    }\n\n    const childrenProps = children.props;\n    if (childrenProps.onFocus && event.currentTarget === childNode) {\n      childrenProps.onFocus(event);\n    }\n  };\n",
      "newContent": "  const handleFocus = (event) => {\n    // Workaround for https://github.com/facebook/react/issues/7769\n    // The autoFocus of React might trigger the event before the componentDidMount.\n    // We need to account for this eventuality.\n    if (!childNode) {\n      setChildNode(event.currentTarget);\n    }\n\n    if (isFocusVisible(event)) {\n      setChildIsFocusVisible(true);\n      handleEnter(event);\n    }\n\n    const childrenProps = children.props;\n    if (childrenProps.onFocus && childNode && childNode.contains(document.activeElement)) {\n      childrenProps.onFocus(event);\n    }\n  };\n"
    }
  ],
  "toolPurpose": "- I want to edit Tooltip focus forwarding so a composite child such as TextField receives its original onFocus callback when the focused native input is contained by the Tooltip child root, while excluding focus events originating from the tooltip itself.",
  "references": {
    "hasJiraContext": false,
    "hasFigmaContext": false
  }
}
```
Output:
```
Successfully replaced content in file Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252/packages/material-ui/src/Tooltip/Tooltip.js
```

12. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --check",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --stat",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --name-only",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git --no-pager diff",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- I want to inspect the complete implementation diff, verify whitespace, and confirm that only the intended production Tooltip source file changed before generating the requested patch artifact."
}
```
Output:
```
I ran all provided commands and below are the outcomes for each command with their status. Please analyze each output carefully and run the commands again for which you see errors to get their output by correcting the command and other parameters.

=== EXECUTION SUMMARY ===
Total Commands: 4
Number of Successful Commands: 4
Number of Failed Commands: 0
Number of Timed Out Commands: 0
========================

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 1 of 4                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --check'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 2 of 4                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --stat'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
packages/material-ui/src/Tooltip/Tooltip.js | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 3 of 4                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --name-only'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
packages/material-ui/src/Tooltip/Tooltip.js

Changes:

__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 4 of 4                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk git --no-pager diff'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
packages/material-ui/src/Tooltip/Tooltip.js | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

Changes:

packages/material-ui/src/Tooltip/Tooltip.js
@@ -340,7 +340,7 @@ const Tooltip = React.forwardRef(function Tooltip(props, ref) {
     }
 
     const childrenProps = children.props;
-    if (childrenProps.onFocus && event.currentTarget === childNode) {
+    if (childrenProps.onFocus && childNode && childNode.contains(document.activeElement)) {
       childrenProps.onFocus(event);
     }
   };
  +1 -1
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

```

13. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --no-compact > /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-20252.patch",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252",
      "profileName": "zsh",
      "readTerminalFullOutput": false,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- I want to generate the requested `mui__material-ui-20252.patch` artifact from the complete uncompressed Git diff at the exact benchmark results path."
}
```
Output:
```
I ran all provided commands and below are the outcomes for each command with their status. Please analyze each output carefully and run the commands again for which you see errors to get their output by correcting the command and other parameters.

=== EXECUTION SUMMARY ===
Total Commands: 1
Number of Successful Commands: 1
Number of Failed Commands: 0
Number of Timed Out Commands: 0
========================

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 1 of 1                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --no-compact > /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-20252.patch'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Output (last 1 lines, 18 chars) ---
__CMD_FINISHED__ 0
--- End of Output ---
═════════════════════════════════════════════════════════════════════════

```

14. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git apply --check /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-20252.patch",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk grep -E \"^(diff --git|--- |\\+\\+\\+ )\" /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-20252.patch",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk grep -Ei \"(^diff --git .*(__tests__|test|spec|snapshot|fixture|artifact)|^(---|\\+\\+\\+) .*(__tests__|test|spec|snapshot|fixture|artifact))\" /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-20252.patch",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk ls -l /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-20252.patch",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- I want to validate that the generated patch applies cleanly, exists at the exact requested path, and contains only the intended production Tooltip source path with no test files or test artifacts."
}
```
Output:
```
I ran all provided commands and below are the outcomes for each command with their status. Please analyze each output carefully and run the commands again for which you see errors to get their output by correcting the command and other parameters.

=== EXECUTION SUMMARY ===
Total Commands: 4
Number of Successful Commands: 2
Number of Failed Commands: 2
Number of Timed Out Commands: 0
========================

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 1 of 4                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk git apply --check /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-20252.patch'
Status: ERROR
─────────────────────────────────────────────────────────────────────────
Output:
Command failed with exit code 1.

--- Full Output ---
error: patch failed: packages/material-ui/src/Tooltip/Tooltip.js:340
error: packages/material-ui/src/Tooltip/Tooltip.js: patch does not apply
__CMD_FINISHED__ 1
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 2 of 4                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk grep -E "^(diff --git|--- |\+\+\+ )" /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-20252.patch'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
diff --git a/packages/material-ui/src/Tooltip/Tooltip.js b/packages/material-ui/src/Tooltip/Tooltip.js
--- a/packages/material-ui/src/Tooltip/Tooltip.js
+++ b/packages/material-ui/src/Tooltip/Tooltip.js
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 3 of 4                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk grep -Ei "(^diff --git .*(__tests__|test|spec|snapshot|fixture|artifact)|^(---|\+\+\+) .*(__tests__|test|spec|snapshot|fixture|artifact))" /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-20252.patch'
Status: ERROR
─────────────────────────────────────────────────────────────────────────
Output:
Command failed with exit code 1.

--- Full Output ---
__CMD_FINISHED__ 1
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 4 of 4                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk ls -l /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-20252.patch'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
644  /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-20252.patch  583B
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

```

15. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git apply --check --reverse /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-20252.patch",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git --no-pager status --short",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk cat /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-20252.patch",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-20252",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- I want to perform final validation against the currently modified tree: confirm the patch reverses cleanly, inspect its complete content, and verify the repository contains only the intended production source modification."
}
```
Output:
```
I ran all provided commands and below are the outcomes for each command with their status. Please analyze each output carefully and run the commands again for which you see errors to get their output by correcting the command and other parameters.

=== EXECUTION SUMMARY ===
Total Commands: 3
Number of Successful Commands: 3
Number of Failed Commands: 0
Number of Timed Out Commands: 0
========================

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 1 of 3                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk git apply --check --reverse /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-20252.patch'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 2 of 3                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk git --no-pager status --short'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
M packages/material-ui/src/Tooltip/Tooltip.js__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 3 of 3                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk cat /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-20252.patch'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
diff --git a/packages/material-ui/src/Tooltip/Tooltip.js b/packages/material-ui/src/Tooltip/Tooltip.js
index 1d81541..90f7637 100644
--- a/packages/material-ui/src/Tooltip/Tooltip.js
+++ b/packages/material-ui/src/Tooltip/Tooltip.js
@@ -340,7 +340,7 @@ const Tooltip = React.forwardRef(function Tooltip(props, ref) {
     }
 
     const childrenProps = children.props;
-    if (childrenProps.onFocus && event.currentTarget === childNode) {
+    if (childrenProps.onFocus && childNode && childNode.contains(document.activeElement)) {
       childrenProps.onFocus(event);
     }
   };
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

```

16. **Tool call: add_agent_memory**
Input:
```json
{
  "memories": [
    {
      "content": "MUI 4.9.6 Tooltip forwards composite-child focus when its root contains document.activeElement, allowing TextField onFocus handlers to run.",
      "scope": "workspace"
    }
  ],
  "toolPurpose": "- Save the project-specific Tooltip composite-focus contract so future work in this Material-UI checkout preserves the TextField event-forwarding behavior."
}
```
Output:
```
Processed 1 memory item(s): 1 stored, 0 skipped (duplicates), 0 failed.
```

## Final Response

## Fix

Updated Tooltip focus handling so composite children such as `TextField` correctly receive their `onFocus` callback when focus is inside the child root.

## 📝 Files Modified

- [Tooltip.js](packages/material-ui/src/Tooltip/Tooltip.js) - Uses focus containment when forwarding `onFocus`. **+1 −1 lines**

## Patch

Created:

`/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-20252.patch`

Validation:

- Patch reverses cleanly against the modified tree.
- Diff whitespace check passed.
- Patch contains only [Tooltip.js](packages/material-ui/src/Tooltip/Tooltip.js).
- No tests, snapshots, fixtures, or test artifacts are included.
- Automated tests and lint could not run because local dependencies and executables are not installed.

---
