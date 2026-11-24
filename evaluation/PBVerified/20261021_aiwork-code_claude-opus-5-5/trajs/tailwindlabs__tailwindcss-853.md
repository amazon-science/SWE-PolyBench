# Instance: tailwindlabs__tailwindcss-853
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: True

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
Ability to only enable specific core plugins
Right now you can disable all core plugins with `corePlugins: false` (thank you @adamwathan!) but [as Adam said](https://github.com/tailwindcss/tailwindcss/issues/833#issuecomment-484162018), it would be useful to have a "whitelisting" option to only enable one or a few core plugins in particular, without worrying that a Tailwind update might change the code's behaviour by introducing new core plugins.

An idea, perhaps the `corePlugins` option could take accept an object formatted like this:
```
corePlugins: {
    only: [
        'backgroundColor',
        'textColor',
    ],
}
```
````

## Operational trajectory

### Turn 1 — tool call call_0001 (exec)

````json
{
 "command": "cat src/util/configurePlugins.js; grep -rn \"configurePlugins\\|corePlugins\" src | head -30"
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
 "stdout": "export default function(pluginConfig, plugins) {\n  return Object.keys(plugins)\n    .filter(pluginName => {\n      return pluginConfig !== false && pluginConfig[pluginName] !== false\n    })\n    .map(pluginName => {\n      return plugins[pluginName]()\n    })\n}\nsrc/corePlugins.js:68:import configurePlugins from './util/configurePlugins'\nsrc/corePlugins.js:70:export default function({ corePlugins: corePluginConfig }) {\nsrc/corePlugins.js:71:  return configurePlugins(corePluginConfig, {\nsrc/processTailwindFeatures.js:11:import corePlugins from './corePlugins'\nsrc/processTailwindFeatures.js:17:    const processedPlugins = processPlugins([...corePlugins(config), ...config.plugins], config)\n",
 "device_targets": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "src",
   "src/util/configurePlugins.js"
  ],
  "command_sha256": [
   "a99e9c6c4c13c5dc3c691fcc9f5f1d2a6a3024962e8536a988f390e9fcd19dbf"
  ]
 },
 "duration_ms": 55
}
````

### Turn 2 — thinking

````text
I should check the tests for expected behavior here, and consider whether corePlugins can be an array form, then look at how resolveConfig merges corePlugins with the defaults.
````

### Turn 2 — tool call call_0002 (exec)

````json
{
 "command": "cat __tests__/configurePlugins.test.js 2>/dev/null; grep -n \"corePlugins\" -r src stubs __tests__ | head -30; git log --oneline | head -5"
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
 "stdout": "import configurePlugins from '../src/util/configurePlugins'\n\ntest('setting a plugin to false removes it', () => {\n  const plugins = {\n    fontSize: () => 'fontSize',\n    display: () => 'display',\n    backgroundPosition: () => 'backgroundPosition',\n  }\n\n  const configuredPlugins = configurePlugins(\n    {\n      display: false,\n    },\n    plugins\n  )\n\n  expect(configuredPlugins).toEqual(['fontSize', 'backgroundPosition'])\n})\n\ntest('passing only false removes all plugins', () => {\n  const plugins = {\n    fontSize: () => 'fontSize',\n    display: () => 'display',\n    backgroundPosition: () => 'backgroundPosition',\n  }\n\n  const configuredPlugins = configurePlugins(false, plugins)\n\n  expect(configuredPlugins).toEqual([])\n})\nsrc/corePlugins.js:70:export default function({ corePlugins: corePluginConfig }) {\nsrc/processTailwindFeatures.js:11:import corePlugins from './corePlugins'\nsrc/processTailwindFeatures.js:17:    const processedPlugins = processPlugins([...corePlugins(config), ...config.plugins], config)\nstubs/defaultConfig.stub.js:444:  corePlugins: {},\n__tests__/applyAtRule.test.js:5:import corePlugins from '../src/corePlugins'\n__tests__/applyAtRule.test.js:11:  corePlugins(resolvedDefaultConfig),\n__tests__/applyAtRule.test.js:216:  return run(input, config, processPlugins(corePlugins(config), config).utilities).then(result => {\n__tests__/applyAtRule.test.js:240:  return run(input, config, processPlugins(corePlugins(config), config).utilities).then(result => {\ndaea662 Merge pull request #852 from tailwindcss/global-variants\nf0bc35a Support configuring a single list of variants to apply to all relevant plugins\n43f63bf Merge pull request #849 from tailwindcss/disable-all-core-plugins\n27cef23 Support disabling all corePlugins with corePlugins: false\n4f58205 Merge pull request #847 from tailwindcss/remove-perfectionist-dependency\n",
 "duration_ms": 60,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "__tests__",
   "__tests__/configurePlugins.test.js",
   "src",
   "stubs"
  ],
  "command_sha256": [
   "d8935b321513061692de225c0dbe5e924f2feabb829561de48e2297e00606037"
  ]
 },
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "failed",
  "exit_code": 141,
  "failure_class": "unknown",
  "retryability": "retry_after_change",
  "open_work_at_failure": false
 },
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "device_targets": []
}
````

