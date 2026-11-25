# SWE-material-ui-26170 Trajectory

---

**Exported:** 2026-09-25T14:03:54.807Z

---

## SWE Benchmark Metadata

- **instanceId:** mui__material-ui-26170
- **repo:** mui/material-ui
- **baseCommit:** 215794b567669951a61183d748c0b2be6483c3ea
- **taskIndex:** 9
- **status:** completed

---

## Execution Metrics
| Metric | Value |
|---|---:|
| Prompt tokens | 0 |
| Completion tokens | 0 |
| Total tokens | 424920 |
| Credits consumed | 0.325309 |
| Total execution time | 2m 33s |

---

## Complete Raw Conversation

# Chat Session Export

**Exported:** 2026-09-25T14:03:54.805Z

## 👤 **User**

The current working directory is already provisioned by the benchmark host at exactly the task base commit, with one reachable commit and no Git remotes. Work only in this isolated local source tree.

Do not add Git remotes, clone, fetch, or pull. Do not access GitHub, GitHub APIs, upstream pull requests, commits, patches, or issue solutions. Do not use curl/wget or web-search tools. The benchmark runtime blocks outbound tools and commands.

Fix the issue using only the problem statement and the isolated local source tree. Generate mui__material-ui-26170.patch from the git diff,verify that git diff mui__material-ui-26170.patch contains only implementation or production files and no test files or test artifacts and then place it at this exact path: /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-26170.patch.

Repository: mui/material-ui
Base Commit: 215794b567669951a61183d748c0b2be6483c3ea
Problem: [TabList] Conditional rendering of Tab fails

