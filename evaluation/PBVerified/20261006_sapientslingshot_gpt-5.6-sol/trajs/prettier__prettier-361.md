# SWE-prettier-361 Trajectory

---

**Exported:** 2026-09-24T17:09:20.222Z

---

## SWE Benchmark Metadata

- **instanceId:** prettier__prettier-361
- **repo:** prettier/prettier
- **baseCommit:** 237e6f44bc75269b96b31541c4a06ad293a591dd
- **taskIndex:** 34
- **status:** completed

---

## Execution Metrics
| Metric | Value |
|---|---:|
| Prompt tokens | 0 |
| Completion tokens | 0 |
| Total tokens | 843440 |
| Credits consumed | 0.635570 |
| Total execution time | 3m 1s |

---

## Complete Raw Conversation

# Chat Session Export

**Exported:** 2026-09-24T17:09:20.220Z

## 👤 **User**

The current working directory is already provisioned by the benchmark host at exactly the task base commit, with one reachable commit and no Git remotes. Work only in this isolated local source tree.

Do not add Git remotes, clone, fetch, or pull. Do not access GitHub, GitHub APIs, upstream pull requests, commits, patches, or issue solutions. Do not use curl/wget or web-search tools. The benchmark runtime blocks outbound tools and commands.

Fix the issue using only the problem statement and the isolated local source tree. Generate prettier__prettier-361.patch from the git diff,verify that git diff prettier__prettier-361.patch contains only implementation or production files and no test files or test artifacts and then place it at this exact path: /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/prettier__prettier-361.patch.

