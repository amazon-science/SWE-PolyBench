# Instance: mui__material-ui-28186

- Final resolved (evaluator, logs/mui__material-ui-28186_result.json): True
- Run state: DONE
- One attempt. Duration 811.5 s, turns 36, actor cost $0.9197175999999999, container commands 6
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/mui__material-ui-28186/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-28186/repo. Consider the following issue description:

<issue_description>
[ButtonBase] Unfocus does not clear ripple
<!-- Provide a general summary of the issue in the Title above -->

keyboard tab between ButtonBase component does not clear the focus ripple. I can confirm that revert the code on this commit does not have this issue (in `ButtonBase.js`). https://github.com/mui-org/material-ui/commit/5f30983bfa16195237fde55a78d5e43b151a29fa

cc @michaldudak can you help take a look?

<!--
  Thank you very much for contributing to Material-UI by creating an issue! ❤️
  To avoid duplicate issues we ask you to check off the following list.
-->

<!-- Checked checkbox should look like this: [x] -->

- [x] The issue is present in the latest release.
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Current Behavior 😯

<!-- Describe what happens instead of the expected behavior. -->

<img width="1440" alt="Screen Shot 2564-09-06 at 14 58 24" src="https://user-images.githubusercontent.com/18292247/132181388-0bdc536c-db56-4330-97a8-8e6b2542e371.png">

## Expected Behavior 🤔

it should clear the ripple element
<!-- Describe what should happen. -->

## Steps to Reproduce 🕹

<!--
  Provide a link to a live example (you can use codesandbox.io) and an unambiguous set of steps to reproduce this bug.
  Include code to reproduce, if relevant (which it most likely is).

  You should use the official codesandbox template as a starting point: https://material-ui.com/r/issue-template-next

  If you have an issue concerning TypeScript please start from this TypeScript playground: https://material-ui.com/r/ts-issue-template

  Issues without some form of live example have a longer response time.
-->

Steps:

1. open https://next.material-ui.com/components/buttons/#main-content
2. tab through the docs
3.
4.

## Context 🔦

<!--
  What are you trying to accomplish? How has this issue affected you?
  Providing context helps us come up with a solution that is most useful in the real world.
-->

## Your Environment 🌎

<!--
  Run `npx @mui/envinfo` and post the results.
  If you encounter issues with TypeScript please include the used tsconfig.
-->
<details>
  <summary>`npx @mui/envinfo`</summary>
  
```
  Don't forget to mention which browser you used.
  Output from `npx @mui/envinfo` goes here.
```
</details>


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-28186/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-28186/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-28186/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-28186/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/mui__material-ui-28186/repo; grep -n "useRippleHandler\|handleBlur\|focusVisible\|Ripple" packages/mui-core/src/ButtonBase/ButtonBase.js packages/material-ui/src/ButtonBase/ButtonBase.js 2>/dev/null | head -80
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; find packages -name "ButtonBase*.js" -o -name "useButton*" | grep -v node_modules
```

tool result:

```
packages/mui-material/src/ButtonBase/ButtonBase.test.js
packages/mui-material/src/ButtonBase/ButtonBase.js
packages/mui-core/src/ButtonUnstyled/useButton.ts
packages/mui-core/src/ButtonUnstyled/useButton.test.tsx
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; cat packages/mui-core/src/ButtonUnstyled/useButton.ts; sed -n 1,260p packages/mui-material/src/ButtonBase/ButtonBase.js
```

tool result:

```
import * as React from 'react';
import {
  unstable_useEventCallback as useEventCallback,
  unstable_useForkRef as useForkRef,
  unstable_useIsFocusVisible as useIsFocusVisible,
} from '@mui/utils';
import UseButtonProps from './UseButtonProps';
import extractEventHandlers from '../utils/extractEventHandlers';