- [x] The issue is present in the latest release.
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Current Behavior 😯
As pointed on [Issue 8093](https://github.com/mui-org/material-ui/issues/8093), when we have a conditional rendering of a Tab, it throws an error.

## Expected Behavior 🤔
The expected behavior is not to consider a null as a valid component. This issue was resolved by [PR 8107](https://github.com/mui-org/material-ui/pull/8107), but for Tabs component.

## Steps to Reproduce 🕹

Just use a condition to render a Tab inside a TabList

[Live example on CodeSandbox](https://codesandbox.io/s/materialui-tablist-conditional-tab-bug-f4rqy)

Steps:

1. Render a TabList
2. Render some Tabs
3. Conditionaly render a Tab inside TabList

## Context 🔦

I was trying to render a Tab depending on a user state.

## Your Environment 🌎

  `npx @material-ui/envinfo`
  
```
  System:
    OS: Linux 5.4 Linux Mint 20.1 (Ulyssa)
  Binaries:
    Node: 14.16.0 - /usr/local/bin/node
    Yarn: 1.22.10 - /usr/local/bin/yarn
    npm: 6.14.13 - /usr/local/bin/npm
  Browsers:
    Chrome: 90.0.4430.93
    Firefox: 88.0.1
  npmPackages:
    @material-ui/core: ^4.11.3 => 4.11.3 
    @material-ui/icons: ^4.11.2 => 4.11.2 
    @material-ui/lab: ^4.0.0-alpha.57 => 4.0.0-alpha.57 
    @material-ui/pickers: ^3.3.10 => 3.3.10 
    @material-ui/styles: ^4.11.3 => 4.11.3 
    @material-ui/system:  4.11.3 
    @material-ui/types:  5.1.0 
    @material-ui/utils:  4.11.2 
    @types/react:  17.0.3 
    react: ^17.0.1 => 17.0.1 
    react-dom: ^17.0.1 => 17.0.1 
    styled-components:  5.2.1
```

---

## 🤖 **Slingshot**

*9/25/2026, 9:01:21 AM*

## Agent Execution Steps

1. **Tool call: register_tools**
Input:
```json
{
  "tool_names": [
    "get_skill_details",
    "get_agent_memory",
    "get_enriched_prompt",
    "read_file",
    "get_workspace_files_list",
    "grep",
    "run_terminal_command",
    "edit_file",
    "write_file",
    "add_agent_memory"
  ],
  "toolPurpose": "- I want to inspect the isolated repository and required environment context, load the accessible-tabs guidance and React coding guidance, implement the TabList production fix, validate it locally, generate the requested patch, and record concise session memory."
}
```
Output:
```
Tools [get_skill_details, get_agent_memory, get_enriched_prompt, read_file, get_workspace_files_list, grep, run_terminal_command, edit_file, write_file, add_agent_memory] are now registered and immediately available for usage.
```

2. **Tool call: get_agent_memory**
Input:
```json
{
  "toolPurpose": "- I want to read prior session and workspace memory before making changes so I can avoid duplicate work and respect established repository conventions."
}
```
Output:
```
Successfully read agent memory content:
Learnings from previous agent sessions: Successfully loaded 261 memory entries. Use these to inform your work and avoid creating duplicate memories when calling `add_agent_memory` tool.
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

```

- **`role="tablist"`**: Identifies the container as a tab list
- **`aria-label`** or **`aria-labelledby`**: Provides accessible name for the tablist

### Tab Buttons
```html

  Tab 1

```

- **`role="tab"`**: Identifies the button as a tab
- **`aria-selected="true"`**: Indicates the currently active tab (false for others)
- **`aria-controls`**: References the ID of the associated tabpanel
- **`id`**: Unique identifier for the tab
- **`tabindex="0"`**: Active tab is in tab order; inactive tabs have `tabindex="-1"`

### Tab Panels
```html

```

- **`role="tabpanel"`**: Identifies the container as a tab panel
- **`id`**: Unique identifier referenced by `aria-controls`
- **`aria-labelledby`**: References the ID of the associated tab
- **`tabindex="0"`**: Makes panel focusable for keyboard users
- **`hidden`** attribute: Hide inactive panels (or use CSS `display: none`)

## Keyboard Interaction

Implement these keyboard behaviors according to WCAG 2.2 and WAI-ARIA APG:

### When focus is on a tab:

- **Tab**: Moves focus to the active tab panel (or first focusable element within it)
- **Left Arrow**: Moves focus to the previous tab (wraps to last tab if on first)
- **Right Arrow**: Moves focus to the next tab (wraps to first tab if on last)
- **Home**: Moves focus to the first tab
- **End**: Moves focus to the last tab
- **Space** or **Enter**: Activates the focused tab (if not using automatic activation)

### Activation Patterns

There are two common patterns:

**1. Automatic Activation (Recommended)**
- Moving focus with arrow keys automatically activates the tab
- Simpler for users
- Preferred pattern in most cases

**2. Manual Activation**
- Arrow keys move focus but don't activate
- User must press Space or Enter to activate
- Use when tab panels are slow to load or contain forms

## HTML Markup Pattern

### Basic Structure

```html

      Section 1

      Section 2

      Section 3

    ## Section 1 Content

💭 **Agent Thoughts:**
> Content for the first tab panel.
>   
>   
>   
>     Section 2 Content
>     Content for the second tab panel.
>   
>   
>   
>     Section 3 Content
>     Content for the third tab panel.
>   
> 
> ```
> 
> ## JavaScript Implementation
> 
> The tabs script handles:
> 
> 1. **Initialization**: Set up event listeners and initial state
> 2. **Tab activation**: Show selected panel, hide others, update ARIA attributes
> 3. **Keyboard navigation**: Arrow keys, Home, End
> 4. **Roving tabindex**: Manage focus between tabs
> 5. **Automatic/manual activation**: Choose activation pattern
> 
> ### Core Methods
> 
> - `init()`: Initialize the tabs component, set up event listeners
> - `activateTab(tab, setFocus)`: Activate a tab, show its panel, update ARIA
> - `handleKeydown(e)`: Handle arrow keys, Home, End navigation
> - `focusNextTab()`: Move focus to next tab (with wrapping)
> - `focusPreviousTab()`: Move focus to previous tab (with wrapping)
> - `focusFirstTab()`: Move focus to first tab
> - `focusLastTab()`: Move focus to last tab
> 
> ### Key Features
> 
> **Roving tabindex**: Only the active tab has `tabindex="0"`, all others have `tabindex="-1"`. This ensures Tab key moves to the panel, not through all tabs.
> 
> **Arrow key wrapping**: When on the last tab, Right Arrow wraps to the first tab. When on the first tab, Left Arrow wraps to the last tab.
> 
> **Automatic activation**: When focus moves to a tab via arrow keys, automatically activate it (show its panel). This is the recommended pattern for most use cases.
> 
> **ARIA state management**: When activating a tab:
> - Set `aria-selected="true"` on active tab, `false` on others
> - Set `tabindex="0"` on active tab, `-1` on others
> - Remove `hidden` from active panel, add to others
> 
> ## CSS Styling Guidelines
> 
> ### Functional Styling (Required)
> 
> Provide minimal CSS for functionality:
> 
> ```css
> /* Hide inactive panels */
> [role="tabpanel"][hidden] {
>   display: none;
> }
> 
> /* Tablist layout */
> [role="tablist"] {
>   display: flex;
>   gap: 0;
>   border-bottom: 1px solid #ccc;
> }
> 
> /* Tab buttons */
> [role="tab"] {
>   background: transparent;
>   border: 1px solid transparent;
>   cursor: pointer;
>   position: relative;
> }
> 
> /* Active tab indicator */
> [role="tab"][aria-selected="true"] {
>   border-bottom-color: transparent;
> }
> 
> /* Focus indicator (required for accessibility) */
> [role="tab"]:focus {
>   outline: 2px solid #0066cc;
>   outline-offset: -2px;
>   z-index: 1;
> }
> 
> /* Tab panel */
> [role="tabpanel"] {
>   padding: 1rem;
> }
> 
> /* Focus indicator for panel */
> [role="tabpanel"]:focus {
>   outline: 2px solid #0066cc;
>   outline-offset: -2px;
> }
> ```
> 
> ### User Customization
> 
> Allow users to customize:
> - Colors (tab background, active tab, borders, text)
> - Typography (font-family, font-size, font-weight)
> - Spacing (padding, margin, gap between tabs)
> - Border styles (width, color, radius)
> - Active tab indicator style (underline, background, border)
> - Hover and focus states
> - Transitions and animations
> - Orientation (horizontal or vertical tabs)
> 
> Provide placeholder CSS comments indicating customization points:
> 
> ```css
> [role="tab"] {
>   /* Customize these properties */
>   background: #f5f5f5;     /* Tab background color */
>   color: #333;              /* Tab text color */
>   padding: 0.75rem 1.5rem; /* Tab padding */
>   border-radius: 0.25rem 0.25rem 0 0; /* Top corners rounded */
>   font-weight: 500;         /* Tab text weight */
> }
> 
> [role="tab"][aria-selected="true"] {
>   background: white;        /* Active tab background */
>   color: #0066cc;          /* Active tab text color */
>   border-color: #ccc;      /* Active tab border */
>   border-bottom-color: white; /* Hide bottom border */
> }
> 
> [role="tab"]:hover:not([aria-selected="true"]) {
>   background: #e8e8e8;     /* Hover background */
> }
> ```
> 
> ## Accessibility Requirements (WCAG 2.2 Level AA)
> 
> ### Keyboard Support
> - ✅ Tab key moves focus from tablist to active panel
> - ✅ Arrow keys navigate between tabs (Left/Right or Up/Down)
> - ✅ Home key moves to first tab
> - ✅ End key moves to last tab
> - ✅ Enter/Space activates tab (if using manual activation)
> - ✅ Focus doesn't get trapped in tablist
> 
> ### Screen Reader Support
> - ✅ `role="tablist"` identifies the tab container
> - ✅ `role="tab"` identifies each tab button
> - ✅ `role="tabpanel"` identifies each content panel
> - ✅ `aria-selected` indicates active tab
> - ✅ `aria-controls` links tabs to panels
> - ✅ `aria-labelledby` links panels to tabs
> - ✅ Tablist has accessible name via `aria-label` or `aria-labelledby`
> 
> ### Visual Requirements
> - ✅ Clear visual indicator of active tab
> - ✅ Visible focus indicators (2px minimum, 3:1 contrast ratio)
> - ✅ Sufficient color contrast (4.5:1 for text, 3:1 for UI components)
> - ✅ Active tab visually connected to its panel
> - ✅ Focus indicators not obscured by other elements
> 
> ### Focus Management
> - ✅ Roving tabindex pattern (only active tab in tab order)
> - ✅ Focus visible at all times
> - ✅ Logical focus order maintained
> - ✅ Tab panels are focusable (`tabindex="0"`)
> 
> ## Orientation: Horizontal vs Vertical
> 
> ### Horizontal Tabs (Default)
> - Tabs arranged left to right
> - Use Left/Right arrow keys for navigation
> - Most common pattern
> 
> ```html
> 
>   
> 
> ```
> 
> ### Vertical Tabs
> - Tabs arranged top to bottom
> - Use Up/Down arrow keys for navigation
> - Add `aria-orientation="vertical"` to tablist
> 
> ```html
> 
>   
> 
> ```
> 
> The JavaScript should detect `aria-orientation` and use appropriate arrow keys:
> - Horizontal: Left/Right arrows
> - Vertical: Up/Down arrows
> 
> ## Common Pitfalls to Avoid
> 
> ❌ **Don't** use `` tags for tabs (use `` elements)
> 
> ❌ **Don't** forget to implement arrow key navigation
> 
> ❌ **Don't** make all tabs `tabindex="0"` (use roving tabindex)
> 
> ❌ **Don't** forget to hide inactive panels (use `hidden` attribute or CSS)
> 
> ❌ **Don't** forget `aria-selected` on tabs
> 
> ❌ **Don't** forget to connect tabs and panels with `aria-controls` and `aria-labelledby`
> 
> ❌ **Don't** use tabs for navigation between pages (use regular links instead)
> 
> ❌ **Don't** nest interactive elements inside tab buttons
> 
> ✅ **Do** use semantic `` elements for tabs
> 
> ✅ **Do** implement complete keyboard navigation (arrows, Home, End)
> 
> ✅ **Do** use roving tabindex pattern
> 
> ✅ **Do** provide clear visual indicators for active and focused tabs
> 
> ✅ **Do** test with keyboard, screen reader, and zoom (up to 200%)
> 
> ✅ **Do** ensure sufficient color contrast
> 
> ✅ **Do** make tab panels focusable with `tabindex="0"`
> 
> ## Code Generation Workflow
> 
> When generating tabs code:
> 
> 1. **Understand the context**: How many tabs? What content? Horizontal or vertical?
> 
> 2. **Generate HTML**: Use proper ARIA roles and attributes, semantic `` elements
> 
> 3. **Include JavaScript**: Provide complete tabs.js module from references (or simplified version)
> 
> 4. **Provide functional CSS**: Include required styles for layout, hiding, and focus indicators
> 
> 5. **Add customization guidance**: Comment CSS to show what users can safely customize
> 
> 6. **Include initialization**: Show how to call `tabs.init()` when DOM is ready
> 
> 7. **Explain ARIA**: Document why each ARIA attribute is used and how they work together
> 
> 8. **Choose activation pattern**: Recommend automatic activation unless there's a specific reason for manual
> 
> ## Testing Checklist
> 
> Ensure generated tabs meet these criteria:
> 
> - [ ] Only one tab has `aria-selected="true"` at a time
> - [ ] Only one panel is visible at a time
> - [ ] Tab key moves from tablist to active panel
> - [ ] Arrow keys navigate between tabs
> - [ ] Home/End keys work correctly
> - [ ] Focus indicators are clearly visible
> - [ ] Screen reader announces tab roles and states
> - [ ] Active tab is visually distinct
> - [ ] Inactive panels are properly hidden
> - [ ] Color contrast meets WCAG AA standards (4.5:1 text, 3:1 UI)
> - [ ] Works at 200% zoom
> - [ ] No JavaScript errors in console
> 
> ## Reference Implementation
> 
> For complete reference code, see:
> - `references/tabs.js` - Full JavaScript implementation with automatic activation
> - `references/tabs.css` - Complete CSS with functional and example styling
> 
> These files contain a proven accessible implementation following WAI-ARIA APG patterns that can be adapted or used directly.
> 
> ## Example Usage Scenarios
> 
> **Content organization**:
> ```html
> 
>   
>     
>       Description
>     
>     
>       Specifications
>     
>     
>       Reviews
>     
>   
>   
>   
>     Product Description
>     Detailed product information...

    ## Technical Specifications

    - Spec 1
- Spec 2

    ## Customer Reviews

    Reviews content...

```

**Settings interface**:
```html

      General

      Privacy

      Notifications

```

## When NOT to Use Tabs

**Don't use tabs for:**
- Navigation between different pages (use regular navigation links)
- Sequential processes (use a stepper/wizard component instead)
- Comparing content side-by-side (tabs hide content)
- Very long content that requires scrolling (consider accordion or separate pages)

**Use tabs when:**
- Content is related but mutually exclusive
- Space is limited and you need to organize content
- Users need to switch between views frequently
- Content sections are roughly equal in importance
```

4. **Tool call: get_enriched_prompt**
Input:
```json
{
  "programming_language": "javascript",
  "framework": "react",
  "platform": "",
  "toolPurpose": "I want enriched React code-generation guidance so the TabList fix follows framework conventions, accessibility requirements, maintainability practices, and appropriate non-functional standards."
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

5. **Tool call: read_file**
Input:
```json
{
  "fileNames": [
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-26170/.env",
      "startLine": 1,
      "endLine": 51
    }
  ],
  "toolPurpose": "- I want to read the exact user-attached .env line range to capture all benchmark context required before analyzing or changing the repository."
}
```
Output:
```

File successfully read, file name .env with file path: enc_file_sovfhn/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-26170/docs/.env

**File Read Information:**
- Lines read: 1 to 1 (1 lines)

Content:
FEEDBACK_URL=https://hgvi836wi8.execute-api.us-east-1.amazonaws.com

```

6. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git --no-pager status --short --branch; /Users/sankanum1/.slingshot/bin/rtk git --no-pager rev-parse HEAD",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-26170",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- I want to verify the isolated repository is clean and at the exact requested base commit before making any implementation changes."
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
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk git --no-pager status --short --branch; /Users/sankanum1/.slingshot/bin/rtk git --no-pager rev-parse HEAD'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
## HEAD (no branch)

215794b567669951a61183d748c0b2be6483c3ea
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

```

7. **Tool call: grep**
Input:
```json
{
  "pattern": "function TabList|const TabList|class TabList|TabList",
  "searchPath": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-26170/packages",
  "glob": [
    "*.js"
  ],
  "outputMode": "files",
  "headLimit": 100,
  "toolPurpose": "- I need to locate the TabList implementation and nearby tests/usages in the isolated source tree without relying on external information."
}
```
Output:
```
{"success":true,"mode":"files","files":[{"file":"material-ui-lab/test/integration/Tabs.test.js","size":1457,"mtime":1790344881107},{"file":"material-ui-lab/src/TabList/TabList.test.js","size":1565,"mtime":1790344881091},{"file":"material-ui-lab/src/TabList/index.js","size":37,"mtime":1790344881091},{"file":"material-ui-lab/src/TabList/TabList.js","size":1274,"mtime":1790344881091},{"file":"material-ui-lab/src/index.js","size":4963,"mtime":1790344881101}],"numFiles":5,"pagination":{"offset":0,"limit":100,"returned":5,"total":5,"hasMore":false}}
```

8. **Tool call: grep**
Input:
```json
{
  "pattern": "React\\.Children\\.(map|forEach)|Children\\.(map|forEach)",
  "searchPath": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-26170/packages/material-ui",
  "glob": [
    "*Tabs*.js",
    "*TabList*.js"
  ],
  "context": 5,
  "outputMode": "grouped",
  "headLimit": 100,
  "toolPurpose": "- I need to compare how Tabs-family production components traverse React children and handle null conditional entries."
}
```
Output:
```
{"success":true,"mode":"content","numFiles":1,"numLines":1,"pagination":{"offset":0,"limit":100,"returned":1,"total":1,"hasMore":false},"matchesByFile":{"src/Tabs/Tabs.js":[{"file":"src/Tabs/Tabs.js","line":605,"content":"const children = React.Children.map(childrenProp, (child) => {","contextBefore":[{"line":600,"content":"}}"},{"line":601,"content":"/>"},{"line":602,"content":");"},{"line":603,"content":""},{"line":604,"content":"let childIndex = 0;"}],"contextAfter":[{"line":606,"content":"if (!React.isValidElement(child)) {"},{"line":607,"content":"return null;"},{"line":608,"content":"}"},{"line":609,"content":""},{"line":610,"content":"if (process.env.NODE_ENV !== 'production') {"}],"matches":["React.Children.map"]}]}}
```

9. **Tool call: read_file**
Input:
```json
{
  "fileNames": [
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-26170/packages/material-ui-lab/src/TabList/TabList.js",
      "startLine": 1
    },
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-26170/packages/material-ui-lab/src/TabList/TabList.test.js",
      "startLine": 1
    },
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-26170/packages/material-ui/src/Tabs/Tabs.js",
      "startLine": 580
    }
  ],
  "toolPurpose": "- I want to inspect the complete TabList implementation and focused tests, plus the relevant Tabs child-traversal implementation, to establish the exact behavioral contract and mirror the proven null-child handling pattern."
}
```

10. **Tool call: read_file**
Input:
```json
{
  "fileNames": [
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-26170/package.json",
      "startLine": 1
    }
  ],
  "toolPurpose": "- I want to inspect repository scripts and package-manager metadata to select the smallest valid focused test and quality-gate commands."
}
```
Output:
```

