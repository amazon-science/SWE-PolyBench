# Instance: prettier__prettier-4667

- Final resolved (evaluator, logs/prettier__prettier-4667_result.json): True
- Run state: DONE
- One attempt. Duration 52.2 s, turns 12, actor cost $0.2235254, container commands 4
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/prettier__prettier-4667/repo
</uploaded_files>
I've uploaded a JavaScript code repository in the directory /work/prettier__prettier-4667/repo. Consider the following issue description:

<issue_description>
Support relative paths for plugin and pluginSearchDir in config files
Context: https://github.com/prettier/prettier/pull/4192#discussion_r186809767

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/prettier__prettier-4667/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/prettier__prettier-4667/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/prettier__prettier-4667/bin/envrun 'git status --short && ls'
Edits you make under /work/prettier__prettier-4667/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cat src/config/resolve-config.js && grep -rn "plugin" src/cli/util.js | head -50 && ls tests_integration/__tests__ | grep -i -E "plugin|config"
```

tool result:

```
"use strict";

const thirdParty = require("../common/third-party");
const minimatch = require("minimatch");
const path = require("path");
const mem = require("mem");

const resolveEditorConfig = require("./resolve-config-editorconfig");

const getExplorerMemoized = mem(opts =>
  thirdParty.cosmiconfig("prettier", {
    sync: opts.sync,
    cache: opts.cache,
    rcExtensions: true,
    transform: result => {
      if (result && result.config) {
        delete result.config.$schema;
      }
      return result;
    }
  })
);

/** @param {{ cache: boolean, sync: boolean }} opts */
function getLoadFunction(opts) {
  // Normalize opts before passing to a memoized function
  opts = Object.assign({ sync: false, cache: false }, opts);
  return getExplorerMemoized(opts).load;
}

function _resolveConfig(filePath, opts, sync) {
  opts = Object.assign({ useCache: true }, opts);
  const loadOpts = {
    cache: !!opts.useCache,
    sync: !!sync,
    editorconfig: !!opts.editorconfig
  };
  const load = getLoadFunction(loadOpts);
  const loadEditorConfig = resolveEditorConfig.getLoadFunction(loadOpts);
  const arr = [load, loadEditorConfig].map(l => l(filePath, opts.config));

  const unwrapAndMerge = arr => {
    const result = arr[0];
    const editorConfigured = arr[1];
    const merged = Object.assign(
      {},
      editorConfigured,
      mergeOverrides(Object.assign({}, result), filePath)
    );

    if (!result && !editorConfigured) {
      return null;
    }

    return merged;
  };

  if (loadOpts.sync) {
    return unwrapAndMerge(arr);
  }

  return Promise.all(arr).then(unwrapAndMerge);
}

const resolveConfig = (filePath, opts) => _resolveConfig(filePath, opts, false);

resolveConfig.sync = (filePath, opts) => _resolveConfig(filePath, opts, true);

function clearCache() {
  mem.clear(getExplorerMemoized);
  resolveEditorConfig.clearCache();
}

function resolveConfigFile(filePath) {
  const load = getLoadFunction({ sync: false });
  return load(filePath).then(result => {
    return result ? result.filepath : null;
  });
}

resolveConfigFile.sync = filePath => {
  const load = getLoadFunction({ sync: true });
  const result = load(filePath);
  return result ? result.filepath : null;
};

function mergeOverrides(configResult, filePath) {
  const options = Object.assign({}, configResult.config);
  if (filePath && options.overrides) {
    const relativeFilePath = path.relative(
      path.dirname(configResult.filepath),
      filePath
    );
    for (const override of options.overrides) {
      if (
        pathMatchesGlobs(
          relativeFilePath,
          override.files,
          override.excludeFiles
        )
      ) {
        Object.assign(options, override.options);
      }
    }
  }

  delete options.overrides;
  return options;
}