### Turn 3 — thinking

````text
I'm recalling how the original Tailwind v1.0 configurePlugins function handled the corePlugins option, checking whether it accepted an array as a whitelist of plugin names versus other config shapes.
````

### Turn 3 — tool call call_0003 (exec)

````json
{
 "command": "cat src/util/resolveConfig.js | head -80"
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
 "stdout": "import mergeWith from 'lodash/mergeWith'\nimport isFunction from 'lodash/isFunction'\nimport defaults from 'lodash/defaults'\nimport map from 'lodash/map'\nimport get from 'lodash/get'\n\nfunction value(valueToResolve, ...args) {\n  return isFunction(valueToResolve) ? valueToResolve(...args) : valueToResolve\n}\n\nfunction mergeExtensions({ extend, ...theme }) {\n  return mergeWith(theme, extend, (themeValue, extensions) => {\n    if (!isFunction(themeValue) && !isFunction(extensions)) {\n      return {\n        ...themeValue,\n        ...extensions,\n      }\n    }\n\n    return resolveThemePath => ({\n      ...value(themeValue, resolveThemePath),\n      ...value(extensions, resolveThemePath),\n    })\n  })\n}\n\nfunction resolveFunctionKeys(object) {\n  const resolveObjectPath = (key, defaultValue) => {\n    const val = get(object, key, defaultValue)\n    return isFunction(val) ? val(resolveObjectPath) : val\n  }\n\n  return Object.keys(object).reduce((resolved, key) => {\n    return {\n      ...resolved,\n      [key]: isFunction(object[key]) ? object[key](resolveObjectPath) : object[key],\n    }\n  }, {})\n}\n\nexport default function resolveConfig(configs) {\n  return defaults(\n    {\n      theme: resolveFunctionKeys(mergeExtensions(defaults({}, ...map(configs, 'theme')))),\n      variants: defaults({}, ...map(configs, 'variants')),\n    },\n    ...configs\n  )\n}\n",
 "device_targets": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "src/util/resolveConfig.js"
  ],
  "command_sha256": [
   "00686177f75e14e44e093b5471b1d1755651d8f440b0a0f1cd208f2e17951d18"
  ]
 },
 "duration_ms": 39
}
````

### Turn 4 — assistant text

Top-level `defaults` keeps the user's value as-is, so an array passes through. I'll support both an array whitelist and `{ only: [...] }`.

### Turn 4 — tool call call_0004 (write)

````json
{
 "file_path": "src/util/configurePlugins.js",
 "content": "export default function(pluginConfig, plugins) {\n  const whitelist = Array.isArray(pluginConfig)\n    ? pluginConfig\n    : pluginConfig && Array.isArray(pluginConfig.only)\n    ? pluginConfig.only\n    : null\n\n  if (whitelist !== null) {\n    return whitelist\n      .filter(pluginName => plugins[pluginName] !== undefined)\n      .map(pluginName => plugins[pluginName]())\n  }\n\n  return Object.keys(plugins)\n    .filter(pluginName => {\n      return pluginConfig !== false && pluginConfig[pluginName] !== false\n    })\n    .map(pluginName => {\n      return plugins[pluginName]()\n    })\n}\n"
}
````

Result:

````text
{
 "success": false,
 "error": {
  "code": "tool_execution_failed",
  "message": "agent error: File 'src/util/configurePlugins.js' already exists (257 bytes). No complete read of this file exists in this session. Call read without offset/limit first, then retry write; or use edit/apply_patch for a targeted change. No bytes were written. Content preview:\n```\nexport default function(pluginConfig, plugins) {\n  return Object.keys(plugins)\n    .filter(pluginName => {\n      return pluginConfig !== false && pluginConfig[pluginName] !== false\n    })\n    .map(plu...\n```"
 },
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "write",
  "status": "failed",
  "failure_class": "unknown",
  "retryability": "retry_after_change",
  "open_work_at_failure": true,
  "evidence_tail": "agent error: File 'src/util/configurePlugins.js' already exists (257 bytes). No complete read of this file exists in this session. Call read without offset/lim…"
 },
 "guidance": "inspect error.message and tool_outcome; change inputs or stop if nonrecoverable"
}
````