File successfully read, file name package.json with file path: enc_file_sovfhn/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-26170/package.json

**File Read Information:**
- Lines read: 1 to 225 (225 lines)
- Total lines in file: 225
- Remaining lines: 0

Content:
{
  "version": "5.0.0-alpha.32",
  "private": true,
  "scripts": {
    "proptypes": "cross-env BABEL_ENV=development babel-node --extensions \".tsx,.ts,.js\" ./scripts/generateProptypes.ts",
    "deduplicate": "node scripts/deduplicate.js",
    "benchmark:browser": "yarn workspace benchmark browser",
    "build:codesandbox": "lerna run --parallel --scope \"@material-ui/*\" build",
    "release:version": "lerna version --exact --no-changelog --no-push --no-git-tag-version",
    "release:build": "lerna run --parallel --scope \"@material-ui/*\" build",
    "release:changelog": "node scripts/releaseChangelog",
    "release:publish": "lerna publish from-package --dist-tag next --contents build",
    "release:publish:dry-run": "lerna publish from-package --dist-tag next --contents build --registry=\"http://localhost:4873/\"",
    "release:tag": "node scripts/releaseTag",
    "docs:api": "rimraf ./docs/pages/api-docs && yarn docs:api:build",
    "docs:api:build": "cross-env BABEL_ENV=development __NEXT_EXPORT_TRAILING_SLASH=true babel-node --extensions \".tsx,.ts,.js\" ./docs/scripts/buildApi.ts  ./docs/pages/api-docs ./packages/material-ui-unstyled/src ./packages/material-ui/src ./packages/material-ui-lab/src --apiPagesManifestPath ./docs/src/pagesApi.js",
    "docs:build": "yarn workspace docs build",
    "docs:build-sw": "yarn workspace docs build-sw",
    "docs:build-color-preview": "babel-node scripts/buildColorTypes",
    "docs:deploy": "yarn workspace docs deploy",
    "docs:dev": "yarn workspace docs dev",
    "docs:export": "yarn workspace docs export",
    "docs:icons": "yarn workspace docs icons",
    "docs:size-why": "cross-env DOCS_STATS_ENABLED=true yarn docs:build",
    "docs:start": "yarn workspace docs start",
    "docs:i18n": "cross-env BABEL_ENV=development babel-node --extensions \".tsx,.ts,.js\" ./docs/scripts/i18n.js",
    "docs:typescript": "yarn docs:typescript:formatted --watch",
    "docs:typescript:check": "yarn workspace docs typescript",
    "docs:typescript:formatted": "cross-env BABEL_ENV=development babel-node --extensions \".tsx,.ts,.js\" ./docs/scripts/formattedTSDemos",
    "docs:mdicons:synonyms": "babel-node --config-file ./babel.config.js ./docs/scripts/updateIconSynonyms",
    "extract-error-codes": "cross-env MUI_EXTRACT_ERROR_CODES=true lerna run --parallel build:modern",
    "framer:build": "yarn workspace framer build",
    "install:codesandbox": "PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 yarn install --ignore-engines",
    "jsonlint": "node ./scripts/jsonlint.js",
    "lint": "eslint . --cache --report-unused-disable-directives --ext .js,.ts,.tsx --max-warnings 0",
    "lint:ci": "eslint . --report-unused-disable-directives --ext .js,.ts,.tsx --max-warnings 0",
    "stylelint": "stylelint --reportInvalidScopeDisables --reportNeedlessDisables 'docs/**/*.{js,ts,tsx}'",
    "prettier": "node ./scripts/prettier.js",
    "prettier:all": "node ./scripts/prettier.js write",
    "size:snapshot": "node --max-old-space-size=2048 ./scripts/sizeSnapshot/create",
    "size:why": "yarn size:snapshot --analyze",
    "start": "yarn && yarn docs:dev",
    "t": "node test/cli.js",
    "test": "yarn lint && yarn typescript && yarn test:coverage",
    "test:coverage": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc --reporter=text mocha 'packages/**/*.test.{js,ts,tsx}' 'docs/**/*.test.{js,ts,tsx}' 'scripts/**/*.test.{js,ts,tsx}' 'test/utils/**/*.test.{js,ts,tsx}'",
    "test:coverage:ci": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc --reporter=lcov mocha 'packages/**/*.test.{js,ts,tsx}' 'docs/**/*.test.{js,ts,tsx}' 'scripts/**/*.test.{js,ts,tsx}' 'test/utils/**/*.test.{js,ts,tsx}'",
    "test:coverage:html": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc --reporter=html mocha 'packages/**/*.test.{js,ts,tsx}' 'docs/**/*.test.{js,ts,tsx}' 'scripts/**/*.test.{js,ts,tsx}' 'test/utils/**/*.test.{js,ts,tsx}'",
    "test:e2e": "cross-env NODE_ENV=production yarn test:e2e:build && concurrently --success first --kill-others \"yarn test:e2e:run\" \"yarn test:e2e:server\"",
    "test:e2e:build": "webpack --config test/e2e/webpack.config.js",
    "test:e2e:dev": "concurrently \"yarn test:e2e:build --watch\" \"yarn test:e2e:server\"",
    "test:e2e:run": "mocha --config test/e2e/.mocharc.js 'test/e2e/**/*.test.{js,ts,tsx}'",
    "test:e2e:server": "serve test/e2e",
    "test:karma": "cross-env NODE_ENV=test karma start test/karma.conf.js",
    "test:karma:profile": "cross-env NODE_ENV=test karma start test/karma.conf.profile.js",
    "test:regressions": "cross-env NODE_ENV=production yarn test:regressions:build && concurrently --success first --kill-others \"yarn test:regressions:run\" \"yarn test:regressions:server\"",
    "test:regressions:build": "webpack --config test/regressions/webpack.config.js",
    "test:regressions:dev": "concurrently \"yarn test:regressions:build --watch\" \"yarn test:regressions:server\"",
    "test:regressions:run": "mocha --config test/regressions/.mocharc.js --delay 'test/regressions/**/*.test.js'",
    "test:regressions:server": "serve test/regressions",
    "test:umd": "node packages/material-ui/test/umd/run.js",
    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/*.test.{js,ts,tsx}' 'docs/**/*.test.{js,ts,tsx}' 'scripts/**/*.test.{js,ts,tsx}' 'test/utils/**/*.test.{js,ts,tsx}'",
    "test:watch": "yarn test:unit --watch",
    "test:argos": "node ./scripts/pushArgos.js",
    "typescript": "lerna run --no-bail --parallel typescript",
    "typescript:ci": "lerna run --concurrency 7 --no-bail --no-sort typescript"
  },
  "devDependencies": {
    "@babel/cli": "^7.10.1",
    "@babel/core": "^7.10.2",
    "@babel/node": "^7.10.1",
    "@babel/plugin-proposal-class-properties": "^7.10.1",
    "@babel/plugin-proposal-object-rest-spread": "^7.10.1",
    "@babel/plugin-transform-object-assign": "^7.10.1",
    "@babel/plugin-transform-react-constant-elements": "^7.10.1",
    "@babel/plugin-transform-runtime": "^7.10.1",
    "@babel/preset-env": "^7.10.2",
    "@babel/preset-react": "^7.10.1",
    "@babel/register": "^7.10.1",
    "@emotion/react": "^11.0.0",
    "@emotion/styled": "^11.0.0",
    "@eps1lon/enzyme-adapter-react-17": "^0.1.0",
    "@octokit/rest": "^18.0.14",
    "@rollup/plugin-replace": "^2.3.1",
    "@testing-library/dom": "^7.22.1",
    "@testing-library/react": "^11.0.2",
    "@types/chai": "^4.2.3",
    "@types/chai-dom": "^0.0.10",
    "@types/enzyme": "^3.10.3",
    "@types/format-util": "^1.0.1",
    "@types/fs-extra": "^9.0.0",
    "@types/jsdom": "^16.1.0",
    "@types/lodash": "^4.14.138",
    "@types/mocha": "^8.0.0",
    "@types/prettier": "^2.0.0",
    "@types/react": "^17.0.3",
    "@types/sinon": "^10.0.0",
    "@types/webpack": "^4.41.22",
    "@types/yargs": "^16.0.0",
    "@typescript-eslint/eslint-plugin": "^4.11.1",
    "@typescript-eslint/parser": "^4.11.1",
    "argos-cli": "^0.3.0",
    "babel-loader": "^8.0.0",
    "babel-plugin-istanbul": "^6.0.0",
    "babel-plugin-macros": "^3.0.0",
    "babel-plugin-module-resolver": "^4.0.0",
    "babel-plugin-optimize-clsx": "^2.3.0",
    "babel-plugin-react-remove-properties": "^0.3.0",
    "babel-plugin-tester": "^10.0.0",
    "babel-plugin-transform-react-remove-prop-types": "^0.4.21",
    "chai": "^4.1.2",
    "chai-dom": "^1.8.1",
    "chalk": "^4.0.0",
    "compression-webpack-plugin": "^6.0.2",
    "concurrently": "^6.0.0",
    "confusing-browser-globals": "^1.0.9",
    "core-js": "^2.6.11",
    "cpy-cli": "^3.1.1",
    "cross-env": "^7.0.0",
    "danger": "^10.0.0",
    "dom-accessibility-api": "^0.5.0",
    "dtslint": "^4.0.0",
    "enzyme": "^3.9.0",
    "eslint": "^7.4.0",
    "eslint-config-airbnb-typescript": "^12.0.0",
    "eslint-config-prettier": "^8.1.0",
    "eslint-import-resolver-webpack": "^0.13.0",
    "eslint-plugin-babel": "^5.3.1",
    "eslint-plugin-import": "^2.22.0",
    "eslint-plugin-jsx-a11y": "^6.3.1",
    "eslint-plugin-mocha": "^8.0.0",
    "eslint-plugin-react": "^7.20.3",
    "eslint-plugin-react-hooks": "^4.0.7",
    "fast-glob": "^3.2.4",
    "format-util": "^1.0.5",
    "fs-extra": "^9.0.0",
    "globby": "^11.0.1",
    "html-webpack-plugin": "^4.5.0",
    "jsdom": "^16.0.0",
    "karma": "^5.0.1",
    "karma-browserstack-launcher": "~1.4.0",
    "karma-chrome-launcher": "^3.0.0",
    "karma-mocha": "^2.0.0",
    "karma-sourcemap-loader": "^0.3.7",
    "karma-webpack": "^4.0.2",
    "lerna": "^4.0.0",
    "lodash": "^4.17.15",
    "mocha": "^8.0.1",
    "node-fetch": "^ 2.6.0",
    "nyc": "^15.0.0",
    "playwright": "^1.6.1",
    "prettier": "^2.0.1",
    "prop-types": "^15.7.2",
    "react": "^17.0.1",
    "react-dom": "^17.0.1",
    "react-router-dom": "^5.2.0",
    "react-test-renderer": "^17.0.1",
    "remark": "^13.0.0",
    "rimraf": "^3.0.0",
    "rollup": "^2.10.8",
    "rollup-plugin-babel": "^4.3.3",
    "rollup-plugin-commonjs": "^10.1.0",
    "rollup-plugin-node-globals": "^1.4.0",
    "rollup-plugin-node-resolve": "^5.2.0",
    "rollup-plugin-size-snapshot": "^0.12.0",
    "rollup-plugin-terser": "^7.0.0",
    "serve": "^11.3.2",
    "sinon": "^10.0.0",
    "source-map-support": "^0.5.19",
    "stylelint": "^13.7.2",
    "stylelint-config-standard": "^21.0.0",
    "stylelint-processor-styled-components": "^1.10.0",
    "terser-webpack-plugin": "^4.2.2",
    "tslint": "5.14.0",
    "typescript": "^4.1.2",
    "unist-util-visit": "^2.0.2",
    "url-loader": "^4.1.0",
    "webpack": "^4.41.0",
    "webpack-bundle-analyzer": "^4.1.0",
    "webpack-cli": "^4.0.0",
    "yargs": "^16.0.3",
    "yarn-deduplicate": "^3.0.0"
  },
  "resolutions": {
    "**/@babel/core": "^7.10.2",
    "**/@babel/code-frame": "^7.10.4",
    "**/@babel/plugin-proposal-class-properties": "^7.10.1",
    "**/@babel/plugin-proposal-object-rest-spread": "^7.10.1",
    "**/@babel/plugin-proposal-nullish-coalescing-operator": "^7.10.1",
    "**/@babel/plugin-proposal-numeric-separator": "^7.10.4",
    "**/@babel/plugin-proposal-optional-chaining": "^7.10.1",
    "**/@babel/plugin-transform-destructuring": "npm:@minh.nguyen/plugin-transform-destructuring@^7.5.2",
    "**/@babel/plugin-transform-runtime": "^7.10.1",
    "**/@babel/preset-env": "^7.10.2",
    "**/@babel/preset-react": "^7.10.1",
    "**/@babel/preset-typescript": "^7.10.4",
    "**/@babel/runtime": "^7.10.2",
    "**/@types/react": "^17.0.0",
    "**/@types/react-dom": "^17.0.0",
    "**/cross-fetch": "^3.0.5",
    "**/dot-prop": "^5.2.0",
    "**/react-is": "^17.0.1"
  },
  "nyc": {
    "include": [
      "packages/material-ui/src/**/*.js",
      "packages/material-ui/lab/**/*.{ts,tsx}",
      "packages/material-ui-utils/src/**/*.js",
      "packages/material-ui-styles/src/**/*.js"
    ],
    "exclude": [
      "**/*.test.{js,ts,tsx}"
    ],
    "sourceMap": false,
    "instrument": false
  },
  "workspaces": [
    "benchmark",
    "packages/*",
    "docs",
    "docs/packages/*",
    "framer",
    "test"
  ]
}