Repository: prettier/prettier
Base Commit: 237e6f44bc75269b96b31541c4a06ad293a591dd
Problem: Export extension syntax not formatted correctly
Code using the [export extensions transform](https://babeljs.io/docs/plugins/transform-export-extensions/) is not formatted correctly.

When running prettier on one of my projects, the following:

```js
export reducer from './reducer'
```

was formatted as:

```js
export { reducer } from './reducer';
```

Note the addition of the curly braces, which changes the semantics of the `export` statement.

---

## 🤖 **Slingshot**

*9/24/2026, 12:06:20 PM*

## Agent Execution Steps

1. **Tool call: register_tools**
Input:
```json
{
  "tool_names": [
    "get_agent_memory",
    "get_workspace_files_list",
    "read_file",
    "grep",
    "run_terminal_command",
    "edit_file",
    "write_file",
    "add_agent_memory"
  ],
  "toolPurpose": "- Inspect the isolated repository and required `.env` context, locate the formatter implementation and relevant tests, implement the production-only fix, run local quality gates, and generate the requested patch artifact without network access."
}
```
Output:
```
Tools [get_agent_memory, get_workspace_files_list, read_file, grep, run_terminal_command, edit_file, write_file, add_agent_memory] are now registered and immediately available for usage.
```

2. **Tool call: get_agent_memory**
Input:
```json
{
  "toolPurpose": "- I want to read prior execution summaries and persistent workspace learnings before inspecting this isolated repository, so I can avoid duplicate work and respect established project conventions."
}
```
Output:
```
Successfully read agent memory content:
Learnings from previous agent sessions: Successfully loaded 144 memory entries. Use these to inform your work and avoid creating duplicate memories when calling `add_agent_memory` tool.
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
* When redirecting RTK git diff to a patch file, use --no-compact; compacted output can omit headers and produce an invalid patch.
* RTK git diff redirected to a file may omit the final newline; validate with git apply --check and regenerate with direct git diff if corrupt.
* A timed-out RTK git clone may leave a child process running; verify HEAD again before patch generation and reset to the requested base if it moved.
* After cherry-pick --no-commit, use git reset and git add -N for new files so plain git diff captures the complete patch.
* When creating a nested Git repo inside another repo, run `git init` with the nested absolute path to avoid reinitializing the parent repository.
```

3. **Tool call: read_file**
Input:
```json
{
  "fileNames": [
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361/.env",
      "startLine": 1,
      "endLine": 51
    }
  ],
  "toolPurpose": "- Read the exact user-required `.env` line range before analysis, while keeping all work confined to the isolated local source tree."
}
```
Output:
```

File successfully read, file name .env with file path: enc_file_sovfhn/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/.env

**File Read Information:**
- Lines read: 1 to 51 (51 lines)

Content:
# ─── Core Environment ──────────────────────────────────────────
# These commands should stay the same unless instructed otherwise
SAGE_ENV=development
ALLOW_DEV_MODE=true
EXECUTION_TRACE=false

# ─── AI Model ──────────────────────────────────────────────────
# getAIModel() defaults to "gpt-5.5" if unset
AI_MODEL=gpt-5.6-sol

# ─── SWE-PolyBench: Language Filter ────────────────────────────
# getSWELanguage() — valid: python | java | javascript | typescript
# Leave unset to load all languages
SWE_LANGUAGE=

# ─── SWE-PolyBench: Index Range ────────────────────────────────
SWE_INDEX_FLOOR= 101
SWE_INDEX_CEILING= 150

# ─── SWE-PolyBench: Concurrency ────────────────────────────────
# getSWEConcurrentTasks() — defaults to 5; min 1
SWE_CONCURRENT_TASKS=3
# getSWEMaxEvalWorkers() — defaults to 2; min 1
SWE_MAX_EVAL_WORKERS=2

# ─── SWE-PolyBench: Dataset ────────────────────────────────────
#If left unset will assume the full dataset

SWE_DATASET=verified # 394 human-verified instances from AmazonScience/SWE-PolyBench_Verified
# SWE_DATASET=500 # 500 stratified instances from AmazonScience/SWE-PolyBench_500 
# SWE_DATASET=full # all 2110 instances from AmazonScience/SWE-PolyBench

# ─── SWE-PolyBench: Subset / Namespace ────────────────────────
# getSWESubsetIds() — comma-separated instance IDs to run; empty = run all
# SWE_SUBSET= apache__dubbo-4678, trinodb__trino-3603

# getSWENamespace() — optional namespace prefix; empty = no namespace
SWE_NAMESPACE=

# ─── SWE-PolyBench: Local Harness Directory ────────────────────
# getSWEPolyBenchDir() — path to cloned amazon-science/SWE-PolyBench repo
SWE_POLYBENCH_DIR=/Users/sankanum1/Documents/SWE-PolyBench

# ─── SWE-PolyBench: Docker Cleanup ────────────────────────────
# getSWECleanupDockerImages() — true | 1 | yes to remove images after eval
SWE_CLEANUP_DOCKER_IMAGES=false

# ─── SWE-PolyBench: Preserve Completed Tabs ───────────────────
# getSWEPreserveCompletedTabs() — true | 1 | yes to keep tabs open
SWE_PRESERVE_COMPLETED_TABS=false

```

4. **Tool call: get_workspace_files_list**
Input:
```json
{
  "folderPaths": [
    "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361"
  ],
  "maxTokens": 12000,
  "toolPurpose": "- Inspect the repository file layout to identify formatter source, parser/printer modules, fixtures, and project scripts relevant to export extension syntax."
}
```
Output:
```
The workspace folder structure was very large so it has been truncated to reduce the context length. If you need further information about any missing files/folders use the get_filenames_using_content_search tool to perform a semantic search that searches workspace based on a search query.
Here is the folder structure for 'Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361':
- prettier__prettier-361
  - .npmignore
  - .travis.yml
  - CHANGELOG.md
  - LICENSE
  - README.md
  - bin
    - prettier.js
  - commands.md
  - docs
    - index.html
    - rollup.config.js
  - editors
    - atom.md
    - emacs
      - README.md
      - prettier-js.el
  - index.js
  - package.json
  - src
    - comments.js
    - doc-builders.js
    - doc-debug.js
    - doc-printer.js
    - doc-utils.js
    - fast-path.js
    - options.js
    - parser.js
    - printer.js
    - util.js
  - tests
    - abnormal
      - __snapshots__
        - jsfmt.spec.js.snap
      - break-continue.js
      - jsfmt.spec.js
      - return.js
    - annot
      - __snapshots__
        - jsfmt.spec.js.snap
      - annot.js
      - any
        - A.js
        - B.js
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
      - forward_ref.js
      - issue-530.js
      - jsfmt.spec.js
      - leak.js
      - other.js
      - scope.js
      - test.js
    - annot2
      - A.js
      - B.js
      - T.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
    - any
      - __snapshots__
        - jsfmt.spec.js.snap
      - any.js
      - anyexportflowfile.js
      - flowfixme.js
      - flowissue.js
      - jsfmt.spec.js
      - nonflowfile.js
      - propagate.js
      - reach.js
    - arith
      - Arith.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - exponent.js
      - generic.js
      - jsfmt.spec.js
      - mult.js
      - relational.js
    - array-filter
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
      - test2.js
    - array_spread
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - multiple.js
      - test.js
    - arraylib
      - __snapshots__
        - jsfmt.spec.js.snap
      - array_lib.js
      - jsfmt.spec.js
    - arrays
      - Arrays.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - last.js
      - numeric_elem.js
    - arrows
      - __snapshots__
        - jsfmt.spec.js.snap
      - advanced_arrows.js
      - arrow_function_expression.js
      - arrows.js
      - jsfmt.spec.js
      - long-call-no-args.js
    - async
      - __snapshots__
        - jsfmt.spec.js.snap
      - async.js
      - async2.js
      - async3.js
      - async_base_class.js
      - async_parse.js
      - async_promise.js
      - async_return_void.js
      - await_parse.js
      - conditional-expression.js
      - jsfmt.spec.js
    - async_iteration
      - __snapshots__
        - jsfmt.spec.js.snap
      - delegate_yield.js
      - generator.js
      - jsfmt.spec.js
      - return.js
      - throw.js
    - autocomplete
      - __snapshots__
        - jsfmt.spec.js.snap
      - customfun.js
      - jsfmt.spec.js
      - unknown.js
    - auxiliary
      - __snapshots__
        - jsfmt.spec.js.snap
      - client.js
      - jsfmt.spec.js
      - lib
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - lib.js
    - binary
      - __snapshots__
        - jsfmt.spec.js.snap
      - in.js
      - jsfmt.spec.js
    - binding
      - __snapshots__
        - jsfmt.spec.js.snap
      - const.js
      - jsfmt.spec.js
      - rebinding.js
      - scope.js
      - tdz.js
    - bom
      - FormData.js
      - MutationObserver.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
    - bounded_poly
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - scope.js
      - test.js
    - bracketSpacing
      - __snapshots__
        - jsfmt.spec.js.snap
      - array.js
      - jsfmt.spec.js
      - object.js
    - break
      - __snapshots__
        - jsfmt.spec.js.snap
      - break.js
      - jsfmt.spec.js
    - builtin_uses
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
      - test2.js
    - builtins
      - __snapshots__
        - jsfmt.spec.js.snap
      - array.js
      - genericfoo.js
      - jsfmt.spec.js
    - call_properties
      - A.js
      - B.js
      - C.js
      - D.js
      - E.js
      - F.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
    - callable
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - optional.js
      - primitives.js
    - check-contents
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - not_flow.js
    - class_munging
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - with_munging.js
      - without_munging.js
    - class_statics
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - class_subtyping
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
      - test2.js
      - test3.js
      - test4.js
    - class_type
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
      - test2.js
    - classes
      - A.js
      - B.js
      - C.js
      - D.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - class_shapes.js
      - expr.js
      - jsfmt.spec.js
      - loc.js
      - statics.js
    - closure
      - Closure.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - cond_havoc.js
      - const.js
      - jsfmt.spec.js
    - comments
      - __snapshots__
        - jsfmt.spec.js.snap
      - issues.js
      - jsfmt.spec.js
    - commonjs
      - Abs.js
      - Rel.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
    - computed_props
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
      - test2.js
      - test3.js
      - test4.js
      - test5.js
      - test6.js
      - test7.js
    - conditional
      - __snapshots__
        - jsfmt.spec.js.snap
      - conditional.js
      - jsfmt.spec.js
    - config_all
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - no_at_flow.js
    - config_all_false
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - no_at_flow.js
    - config_all_weak
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - no_at_flow.js
    - config_file_extensions
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - config_ignore
      - __snapshots__
        - jsfmt.spec.js.snap
      - dir
        - __snapshots__
          - jsfmt.spec.js.snap
        - foo.js
        - jsfmt.spec.js
      - foo.js
      - jsfmt.spec.js
    - config_module_name_mapper_PROJECT_ROOT-1.0
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - main.js
      - src
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - testmodule.js
    - config_module_name_mapper_filetype
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - config_module_name_rewrite_haste
      - A.js
      - Exists.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
    - config_module_name_rewrite_node
      - A.js
      - Exists.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
    - config_module_system_node_resolve_dirname
      - __snapshots__
        - jsfmt.spec.js.snap
      - custom_resolve_dir
        - testproj
          - __snapshots__
            - jsfmt.spec.js.snap
          - index.js
          - jsfmt.spec.js
        - testproj2
          - __snapshots__
            - jsfmt.spec.js.snap
          - index.js
          - jsfmt.spec.js
      - jsfmt.spec.js
      - subdir
        - __snapshots__
          - jsfmt.spec.js.snap
        - custom_resolve_dir
          - testproj2
            - __snapshots__
              - jsfmt.spec.js.snap
            - index.js
            - jsfmt.spec.js
        - jsfmt.spec.js
        - sublevel.js
      - toplevel.js
    - config_munging_underscores
      - __snapshots__
        - jsfmt.spec.js.snap
      - chain.js
      - commonjs_export.js
      - commonjs_import.js
      - jsfmt.spec.js
    - config_munging_underscores2
      - __snapshots__
        - jsfmt.spec.js.snap
      - chain.js
      - jsfmt.spec.js
    - const_params
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - constructor
      - __snapshots__
        - jsfmt.spec.js.snap
      - constructor.js
      - jsfmt.spec.js
    - constructor_annots
      - __snapshots__
        - jsfmt.spec.js.snap
      - constructors.js
      - jsfmt.spec.js
      - test.js
    - contents
      - ignore
        - __snapshots__
          - jsfmt.spec.js.snap
        - dummy.js
        - jsfmt.spec.js
        - test.js
      - no_flow
        - __snapshots__
          - jsfmt.spec.js.snap
        - dummy.js
        - jsfmt.spec.js
        - test.js
    - core_tests
      - __snapshots__
        - jsfmt.spec.js.snap
      - boolean.js
      - jsfmt.spec.js
      - map.js
      - regexp.js
      - weakset.js
    - covariance
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - coverage
      - __snapshots__
        - jsfmt.spec.js.snap
      - crash.js
      - declare_module.js
      - jsfmt.spec.js
      - no_pragma.js
      - non-termination.js
    - cycle
      - A.js
      - B.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
    - date
      - __snapshots__
        - jsfmt.spec.js.snap
      - date.js
      - jsfmt.spec.js
    - declaration_files_haste
      - ExplicitProvidesModuleDifferentName.js
      - ExplicitProvidesModuleSameName.js
      - ImplicitProvidesModule.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - external
        - _d3
          - __snapshots__
            - jsfmt.spec.js.snap
          - jsfmt.spec.js
          - min.js
      - foo
        - bar
          - __snapshots__
            - jsfmt.spec.js.snap
          - jsfmt.spec.js
          - nested_test.js
      - jsfmt.spec.js
      - md5.js
      - test.js
      - ws
        - __snapshots__
          - jsfmt.spec.js.snap
        - index.js
        - jsfmt.spec.js
        - test
          - __snapshots__
            - jsfmt.spec.js.snap
          - client.js
          - jsfmt.spec.js
    - declaration_files_incremental_haste
      - A.js
      - ExplicitProvidesModuleDifferentName.js
      - ExplicitProvidesModuleSameName.js
      - ImplicitProvidesModule.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - external
        - _d3
          - __snapshots__
            - jsfmt.spec.js.snap
          - jsfmt.spec.js
          - min.js
      - foo
        - bar
          - __snapshots__
            - jsfmt.spec.js.snap
          - jsfmt.spec.js
          - nested_test.js
      - jsfmt.spec.js
      - md5.js
      - test.js
      - ws
        - __snapshots__
          - jsfmt.spec.js.snap
        - index.js
        - jsfmt.spec.js
        - test
          - __snapshots__
            - jsfmt.spec.js.snap
          - client.js
          - jsfmt.spec.js
    - declaration_files_incremental_node
      - A.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test_absolute.js
      - test_relative.js
    - declaration_files_node
      - A.js
      - CJS.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test_absolute.js
      - test_relative.js
    - declare_class
      - __snapshots__
        - jsfmt.spec.js.snap
      - declare_class.js
      - jsfmt.spec.js
      - lib
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - test.js
    - declare_export
      - B.js
      - C.js
      - CommonJS_Clobbering_Class.js
      - CommonJS_Clobbering_Lit.js
      - CommonJS_Named.js
      - ES6_DefaultAndNamed.js
      - ES6_Default_AnonFunction1.js
      - ES6_Default_AnonFunction2.js
      - ES6_Default_NamedClass1.js
      - ES6_Default_NamedClass2.js
      - ES6_Default_NamedFunction1.js
      - ES6_Default_NamedFunction2.js
      - ES6_ExportAllFromMulti.js
      - ES6_ExportAllFrom_Intermediary1.js
      - ES6_ExportAllFrom_Intermediary2.js
      - ES6_ExportAllFrom_Source1.js
      - ES6_ExportAllFrom_Source2.js
      - ES6_ExportFrom_Intermediary1.js
      - ES6_ExportFrom_Intermediary2.js
      - ES6_ExportFrom_Source1.js
      - ES6_ExportFrom_Source2.js
      - ES6_Named1.js
      - ES6_Named2.js
      - ProvidesModuleA.js
      - ProvidesModuleCJSDefault.js
      - ProvidesModuleD.js
      - ProvidesModuleES6Default.js
      - SideEffects.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - es6modules.js
      - jsfmt.spec.js
    - declare_fun
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - declare_module_exports
      - __snapshots__
        - jsfmt.spec.js.snap
      - flow-typed
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - libs.js
      - jsfmt.spec.js
      - main.js
    - declare_type
      - __snapshots__
        - jsfmt.spec.js.snap
      - import_declare_type.js
      - jsfmt.spec.js
      - lib
        - DeclareModule_TypeAlias.js
        - __snapshots__
          - jsfmt.spec.js.snap
        - declare_type_exports.js
        - jsfmt.spec.js
    - def_site_variance
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - demo
      - 1
        - __snapshots__
          - jsfmt.spec.js.snap
        - f.js
        - jsfmt.spec.js
      - 2
        - A.js
        - B.js
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
    - deps
      - A.js
      - B.js
      - C.js
      - D.js
      - E.js
      - F.js
      - G.js
      - H.js
      - I.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
    - destructuring
      - __snapshots__
        - jsfmt.spec.js.snap
      - array_rest.js
      - computed.js
      - defaults.js
      - destructuring.js
      - destructuring_param.js
      - eager.js
      - jsfmt.spec.js
      - poly.js
      - rec.js
      - string_lit.js
      - unannotated.js
    - dictionary
      - __snapshots__
        - jsfmt.spec.js.snap
      - any.js
      - compatible.js
      - dictionary.js
      - incompatible.js
      - issue-1745.js
      - jsfmt.spec.js
      - test.js
      - test_client.js
    - disjoint-union-perf
      - __snapshots__
        - jsfmt.spec.js.snap
      - ast.js
      - emit.js
      - jsAst.js
      - jsfmt.spec.js
    - docblock_flow
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - license_with_flow.js
      - max_header_tokens.js
      - multiple_flows_1.js
      - multiple_flows_2.js
      - multiple_providesModule_1.js
      - multiple_providesModule_2.js
      - use_strict_with_flow.js
      - with_flow.js
      - without_flow.js
    - dom
      - CanvasRenderingContext2D.js
      - CustomEvent.js
      - Document.js
      - Element.js
      - HTMLCanvasElement.js
      - HTMLElement.js
      - HTMLInputElement.js
      - URL.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - eventtarget.js
      - jsfmt.spec.js
      - path2d.js
      - registerElement.js
      - traversal.js
    - dump-types
      - __snapshots__
        - jsfmt.spec.js.snap
      - import.js
      - jsfmt.spec.js
      - test.js
    - duplicate_methods
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - empty_statement
      - __snapshots__
        - jsfmt.spec.js.snap
      - body.js
      - jsfmt.spec.js
    - encaps
      - __snapshots__
        - jsfmt.spec.js.snap
      - encaps.js
      - jsfmt.spec.js
    - enumerror
      - __snapshots__
        - jsfmt.spec.js.snap
      - enumerror.js
      - jsfmt.spec.js
    - equals
      - __snapshots__
        - jsfmt.spec.js.snap
      - equals.js
      - jsfmt.spec.js
    - error_messages
      - __snapshots__
        - jsfmt.spec.js.snap
      - errors.js
      - jsfmt.spec.js
    - es6modules
      - B.js
      - C.js
      - CommonJS_Clobbering_Class.js
      - CommonJS_Clobbering_Frozen.js
      - CommonJS_Clobbering_Lit.js
      - CommonJS_Named.js
      - ES6_DefaultAndNamed.js
      - ES6_Default_AnonClass1.js
      - ES6_Default_AnonClass2.js
      - ES6_Default_AnonFunction1.js
      - ES6_Default_AnonFunction2.js
      - ES6_Default_NamedClass1.js
      - ES6_Default_NamedClass2.js
      - ES6_Default_NamedFunction1.js
      - ES6_Default_NamedFunction2.js
      - ES6_ExportAllFromMulti.js
      - ES6_ExportAllFrom_Intermediary1.js
      - ES6_ExportAllFrom_Intermediary2.js
      - ES6_ExportAllFrom_Source1.js
      - ES6_ExportAllFrom_Source2.js
      - ES6_ExportFrom_Intermediary1.js
      - ES6_ExportFrom_Intermediary2.js
      - ES6_ExportFrom_Source1.js
      - ES6_ExportFrom_Source2.js
      - ES6_Named1.js
      - ES6_Named2.js
      - ExportType.js
      - ProvidesModuleA.js
      - ProvidesModuleCJSDefault.js
      - ProvidesModuleD.js
      - ProvidesModuleES6Default.js
      - SideEffects.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - es6modules.js
      - export_default_arrow_expression.js
      - export_default_call_expression.js
      - export_default_function_expression.js
      - export_default_new_expression.js
      - jsfmt.spec.js
      - test_imports_are_frozen.js
    - es_declare_module
      - __snapshots__
        - jsfmt.spec.js.snap
      - es_declare_module.js
      - flow-typed
        - __snapshots__
          - jsfmt.spec.js.snap
        - declares.js
        - jsfmt.spec.js
      - jsfmt.spec.js
    - esproposal_export_star_as.enable
      - __snapshots__
        - jsfmt.spec.js.snap
      - dest.js
      - jsfmt.spec.js
      - source.js
    - esproposal_export_star_as.ignore
      - __snapshots__
        - jsfmt.spec.js.snap
      - dest.js
      - jsfmt.spec.js
      - source.js
    - export
      - __snapshots__
        - jsfmt.spec.js.snap
      - bracket.js
      - empty.js
      - jsfmt.spec.js
    - export_default
      - P.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - lib
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - lib.js
      - test.js
    - export_type
      - __snapshots__
        - jsfmt.spec.js.snap
      - cjs_with_types.js
      - importer.js
      - jsfmt.spec.js
      - types_only.js
      - types_only2.js
    - extensions
      - __snapshots__
        - jsfmt.spec.js.snap
      - foo.js
      - jsfmt.spec.js
    - facebook_fbt_none
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - main.js
    - facebook_fbt_some
      - __snapshots__
        - jsfmt.spec.js.snap
      - flow-typed
        - __snapshots__
          - jsfmt.spec.js.snap
        - fbt.js
        - jsfmt.spec.js
      - jsfmt.spec.js
      - main.js
    - facebookisms
      - Bar.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - copyProperties.js
      - invariant.js
      - jsfmt.spec.js
      - lib.js
      - mergeInto.js
      - test.js
    - fetch
      - __snapshots__
        - jsfmt.spec.js.snap
      - fetch.js
      - headers.js
      - jsfmt.spec.js
      - request.js
      - response.js
      - urlsearchparams.js
    - find-module
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - req.js
      - test.js
    - fixpoint
      - Fun.js
      - Ycombinator.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
    - flow_ast.template_strings
      - __snapshots__
        - jsfmt.spec.js.snap
      - foo.js
      - jsfmt.spec.js
    - for
      - __snapshots__
        - jsfmt.spec.js.snap
      - abnormal.js
      - abnormal_for_in.js
      - abnormal_for_of.js
      - for.js
      - jsfmt.spec.js
    - forof
      - __snapshots__
        - jsfmt.spec.js.snap
      - forof.js
      - jsfmt.spec.js
    - function
      - __snapshots__
        - jsfmt.spec.js.snap
      - apply.js
      - bind.js
      - call.js
      - function.js
      - function_expression.js
      - jsfmt.spec.js
      - rest.js
    - funrec
      - __snapshots__
        - jsfmt.spec.js.snap
      - funrec.js
      - jsfmt.spec.js
    - generators
      - __snapshots__
        - jsfmt.spec.js.snap
      - class.js
      - class_failure.js
      - generators.js
      - jsfmt.spec.js
      - return.js
      - throw.js
      - variance.js
    - generics
      - __snapshots__
        - jsfmt.spec.js.snap
      - generics.js
      - jsfmt.spec.js
    - geolocation
      - __snapshots__
        - jsfmt.spec.js.snap
      - a.js
      - jsfmt.spec.js
    - get-def
      - __snapshots__
        - jsfmt.spec.js.snap
      - example.js
      - helpers
        - __snapshots__
          - jsfmt.spec.js.snap
        - exports_default.js
        - exports_named.js
        - jsfmt.spec.js
      - imports.js
      - jsfmt.spec.js
      - library.js
    - get-def2
      - Parent.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - lib
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - jsx.js
      - main.js
      - override.js
      - react.js
      - types.js
    - get-imports-and-importers
      - __snapshots__
        - jsfmt.spec.js.snap
      - a.js
      - b.js
      - c.js
      - jsfmt.spec.js
    - getters_and_setters_disabled
      - __snapshots__
        - jsfmt.spec.js.snap
      - getters_and_setters.js
      - jsfmt.spec.js
    - getters_and_setters_enabled
      - __snapshots__
        - jsfmt.spec.js.snap
      - class.js
      - jsfmt.spec.js
      - object.js
      - react.js
      - variance.js
    - haste_cycle
      - API.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - models
        - OpenGraphAction.js
        - OpenGraphObject.js
        - OpenGraphValueContainer.js
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
    - haste_dupe
      - __snapshots__
        - jsfmt.spec.js.snap
      - dupe1.js
      - dupe2.js
      - jsfmt.spec.js
      - requires_dupe.js
    - ignore_package
      - __snapshots__
        - jsfmt.spec.js.snap
      - foo.js
      - jsfmt.spec.js
    - immutable_methods
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - import
      - __snapshots__
        - jsfmt.spec.js.snap
      - brackets.js
      - jsfmt.spec.js
    - import_type
      - ExportCJSDefault_Class.js
      - ExportCJSNamed_Class.js
      - ExportDefault_Class.js
      - ExportNamed_Alias.js
      - ExportNamed_Class.js
      - ExportsANumber.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - import_type.js
      - issue-359.js
      - jsfmt.spec.js
    - import_typeof
      - ExportCJSDefault_Class.js
      - ExportCJSDefault_Number.js
      - ExportCJSNamed_Class.js
      - ExportCJSNamed_Number.js
      - ExportDefault_Class.js
      - ExportDefault_Number.js
      - ExportNamed_Alias.js
      - ExportNamed_Class.js
      - ExportNamed_Multi.js
      - ExportNamed_Number.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - import_typeof.js
      - jsfmt.spec.js
    - include
      - foo
        - batman
          - __snapshots__
            - jsfmt.spec.js.snap
          - baz.js
          - jsfmt.spec.js
      - included
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - test.js
    - incremental
      - __snapshots__
        - jsfmt.spec.js.snap
      - a.js
      - b.js
      - dup_a.js
      - jsfmt.spec.js
    - incremental_basic
      - __snapshots__
        - jsfmt.spec.js.snap
      - a.js
      - b.js
      - c.js
      - jsfmt.spec.js
      - tmp1
        - __snapshots__
          - jsfmt.spec.js.snap
        - b.js
        - jsfmt.spec.js
      - tmp2
        - __snapshots__
          - jsfmt.spec.js.snap
        - a.js
        - jsfmt.spec.js
      - tmp3
        - __snapshots__
          - jsfmt.spec.js.snap
        - b.js
        - jsfmt.spec.js
    - incremental_cycle
      - A.js
      - B.js
      - C.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - tmp1
        - B.js
        - C.js
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
      - tmp2
        - B.js
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
      - tmp3
        - B.js
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
    - incremental_delete
      - __snapshots__
        - jsfmt.spec.js.snap
      - a.js
      - b.js
      - c.js
      - dupe1.js
      - dupe2.js
      - jsfmt.spec.js
      - requires_dupe.js
      - requires_unchecked.js
      - unchecked.js
    - incremental_duplicate_delete
      - A.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
    - incremental_json
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - incremental_mixed_naming_cycle
      - __snapshots__
        - jsfmt.spec.js.snap
      - a.js
      - b.js
      - c.js
      - d.js
      - jsfmt.spec.js
      - root.js
      - tmp1
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - root.js
    - incremental_non_flow_move
      - __snapshots__
        - jsfmt.spec.js.snap
      - foo.js
      - jsfmt.spec.js
      - test.js
    - incremental_path
      - dir
        - __snapshots__
          - jsfmt.spec.js.snap
        - a.js
        - jsfmt.spec.js
    - indexer
      - A.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - multiple.js
    - init
      - __snapshots__
        - jsfmt.spec.js.snap
      - hoisted.js
      - hoisted2.js
      - jsfmt.spec.js
      - let.js
      - nullable-init.js
    - instanceof
      - __snapshots__
        - jsfmt.spec.js.snap
      - instanceof.js
      - jsfmt.spec.js
    - integration
      - __snapshots__
        - jsfmt.spec.js.snap
      - bar.js
      - foo.js
      - jsfmt.spec.js
    - interface
      - __snapshots__
        - jsfmt.spec.js.snap
      - import.js
      - indexer.js
      - interface.js
      - jsfmt.spec.js
      - test.js
      - test2.js
      - test3.js
      - test4.js
    - intersection
      - __snapshots__
        - jsfmt.spec.js.snap
      - intersection.js
      - jsfmt.spec.js
      - lib
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - lib.js
      - objassign.js
      - pred.js
      - test_fun.js
      - test_obj.js
    - issues-11
      - __snapshots__
        - jsfmt.spec.js.snap
      - export.js
      - import.js
      - jsfmt.spec.js
    - iter
      - __snapshots__
        - jsfmt.spec.js.snap
      - iter.js
      - jsfmt.spec.js
    - iterable
      - __snapshots__
        - jsfmt.spec.js.snap
      - array.js
      - caching_bug.js
      - iter.js
      - iterator_result.js
      - jsfmt.spec.js
      - map.js
      - set.js
      - string.js
      - variance.js
    - jsx
      - __snapshots__
        - jsfmt.spec.js.snap
      - expression.js
      - jsfmt.spec.js
      - quotes.js
    - jsx_escape
      - __snapshots__
        - jsfmt.spec.js.snap
      - escape.js
      - jsfmt.spec.js
    - jsx_intrinsics.builtin
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - main.js
      - strings.js
    - jsx_intrinsics.custom
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - lib
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - jsx.js
      - main.js
      - strings.js
    - keys
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - keys.js
    - keyvalue
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - keyvalue.js
    - last_argument_expansion
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - jsx.js
      - object.js
    - last_duplicate_property_wins
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - lib
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - libtest.js
    - lib_interfaces
      - declarations
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - underscore.js
    - libconfig
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - libA.js
      - libB.js
      - libtest.js
    - libdef_ignored_module
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - lib
        - __snapshots__
          - jsfmt.spec.js.snap
        - foo.js
        - jsfmt.spec.js
      - test.js
    - liberr
      - __snapshots__
        - jsfmt.spec.js.snap
      - a.js
      - jsfmt.spec.js
      - libs
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - type_error.js
    - libflow-typed
      - __snapshots__
        - jsfmt.spec.js.snap
      - flow-typed
        - __snapshots__
          - jsfmt.spec.js.snap
        - dino.js
        - jsfmt.spec.js
      - jsfmt.spec.js
      - libtest.js
    - librec
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - lib
        - A
          - __snapshots__
            - jsfmt.spec.js.snap
          - jsfmt.spec.js
          - libA.js
        - B
          - __snapshots__
            - jsfmt.spec.js.snap
          - jsfmt.spec.js
          - libB.js
      - libtest.js
    - line-endings
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - windows.js
    - literal
      - __snapshots__
        - jsfmt.spec.js.snap
      - enum.js
      - enum_client.js
      - jsfmt.spec.js
      - number.js
    - locals
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - lex.js
      - locals.js
    - logical
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - logical.js
    - loners
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - loners.js
    - method_properties
      - __snapshots__
        - jsfmt.spec.js.snap
      - exports_optional_prop.js
      - jsfmt.spec.js
      - test.js
    - misc
      - A.js
      - B.js
      - C.js
      - D.js
      - E.js
      - F.js
      - G.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
    - missing_annotation
      - __snapshots__
        - jsfmt.spec.js.snap
      - array.js
      - async_return.js
      - infer.js
      - jsfmt.spec.js
    - modified_lib
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - lib
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - lib.js
      - test.js
    - module_not_found_errors
      - src
        - __snapshots__
          - jsfmt.spec.js.snap
        - index.js
        - jsfmt.spec.js
    - module_redirect
      - A.js
      - B.js
      - C.js
      - D.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
    - module_use_strict
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - modules
      - __snapshots__
        - jsfmt.spec.js.snap
      - cli.js
      - cli2.js
      - jsfmt.spec.js
      - lib.js
    - more_annot
      - __snapshots__
        - jsfmt.spec.js.snap
      - client_object.js
      - jsfmt.spec.js
      - object.js
      - proto.js
      - super.js
    - more_classes
      - Bar.js
      - Foo.js
      - Qux.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
    - more_generics
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - poly.js
    - more_path
      - Condition.js
      - FlowSA.js
      - Sigma.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - more_react
      - API.react.js
      - App.react.js
      - JSX.js
      - jsfmt.spec.js
      - propTypes.js
    - more_statics
      - __snapshots__
        - jsfmt.spec.js.snap
      - class_static.js
      - jsfmt.spec.js
    - name_prop
      - __snapshots__
        - jsfmt.spec.js.snap
      - class.js
      - function.js
      - jsfmt.spec.js
    - namespace
      - __snapshots__
        - jsfmt.spec.js.snap
      - client.js
      - jsfmt.spec.js
      - namespace.js
    - new_expression
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - new_expression.js
    - new_react
      - FeedUFI.react.js
      - Mixin.js
      - UFILikeCount.react.js
      - bad_default_props.js
      - classes.js
      - fakelib
        - jsfmt.spec.js
        - type_aliases.js
      - import-react.js
      - jsfmt.spec.js
      - new_react.js
      - propTypes.js
      - props.js
      - props2.js
      - props3.js
      - props4.js
      - props5.js
      - state.js
      - state2.js
      - state3.js
      - state4.js
      - state5.js
    - node_haste
      - __snapshots__
        - jsfmt.spec.js.snap
      - client.js
      - external
        - _d3
          - __snapshots__
            - jsfmt.spec.js.snap
          - jsfmt.spec.js
          - min.js
      - foo
        - bar
          - __snapshots__
            - jsfmt.spec.js.snap
          - client.js
          - jsfmt.spec.js
      - jsfmt.spec.js
      - md5.js
      - ws
        - __snapshots__
          - jsfmt.spec.js.snap
        - index.js
        - jsfmt.spec.js
        - test
          - __snapshots__
            - jsfmt.spec.js.snap
          - client.js
          - jsfmt.spec.js
    - node_modules_with_symlinks
      - root
        - __snapshots__
          - jsfmt.spec.js.snap
        - foo.js
        - jsfmt.spec.js
        - symlink_lib
          - __snapshots__
            - jsfmt.spec.js.snap
          - index.js
          - jsfmt.spec.js
      - symlink_lib_outside_root
        - __snapshots__
          - jsfmt.spec.js.snap
        - index.js
        - jsfmt.spec.js
    - node_modules_without_json
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - node_tests
      - assert
        - __snapshots__
          - jsfmt.spec.js.snap
        - assert.js
        - jsfmt.spec.js
      - basic
        - __snapshots__
          - jsfmt.spec.js.snap
        - bar.js
        - foo.js
        - jsfmt.spec.js
      - basic_file
        - __snapshots__
          - jsfmt.spec.js.snap
        - bar.js
        - foo.js
        - jsfmt.spec.js
      - basic_node_modules
        - __snapshots__
          - jsfmt.spec.js.snap
        - foo.js
        - jsfmt.spec.js
      - basic_node_modules_with_path
        - __snapshots__
          - jsfmt.spec.js.snap
        - foo.js
        - jsfmt.spec.js
      - basic_package
        - __snapshots__
          - jsfmt.spec.js.snap
        - bar_lib
          - __snapshots__
            - jsfmt.spec.js.snap
          - bar.js
          - jsfmt.spec.js
        - foo.js
        - jsfmt.spec.js
      - buffer
        - __snapshots__
          - jsfmt.spec.js.snap
        - buffer.js
        - jsfmt.spec.js
      - child_process
        - __snapshots__
          - jsfmt.spec.js.snap
        - exec.js
        - execFile.js
        - execSync.js
        - jsfmt.spec.js
        - spawn.js
      - crypto
        - __snapshots__
          - jsfmt.spec.js.snap
        - crypto.js
        - jsfmt.spec.js
      - fs
        - __snapshots__
          - jsfmt.spec.js.snap
        - fs.js
        - jsfmt.spec.js
      - json_file
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - package2
          - __snapshots__
            - jsfmt.spec.js.snap
          - index.js
          - jsfmt.spec.js
        - test.js
      - os
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - userInfo.js
      - package_file
        - __snapshots__
          - jsfmt.spec.js.snap
        - bar_lib
          - __snapshots__
            - jsfmt.spec.js.snap
          - bar.js
          - jsfmt.spec.js
        - bar_lib.js
        - foo.js
        - jsfmt.spec.js
      - package_file_node_modules
        - foo
          - __snapshots__
            - jsfmt.spec.js.snap
          - foo.js
          - jsfmt.spec.js
      - path_node_modules
        - __snapshots__
          - jsfmt.spec.js.snap
        - foo.js
        - jsfmt.spec.js
      - path_node_modules_with_short_main
        - __snapshots__
          - jsfmt.spec.js.snap
        - foo.js
        - jsfmt.spec.js
      - path_node_modules_without_main
        - __snapshots__
          - jsfmt.spec.js.snap
        - foo.js
        - jsfmt.spec.js
      - path_package
        - __snapshots__
          - jsfmt.spec.js.snap
        - foo.js
        - jsfmt.spec.js
      - stream
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - stream.js
      - timers
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - timers.js
      - url
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - url.js
    - nullable
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - maybe.js
      - nullable.js
      - simple_nullable.js
    - number_constants
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - number_constants.js
    - object-method
      - __snapshots__
        - jsfmt.spec.js.snap
      - id.js
      - jsfmt.spec.js
      - subtype.js
      - test.js
      - test2.js
      - test3.js
    - object_annot
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - object_api
      - __snapshots__
        - jsfmt.spec.js.snap
      - a.js
      - b.js
      - c.js
      - jsfmt.spec.js
      - object_assign.js
      - object_create.js
      - object_getprototypeof.js
      - object_keys.js
      - object_missing.js
      - object_prototype.js
    - object_assign
      - A.js
      - B.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - apply.js
      - jsfmt.spec.js
      - non_objects.js
      - undefined.js
    - object_freeze
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - object_freeze.js
    - object_is
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - object_is.js
    - objects
      - __snapshots__
        - jsfmt.spec.js.snap
      - conversion.js
      - jsfmt.spec.js
      - objects.js
      - unaliased_assign.js
    - objmap
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - objmap.js
    - optional
      - __snapshots__
        - jsfmt.spec.js.snap
      - client_optional.js
      - default.js
      - generic.js
      - jsfmt.spec.js
      - maybe.js
      - nullable.js
      - optional.js
      - optional_param.js
      - optional_param2.js
      - optional_param3.js
      - optional_param4.js
      - undefined.js
      - undefined2.js
    - optional_props
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
      - test2.js
      - test3.js
      - test3_failure.js
    - overload
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - lib
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - lib.js
      - overload.js
      - test.js
      - test2.js
      - test3.js
      - union.js
    - parse
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - no_parse_error.js
    - parse_error_haste
      - Client.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
    - parse_error_node
      - Client.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
    - path
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - while.js
    - plsummit
      - __snapshots__
        - jsfmt.spec.js.snap
      - arrays.js
      - export_class.js
      - generics.js
      - import_class.js
      - jsfmt.spec.js
      - locals.js
      - objects.js
    - poly
      - __snapshots__
        - jsfmt.spec.js.snap
      - annot.js
      - implicit_bounded_instantiation.js
      - issue-1029.js
      - jsfmt.spec.js
      - poly.js
      - test.js
    - poly_class_export
      - A.js
      - B.js
      - C.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
    - poly_overload
      - decls
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
        - typescript-deferred.js
    - predicates-abstract
      - __snapshots__
        - jsfmt.spec.js.snap
      - filter-union.js
      - filter.js
      - jsfmt.spec.js
      - refine.js
      - sanity-filter-union.js
      - sanity-filter.js
      - sanity-refine.js
    - predicates-declared
      - __snapshots__
        - jsfmt.spec.js.snap
      - function-bind.js
      - function-union.js
      - is-string-decl.js
      - jsfmt.spec.js
      - logical-or.js
      - object-invariant.js
      - orig-string-tag-check.js
      - sanity-fall-through.js
      - sanity-invalid-calls.js
      - sanity-is-string-bug.js
      - sanity-parameter-mismatch.js
      - sanity-pred-with-body.js
      - sanity-return-type.js
    - predicates-inferred
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - sanity-multi-params.js
      - sanity-ordering.js
      - sanity-unbound-var.js
      - sanity.js
      - simple-predicate-func-post.js
      - simple-predicate-func.js
    - predicates-parsing
      - __snapshots__
        - jsfmt.spec.js.snap
      - fail-0.js
      - fail-1.js
      - fail-2.js
      - fail-3.js
      - jsfmt.spec.js
      - pass.js
    - prettier
      - __snapshots__
        - jsfmt.spec.js.snap
      - binary-expressions.js
      - directives.js
      - exports.js
      - jsfmt.spec.js
      - jsx-multiline-assign.js
      - jsx-significant-space.js
      - jsx-split-attrs.js
      - jsx-stateless-arrow-fn.js
      - method-chain.js
      - optional-type-name.js
    - promises
      - __snapshots__
        - jsfmt.spec.js.snap
      - all.js
      - covariance.js
      - jsfmt.spec.js
      - promise.js
      - resolve_global.js
      - resolve_void.js
    - pure_component
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - qualified
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - qualified.js
    - quotes
      - __snapshots__
        - jsfmt.spec.js.snap
      - functions.js
      - jsfmt.spec.js
      - strings.js
    - react
      - ArityError.react.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - createElementRequiredProp_string.js
      - createElement_string.js
      - import_react.js
      - jsfmt.spec.js
      - jsx_spread.js
      - proptype_arrayOf.js
      - proptype_func.js
      - proptype_missing.js
      - proptype_object.js
      - proptype_objectOf.js
      - proptype_oneOf.js
      - proptype_oneOfType.js
    - react_functional
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - react_modules
      - __snapshots__
        - jsfmt.spec.js.snap
      - createclass-callsite.js
      - createclass-module.js
      - es6class-types-callsite.js
      - es6class-types-module.js
      - jsfmt.spec.js
    - rec
      - __snapshots__
        - jsfmt.spec.js.snap
      - issue-1228.js
      - issue-598.js
      - jsfmt.spec.js
      - test.js
      - test2.js
      - test3.js
      - test4.js
      - test5.js
    - recheck
      - __snapshots__
        - jsfmt.spec.js.snap
      - a1.js
      - a2.js
      - a3.js
      - b0.js
      - b1.js
      - b2.js
      - b3.js
      - c1.js
      - c2.js
      - c3.js
      - d1.js
      - d2.js
      - e1.js
      - e2.js
      - f1.js
      - f2.js
      - g1.js
      - g2.js
      - g3.js
      - h1.js
      - h2.js
      - jsfmt.spec.js
      - tmp1a
        - __snapshots__
          - jsfmt.spec.js.snap
        - a1.js
        - jsfmt.spec.js
      - tmp1b
        - __snapshots__
          - jsfmt.spec.js.snap
        - b1.js
        - jsfmt.spec.js
      - tmp1c
        - __snapshots__
          - jsfmt.spec.js.snap
        - c2.js
        - jsfmt.spec.js
      - tmp1d
        - __snapshots__
          - jsfmt.spec.js.snap
        - d1.js
        - jsfmt.spec.js
      - tmp1e
        - __snapshots__
          - jsfmt.spec.js.snap
        - e2.js
        - jsfmt.spec.js
      - tmp1f
        - __snapshots__
          - jsfmt.spec.js.snap
        - f1.js
        - jsfmt.spec.js
      - tmp1g
        - __snapshots__
          - jsfmt.spec.js.snap
        - g1.js
        - jsfmt.spec.js
      - tmp1h
        - __snapshots__
          - jsfmt.spec.js.snap
        - h1.js
        - jsfmt.spec.js
      - tmp2a
        - __snapshots__
          - jsfmt.spec.js.snap
        - a1.js
        - jsfmt.spec.js
      - tmp2b
        - __snapshots__
          - jsfmt.spec.js.snap
        - b0.js
        - jsfmt.spec.js
      - tmp2c
        - __snapshots__
          - jsfmt.spec.js.snap
        - c1.js
        - jsfmt.spec.js
      - tmp2e
        - __snapshots__
          - jsfmt.spec.js.snap
        - e1.js
        - jsfmt.spec.js
      - tmp2f
        - __snapshots__
          - jsfmt.spec.js.snap
        - f1.js
        - jsfmt.spec.js
      - tmp3e
        - __snapshots__
          - jsfmt.spec.js.snap
        - e1.js
        - e2.js
        - jsfmt.spec.js
      - tmp3f
        - __snapshots__
          - jsfmt.spec.js.snap
        - f1.js
        - jsfmt.spec.js
      - tmp4f
        - __snapshots__
          - jsfmt.spec.js.snap
        - f1.js
        - jsfmt.spec.js
    - recheck-haste
      - A1.js
      - A3.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - tmp1A
        - A2.js
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
      - tmp2A
        - A3.js
        - __snapshots__
          - jsfmt.spec.js.snap
        - jsfmt.spec.js
    - record
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - refi
      - __snapshots__
        - jsfmt.spec.js.snap
      - bound.js
      - heap.js
      - jsfmt.spec.js
      - lex.js
      - local.js
      - null_tests.js
      - switch.js
      - typeof_tests.js
      - undef_tests.js
      - void_tests.js
    - refinements
      - __snapshots__
        - jsfmt.spec.js.snap
      - assignment.js
      - ast_node.js
      - bool.js
      - computed_string_literal.js
      - cond_prop.js
      - constants.js
      - eq.js
      - exists.js
      - func_call.js
      - hasOwnProperty.js
      - heap_defassign.js
      - jsfmt.spec.js
      - lib.js
      - missing-property-cond.js
      - mixed.js
      - node1.js
      - not.js
      - null.js
      - number.js
      - property.js
      - refinements.js
      - string.js
      - super_member.js
      - switch.js
      - tagged_union.js
      - tagged_union_import.js
      - typeof.js
      - undef.js
      - union.js
      - void.js
    - reflection
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - type.js
    - regexp
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - regexp.js
    - replace
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - test.js
    - require
      - B.js
      - C.js
      - E.js
      - ProvidesModuleA.js
      - ProvidesModuleD.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - not_builtin_require.js
      - not_builtin_require2.js
      - require.js
    - requireLazy
      - A.js
      - B.js
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js
      - requireLazy.js
    - rest
      - __snapshots__
        - jsfmt.spec.js.snap
      - jsfmt.spec.js

```

5. **Tool call: grep**
Input:
```json
{
  "pattern": "ExportDefaultSpecifier|ExportNamespaceSpecifier|ExportNamedDeclaration|exportKind",
  "searchPath": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361",
  "glob": [
    "*.js"
  ],
  "outputMode": "grouped",
  "headLimit": 300,
  "context": 3,
  "toolPurpose": "- Search local production and test code for export declaration/specifier handling so the semantic formatting defect can be traced without external sources."
}
```
Output:
```
{"success":true,"mode":"content","numFiles":3,"numLines":21,"pagination":{"offset":0,"limit":300,"returned":21,"total":21,"hasMore":false},"matchesByFile":{"src/printer.js":[{"file":"src/printer.js","line":375,"content":"case \"ExportNamedDeclaration\":","contextBefore":[{"line":372,"content":"return path.call(print, \"id\");"},{"line":373,"content":"case \"ExportDeclaration\":"},{"line":374,"content":"case \"ExportDefaultDeclaration\":"}],"contextAfter":[{"line":376,"content":"return printExportDeclaration(path, options, print);"},{"line":377,"content":"case \"ExportAllDeclaration\":"},{"line":378,"content":"parts.push(\"export *\");"}],"matches":["ExportNamedDeclaration"]},{"file":"src/printer.js","line":387,"content":"case \"ExportNamespaceSpecifier\":","contextBefore":[{"line":384,"content":"parts.push(\" from \", path.call(print, \"source\"), \";\");"},{"line":385,"content":""},{"line":386,"content":"return concat(parts);"}],"contextAfter":[{"line":388,"content":"return concat([ \"* as \", path.call(print, \"exported\") ]);"}],"matches":["ExportNamespaceSpecifier"]},{"file":"src/printer.js","line":389,"content":"case \"ExportDefaultSpecifier\":","contextBefore":[{"line":388,"content":"return concat([ \"* as \", path.call(print, \"exported\") ]);"}],"contextAfter":[{"line":390,"content":"return path.call(print, \"exported\");"},{"line":391,"content":"case \"ImportDeclaration\":"},{"line":392,"content":"parts.push(\"import \");"}],"matches":["ExportDefaultSpecifier"]},{"file":"src/printer.js","line":1845,"content":"decl.exportKind === \"type\" ? \"type \" : \"\",","contextBefore":[{"line":1842,"content":"parts.push(\"*\");"},{"line":1843,"content":"} else {"},{"line":1844,"content":"parts.push("}],"contextAfter":[{"line":1846,"content":"multilineGroup("},{"line":1847,"content":"concat(["},{"line":1848,"content":"\"{\","}],"matches":["exportKind"]}],"src/util.js":[{"file":"src/util.js","line":61,"content":"case \"ExportDefaultSpecifier\":","contextBefore":[{"line":58,"content":"if (node) switch (node.type) {"},{"line":59,"content":"case \"ExportDeclaration\":"},{"line":60,"content":"case \"ExportDefaultDeclaration\":"}],"contextAfter":[{"line":62,"content":"case \"DeclareExportDeclaration\":"}],"matches":["ExportDefaultSpecifier"]},{"file":"src/util.js","line":63,"content":"case \"ExportNamedDeclaration\":","contextBefore":[{"line":62,"content":"case \"DeclareExportDeclaration\":"}],"contextAfter":[{"line":64,"content":"case \"ExportAllDeclaration\":"},{"line":65,"content":"return true;"},{"line":66,"content":"}"}],"matches":["ExportNamedDeclaration"]}],"tests/type-printer/types.js":[{"file":"tests/type-printer/types.js","line":1670,"content":"type: 'ExportNamedDeclaration';","contextBefore":[{"line":1667,"content":"start: number;"},{"line":1668,"content":"trailingComments: ?Array;"},{"line":1669,"content":"} | {"}],"matches":["ExportNamedDeclaration"]},{"file":"tests/type-printer/types.js","line":1671,"content":"_ExportNamedDeclaration: void;","contextAfter":[{"line":1672,"content":"declaration: Node;"},{"line":1673,"content":"source: Literal;"},{"line":1674,"content":"specifiers: Array;"}],"matches":["ExportNamedDeclaration"]},{"file":"tests/type-printer/types.js","line":1685,"content":"type: 'ExportDefaultSpecifier';","contextBefore":[{"line":1682,"content":"start: number;"},{"line":1683,"content":"trailingComments: ?Array;"},{"line":1684,"content":"} | {"}],"matches":["ExportDefaultSpecifier"]},{"file":"tests/type-printer/types.js","line":1686,"content":"_ExportDefaultSpecifier: void;","contextAfter":[{"line":1687,"content":"exported: Node;"},{"line":1688,"content":"end: number;"},{"line":1689,"content":"innerComments: ?Array;"}],"matches":["ExportDefaultSpecifier"]},{"file":"tests/type-printer/types.js","line":1698,"content":"type: 'ExportNamespaceSpecifier';","contextBefore":[{"line":1695,"content":"start: number;"},{"line":1696,"content":"trailingComments: ?Array;"},{"line":1697,"content":"} | {"}],"matches":["ExportNamespaceSpecifier"]},{"file":"tests/type-printer/types.js","line":1699,"content":"_ExportNamespaceSpecifier: void;","contextAfter":[{"line":1700,"content":"exported: Node;"},{"line":1701,"content":"end: number;"},{"line":1702,"content":"innerComments: ?Array;"}],"matches":["ExportNamespaceSpecifier"]},{"file":"tests/type-printer/types.js","line":4253,"content":"export type ExportNamedDeclaration = {","contextBefore":[{"line":4250,"content":"};"},{"line":4251,"content":""},{"line":4252,"content":"// TODO: Make this correct."}],"matches":["ExportNamedDeclaration"]},{"file":"tests/type-printer/types.js","line":4254,"content":"type: 'ExportNamedDeclaration';","matches":["ExportNamedDeclaration"]},{"file":"tests/type-printer/types.js","line":4255,"content":"_ExportNamedDeclaration: void;","contextAfter":[{"line":4256,"content":"declaration: Node;"},{"line":4257,"content":"source: Literal;"},{"line":4258,"content":"specifiers: Array;"}],"matches":["ExportNamedDeclaration"]},{"file":"tests/type-printer/types.js","line":4271,"content":"export type ExportDefaultSpecifier = {","contextBefore":[{"line":4268,"content":"};"},{"line":4269,"content":""},{"line":4270,"content":"// TODO: Make this correct."}],"matches":["ExportDefaultSpecifier"]},{"file":"tests/type-printer/types.js","line":4272,"content":"type: 'ExportDefaultSpecifier';","matches":["ExportDefaultSpecifier"]},{"file":"tests/type-printer/types.js","line":4273,"content":"_ExportDefaultSpecifier: void;","contextAfter":[{"line":4274,"content":"exported: Node;"},{"line":4275,"content":"end: number;"},{"line":4276,"content":"innerComments: ?Array;"}],"matches":["ExportDefaultSpecifier"]},{"file":"tests/type-printer/types.js","line":4287,"content":"export type ExportNamespaceSpecifier = {","contextBefore":[{"line":4284,"content":"};"},{"line":4285,"content":""},{"line":4286,"content":"// TODO: Make this correct."}],"matches":["ExportNamespaceSpecifier"]},{"file":"tests/type-printer/types.js","line":4288,"content":"type: 'ExportNamespaceSpecifier';","matches":["ExportNamespaceSpecifier"]},{"file":"tests/type-printer/types.js","line":4289,"content":"_ExportNamespaceSpecifier: void;","contextAfter":[{"line":4290,"content":"exported: Node;"},{"line":4291,"content":"end: number;"},{"line":4292,"content":"innerComments: ?Array;"}],"matches":["ExportNamespaceSpecifier"]}]}}
```

6. **Tool call: register_tools**
Input:
```json
{
  "tool_names": [
    "get_available_terminals"
  ],
  "toolPurpose": "- Determine the configured local terminal profile before running repository-only Git and test commands in the isolated workspace."
}
```
Output:
```
Tools [get_available_terminals] are now registered and immediately available for usage.
```

7. **Tool call: get_available_terminals**
Input:
```json
{
  "toolPurpose": "- Identify the available macOS terminal profile so all subsequent local validation commands use the repository environment correctly."
}
```
Output:
```
Available terminal profiles: bash, zsh, fish, tmux, pwsh. Default profile for darwin: null.
```

8. **Tool call: read_file**
Input:
```json
{
  "fileNames": [
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361/src/printer.js",
      "startLine": 1
    },
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361/src/parser.js",
      "startLine": 1
    },
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361/package.json",
      "startLine": 1
    },
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361/index.js",
      "startLine": 1
    }
  ],
  "toolPurpose": "- Read the formatter's export printer, parser setup, public API, and package scripts to define the implementation contract and available local checks."
}
```

9. **Tool call: read_file**
Input:
```json
{
  "fileNames": [
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361/tests/es6modules/es6modules.js",
      "startLine": 1
    },
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361/tests/export/bracket.js",
      "startLine": 1
    },
    {
      "fileName": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361/tests/prettier/exports.js",
      "startLine": 1
    }
  ],
  "toolPurpose": "- Inspect existing export-related fixtures as the behavioral contract without modifying or including test files in the requested patch."
}
```

10. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git --no-pager status --short --branch",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git --no-pager log -1 --oneline",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "/Users/sankanum1/.slingshot/bin/rtk git remote -v",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- Verify the isolated repository is clean, at the specified base commit, and has no remotes before making local changes."
}
```

11. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "git --no-pager status --short --branch",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "git --no-pager log -1 --format=%H",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- Retry the blocked local Git verification without the unsupported command proxy, limited strictly to the isolated repository and with no network access."
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
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc 'git --no-pager status --short --branch'
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
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc 'git --no-pager log -1 --format=%H'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
237e6f44bc75269b96b31541c4a06ad293a591dd
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

```

12. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "node -  ({type, exported: exported && exported.name, local: local && local.name}))));\n  } catch (error) {\n    console.log(code + ' -> ERROR: ' + error.message);\n  }\n}\nNODE",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "node -  ({type, exported: exported && exported.name, local: local && local.name}))));
  } catch (error) {
    console.log(code + '"'"' -> ERROR: '"'"' + error.message);
  }
}
NODE'
Status: ERROR
─────────────────────────────────────────────────────────────────────────
Output:
Command failed with exit code 1.

--- Full Output ---
node:internal/modules/cjs/loader:1573
  throw err;
  ^

Error: Cannot find module 'babylon'
Require stack:
- /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361/[stdin]
    at Module._resolveFilename (node:internal/modules/cjs/loader:1569:15)
    at wrapResolveFilename (node:internal/modules/cjs/loader:1123:27)
    at defaultResolveImplForCJSLoading (node:internal/modules/cjs/loader:1147:10)
    at resolveForCJSWithHooks (node:internal/modules/cjs/loader:1174:12)
    at Module._load (node:internal/modules/cjs/loader:1346:5)
    at wrapModuleLoad (node:internal/modules/cjs/loader:261:19)
    at Module.require (node:internal/modules/cjs/loader:1679:12)
    at require (node:internal/modules/helpers:196:16)
    at [stdin]:1:17
    at runScriptInThisContext (node:internal/vm:219:10) {
  code: 'MODULE_NOT_FOUND',
  requireStack: [
    '/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361/[stdin]'
  ]
}