### Turn 5 — tool call call_0005 (edit)

````json
{
 "file_path": "src/util/configurePlugins.js",
 "old_string": "export default function(pluginConfig, plugins) {\n  return Object.keys(plugins)",
 "new_string": "export default function(pluginConfig, plugins) {\n  const whitelist = Array.isArray(pluginConfig)\n    ? pluginConfig\n    : pluginConfig && Array.isArray(pluginConfig.only)\n    ? pluginConfig.only\n    : null\n\n  if (whitelist !== null) {\n    return whitelist\n      .filter(pluginName => plugins[pluginName] !== undefined)\n      .map(pluginName => plugins[pluginName]())\n  }\n\n  return Object.keys(plugins)"
}
````

Result:

````text
{
 "path": "src/util/configurePlugins.js",
 "edited": true,
 "replacements": 1,
 "total_file_lines": 21,
 "total_file_size_bytes": 580,
 "diff": "+   const whitelist = Array.isArray(pluginConfig)\n+     ? pluginConfig\n+     : pluginConfig && Array.isArray(pluginConfig.only)\n+     ? pluginConfig.only\n+     : null\n+ \n+   if (whitelist !== null) {\n+     return whitelist\n+       .filter(pluginName => plugins[pluginName] !== undefined)\n+       .map(pluginName => plugins[pluginName]())\n+   }\n+ ",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "edit",
    "paths": [
     "src/util/configurePlugins.js"
    ]
   }
  ]
 },
 "file_change": {
  "kind": "diff",
  "operation": "update",
  "path": "src/util/configurePlugins.js",
  "patch": "+   const whitelist = Array.isArray(pluginConfig)\n+     ? pluginConfig\n+     : pluginConfig && Array.isArray(pluginConfig.only)\n+     ? pluginConfig.only\n+     : null\n+ \n+   if (whitelist !== null) {\n+     return whitelist\n+       .filter(pluginName => plugins[pluginName] !== undefined)\n+       .map(pluginName => plugins[pluginName]())\n+   }\n+ ",
  "additions": 12,
  "deletions": 0,
  "truncated": false,
  "omitted_lines": 0
 }
}
````

### Turn 6 — tool call call_0006 (exec)

````json
{
 "command": "cat > /tmp/t.test.js <<'EOF'\nimport c from '../src/util/configurePlugins'\nconst p = { a: () => 'a', b: () => 'b', d: () => 'd' }\ntest('x', () => {\n  expect(c(['d','a'], p)).toEqual(['d','a'])\n  expect(c({only:['b']}, p)).toEqual(['b'])\n  expect(c({a:false}, p)).toEqual(['b','d'])\n  expect(c(false, p)).toEqual([])\n})\nEOF\ncp /tmp/t.test.js __tests__/zztmp.test.js && npx jest __tests__/zztmp.test.js __tests__/configurePlugins.test.js 2>&1 | tail -8; rm __tests__/zztmp.test.js"
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
 "stdout": "PASS __tests__/zztmp.test.js\nPASS __tests__/configurePlugins.test.js\n\nTest Suites: 2 passed, 2 total\nTests:       3 passed, 3 total\nSnapshots:   0 total\nTime:        3.706s\nRan all test suites matching /__tests__\\/zztmp.test.js|__tests__\\/configurePlugins.test.js/i.\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 6695,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "write",
    "paths": [
     "/tmp/t.test.js",
     "__tests__/zztmp.test.js"
    ]
   }
  ],
  "reads": [
   "/tmp/t.test.js"
  ],
  "command_sha256": [
   "5edc46cb851416c4e77c134747f5c665ec521b22bf1da215a21376a63f30ac88"
  ]
 }
}
````

### Turn 7 — thinking

````text
Let me run the full test suite quickly to verify everything passes.
````

### Turn 7 — tool call call_0007 (exec)

````json
{
 "command": "npx jest 2>&1 | tail -6; git status --short"
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
 "stdout": "\nTest Suites: 2 failed, 22 passed, 24 total\nTests:       2 failed, 145 passed, 147 total\nSnapshots:   0 total\nTime:        38.898s\nRan all test suites.\n M src/util/configurePlugins.js\n?? Dockerfile\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 40289,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [],
  "command_sha256": [
   "8d9494414ab7dd6a978ba164a0fb96870c554087e839fe843452a2fe87dfb70f"
  ]
 }
}
````

### Turn 8 — tool call call_0008 (exec)

