# Instance: mui__material-ui-15526

- Final resolved (evaluator, logs/mui__material-ui-15526_result.json): False
- Run state: DONE
- One attempt. Duration 949.4 s, turns 27, actor cost $0.6151472, container commands 8
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/mui__material-ui-15526/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-15526/repo. Consider the following issue description:

<issue_description>
[Zoom] Not accepting child component
First of all, Thanks for giving this beautiful framework. It has always been a great experience to work with Material-UI.

Today, I updated my project to `@material-ui/core@next`. Successfully removed all deprecated props. But, failed to solve this issue. Prior to v4 this was working.

- [ x ] This is not a v0.x issue.
- [ x ] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

```jsx
// Input Field component
const InputField = ({
    field,
    form: { touched, errors },
    ...props
}) => {
    const error = errors[field.name];
    return (
        <TextField
            variant="outlined"
            margin="dense"
            error={touched && error ? true : false}
            helperText={touched && error ? `- ${error}` : null}
            fullWidth
            {...field}
            {...props}
        />
    );
};
```

## Expected Behavior 🤔
Zoom component is not accepting a `<Field/>` component from Formik as child.

```jsx
import { Field } from 'formik';

<Zoom in={show}>
         <Field
                 name="title"
                 type="text"
                 variant="outlined"
                 margin="dense"
                 component={InputField}
          />
</Zoom>
```
## Current Behavior 😯
Zoom should be given a `<div/>` to wrap the `<Field/>` component

```jsx
import { Field } from 'formik';

<Zoom in={show}>
           <div>
                  <Field
                            name="title"
                            type="text"
                            variant="outlined"
                            margin="dense"
                            component={InputField}
                   />
           </div>
</Zoom>
```

## Error
I am getting this error in the console.

```bash
Warning: Function components cannot be given refs. Attempts to access this ref will fail. Did you mean to use React.forwardRef()?

Check the render method of `Transition`.
```

## Context 🔦
I am trying to animate fields/buttons in form whenever the form appears in the DOM.

## Your Environment 🌎

| Tech         | Version |
|--------------|---------|
| Material-UI  | ^4.0.0-beta.0  |
| React        |     ^16.8.6    |
| Browser      |     Chromium: 74.0.3729.108    |

Fun Fact: This is my first contribution 😋

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-15526/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-15526/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-15526/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-15526/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/mui__material-ui-15526/repo; cat packages/material-ui/src/Zoom/Zoom.js; ls packages/material-ui/src/Zoom packages/material-ui/src/Fade packages/material-ui/src/Grow; cat packages/material-ui/src/Fade/Fade.js
```

tool result:

```
// @inheritedComponent Transition

import React from 'react';
import PropTypes from 'prop-types';
import { Transition } from 'react-transition-group';
import { duration } from '../styles/transitions';
import withTheme from '../styles/withTheme';
import { reflow, getTransitionProps } from '../transitions/utils';
import { useForkRef } from '../utils/reactHelpers';

const styles = {
  entering: {
    transform: 'scale(1)',
  },
  entered: {
    transform: 'scale(1)',
  },
};

/**
 * The Zoom transition can be used for the floating variant of the
 * [Button](https://material-ui.com/demos/buttons/#floating-action-buttons) component.
 * It uses [react-transition-group](https://github.com/reactjs/react-transition-group) internally.
 */
const Zoom = React.forwardRef(function Zoom(props, ref) {
  const { children, in: inProp, onEnter, onExit, style, theme, ...other } = props;
  const handleRef = useForkRef(children.ref, ref);

  const handleEnter = node => {
    reflow(node); // So the animation always start from the start.

    const transitionProps = getTransitionProps(props, {
      mode: 'enter',
    });
    node.style.webkitTransition = theme.transitions.create('transform', transitionProps);
    node.style.transition = theme.transitions.create('transform', transitionProps);

    if (onEnter) {
      onEnter(node);
    }
  };

  const handleExit = node => {
    const transitionProps = getTransitionProps(props, {
      mode: 'exit',
    });
    node.style.webkitTransition = theme.transitions.create('transform', transitionProps);
    node.style.transition = theme.transitions.create('transform', transitionProps);

    if (onExit) {
      onExit(node);
    }
  };

  return (
    <Transition appear in={inProp} onEnter={handleEnter} onExit={handleExit} {...other}>
      {(state, childProps) => {
        return React.cloneElement(children, {
          style: {
            transform: 'scale(0)',
            visibility: state === 'exited' && !inProp ? 'hidden' : undefined,
            ...styles[state],
            ...style,
            ...children.props.style,
          },
          ref: handleRef,
          ...childProps,
        });
      }}
    </Transition>
  );
});

Zoom.propTypes = {
  /**
   * A single child content element.
   */
  children: PropTypes.element,
  /**
   * If `true`, the component will transition in.
   */
  in: PropTypes.bool,
  /**
   * @ignore
   */
  onEnter: PropTypes.func,
  /**
   * @ignore
   */
  onExit: PropTypes.func,
  /**
   * @ignore
   */
  style: PropTypes.object,
  /**
   * @ignore
   */
  theme: PropTypes.object.isRequired,
  /**
   * The duration for the transition, in milliseconds.
   * You may specify a single timeout for all transitions, or individually with an object.
   */
  timeout: PropTypes.oneOfType([
    PropTypes.number,
    PropTypes.shape({ enter: PropTypes.number, exit: PropTypes.number }),
  ]),
};

Zoom.defaultProps = {
  timeout: {
    enter: duration.enteringScreen,
    exit: duration.leavingScreen,
  },
};

export default withTheme(Zoom);
packages/material-ui/src/Fade:
Fade.d.ts
Fade.js
Fade.test.js
index.d.ts
index.js

packages/material-ui/src/Grow:
Grow.d.ts
Grow.js
Grow.test.js
index.d.ts
index.js

packages/material-ui/src/Zoom:
Zoom.d.ts
Zoom.js
Zoom.test.js
index.d.ts
index.js
// @inheritedComponent Transition

import React from 'react';
import PropTypes from 'prop-types';
import { Transition } from 'react-transition-group';
import { duration } from '../styles/transitions';
import withTheme from '../styles/withTheme';
import { reflow, getTransitionProps } from '../transitions/utils';
import { useForkRef } from '../utils/reactHelpers';

const styles = {
  entering: {
    opacity: 1,
  },
  entered: {
    opacity: 1,
  },
};

/**
 * The Fade transition is used by the [Modal](/utils/modal/) component.
 * It uses [react-transition-group](https://github.com/reactjs/react-transition-group) internally.
 */
const Fade = React.forwardRef(function Fade(props, ref) {
  const { children, in: inProp, onEnter, onExit, style, theme, ...other } = props;
  const handleRef = useForkRef(children.ref, ref);

  const handleEnter = node => {
    reflow(node); // So the animation always start from the start.

    const transitionProps = getTransitionProps(props, {
      mode: 'enter',
    });
    node.style.webkitTransition = theme.transitions.create('opacity', transitionProps);
    node.style.transition = theme.transitions.create('opacity', transitionProps);

    if (onEnter) {
      onEnter(node);
    }
  };

  const handleExit = node => {
    const transitionProps = getTransitionProps(props, {
      mode: 'exit',
    });
    node.style.webkitTransition = theme.transitions.create('opacity', transitionProps);
    node.style.transition = theme.transitions.create('opacity', transitionProps);

    if (onExit) {
      onExit(node);
    }
  };

  return (
    <Transition appear in={inProp} onEnter={handleEnter} onExit={handleExit} {...other}>
      {(state, childProps) => {
        return React.cloneElement(children, {
          style: {
            opacity: 0,
            visibility: state === 'exited' && !inProp ? 'hidden' : undefined,
            ...styles[state],
            ...style,
            ...children.props.style,
          },
          ref: handleRef,
          ...childProps,
        });
      }}
    </Transition>
  );
});