Node.js v26.8.1
__CMD_FINISHED__ 1
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 2 of 2                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc 'node -  (/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361/src/comments.js:2:13)
    at Module._compile (node:internal/modules/cjs/loader:1934:14) {
  code: 'MODULE_NOT_FOUND',
  requireStack: [
    '/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361/src/comments.js',
    '/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361/index.js',
    '/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361/[stdin]'
  ]
}

Node.js v26.8.1
__CMD_FINISHED__ 1
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

```

13. **Tool call: edit_file**
Input:
```json
{
  "operations": [
    {
      "filePath": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361/src/printer.js",
      "originalContent": "function printExportDeclaration(path, options, print) {\n  var decl = path.getValue();\n  var parts = [ \"export \" ];\n\n  namedTypes.Declaration.assert(decl);\n\n  if (decl[\"default\"] || decl.type === \"ExportDefaultDeclaration\") {\n    parts.push(\"default \");\n  }\n\n  if (decl.declaration) {\n    parts.push(path.call(print, \"declaration\"));\n\n    if (\n      decl.type === \"ExportDefaultDeclaration\" &&\n        (decl.declaration.type !== \"ClassDeclaration\" &&\n          decl.declaration.type !== \"FunctionDeclaration\" &&\n          decl.declaration.type !== \"FunctionExpression\")\n    ) {\n      parts.push(\";\");\n    }\n  } else {\n    if (decl.specifiers && decl.specifiers.length > 0) {\n      if (\n        decl.specifiers.length === 1 &&\n          decl.specifiers[0].type === \"ExportBatchSpecifier\"\n      ) {\n        parts.push(\"*\");\n      } else {\n        parts.push(\n          decl.exportKind === \"type\" ? \"type \" : \"\",\n          multilineGroup(\n            concat([\n              \"{\",\n              indent(\n                options.tabWidth,\n                concat([\n                  options.bracketSpacing ? line : softline,\n                  join(concat([ \",\", line ]), path.map(print, \"specifiers\"))\n                ])\n              ),\n              ifBreak(options.trailingComma ? \",\" : \"\"),\n              options.bracketSpacing ? line : softline,\n              \"}\"\n            ])\n          )\n        );\n      }\n    } else {\n      parts.push(\"{}\");\n    }\n\n    if (decl.source) {\n      parts.push(\" from \", path.call(print, \"source\"));\n    }\n\n    parts.push(\";\");\n  }\n\n  return concat(parts);\n}\n\nfunction printFlowDeclaration(path, parts) {\n  var parentExportDecl = util.getParentExportDeclaration(path);\n\n  if (parentExportDecl) {\n    assert.strictEqual(parentExportDecl.type, \"DeclareExportDeclaration\");\n  } else {\n    // If the parent node has type DeclareExportDeclaration, then it\n    // will be responsible for printing the \"declare\" token. Otherwise\n    // it needs to be printed with this non-exported declaration node.\n    parts.unshift(\"declare \");\n  }\n\n  return concat(parts);\n}",
      "newContent": "function printExportDeclaration(path, options, print) {\n  var decl = path.getValue();\n  var parts = [ \"export \" ];\n\n  namedTypes.Declaration.assert(decl);\n\n  if (decl[\"default\"] || decl.type === \"ExportDefaultDeclaration\") {\n    parts.push(\"default \");\n  }\n\n  if (decl.declaration) {\n    parts.push(path.call(print, \"declaration\"));\n\n    if (\n      decl.type === \"ExportDefaultDeclaration\" &&\n        (decl.declaration.type !== \"ClassDeclaration\" &&\n          decl.declaration.type !== \"FunctionDeclaration\" &&\n          decl.declaration.type !== \"FunctionExpression\")\n    ) {\n      parts.push(\";\");\n    }\n  } else {\n    if (decl.specifiers && decl.specifiers.length > 0) {\n      if (\n        decl.specifiers.length === 1 &&\n          decl.specifiers[0].type === \"ExportBatchSpecifier\"\n      ) {\n        parts.push(\"*\");\n      } else {\n        var standalones = [];\n        var grouped = [];\n\n        path.each(\n          function(specifierPath) {\n            var specifier = specifierPath.getValue();\n            if (\n              specifier.type === \"ExportDefaultSpecifier\" ||\n                specifier.type === \"ExportNamespaceSpecifier\"\n            ) {\n              standalones.push(print(specifierPath));\n            } else {\n              grouped.push(print(specifierPath));\n            }\n          },\n          \"specifiers\"\n        );\n\n        if (standalones.length > 0) {\n          parts.push(join(\", \", standalones));\n        }\n\n        if (standalones.length > 0 && grouped.length > 0) {\n          parts.push(\", \");\n        }\n\n        if (grouped.length > 0) {\n          parts.push(\n            decl.exportKind === \"type\" ? \"type \" : \"\",\n            multilineGroup(\n              concat([\n                \"{\",\n                indent(\n                  options.tabWidth,\n                  concat([\n                    options.bracketSpacing ? line : softline,\n                    join(concat([ \",\", line ]), grouped)\n                  ])\n                ),\n                ifBreak(options.trailingComma ? \",\" : \"\"),\n                options.bracketSpacing ? line : softline,\n                \"}\"\n              ])\n            )\n          );\n        }\n      }\n    } else {\n      parts.push(\"{}\");\n    }\n\n    if (decl.source) {\n      parts.push(\" from \", path.call(print, \"source\"));\n    }\n\n    parts.push(\";\");\n  }\n\n  return concat(parts);\n}\n\nfunction printFlowDeclaration(path, parts) {\n  var parentExportDecl = util.getParentExportDeclaration(path);\n\n  if (parentExportDecl) {\n    assert.strictEqual(parentExportDecl.type, \"DeclareExportDeclaration\");\n  } else {\n    // If the parent node has type DeclareExportDeclaration, then it\n    // will be responsible for printing the \"declare\" token. Otherwise\n    // it needs to be printed with this non-exported declaration node.\n    parts.unshift(\"declare \");\n  }\n\n  return concat(parts);\n}"
    }
  ],
  "toolPurpose": "- Update export declaration printing so default and namespace export-extension specifiers remain standalone instead of being wrapped in semantic-changing braces, while preserving grouped named exports.",
  "references": {
    "hasJiraContext": false,
    "hasFigmaContext": false
  }
}
```
Output:
```
Successfully replaced content in file Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361/src/printer.js
```

14. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "node --check src/printer.js",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "git --no-pager diff --check",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "git --no-pager diff --stat && git --no-pager diff --name-only && git --no-pager diff -- src/printer.js",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    },
    {
      "command": "npm test -- --runInBand",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361",
      "profileName": "zsh",
      "readTerminalFullOutput": false,
      "timeoutMs": 120000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- Validate syntax and whitespace, inspect the complete production-only diff, and attempt the repository's local test suite without network access."
}
```
Output:
```
I ran all provided commands and below are the outcomes for each command with their status. Please analyze each output carefully and run the commands again for which you see errors to get their output by correcting the command and other parameters.

=== EXECUTION SUMMARY ===
Total Commands: 4
Number of Successful Commands: 3
Number of Failed Commands: 1
Number of Timed Out Commands: 0
========================

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 1 of 4                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc 'node --check src/printer.js'
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
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc 'git --no-pager diff --check'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 3 of 4                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc 'git --no-pager diff --stat && git --no-pager diff --name-only && git --no-pager diff -- src/printer.js'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
src/printer.js | 62 ++++++++++++++++++++++++++++++++++++++++++----------------
 1 file changed, 45 insertions(+), 17 deletions(-)
src/printer.js
diff --git a/src/printer.js b/src/printer.js
index 2468bbd..fff8ca5 100644
--- a/src/printer.js
+++ b/src/printer.js
@@ -1841,24 +1841,52 @@ function printExportDeclaration(path, options, print) {
       ) {
         parts.push("*");
       } else {
-        parts.push(
-          decl.exportKind === "type" ? "type " : "",
-          multilineGroup(
-            concat([
-              "{",
-              indent(
-                options.tabWidth,
-                concat([
-                  options.bracketSpacing ? line : softline,
-                  join(concat([ ",", line ]), path.map(print, "specifiers"))
-                ])
-              ),
-              ifBreak(options.trailingComma ? "," : ""),
-              options.bracketSpacing ? line : softline,
-              "}"
-            ])
-          )
+        var standalones = [];
+        var grouped = [];
+
+        path.each(
+          function(specifierPath) {
+            var specifier = specifierPath.getValue();
+            if (
+              specifier.type === "ExportDefaultSpecifier" ||
+                specifier.type === "ExportNamespaceSpecifier"
+            ) {
+              standalones.push(print(specifierPath));
+            } else {
+              grouped.push(print(specifierPath));
+            }
+          },
+          "specifiers"
         );
+
+        if (standalones.length > 0) {
+          parts.push(join(", ", standalones));
+        }
+
+        if (standalones.length > 0 && grouped.length > 0) {
+          parts.push(", ");
+        }
+
+        if (grouped.length > 0) {
+          parts.push(
+            decl.exportKind === "type" ? "type " : "",
+            multilineGroup(
+              concat([
+                "{",
+                indent(
+                  options.tabWidth,
+                  concat([
+                    options.bracketSpacing ? line : softline,
+                    join(concat([ ",", line ]), grouped)
+                  ])
+                ),
+                ifBreak(options.trailingComma ? "," : ""),
+                options.bracketSpacing ? line : softline,
+                "}"
+              ])
+            )
+          );
+        }
       }
     } else {
       parts.push("{}");
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════╗
║ COMMAND 4 of 4                                                        ║
╚══════════════════════════════════════════════════════════════════════╝
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc 'npm test -- --runInBand'
Status: ERROR
─────────────────────────────────────────────────────────────────────────
Output:
Command failed with exit code 127.

--- Output (last 5 lines, 91 chars) ---
> prettier@0.0.10 test
> jest --runInBand

sh: jest: command not found
__CMD_FINISHED__ 127
--- End of Output ---
═════════════════════════════════════════════════════════════════════════

```

15. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "mkdir -p /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361",
      "profileName": "zsh",
      "readTerminalFullOutput": false,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- Create the benchmark's required local results directory before writing the patch artifact, without accessing any network resource."
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
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc 'mkdir -p /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Output (last 1 lines, 18 chars) ---
__CMD_FINISHED__ 0
--- End of Output ---
═════════════════════════════════════════════════════════════════════════

```

16. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "git --no-pager diff --binary -- src/printer.js > /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/prettier__prettier-361.patch",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361",
      "profileName": "zsh",
      "readTerminalFullOutput": false,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- Generate the requested patch directly from the isolated repository's Git diff, restricted to the modified production formatter source."
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
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc 'git --no-pager diff --binary -- src/printer.js > /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/prettier__prettier-361.patch'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Output (last 1 lines, 18 chars) ---
__CMD_FINISHED__ 0
--- End of Output ---
═════════════════════════════════════════════════════════════════════════

```

17. **Tool call: run_terminal_command**
Input:
```json
{
  "commands": [
    {
      "command": "set -e\npatch=/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/prettier__prettier-361.patch\ntest -s \"$patch\"\ngit apply --check --reverse \"$patch\"\nprintf '%s\\n' 'Patch files:'\ngit apply --numstat \"$patch\"\nprintf '%s\\n' 'Patch headers:'\ngrep '^diff --git ' \"$patch\"\nif grep '^diff --git ' \"$patch\" | grep -E '(^|[ /])(tests?|__tests__|__snapshots__|fixtures?|coverage|artifacts?)([ /]|$)'; then\n  echo 'ERROR: test file or test artifact found in patch' >&2\n  exit 1\nfi\ncurrent_diff=$(mktemp)\ngit --no-pager diff --binary -- src/printer.js > \"$current_diff\"\ncmp \"$current_diff\" \"$patch\"\nrm \"$current_diff\"\nshasum -a 256 \"$patch\"\ngit --no-pager status --short",
      "cwd": "/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/prettier__prettier-361",
      "profileName": "zsh",
      "readTerminalFullOutput": true,
      "timeoutMs": 30000,
      "isInteractive": false
    }
  ],
  "toolPurpose": "- Verify the patch is non-empty, reversibly applies to the modified tree, exactly matches the current Git diff, and contains only the production file with no tests, snapshots, fixtures, coverage, or other test artifacts."
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
Command: /usr/bin/sandbox-exec -p '(version 1) (allow default) (deny network*)' /bin/zsh -lc 'set -e
patch=/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/prettier__prettier-361.patch
test -s "$patch"
git apply --check --reverse "$patch"
printf '"'"'%s\n'"'"' '"'"'Patch files:'"'"'
git apply --numstat "$patch"
printf '"'"'%s\n'"'"' '"'"'Patch headers:'"'"'
grep '"'"'^diff --git '"'"' "$patch"
if grep '"'"'^diff --git '"'"' "$patch" | grep -E '"'"'(^|[ /])(tests?|__tests__|__snapshots__|fixtures?|coverage|artifacts?)([ /]|$)'"'"'; then
  echo '"'"'ERROR: test file or test artifact found in patch'"'"' >&2
  exit 1
fi
current_diff=$(mktemp)
git --no-pager diff --binary -- src/printer.js > "$current_diff"
cmp "$current_diff" "$patch"
rm "$current_diff"
shasum -a 256 "$patch"
git --no-pager status --short'
Status: SUCCESS
─────────────────────────────────────────────────────────────────────────
Output:
Command success.

--- Full Output ---
Patch files:
45	17	src/printer.js
Patch headers:
diff --git a/src/printer.js b/src/printer.js
da77f06d82db516e676487ee7ec1fbacfb4c9a1269a1abda4c1439dde762d46f  /Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/prettier__prettier-361.patch
 M src/printer.js
__CMD_FINISHED__ 0
--- End of Full Output ---
═════════════════════════════════════════════════════════════════════════

```