```

11. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "if [ -d node_modules ]; then printf 'node_modules=present\\n'; else printf 'node_modules=absent\\n'; fi; if [ -x node_modules/.bin/mocha ]; then printf 'mocha=present\\n'; else printf 'mocha=absent\\n'; fi; node --version; yarn --version",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-26170",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- I want to determine whether the isolated checkout has the local dependencies and runtimes needed to execute the focused TabList test without attempting any network installation."
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
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc 'if [ -d node_modules ]; then printf '"'"'node_modules=present\n'"'"'; else printf '"'"'node_modules=absent\n'"'"'; fi; if [ -x node_modules/.bin/mocha ]; then printf '"'"'mocha=present\n'"'"'; else printf '"'"'mocha=absent\n'"'"'; fi; node --version; yarn --version'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
node_modules=absent
mocha=absent
v26.8.1
4.18.0
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

```

12. **Tool call: edit_file**
Input:
```json
{
  "operations": [
    {
      "filePath": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-26170/packages/material-ui-lab/src/TabList/TabList.js",
      "originalContent": "const TabList = React.forwardRef(function TabList(props, ref) {\n  const { children: childrenProp, ...other } = props;\n  const context = useTabContext();\n  if (context === null) {\n    throw new TypeError('No TabContext provided');\n  }\n  const children = React.Children.map(childrenProp, (child) => {\n    return React.cloneElement(child, {\n      // SOMEDAY: `Tabs` will set those themselves\n      'aria-controls': getPanelId(context, child.props.value),\n      id: getTabId(context, child.props.value),\n    });\n  });\n\n  return (\n    \n      {children}\n    \n  );\n});",
      "newContent": "const TabList = React.forwardRef(function TabList(props, ref) {\n  const { children: childrenProp, ...other } = props;\n  const context = useTabContext();\n  if (context === null) {\n    throw new TypeError('No TabContext provided');\n  }\n  const children = React.Children.map(childrenProp, (child) => {\n    if (!React.isValidElement(child)) {\n      return null;\n    }\n\n    return React.cloneElement(child, {\n      // SOMEDAY: `Tabs` will set those themselves\n      'aria-controls': getPanelId(context, child.props.value),\n      id: getTabId(context, child.props.value),\n    });\n  });\n\n  return (\n    \n      {children}\n    \n  );\n});"
    }
  ],
  "toolPurpose": "- I want to update TabList so React child traversal ignores null, false, and other non-elements before accessing props or cloning, matching the established Tabs behavior for conditional rendering.",
  "references": {
    "hasJiraContext": false,
    "hasFigmaContext": false
  }
}
```
Output:
```
Successfully replaced content in file Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-26170/packages/material-ui-lab/src/TabList/TabList.js
```

13. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --no-compact; /Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --check; /Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --name-only",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/mui__material-ui-26170",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- I want to review the complete implementation diff, check whitespace correctness, and confirm only the intended production file changed before generating the benchmark patch."
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
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc '/Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --no-compact; /Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --check; /Users/sankanum1/.slingshot/bin/rtk git --no-pager diff --name-only'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
diff --git a/packages/material-ui-lab/src/TabList/TabList.js b/packages/material-ui-lab/src/TabList/TabList.js
index 95a1783..45a570d 100644
--- a/packages/material-ui-lab/src/TabList/TabList.js
+++ b/packages/material-ui-lab/src/TabList/TabList.js
@@ -10,6 +10,10 @@ const TabList = React.forwardRef(function TabList(props, ref) {
     throw new TypeError('No TabContext provided');
   }
   const children = React.Children.map(childrenProp, (child) => {
+    if (!React.isValidElement(child)) {
+      return null;
+    }
+
     return React.cloneElement(child, {
       // SOMEDAY: `Tabs` will set those themselves
       'aria-controls': getPanelId(context, child.props.value),

packages/material-ui-lab/src/TabList/TabList.js

Changes:

__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

```

14. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "mkdir -p /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results; git --no-pager diff -- packages/material-ui-lab/src/TabList/TabList.js > /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-26170.patch; git apply --check --reverse /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-26170.patch; changed_files=$(git apply --numstat /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-26170.patch | cut -f3); printf 'patch_files=%s\\n' \"$changed_files\"; if [ \"$changed_files\" != \"packages/material-ui-lab/src/TabList/TabList.js\" ]; then printf 'Unexpected patch contents\\n' >&2; exit 1; fi; while IFS=$'\\t' read -r added deleted file; do case \"$file\" in */test/*|*.test.*|*__snapshots__*|*coverage*|*test-artifact*) printf 'Forbidden test file or artifact: %s\\n' \"$file\" >&2; exit 1;; esac; printf 'validated_production_file=%s (+%s -%s)\\n' \"$file\" \"$added\" \"$deleted\"; done  /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-26170.patch; git apply --check --reverse /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-26170.patch; changed_files=$(git apply --numstat /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/mui__material-ui-26170.patch | cut -f3); printf '"'"'patch_files=%s\n'"'"' "$changed_files"; if [ "$changed_files" != "packages/material-ui-lab/src/TabList/TabList.js" ]; then printf '"'"'Unexpected patch contents\n'"'"' >&2; exit 1; fi; while IFS=$'"'"'\t'"'"' read -r added deleted file; do case "$file" in */test/*|*.test.*|*__snapshots__*|*coverage*|*test-artifact*) printf '"'"'Forbidden test file or artifact: %s\n'"'"' "$file" >&2; exit 1;; esac; printf '"'"'validated_production_file=%s (+%s -%s)\n'"'"' "$file" "$added" "$deleted"; done  {
+    if (!React.isValidElement(child)) {
+      return null;
+    }
+
     return React.cloneElement(child, {
       // SOMEDAY: `Tabs` will set those themselves
       'aria-controls': getPanelId(context, child.props.value),
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
      "command": "cmp ` rendering now matches the existing `Tabs` behavior.

## Validation

- Patch matches the complete Git diff.
- Patch applies/reverses cleanly.
- `git diff --check` passed.
- Patch contains exactly one production file.
- No tests or test artifacts are included.
- Repository remains at base commit `215794b567669951a61183d748c0b2be6483c3ea`.
- Unit tests and lint could not run because the isolated checkout has no `node_modules`.

## 📝 Files Modified

- [TabList.js](packages/material-ui-lab/src/TabList/TabList.js) — Added invalid-child guard. **+4 −0 lines**

## 📁 Files Created

- [mui__material-ui-26170.patch](../swe-results/mui__material-ui-26170.patch) — Generated benchmark patch at the required location. **+15 −0 lines**

---