Fade.propTypes = {
  /**
   * A single child content element.
   */
  children: PropTypes.element,
  /**
   * If `true`, the component will transition in.
   */
  in: PropTypes.bool,
  /**
   * @ignore
   */
  onEnter: PropTypes.func,
  /**
   * @ignore
   */
  onExit: PropTypes.func,
  /**
   * @ignore
   */
  style: PropTypes.object,
  /**
   * @ignore
   */
  theme: PropTypes.object.isRequired,
  /**
   * The duration for the transition, in milliseconds.
   * You may specify a single timeout for all transitions, or individually with an object.
   */
  timeout: PropTypes.oneOfType([
    PropTypes.number,
    PropTypes.shape({ ent
[... 204 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-15526/repo; git log --oneline -2; cat packages/material-ui/src/Zoom/Zoom.test.js | head -60; grep -rn "elementAcceptingRef\|refType" packages/material-ui-utils/src/index.js packages/material-ui/src --include=*.js -l | head -30
```

tool result:

```
6ef44f1cf [ButtonBase] Use fork of focus-visible polyfill (#15484)
c867c5f12 [docs] Updated v3 Migration guide (#15518)
import React from 'react';
import { assert } from 'chai';
import { spy, useFakeTimers } from 'sinon';
import { createMount, describeConformance } from '@material-ui/core/test-utils';
import Zoom from './Zoom';

describe('<Zoom />', () => {
  let mount;

  before(() => {
    // StrictModeViolation: uses react-transition-group
    mount = createMount({ strict: false });
  });

  after(() => {
    mount.cleanUp();
  });

  describeConformance(
    <Zoom in>
      <div />
    </Zoom>,
    () => ({
      classes: {},
      inheritComponent: 'Transition',
      mount,
      skip: ['componentProp', 'refForwarding'],
    }),
  );

  describe('transition lifecycle', () => {
    let clock;
    let wrapper;
    let child;

    const handleEnter = spy();
    const handleEntering = spy();
    const handleEntered = spy();
    const handleExit = spy();
    const handleExiting = spy();
    const handleExited = spy();

    before(() => {
      clock = useFakeTimers();
      wrapper = mount(
        <Zoom
          onEnter={handleEnter}
          onEntering={handleEntering}
          onEntered={handleEntered}
          onExit={handleExit}
          onExiting={handleExiting}
          onExited={handleExited}
        >
          <div id="test" />
        </Zoom>,
      );
      child = wrapper.find('#test');
    });

    after(() => {
(eval):1: no matches found: --include=*.js
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-15526/repo; ls packages/material-ui-utils/src; cat packages/material-ui-utils/src/index.js; grep -rln "elementAcceptingRef" packages/material-ui/src | head -30
```

tool result:

```
chainPropTypes.js
chainPropTypes.test.js
elementTypeAcceptingRef.js
elementTypeAcceptingRef.test.js
exactProp.js
exactProp.test.js
getDisplayName.js
getDisplayName.test.js
index.js
ponyfillGlobal.js
ponyfillGlobal.test.js
export { default as chainPropTypes } from './chainPropTypes';
export { default as elementTypeAcceptingRef } from './elementTypeAcceptingRef';
export { default as exactProp } from './exactProp';
export { default as getDisplayName } from './getDisplayName';
export { default as ponyfillGlobal } from './ponyfillGlobal';
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-15526/repo; cat packages/material-ui-utils/src/elementTypeAcceptingRef.js; cat packages/material-ui-utils/src/elementTypeAcceptingRef.test.js | head -40; grep -rn "elementTypeAcceptingRef\|AcceptingRef" packages docs/src --include=*.js -l | grep -v node_modules
```

tool result:

```
import * as PropTypes from 'prop-types';
import chainPropTypes from './chainPropTypes';

function isClassComponent(elementType) {
  // elementType.prototype?.isReactComponent
  const { prototype = {} } = elementType;

  return Boolean(prototype.isReactComponent);
}

function elementTypeAcceptingRef(props, propName, componentName, location, propFullName) {
  const propValue = props[propName];
  const safePropName = propFullName || propName;

  if (propValue == null) {
    return null;
  }

  let warningHint;

  /**
   * Blacklisting instead of whitelisting
   *
   * Blacklisting will miss some components, such as React.Fragment. Those will at least
   * trigger a warning in React.
   * We can't whitelist because there is no safe way to detect React.forwardRef
   * or class components. "Safe" means there's no public API.
   *
   */
  if (typeof propValue === 'function' && !isClassComponent(propValue)) {
    warningHint = 'Did you accidentally provide a plain function component instead?';
  }

  if (warningHint !== undefined) {
    return new Error(
      `Invalid ${location} \`${safePropName}\` supplied to \`${componentName}\`. ` +
        `Expected an element type that can hold a ref. ${warningHint} ` +
        'For more information see https://next.material-ui.com/guides/composition/#caveat-with-refs',
    );
  }

  return null;
}

export default chainPropTypes(PropTypes.elementType, elementTypeAcceptingRef);
/* eslint-disable react/prefer-stateless-function */
import { assert } from 'chai';
import * as PropTypes from 'prop-types';
import React from 'react';
import ReactDOM from 'react-dom';
import { createMount } from '@material-ui/core/test-utils';
import consoleErrorMock from 'test/utils/consoleErrorMock';
import elementTypeAcceptingRef from './elementTypeAcceptingRef';

describe('elementTypeAcceptingRef', () => {
  let mount;

  function checkPropType(elementType) {
    PropTypes.checkPropTypes(
      { component: elementTypeAcceptingRef },
      { component: elementType },
      'props',
      'DummyComponent',
    );
  }

  before(() => {
    mount = createMount();
  });

  after(() => {
    mount.cleanUp();
  });

  beforeEach(() => {
    consoleErrorMock.spy();
  });

  afterEach(() => {
    consoleErrorMock.reset();
    PropTypes.resetWarningCache();
  });

  describe('acceptance', () => {
    let rootNode;
(eval):1: no matches found: --include=*.js
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-15526/repo; cat packages/material-ui-utils/src/chainPropTypes.js; grep -rn "elementTypeAcceptingRef" packages docs --include='*.js' --include='*.md' | grep -v node_modules | grep -v "material-ui-utils/src"; grep -rln "children: PropTypes.element[,.]" packages/material-ui/src
```

tool result:

```
function chainPropTypes(propType1, propType2) {
  if (process.env.NODE_ENV === 'production') {
    return () => null;
  }

  return function validate(...args) {
    return propType1(...args) || propType2(...args);
  };
}

export default chainPropTypes;
packages/material-ui/src/ButtonBase/ButtonBase.js:5:import { elementTypeAcceptingRef } from '@material-ui/utils';
packages/material-ui/src/ButtonBase/ButtonBase.js:342:  component: elementTypeAcceptingRef,
packages/material-ui/src/SwipeableDrawer/SwipeableDrawer.js:7:import { elementTypeAcceptingRef } from '@material-ui/utils';
packages/material-ui/src/SwipeableDrawer/SwipeableDrawer.js:458:      component: elementTypeAcceptingRef,
packages/material-ui/src/SwipeableDrawer/SwipeableDrawer.js:481:    component: elementTypeAcceptingRef,
packages/material-ui/src/Popover/Popover.js:10:import { chainPropTypes, elementTypeAcceptingRef } from '@material-ui/utils';
packages/material-ui/src/Popover/Popover.js:526:    component: elementTypeAcceptingRef,
docs/src/modules/utils/generateMarkdown.js:78:  return type.raw === 'elementTypeAcceptingRef';
packages/material-ui/src/Tooltip/Tooltip.js
packages/material-ui/src/Slide/Slide.js
packages/material-ui/src/Snackbar/Snackbar.js
packages/material-ui/src/Fade/Fade.js
packages/material-ui/src/ListItemIcon/ListItemIcon.js
packages/material-ui/src/Grow/Grow.js
packages/material-ui/src/Zoom/Zoom.js
packages/material-ui/src/RootRef/RootRef.js
packages/material-ui/src/ListItemAvatar/ListItemAvatar.js
packages/material-ui/src/Modal/TrapFocus.js
packages/material-ui/src/Modal/Modal.js
packages/material-ui/src/ClickAwayListener/ClickAwayListener.js
```

**thinking:**

```
Zoom, Fade, Grow and Slide clone their children and attach a ref, which breaks function component children like Formik's `Field` with only a vague React warning. I'll add an `elementAcceptingRef` prop-type that names this issue and links to the docs, then apply it to those transitions' `children`.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-15526/repo; sed -n 60,110p docs/src/modules/utils/generateMarkdown.js; grep -n "children" packages/material-ui/src/Slide/Slide.js | head; grep -n "children\|^import" packages/material-ui/src/Grow/Grow.js | head -20
```

tool result:

```
        type: parsed.props.bar.type,
        required: parsed.props.bar.required,
      };
    }
  }

  return false;
}

function escapeCell(value) {
  // As the pipe is use for the table structure
  return value
    .replace(/</g, '&lt;')
    .replace(/`&lt;/g, '`<')
    .replace(/\|/g, '\\|');
}

function isElementTypeAcceptingRefProp(type) {
  return type.raw === 'elementTypeAcceptingRef';
}

function generatePropDescription(prop) {
  const { description } = prop;
  const type = prop.flowType || prop.type;
  let deprecated = '';

  if (type.name === 'custom') {
    const deprecatedInfo = getDeprecatedInfo(type);
    if (deprecatedInfo) {
      deprecated = `*Deprecated*. ${deprecatedInfo.explanation}<br><br>`;
    }
  }

  const parsed = parseDoctrine(description, {
    sloppy: true,
  });

  // Two new lines result in a newline in the table.
  // All other new lines must be eliminated to prevent markdown mayhem.
  const jsDocText = escapeCell(parsed.description)
    .replace(/\n\n/g, '<br>')
    .replace(/\n/g, ' ')
    .replace(/\r/g, '');

  if (parsed.tags.some(tag => tag.title === 'ignore')) {
    return null;
  }

  let signature = '';

  if (type.name === 'func' && parsed.tags.length > 0) {
75:    children,
88:  const childrenRef = React.useRef();
90:   * used in cloneElement(children, { ref: handleRef })
94:    childrenRef.current = ReactDOM.findDOMNode(instance);
96:  const handleRefIntermediary = useForkRef(children.ref, handleOwnRef);
100:    const node = childrenRef.current;
110:    const node = childrenRef.current;
133:    const node = childrenRef.current;
156:    const node = childrenRef.current;
167:    if (childrenRef.current) {
3:import React from 'react';
4:import PropTypes from 'prop-types';
5:import { Transition } from 'react-transition-group';
6:import withTheme from '../styles/withTheme';
7:import { reflow, getTransitionProps } from '../transitions/utils';
8:import { useForkRef } from '../utils/reactHelpers';
32:  const { children, in: inProp, onEnter, onExit, style, theme, timeout, ...other } = props;
35:  const handleRef = useForkRef(children.ref, ref);
122:        return React.cloneElement(children, {
129:            ...children.props.style,
143:  children: PropTypes.element,
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-15526/repo; grep -n "isElementTypeAcceptingRefProp\|elementType\b" -A6 docs/src/modules/utils/generateMarkdown.js | sed -n 1,60p; grep -n "children: PropTypes.element" -B3 packages/material-ui/src/Slide/Slide.js
```

tool result:

```
77:function isElementTypeAcceptingRefProp(type) {
78-  return type.raw === 'elementTypeAcceptingRef';
79-}
80-
81-function generatePropDescription(prop) {
82-  const { description } = prop;
83-  const type = prop.flowType || prop.type;
--
154:  if (isElementTypeAcceptingRefProp(type)) {
155-    notes += '<br>⚠️ [Needs to be able to hold a ref](/guides/composition/#caveat-with-refs).';
156-  }
157-
158-  return `${deprecated}${jsDocText}${signature}${notes}`;
159-}
160-
--
164:      if (isElementTypeAcceptingRefProp(type)) {
165-        return `element type`;
166-      }
167-
168-      const deprecatedInfo = getDeprecatedInfo(type);
169-      if (deprecatedInfo !== false) {
170-        return generatePropType({
229-   *
230-   * ⚠️The component used as a child [must be able to hold a ref](/guides/composition/#children).
231-   */
232:  children: PropTypes.element,
```

**assistant:** Now I'll create the util and wire it up.

**tool call: Bash**

```bash
cd /work/mui__material-ui-15526/repo
cat > packages/material-ui-utils/src/elementAcceptingRef.js <<'EOF'
import * as PropTypes from 'prop-types';
import chainPropTypes from './chainPropTypes';

function isClassComponent(elementType) {
  // elementType.prototype?.isReactComponent
  const { prototype = {} } = elementType;

  return Boolean(prototype.isReactComponent);
}

function elementAcceptingRef(props, propName, componentName, location, propFullName) {
  const propValue = props[propName];
  const safePropName = propFullName || propName;

  if (propValue == null) {
    return null;
  }

  let warningHint;

  const elementType = propValue.type;
  /**
   * Blacklisting instead of whitelisting
   *
   * Blacklisting will miss some components, such as React.Fragment. Those will at least
   * trigger a warning in React.
   * We can't whitelist because there is no safe way to detect React.forwardRef
   * or class components. "Safe" means there's no public API.
   *
   */
  if (typeof elementType === 'function' && !isClassComponent(elementType)) {
    warningHint = 'Did you accidentally use a plain function component for an element instead?';
  }

  if (warningHint !== undefined) {
    return new Error(
      `Invalid ${location} \`${safePropName}\` supplied to \`${componentName}\`. ` +
        `Expected an element that can hold a ref. ${warningHint} ` +
        'For more information see https://next.material-ui.com/guides/composition/#caveat-with-refs',
    );
  }

  return null;
}

export default chainPropTypes(PropTypes.element, elementAcceptingRef);
EOF
python3 - <<'EOF'
import re
p='packages/material-ui-utils/src/index.js'
s=open(p).read()
s=s.replace("export { default as elementTypeAcceptingRef }","export { default as elementAcceptingRef } from './elementAcceptingRef';\nexport { default as elementTypeAcceptingRef }")
open(p,'w').write(s)
for c in ['Fade','Grow','Zoom','Slide']:
    p=f'packages/material-ui/src/{c}/{c}.js'
    s=open(p).read()
    assert s.count('  children: PropTypes.element,')==1
    s=s.replace('  children: PropTypes.element,','  children: elementAcceptingRef,')
    s=s.replace("import PropTypes from 'prop-types';\n","import PropTypes from 'prop-types';\nimport { elementAcceptingRef } from '@material-ui/utils';\n",1)
    open(p,'w').write(s)
p='docs/src/modules/utils/generateMarkdown.js'
s=open(p).read()
s=s.replace("""function isElementTypeAcceptingRefProp(type) {
  return type.raw === 'elementTypeAcceptingRef';
}
""","""function isElementTypeAcceptingRefProp(type) {
  return type.raw === 'elementTypeAcceptingRef';
}

function isElementAcceptingRefProp(type) {
  return type.raw === 'elementAcceptingRef';
}
""")
s=s.replace("""  if (isElementTypeAcceptingRefProp(type)) {
    notes += '<br>⚠️ [Needs to be able to hold a ref](/guides/composition/#caveat-with-refs).';
  }""","""  if (isElementTypeAcceptingRefProp(type) || isElementAcceptingRefProp(type)) {
    notes += '<br>⚠️ [Needs to be able to hold a ref](/guides/composition/#caveat-with-refs).';
  }""")
s=s.replace("""      if (isElementTypeAcceptingRefProp(type)) {
        return `element type`;
      }
""","""      if (isElementTypeAcceptingRefProp(type)) {
        return `element type`;
      }
      if (isElementAcceptingRefProp(type)) {
        return `element`;
      }
""")
open(p,'w').write(s)
EOF
git diff --stat; grep -n "import" packages/material-ui/src/Slide/Slide.js
```

tool result:

```
 docs/src/modules/utils/generateMarkdown.js |  9 ++++-
 package.json                               |  7 +++-
 packages/material-ui-utils/src/index.js    |  1 +
 packages/material-ui/src/Fade/Fade.js      |  3 +-
 packages/material-ui/src/Grow/Grow.js      |  3 +-
 packages/material-ui/src/Slide/Slide.js    |  3 +-
 packages/material-ui/src/Zoom/Zoom.js      |  3 +-
 yarn.lock                                  | 56 +++++++++++++++++++++++++++---
 8 files changed, 74 insertions(+), 11 deletions(-)
3:import React from 'react';
4:import PropTypes from 'prop-types';
5:import { elementAcceptingRef } from '@material-ui/utils';
6:import ReactDOM from 'react-dom';
7:import debounce from 'debounce'; // < 1kb payload overhead when lodash/debounce is > 3kb.
8:import { Transition } from 'react-transition-group';
9:import { useForkRef } from '../utils/reactHelpers';
10:import withTheme from '../styles/withTheme';
11:import { duration } from '../styles/transitions';
12:import { reflow, getTransitionProps } from '../transitions/utils';
```

**assistant:** `package.json` and `yarn.lock` show changes I didn't make. Let me check what they are.

**tool call: Bash**

```bash
cd /work/mui__material-ui-15526/repo; git diff package.json; git diff yarn.lock | head -30
```

tool result:

```
diff --git a/package.json b/package.json
index a28679a61..acfd2c930 100644
--- a/package.json
+++ b/package.json
@@ -77,16 +77,21 @@
     "@emotion/styled": "^10.0.0",
     "@trendmicro/react-interpolate": "0.5.5",
     "@types/autosuggest-highlight": "^3.1.0",
+    "@types/chai": "^5.2.2",
+    "@types/chai-dom": "^1.11.3",
     "@types/enzyme": "^3.1.4",
+    "@types/format-util": "^1.0.4",
     "@types/lodash": "^4.14.123",
+    "@types/prop-types": "^15.7.15",
     "@types/react": "^16.8.10",
     "@types/react-autosuggest": "^9.3.7",
-    "@types/react-dom": "^16.0.9",
+    "@types/react-dom": "^19.1.8",
     "@types/react-router-dom": "^4.3.1",
     "@types/react-select": "^2.0.14",
     "@types/react-swipeable-views": "^0.13.0",
     "@types/react-text-mask": "^5.4.2",
     "@types/react-window": "^1.7.0",
+    "@types/sinon": "^17.0.4",
     "@types/styled-components": "^4.1.11",
     "@zeit/next-typescript": "^1.1.1",
     "address": "^1.0.3",
diff --git a/yarn.lock b/yarn.lock
index b8902127c..c102a53c2 100644
--- a/yarn.lock
+++ b/yarn.lock
@@ -1721,12 +1721,12 @@
     write-file-atomic "^2.3.0"
 
 "@material-ui/core@^3.9.3":
-  version "4.0.0-alpha.8"
+  version "4.0.0-beta.0"
   dependencies:
     "@babel/runtime" "^7.2.0"
-    "@material-ui/styles" "^4.0.0-alpha.8"
-    "@material-ui/system" "^4.0.0-alpha.8"
-    "@material-ui/utils" "^4.0.0-alpha.8"
+    "@material-ui/styles" "^4.0.0-beta.0"
+    "@material-ui/system" "^4.0.0-beta.0"
+    "@material-ui/utils" "^4.0.0-beta.0"
     "@types/react-transition-group" "^2.0.16"
     clsx "^1.0.2"
     csstype "^2.5.2"
@@ -1840,6 +1840,20 @@
   resolved "https://registry.yarnpkg.com/@types/autosuggest-highlight/-/autosuggest-highlight-3.1.0.tgz#62045417c2f6d841f9f12e715336218e4db0fcb1"
   integrity sha512-rJWvrDFKf2NkB3CkeJPcnX3oD0XAQriJOhYC5DUwiK6X/KTM96e1rW+1/PgI0U4tL6GQ2K7dvoiYFhMnAaNLUw==
 
+"@types/chai-dom@^1.11.3":
+  version "1.11.3"
+  resolved "https://registry.yarnpkg.com/@types/chai-dom/-/chai-dom-1.11.3.tgz#1659ace2698cdcd9ed8b2c007876f53e37d9cc89"
+  integrity sha512-EUEZI7uID4ewzxnU7DJXtyvykhQuwe+etJ1wwOiJyQRTH/ifMWKX+ghiXkxCUvNJ6IQDodf0JXhuP6zZcy2qXQ==
+  dependencies:
```

**thinking:**

```
The package.json/yarn.lock changes are from environment setup, not mine, so I'll leave them as is. Now I'll write a quick test checking the new warning appears while existing behavior still works.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-15526/repo
cat > packages/material-ui/src/Zoom/repro.test.js <<'EOF'
import React from 'react';
import { assert } from 'chai';
import PropTypes from 'prop-types';
import { createMount } from '@material-ui/core/test-utils';
import consoleErrorMock from 'test/utils/consoleErrorMock';
import Zoom from './Zoom';
import Fade from '../Fade';

describe('repro', () => {
  let mount;
  before(() => { mount = createMount({ strict: false }); });
  after(() => mount.cleanUp());
  beforeEach(() => consoleErrorMock.spy());
  afterEach(() => { consoleErrorMock.reset(); PropTypes.resetWarningCache(); });

  it('warns for function component', () => {
    const Field = () => <div />;
    mount(<Zoom in><Field /></Zoom>);
    console.log(consoleErrorMock.args().map(a => a[0]).join('\n---\n'));
    assert.include(consoleErrorMock.args()[0][0], 'Expected an element that can hold a ref');
  });
  it('no warning for forwardRef / class / host', () => {
    const F = React.forwardRef((p, ref) => <div ref={ref} />);
    class C extends React.Component { render() { return <div />; } }
    mount(<Fade in><F /></Fade>);
    mount(<Fade in><C /></Fade>);
    mount(<Zoom in><div /></Zoom>);
    assert.strictEqual(consoleErrorMock.callCount(), 0);
  });
});
EOF
/work/mui__material-ui-15526/bin/envrun 'cat package.json | grep "\"test:unit"; NODE_ENV=test yarn -s mocha packages/material-ui/src/Zoom/repro.test.js 2>&1 | tail -40'
```

tool result:

```
Command did not complete within its 120s timeout and was moved to the background (ID: b58d1ur07). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/db6e4503-f1cb-4874-b1e1-5e107dca7a8d/tasks/b58d1ur07.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /work/mui__material-ui-15526/repo; directory changes made by the backgrounded command do not apply to subsequent commands.
```

**tool call: Bash**

```bash
sleep 90; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/db6e4503-f1cb-4874-b1e1-5e107dca7a8d/tasks/b58d1ur07.output
```

tool result:

```
    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/
```

**tool call: Bash**

```bash
sleep 120; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/db6e4503-f1cb-4874-b1e1-5e107dca7a8d/tasks/b58d1ur07.output; cat /work/mui__material-ui-15526/repo/.mocharc* 2>/dev/null; ls -a /work/mui__material-ui-15526/repo/test
```

tool result:

```
Exit code 143
Command timed out after 2m 0s
```

**tool call: Bash**

```bash
cat /tmp/cell-scratch/claude-502/<actor-session-slug>/db6e4503-f1cb-4874-b1e1-5e107dca7a8d/tasks/b58d1ur07.output; ls -a /work/mui__material-ui-15526/repo/test
```

tool result:

```
    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/.
..
README.md
docs-regressions-before.png
docs-regressions-diff.png
karma.conf.js
karma.tests.js
mocha.opts
regressions
utils
vrtest.config.js
```

**assistant:** The test run is still going, probably because Babel is compiling on first run. I'll wait for it to finish.

**tool call: Bash**

```bash
cat /work/mui__material-ui-15526/repo/test/mocha.opts; sleep 100; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/db6e4503-f1cb-4874-b1e1-5e107dca7a8d/tasks/b58d1ur07.output
```

tool result:

```
--require @babel/register
--reporter dot
--recursive
test/utils/setup.js
    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/
```

**tool call: Bash**

```bash
sleep 240; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/db6e4503-f1cb-4874-b1e1-5e107dca7a8d/tasks/b58d1ur07.output
```

tool result:

```
    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/
```

**assistant:** Still nothing after several minutes, so something is likely hanging. Let me check what's running in the container.

**tool call: Bash**

```bash
/work/mui__material-ui-15526/bin/envrun 'ps aux | head -20'
```

tool result:

```
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0 287720  2948 ?        Ss   06:14   0:00 sleep infinity
root         7  0.0  0.0 289616  6348 ?        Ss   06:15   0:00 bash -lc cat package.json | grep "\"test:unit"; NODE_ENV=test yarn -s mocha packages/material-ui/src/Zoom/repro.test.js 2>&1 | tail -40
root        17  0.1  1.1 1160216 93796 ?       Sl   06:15   0:00 node --no-opt -r /proc/.reset /usr/local/nvm/versions/node/v16.20.2/bin/yarn -s mocha packages/material-ui/src/Zoom/repro.test.js
root        18  0.0  0.0 287760  3016 ?        S    06:15   0:00 tail -40
root        29  0.0  0.0 287856  3348 ?        S    06:15   0:00 /bin/sh -c /testbed/node_modules/.bin/mocha packages/material-ui/src/Zoom/repro.test.js
root        30  0.0  0.5 616716 47644 ?        Sl   06:15   0:00 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/.bin/mocha packages/material-ui/src/Zoom/repro.test.js
root        37  0.5  2.0 970844 161984 ?       Sl   06:15   0:03 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/mocha/bin/_mocha --require @babel/register --reporter dot --recursive test/utils/setup.js packages/material-ui/src/Zoom/repro.test.js
root        44  0.0  0.0 289612  6332 ?        Ss   06:26   0:00 bash -lc ps aux | head -20
root        52  0.0  0.0 292124  5168 ?        R    06:26   0:00 ps aux
root        53  0.0  0.0 287732  2968 ?        S    06:26   0:00 head -20
```

**assistant:** The mocha process is idle, not working, so it probably finished but never exited, and `tail` is holding the output until it does. I'll kill it and rerun with `--exit`.

**tool call: Bash**

```bash
/work/mui__material-ui-15526/bin/envrun 'kill 37 30 17; NODE_ENV=test timeout 100 node_modules/.bin/mocha --exit packages/material-ui/src/Zoom/repro.test.js 2>&1 | tail -40'
```

tool result:

```
Browserslist: caniuse-lite is outdated. Please run next command `yarn upgrade`

Warning: Failed prop type: Invalid prop `children` supplied to `ForwardRef(Zoom)`. Expected an element that can hold a ref. Did you accidentally use a plain function component for an element instead? For more information see https://next.material-ui.com/guides/composition/#caveat-with-refs
    in ForwardRef(Zoom) (created by WithTheme(ForwardRef(Zoom)))
    in WithTheme(ForwardRef(Zoom))
    in Mode (created by WrapperComponent)
    in WrapperComponent
---
Warning: Function components cannot be given refs. Attempts to access this ref will fail. Did you mean to use React.forwardRef()?%s%s

  ․․

  2 passing (169ms)
```

**thinking:**

```
The reproduction confirms plain function component children now trigger the expected prop-type warning, while forwardRef, class, and DOM children stay silent. Next I'll add an `.isRequired` variant, regenerate the API docs, and run the existing tests.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-15526/repo; rm packages/material-ui/src/Zoom/repro.test.js
python3 - <<'EOF'
p='packages/material-ui-utils/src/elementAcceptingRef.js'
s=open(p).read()
s=s.replace("function elementAcceptingRef(","function acceptingRef(")
s=s.replace("export default chainPropTypes(PropTypes.element, elementAcceptingRef);\n","""const elementAcceptingRef = chainPropTypes(PropTypes.element, acceptingRef);
elementAcceptingRef.isRequired = chainPropTypes(PropTypes.element.isRequired, acceptingRef);

export default elementAcceptingRef;
""")
open(p,'w').write(s)
EOF
ls packages/material-ui-utils/src/*.d.ts 2>/dev/null; grep -n '"docs:api"' package.json
```

tool result:

```
(eval):13: no matches found: packages/material-ui-utils/src/*.d.ts
24:    "docs:api": "yarn docs:api:core && yarn docs:api:lab",
```

**tool call: Bash**

```bash
/work/mui__material-ui-15526/bin/envrun 'timeout 300 yarn -s docs:api:core >/tmp/docs.log 2>&1; echo $?; tail -5 /tmp/docs.log; git status --short; git diff docs/pages'
```

tool result:

```
Exit code 128
0
Built markdown docs for TextField
Built markdown docs for Tooltip
Built markdown docs for Tabs
Built markdown docs for Typography
Built markdown docs for Zoom
 M docs/src/modules/utils/generateMarkdown.js
 M package.json
 M packages/material-ui-utils/src/index.js
 M packages/material-ui/src/Fade/Fade.js
 M packages/material-ui/src/Grow/Grow.js
 M packages/material-ui/src/Slide/Slide.js
 M packages/material-ui/src/Zoom/Zoom.js
 M pages/api/fade.md
 M pages/api/grow.md
 M pages/api/slide.md
 M pages/api/zoom.md
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
?? packages/material-ui-utils/src/elementAcceptingRef.js
fatal: ambiguous argument 'docs/pages': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-15526/repo; git diff pages
```

tool result:

```
diff --git a/pages/api/fade.md b/pages/api/fade.md
index 689f7f3d6..2508b932d 100644
--- a/pages/api/fade.md
+++ b/pages/api/fade.md
@@ -19,7 +19,7 @@ It uses [react-transition-group](https://github.com/reactjs/react-transition-gro
 
 | Name | Type | Default | Description |
 |:-----|:-----|:--------|:------------|
-| <span class="prop-name">children</span> | <span class="prop-type">element</span> |  | A single child content element. |
+| <span class="prop-name">children</span> | <span class="prop-type">element</span> |  | A single child content element.<br>⚠️ [Needs to be able to hold a ref](/guides/composition/#caveat-with-refs). |
 | <span class="prop-name">in</span> | <span class="prop-type">bool</span> |  | If `true`, the component will transition in. |
 | <span class="prop-name">timeout</span> | <span class="prop-type">union:&nbsp;number&nbsp;&#124;<br>&nbsp;{ enter?: number, exit?: number }<br></span> | <span class="prop-default">{  enter: duration.enteringScreen,  exit: duration.leavingScreen,}</span> | The duration for the transition, in milliseconds. You may specify a single timeout for all transitions, or individually with an object. |
 
diff --git a/pages/api/grow.md b/pages/api/grow.md
index 9229eaf61..ff5f4598b 100644
--- a/pages/api/grow.md
+++ b/pages/api/grow.md
@@ -20,7 +20,7 @@ It uses [react-transition-group](https://github.com/reactjs/react-transition-gro
 
 | Name | Type | Default | Description |
 |:-----|:-----|:--------|:------------|
-| <span class="prop-name">children</span> | <span class="prop-type">element</span> |  | A single child content element. |
+| <span class="prop-name">children</span> | <span class="prop-type">element</span> |  | A single child content element.<br>⚠️ [Needs to be able to hold a ref](/guides/composition/#caveat-with-refs). |
 | <span class="prop-name">in</span> | <span class="prop-type">bool</span> |  | If `true`, show the component; triggers the enter or exit animation. |
 | <span class="prop-name">timeout</span> | <span class="prop-type">union:&nbsp;number&nbsp;&#124;<br>&nbsp;{ enter?: number, exit?: number }&nbsp;&#124;<br>&nbsp;enum:&nbsp;'auto'<br><br></span> | <span class="prop-default">'auto'</span> | The duration for the transition, in milliseconds. You may specify a single timeout for all transitions, or individually with an object.<br>Set to 'auto' to automatically calculate transition time based on height. |
 
diff --git a/pages/api/slide.md b/pages/api/slide.md
index 1bb2e25e9..320bd2d1c 100644
--- a/pages/api/slide.md
+++ b/pages/api/slide.md
@@ -19,7 +19,7 @@ It uses [react-transition-group](https://github.com/reactjs/react-transition-gro
 
 | Name | Type | Default | Description |
 |:-----|:-----|:--------|:------------|
-| <span class="prop-name">children</span> | <span class="prop-type">element</span> |  | A single child content element.<br>⚠️The component used as a child [must be able to hold a ref](/guides/composition/#children). |
+| <span class="prop-name">children</span> | <span class="prop-type">element</span> |  | A single child content element.<br>⚠️The component used as a child [must be able to hold a ref](/guides/composition/#children).<br>⚠️ [Needs to be able to hold a ref](/guides/composition/#caveat-with-refs). |
 | <span class="prop-name">direction</span> | <span class="prop-type">enum:&nbsp;'left'&nbsp;&#124;<br>&nbsp;'right'&nbsp;&#124;<br>&nbsp;'up'&nbsp;&#124;<br>&nbsp;'down'<br></span> | <span class="prop-default">'down'</span> | Direction the child node will enter from. |
 | <span class="prop-name">in</span> | <span class="prop-type">bool</span> |  | If `true`, show the component; triggers the enter or exit animation. |
 | <span class="prop-name">timeout</span> | <span class="prop-type">union:&nbsp;number&nbsp;&#124;<br>&nbsp;{ enter?: number, exit?: number }<br></span> | <span class="prop-default">{  enter: duration.enteringScreen,  exit: duration.leavingScreen,}</span> | The duration for the transition, in milliseconds. You may specify a single timeout for all transitions, or individually with an object. |
diff --git a/pages/api/zoom.md b/pages/api/zoom.md
index 5eaa4bccd..48e79a642 100644
--- a/pages/api/zoom.md
+++ b/pages/api/zoom.md
@@ -20,7 +20,7 @@ It uses [react-transition-group](https://github.com/reactjs/react-transition-gro
 
 | Name | Type | Default | Description |
 |:-----|:-----|:--------|:------------|
-| <span class="prop-name">children</span> | <span class="prop-type">element</span> |  | A single child content element. |
+| <span class="prop-name">children</span> | <span class="prop-type">element</span> |  | A single child content element.<br>⚠️ [Needs to be able to hold a ref](/guides/composition/#caveat-with-refs). |
 | <span class="prop-name">in</span> | <span class="prop-type">bool</span> |  | If `true`, the component will transition in. |
 | <span class="prop-name">timeout</span> | <span class="prop-type">union:&nbsp;number&nbsp;&#124;<br>&nbsp;{ enter?: number, exit?: number }<br></span> | <span class="prop-default">{  enter: duration.enteringScreen,  exit: duration.leavingScreen,}</span> | The duration for the transition, in milliseconds. You may specify a single timeout for all transitions, or individually with an object. |
```

**assistant:** Slide's description already had a manual ref note, which is now duplicated. I'll remove the manual note from Slide's JSDoc and regenerate, then run the tests and lint.

**tool call: Bash**

```bash
cd /work/mui__material-ui-15526/repo; sed -n 224,233p packages/material-ui/src/Slide/Slide.js
```

tool result:

```
  );
});

Slide.propTypes = {
  /**
   * A single child content element.
   *
   * ⚠️The component used as a child [must be able to hold a ref](/guides/composition/#children).
   */
  children: elementAcceptingRef,
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-15526/repo; python3 - <<'EOF'
p='packages/material-ui/src/Slide/Slide.js'
s=open(p).read()
old="""   * A single child content element.
   *
   * ⚠️The component used as a child [must be able to hold a ref](/guides/composition/#children).
   */"""
assert old in s
s=s.replace(old,"""   * A single child content element.
   */""")
open(p,'w').write(s)
EOF
/work/mui__material-ui-15526/bin/envrun 'timeout 300 yarn -s docs:api:core >/tmp/docs.log 2>&1; echo docs $?; git diff --stat pages; NODE_ENV=test timeout 300 node_modules/.bin/mocha --exit "packages/material-ui/src/{Zoom,Fade,Grow,Slide,Snackbar,Popover,Popper,Tooltip,Menu,Dialog,SpeedDial,Modal}/**/*.test.js" "packages/material-ui-utils/src/**/*.test.js" 2>&1 | tail -15; node_modules/.bin/eslint packages/material-ui-utils/src packages/material-ui/src/{Zoom,Fade,Grow,Slide} docs/src/modules/utils/generateMarkdown.js && echo lint ok'
```

tool result:

```
docs 0
 pages/api/fade.md  | 2 +-
 pages/api/grow.md  | 2 +-
 pages/api/slide.md | 2 +-
 pages/api/zoom.md  | 2 +-
 4 files changed, 4 insertions(+), 4 deletions(-)
      at ReactWrapper.props (node_modules/enzyme/build/ReactWrapper.js:1013:21)
      at Context.props (packages/material-ui/src/Zoom/Zoom.test.js:143:44)
      at processImmediate (node:internal/timers:466:21)

  182) <Zoom />
       prop: appear
         should work when initially hidden: appear=false:
     Error: Method “props” is meant to be run on 1 node. 0 found instead.
      at ReactWrapper.single (node_modules/enzyme/build/ReactWrapper.js:1718:17)
      at ReactWrapper.props (node_modules/enzyme/build/ReactWrapper.js:1013:21)
      at Context.props (packages/material-ui/src/Zoom/Zoom.test.js:155:44)
      at processImmediate (node:internal/timers:466:21)



lint ok
```

**assistant:** 182 tests fail in that run. I need to know whether the failures already existed before my change, so I'll rerun the same set on a stashed (original) tree for comparison.

**tool call: Bash**

```bash
/work/mui__material-ui-15526/bin/envrun 'T="packages/material-ui/src/{Zoom,Fade,Grow,Slide,Snackbar,Popover,Popper,Tooltip,Menu,Dialog,SpeedDial,Modal}/**/*.test.js"; NODE_ENV=test timeout 300 node_modules/.bin/mocha --exit "$T" "packages/material-ui-utils/src/**/*.test.js" 2>&1 | grep -E "passing|failing|pending"; git stash -q -- packages docs; NODE_ENV=test timeout 300 node_modules/.bin/mocha --exit "$T" "packages/material-ui-utils/src/**/*.test.js" 2>&1 | grep -E "passing|failing|pending"; git stash pop -q; git status --short'
```

tool result:

```
  80 passing (33s)
  182 failing
  80 passing (33s)
  182 failing
 M docs/src/modules/utils/generateMarkdown.js
 M package.json
 M packages/material-ui-utils/src/index.js
 M packages/material-ui/src/Fade/Fade.js
 M packages/material-ui/src/Grow/Grow.js
 M packages/material-ui/src/Slide/Slide.js
 M packages/material-ui/src/Zoom/Zoom.js
 M pages/api/fade.md
 M pages/api/grow.md
 M pages/api/slide.md
 M pages/api/zoom.md
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
?? packages/material-ui-utils/src/elementAcceptingRef.js
```

**thinking:**

```
Results are the same with or without my change (80 passing, 182 failing), confirming the failures are caused by test interference rather than my edit. I'll run the transition and utils test files individually to verify.


```

**tool call: Bash**

```bash
/work/mui__material-ui-15526/bin/envrun 'for f in packages/material-ui/src/{Zoom,Fade,Grow,Slide}/*.test.js packages/material-ui-utils/src/*.test.js; do echo "$f: $(NODE_ENV=test timeout 200 node_modules/.bin/mocha --exit $f 2>&1 | grep -E "passing|failing" | tr "\n" " ")"; done'
```

tool result:

```
packages/material-ui/src/Zoom/Zoom.test.js:   3 passing (278ms)   3 failing 
packages/material-ui/src/Fade/Fade.test.js:   3 passing (264ms)   3 failing 
packages/material-ui/src/Grow/Grow.test.js:   3 passing (298ms)   7 failing 
packages/material-ui/src/Slide/Slide.test.js:   6 passing (309ms)   11 failing 
packages/material-ui-utils/src/chainPropTypes.test.js:   3 passing (115ms) 
packages/material-ui-utils/src/elementTypeAcceptingRef.test.js:   10 passing (218ms) 
packages/material-ui-utils/src/exactProp.test.js:   3 passing (114ms) 
packages/material-ui-utils/src/getDisplayName.test.js:   2 passing (108ms) 
packages/material-ui-utils/src/ponyfillGlobal.test.js:   0 passing (0ms)
```

**tool call: Bash**

```bash
/work/mui__material-ui-15526/bin/envrun 'NODE_ENV=test timeout 200 node_modules/.bin/mocha --exit packages/material-ui/src/Zoom/Zoom.test.js 2>&1 | grep -A8 "1) <Zoom"| head -30; git stash -q -- packages docs; for f in packages/material-ui/src/{Zoom,Fade,Grow,Slide}/*.test.js; do echo "$f: $(NODE_ENV=test timeout 200 node_modules/.bin/mocha --exit $f 2>&1 | grep -E "passing|failing" | tr "\n" " ")"; done; git stash pop -q'
```

tool result:

```
  1) <Zoom />
       transition lifecycle
         "before all" hook:
     TypeError: performance.mark is not a function
      at beginMark (node_modules/react-dom/cjs/react-dom.development.js:9130:15)
      at startWorkLoopTimer (node_modules/react-dom/cjs/react-dom.development.js:9388:5)
      at renderRoot (node_modules/react-dom/cjs/react-dom.development.js:19396:3)
      at performWorkOnRoot (node_modules/react-dom/cjs/react-dom.development.js:20307:7)
      at performWork (node_modules/react-dom/cjs/react-dom.development.js:20219:7)
packages/material-ui/src/Zoom/Zoom.test.js:   3 passing (274ms)   3 failing 
packages/material-ui/src/Fade/Fade.test.js:   3 passing (252ms)   3 failing 
packages/material-ui/src/Grow/Grow.test.js:   3 passing (284ms)   7 failing 
packages/material-ui/src/Slide/Slide.test.js:   6 passing (303ms)   11 failing
```

**thinking:**

```
These same per-file failures occur on the original tree too, confirming they're caused by an environment issue (Sinon's fake timers conflicting with React DOM on Node 16), not my change. I'll show the final source diff next.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-15526/repo; git diff packages docs/src; cat packages/material-ui-utils/src/elementAcceptingRef.js | tail -8
```

tool result:

```
diff --git a/docs/src/modules/utils/generateMarkdown.js b/docs/src/modules/utils/generateMarkdown.js
index 980553988..64cbe9232 100644
--- a/docs/src/modules/utils/generateMarkdown.js
+++ b/docs/src/modules/utils/generateMarkdown.js
@@ -78,6 +78,10 @@ function isElementTypeAcceptingRefProp(type) {
   return type.raw === 'elementTypeAcceptingRef';
 }
 
+function isElementAcceptingRefProp(type) {
+  return type.raw === 'elementAcceptingRef';
+}
+
 function generatePropDescription(prop) {
   const { description } = prop;
   const type = prop.flowType || prop.type;
@@ -151,7 +155,7 @@ function generatePropDescription(prop) {
   }
 
   let notes = '';
-  if (isElementTypeAcceptingRefProp(type)) {
+  if (isElementTypeAcceptingRefProp(type) || isElementAcceptingRefProp(type)) {
     notes += '<br>⚠️ [Needs to be able to hold a ref](/guides/composition/#caveat-with-refs).';
   }
 
@@ -164,6 +168,9 @@ function generatePropType(type) {
       if (isElementTypeAcceptingRefProp(type)) {
         return `element type`;
       }
+      if (isElementAcceptingRefProp(type)) {
+        return `element`;
+      }
 
       const deprecatedInfo = getDeprecatedInfo(type);
       if (deprecatedInfo !== false) {
diff --git a/packages/material-ui-utils/src/index.js b/packages/material-ui-utils/src/index.js
index 5a000566f..c8d84ec32 100644
--- a/packages/material-ui-utils/src/index.js
+++ b/packages/material-ui-utils/src/index.js
@@ -1,4 +1,5 @@
 export { default as chainPropTypes } from './chainPropTypes';
+export { default as elementAcceptingRef } from './elementAcceptingRef';
 export { default as elementTypeAcceptingRef } from './elementTypeAcceptingRef';
 export { default as exactProp } from './exactProp';
 export { default as getDisplayName } from './getDisplayName';
diff --git a/packages/material-ui/src/Fade/Fade.js b/packages/material-ui/src/Fade/Fade.js
index f3160bd65..8fd1a59ca 100644
--- a/packages/material-ui/src/Fade/Fade.js
+++ b/packages/material-ui/src/Fade/Fade.js
@@ -2,6 +2,7 @@
 
 import React from 'react';
 import PropTypes from 'prop-types';
+import { elementAcceptingRef } from '@material-ui/utils';
 import { Transition } from 'react-transition-group';
 import { duration } from '../styles/transitions';
 import withTheme from '../styles/withTheme';
@@ -74,7 +75,7 @@ Fade.propTypes = {
   /**
    * A single child content element.
    */
-  children: PropTypes.element,
+  children: elementAcceptingRef,
   /**
    * If `true`, the component will transition in.
    */
diff --git a/packages/material-ui/src/Grow/Grow.js b/packages/material-ui/src/Grow/Grow.js
index a4fcfd98b..b1d274bf5 100644
--- a/packages/material-ui/src/Grow/Grow.js
+++ b/packages/material-ui/src/Grow/Grow.js
@@ -2,6 +2,7 @@
 
 import React from 'react';
 import PropTypes from 'prop-types';
+import { elementAcceptingRef } from '@material-ui/utils';
 import { Transition } from 'react-transition-group';
 import withTheme from '../styles/withTheme';
 import { reflow, getTransitionProps } from '../transitions/utils';
@@ -140,7 +141,7 @@ Grow.propTypes = {
   /**
    * A single child content element.
    */
-  children: PropTypes.element,
+  children: elementAcceptingRef,
   /**
    * If `true`, show the component; triggers the enter or exit animation.
    */
diff --git a/packages/material-ui/src/Slide/Slide.js b/packages/material-ui/src/Slide/Slide.js
index ac93b39f2..07989104a 100644
--- a/packages/material-ui/src/Slide/Slide.js
+++ b/packages/material-ui/src/Slide/Slide.js
@@ -2,6 +2,7 @@
 
 import React from 'react';
 import PropTypes from 'prop-types';
+import { elementAcceptingRef } from '@material-ui/utils';
 import ReactDOM from 'react-dom';
 import debounce from 'debounce'; // < 1kb payload overhead when lodash/debounce is > 3kb.
 import { Transition } from 'react-transition-group';
@@ -226,10 +227,8 @@ const Slide = React.forwardRef(function Slide(props, ref) {
 Slide.propTypes = {
   /**
    * A single child content element.
-   *
-   * ⚠️The component used as a child [must be able to hold a ref](/guides/composition/#children).
    */
-  children: PropTypes.element,
+  children: elementAcceptingRef,
   /**
    * Direction the child node will enter from.
    */
diff --git a/packages/material-ui/src/Zoom/Zoom.js b/packages/material-ui/src/Zoom/Zoom.js
index b0e37b153..97ae44eb6 100644
--- a/packages/material-ui/src/Zoom/Zoom.js
+++ b/packages/material-ui/src/Zoom/Zoom.js
@@ -2,6 +2,7 @@
 
 import React from 'react';
 import PropTypes from 'prop-types';
+import { elementAcceptingRef } from '@material-ui/utils';
 import { Transition } from 'react-transition-group';
 import { duration } from '../styles/transitions';
 import withTheme from '../styles/withTheme';
@@ -75,7 +76,7 @@ Zoom.propTypes = {
   /**
    * A single child content element.
    */
-  children: PropTypes.element,
+  children: elementAcceptingRef,
   /**
    * If `true`, the component will transition in.
    */

  return null;
}

const elementAcceptingRef = chainPropTypes(PropTypes.element, acceptingRef);
elementAcceptingRef.isRequired = chainPropTypes(PropTypes.element.isRequired, acceptingRef);

export default elementAcceptingRef;
```

**assistant:** Zoom still needs a child that can hold a ref, so it can't work with a plain function component like Formik's `<Field>`. What I changed is that you now get a clear warning explaining the problem, instead of React's vague one.

**Why it broke in v4:** Zoom (and Fade, Grow, Slide) now attach a ref to their child to find the DOM node they animate. Function components can't take refs, so the animation can't reach the node. React's only signal was "Function components cannot be given refs… Check the render method of `Transition`", which doesn't say what's wrong.

**Changes:**
- **New `elementAcceptingRef` prop-type** in `packages/material-ui-utils/src/elementAcceptingRef.js`, exported from `@material-ui/utils`. It works like the existing `elementTypeAcceptingRef`, but checks an element (`children`) rather than a component type. It warns when the element is a plain function component; DOM elements, class components and `forwardRef` components pass. It also has an `.isRequired` variant.
- **Zoom, Fade, Grow and Slide** now use it for `children`. Your example now logs:
  > Invalid prop `children` supplied to `ForwardRef(Zoom)`. Expected an element that can hold a ref. Did you accidentally use a plain function component for an element instead? For more information see https://next.material-ui.com/guides/composition/#caveat-with-refs
- **Docs:** `generateMarkdown.js` recognises the new prop-type, and I regenerated `pages/api/{fade,grow,slide,zoom}.md`. Each now shows a "⚠️ Needs to be able to hold a ref" note on `children`. I removed Slide's hand-written copy of that note so it doesn't appear twice.

**The fix for the user** is to give Zoom something that can hold a ref: either keep the `<div>` wrapper, or make the child forward its ref with `React.forwardRef`.

**Testing:**
- A temporary test confirmed the new warning for a plain function component child, and no warnings for `forwardRef`, class or DOM children. I deleted it afterwards.
- ESLint passes on the changed files, and the utils package tests pass.
- The existing Zoom, Fade, Grow and Slide test files have failures in this container, but the counts are identical with and without my change. The error is `performance.mark is not a function`: Sinon's fake timers clash with React DOM on Node 16, which is an environment problem rather than this change.

**Not mine:** `package.json` and `yarn.lock` were already modified and `Dockerfile` and `custom-reporter.js` were untracked before I started; they look like environment setup, and I left them alone.

_session end: success, turns 27, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.13 s: ps aux | head -20
- `rc=0` 688.26 s: cat package.json | grep "\"test:unit"; NODE_ENV=test yarn -s mocha packages/material-ui/src/Zoom/repro.test.js 2>&1 | tail -40
- `rc=0` 1.88 s: kill 37 30 17; NODE_ENV=test timeout 100 node_modules/.bin/mocha --exit packages/material-ui/src/Zoom/repro.test.js 2>&1 | tail -40
- `rc=128` 17.8 s: timeout 300 yarn -s docs:api:core >/tmp/docs.log 2>&1; echo $?; tail -5 /tmp/docs.log; git status --short; git diff docs/pages
- `rc=0` 51.06 s: timeout 300 yarn -s docs:api:core >/tmp/docs.log 2>&1; echo docs $?; git diff --stat pages; NODE_ENV=test timeout 300 node_modules/.bin/mocha --exit "packages/material-ui/src/{Zoom,Fade,Grow,Slide,Snackbar,Popover,Popper,Tooltip,Menu,Dialog,SpeedDial,Modal}/**/*.test.js" "packages/material-ui-utils/src/**/*.test.js" 2>&1 | tail -15; node_modules/.bin/eslint packages/material-ui-utils/src packages/material-ui/src/{Zoom,Fade,Grow,Slide} docs/src/modules/utils/generateMarkdown.js && echo lint ok
- `rc=0` 71.04 s: T="packages/material-ui/src/{Zoom,Fade,Grow,Slide,Snackbar,Popover,Popper,Tooltip,Menu,Dialog,SpeedDial,Modal}/**/*.test.js"; NODE_ENV=test timeout 300 node_modules/.bin/mocha --exit "$T" "packages/material-ui-utils/src/**/*.test.js" 2>&1 | grep -E "passing|failing|pending"; git stash -q -- packages docs; NODE_ENV=test timeout 300 node_modules/.bin/mocha --exit "$T" "packages/material-ui-utils/src/**/*.test.js" 2>&1 | grep -E "passing|failing|pending"; git stash pop -q; git status --short
- `rc=0` 17.79 s: for f in packages/material-ui/src/{Zoom,Fade,Grow,Slide}/*.test.js packages/material-ui-utils/src/*.test.js; do echo "$f: $(NODE_ENV=test timeout 200 node_modules/.bin/mocha --exit $f 2>&1 | grep -E "passing|failing" | tr "\n" " ")"; done
- `rc=0` 11.46 s: NODE_ENV=test timeout 200 node_modules/.bin/mocha --exit packages/material-ui/src/Zoom/Zoom.test.js 2>&1 | grep -A8 "1) <Zoom"| head -30; git stash -q -- packages docs; for f in packages/material-ui/src/{Zoom,Fade,Grow,Slide}/*.test.js; do echo "$f: $(NODE_ENV=test timeout 200 node_modules/.bin/mocha --exit $f 2>&1 | grep -E "passing|failing" | tr "\n" " ")"; done; git stash pop -q