````json
{
 "command": "npx jest 2>&1 | grep -E \"FAIL|●\" | head; git stash -q && npx jest 2>&1 | grep -E \"FAIL|Tests:\"; git stash pop -q"
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
 "stdout": "FAIL __tests__/cli.compile.test.js (18.326s)\n  ● Console\n  ● cli compile › compiles CSS file\nFAIL __tests__/cli.test.js (18.84s)\n  ● Console\n  ● cli › build › compiles CSS file with autoprefixer\nFAIL __tests__/cli.compile.test.js (18.326s)\n  ● cli compile › compiles CSS file\nFAIL __tests__/cli.test.js (18.84s)\n  ● cli › build › compiles CSS file with autoprefixer\n",
 "stderr": "\n*** Please tell me who you are.\n\nRun\n\n  git config --global user.email \"you@example.com\"\n  git config --global user.name \"Your Name\"\n\nto set your account's default identity.\nOmit --global to set the identity only in this repository.\n\nfatal: unable to auto-detect email address (got 'root@0d2c50cbdc0e.(none)')\nCannot save the current index state\nNo stash found.\n",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [],
  "command_sha256": [
   "0f9545e0213befa88cf2feb2e44f52a20c11bd7ebbc9353a98f4fd6a23d7a9ad"
  ]
 },
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "failed",
  "exit_code": 1,
  "failure_class": "unknown",
  "retryability": "retry_after_change",
  "open_work_at_failure": false,
  "evidence_tail": "\n*** Please tell me who you are.\n\nRun\n\n  git config --global user.email \"you@example.com\"\n  git config --global user.name \"Your Name\"\n\nto set your account's default identity.\nOmit --global to set the identity only in this repository.\n\nfatal: unable to auto-detect email address (got 'root@0d2c50cbdc0e.(none)')\nCannot save the current index state\nNo stash found.\n"
 },
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "device_targets": [],
 "duration_ms": 38811
}
````

### Turn 9 — tool call call_0009 (exec)

````json
{
 "command": "npx jest __tests__/cli.compile.test.js 2>&1 | grep -A15 \"● cli compile\" | head -30"
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
 "stdout": "  ● cli compile › compiles CSS file\n\n    expect(received).toContain(expected) // indexOf\n\n    Expected substring: \"-ms-input-placeholder\"\n    Received string:    \"/*! normalize.css v8.0.1 | MIT License | github.com/necolas/normalize.css */·\n    /* Document\n       ========================================================================== */·\n    /**\n     * 1. Correct the line height in all browsers.\n     * 2. Prevent adjustments of font size after orientation changes in iOS.\n     */·\n    html {\n      line-height: 1.15; /* 1 */\n      -webkit-text-size-adjust: 100%; /* 2 */\n    }·\n",
 "duration_ms": 4282,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [],
  "command_sha256": [
   "5295f78d4d110212e48a4a9f3bd1b50215b77319b66cea9c966e3409bf208142"
  ]
 },
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "failed",
  "exit_code": 1,
  "failure_class": "unknown",
  "retryability": "retry_after_change",
  "open_work_at_failure": false
 },
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "device_targets": []
}
````

### Turn 10 — thinking

````text
That autoprefixer/browserslist warning is just an environment quirk, unrelated to my change.
````

### Turn 11 — thinking

````text
The CLI failures seem unrelated to my change, stemming from autoprefixer's browserslist data instead. Since my stash attempt failed, I haven't actually confirmed this against the original code, so I'll verify by saving the diff to a file, checking out the original, and reapplying the diff afterward to restore my changes.
````

### Turn 11 — assistant text

I've changed `corePlugins` so you can list only the core plugins you want, and any new core plugins added in a Tailwind update stay off. There are two ways to write it:

```js
corePlugins: ['backgroundColor', 'textColor']
// or
corePlugins: { only: ['backgroundColor', 'textColor'] }
```

The only file changed is `src/util/configurePlugins.js`. Listed plugins are loaded in the order you write them, and names that don't match a core plugin are silently skipped. The existing forms work as before: `{ pluginName: false }` turns off one plugin, and `corePlugins: false` turns them all off. The rest of the config handling passes an array through unchanged, so nothing else needed editing.

**Tests:** I ran a temporary test covering the array form, the `{ only }` form, and both existing forms. It passed, and so did the existing `configurePlugins` tests; I deleted the temporary test file afterwards.

**Two failures in the full suite:** 145 of 147 tests pass. The two failures are CLI tests (`cli.compile.test.js` and `cli.test.js`) that expect autoprefixer's `-ms-input-placeholder` prefix in the output, and it's missing. That points to this environment's browser-target settings rather than to this change, which only affects which plugins load. I tried running the suite without my change to confirm, but `git stash` failed because no git user is configured here, so that comparison didn't happen.

