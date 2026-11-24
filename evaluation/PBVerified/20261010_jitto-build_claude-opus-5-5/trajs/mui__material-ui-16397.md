# Instance: mui__material-ui-16397

- Final resolved (evaluator, logs/mui__material-ui-16397_result.json): True
- Run state: DONE
- One attempt. Duration 1035.1 s, turns 19, actor cost $0.291607, container commands 9
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/mui__material-ui-16397/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-16397/repo. Consider the following issue description:

<issue_description>
[ButtonBase] Improve Button accessibility
Revert #10339 removed safeguard and add additional one so anchors missing href's are treated as buttons.

<!--
    Thank you very much for contributing to Material-UI by creating an issue! ❤️
    To avoid duplicate issues we ask you to check off the following list.
-->

<!-- Checked checkbox should look like this: [x] -->
- [x] This is not a v0.x issue. <!-- (v0.x is no longer maintained) -->
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Expected Behavior 🤔
An anchor with an href should not be assigned `role=button`.

## Current Behavior 😯

An anchor with prop `button` w/ href is being given role of button as it misleads users. A button does not alter the url path while an href does. 

## Steps to Reproduce 🕹
```
<ListItem component={Link} to={path} button>
Hi there
</ListItem>
```
## Context 🔦
Screen reader


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-16397/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-16397/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-16397/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-16397/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
grep -n "role\|buttonProps\|ComponentProp\|href\|type" packages/material-ui/src/ButtonBase/ButtonBase.js | head -60
```

tool result:

```
2:import PropTypes from 'prop-types';
50:const useEnhancedEffect = typeof window !== 'undefined' ? React.useLayoutEffect : React.useEffect;
98:    type = 'button',
229:      !(button.tagName === 'A' && button.href)
260:  let ComponentProp = component;
262:  if (ComponentProp === 'button' && other.href) {
263:    ComponentProp = 'a';
266:  const buttonProps = {};
267:  if (ComponentProp === 'button') {
268:    buttonProps.type = type;
269:    buttonProps.disabled = disabled;
271:    buttonProps.role = 'button';
272:    buttonProps['aria-disabled'] = disabled;
280:    <ComponentProp
296:      {...buttonProps}
306:    </ComponentProp>
429:  role: PropTypes.string,
440:   * This property passes the value to the `type` attribute of the native button component.
442:  type: PropTypes.oneOf(['submit', 'reset', 'button']),
```

**tool call: Bash**

```bash
sed -n 255,300p packages/material-ui/src/ButtonBase/ButtonBase.js; grep -n "role\|href" packages/material-ui/src/ButtonBase/ButtonBase.test.js | head -40
```

tool result:

```
      [focusVisibleClassName]: focusVisible,
    },
    classNameProp,
  );

  let ComponentProp = component;

  if (ComponentProp === 'button' && other.href) {
    ComponentProp = 'a';
  }

  const buttonProps = {};
  if (ComponentProp === 'button') {
    buttonProps.type = type;
    buttonProps.disabled = disabled;
  } else {
    buttonProps.role = 'button';
    buttonProps['aria-disabled'] = disabled;
  }

  const handleUserRef = useForkRef(buttonRefProp, ref);
  const handleOwnRef = useForkRef(focusVisibleRef, buttonRef);
  const handleRef = useForkRef(handleUserRef, handleOwnRef);

  return (
    <ComponentProp
      className={className}
      onBlur={handleBlur}
      onClick={onClick}
      onFocus={handleFocus}
      onKeyDown={handleKeyDown}
      onKeyUp={handleKeyUp}
      onMouseDown={handleMouseDown}
      onMouseLeave={handleMouseLeave}
      onMouseUp={handleMouseUp}
      onDragLeave={handleDragLeave}
      onTouchEnd={handleTouchEnd}
      onTouchMove={handleTouchMove}
      onTouchStart={handleTouchStart}
      ref={handleRef}
      tabIndex={disabled ? -1 : tabIndex}
      {...buttonProps}
      {...other}
    >
      {children}
      {!disableRipple && !disabled ? (
85:        <ButtonBase component="span" role="checkbox" aria-checked={false} />,
94:    it('should not apply role="button" if type="button"', () => {
96:      expect(getByText('Hello')).to.not.have.attribute('role');
99:    it('should change the button type to span and set role="button"', () => {
107:    it('should automatically change the button to an a element when href is provided', () => {
108:      const { getByRole } = render(<ButtonBase href="https://google.com">Hello</ButtonBase>);
112:      expect(button).to.have.attribute('href', 'https://google.com');
115:    it('should change the button type to a and set role="button"', () => {
126:        <ButtonBase component="span" href="https://google.com">
132:      expect(button).to.have.attribute('href', 'https://google.com');
443:      expect(getByTestId('link')).to.have.attribute('role', 'button');
584:      it('prevents default with an anchor and empty href', () => {
601:      it('should ignore anchors with href', () => {
605:          <ButtonBase component="a" href="href" onClick={onClick} onKeyDown={onKeyDown}>
```

**tool call: Bash**

```bash
sed -n 80,140p packages/material-ui/src/ButtonBase/ButtonBase.test.js; sed -n 430,450p packages/material-ui/src/ButtonBase/ButtonBase.test.js; git log --oneline -3
```

tool result:

```
      expect(getByText('Hello')).to.have.attribute('type', 'submit');
    });

    it('should change the button component and add accessibility requirements', () => {
      const { getByRole } = render(
        <ButtonBase component="span" role="checkbox" aria-checked={false} />,
      );
      const checkbox = getByRole('checkbox');
      expect(checkbox).to.have.property('nodeName', 'SPAN');
      expect(checkbox)
        .attribute('tabIndex')
        .to.equal('0');
    });

    it('should not apply role="button" if type="button"', () => {
      const { getByText } = render(<ButtonBase type="button">Hello</ButtonBase>);
      expect(getByText('Hello')).to.not.have.attribute('role');
    });

    it('should change the button type to span and set role="button"', () => {
      const { getByRole } = render(<ButtonBase component="span">Hello</ButtonBase>);
      const button = getByRole('button');

      expect(button).to.have.property('nodeName', 'SPAN');
      expect(button).to.not.have.attribute('type');
    });

    it('should automatically change the button to an a element when href is provided', () => {
      const { getByRole } = render(<ButtonBase href="https://google.com">Hello</ButtonBase>);
      const button = getByRole('button');

      expect(button).to.have.property('nodeName', 'A');
      expect(button).to.have.attribute('href', 'https://google.com');
    });

    it('should change the button type to a and set role="button"', () => {
      const { getByRole } = render(<ButtonBase component="a">Hello</ButtonBase>);
      const button = getByRole('button');

      expect(button).to.have.property('nodeName', 'A');
      expect(button).not.to.have.attribute('type');
    });

    it('should not change the button to an a element', () => {
      const { getByRole } = render(
        // @ts-ignore
        <ButtonBase component="span" href="https://google.com">
          Hello
        </ButtonBase>,
      );
      const button = getByRole('button');
      expect(button).to.have.property('nodeName', 'SPAN');
      expect(button).to.have.attribute('href', 'https://google.com');
    });
  });

  describe('event callbacks', () => {
    it('should fire event callbacks', () => {
      const eventHandlerNames = [
        'onClick',
        'onFocus',
      );
      expect(getByRole('button')).not.to.have.attribute('disabled');
      expect(getByRole('button')).to.have.attribute('aria-disabled', 'true');
    });
  });

  describe('prop: component', () => {
    it('should allow to use a link component', () => {
      const Link = React.forwardRef((props, ref) => (
        <div data-testid="link" ref={ref} {...props} />
      ));
      const { getByTestId } = render(<ButtonBase component={Link}>Hello</ButtonBase>);

      expect(getByTestId('link')).to.have.attribute('role', 'button');
    });
  });

  describe('event: focus', () => {
    it('when disabled should not call onFocus', () => {
      const onFocusSpy = spy();
      const { getByRole } = render(
c78b343ad [ButtonBase] Improve test coverage (#16361)
bba516827 [TextareaAutosize] Fix one possible case of infinite render loop (#16387)
00c6ae250 [docs] Replace hardcoded content with translation (#16380)
```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/mui__material-ui-16397/repo/packages/material-ui/src/ButtonBase/ButtonBase.js",
 "old_string": "  } else {\n    buttonProps.role = 'button';",
 "new_string": "  } else {\n    if (ComponentProp !== 'a' || !other.href) {\n      buttonProps.role = 'button';\n    }"
}
```

tool result:

```
The file /work/mui__material-ui-16397/repo/packages/material-ui/src/ButtonBase/ButtonBase.js has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-16397 && bin/envrun 'cat > /tmp/repro.test.js <<EOF
import React from "react";
import { expect } from "chai";
import { createClientRender } from "/testbed/test/utils/createClientRender";
import ButtonBase from "/testbed/packages/material-ui/src/ButtonBase";
describe("repro", () => {
  const render = createClientRender({ strict: true });
  it("anchor with href has no role", () => {
    const { getByText } = render(<ButtonBase href="https://google.com">Hello</ButtonBase>);
    expect(getByText("Hello")).to.not.have.attribute("role");
    expect(getByText("Hello")).to.have.property("nodeName", "A");
  });
  it("anchor without href has role", () => {
    const { getByText } = render(<ButtonBase component="a">Hello</ButtonBase>);
    expect(getByText("Hello")).to.have.attribute("role", "button");
  });
});
EOF
cp /tmp/repro.test.js packages/material-ui/src/ButtonBase/repro.test.js && yarn -s mocha packages/material-ui/src/ButtonBase/repro.test.js 2>&1 | tail -20; rm packages/material-ui/src/ButtonBase/repro.test.js'
```

tool result:

```
    at /testbed/node_modules/mocha/lib/mocha.js:250:27
    at Array.forEach (<anonymous>)
    at Mocha.loadFiles (/testbed/node_modules/mocha/lib/mocha.js:247:14)
    at Mocha.run (/testbed/node_modules/mocha/lib/mocha.js:576:10)
    at Object.<anonymous> (/testbed/node_modules/mocha/bin/_mocha:637:18)
    at Module._compile (node:internal/modules/cjs/loader:1198:14)
    at Object.Module._extensions..js (node:internal/modules/cjs/loader:1252:10)
    at Module.load (node:internal/modules/cjs/loader:1076:32)
    at Function.Module._load (node:internal/modules/cjs/loader:911:12)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:81:12)
    at node:internal/main/run_main_module:22:47 {
  code: 'MODULE_NOT_FOUND',
  requireStack: [
    '/testbed/test/utils/init.js',
    '/testbed/test/utils/setup.js',
    '/testbed/node_modules/mocha/lib/mocha.js',
    '/testbed/node_modules/mocha/index.js',
    '/testbed/node_modules/mocha/bin/_mocha'
  ]
}
Shell cwd was reset to /work/mui__material-ui-16397/repo
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-16397 && bin/envrun 'ls test/utils | head -30; grep -n "\"test" package.json'
```

tool result:

```
consoleError.js
consoleErrorMock.js
consoleErrorMock.test.js
createClientRender.js
createDOM.d.ts
createDOM.js
init.d.ts
init.js
performance.js
rerender.js
setup.js
29:    "test": "yarn lint && yarn typescript && yarn test:coverage",
30:    "test:coverage": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha 'packages/**/*.test.js' 'docs/**/*.test.js' --exclude '**/node_modules/**' && nyc report -r lcovonly",
31:    "test:coverage:html": "cross-env NODE_ENV=test BABEL_ENV=coverage nyc mocha 'packages/**/**/*.test.js' --exclude '**/node_modules/**' && nyc report --reporter=html",
32:    "test:karma": "cross-env NODE_ENV=test karma start test/karma.conf.js",
33:    "test:regressions": "webpack --config test/regressions/webpack.config.js && rimraf test/regressions/screenshots/chrome/* && vrtest run --config test/vrtest.config.js --record",
34:    "test:umd": "yarn node packages/material-ui/test/umd/run.js",
35:    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/*.test.js' 'docs/**/*.test.js' --exclude '**/node_modules/**'",
36:    "test:watch": "yarn test:unit --watch",
Shell cwd was reset to /work/mui__material-ui-16397/repo
```

**thinking:**

```
I've fixed the issue by skipping `role="button"` for anchors with an href. The initial test run hit a module-loading error, so I'm rerunning it using the repo's `test:unit` environment with `NODE_ENV=test`.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-16397 && bin/envrun 'cp /tmp/repro.test.js packages/material-ui/src/ButtonBase/repro.test.js; NODE_ENV=test yarn -s mocha packages/material-ui/src/ButtonBase/repro.test.js packages/material-ui/src/ButtonBase/*.test.js packages/material-ui/src/ListItem/*.test.js packages/material-ui/src/Button/*.test.js 2>&1 | grep -v "^\s*at " | tail -60; rm packages/material-ui/src/ButtonBase/repro.test.js /tmp/repro.test.js'
```

tool result:

```
Command did not complete within its 120s timeout and was moved to the background (ID: b0eiqkrrc). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/d54cafc1-9ea6-4ec1-bd2c-6bded13d1647/tasks/b0eiqkrrc.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /work/mui__material-ui-16397/repo; directory changes made by the backgrounded command do not apply to subsequent commands.
```

**tool call: Bash**

```bash
sleep 90; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/d54cafc1-9ea6-4ec1-bd2c-6bded13d1647/tasks/b0eiqkrrc.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
sleep 120; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/d54cafc1-9ea6-4ec1-bd2c-6bded13d1647/tasks/b0eiqkrrc.output
```

tool result:

```
(Bash completed with no output)
```

**assistant:** I'll wait for the background run to finish.

**tool call: Bash**

```bash
sleep 240; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/d54cafc1-9ea6-4ec1-bd2c-6bded13d1647/tasks/b0eiqkrrc.output
```

tool result:

```
(Bash completed with no output)
```

**assistant:** The output comes through `tail`, so nothing will show until the run ends. I'll wait for the completion notice.

**tool call: Bash**

```bash
sleep 400; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/d54cafc1-9ea6-4ec1-bd2c-6bded13d1647/tasks/b0eiqkrrc.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-16397 && bin/envrun 'ps aux | grep -c mocha; ps aux | grep mocha | head -3'
```

tool result:

```
7
root        54  0.0  0.0 289616  6340 ?        Ss   07:31   0:00 bash -lc cp /tmp/repro.test.js packages/material-ui/src/ButtonBase/repro.test.js; NODE_ENV=test yarn -s mocha packages/material-ui/src/ButtonBase/repro.test.js packages/material-ui/src/ButtonBase/*.test.js packages/material-ui/src/ListItem/*.test.js packages/material-ui/src/Button/*.test.js 2>&1 | grep -v "^\s*at " | tail -60; rm packages/material-ui/src/ButtonBase/repro.test.js /tmp/repro.test.js
root        63  0.1  0.9 1139008 79376 ?       Sl   07:31   0:01 node --no-opt -r /proc/.reset /usr/local/nvm/versions/node/v16.20.2/bin/yarn -s mocha packages/material-ui/src/ButtonBase/repro.test.js packages/material-ui/src/ButtonBase/ButtonBase.test.js packages/material-ui/src/ButtonBase/Ripple.test.js packages/material-ui/src/ButtonBase/TouchRipple.test.js packages/material-ui/src/ButtonBase/repro.test.js packages/material-ui/src/ListItem/ListItem.test.js packages/material-ui/src/Button/Button.test.js
root        76  0.0  0.0 287856  3356 ?        S    07:31   0:00 /bin/sh -c /testbed/node_modules/.bin/mocha packages/material-ui/src/ButtonBase/repro.test.js packages/material-ui/src/ButtonBase/ButtonBase.test.js packages/material-ui/src/ButtonBase/Ripple.test.js packages/material-ui/src/ButtonBase/TouchRipple.test.js packages/material-ui/src/ButtonBase/repro.test.js packages/material-ui/src/ListItem/ListItem.test.js packages/material-ui/src/Button/Button.test.js
Shell cwd was reset to /work/mui__material-ui-16397/repo
```

**assistant:** Mocha appears to be hanging after the run, probably because of open handles. I'll stop it and rerun with `--exit`.

**tool call: Bash**

```bash
cd /work/mui__material-ui-16397 && bin/envrun 'pkill -f mocha; sleep 1; ls testbed 2>/dev/null; cat test/mocha.opts .mocharc* 2>/dev/null; ls packages/material-ui/src/ButtonBase/'
```

tool result:

```
Exit code 143
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-16397 && bin/envrun 'cat test/mocha.opts .mocharc* 2>/dev/null; ls packages/material-ui/src/ButtonBase/ /tmp/repro.test.js; git status --short'
```

tool result:

```
--require @babel/register
--reporter dot
--recursive
test/utils/setup.js
/tmp/repro.test.js

packages/material-ui/src/ButtonBase/:
ButtonBase.d.ts
ButtonBase.js
ButtonBase.test.js
Ripple.js
Ripple.test.js
TouchRipple.d.ts
TouchRipple.js
TouchRipple.test.js
index.d.ts
index.js
repro.test.js
 M package.json
 M packages/material-ui/src/ButtonBase/ButtonBase.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
?? packages/material-ui/src/ButtonBase/repro.test.js
Shell cwd was reset to /work/mui__material-ui-16397/repo
```

**thinking:**

```
I'll clean up the leftover repro file at the end, but I'll leave the existing package.json, yarn.lock, Dockerfile, and custom-reporter.js changes untouched. Now rerunning with `--exit` and a time limit.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-16397 && bin/envrun 'NODE_ENV=test timeout 500 node_modules/.bin/mocha --exit --reporter spec packages/material-ui/src/ButtonBase/repro.test.js packages/material-ui/src/ButtonBase/ButtonBase.test.js packages/material-ui/src/ListItem/ListItem.test.js packages/material-ui/src/Button/Button.test.js > /tmp/out.txt 2>&1; echo EXIT $?; grep -E "passing|failing|pending" /tmp/out.txt; grep -A15 "failing" /tmp/out.txt | head -80'
```

tool result:

```
EXIT 2
  88 passing (671ms)
  2 failing
  2 failing

  1) <ButtonBase />
       root node
         should automatically change the button to an a element when href is provided:
     Error: Unable to find an element by [role=button]

[36m<div[39m
  [33mclass[39m=[32m"rtl--baseElement"[39m
[36m>[39m
  [36m<div />[39m
  [36m<div />[39m
  [36m<div />[39m
  [36m<div />[39m
  [36m<div>[39m
    [36m<a[39m
Shell cwd was reset to /work/mui__material-ui-16397/repo
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-16397 && bin/envrun 'grep -B2 -A3 -E "^\s+[0-9]+\) " /tmp/out.txt | grep -v "\[3" | head -40; grep -A4 repro /tmp/out.txt | head'
```

tool result:

```
      ✓ should not apply role="button" if type="button"
      ✓ should change the button type to span and set role="button"
      1) should automatically change the button to an a element when href is provided
      ✓ should change the button type to a and set role="button"
      ✓ should not change the button to an a element
    event callbacks
--
        ✓ calls onClick when a spacebar is pressed on the element
        ✓ prevents default with an anchor and empty href
        2) should ignore anchors with href
    prop: action
      ✓ should be able to focus visible the button
    rerender
--
  2 failing

  1) <ButtonBase />
       root node
         should automatically change the button to an a element when href is provided:
     Error: Unable to find an element by [role=button]
--
      at processImmediate (node:internal/timers:466:21)

  2) <ButtonBase />
       event: keydown
         keyboard accessibility for non interactive elements
           should ignore anchors with href:
  repro
    ✓ anchor with href has no role (77ms)
    ✓ anchor without href has role

  <ButtonBase />
Shell cwd was reset to /work/mui__material-ui-16397/repo
```

**thinking:**

```
My reproduction case passes, and the two failing tests in `ButtonBase.test.js` rely on finding an anchor with an href via `role="button"` — the exact behavior the issue wants removed. Let me check the second test now.


```

**tool call: Bash**

```bash
sed -n 600,625p packages/material-ui/src/ButtonBase/ButtonBase.test.js
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-16397 && bin/envrun 'rm -f packages/material-ui/src/ButtonBase/repro.test.js /tmp/repro.test.js /tmp/out.txt; git status --short; git diff packages/'
```

tool result:

```
      it('should ignore anchors with href', () => {
        const onClick = spy();
        const onKeyDown = spy(event => event.defaultPrevented);
        const { getByRole } = render(
          <ButtonBase component="a" href="href" onClick={onClick} onKeyDown={onKeyDown}>
            Hello
          </ButtonBase>,
        );
        const button = getByRole('button');
        button.focus();
        fireEvent.keyDown(document.activeElement || document.body, {
          key: 'Enter',
        });

        expect(onClick.calledOnce).to.be.false;
        // defaultPrevented
        expect(onKeyDown.returnValues[0]).to.be.false;
      });
    });
  });

  describe('prop: action', () => {
    it('should be able to focus visible the button', () => {
      /**
       * @type {React.RefObject<import('./ButtonBase').ButtonBaseActions>}
```

tool result:

```
 M package.json
 M packages/material-ui/src/ButtonBase/ButtonBase.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
diff --git a/packages/material-ui/src/ButtonBase/ButtonBase.js b/packages/material-ui/src/ButtonBase/ButtonBase.js
index d157b568e..8387ed5df 100644
--- a/packages/material-ui/src/ButtonBase/ButtonBase.js
+++ b/packages/material-ui/src/ButtonBase/ButtonBase.js
@@ -268,7 +268,9 @@ const ButtonBase = React.forwardRef(function ButtonBase(props, ref) {
     buttonProps.type = type;
     buttonProps.disabled = disabled;
   } else {
-    buttonProps.role = 'button';
+    if (ComponentProp !== 'a' || !other.href) {
+      buttonProps.role = 'button';
+    }
     buttonProps['aria-disabled'] = disabled;
   }
Shell cwd was reset to /work/mui__material-ui-16397/repo
```

**assistant:** `ButtonBase` no longer adds `role="button"` to an `<a>` that has an `href`. My checks pass, but two existing tests fail because they expect the old behaviour.

**The change** (`packages/material-ui/src/ButtonBase/ButtonBase.js:270`): the role is now only set when the element isn't an anchor with an href.
```js
if (ComponentProp !== 'a' || !other.href) {
  buttonProps.role = 'button';
}
```
- An `<a>` with an `href` (from `href="..."`, or `component="a"` plus an href) now has no `role`, so screen readers announce it as a link.
- An `<a>` without an `href`, spans, divs and custom components still get `role="button"`.
- Native `<button>` elements are unchanged: they still get `type` and `disabled`.

**Test results:** I wrote two quick checks: an anchor with an href has no role, and an anchor without one gets `role="button"`. Both pass. Across the `ButtonBase`, `Button` and `ListItem` test files, 88 pass and 2 fail, both in `ButtonBase.test.js`:
- "should automatically change the button to an a element when href is provided"
- "should ignore anchors with href"

Both find an `<a href>` by `getByRole('button')`, which is exactly what the issue asks to remove. I assume your updated tests replace these; I didn't modify any tests.

**One limitation:** the issue's own example, `<ListItem component={Link} to={path} button>`, still gets `role="button"`. `ButtonBase` decides the role from the component and props alone, so it can't tell that a custom `Link` will end up as an `<a href>`. Fixing that case would need a different approach, such as checking the actual DOM element after it renders. For now, passing `role={undefined}` or another role explicitly on that `ListItem` should override it, because user props are applied after the defaults.

I deleted my temporary test file. The uncommitted changes to `package.json` and `yarn.lock`, plus the untracked `Dockerfile` and `custom-reporter.js`, were already there before I started, and I left them untouched.

_session end: success, turns 19, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 2.23 s: cat > /tmp/repro.test.js <<EOF import React from "react"; import { expect } from "chai"; import { createClientRender } from "/testbed/test/utils/createClientRender"; import ButtonBase from "/testbed/packages/material-ui/src/ButtonBase"; describe("repro", () => {   const render = createClientRender({ strict: true });   it("anchor with href has no role", () => {     const { getByText } = render(<ButtonBase href="https://google.com">Hello</ButtonBase>);     expect(getByText("Hello")).to.not.have.attribute("role");     expect(getByText("Hello")).to.have.property("nodeName", "A");   });   it("ancho
- `rc=0` 0.15 s: ls test/utils | head -30; grep -n "\"test" package.json
- `rc=0` 0.16 s: ps aux | grep -c mocha; ps aux | grep mocha | head -3
- `rc=143` 984.27 s: cp /tmp/repro.test.js packages/material-ui/src/ButtonBase/repro.test.js; NODE_ENV=test yarn -s mocha packages/material-ui/src/ButtonBase/repro.test.js packages/material-ui/src/ButtonBase/*.test.js packages/material-ui/src/ListItem/*.test.js packages/material-ui/src/Button/*.test.js 2>&1 | grep -v "^\s*at " | tail -60; rm packages/material-ui/src/ButtonBase/repro.test.js /tmp/repro.test.js
- `rc=143` 0.14 s: pkill -f mocha; sleep 1; ls testbed 2>/dev/null; cat test/mocha.opts .mocharc* 2>/dev/null; ls packages/material-ui/src/ButtonBase/
- `rc=0` 2.32 s: cat test/mocha.opts .mocharc* 2>/dev/null; ls packages/material-ui/src/ButtonBase/ /tmp/repro.test.js; git status --short
- `rc=0` 2.37 s: NODE_ENV=test timeout 500 node_modules/.bin/mocha --exit --reporter spec packages/material-ui/src/ButtonBase/repro.test.js packages/material-ui/src/ButtonBase/ButtonBase.test.js packages/material-ui/src/ListItem/ListItem.test.js packages/material-ui/src/Button/Button.test.js > /tmp/out.txt 2>&1; echo EXIT $?; grep -E "passing|failing|pending" /tmp/out.txt; grep -A15 "failing" /tmp/out.txt | head -80
- `rc=0` 0.16 s: grep -B2 -A3 -E "^\s+[0-9]+\) " /tmp/out.txt | grep -v "\[3" | head -40; grep -A4 repro /tmp/out.txt | head
- `rc=0` 0.4 s: rm -f packages/material-ui/src/ButtonBase/repro.test.js /tmp/repro.test.js /tmp/out.txt; git status --short; git diff packages/