// Based on eslint: https://github.com/eslint/eslint/blob/master/lib/config/config-ops.js
function pathMatchesGlobs(filePath, patterns, excludedPatterns) {
  const patternList = [].concat(patterns);
  const excludedPatternList = [].concat(excludedPatterns || []);
  const opts = { matchBase: true };

  return (
    patternList.some(pattern => minimatch(filePath, pattern, opts)) &&
    !excludedPatternList.some(excludedPattern =>
      minimatch(filePath, excludedPattern, opts)
    )
  );
}

module.exports = {
  resolveConfig,
  resolveConfigFile,
  clearCache
};
src/cli/util.js:112:    plugins: context.argv["plugin"],
src/cli/util.js:113:    pluginSearchDirs: context.argv["plugin-search-dir"]
src/cli/util.js:237:  const hasPlugins = options && options.plugins;
src/cli/util.js:239:    pushContextPlugins(context, options.plugins);
src/cli/util.js:657:  const pluginDefaults =
src/cli/util.js:658:    option.pluginDefaults && Object.keys(option.pluginDefaults).length
src/cli/util.js:659:      ? `\nPlugin defaults:${Object.keys(option.pluginDefaults).map(
src/cli/util.js:662:              option.pluginDefaults[key]
src/cli/util.js:666:  return `${header}${description}${choices}${defaults}${pluginDefaults}`;
src/cli/util.js:799:          option.name === "plugin" ||
src/cli/util.js:800:          option.name === "plugin-search-dir"
src/cli/util.js:864:  normalizeContextArgv(context, ["loglevel", "plugin", "plugin-search-dir"]);
src/cli/util.js:870:    context.argv["plugin"],
src/cli/util.js:871:    context.argv["plugin-search-dir"]
src/cli/util.js:882:function updateContextOptions(context, plugins, pluginSearchDirs) {
src/cli/util.js:887:    plugins,
src/cli/util.js:888:    pluginSearchDirs
src/cli/util.js:911:function pushContextPlugins(context, plugins, pluginSearchDirs) {
src/cli/util.js:916:  updateContextOptions(context, plugins, pluginSearchDirs);
src/cli/util.js:926:function updateContextArgv(context, plugins, pluginSearchDirs) {
src/cli/util.js:927:  pushContextPlugins(context, plugins, pluginSearchDirs);
config-invalid.js
config-resolution.js
plugin-default-options.js
plugin-extensions.js
plugin-options.js
plugin-precedence.js
plugin-preprocess.js
plugin-resolution.js
with-config-precedence.js
```

**tool call: Bash**

```bash
cat src/common/load-plugins.js; grep -rn "pluginSearchDirs\|plugins" src/main/options.js src/index.js | head -30
```

tool result:

```
"use strict";

const uniqBy = require("lodash.uniqby");
const fs = require("fs");
const globby = require("globby");
const path = require("path");
const resolve = require("resolve");
const thirdParty = require("./third-party");
const internalPlugins = require("./internal-plugins");

function loadPlugins(plugins, pluginSearchDirs) {
  if (!plugins) {
    plugins = [];
  }

  if (!pluginSearchDirs) {
    pluginSearchDirs = [];
  }
  // unless pluginSearchDirs are provided, auto-load plugins from node_modules that are parent to Prettier
  if (!pluginSearchDirs.length) {
    const autoLoadDir = thirdParty.findParentDir(
      thirdParty.findParentDir(__dirname, "prettier"),
      "node_modules"
    );
    if (autoLoadDir) {
      pluginSearchDirs = [autoLoadDir];
    }
  }

  const externalManualLoadPluginInfos = plugins.map(pluginName => {
    let requirePath;
    try {
      // try local files
      requirePath = resolve.sync(path.resolve(process.cwd(), pluginName));
    } catch (e) {
      // try node modules
      requirePath = resolve.sync(pluginName, { basedir: process.cwd() });
    }
    return {
      name: pluginName,
      requirePath
    };
  });

  const externalAutoLoadPluginInfos = pluginSearchDirs
    .map(pluginSearchDir => {
      const resolvedPluginSearchDir = path.resolve(
        process.cwd(),
        pluginSearchDir
      );

      if (!isDirectory(resolvedPluginSearchDir)) {
        throw new Error(
          `${pluginSearchDir} does not exist or is not a directory`
        );
      }

      const nodeModulesDir = path.resolve(
        resolvedPluginSearchDir,
        "node_modules"
      );

      return findPluginsInNodeModules(nodeModulesDir).map(pluginName => ({
        name: pluginName,
        requirePath: resolve.sync(pluginName, {
          basedir: resolvedPluginSearchDir
        })
      }));
    })
    .reduce((a, b) => a.concat(b), []);

  const externalPlugins = uniqBy(
    externalManualLoadPluginInfos.concat(externalAutoLoadPluginInfos),
    "requirePath"
  ).map(externalPluginInfo =>
    Object.assign(
      { name: externalPluginInfo.name },
      eval("require")(externalPluginInfo.requirePath)
    )
  );

  return internalPlugins.concat(externalPlugins);
}

function findPluginsInNodeModules(nodeModulesDir) {
  const pluginPackageJsonPaths = globby.sync(
    ["prettier-plugin-*/package.json", "@prettier/plugin-*/package.json"],
    { cwd: nodeModulesDir }
  );
  return pluginPackageJsonPaths.map(path.dirname);
}

function isDirectory(dir) {
  try {
    return fs.statSync(dir).isDirectory();
  } catch (e) {
    return false;
  }
}
module.exports = loadPlugins;
grep: src/index.js: No such file or directory
src/main/options.js:24:    plugins: options.plugins,
src/main/options.js:44:      rawOptions.parser = inferParser(rawOptions.filepath, rawOptions.plugins);
src/main/options.js:105:  const printerPlugin = options.plugins.find(
src/main/options.js:115:function inferParser(filepath, plugins) {
src/main/options.js:120:    plugins
```

**tool call: Bash**

```bash
git log --oneline -1; grep -rln "pluginSearchDirs\|\"plugins\"" tests_integration | grep -v node_modules | head; 
```

tool result:

```
4a163194 Travis - Allow failures in Node 6 (#4690)
tests_integration/plugins/options/config.json
tests_integration/plugins/defaultOptions/config.json
tests_integration/__tests__/plugin-resolution.js
tests_integration/__tests__/plugin-precedence.js
tests_integration/__tests__/file-info.js
tests_integration/__tests__/__snapshots__/support-info.js.snap
tests_integration/__tests__/__snapshots__/schema.js.snap
```

**tool call: Bash**

```bash
grep -n -B3 -A20 "config" tests_integration/__tests__/plugin-resolution.js | head -60; cat tests_integration/plugins/options/config.json
```

tool result:

```
{
    "plugins": ["./plugin"],
    "fooOption": "baz"
}
```

**assistant:** Let me reproduce: a config in a subdirectory referencing a plugin relative to the config file, with Prettier run from the repo root.

**tool call: Bash**

```bash
mkdir -p /tmp/x 2>/dev/null; cd tests_integration/plugins && ls; cat options/plugin.js | head -30
```

tool result:

```
automatic
bespoke
defaultOptions
extensions
options
preprocess
"use strict";

module.exports = {
  languages: [
    {
      name: "foo",
      parsers: ["foo-parser"],
      extensions: [".foo"],
      since: "1.0.0"
    }
  ],
  options: {
    fooOption: {
      type: "choice",
      default: "bar",
      description: "foo description",
      choices: [
        {
          value: "bar",
          description: "bar description"
        },
        {
          value: "baz",
          description: "baz description"
        }
      ]
    }
  },
  parsers: {
    "foo-parser": {
```

**tool call: Bash**

```bash
cd /work/prettier__prettier-4667/repo && mkdir -p repro_tmp/cfg && cat > repro_tmp/cfg/.prettierrc <<'EOF'
{ "plugins": ["../../tests_integration/plugins/options/plugin"], "pluginSearchDirs": ["../../tests_integration/plugins/automatic"] }
EOF
echo 'hello' > repro_tmp/cfg/file.foo
../bin/envrun 'node bin/prettier.js repro_tmp/cfg/file.foo; node -e "console.log(require(\"./\").resolveConfig.sync(\"repro_tmp/cfg/file.foo\"))"'
```

tool result:

```
/testbed/node_modules/find-parent-dir/index.js:10
  var parts = path.split(/(\/|\\)/);
                   ^

TypeError: Cannot read properties of null (reading 'split')
    at splitPath (/testbed/node_modules/find-parent-dir/index.js:10:20)
    at Object.exports.sync [as findParentDir] (/testbed/node_modules/find-parent-dir/index.js:44:18)
    at loadPlugins (/testbed/src/common/load-plugins.js:21:36)
    at Object.getSupportInfo (/testbed/index.js:21:16)
    at updateContextOptions (/testbed/src/cli/util.js:883:35)
    at pushContextPlugins (/testbed/src/cli/util.js:916:3)
    at updateContextArgv (/testbed/src/cli/util.js:927:3)
    at Object.createContext (/testbed/src/cli/util.js:863:3)
    at Object.run (/testbed/src/cli/index.js:8:24)
    at Object.<anonymous> (/testbed/bin/prettier.js:5:23)
{
  plugins: [ '../../tests_integration/plugins/options/plugin' ],
  pluginSearchDirs: [ '../../tests_integration/plugins/automatic' ]
}
(node:6) [DEP0128] DeprecationWarning: Invalid 'main' field in '/testbed/node_modules/find-parent-dir/package.json' of 'find-parent-dir.js'. Please either fix that or report it to the module author
(Use `node --trace-deprecation ...` to show where the warning was created)
```

**thinking:**

```
Confirmed: `resolveConfig` leaves relative `plugins`/`pluginSearchDirs` paths unresolved, so `loadPlugins` later resolves them against `process.cwd()` instead of the config file's directory (the CLI crash is a separate, unrelated issue). I'll fix this by resolving relative paths against the config file's directory in `resolveConfig`.


```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/prettier__prettier-4667/repo/src/config/resolve-config.js",
 "old_string": "      mergeOverrides(Object.assign({}, result), filePath)\n    );\n\n    if",
 "new_string": "      mergeOverrides(Object.assign({}, result), filePath)\n    );\n\n    [\"plugins\", \"pluginSearchDirs\"].forEach(optionName => {\n      if (Array.isArray(merged[optionName])) {\n        merged[optionName] = merged[optionName].map(\n          value =>\n            typeof value === \"string\" && value.startsWith(\".\") // relative path\n              ? path.resolve(path.dirname(result.filepath), value)\n              : value\n        );\n      }\n    });\n\n    if"
}
```

tool result:

```
The file /work/prettier__prettier-4667/repo/src/config/resolve-config.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**thinking:**

```
Confirming that only dot-prefixed values are treated as relative paths—package names and absolute paths pass through unchanged, and since `plugins` only comes from cosmiconfig, `result.filepath` is always defined when needed. Now I'll verify this.


```

**tool call: Bash**

```bash
cat > repro_tmp/cfg/.prettierrc <<'EOF'
{ "plugins": ["../../tests_integration/plugins/options/plugin", "some-pkg", "/abs/x"], "pluginSearchDirs": ["../../tests_integration/plugins/automatic"], "fooOption": "baz" }
EOF
../bin/envrun 'node -e "
const p=require(\"./\");
const o=p.resolveConfig.sync(\"repro_tmp/cfg/file.foo\"); console.log(o);
p.resolveConfig(\"repro_tmp/cfg/file.foo\").then(a=>console.log(\"async\",a.plugins[0]));
o.plugins=[o.plugins[0]]; o.pluginSearchDirs=[];
console.log(p.format(\"hello\", Object.assign({}, o, {filepath:\"repro_tmp/cfg/file.foo\"})));
" 2>&1 | grep -v -i deprecat'
```

tool result:

```
{
  plugins: [
    '/testbed/tests_integration/plugins/options/plugin',
    'some-pkg',
    '/abs/x'
  ],
  pluginSearchDirs: [ '/testbed/tests_integration/plugins/automatic' ],
  fooOption: 'baz'
}
/testbed/node_modules/find-parent-dir/index.js:10
  var parts = path.split(/(\/|\\)/);
                   ^

TypeError: Cannot read properties of null (reading 'split')
    at splitPath (/testbed/node_modules/find-parent-dir/index.js:10:20)
    at Object.exports.sync [as findParentDir] (/testbed/node_modules/find-parent-dir/index.js:44:18)
    at loadPlugins (/testbed/src/common/load-plugins.js:21:36)
    at /testbed/index.js:21:16
    at Object.format (/testbed/index.js:41:12)
    at [eval]:6:15
    at Script.runInThisContext (node:vm:129:12)
    at Object.runInThisContext (node:vm:313:38)
    at node:internal/process/execution:79:19
    at [eval]-wrapper:6:22
```

**thinking:**

```
Paths resolve correctly now, and the `format` crash turns out to be the same container-path issue, caused by an empty `pluginSearchDirs` triggering auto-load. Next I'll run an end-to-end CLI check from the repo root along with the related test suites.


```

**tool call: Bash**

```bash
cat > repro_tmp/cfg/.prettierrc <<'EOF'
{ "plugins": ["../../tests_integration/plugins/options/plugin"], "pluginSearchDirs": ["../../tests_integration/plugins/automatic"], "fooOption": "baz" }
EOF
../bin/envrun 'node bin/prettier.js --plugin-search-dir=. repro_tmp/cfg/file.foo 2>&1 | grep -v -i deprecat; yarn jest tests_integration/__tests__/plugin tests_integration/__tests__/config tests_integration/__tests__/with-config tests_integration/__tests__/file-info 2>&1 | tail -15'
```

tool result:

```
/testbed/node_modules/find-parent-dir/index.js:10
  var parts = path.split(/(\/|\\)/);
                   ^

TypeError: Cannot read properties of null (reading 'split')
    at splitPath (/testbed/node_modules/find-parent-dir/index.js:10:20)
    at Object.exports.sync [as findParentDir] (/testbed/node_modules/find-parent-dir/index.js:44:18)
    at loadPlugins (/testbed/src/common/load-plugins.js:21:36)
    at Object.getSupportInfo (/testbed/index.js:21:16)
    at updateContextOptions (/testbed/src/cli/util.js:883:35)
    at pushContextPlugins (/testbed/src/cli/util.js:916:3)
    at updateContextArgv (/testbed/src/cli/util.js:927:3)
    at Object.createContext (/testbed/src/cli/util.js:863:3)
    at Object.run (/testbed/src/cli/index.js:8:24)
    at Object.<anonymous> (/testbed/bin/prettier.js:5:23)
      at Object.<anonymous> (tests_integration/__tests__/file-info.js:224:19)
          at new Promise (<anonymous>)
      at processTicksAndRejections (node:internal/process/task_queues:96:5)

PASS tests_integration/__tests__/plugin-resolution.js
PASS tests_integration/__tests__/config-resolution.js
PASS tests_integration/__tests__/with-config-precedence.js

Test Suites: 1 failed, 9 passed, 10 total
Tests:       8 failed, 257 passed, 265 total
Snapshots:   117 passed, 117 total
Time:        2.231s
Ran all test suites matching /tests_integration\/__tests__\/plugin|tests_integration\/__tests__\/config|tests_integration\/__tests__\/with-config|tests_integration\/__tests__\/file-info/i.
error Command failed with exit code 1.
info Visit https://yarnpkg.com/en/docs/cli/run for documentation about this command.
```

**assistant:** I'll check whether the `file-info` failures were already there before my change:

**tool call: Bash**

```bash
git stash -q && ../bin/envrun 'yarn jest tests_integration/__tests__/file-info 2>&1 | grep -E "^Tests:|TypeError" | sort | uniq -c'; git stash pop -q && git status --short
```

tool result:

```
      8     TypeError: Cannot read properties of null (reading 'split')
      1 Tests:       8 failed, 49 passed, 57 total

 M package.json
 M src/config/resolve-config.js
?? Dockerfile
?? repro_tmp/
```

**assistant:** The 8 `file-info` failures happen without my change too. They come from the same environment issue. `package.json` and `Dockerfile` show up as changed, so I'll check what changed:

**tool call: Bash**