18. **Tool call: add_agent_memory**
Input:
```json
{
  "memories": [
    {
      "content": "Prettier 0.0.10 must print ExportDefaultSpecifier and ExportNamespaceSpecifier outside braces to preserve export-extension semantics.",
      "scope": "workspace"
    },
    {
      "content": "This Prettier workspace has no node_modules; Jest and formatter smoke tests are blocked by missing local dependencies.",
      "scope": "workspace"
    }
  ],
  "toolPurpose": "- Save concise project-specific formatter and validation constraints discovered during this completed fix so future work in the same workspace avoids repeating the analysis."
}
```
Output:
```
Processed 2 memory item(s): 2 stored, 0 skipped (duplicates), 0 failed.
```

## Final Response

## Summary

Fixed export-extension formatting so standalone default and namespace specifiers are not wrapped in braces, preserving statement semantics.

## 📝 Files Modified

- [printer.js](src/printer.js) — Separates standalone export specifiers from grouped named exports. **+45 −17 lines**

## 📁 Files Created

- [prettier__prettier-361.patch](/Users/sankanum1/Documents/SWEPolyBenchRuns/R2VerifiedGPT5.6Sol/running-env/swe-results/prettier__prettier-361.patch) — Generated and verified Git patch. **+74 −0 lines**

## Validation

- JavaScript syntax check: passed
- Git whitespace check: passed
- Patch reverse-apply check: passed
- Patch exactly matches the current Git diff
- Patch contains only `src/printer.js`; no tests or test artifacts
- Jest could not run because dependencies are not installed (`jest: command not found`)

---
