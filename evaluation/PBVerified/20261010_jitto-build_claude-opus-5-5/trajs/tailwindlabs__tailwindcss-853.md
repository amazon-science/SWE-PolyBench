# Instance: tailwindlabs__tailwindcss-853

- Final resolved (evaluator, logs/tailwindlabs__tailwindcss-853_result.json): True
- Run state: DONE
- One attempt. Duration 62.6 s, turns 10, actor cost $0.1670036, container commands 4
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/tailwindlabs__tailwindcss-853/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/tailwindlabs__tailwindcss-853/repo. Consider the following issue description:

<issue_description>
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

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/tailwindlabs__tailwindcss-853/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/tailwindlabs__tailwindcss-853/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/tailwindlabs__tailwindcss-853/bin/envrun 'git status --short && ls'
Edits you make under /work/tailwindlabs__tailwindcss-853/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
grep -rn "corePlugins" src __tests__ | head -40; cat src/util/configurePlugins.js
```

tool result:

```
src/processTailwindFeatures.js:11:import corePlugins from './corePlugins'
src/processTailwindFeatures.js:17:    const processedPlugins = processPlugins([...corePlugins(config), ...config.plugins], config)
src/corePlugins.js:70:export default function({ corePlugins: corePluginConfig }) {
__tests__/applyAtRule.test.js:5:import corePlugins from '../src/corePlugins'
__tests__/applyAtRule.test.js:11:  corePlugins(resolvedDefaultConfig),
__tests__/applyAtRule.test.js:216:  return run(input, config, processPlugins(corePlugins(config), config).utilities).then(result => {
__tests__/applyAtRule.test.js:240:  return run(input, config, processPlugins(corePlugins(config), config).utilities).then(result => {
export default function(pluginConfig, plugins) {
  return Object.keys(plugins)
    .filter(pluginName => {
      return pluginConfig !== false && pluginConfig[pluginName] !== false
    })
    .map(pluginName => {
      return plugins[pluginName]()
    })
}
```

**tool call: Bash**

```bash
cat __tests__/configurePlugins.test.js; git log --oneline -2
```

tool result:

```
import configurePlugins from '../src/util/configurePlugins'

test('setting a plugin to false removes it', () => {
  const plugins = {
    fontSize: () => 'fontSize',
    display: () => 'display',
    backgroundPosition: () => 'backgroundPosition',
  }

  const configuredPlugins = configurePlugins(
    {
      display: false,
    },
    plugins
  )

  expect(configuredPlugins).toEqual(['fontSize', 'backgroundPosition'])
})

test('passing only false removes all plugins', () => {
  const plugins = {
    fontSize: () => 'fontSize',
    display: () => 'display',
    backgroundPosition: () => 'backgroundPosition',
  }

  const configuredPlugins = configurePlugins(false, plugins)

  expect(configuredPlugins).toEqual([])
})
daea662 Merge pull request #852 from tailwindcss/global-variants
f0bc35a Support configuring a single list of variants to apply to all relevant plugins
```

**tool call: Bash**

```bash
grep -n "corePlugins" -r src stubs; sed -n 1,80p src/util/resolveConfig.js
```

tool result:

```
src/processTailwindFeatures.js:11:import corePlugins from './corePlugins'
src/processTailwindFeatures.js:17:    const processedPlugins = processPlugins([...corePlugins(config), ...config.plugins], config)
src/corePlugins.js:70:export default function({ corePlugins: corePluginConfig }) {
stubs/defaultConfig.stub.js:444:  corePlugins: {},
import mergeWith from 'lodash/mergeWith'
import isFunction from 'lodash/isFunction'
import defaults from 'lodash/defaults'
import map from 'lodash/map'
import get from 'lodash/get'

function value(valueToResolve, ...args) {
  return isFunction(valueToResolve) ? valueToResolve(...args) : valueToResolve
}

function mergeExtensions({ extend, ...theme }) {
  return mergeWith(theme, extend, (themeValue, extensions) => {
    if (!isFunction(themeValue) && !isFunction(extensions)) {
      return {
        ...themeValue,
        ...extensions,
      }
    }

    return resolveThemePath => ({
      ...value(themeValue, resolveThemePath),
      ...value(extensions, resolveThemePath),
    })
  })
}

function resolveFunctionKeys(object) {
  const resolveObjectPath = (key, defaultValue) => {
    const val = get(object, key, defaultValue)
    return isFunction(val) ? val(resolveObjectPath) : val
  }

  return Object.keys(object).reduce((resolved, key) => {
    return {
      ...resolved,
      [key]: isFunction(object[key]) ? object[key](resolveObjectPath) : object[key],
    }
  }, {})
}

export default function resolveConfig(configs) {
  return defaults(
    {
      theme: resolveFunctionKeys(mergeExtensions(defaults({}, ...map(configs, 'theme')))),
      variants: defaults({}, ...map(configs, 'variants')),
    },
    ...configs
  )
}
```

**tool call: Bash**

```bash
cat > /tmp/x.test.js <<'EOF'
EOF
cat > __tests__/zz_repro.test.js <<'EOF'
import configurePlugins from '../src/util/configurePlugins'
const plugins = { fontSize: () => 'fontSize', display: () => 'display', backgroundPosition: () => 'backgroundPosition' }
test('array', () => expect(configurePlugins(['backgroundPosition', 'display'], plugins)).toEqual(['display', 'backgroundPosition']))
test('only', () => expect(configurePlugins({ only: ['display'] }, plugins)).toEqual(['display']))
EOF
/work/tailwindlabs__tailwindcss-853/bin/envrun 'npx jest __tests__/zz_repro.test.js 2>&1 | tail -20'
```

tool result:

```
(eval):1: operation not permitted: /tmp/x.test.js
mesg: ttyname failed: Inappropriate ioctl for device

      Array [
    +   "fontSize",
        "display",
    +   "backgroundPosition",
      ]

      2 | const plugins = { fontSize: () => 'fontSize', display: () => 'display', backgroundPosition: () => 'backgroundPosition' }
      3 | test('array', () => expect(configurePlugins(['backgroundPosition', 'display'], plugins)).toEqual(['display', 'backgroundPosition']))
    > 4 | test('only', () => expect(configurePlugins({ only: ['display'] }, plugins)).toEqual(['display']))
        |                                                                             ^
      5 |

      at Object.<anonymous>.test (__tests__/zz_repro.test.js:4:77)

Test Suites: 1 failed, 1 total
Tests:       2 failed, 2 total
Snapshots:   0 total
Time:        1.208s
Ran all test suites matching /__tests__\/zz_repro.test.js/i.
```

**assistant:** Reproduced. Now the fix — supporting both an array whitelist and the `{ only: [...] }` form from the issue, preserving core plugin order:

**tool call: Write**

```json
{
 "file_path": "/work/tailwindlabs__tailwindcss-853/repo/src/util/configurePlugins.js",
 "content": "export default function(pluginConfig, plugins) {\n  const whitelist = Array.isArray(pluginConfig)\n    ? pluginConfig\n    : pluginConfig && Array.isArray(pluginConfig.only)\n      ? pluginConfig.only\n      : null\n\n  return Object.keys(plugins)\n    .filter(pluginName => {\n      if (whitelist !== null) {\n        return whitelist.includes(pluginName)\n      }\n\n      return pluginConfig !== false && pluginConfig[pluginName] !== false\n    })\n    .map(pluginName => {\n      return plugins[pluginName]()\n    })\n}\n"
}
```

tool result:

```
The file /work/tailwindlabs__tailwindcss-853/repo/src/util/configurePlugins.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
/work/tailwindlabs__tailwindcss-853/bin/envrun 'npx jest 2>&1 | tail -8; npx eslint src/util/configurePlugins.js'; rm __tests__/zz_repro.test.js; git status --short
```

tool result:

```
mesg: ttyname failed: Inappropriate ioctl for device
      at then (__tests__/cli.test.js:68:55)


Test Suites: 2 failed, 23 passed, 25 total
Tests:       2 failed, 147 passed, 149 total
Snapshots:   0 total
Time:        7.504s
Ran all test suites.

/testbed/src/util/configurePlugins.js
  2:21  error  Do not nest ternary expressions  no-nested-ternary
  5:5   error  Delete `··`                      prettier/prettier
  6:1   error  Delete `··`                      prettier/prettier

✖ 3 problems (3 errors, 0 warnings)
  2 errors and 0 warnings potentially fixable with the `--fix` option.


 M src/util/configurePlugins.js
?? Dockerfile
```

**assistant:** Lint complains about the nested ternary; I'll restructure. I'll also check which tests failed and re-run the reproduction (I removed it too early).

**tool call: Write**

```json
{
 "file_path": "/work/tailwindlabs__tailwindcss-853/repo/src/util/configurePlugins.js",
 "content": "function getWhitelist(pluginConfig) {\n  if (Array.isArray(pluginConfig)) {\n    return pluginConfig\n  }\n\n  if (pluginConfig && Array.isArray(pluginConfig.only)) {\n    return pluginConfig.only\n  }\n\n  return null\n}\n\nexport default function(pluginConfig, plugins) {\n  const whitelist = getWhitelist(pluginConfig)\n\n  return Object.keys(plugins)\n    .filter(pluginName => {\n      if (whitelist !== null) {\n        return whitelist.includes(pluginName)\n      }\n\n      return pluginConfig !== false && pluginConfig[pluginName] !== false\n    })\n    .map(pluginName => {\n      return plugins[pluginName]()\n    })\n}\n"
}
```

tool result:

```
The file /work/tailwindlabs__tailwindcss-853/repo/src/util/configurePlugins.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
cat > __tests__/zz_repro.test.js <<'EOF'
import configurePlugins from '../src/util/configurePlugins'
const plugins = { fontSize: () => 'fontSize', display: () => 'display', backgroundPosition: () => 'backgroundPosition' }
test('array', () => expect(configurePlugins(['backgroundPosition', 'display'], plugins)).toEqual(['display', 'backgroundPosition']))
test('only', () => expect(configurePlugins({ only: ['display'] }, plugins)).toEqual(['display']))
test('empty', () => expect(configurePlugins([], plugins)).toEqual([]))
EOF
/work/tailwindlabs__tailwindcss-853/bin/envrun 'npx jest 2>&1 | grep -E "✕|FAIL|Tests:"; npx eslint src/util/configurePlugins.js && echo LINT OK; git stash -q && npx jest 2>&1 | grep -E "✕|FAIL|Tests:"; git stash pop -q'; rm __tests__/zz_repro.test.js; git status --short
```

tool result:

```
mesg: ttyname failed: Inappropriate ioctl for device
FAIL __tests__/cli.compile.test.js
FAIL __tests__/cli.test.js (5.119s)
FAIL __tests__/cli.compile.test.js
FAIL __tests__/cli.test.js (5.119s)
Tests:       2 failed, 148 passed, 150 total
LINT OK

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'root@f1a54d942969.(none)')
Cannot save the current index state
No stash found.

 M src/util/configurePlugins.js
?? Dockerfile
```

**assistant:** The reproduction passes now and lint is clean. The stash failed because git isn't configured in the container, so I'll check the two CLI failures a different way:

**tool call: Bash**

```bash
/work/tailwindlabs__tailwindcss-853/bin/envrun 'npx jest __tests__/cli.test.js 2>&1 | grep -B2 -A12 "●" | head -40'
```

tool result:

```
mesg: ttyname failed: Inappropriate ioctl for device
      ✓ compiles CSS file without autoprefixer (565ms)

  ● cli › build › compiles CSS file

    expect(received).toContain(expected) // indexOf

    Expected substring: ".example"
    Received string:    "  console.warn node_modules/browserslist/node.js:480
        Browserslist: browsers data (caniuse-lite) is 14 months old. Please run:
          npx update-browserslist-db@latest
          Why you should do it regularly: https://github.com/browserslist/update-db#readme·
    "

      46 |     it('compiles CSS file', () => {
      47 |       return cli(['build', inputCssPath]).then(() => {
--
      at then (__tests__/cli.test.js:48:55)

  ● cli › build › compiles CSS file with autoprefixer

    expect(received).toContain(expected) // indexOf

    Expected substring: "-ms-input-placeholder"
    Received string:    "/*! normalize.css v8.0.1 | MIT License | github.com/necolas/normalize.css */·
    /* Document
       ========================================================================== */·
    /**
     * 1. Correct the line height in all browsers.
     * 2. Prevent adjustments of font size after orientation changes in iOS.
     */·
    html {
```

**assistant:** You can now give `corePlugins` a list of plugins to enable, and every other core plugin stays off. That includes any core plugins added in future Tailwind updates.

**Change:** the only file touched is `src/util/configurePlugins.js`. Both of these forms work:

```js
// Plain array
corePlugins: ['backgroundColor', 'textColor']

// The object form proposed in the issue
corePlugins: { only: ['backgroundColor', 'textColor'] }
```

- Enabled plugins still run in Tailwind's normal order, whatever order you list them in, so the order of the generated CSS doesn't change.
- An empty list (`[]`) turns everything off, the same as `corePlugins: false`.
- The existing forms still work: `false` disables all core plugins, and `{ display: false }` disables just that one.

**Testing:**
- Before the fix, a temporary test reproduced the problem: both list forms were ignored and all plugins stayed on.
- After the fix it passed, including the empty-list case. I deleted the temporary test afterwards.
- Full suite: 148 passed, 2 failed. Both failures are in the CLI tests (`__tests__/cli.test.js` and `__tests__/cli.compile.test.js`). The output I inspected comes from the container's setup, not this change: a "browsers data is 14 months old" warning gets captured instead of the CSS, and the vendor prefixes the autoprefixer test expects aren't added.
- I couldn't confirm the failures happen without my change, because temporarily stashing it failed (git has no user configured in the container).
- ESLint passes on the changed file.

The `Dockerfile` that shows as untracked in `git status` isn't mine, so I left it alone.

_session end: success, turns 10, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 2.42 s: npx jest __tests__/zz_repro.test.js 2>&1 | tail -20
- `rc=1` 9.92 s: npx jest 2>&1 | tail -8; npx eslint src/util/configurePlugins.js
- `rc=1` 10.0 s: npx jest 2>&1 | grep -E "✕|FAIL|Tests:"; npx eslint src/util/configurePlugins.js && echo LINT OK; git stash -q && npx jest 2>&1 | grep -E "✕|FAIL|Tests:"; git stash pop -q
- `rc=0` 5.62 s: npx jest __tests__/cli.test.js 2>&1 | grep -B2 -A12 "●" | head -40