```bash
git diff package.json; rm -rf repro_tmp; git status --short
```

tool result:

```
diff --git a/package.json b/package.json
index 797a0b80..6d45232a 100644
--- a/package.json
+++ b/package.json
@@ -99,7 +99,7 @@
     "test": "jest",
     "test:dist": "node ./scripts/test-dist.js",
     "test-integration": "jest tests_integration",
-    "lint": "cross-env EFF_NO_LINK_RULES=true eslint . --format node_modules/eslint-friendly-formatter",
+    "lint": "echo noop",
     "lint-docs": "prettylint {.,docs,website,website/blog}/*.md",
     "build": "node ./scripts/build/build.js",
     "build-docs": "node ./scripts/build-docs.js",
 M package.json
 M src/config/resolve-config.js
?? Dockerfile
```

**assistant:** I fixed it: relative `plugins` and `pluginSearchDirs` entries in a config file now resolve from the directory containing the config file, not from where Prettier is run.

**Cause:** `resolveConfig` passed these values through unchanged. Prettier's plugin loader (`src/common/load-plugins.js`) then resolved them against `process.cwd()`. So a `.prettierrc` with `"plugins": ["./my-plugin"]` only worked if you ran Prettier from the folder holding that config file.

**Fix:** in `src/config/resolve-config.js`, after the config and its `overrides` are merged, any string value in `plugins` or `pluginSearchDirs` that starts with `.` is turned into an absolute path based on the config file's directory. The function is shared, so the sync and async versions both get the fix. Values that don't start with `.` are left alone: package names like `prettier-plugin-foo` or `@scope/plugin` still resolve from `node_modules`, and absolute paths pass through. Paths passed on the command line (`--plugin`, `--plugin-search-dir`) still resolve from the current directory.

**Checks:**
- **Reproduction:** a config in a subfolder with `"plugins": ["../../tests_integration/plugins/options/plugin"]`, resolved from the repo root. Before the fix the relative path came back unchanged. After it, it came back as `/testbed/tests_integration/plugins/options/plugin`. `pluginSearchDirs` was fixed the same way, and the `some-pkg` and `/abs/x` entries were unchanged.
- **I couldn't run a full end-to-end format in the container.** Both the CLI and `format()` crash in plugin auto-loading before they get to the config. That's because the repo is mounted at `/testbed`, so Prettier can't find a parent folder named `prettier`. This happens with or without my change.
- **Tests:** I ran the plugin, config-resolution, with-config-precedence and file-info suites. 257 tests pass and 8 fail, all in `file-info.js`. Those same 8 fail with my change stashed, with the same `/testbed` crash.

I deleted my reproduction files. The changes to `package.json` (lint script set to `echo noop`) and the untracked `Dockerfile` were already there before I started and look like setup for this environment, so I left them alone.

_session end: success, turns 12, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.96 s: node bin/prettier.js repro_tmp/cfg/file.foo; node -e "console.log(require(\"./\").resolveConfig.sync(\"repro_tmp/cfg/file.foo\"))"
- `rc=0` 0.53 s: node -e " const p=require(\"./\"); const o=p.resolveConfig.sync(\"repro_tmp/cfg/file.foo\"); console.log(o); p.resolveConfig(\"repro_tmp/cfg/file.foo\").then(a=>console.log(\"async\",a.plugins[0])); o.plugins=[o.plugins[0]]; o.pluginSearchDirs=[]; console.log(p.format(\"hello\", Object.assign({}, o, {filepath:\"repro_tmp/cfg/file.foo\"}))); " 2>&1 | grep -v -i deprecat
- `rc=0` 5.64 s: node bin/prettier.js --plugin-search-dir=. repro_tmp/cfg/file.foo 2>&1 | grep -v -i deprecat; yarn jest tests_integration/__tests__/plugin tests_integration/__tests__/config tests_integration/__tests__/with-config tests_integration/__tests__/file-info 2>&1 | tail -15
- `rc=0` 2.5 s: yarn jest tests_integration/__tests__/file-info 2>&1 | grep -E "^Tests:|TypeError" | sort | uniq -c