### Turn 11 — tool call call_0010 (exec)

````json
{
 "command": "git diff > /tmp/fix.patch && git checkout src/util/configurePlugins.js && npx jest __tests__/cli.compile.test.js 2>&1 | grep -E \"Tests:\"; git apply /tmp/fix.patch && git status --short"
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
 "stdout": "Tests:       1 failed, 1 total\n M src/util/configurePlugins.js\n?? Dockerfile\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 5497,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "write",
    "paths": [
     "/tmp/fix.patch"
    ]
   }
  ],
  "reads": [],
  "command_sha256": [
   "cbf205cee3c2a860d5bdf776848f6459ac28659678cf11a3fbc57ddb8662b526"
  ]
 }
}
````

### Turn 12 — thinking

````text
I've worked through everything I need; time to put together the final answer.
````

### Turn 12 — assistant text

I added whitelist support to `corePlugins`, so you can now turn on only the core plugins you name. Any core plugins added in later releases stay off. Both of these forms work:

```js
corePlugins: ['backgroundColor', 'textColor']
// or
corePlugins: { only: ['backgroundColor', 'textColor'] }
```

The change is in `src/util/configurePlugins.js`. When it gets a list, it builds just those plugins, in the order you list them, and skips names it doesn't recognise. The existing settings work as before: `corePlugins: false` and `{ pluginName: false }`.

**Checks:**
- **New behaviour:** I wrote a throwaway test covering the array form, the `{ only }` form, and the two existing forms. It passed alongside the existing `configurePlugins` tests, and I deleted it afterwards.
- **Full suite:** 145 of 147 tests pass. The two failures are in `cli.compile.test.js` and `cli.test.js`, where the output lacks the expected `-ms-input-placeholder` prefix that autoprefixer normally adds. `cli.compile.test.js` also fails with my change removed, so that failure was already there. I didn't run `cli.test.js` without my change.

### Turn 13 — assistant text

You can now pass `corePlugins` a whitelist, so only the named core plugins are enabled. The change is in `src/util/configurePlugins.js` and nothing else was touched. The fix accepts two forms:

```js
corePlugins: ['backgroundColor', 'textColor']
// or
corePlugins: { only: ['backgroundColor', 'textColor'] }
```

With a whitelist, plugins load in the order you list them, and names that don't match a core plugin are skipped. Core plugins added in future Tailwind versions stay off unless you add them to the list. The existing forms still work as before: `corePlugins: false` disables everything, and `{ pluginName: false }` turns off a single plugin. No config resolution changes were needed, because the user's `corePlugins` value already reaches this function unchanged.

**Checks:**
- `__tests__/configurePlugins.test.js` passes.
- A throwaway test (since deleted) confirmed the array form, the `{ only }` form, turning one plugin off, and `false`.
- Full suite: 145 of 147 tests pass. The two failures are in `cli.compile.test.js` and `cli.test.js`: autoprefixer output doesn't contain the expected `-ms-input-placeholder` prefix. `cli.compile.test.js` fails the same way with my change temporarily reverted, so that failure was already there. I didn't re-run `cli.test.js` without my change, but it's the same autoprefixer check.

## Final answer

You can now pass `corePlugins` a whitelist, so only the named core plugins are enabled. The change is in `src/util/configurePlugins.js` and nothing else was touched. The fix accepts two forms:

```js
corePlugins: ['backgroundColor', 'textColor']
// or
corePlugins: { only: ['backgroundColor', 'textColor'] }
```

With a whitelist, plugins load in the order you list them, and names that don't match a core plugin are skipped. Core plugins added in future Tailwind versions stay off unless you add them to the list. The existing forms still work as before: `corePlugins: false` disables everything, and `{ pluginName: false }` turns off a single plugin. No config resolution changes were needed, because the user's `corePlugins` value already reaches this function unchanged.

**Checks:**
- `__tests__/configurePlugins.test.js` passes.
- A throwaway test (since deleted) confirmed the array form, the `{ only }` form, turning one plugin off, and `false`.
- Full suite: 145 of 147 tests pass. The two failures are in `cli.compile.test.js` and `cli.test.js`: autoprefixer output doesn't contain the expected `-ms-input-placeholder` prefix. `cli.compile.test.js` fails the same way with my change temporarily reverted, so that failure was already there. I didn't re-run `cli.test.js` without my change, but it's the same autoprefixer check.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 202741 | 3672 | 181262 | 21449 | 206413 |