export default function useButton(props: UseButtonProps) {
  const { component, components = {}, disabled = false, href, ref, tabIndex = 0, to, type } = props;

  const buttonRef = React.useRef<HTMLButtonElement | HTMLAnchorElement | HTMLElement>();

  const [active, setActive] = React.useState<boolean>(false);

  const {
    isFocusVisibleRef,
    onFocus: handleFocusVisible,
    onBlur: handleBlurVisible,
    ref: focusVisibleRef,
  } = useIsFocusVisible();

  const [focusVisible, setFocusVisible] = React.useState(false);
  if (disabled && focusVisible) {
    setFocusVisible(false);
  }

  React.useEffect(() => {
    isFocusVisibleRef.current = focusVisible;
  }, [focusVisible, isFocusVisibleRef]);

  const handleMouseLeave =
    (otherHandlers: Record<string, React.EventHandler<any>>) => (event: React.MouseEvent) => {
      if (focusVisible) {
        event.preventDefault();
      }

      otherHandlers.onMouseLeave?.(event);
    };

  const handleBlur =
    (otherHandlers: Record<string, React.EventHandler<any>>) => (event: React.FocusEvent) => {
      handleBlurVisible(event);

      if (isFocusVisibleRef.current === false) {
        setFocusVisible(false);
      }

      otherHandlers.onBlur?.(event);
    };

  const handleFocus = useEventCallback(
    (otherHandlers: Record<string, React.EventHandler<any>>) =>
      (event: React.FocusEvent<HTMLButtonElement>) => {
        // Fix for https://github.com/facebook/react/issues/7769
        if (!buttonRef.current) {
          buttonRef.current = event.currentTarget;
        }

        handleFocusVisible(event);
        if (isFocusVisibleRef.current === true) {
          setFocusVisible(true);
          otherHandlers.onFocusVisible?.(event);
        }

        otherHandlers.onFocus?.(event);
      },
  );

  const elementType = component ?? components.Root ?? 'button';

  const isNonNativeButton = () => {
    const button = buttonRef.current;
    return (
      elementType !== 'button' && !(button?.tagName === 'A' && (button as HTMLAnchorElement)?.href)
    );
  };

  const handleMouseDown =
    (otherHandlers: Record<string, React.EventHandler<any>>) =>
    (event: React.MouseEvent<HTMLButtonElement>) => {
      if (event.target === event.currentTarget && !disabled) {
        setActive(true);
      }

      otherHandlers.onMouseDown?.(event);
    };

  const handleMouseUp =
    (otherHandlers: Record<string, React.EventHandler<any>>) =>
    (event: React.MouseEvent<HTMLButtonElement>) => {
      if (event.target === event.currentTarget) {
        setActive(false);
      }

      otherHandlers.onMouseUp?.(event);
    };

  const handleKeyDown = useEventCallback(
    (otherHandlers: Record<string, React.EventHandler<any>>) => (event: React.KeyboardEvent) => {
      if (event.target === event.currentTarget && isNonNativeButton() && event.key === ' ') {
        event.preventDefault();
      }

      if (event.target === event.currentTarget && event.key === ' ' && !disabled) {
        setActive(true);
      }

      otherHandlers.onKeyDown?.(event);

      // Keyboard accessibility for non interactive elements
      if (
        event.target === event.currentTarget &&
        isNonNativeButton() &&
        event.key === 'Enter' &&
        !disabled
      ) {
        event.preventDefault();
        otherHandlers.onClick?.(event);
      }
    },
  );

  const handleKeyUp = useEventCallback(
    (otherHandlers: Record<string, React.EventHandler<any>>) => (event: React.KeyboardEvent) => {
      // calling preventDefault in keyUp on a <button> will not dispatch a click event if Space is pressed
      // https://codesandbox.io/s/button-keyup-preventdefault-dn7f0

      if (event.target === event.currentTarget) {
        setActive(false);
      }

      otherHandlers.onKeyUp?.(event);

      // Keyboard accessibility for non interactive elements
      if (
        event.target === event.currentTarget &&
        isNonNativeButton() &&
        event.key === ' ' &&
        !event.defaultPrevented
      ) {
        otherHandlers.onClick?.(event);
      }
    },
  );

  const buttonProps: Record<string, unknown> = {};
  if (elementType === 'button') {
    buttonProps.type = type ?? 'button';
    buttonProps.disabled = disabled;
  } else {
    if (!href && !to) {
      buttonProps.role = 'button';
    }
    if (disabled) {
      buttonProps['aria-disabled'] = disabled;
    }
  }

  const handleOwnRef = useForkRef(focusVisibleRef, buttonRef);
  const handleRef = useForkRef(ref, handleOwnRef);

  const getRootProps = (otherHandlers?: Record<string, React.EventHandler<any>>) => {
    const propsEventHandlers = extractEventHandlers(props);
    const externalEventHandlers = { ...propsEventHandlers, ...otherHandlers };

    const ownEventHandlers = {
      onBlur: handleBlur(externalEventHandlers),
      onFocus: handleFocus(externalEventHandlers),
      onKeyDown: handleKeyDown(externalEventHandlers),
      onKeyUp: handleKeyUp(externalEventHandlers),
      onMouseDown: handleMouseDown(externalEventHandlers),
      onMouseLeave: handleMouseLeave(externalEventHandlers),
      onMouseUp: handleMouseUp(externalEventHandlers),
    };

    const mergedEventHandlers: Record<string, React.EventHandler<any>> = {
      ...externalEventHandlers,
      ...ownEventHandlers,
    };

    // onFocusVisible can be present on the props, but since it's not a valid React event handler,
    // it must not be forwarded to the inner component.
    delete mergedEventHandlers.onFocusVisible;

    return {
      tabIndex: disabled ? -1 : tabIndex,
      type,
      ref: handleRef as React.Ref<any>,
      ...buttonProps,
      ...mergedEventHandlers,
    };
  };

  return {
 
[... 7542 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; sed -n 260,400p packages/mui-material/src/ButtonBase/ButtonBase.js
```

tool result:

```
   */
  LinkComponent: PropTypes.elementType,
  /**
   * @ignore
   */
  onBlur: PropTypes.func,
  /**
   * @ignore
   */
  onClick: PropTypes.func,
  /**
   * @ignore
   */
  onContextMenu: PropTypes.func,
  /**
   * @ignore
   */
  onDragLeave: PropTypes.func,
  /**
   * @ignore
   */
  onFocus: PropTypes.func,
  /**
   * Callback fired when the component is focused with a keyboard.
   * We trigger a `onFocus` callback too.
   */
  onFocusVisible: PropTypes.func,
  /**
   * @ignore
   */
  onKeyDown: PropTypes.func,
  /**
   * @ignore
   */
  onKeyUp: PropTypes.func,
  /**
   * @ignore
   */
  onMouseDown: PropTypes.func,
  /**
   * @ignore
   */
  onMouseLeave: PropTypes.func,
  /**
   * @ignore
   */
  onMouseUp: PropTypes.func,
  /**
   * @ignore
   */
  onTouchEnd: PropTypes.func,
  /**
   * @ignore
   */
  onTouchMove: PropTypes.func,
  /**
   * @ignore
   */
  onTouchStart: PropTypes.func,
  /**
   * The system prop that allows defining system overrides as well as additional CSS styles.
   */
  sx: PropTypes.object,
  /**
   * @default 0
   */
  tabIndex: PropTypes.number,
  /**
   * Props applied to the `TouchRipple` element.
   */
  TouchRippleProps: PropTypes.object,
  /**
   * @ignore
   */
  type: PropTypes.oneOfType([PropTypes.oneOf(['button', 'reset', 'submit']), PropTypes.string]),
};

export default ButtonBase;
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; ls packages/mui-material/src/useTouchRipple; cat packages/mui-material/src/useTouchRipple/useTouchRipple.ts; cat packages/mui-core/src/utils/extractEventHandlers.ts
```

tool result:

```
index.ts
useTouchRipple.ts
import * as React from 'react';
import { TouchRippleActions } from '../ButtonBase/TouchRipple';
import { useEventCallback } from '../utils';

interface UseTouchRippleProps {
  disabled: boolean;
  disableFocusRipple?: boolean;
  disableRipple?: boolean;
  disableTouchRipple?: boolean;
  focusVisible: boolean;
  rippleRef: React.RefObject<TouchRippleActions>;
}

interface RippleEventHandlers {
  onBlur: React.FocusEventHandler;
  onContextMenu: React.MouseEventHandler;
  onDragLeave: React.DragEventHandler;
  onKeyDown: React.KeyboardEventHandler;
  onKeyUp: React.KeyboardEventHandler;
  onMouseDown: React.MouseEventHandler;
  onMouseLeave: React.MouseEventHandler;
  onMouseUp: React.MouseEventHandler;
  onTouchEnd: React.TouchEventHandler;
  onTouchMove: React.TouchEventHandler;
  onTouchStart: React.TouchEventHandler;
}

const useTouchRipple = (props: UseTouchRippleProps) => {
  const {
    disabled,
    disableFocusRipple,
    disableRipple,
    disableTouchRipple,
    focusVisible,
    rippleRef,
  } = props;

  React.useEffect(() => {
    if (focusVisible && !disableFocusRipple && !disableRipple) {
      rippleRef.current?.pulsate();
    }
  }, [rippleRef, focusVisible, disableFocusRipple, disableRipple]);

  function useRippleHandler(
    rippleAction: keyof TouchRippleActions,
    eventCallback?: (event: React.SyntheticEvent) => void,
    skipRippleAction = disableTouchRipple,
  ) {
    return useEventCallback((event: React.SyntheticEvent) => {
      eventCallback?.(event);

      if (!skipRippleAction && rippleRef.current) {
        rippleRef.current[rippleAction](event);
      }

      return true;
    });
  }

  const keydownRef = React.useRef(false);
  const handleKeyDown = useEventCallback((event: React.KeyboardEvent) => {
    if (
      !disableFocusRipple &&
      !keydownRef.current &&
      focusVisible &&
      rippleRef.current &&
      event.key === ' '
    ) {
      keydownRef.current = true;
      rippleRef.current.stop(event, () => {
        rippleRef?.current?.start(event);
      });
    }
  });

  const handleKeyUp = useEventCallback((event: React.KeyboardEvent) => {
    // calling preventDefault in keyUp on a <button> will not dispatch a click event if Space is pressed
    // https://codesandbox.io/s/button-keyup-preventdefault-dn7f0
    if (
      !disableFocusRipple &&
      event.key === ' ' &&
      rippleRef.current &&
      focusVisible &&
      !event.defaultPrevented
    ) {
      keydownRef.current = false;
      rippleRef.current.stop(event, () => {
        rippleRef?.current?.pulsate(event);
      });
    }
  });

  const handleBlur = useRippleHandler('stop');
  const handleMouseDown = useRippleHandler('start');
  const handleContextMenu = useRippleHandler('stop');
  const handleDragLeave = useRippleHandler('stop');
  const handleMouseUp = useRippleHandler('stop');
  const handleMouseLeave = useRippleHandler('stop');
  const handleTouchStart = useRippleHandler('start');
  const handleTouchEnd = useRippleHandler('stop');
  const handleTouchMove = useRippleHandler('stop');

  const [mountedState, setMountedState] = React.useState(false);

  React.useEffect(() => {
    setMountedState(true);
  }, []);

  const enableTouchRipple = mountedState && !disableRipple && !disabled;

  const getRippleHandlers = React.useMemo(() => {
    const rippleHandlers = {
      onBlur: handleBlur,
      onKeyDown: handleKeyDown,
      onKeyUp: handleKeyUp,
      onMouseDown: handleMouseDown,
      onMouseUp: handleMouseUp,
      onMouseLeave: handleMouseLeave,
      onContextMenu: handleContextMenu,
      onDragLeave: handleDragLeave,
      onTouchStart: handleTouchStart,
      onTouchEnd: handleTouchEnd,
      onTouchMove: handleTouchMove,
    } as RippleEventHandlers;

    return (otherEvents: Partial<RippleEventHandlers> = {}) => {
      const eventNames = Object.keys(rippleHandlers) as (keyof RippleEventHandlers)[];
      const wrappedEvents = eventNames.map((eventName) => ({
        name: eventName,
        handler: (ev: any) => {
          otherEvents[eventName]?.(ev);
          rippleHandlers[eventName](ev);
        },
      }));

      return wrappedEvents.reduce((acc, current) => {
        acc[current.name] = current.handler;
        return acc;
      }, {} as RippleEventHandlers);
    };
  }, [
    handleBlur,
    handleKeyDown,
    handleKeyUp,
    handleMouseDown,
    handleMouseUp,
    handleMouseLeave,
    handleContextMenu,
    handleDragLeave,
    handleTouchStart,
    handleTouchEnd,
    handleTouchMove,
  ]);

  return {
    enableTouchRipple,
    getRippleHandlers,
  };
};

export default useTouchRipple;
/**
 * Extracts event handlers from a given object.
 * A prop is considered an event handler if it is a function and its name starts with `on`.
 *
 * @param object An object to extract event handlers from.
 */
export default function extractEventHandlers(object: Record<string, any> | undefined) {
  if (object === undefined) {
    return {};
  }

  const result: Record<string, React.EventHandler<any>> = {};

  Object.keys(object)
    .filter((prop) => prop.match(/^on[A-Z]/) && typeof object[prop] === 'function')
    .forEach((prop) => {
      result[prop] = object[prop];
    });

  return result;
}
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; grep -n "stop = \|const stop\|pulsate\|start = " -A25 packages/mui-material/src/ButtonBase/TouchRipple.js | sed -n 1,200p | grep -n "" | sed -n 1,140p
```

tool result:

```
1:36:const pulsateKeyframe = keyframes`
2:37-  0% {
3:38-    transform: scale(1);
4:39-  }
5:40-
6:41-  50% {
7:42-    transform: scale(0.92);
8:43-  }
9:44-
10:45-  100% {
11:46-    transform: scale(1);
12:47-  }
13:48-`;
14:49-
15:50-export const TouchRippleRoot = styled('span', {
16:51-  name: 'MuiTouchRipple',
17:52-  slot: 'Root',
18:53-  skipSx: true,
19:54-})({
20:55-  overflow: 'hidden',
21:56-  pointerEvents: 'none',
22:57-  position: 'absolute',
23:58-  zIndex: 0,
24:59-  top: 0,
25:60-  right: 0,
26:61-  bottom: 0,
27:--
28:108:    animation-name: ${pulsateKeyframe};
29:109-    animation-duration: 2500ms;
30:110-    animation-timing-function: ${({ theme }) => theme.transitions.easing.easeInOut};
31:111-    animation-iteration-count: infinite;
32:112-    animation-delay: 200ms;
33:113-  }
34:114-`;
35:115-
36:116-/**
37:117- * @ignore - internal component.
38:118- *
39:119- * TODO v5: Make private
40:120- */
41:121-const TouchRipple = React.forwardRef(function TouchRipple(inProps, ref) {
42:122-  const props = useThemeProps({ props: inProps, name: 'MuiTouchRipple' });
43:123-
44:124-  const { center: centerProp = false, classes = {}, className, ...other } = props;
45:125-  const [ripples, setRipples] = React.useState([]);
46:126-  const nextKey = React.useRef(0);
47:127-  const rippleCallback = React.useRef(null);
48:128-
49:129-  React.useEffect(() => {
50:130-    if (rippleCallback.current) {
51:131-      rippleCallback.current();
52:132-      rippleCallback.current = null;
53:133-    }
54:--
55:154:      const { pulsate, rippleX, rippleY, rippleSize, cb } = params;
56:155-
57:156-      setRipples((oldRipples) => [
58:157-        ...oldRipples,
59:158-        <TouchRippleRipple
60:159-          key={nextKey.current}
61:160-          classes={{
62:161-            ripple: clsx(classes.ripple, touchRippleClasses.ripple),
63:162-            rippleVisible: clsx(classes.rippleVisible, touchRippleClasses.rippleVisible),
64:163-            ripplePulsate: clsx(classes.ripplePulsate, touchRippleClasses.ripplePulsate),
65:164-            child: clsx(classes.child, touchRippleClasses.child),
66:165-            childLeaving: clsx(classes.childLeaving, touchRippleClasses.childLeaving),
67:166-            childPulsate: clsx(classes.childPulsate, touchRippleClasses.childPulsate),
68:167-          }}
69:168-          timeout={DURATION}
70:169:          pulsate={pulsate}
71:170-          rippleX={rippleX}
72:171-          rippleY={rippleY}
73:172-          rippleSize={rippleSize}
74:173-        />,
75:174-      ]);
76:175-      nextKey.current += 1;
77:176-      rippleCallback.current = cb;
78:177-    },
79:178-    [classes],
80:179-  );
81:180-
82:181:  const start = React.useCallback(
83:182-    (event = {}, options = {}, cb) => {
84:183-      const {
85:184:        pulsate = false,
86:185:        center = centerProp || options.pulsate,
87:186-        fakeElement = false, // For test purposes
88:187-      } = options;
89:188-
90:189-      if (event.type === 'mousedown' && ignoringMouseDown.current) {
91:190-        ignoringMouseDown.current = false;
92:191-        return;
93:192-      }
94:193-
95:194-      if (event.type === 'touchstart') {
96:195-        ignoringMouseDown.current = true;
97:196-      }
98:197-
99:198-      const element = fakeElement ? null : container.current;
100:199-      const rect = element
101:200-        ? element.getBoundingClientRect()
102:201-        : {
103:202-            width: 0,
104:203-            height: 0,
105:204-            left: 0,
106:205-            top: 0,
107:206-          };
108:207-
109:208-      // Get the size of the ripple
110:209-      let rippleX;
111:210-      let rippleY;
112:--
113:249:            startCommit({ pulsate, rippleX, rippleY, rippleSize, cb });
114:250-          };
115:251-          // Delay the execution of the ripple effect.
116:252-          startTimer.current = setTimeout(() => {
117:253-            if (startTimerCommit.current) {
118:254-              startTimerCommit.current();
119:255-              startTimerCommit.current = null;
120:256-            }
121:257-          }, DELAY_RIPPLE); // We have to make a tradeoff with this value.
122:258-        }
123:259-      } else {
124:260:        startCommit({ pulsate, rippleX, rippleY, rippleSize, cb });
125:261-      }
126:262-    },
127:263-    [centerProp, startCommit],
128:264-  );
129:265-
130:266:  const pulsate = React.useCallback(() => {
131:267:    start({}, { pulsate: true });
132:268-  }, [start]);
133:269-
134:270:  const stop = React.useCallback((event, cb) => {
135:271-    clearTimeout(startTimer.current);
136:272-
137:273-    // The touch interaction occurs too quickly.
138:274-    // We still want to show ripple effect.
139:275-    if (event.type === 'touchend' && startTimerCommit.current) {
140:276-      startTimerCommit.current();
```

**assistant:** Let me check the existing tests around blur/focus ripple to see what's expected.

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; grep -n "blur\|Blur" packages/mui-material/src/ButtonBase/ButtonBase.test.js | head -40; git log --oneline -3
```

tool result:

```
177:      const onBlur = spy();
192:          onBlur={onBlur}
249:        button.blur();
251:      expect(onBlur.callCount).to.equal(1);
347:      it('should stop the ripple when the button blurs', () => {
362:        button.blur();
668:    it('should stop on blur and set focusVisible to false', () => {
685:        button.blur();
821:              onBlur={() => eventLog.push('blur')}
838:      expect(eventLog).to.deep.equal(['focus-visible', 'focus', 'blur']);
f588d8fdf6 [codemod] Fix various reported issues on `preset-safe` (#28183)
49b3469442 [core] Rename directories to match the new package names (#28185)
2db48e8cab [core] Remove unused include (#28187)
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; sed -n 330,375p packages/mui-material/src/ButtonBase/ButtonBase.test.js; sed -n 640,700p packages/mui-material/src/ButtonBase/ButtonBase.test.js
```

tool result:

```
                childLeaving: 'child-leaving',
              },
            }}
          />,
        );
        const button = getByRole('button');
        fireEvent.mouseDown(button);
        fireEvent.mouseUp(button);

        fireEvent.mouseDown(button);

        expect(button.querySelectorAll('.ripple-visible .child-leaving')).to.have.lengthOf(1);
        expect(
          button.querySelectorAll('.ripple-visible .child:not(.child-leaving)'),
        ).to.have.lengthOf(1);
      });

      it('should stop the ripple when the button blurs', () => {
        const { getByRole } = render(
          <ButtonBase
            TouchRippleProps={{
              classes: {
                rippleVisible: 'ripple-visible',
                child: 'child',
                childLeaving: 'child-leaving',
              },
            }}
          />,
        );
        const button = getByRole('button');
        fireEvent.mouseDown(button);

        button.blur();

        expect(button.querySelectorAll('.ripple-visible .child-leaving')).to.have.lengthOf(0);
        expect(
          button.querySelectorAll('.ripple-visible .child:not(.child-leaving)'),
        ).to.have.lengthOf(1);
      });

      it('should restart the ripple when the mouse is pressed again', () => {
        const { getByRole } = render(
          <ButtonBase
            TouchRippleProps={{
              classes: {
                rippleVisible: 'ripple-visible',
      expect(button.querySelectorAll('.ripple-visible')).to.have.lengthOf(0);
    });

    it('should stop and re-pulsate when space bar is released', () => {
      const { getByRole } = render(
        <ButtonBase
          focusRipple
          TouchRippleProps={{
            classes: {
              childLeaving: 'child-leaving',
              ripplePulsate: 'ripple-pulsate',
              rippleVisible: 'ripple-visible',
            },
          }}
        />,
      );
      const button = getByRole('button');

      simulatePointerDevice();
      focusVisible(button);
      fireEvent.keyDown(button, { key: ' ' });
      fireEvent.keyUp(button, { key: ' ' });

      expect(button.querySelectorAll('.ripple-pulsate .child-leaving')).to.have.lengthOf(1);
      expect(button.querySelectorAll('.ripple-pulsate')).to.have.lengthOf(2);
      expect(button.querySelectorAll('.ripple-visible')).to.have.lengthOf(3);
    });

    it('should stop on blur and set focusVisible to false', () => {
      const { getByRole } = render(
        <ButtonBase
          focusRipple
          TouchRippleProps={{
            classes: {
              childLeaving: 'child-leaving',
              rippleVisible: 'ripple-visible',
            },
          }}
        />,
      );
      const button = getByRole('button');
      simulatePointerDevice();
      focusVisible(button);

      act(() => {
        button.blur();
      });

      expect(button.querySelectorAll('.ripple-visible .child-leaving')).to.have.lengthOf(1);
    });
  });

  describe('prop: disabled', () => {
    it('should have a negative tabIndex', () => {
      const { getByText } = render(<ButtonBase disabled>Hello</ButtonBase>);
      expect(getByText('Hello')).to.have.property('tabIndex', -1);
    });

    it('should forward it to native buttons', () => {
      const { getByText } = render(
        <ButtonBase disabled component="button">
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; grep -rn "disableTouchRipple" packages/mui-material/src --include=*.js | grep -v "\.d\.ts\|PropTypes\|@default\|\* " | head -20; git show --stat HEAD~0 | head; git status
```

tool result:

```
(eval):1: no matches found: --include=*.js
commit f588d8fdf63b8558e26cfa288f20ff400140ed6c
Author: Marija Najdova <mnajdova@gmail.com>
Date:   Mon Sep 6 21:52:04 2021 +0200

    [codemod] Fix various reported issues on `preset-safe` (#28183)

 packages/mui-codemod/src/util/renameClassKey.js                     | 2 +-
 packages/mui-codemod/src/v5.0.0/avatar-circle-circular.js           | 2 +-
 packages/mui-codemod/src/v5.0.0/badge-overlap-value.js              | 4 ++--
 packages/mui-codemod/src/v5.0.0/circularprogress-variant.js         | 2 +-
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   package.json
	modified:   yarn.lock

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Dockerfile
	custom-reporter.js

no changes added to commit (use "git add" and/or "git commit -a")
```

**assistant:** Let me write a quick repro test that tabs between two buttons.

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; sed -n 1,30p packages/mui-material/src/ButtonBase/ButtonBase.test.js; grep -rn "export function focusVisible" -A12 test/utils/ ; sed -n 270,300p packages/mui-material/src/ButtonBase/TouchRipple.js; cat package.json | grep '"test'
```

tool result:

```
// @ts-check
import * as React from 'react';
import { expect } from 'chai';
import { spy, stub } from 'sinon';
import {
  describeConformance,
  act,
  createClientRender,
  fireEvent,
  screen,
  focusVisible,
  simulatePointerDevice,
  programmaticFocusTriggersFocusVisible,
} from 'test/utils';
import PropTypes from 'prop-types';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import ButtonBase, { buttonBaseClasses as classes } from '@mui/material/ButtonBase';

describe('<ButtonBase />', () => {
  const render = createClientRender();

  // https://developer.microsoft.com/en-us/microsoft-edge/platform/issues/14156632/
  let canFireDragEvents = true;

  before(() => {
    // browser testing config
    try {
      const EventConstructor = window.DragEvent || window.Event;
      // eslint-disable-next-line no-new
      new EventConstructor('');
  const stop = React.useCallback((event, cb) => {
    clearTimeout(startTimer.current);

    // The touch interaction occurs too quickly.
    // We still want to show ripple effect.
    if (event.type === 'touchend' && startTimerCommit.current) {
      startTimerCommit.current();
      startTimerCommit.current = null;
      startTimer.current = setTimeout(() => {
        stop(event, cb);
      });
      return;
    }

    startTimerCommit.current = null;

    setRipples((oldRipples) => {
      if (oldRipples.length > 0) {
        return oldRipples.slice(1);
      }
      return oldRipples;
    });
    rippleCallback.current = cb;
  }, []);

  React.useImperativeHandle(
    ref,
    () => ({
      pulsate,
      start,
      stop,
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
    "test:umd": "node packages/mui-material/test/umd/run.js",
    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/*.test.{js,ts,tsx}' 'docs/**/*.test.{js,ts,tsx}' 'scripts/**/*.test.{js,ts,tsx}' 'test/utils/**/*.test.{js,ts,tsx}'",
    "test:watch": "yarn test:unit --watch",
    "test:argos": "node ./scripts/pushArgos.js",
    "test"
```

**tool call: Bash**

```bash
/work/mui__material-ui-28186/bin/envrun 'yarn -s cross-env NODE_ENV=test mocha packages/mui-material/src/ButtonBase/ButtonBase.test.js 2>&1 | tail -40'
```

tool result:

```
Command did not complete within its 300s timeout and was moved to the background (ID: box7q0wuv). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/1ea51d62-4e3f-4895-b78d-42be9ff1ed24/tasks/box7q0wuv.output. You will be notified when it completes. To check interim output, use Read on that file path.
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; git log --oneline -3 5f30983bfa 2>&1 | head; git show 5f30983bfa --stat 2>&1 | head -30
```

tool result:

```
5f30983bfa [Button] Create ButtonUnstyled and useButton (#27600)
65da499731 [docs] Fix Fab demo overflow on mobile (#28033)
c29d229e8c [test] Disable browserstack for PRs (#28041)
commit 5f30983bfa16195237fde55a78d5e43b151a29fa
Author: Michał Dudak <michal@dudak.me>
Date:   Mon Aug 30 13:11:59 2021 +0200

    [Button] Create ButtonUnstyled and useButton (#27600)

 docs/pages/api-docs/button-unstyled.js             |  23 ++
 docs/pages/api-docs/button-unstyled.json           |  25 +++
 .../components/buttons/UnstyledButtonCustom.js     | 108 ++++++++++
 .../components/buttons/UnstyledButtonCustom.tsx    | 110 ++++++++++
 .../components/buttons/UnstyledButtonsSimple.js    |  52 +++++
 .../components/buttons/UnstyledButtonsSimple.tsx   |  53 +++++
 .../components/buttons/UnstyledButtonsSpan.js      |  52 +++++
 .../components/buttons/UnstyledButtonsSpan.tsx     |  53 +++++
 docs/src/pages/components/buttons/UseButton.js     |  73 +++++++
 docs/src/pages/components/buttons/UseButton.tsx    |  74 +++++++
 docs/src/pages/components/buttons/buttons.md       |  45 +++-
 docs/src/pagesApi.js                               |   1 +
 .../button-unstyled/button-unstyled-de.json        |   7 +
 .../button-unstyled/button-unstyled-es.json        |   7 +
 .../button-unstyled/button-unstyled-fr.json        |   7 +
 .../button-unstyled/button-unstyled-ja.json        |   7 +
 .../button-unstyled/button-unstyled-pt.json        |   7 +
 .../button-unstyled/button-unstyled-ru.json        |   7 +
 .../button-unstyled/button-unstyled-zh.json        |   7 +
 .../api-docs/button-unstyled/button-unstyled.json  |  10 +
 .../src/ButtonUnstyled/ButtonUnstyled.test.tsx     |  22 ++
 .../src/ButtonUnstyled/ButtonUnstyled.tsx          | 163 +++++++++++++++
 .../src/ButtonUnstyled/ButtonUnstyledProps.ts      |  37 ++++
 .../src/ButtonUnstyled/UseButtonProps.ts           |  35 ++++
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; git show 5f30983bfa -- '*ButtonBase.js' | head -300
```

tool result:

```
commit 5f30983bfa16195237fde55a78d5e43b151a29fa
Author: Michał Dudak <michal@dudak.me>
Date:   Mon Aug 30 13:11:59 2021 +0200

    [Button] Create ButtonUnstyled and useButton (#27600)

diff --git a/packages/material-ui/src/ButtonBase/ButtonBase.js b/packages/material-ui/src/ButtonBase/ButtonBase.js
index 211f478ba3..f5bc04ba68 100644
--- a/packages/material-ui/src/ButtonBase/ButtonBase.js
+++ b/packages/material-ui/src/ButtonBase/ButtonBase.js
@@ -2,14 +2,13 @@ import * as React from 'react';
 import PropTypes from 'prop-types';
 import clsx from 'clsx';
 import { elementTypeAcceptingRef, refType } from '@material-ui/utils';
-import { unstable_composeClasses as composeClasses } from '@material-ui/unstyled';
+import { unstable_composeClasses as composeClasses, useButton } from '@material-ui/unstyled';
 import styled from '../styles/styled';
 import useThemeProps from '../styles/useThemeProps';
 import useForkRef from '../utils/useForkRef';
-import useEventCallback from '../utils/useEventCallback';
-import useIsFocusVisible from '../utils/useIsFocusVisible';
 import TouchRipple from './TouchRipple';
 import buttonBaseClasses, { getButtonBaseUtilityClass } from './buttonBaseClasses';
+import useTouchRipple from '../useTouchRipple';
 
 const useUtilityClasses = (ownerState) => {
   const { disabled, focusVisible, focusVisibleClassName, classes } = ownerState;
@@ -105,22 +104,21 @@ const ButtonBase = React.forwardRef(function ButtonBase(inProps, ref) {
   } = props;
 
   const buttonRef = React.useRef(null);
+  const handleRef = useForkRef(buttonRef, ref);
 
   const rippleRef = React.useRef(null);
 
-  const {
-    isFocusVisibleRef,
-    onFocus: handleFocusVisible,
-    onBlur: handleBlurVisible,
-    ref: focusVisibleRef,
-  } = useIsFocusVisible();
-  const [focusVisible, setFocusVisible] = React.useState(false);
-  if (disabled && focusVisible) {
-    setFocusVisible(false);
+  let ComponentProp = component;
+
+  if (ComponentProp === 'button' && (other.href || other.to)) {
+    ComponentProp = LinkComponent;
   }
-  React.useEffect(() => {
-    isFocusVisibleRef.current = focusVisible;
-  }, [focusVisible, isFocusVisibleRef]);
+
+  const { focusVisible, setFocusVisible, getRootProps } = useButton({
+    ...props,
+    component: ComponentProp,
+    ref: handleRef,
+  });
 
   React.useImperativeHandle(
     action,
@@ -130,187 +128,18 @@ const ButtonBase = React.forwardRef(function ButtonBase(inProps, ref) {
         buttonRef.current.focus();
       },
     }),
-    [],
+    [setFocusVisible],
   );
 
-  React.useEffect(() => {
-    if (focusVisible && focusRipple && !disableRipple) {
-      rippleRef.current.pulsate();
-    }
-  }, [disableRipple, focusRipple, focusVisible]);
-
-  function useRippleHandler(rippleAction, eventCallback, skipRippleAction = disableTouchRipple) {
-    return useEventCallback((event) => {
-      if (eventCallback) {
-        eventCallback(event);
-      }
-
-      const ignore = skipRippleAction;
-      if (!ignore && rippleRef.current) {
-        rippleRef.current[rippleAction](event);
-      }
-
-      return true;
-    });
-  }
-
-  const handleMouseDown = useRippleHandler('start', onMouseDown);
-  const handleContextMenu = useRippleHandler('stop', onContextMenu);
-  const handleDragLeave = useRippleHandler('stop', onDragLeave);
-  const handleMouseUp = useRippleHandler('stop', onMouseUp);
-  const handleMouseLeave = useRippleHandler('stop', (event) => {
-    if (focusVisible) {
-      event.preventDefault();
-    }
-    if (onMouseLeave) {
-      onMouseLeave(event);
-    }
-  });
-  const handleTouchStart = useRippleHandler('start', onTouchStart);
-  const handleTouchEnd = useRippleHandler('stop', onTouchEnd);
-  const handleTouchMove = useRippleHandler('stop', onTouchMove);
-
-  const handleBlur = useRippleHandler(
-    'stop',
-    (event) => {
-      handleBlurVisible(event);
-      if (isFocusVisibleRef.current === false) {
-        setFocusVisible(false);
-      }
-      if (onBlur) {
-        onBlur(event);
-      }
-    },
-    false,
-  );
-
-  const handleFocus = useEventCallback((event) => {
-    // Fix for https://github.com/facebook/react/issues/7769
-    if (!buttonRef.current) {
-      buttonRef.current = event.currentTarget;
-    }
-
-    handleFocusVisible(event);
-    if (isFocusVisibleRef.current === true) {
-      setFocusVisible(true);
-
-      if (onFocusVisible) {
-        onFocusVisible(event);
-      }
-    }
-
-    if (onFocus) {
-      onFocus(event);
-    }
-  });
-
-  const isNonNativeButton = () => {
-    const button = buttonRef.current;
-    return component && component !== 'button' && !(button.tagName === 'A' && button.href);
-  };
-
-  /**
-   * IE11 shim for https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/repeat
-   */
-  const keydownRef = React.useRef(false);
-  const handleKeyDown = useEventCallback((event) => {
-    // Check if key is already down to avoid repeats being counted as multiple activations
-    if (
-      focusRipple &&
-      !keydownRef.current &&
-      focusVisible &&
-      rippleRef.current &&
-      event.key === ' '
-    ) {
-      keydownRef.current = true;
-      rippleRef.current.stop(event, () => {
-        rippleRef.current.start(event);
-      });
-    }
-
-    if (event.target === event.currentTarget && isNonNativeButton() && event.key === ' ') {
-      event.preventDefault();
-    }
-
-    if (onKeyDown) {
-      onKeyDown(event);
-    }
-
-    // Keyboard accessibility for non interactive elements
-    if (
-      event.target === event.currentTarget &&
-      isNonNativeButton() &&
-      event.key === 'Enter' &&
-      !disabled
-    ) {
-      event.preventDefault();
-      if (onClick) {
-        onClick(event);
-      }
-    }
-  });
-
-  const handleKeyUp = useEventCallback((event) => {
-    // calling preventDefault in keyUp on a <button> will not dispatch a click event if Space is pressed
-    // https://codesandbox.io/s/button-keyup-preventdefault-dn7f0
-    
[... 2606 more characters not shown]
```

**thinking:**

```
I noticed the refactored `useTouchRipple` dropped the explicit `false` for `skipRippleAction` on blur, so blur no longer stops the ripple when `disableTouchRipple` is set. I'll check if the docs theme enables that setting.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; grep -rn "disableTouchRipple" docs/src/modules docs/src/pages.ts docs/pages/_app.js packages/mui-material/src --include='*.js' 2>/dev/null | grep -v "test\|PropTypes\|^\s*\*" | head
```

tool result:

```
packages/mui-material/src/ButtonBase/ButtonBase.js:82:    disableTouchRipple = false,
packages/mui-material/src/ButtonBase/ButtonBase.js:138:    disableTouchRipple,
packages/mui-material/src/ButtonBase/ButtonBase.js:163:    disableTouchRipple,
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; grep -n "<ButtonRoot" -A20 packages/mui-material/src/Button/Button.js; cat packages/mui-utils/src/useEventCallback.ts
```

tool result:

```
327:    <ButtonRoot
328-      ownerState={ownerState}
329-      component={component}
330-      disabled={disabled}
331-      focusRipple={!disableFocusRipple}
332-      focusVisibleClassName={clsx(classes.focusVisible, focusVisibleClassName)}
333-      ref={ref}
334-      type={type}
335-      {...other}
336-      classes={classes}
337-    >
338-      {startIcon}
339-      {children}
340-      {endIcon}
341-    </ButtonRoot>
342-  );
343-});
344-
345-Button.propTypes /* remove-proptypes */ = {
346-  // ----------------------------- Warning --------------------------------
347-  // | These PropTypes are generated from the TypeScript type definitions |
import * as React from 'react';
import useEnhancedEffect from './useEnhancedEffect';

/**
 * https://github.com/facebook/react/issues/14099#issuecomment-440013892
 */
export default function useEventCallback<Args extends unknown[], Return>(
  fn: (...args: Args) => Return,
): (...args: Args) => Return {
  const ref = React.useRef(fn);
  useEnhancedEffect(() => {
    ref.current = fn;
  });
  return React.useCallback(
    (...args: Args) =>
      // @ts-expect-error hide `this`
      // tslint:disable-next-line:ban-comma-operator
      (0, ref.current!)(...args),
    [],
  );
}
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; sed -n 120,200p packages/mui-utils/src/useIsFocusVisible.ts
```

tool result:

```
Exit code 1
sed: packages/mui-utils/src/useIsFocusVisible.ts: No such file or directory
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; f=$(ls packages/mui-utils/src/useIsFocusVisible.*); sed -n 110,200p $f
```

tool result:

```
Exit code 1
sed: packages/mui-utils/src/useIsFocusVisible.d.ts
packages/mui-utils/src/useIsFocusVisible.js
packages/mui-utils/src/useIsFocusVisible.test.js: No such file or directory
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; sed -n 110,200p packages/mui-utils/src/useIsFocusVisible.js
```

tool result:

```
    // want to crash if focus-visible malfunctioned?
  }

  // No need for validFocusTarget check. The user does that by attaching it to
  // focusable events only.
  return hadKeyboardEvent || focusTriggersKeyboardModality(target);
}

export default function useIsFocusVisible() {
  const ref = React.useCallback((node) => {
    if (node != null) {
      prepare(node.ownerDocument);
    }
  }, []);

  const isFocusVisibleRef = React.useRef(false);

  /**
   * Should be called if a blur event is fired
   */
  function handleBlurVisible() {
    // checking against potential state variable does not suffice if we focus and blur synchronously.
    // React wouldn't have time to trigger a re-render so `focusVisible` would be stale.
    // Ideally we would adjust `isFocusVisible(event)` to look at `relatedTarget` for blur events.
    // This doesn't work in IE11 due to https://github.com/facebook/react/issues/3751
    // TODO: check again if React releases their internal changes to focus event handling (https://github.com/facebook/react/pull/19186).
    if (isFocusVisibleRef.current) {
      // To detect a tab/window switch, we look for a blur event followed
      // rapidly by a visibility change.
      // If we don't see a visibility change within 100ms, it's probably a
      // regular focus change.
      hadFocusVisibleRecently = true;
      window.clearTimeout(hadFocusVisibleRecentlyTimeout);
      hadFocusVisibleRecentlyTimeout = window.setTimeout(() => {
        hadFocusVisibleRecently = false;
      }, 100);

      isFocusVisibleRef.current = false;

      return true;
    }

    return false;
  }

  /**
   * Should be called if a blur event is fired
   */
  function handleFocusVisible(event) {
    if (isFocusVisible(event)) {
      isFocusVisibleRef.current = true;
      return true;
    }
    return false;
  }

  return { isFocusVisibleRef, onFocus: handleFocusVisible, onBlur: handleBlurVisible, ref };
}
```

**tool call: Bash**

```bash
sleep 60; tail -40 /tmp/cell-scratch/claude-502/<actor-session-slug>/1ea51d62-4e3f-4895-b78d-42be9ff1ed24/tasks/box7q0wuv.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
sleep 120; tail -40 /tmp/cell-scratch/claude-502/<actor-session-slug>/1ea51d62-4e3f-4895-b78d-42be9ff1ed24/tasks/box7q0wuv.output
```

tool result:

```
Exit code 143
Command timed out after 2m 0s
```

**tool call: Bash**

```bash
cat /tmp/cell-scratch/claude-502/<actor-session-slug>/1ea51d62-4e3f-4895-b78d-42be9ff1ed24/tasks/box7q0wuv.output | tail -40
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; grep -n '"react"\|"react-dom"' package.json docs/package.json; git diff package.json
```

tool result:

```
package.json:158:    "react": "^17.0.2",
package.json:159:    "react-dom": "^17.0.2",
docs/package.json:94:    "react": "^17.0.2",
docs/package.json:96:    "react-dom": "^17.0.2",
diff --git a/package.json b/package.json
index 19c0cc8038..4efea41bb0 100644
--- a/package.json
+++ b/package.json
@@ -83,17 +83,20 @@
     "@rollup/plugin-replace": "^3.0.0",
     "@testing-library/dom": "^8.1.0",
     "@testing-library/react": "^12.0.0",
-    "@types/chai": "^4.2.21",
+    "@types/chai": "^4.3.20",
     "@types/chai-dom": "^0.0.10",
     "@types/enzyme": "^3.10.9",
-    "@types/format-util": "^1.0.1",
+    "@types/format-util": "^1.0.4",
     "@types/fs-extra": "^9.0.12",
     "@types/jsdom": "^16.2.13",
     "@types/lodash": "^4.14.172",
     "@types/mocha": "^9.0.0",
     "@types/prettier": "^2.3.2",
+    "@types/prop-types": "^15.7.15",
     "@types/react": "^17.0.19",
-    "@types/sinon": "^10.0.2",
+    "@types/react-dom": "^19.1.8",
+    "@types/sinon": "^10.0.20",
+    "@types/testing-library__react": "^10.2.0",
     "@types/webpack": "^4.41.22",
     "@types/yargs": "^17.0.0",
     "@typescript-eslint/eslint-plugin": "^4.29.0",
```

**tool call: Bash**

```bash
sleep 100; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/1ea51d62-4e3f-4895-b78d-42be9ff1ed24/tasks/box7q0wuv.output | tail -60
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; cat .mocharc.js
```

tool result:

```
module.exports = {
  extension: ['js', 'ts', 'tsx'],
  ignore: [
    '**/build/**',
    '**/node_modules/**',
    // Mocha seems to ignore .next anyway (maybe because dotfiles?).
    // We're leaving this to make sure.
    'docs/.next/**',
  ],
  recursive: true,
  timeout: (process.env.CIRCLECI === 'true' ? 5 : 2) * 1000, // Circle CI has low-performance CPUs.
  reporter: 'dot',
  require: [require.resolve('./test/utils/setupBabel'), require.resolve('./test/utils/setupJSDOM')],
  'watch-ignore': [
    // default
    '.git',
    // node_modules can be nested with workspaces
    '**/node_modules/**',
    // Unrelated directories with a large number of files
    '**/build/**',
    'docs/.next/**',
  ],
};
```

**assistant:** While the test run warms up, I'll write a repro test that tabs between two focus-ripple buttons.

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; cat > packages/mui-material/src/ButtonBase/repro.test.js <<'EOF'
import * as React from 'react';
import { expect } from 'chai';
import { act, createClientRender, fireEvent, simulatePointerDevice } from 'test/utils';
import ButtonBase from '@mui/material/ButtonBase';

describe('repro', () => {
  const render = createClientRender();
  [false, true].forEach((disableTouchRipple) => {
    it(`tab between buttons disableTouchRipple=${disableTouchRipple}`, () => {
      const rp = { classes: { rippleVisible: 'rv', childLeaving: 'cl' } };
      const { getAllByRole } = render(
        <div>
          <ButtonBase focusRipple disableTouchRipple={disableTouchRipple} TouchRippleProps={rp}>a</ButtonBase>
          <ButtonBase focusRipple disableTouchRipple={disableTouchRipple} TouchRippleProps={rp}>b</ButtonBase>
        </div>,
      );
      const [a, b] = getAllByRole('button');
      simulatePointerDevice();
      fireEvent.keyDown(document.body, { key: 'Tab' });
      act(() => a.focus());
      expect(a.querySelectorAll('.rv:not(:has(.cl))').length).to.equal(1);
      fireEvent.keyDown(a, { key: 'Tab' });
      act(() => b.focus());
      fireEvent.keyUp(b, { key: 'Tab' });
      expect(a.querySelectorAll('.rv .cl').length, 'a leaving').to.equal(1);
      expect(b.querySelectorAll('.rv').length, 'b visible').to.equal(1);
    });
  });
});
EOF
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; sed -i '' "s/'.rv:not(:has(.cl))'/'.rv'/" packages/mui-material/src/ButtonBase/repro.test.js; grep -n "rv'" packages/mui-material/src/ButtonBase/repro.test.js
```

tool result:

```
10:      const rp = { classes: { rippleVisible: 'rv', childLeaving: 'cl' } };
21:      expect(a.querySelectorAll('.rv').length).to.equal(1);
26:      expect(b.querySelectorAll('.rv').length, 'b visible').to.equal(1);
```

**tool call: Bash**

```bash
sleep 30; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/1ea51d62-4e3f-4895-b78d-42be9ff1ed24/tasks/box7q0wuv.output | tail -60; /work/mui__material-ui-28186/bin/envrun 'ps aux | grep -c mocha'
```

tool result:

```
8
```

**tool call: Bash**

```bash
/work/mui__material-ui-28186/bin/envrun 'ps aux | grep -v grep | grep -i "mocha\|node" | cut -c1-250'
```

tool result:

```
root         7  0.0  0.0 419788  6348 ?        Ss   13:45   0:00 bash -lc yarn -s cross-env NODE_ENV=test mocha packages/mui-material/src/ButtonBase/ButtonBase.test.js 2>&1 | tail -40
root        15  0.0  0.5 1049032 84260 ?       Sl   13:45   0:00 node --no-opt -r /proc/.reset /usr/local/nvm/versions/node/v16.20.2/bin/yarn -s cross-env NODE_ENV=test mocha packages/mui-material/src/ButtonBase/ButtonBase.test.js
root        23  0.1  0.5 1215056 91196 ?       Sl   13:45   0:01 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/.yarn/releases/yarn-1.22.10.js -s cross-env NODE_ENV=test mocha packages/mui-material/src/ButtonBase/But
root        34  0.0  0.0 418032  3364 ?        S    13:45   0:00 /bin/sh -c /testbed/node_modules/.bin/cross-env NODE_ENV=test mocha packages/mui-material/src/ButtonBase/ButtonBase.test.js
root        35  0.0  0.3 945224 51056 ?        Sl   13:45   0:00 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/.bin/cross-env NODE_ENV=test mocha packages/mui-material/src/ButtonBase/ButtonBase.test.js
root        42  1.2  1.5 11631416 259560 ?     Sl   13:45   0:08 /usr/local/nvm/versions/node/v16.20.2/bin/node --no-opt -r /proc/.reset /testbed/node_modules/.bin/mocha packages/mui-material/src/ButtonBase/ButtonBase.test.js
```

**assistant:** The mocha process looks idle (only 8s CPU), possibly hanging after finishing. I'll kill it and rerun with `--exit`.

**tool call: Bash**

```bash
/work/mui__material-ui-28186/bin/envrun 'pkill -f mocha; cd /testbed && NODE_ENV=test timeout 250 node_modules/.bin/mocha --exit packages/mui-material/src/ButtonBase/repro.test.js 2>&1 | tail -40'
```

tool result:

```
Exit code 143
```

**assistant:** `pkill -f mocha` matched its own shell, so it killed itself. Running again without it:

**tool call: Bash**

```bash
/work/mui__material-ui-28186/bin/envrun 'cd /testbed && NODE_ENV=test timeout 280 node_modules/.bin/mocha --exit --reporter spec packages/mui-material/src/ButtonBase/repro.test.js 2>&1 | tail -40'
```

tool result:

```
Browserslist: caniuse-lite is outdated. Please run:
npx browserslist@latest --update-db

Why you should do it regularly:
https://github.com/browserslist/browserslist#browsers-data-updating
including inaccessible elements by default


  repro
    ✔ tab between buttons disableTouchRipple=false (176ms)
    1) tab between buttons disableTouchRipple=true


  1 passing (256ms)
  1 failing

  1) repro
       tab between buttons disableTouchRipple=true:

      a leaving
      + expected - actual

      -0
      +1
      
      at Context.<anonymous> (packages/mui-material/src/ButtonBase/repro.test.js:25:68)
      at processImmediate (node:internal/timers:466:21)
```

**thinking:**

```
Confirmed: with `disableTouchRipple`, blurring no longer stops the focus ripple, while the default case still passes in jsdom. Now I'll check if the docs theme sets `disableTouchRipple` in a TS file my earlier grep missed.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; grep -rn "disableTouchRipple\|disableRipple" docs/src --include='*.ts' --include='*.tsx' --include='*.js' | grep -v "pages/components\|pages/guides\|pages/customization" | head
```

tool result:

```
docs/src/components/home/CoreShowcase.tsx:25:        disableTouchRipple: true,
docs/src/components/home/MaterialDesignComponents.tsx:238:          disableTouchRipple: true,
docs/src/components/showcase/ThemeAccordion.tsx:93:              disableTouchRipple: true,
docs/src/components/showcase/PlayerCard.tsx:75:              disableTouchRipple: true,
docs/src/components/showcase/NotificationCard.tsx:104:              disableTouchRipple: true,
docs/src/components/showcase/ThemeTabs.tsx:50:              disableTouchRipple: true,
docs/src/components/showcase/ThemeDatePicker.tsx:81:            disableTouchRipple: true,
docs/src/components/showcase/ThemeToggleButton.tsx:73:              disableTouchRipple: true,
docs/src/components/showcase/ViewToggleButton.tsx:90:              disableTouchRipple: true,
docs/src/components/header/HeaderNavDropdown.tsx:78:        disableRipple
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; grep -rn "disableTouchRipple" docs/src/modules | head
```

tool result:

```
docs/src/modules/brandingTheme.ts:290:          disableTouchRipple: true,
docs/src/modules/brandingTheme.ts:401:          disableTouchRipple: true,
```

**thinking:**

```
Found it: the docs branding theme sets `disableTouchRipple: true`, and the refactored ButtonBase lost the old blur-stop behavior that previously ran regardless of that flag. Applying the fix now.


```

**tool call: Edit**

```json
{
 "replace_all": false,
 "file_path": "/work/mui__material-ui-28186/repo/packages/mui-material/src/useTouchRipple/useTouchRipple.ts",
 "old_string": "  const handleBlur = useRippleHandler('stop');",
 "new_string": "  // The focus ripple must be stopped on blur even if touch ripples are disabled.\n  const handleBlur = useRippleHandler('stop', undefined, false);"
}
```

tool result:

```
The file /work/mui__material-ui-28186/repo/packages/mui-material/src/useTouchRipple/useTouchRipple.ts has been updated successfully. (file state is current in your context — no need to Read it back)
```

**tool call: Bash**

```bash
/work/mui__material-ui-28186/bin/envrun 'cd /testbed && NODE_ENV=test timeout 280 node_modules/.bin/mocha --exit packages/mui-material/src/ButtonBase/repro.test.js packages/mui-material/src/ButtonBase/*.test.js packages/mui-core/src/ButtonUnstyled/*.test.tsx packages/mui-material/src/Button/Button.test.js 2>&1 | tail -30'
```

tool result:

```
Browserslist: caniuse-lite is outdated. Please run:
npx browserslist@latest --update-db

Why you should do it regularly:
https://github.com/browserslist/browserslist#browsers-data-updating
including inaccessible elements by default


  .........,,,,...........................................
  ........................................................
  .................................,,,,.

  142 passing (1s)
  8 pending
```

**assistant:** Everything passes, including both repro cases. Now I'll delete the repro file and check the diff:

**tool call: Bash**

```bash
cd /work/mui__material-ui-28186/repo; rm packages/mui-material/src/ButtonBase/repro.test.js; git status --short; git diff packages/
```

tool result:

```
 M package.json
 M packages/mui-material/src/useTouchRipple/useTouchRipple.ts
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
diff --git a/packages/mui-material/src/useTouchRipple/useTouchRipple.ts b/packages/mui-material/src/useTouchRipple/useTouchRipple.ts
index 5f444d8e57..f3ca47fe8f 100644
--- a/packages/mui-material/src/useTouchRipple/useTouchRipple.ts
+++ b/packages/mui-material/src/useTouchRipple/useTouchRipple.ts
@@ -90,7 +90,8 @@ const useTouchRipple = (props: UseTouchRippleProps) => {
     }
   });
 
-  const handleBlur = useRippleHandler('stop');
+  // The focus ripple must be stopped on blur even if touch ripples are disabled.
+  const handleBlur = useRippleHandler('stop', undefined, false);
   const handleMouseDown = useRippleHandler('start');
   const handleContextMenu = useRippleHandler('stop');
   const handleDragLeave = useRippleHandler('stop');
```

**assistant:** I fixed the bug: tabbing away from a button now clears its focus ripple. The fix is a one-line change in `packages/mui-material/src/useTouchRipple/useTouchRipple.ts`.

**Cause:** Before commit 5f30983, ButtonBase always stopped the ripple on blur, even when touch ripples were turned off. When that logic moved into `useTouchRipple`, the blur handler started following `disableTouchRipple` like the mouse and touch handlers. So any button with `disableTouchRipple` started the focus ripple when it gained keyboard focus, but never stopped it when it lost focus.

That's why it shows up on the docs site: the docs theme sets `disableTouchRipple: true` for all `MuiButtonBase` components (`docs/src/modules/brandingTheme.ts:290`). Buttons without that setting never had the problem.

**Fix:** the blur handler now always stops the ripple, as it did before:
```ts
// The focus ripple must be stopped on blur even if touch ripples are disabled.
const handleBlur = useRippleHandler('stop', undefined, false);
```

**Verification:**
- **Repro:** I wrote a temporary test that tabs between two focus-ripple buttons. With `disableTouchRipple`, the first button kept its ripple after losing focus; without it, the test already passed. After the fix, both cases pass. I've deleted the test.
- **Existing tests:** the ButtonBase, ButtonUnstyled and Button tests all pass (142 passing, 8 skipped).

I didn't check it in a real browser, only in the jsdom tests. The `package.json`, `yarn.lock`, `Dockerfile` and `custom-reporter.js` changes were already there before I started; I didn't touch them.

_session end: success, turns 36, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.15 s: ps aux | grep -c mocha
- `rc=0` 0.13 s: ps aux | grep -v grep | grep -i "mocha\|node" | cut -c1-250
- `rc=143` 0.14 s: pkill -f mocha; cd /testbed && NODE_ENV=test timeout 250 node_modules/.bin/mocha --exit packages/mui-material/src/ButtonBase/repro.test.js 2>&1 | tail -40
- `rc=143` 709.33 s: yarn -s cross-env NODE_ENV=test mocha packages/mui-material/src/ButtonBase/ButtonBase.test.js 2>&1 | tail -40
- `rc=0` 2.82 s: cd /testbed && NODE_ENV=test timeout 280 node_modules/.bin/mocha --exit --reporter spec packages/mui-material/src/ButtonBase/repro.test.js 2>&1 | tail -40
- `rc=0` 4.4 s: cd /testbed && NODE_ENV=test timeout 280 node_modules/.bin/mocha --exit packages/mui-material/src/ButtonBase/repro.test.js packages/mui-material/src/ButtonBase/*.test.js packages/mui-core/src/ButtonUnstyled/*.test.tsx packages/mui-material/src/Button/Button.test.js 2>&1 | tail -30
