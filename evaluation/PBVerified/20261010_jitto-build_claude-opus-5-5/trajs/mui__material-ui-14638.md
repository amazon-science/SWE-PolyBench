# Instance: mui__material-ui-14638

- Final resolved (evaluator, logs/mui__material-ui-14638_result.json): True
- Run state: DONE
- One attempt. Duration 2465.0 s, turns 33, actor cost $0.92465, container commands 8
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/mui__material-ui-14638/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-14638/repo. Consider the following issue description:

<issue_description>
[Tabs] Awkward line height when 2 lines
- [x] This is not a v0.x issue. <!-- (v0.x is no longer maintained) -->
- [x] I have searched the [issues](https://github.com/mui-org/material-ui/issues) of this repository and believe that this is not a duplicate.

## Expected Behavior 🤔
![a989bab3-e062-4dcf-a679-0afd21b9b4e6](https://user-images.githubusercontent.com/1693592/52843618-f6186400-3102-11e9-8e63-6b2a7e202dd4.png)

It should look like this:

![annotation 2019-02-15 110003](https://user-images.githubusercontent.com/1693592/52849279-ee5fbc00-3110-11e9-8922-97d94f709a03.png)

## Current Behavior 😯
When a tab title takes multiple lines, the line height of `1.75` is to large.

![588df98b-6a19-427c-9b54-56c2ab9b0401](https://user-images.githubusercontent.com/1693592/52849262-e6a01780-3110-11e9-8b40-d072d32cac8f.png)

## Steps to Reproduce 🕹
Link:

1. https://material.io/design/components/tabs.html#anatomy

| Tech         | Version |
|--------------|---------|
| Material-UI  | v3.9.2  |

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-14638/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-14638/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-14638/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-14638/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
cd /work/mui__material-ui-14638/repo; cat packages/material-ui/src/Tab/Tab.js; git log --oneline -1
```

tool result:

```
// @inheritedComponent ButtonBase

import React from 'react';
import PropTypes from 'prop-types';
import clsx from 'clsx';
import withStyles from '../styles/withStyles';
import ButtonBase from '../ButtonBase';
import { capitalize } from '../utils/helpers';
import unsupportedProp from '../utils/unsupportedProp';

export const styles = theme => ({
  /* Styles applied to the root element. */
  root: {
    ...theme.typography.button,
    maxWidth: 264,
    minWidth: 72,
    position: 'relative',
    boxSizing: 'border-box',
    padding: 0,
    minHeight: 48,
    flexShrink: 0,
    overflow: 'hidden',
    whiteSpace: 'normal',
    textAlign: 'center',
    [theme.breakpoints.up('md')]: {
      fontSize: theme.typography.pxToRem(13),
      minWidth: 160,
    },
  },
  /* Styles applied to the root element if both `icon` and `label` are provided. */
  labelIcon: {
    minHeight: 72,
    // paddingTop supposed to be 12px
    // - 3px from the paddingBottom
    paddingTop: 9,
    // paddingBottom supposed to be 12px
    // -3px for line-height of the label
    // -6px for label padding
    // = 3px
  },
  /* Styles applied to the root element if `textColor="inherit"`. */
  textColorInherit: {
    color: 'inherit',
    opacity: 0.7,
    '&$selected': {
      opacity: 1,
    },
    '&$disabled': {
      opacity: 0.4,
    },
  },
  /* Styles applied to the root element if `textColor="primary"`. */
  textColorPrimary: {
    color: theme.palette.text.secondary,
    '&$selected': {
      color: theme.palette.primary.main,
    },
    '&$disabled': {
      color: theme.palette.text.disabled,
    },
  },
  /* Styles applied to the root element if `textColor="secondary"`. */
  textColorSecondary: {
    color: theme.palette.text.secondary,
    '&$selected': {
      color: theme.palette.secondary.main,
    },
    '&$disabled': {
      color: theme.palette.text.disabled,
    },
  },
  /* Styles applied to the root element if `selected={true}` (controlled by the Tabs component). */
  selected: {},
  /* Styles applied to the root element if `disabled={true}` (controlled by the Tabs component). */
  disabled: {},
  /* Styles applied to the root element if `fullWidth={true}` (controlled by the Tabs component). */
  fullWidth: {
    flexShrink: 1,
    flexGrow: 1,
    maxWidth: 'none',
  },
  /* Styles applied to the `icon` and `label`'s wrapper element. */
  wrapper: {
    display: 'inline-flex',
    alignItems: 'center',
    justifyContent: 'center',
    width: '100%',
    flexDirection: 'column',
  },
  /* Styles applied to the label container element if `label` is provided. */
  labelContainer: {
    width: '100%', // Fix an IE 11 issue
    boxSizing: 'border-box',
    padding: '6px 12px',
    [theme.breakpoints.up('md')]: {
      padding: '6px 24px',
    },
  },
  /* Styles applied to the label wrapper element if `label` is provided. */
  label: {},
  /* Deprecated, the styles will be removed in v4. */
  labelWrapped: {},
});

class Tab extends React.Component {
  state = {
    labelWrapped: false,
  };

  componentDidMount() {
    this.checkTextWrap();
  }

  componentDidUpdate(prevProps, prevState) {
    if (this.state.labelWrapped === prevState.labelWrapped) {
      /**
       * At certain text and tab lengths, a larger font size may wrap to two lines while the smaller
       * font size still only requires one line.  This check will prevent an infinite render loop
       * from occurring in that scenario.
       */
      this.checkTextWrap();
    }
  }

  handleChange = event => {
    const { onChange, value, onClick } = this.props;

    if (onChange) {
      onChange(event, value);
    }

    if (onClick) {
      onClick(event);
    }
  };

  checkTextWrap = () => {
    if (this.labelRef) {
      const labelWrapped = this.labelRef.getClientRects().length > 1;
      if (this.state.labelWrapped !== labelWrapped) {
        this.setState({ labelWrapped });
      }
    }
  };

  render() {
    const {
      classes,
      className,
      disabled,
      fullWidth,
      icon,
      indicator,
      label: labelProp,
      onChange,
      selected,
      textColor,
      value,
      ...other
    } = this.props;

    let label;

    if (labelProp !== undefined) {
      label = (
        <span className={classes.labelContainer}>
          <span
            className={clsx(classes.label, {
              [classes.labelWrapped]: this.state.labelWrapped,
            })}
            ref={ref => {
              this.labelRef = ref;
            }}
          >
            {labelProp}
          </span>
        </span>
      );
    }

    return (
      <ButtonBase
        focusRipple
        className={clsx(
          classes.root,
          classes[`textColor${capitalize(textColor)}`],
          {
            [classes.disabled]: disabled,
            [classes.selected]: selected,
            [classes.labelIcon]: icon && label,
            [classes.fullWidth]: fullWidth,
          },
          className,
        )}
        role="tab"
        aria-selected={selected}
        disabled={disabled}
        {...other}
        onClick={this.handleChange}
      >
        <span className={classes.wrapper}>
          {icon}
          {label}
        </span>
        {indicator}
      </ButtonBase>
    );
  }
}

Tab.propTypes = {
  /**
   * This property isn't supported.
   * Use the `component` property if you need to change the children structure.
   */
  children: unsupportedProp,
  /**
   * Override or extend the styles applied to the component.
   * See [CSS API](#css) below for more details.
   */
  classes: PropTypes.object.isRequired,
  /**
   * @ignore
   */
  className: PropTypes.string,
  /**
   * If `true`, the tab will be disabled.
   */
  disabled: PropTypes.bool,
  /**
   * @ignore
   */
  fullWidth: PropTypes.bool,
  /**
   * The icon element.
   */
  icon: PropTypes.node,
  /**
   * @ignore
   * For server-side rendering consideration, we let the selected tab
   * render the indicator.
   */
  indicator: PropTypes.
[... 643 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; cat packages/material-ui/src/Tab/Tab.test.js; cat packages/material-ui/src/Tab/Tab.d.ts; grep -rn "labelContainer\|labelWrapped\|MuiTab-label\|classes.label\b" --include=*.js --include=*.ts --include=*.tsx --include=*.md . | grep -v node_modules | grep -v "^./packages/material-ui/src/Tab/Tab.js"
```

tool result:

```
import React from 'react';
import { assert } from 'chai';
import { spy, stub } from 'sinon';
import { createShallow, createMount, getClasses, unwrap } from '@material-ui/core/test-utils';
import Tab from './Tab';
import ButtonBase from '../ButtonBase';
import Icon from '../Icon';

describe('<Tab />', () => {
  let shallow;
  let mount;
  let classes;
  const icon = <Icon>restore</Icon>;

  before(() => {
    shallow = createShallow({ dive: true });
    mount = createMount();
    classes = getClasses(<Tab textColor="inherit" />);
  });

  after(() => {
    mount.cleanUp();
  });

  it('should render with the root class', () => {
    const wrapper = shallow(<Tab textColor="inherit" />);
    assert.strictEqual(wrapper.type(), ButtonBase);
    assert.strictEqual(wrapper.hasClass(classes.root), true);
  });

  describe('prop: className', () => {
    it('should render with the user and root classes', () => {
      const wrapper = shallow(<Tab textColor="inherit" className="woofTab" />);
      assert.strictEqual(wrapper.hasClass('woofTab'), true);
      assert.strictEqual(wrapper.hasClass(classes.root), true);
    });
  });

  describe('prop: selected', () => {
    it('should render with the selected and root classes', () => {
      const wrapper = shallow(<Tab selected textColor="secondary" />);
      assert.strictEqual(wrapper.hasClass(classes.selected), true);
      assert.strictEqual(wrapper.hasClass(classes.textColorSecondary), true);
      assert.strictEqual(wrapper.hasClass(classes.root), true);
      assert.strictEqual(wrapper.props()['aria-selected'], true);
    });
  });

  describe('prop: disabled', () => {
    it('should render with the disabled and root classes', () => {
      const wrapper = shallow(<Tab disabled textColor="secondary" />);
      assert.strictEqual(wrapper.hasClass(classes.disabled), true);
      assert.strictEqual(wrapper.hasClass(classes.textColorSecondary), true);
      assert.strictEqual(wrapper.hasClass(classes.root), true);
    });
  });

  describe('prop: onClick', () => {
    it('should be called when a click is triggered', () => {
      const handleClick = spy();
      const wrapper = shallow(
        <Tab textColor="inherit" onClick={handleClick} onChange={() => {}} />,
      );
      wrapper.simulate('click');
      assert.strictEqual(handleClick.callCount, 1, 'it should forward the onClick');
    });
  });

  describe('prop: label', () => {
    it('should render label with the label class', () => {
      const wrapper = shallow(<Tab textColor="inherit" label="foo" />);
      const label = wrapper
        .childAt(0)
        .childAt(0)
        .childAt(0);
      assert.strictEqual(label.hasClass(classes.label), true);
    });

    it('should render with text wrapping', () => {
      const wrapper = shallow(<Tab textColor="inherit" label="foo" />);
      const instance = wrapper.instance();
      instance.labelRef = { getClientRects: stub().returns({ length: 2 }) };
      instance.checkTextWrap();
      wrapper.update();
      const label = wrapper
        .childAt(0)
        .childAt(0)
        .childAt(0);
      assert.strictEqual(
        label.hasClass(classes.labelWrapped),
        true,
        'should have labelWrapped class',
      );
      assert.strictEqual(wrapper.state().labelWrapped, true, 'labelWrapped state should be true');
    });
  });

  describe('prop: classes', () => {
    it('should render label with a custom label class', () => {
      const wrapper = shallow(
        <Tab textColor="inherit" label="foo" classes={{ label: 'MyLabel' }} />,
      );
      const label = wrapper
        .childAt(0)
        .childAt(0)
        .childAt(0);
      assert.strictEqual(label.hasClass(classes.label), true);
      assert.strictEqual(label.hasClass('MyLabel'), true);
    });
  });

  describe('prop: icon', () => {
    it('should render icon element', () => {
      const wrapper = shallow(<Tab textColor="inherit" icon={icon} />);
      const iconWrapper = wrapper.childAt(0).childAt(0);
      assert.strictEqual(iconWrapper.is(Icon), true);
    });
  });

  describe('prop: textColor', () => {
    it('should support the inherit value', () => {
      const wrapper = shallow(<Tab selected textColor="inherit" />);
      assert.strictEqual(wrapper.hasClass(classes.selected), true);
      assert.strictEqual(wrapper.hasClass(classes.textColorInherit), true);
      assert.strictEqual(wrapper.hasClass(classes.root), true);
    });
  });

  describe('prop: fullWidth', () => {
    it('should have the fullWidth class', () => {
      const wrapper = shallow(<Tab textColor="inherit" fullWidth />);
      assert.strictEqual(wrapper.hasClass(classes.fullWidth), true);
    });
  });

  describe('prop: style', () => {
    it('should be able to override everything', () => {
      const style = { width: '80%', color: 'red', alignText: 'center' };
      const wrapper = shallow(<Tab fullWidth style={style} />);
      assert.deepEqual(wrapper.props().style, style);
    });
  });

  it('should have a ref on label property', () => {
    const TabNaked = unwrap(Tab);
    const instance = mount(
      <TabNaked textColor="inherit" label="foo" classes={classes} />,
    ).instance();
    assert.isDefined(instance.labelRef, 'should be defined');
  });
});
import * as React from 'react';
import { StandardProps } from '..';
import { ButtonBaseProps } from '../ButtonBase';

export interface TabProps extends StandardProps<ButtonBaseProps, TabClassKey, 'onChange'> {
  disabled?: boolean;
  fullWidth?: boolean;
  icon?: string | React.ReactElement<any>;
  value?: any;
  label?: React.ReactNode;
  onChange?: (event: React.ChangeEvent<{ checked: boolean }>, value: any) => void;
  onClick?: React.EventHandler<any>;
  selected?: boolean;
  style?: React.CSSProperties;
  textColor?: string | 'secondary' | 'primary' | 'inherit';
}

export type TabClassKey =
  | 'root'
  | 'labelIcon'
  | 'textColorInherit'
  | 'textColorPrimary'
  | 'textColorSecondary'
  | 'selected'
  | 'disabled'
  | 'f
[... 191 more characters not shown]
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; grep -rn -i "tab" docs/src/pages/guides/migration-v3/*.md | head -30; grep -rln "labelContainer\|labelWrapped" docs packages --exclude-dir=node_modules | head
```

tool result:

```
(eval):1: no matches found: docs/src/pages/guides/migration-v3/*.md
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js
docs/src/pages/premium-themes/paperbase/Paperbase.js
packages/material-ui/src/Tab/Tab.d.ts
packages/material-ui/src/Tab/Tab.js
packages/material-ui/src/Tab/Tab.test.js
packages/material-ui/src/StepLabel/StepLabel.js
packages/material-ui/src/StepLabel/StepLabel.d.ts
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; find . -path "*node_modules/@material-ui/core/Tab/Tab.js" 2>/dev/null | head; grep -n "version" packages/material-ui/package.json | head -2; head -40 CHANGELOG.md
```

tool result:

````
5:  "version": "4.0.0-alpha.1",
### [Versions](https://material-ui.com/versions/)

## 4.0.0-alpha.1
###### *Feb 20, 2019*

A big thanks to the 16 contributors who made this release possible!

Here are some highlights ✨:

- Important accessibility fixes (#14465, #14545) @eps1lon, @oliviertassinari
- Improve the Gastby integration (we will continue working on it to get something awesome) (#14552)
- Remove the deprecated Typography variants (#14562) @joshwooding
- And many more 🐛 bug fixes and 📝 documentation improvements.

### `@material-ui/core@v4.0.0-alpha.1`

### Breaking change

- [Typography] Remove deprecated Typography variants (#14562) @joshwooding

  - Remove the deprecated typography variants. You can upgrade by performing the following replacements:
    - display4 => h1
    - display3 => h2
    - display2 => h3
    - display1 => h4
    - headline => h5
    - title => h6
    - subheading => subtitle1
    - body2 => body1
    - body1 (default) => body2 (default)
  - Remove the opinionated `display: block` default typograpghy style.
  You can use the new `display?: 'initial' | 'inline' | 'block';` property.
  - Rename the `headlineMapping` property to better align with its purpose.
  ```diff
  -<MuiTypography headlineMapping={headlineMapping}>
  +<MuiTypography variantMapping={variantMapping}>
  ```

- [InputLabel] Remove FormLabelClasses in favor of asterisk class (#14504) @umairfarooq44
````

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; grep -rn -B3 -A10 "labelContainer\|labelWrapped\|label:" docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js; grep -n -B3 -A8 "labelContainer\|MuiTab" docs/src/pages/premium-themes/paperbase/Paperbase.js; ls docs/src/pages/guides/; grep -rn "classes={{.*label" docs/src/pages/demos/tabs | head
```

tool result:

```
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js-50-        color: '#999',
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js-51-      },
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js-52-    },
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js:53:    labelContainer: {
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js-54-      padding: 0,
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js-55-      [theme.breakpoints.up('md')]: {
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js-56-        padding: 0,
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js-57-        paddingLeft: 0,
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js-58-        paddingRight: 0,
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js-59-      },
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js-60-    },
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js:61:    label: {
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js-62-      letterSpacing: 1,
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js-63-      textTransform: 'uppercase',
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js-64-    },
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js-65-  },
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js-66-});
--
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-40-        fontSize: 26.25,
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-41-      },
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-42-    },
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js:43:    labelContainer: {
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-44-      width: '100%',
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-45-      padding: 15,
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-46-      [theme.breakpoints.up('md')]: {
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-47-        padding: 15,
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-48-      },
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-49-      '&:hover': {
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-50-        backgroundColor: 'rgba(29, 161, 242, 0.1)',
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-51-      },
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-52-    },
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js:53:    label: {
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-54-      textTransform: 'none',
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-55-      fontSize: 15,
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-56-      fontWeight: 700,
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-57-      color: '#657786',
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-58-    },
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-59-  },
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js-60-});
46-        },
47-      },
48-    },
49:    MuiTabs: {
50-      root: {
51-        marginLeft: theme.spacing(1),
52-      },
53-      indicator: {
54-        height: 3,
55-        borderTopLeftRadius: 3,
56-        borderTopRightRadius: 3,
57-        backgroundColor: theme.palette.common.white,
58-      },
59-    },
60:    MuiTab: {
61-      root: {
62-        textTransform: 'initial',
63-        margin: '0 16px',
64-        minWidth: 0,
65-        [theme.breakpoints.up('md')]: {
66-          minWidth: 0,
67-        },
68-      },
69:      labelContainer: {
70-        padding: 0,
71-        [theme.breakpoints.up('md')]: {
72-          padding: 0,
73-        },
74-      },
75-    },
76-    MuiIconButton: {
77-      root: {
--
110-    },
111-  },
112-  props: {
113:    MuiTab: {
114-      disableRipple: true,
115-    },
116-  },
117-  mixins: {
118-    ...theme.mixins,
119-    toolbar: {
120-      minHeight: 48,
121-    },
api
composition
csp
flow
interoperability
migration-v0x
minimizing-bundle-size
right-to-left
server-rendering
testing
typescript
```

**thinking:**

```
I found that wrapped labels incorrectly inherit the button's 1.75 line-height due to extra wrapper spans and an empty `labelWrapped` class from JS measurement. I'll remove that measurement logic and extra spans, shift padding to the root, and add a `wrapped` prop implementing Material's two-line spec (12px font, 1.5 line-height).


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; python3 - <<'EOF'
p='packages/material-ui/src/Tab/Tab.js'
s=open(p).read()
def rep(a,b):
    global s
    assert a in s, a
    s=s.replace(a,b,1)
rep("""    boxSizing: 'border-box',
    padding: 0,
    minHeight: 48,
    flexShrink: 0,
    overflow: 'hidden',
    whiteSpace: 'normal',
    textAlign: 'center',
    [theme.breakpoints.up('md')]: {
      fontSize: theme.typography.pxToRem(13),
      minWidth: 160,
    },
  },""","""    boxSizing: 'border-box',
    minHeight: 48,
    flexShrink: 0,
    padding: '6px 12px',
    overflow: 'hidden',
    whiteSpace: 'normal',
    textAlign: 'center',
    [theme.breakpoints.up('md')]: {
      padding: '6px 24px',
      fontSize: theme.typography.pxToRem(13),
      minWidth: 160,
    },
  },""")
rep("""    minHeight: 72,
    // paddingTop supposed to be 12px
    // - 3px from the paddingBottom
    paddingTop: 9,
    // paddingBottom supposed to be 12px
    // -3px for line-height of the label
    // -6px for label padding
    // = 3px
  },""","""    minHeight: 72,
    paddingTop: 9,
    '& $wrapper > *:first-child': {
      marginBottom: 6,
    },
  },""")
rep("""    maxWidth: 'none',
  },
""","""    maxWidth: 'none',
  },
  /* Styles applied to the root element if `wrapped={true}`. */
  wrapped: {
    fontSize: theme.typography.pxToRem(12),
    lineHeight: 1.5,
  },
""")
rep("""    flexDirection: 'column',
  },
  /* Styles applied to the label container element if `label` is provided. */
  labelContainer: {
    width: '100%', // Fix an IE 11 issue
    boxSizing: 'border-box',
    padding: '6px 12px',
    [theme.breakpoints.up('md')]: {
      padding: '6px 24px',
    },
  },
  /* Styles applied to the label wrapper element if `label` is provided. */
  label: {},
  /* Deprecated, the styles will be removed in v4. */
  labelWrapped: {},
});""","""    flexDirection: 'column',
  },
});""")
rep("""  state = {
    labelWrapped: false,
  };

  componentDidMount() {
    this.checkTextWrap();
  }

  componentDidUpdate(prevProps, prevState) {
    if (this.state.labelWrapped === prevState.labelWrapped) {
      /**
       * At certain text and tab lengths, a larger font size may wrap to two lines while the smaller
       * font size still only requires one line.  This check will prevent an infinite render loop
       * from occurring in that scenario.
       */
      this.checkTextWrap();
    }
  }

""","")
rep("""  checkTextWrap = () => {
    if (this.labelRef) {
      const labelWrapped = this.labelRef.getClientRects().length > 1;
      if (this.state.labelWrapped !== labelWrapped) {
        this.setState({ labelWrapped });
      }
    }
  };

""","")
rep("""      label: labelProp,
      onChange,
      selected,
      textColor,
      value,
      ...other
    } = this.props;

    let label;

    if (labelProp !== undefined) {
      label = (
        <span className={classes.labelContainer}>
          <span
            className={clsx(classes.label, {
              [classes.labelWrapped]: this.state.labelWrapped,
            })}
            ref={ref => {
              this.labelRef = ref;
            }}
          >
            {labelProp}
          </span>
        </span>
      );
    }
""","""      label,
      onChange,
      selected,
      textColor,
      value,
      wrapped,
      ...other
    } = this.props;
""")
rep("""            [classes.fullWidth]: fullWidth,
          },""","""            [classes.fullWidth]: fullWidth,
            [classes.wrapped]: wrapped,
          },""")
rep("""  value: PropTypes.any,
};

Tab.defaultProps = {
  disabled: false,
  textColor: 'inherit',
};""","""  value: PropTypes.any,
  /**
   * Tab labels appear in a single row.
   * They can use a second line if needed.
   */
  wrapped: PropTypes.bool,
};

Tab.defaultProps = {
  disabled: false,
  textColor: 'inherit',
  wrapped: false,
};""")
open(p,'w').write(s)

p='packages/material-ui/src/Tab/Tab.d.ts'
s=open(p).read()
rep("""  textColor?: string | 'secondary' | 'primary' | 'inherit';
""","""  textColor?: string | 'secondary' | 'primary' | 'inherit';
  wrapped?: boolean;
""")
rep("""  | 'wrapper'
  | 'labelContainer'
  | 'label'
  | 'labelWrapped';""","""  | 'wrapped'
  | 'wrapper';""")
open(p,'w').write(s)
EOF
git diff --stat
```

tool result:

```
 package.json                          |  7 ++-
 packages/material-ui/src/Tab/Tab.d.ts |  7 ++-
 packages/material-ui/src/Tab/Tab.js   | 87 ++++++++---------------------------
 yarn.lock                             | 51 +++++++++++++++++---
 4 files changed, 73 insertions(+), 79 deletions(-)
```

**assistant:** `package.json` and `yarn.lock` show changes I didn't make. I'll check what they are before going on.

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; git diff package.json; git log -1 --format=%cd; ls -la package.json yarn.lock
```

tool result:

```
diff --git a/package.json b/package.json
index 688d4e1c5..984805834 100644
--- a/package.json
+++ b/package.json
@@ -73,11 +73,16 @@
     "@emotion/core": "^10.0.0",
     "@emotion/styled": "^10.0.0",
     "@trendmicro/react-interpolate": "0.5.5",
+    "@types/chai": "^5.2.2",
+    "@types/chai-dom": "^1.11.3",
     "@types/enzyme": "^3.1.4",
+    "@types/format-util": "^1.0.4",
+    "@types/prop-types": "^15.7.15",
     "@types/react": "^16.7.10",
-    "@types/react-dom": "^16.0.9",
+    "@types/react-dom": "^19.1.8",
     "@types/react-router-dom": "^4.3.1",
     "@types/react-text-mask": "^5.4.2",
+    "@types/sinon": "^17.0.4",
     "@types/styled-components": "^4.1.8",
     "accept-language": "^3.0.18",
     "argos-cli": "^0.0.9",
Sat Feb 23 15:51:06 2019 +0100
-rw-r--r--  1 user  staff    9068 Aug 27  2025 package.json
-rw-r--r--  1 user  staff  595141 Aug 27  2025 yarn.lock
```

**thinking:**

```
The package.json/yarn.lock changes were pre-existing, so I'll leave them as is. Next, I'll update the doc themes that override the removed labelContainer/label keys and regenerate the API docs.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; sed -n 1,80p docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js; echo ----; sed -n 1,70p docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js; ls docs/pages/api/tab*; grep -n '"docs:api\|"prettier\|"lint"' package.json
```

tool result:

```
export default ({ attach, theme, nest, ICON, TAB }) => ({
  MuiTabs: {
    root: {
      borderTop: '1px solid #efefef',
      overflow: 'visible',
    },
    fixed: {
      overflowX: 'visible',
    },
    indicator: {
      height: 1,
      transform: 'translateY(-53px)',
      backgroundColor: '#262626',
    },
  },
  MuiTab: {
    root: {
      lineHeight: 'inherit',
      minWidth: 0,
      marginRight: theme.spacing(1),
      marginLeft: theme.spacing(1),
      [theme.breakpoints.up('md')]: {
        minWidth: 0,
        marginRight: 30,
        marginLeft: 30,
      },
      [attach(TAB.selected)]: {
        [nest(TAB.label)]: {
          fontWeight: 600,
        },
        '& *': {
          color: '#262626 !important',
        },
      },
    },
    labelIcon: {
      minHeight: 53,
      paddingTop: 0,
      '& .MuiTab-wrapper': {
        flexDirection: 'row',
      },
      [nest(ICON.root)]: {
        fontSize: 16,
        marginRight: 6,
      },
    },
    wrapper: {
      flexDirection: 'row',
      '& *': {
        color: '#999',
      },
    },
    labelContainer: {
      padding: 0,
      [theme.breakpoints.up('md')]: {
        padding: 0,
        paddingLeft: 0,
        paddingRight: 0,
      },
    },
    label: {
      letterSpacing: 1,
      textTransform: 'uppercase',
    },
  },
});
----
export default ({ theme, attach, nest, ICON, TABS, TAB }) => ({
  MuiTabs: {
    root: {
      [attach(TABS.underline)]: {
        borderBottom: '1px solid #e6ecf0',
      },
      [`& .${TAB.selected} .${TAB.wrapper} *`]: {
        color: theme.palette.primary.main,
      },
    },
    indicator: {
      backgroundColor: theme.palette.primary.main,
    },
  },
  MuiTab: {
    root: {
      minHeight: 53,
      minWidth: 0,
      [theme.breakpoints.up('md')]: {
        minWidth: 0,
      },
      [attach(TAB.onlyIcon)]: {
        [nest(TAB.wrapper)]: {
          width: 'auto',
          padding: 8,
          borderRadius: 25,
          color: '#657786',
          '&:hover': {
            color: theme.palette.primary.main,
            backgroundColor: 'rgba(29, 161, 242, 0.1)',
          },
        },
      },
    },
    textColorInherit: {
      opacity: 1,
    },
    wrapper: {
      [nest(ICON.root)]: {
        fontSize: 26.25,
      },
    },
    labelContainer: {
      width: '100%',
      padding: 15,
      [theme.breakpoints.up('md')]: {
        padding: 15,
      },
      '&:hover': {
        backgroundColor: 'rgba(29, 161, 242, 0.1)',
      },
    },
    label: {
      textTransform: 'none',
      fontSize: 15,
      fontWeight: 700,
      color: '#657786',
    },
  },
});
(eval):1: no matches found: docs/pages/api/tab*
24:    "docs:api": "yarn docs:api:core && yarn docs:api:lab",
25:    "docs:api:core": "rimraf ./pages/api && cross-env BABEL_ENV=docs-development babel-node ./docs/scripts/buildApi.js ./packages/material-ui/src ./pages/api",
26:    "docs:api:lab": "rimraf ./pages/lab/api && cross-env BABEL_ENV=docs-development babel-node ./docs/scripts/buildApi.js ./packages/material-ui-lab/src ./pages/lab/api",
39:    "lint": "eslint . --cache --report-unused-disable-directives && echo \"eslint: no lint errors\"",
41:    "prettier": "yarn babel-node ./scripts/prettier.js",
42:    "prettier:all": "yarn babel-node ./scripts/prettier.js write",
160:    "prettier": "^1.8.2",
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; grep -rn "TAB\b\|TAB =" docs/src/pages/premium-themes --include=*.js | grep -v "components/" | head; grep -rln "TAB.label\|labelContainer" docs/src pages 2>/dev/null; ls pages/api | grep -i tab
```

tool result:

```
(eval):1: no matches found: --include=*.js
docs/src/pages/premium-themes/instapaper/components/molecules/Tab.js
docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js
docs/src/pages/premium-themes/tweeper/components/molecules/Tab.js
docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js
docs/src/pages/premium-themes/paperbase/Paperbase.js
pages/api/tab.md
pages/api/step-label.md
tab.js
tab.md
table-body.js
table-body.md
table-cell.js
table-cell.md
table-footer.js
table-footer.md
table-head.js
table-head.md
table-pagination.js
table-pagination.md
table-row.js
table-row.md
table-sort-label.js
table-sort-label.md
table.js
table.md
tabs.js
tabs.md
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; cat docs/src/pages/premium-themes/instapaper/components/molecules/Tab.js docs/src/pages/premium-themes/tweeper/components/molecules/Tab.js
```

tool result:

```
import React from 'react';
import clsx from 'clsx';
import MuiTab from '@material-ui/core/Tab';
import { TAB } from '../../theme/core';

const Tab = ({ className, inverted, ...props }) => (
  <MuiTab
    className={clsx(TAB.root, className)}
    classes={{ label: TAB.label, selected: TAB.selected }}
    {...props}
  />
);

export default Tab;
import React from 'react';
import clsx from 'clsx';
import MuiTab from '@material-ui/core/Tab';
import { TAB } from '../../theme/core';

const Tab = ({ className, onlyIcon, inverted, ...props }) => (
  <MuiTab
    className={clsx(TAB.root, className, onlyIcon && TAB.onlyIcon)}
    classes={{
      label: TAB.label,
      wrapper: TAB.wrapper,
      selected: TAB.selected,
    }}
    {...props}
  />
);

export default Tab;
```

**assistant:** Now I'll update the premium-theme demos so they stop passing or overriding the removed class keys. Otherwise withStyles would warn about unknown classes.

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; python3 - <<'EOF'
def edit(p, pairs):
    s=open(p).read()
    for a,b in pairs:
        assert a in s, (p,a)
        s=s.replace(a,b,1)
    open(p,'w').write(s)

edit('docs/src/pages/premium-themes/instapaper/components/molecules/Tab.js',[
("classes={{ label: TAB.label, selected: TAB.selected }}","classes={{ selected: TAB.selected }}")])
edit('docs/src/pages/premium-themes/tweeper/components/molecules/Tab.js',[
("""    classes={{
      label: TAB.label,
      wrapper: TAB.wrapper,""","""    classes={{
      wrapper: TAB.wrapper,""")])
edit('docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js',[
("""      lineHeight: 'inherit',
      minWidth: 0,
      marginRight: theme.spacing(1),
      marginLeft: theme.spacing(1),
      [theme.breakpoints.up('md')]: {
        minWidth: 0,
        marginRight: 30,
        marginLeft: 30,
      },
      [attach(TAB.selected)]: {
        [nest(TAB.label)]: {
          fontWeight: 600,
        },
        '& *': {""","""      lineHeight: 'inherit',
      minWidth: 0,
      padding: 0,
      marginRight: theme.spacing(1),
      marginLeft: theme.spacing(1),
      letterSpacing: 1,
      textTransform: 'uppercase',
      [theme.breakpoints.up('md')]: {
        minWidth: 0,
        padding: 0,
        marginRight: 30,
        marginLeft: 30,
      },
      [attach(TAB.selected)]: {
        fontWeight: 600,
        '& *': {"""),
("""    labelContainer: {
      padding: 0,
      [theme.breakpoints.up('md')]: {
        padding: 0,
        paddingLeft: 0,
        paddingRight: 0,
      },
    },
    label: {
      letterSpacing: 1,
      textTransform: 'uppercase',
    },
""","")])
edit('docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js',[
("""      minHeight: 53,
      minWidth: 0,
      [theme.breakpoints.up('md')]: {
        minWidth: 0,
      },
""","""      minHeight: 53,
      minWidth: 0,
      padding: 15,
      textTransform: 'none',
      fontSize: 15,
      fontWeight: 700,
      color: '#657786',
      [theme.breakpoints.up('md')]: {
        minWidth: 0,
        padding: 15,
        fontSize: 15,
      },
      '&:hover': {
        backgroundColor: 'rgba(29, 161, 242, 0.1)',
      },
"""),
("""    labelContainer: {
      width: '100%',
      padding: 15,
      [theme.breakpoints.up('md')]: {
        padding: 15,
      },
      '&:hover': {
        backgroundColor: 'rgba(29, 161, 242, 0.1)',
      },
    },
    label: {
      textTransform: 'none',
      fontSize: 15,
      fontWeight: 700,
      color: '#657786',
    },
""","")])
edit('docs/src/pages/premium-themes/paperbase/Paperbase.js',[
("""        textTransform: 'initial',
        margin: '0 16px',
        minWidth: 0,
        [theme.breakpoints.up('md')]: {
          minWidth: 0,
        },
      },
      labelContainer: {
        padding: 0,
        [theme.breakpoints.up('md')]: {
          padding: 0,
        },
      },""","""        textTransform: 'initial',
        margin: '0 16px',
        minWidth: 0,
        padding: 0,
        [theme.breakpoints.up('md')]: {
          padding: 0,
          minWidth: 0,
        },
      },""")])
EOF
grep -rn "label" docs/src/pages/premium-themes/*/theme/core.js 2>/dev/null | head; grep -rln "TAB\.label" docs/src
```

tool result:

```
(eval):121: no matches found: docs/src/pages/premium-themes/*/theme/core.js
```

**assistant:** For the tweeper icon-only tabs there's an edge case: before, the 15px padding and hover background lived on the label container, which those tabs don't render. I'll reset both for that case.

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; python3 - <<'EOF'
p='docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js'
s=open(p).read()
a="""      [attach(TAB.onlyIcon)]: {
        [nest(TAB.wrapper)]: {"""
b="""      [attach(TAB.onlyIcon)]: {
        padding: 0,
        '&:hover': {
          backgroundColor: 'transparent',
        },
        [nest(TAB.wrapper)]: {"""
assert a in s
s=s.replace(a,b,1)
open(p,'w').write(s)
EOF
git diff docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js | head -60; sed -n '/render()/,/^  }$/p' packages/material-ui/src/Tab/Tab.js
```

tool result:

```
diff --git a/docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js b/docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js
index fc53fbb10..a9673027c 100644
--- a/docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js
+++ b/docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js
@@ -16,10 +16,24 @@ export default ({ theme, attach, nest, ICON, TABS, TAB }) => ({
     root: {
       minHeight: 53,
       minWidth: 0,
+      padding: 15,
+      textTransform: 'none',
+      fontSize: 15,
+      fontWeight: 700,
+      color: '#657786',
       [theme.breakpoints.up('md')]: {
         minWidth: 0,
+        padding: 15,
+        fontSize: 15,
+      },
+      '&:hover': {
+        backgroundColor: 'rgba(29, 161, 242, 0.1)',
       },
       [attach(TAB.onlyIcon)]: {
+        padding: 0,
+        '&:hover': {
+          backgroundColor: 'transparent',
+        },
         [nest(TAB.wrapper)]: {
           width: 'auto',
           padding: 8,
@@ -40,21 +54,5 @@ export default ({ theme, attach, nest, ICON, TABS, TAB }) => ({
         fontSize: 26.25,
       },
     },
-    labelContainer: {
-      width: '100%',
-      padding: 15,
-      [theme.breakpoints.up('md')]: {
-        padding: 15,
-      },
-      '&:hover': {
-        backgroundColor: 'rgba(29, 161, 242, 0.1)',
-      },
-    },
-    label: {
-      textTransform: 'none',
-      fontSize: 15,
-      fontWeight: 700,
-      color: '#657786',
-    },
   },
 });
  render() {
    const {
      classes,
      className,
      disabled,
      fullWidth,
      icon,
      indicator,
      label,
      onChange,
      selected,
      textColor,
      value,
      wrapped,
      ...other
    } = this.props;

    return (
      <ButtonBase
        focusRipple
        className={clsx(
          classes.root,
          classes[`textColor${capitalize(textColor)}`],
          {
            [classes.disabled]: disabled,
            [classes.selected]: selected,
            [classes.labelIcon]: icon && label,
            [classes.fullWidth]: fullWidth,
            [classes.wrapped]: wrapped,
          },
          className,
        )}
        role="tab"
        aria-selected={selected}
        disabled={disabled}
        {...other}
        onClick={this.handleChange}
      >
        <span className={classes.wrapper}>
          {icon}
          {label}
        </span>
        {indicator}
      </ButtonBase>
    );
  }
```

**thinking:**

```
Tab now renders ButtonBase > span.wrapper > {icon}{label}, with wrapped labels getting fontSize: 12px and lineHeight: 1.5 via the new `wrapped` prop. Next I'll write a reproduction script to verify the DOM and CSS output, then run the existing tests.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; cat > packages/material-ui/src/Tab/repro.test.js <<'EOF'
import React from 'react';
import { assert } from 'chai';
import { createMount, getClasses } from '@material-ui/core/test-utils';
import { createMuiTheme } from '../styles';
import { styles } from './Tab';
import Tab from './Tab';

describe('repro Tab wrapped', () => {
  it('styles + DOM', () => {
    const theme = createMuiTheme();
    const s = styles(theme);
    console.log('wrapped style', JSON.stringify(s.wrapped), 'root lineHeight', s.root.lineHeight);
    const mount = createMount();
    const classes = getClasses(<Tab />);
    const w = mount(<Tab label="A very long label that spans two lines" wrapped />);
    const html = w.html();
    console.log(html);
    assert.include(html, classes.wrapped);
    assert.strictEqual(s.wrapped.lineHeight, 1.5);
    mount.cleanUp();
  });
});
EOF
cd ..; bin/envrun 'NODE_ENV=test npx mocha --require @babel/register packages/material-ui/src/Tab/repro.test.js packages/material-ui/src/Tab/Tab.test.js packages/material-ui/src/Tabs/Tabs.test.js 2>&1 | tail -60'; grep -n '"test:unit"' testbed/package.json
```

tool result:

```
Command did not complete within its 120s timeout and was moved to the background (ID: b4aue3h1n). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/9af23c25-a392-46e7-a485-4f859ea3077f/tasks/b4aue3h1n.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /work/mui__material-ui-14638/repo; directory changes made by the backgrounded command do not apply to subsequent commands.
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; grep -n '"test:unit"' package.json; cat .mocharc* test/mocha.opts 2>/dev/null
```

tool result:

```
Exit code 1
52:    "test:unit": "cross-env NODE_ENV=test mocha 'packages/**/*.test.js' 'docs/**/*.test.js' --exclude '**/node_modules/**'",
(eval):1: no matches found: .mocharc*
```

**tool call: Bash**

```bash
sleep 90; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/9af23c25-a392-46e7-a485-4f859ea3077f/tasks/b4aue3h1n.output; ls /work/mui__material-ui-14638/repo/test
```

**tool call: Bash**

```bash
cat /work/mui__material-ui-14638/repo/.mocharc.js
```

tool result:

```
Exit code 1
cat: /work/mui__material-ui-14638/repo/.mocharc.js: No such file or directory
```

tool result:

```
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

**tool call: Bash**

```bash
sleep 120; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/9af23c25-a392-46e7-a485-4f859ea3077f/tasks/b4aue3h1n.output
```

tool result:

```
Exit code 143
Command timed out after 2m 0s
```

**tool call: Bash**

```bash
sleep 100; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/9af23c25-a392-46e7-a485-4f859ea3077f/tasks/b4aue3h1n.output
```

tool result:

```
(Bash completed with no output)
```

**assistant:** The first mocha run is slow to start inside the container, probably babel compiling on a cold cache. I'm waiting for it to finish.

**tool call: Bash**

```bash
sleep 240; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/9af23c25-a392-46e7-a485-4f859ea3077f/tasks/b4aue3h1n.output
```

tool result:

```
(Bash completed with no output)
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; cat test/mocha.opts; ../bin/envrun 'ps aux | grep -c mocha; ps aux | grep mocha | head -3'
```

tool result:

```
--require @babel/register
--reporter dot
--recursive
test/utils/setup.js
7
root         7  0.0  0.0 289612  6320 ?        Ss   05:31   0:00 bash -lc NODE_ENV=test npx mocha --require @babel/register packages/material-ui/src/Tab/repro.test.js packages/material-ui/src/Tab/Tab.test.js packages/material-ui/src/Tabs/Tabs.test.js 2>&1 | tail -60
root        15  0.1  1.0 1139332 80656 ?       Sl   05:31   0:00 node --no-opt -r /proc/.reset /usr/local/nvm/versions/node/v16.20.2/bin/npx mocha --require @babel/register packages/material-ui/src/Tab/repro.test.js packages/material-ui/src/Tab/Tab.test.js packages/material-ui/src/Tabs/Tabs.test.js
root        27  0.0  0.0 287844  3320 ?        S    05:31   0:00 sh -c -- mocha --require @babel/register packages/material-ui/src/Tab/repro.test.js packages/material-ui/src/Tab/Tab.test.js packages/material-ui/src/Tabs/Tabs.test.js
```

**assistant:** The run looks hung (almost no CPU after several minutes). I'll kill it and call mocha directly, with a timeout.

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; ../bin/envrun 'pkill -f mocha; ps aux | grep -v grep | grep -c mocha; NODE_ENV=test timeout 500 ./node_modules/.bin/mocha packages/material-ui/src/Tab/repro.test.js packages/material-ui/src/Tab/Tab.test.js packages/material-ui/src/Tabs/Tabs.test.js 2>&1 | tail -60'
```

tool result:

```
Exit code 143
```

**assistant:** `pkill -f mocha` also matched and killed the shell running it. I'll start the tests in a separate call.

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; ../bin/envrun 'NODE_ENV=test timeout 500 ./node_modules/.bin/mocha packages/material-ui/src/Tab/repro.test.js packages/material-ui/src/Tab/Tab.test.js packages/material-ui/src/Tabs/Tabs.test.js 2>&1 | tail -60'
```

tool result:

```
       prop: label
         should render with text wrapping:
     TypeError: instance.checkTextWrap is not a function
      at Context.checkTextWrap (packages/material-ui/src/Tab/Tab.test.js:83:16)
      at processImmediate (node:internal/timers:466:21)

  4) <Tab />
       prop: classes
         should render label with a custom label class:
     Error: Warning: Material-UI: the key `label` provided to the classes property is not implemented in Tab.
You can only override one of the following: root,labelIcon,textColorInherit,textColorPrimary,textColorSecondary,selected,disabled,fullWidth,wrapped,wrapper.
      at _construct (node_modules/@babel/runtime/helpers/construct.js:30:21)
      at console.error (test/utils/consoleError.js:8:5)
      at printWarning (node_modules/warning/warning.js:34:15)
      at warning (node_modules/warning/warning.js:57:20)
      at /testbed/packages/material-ui/src/styles/mergeClasses.js:27:5
      at Array.forEach (<anonymous>)
      at forEach (packages/material-ui/src/styles/mergeClasses.js:26:27)
      at WithStyles.getClasses (packages/material-ui/src/styles/withStyles.js:168:35)
      at WithStyles.getClasses [as render] (packages/material-ui/src/styles/withStyles.js:281:49)
      at ReactShallowRenderer._mountClassComponent (node_modules/react-test-renderer/cjs/react-test-renderer-shallow.development.js:772:37)
      at ReactShallowRenderer.render (node_modules/react-test-renderer/cjs/react-test-renderer-shallow.development.js:710:14)
      at /testbed/node_modules/enzyme-adapter-react-16/build/ReactSixteenAdapter.js:496:35
      at withSetStateAllowed (node_modules/enzyme-adapter-utils/build/Utils.js:143:16)
      at Object.render (node_modules/enzyme-adapter-react-16/build/ReactSixteenAdapter.js:495:68)
      at new ShallowWrapper (node_modules/enzyme/build/ShallowWrapper.js:206:22)
      at shallow (node_modules/enzyme/build/shallow.js:21:10)
      at shallow (packages/material-ui/src/test-utils/createShallow.js:18:21)
      at Context.shallow (packages/material-ui/src/Tab/Tab.test.js:100:23)
      at processImmediate (node:internal/timers:466:21)

  5) <Tabs />
       prop: variant="scrollable"
         should get a scrollbar size listener:
     TypeError: performance.mark is not a function
      at beginMark (node_modules/react-dom/cjs/react-dom.development.js:9029:15)
      at startWorkLoopTimer (node_modules/react-dom/cjs/react-dom.development.js:9287:5)
      at renderRoot (node_modules/react-dom/cjs/react-dom.development.js:18908:3)
      at performWorkOnRoot (node_modules/react-dom/cjs/react-dom.development.js:19809:7)
      at performWork (node_modules/react-dom/cjs/react-dom.development.js:19721:7)
      at performSyncWork (node_modules/react-dom/cjs/react-dom.development.js:19695:3)
      at requestWork (node_modules/react-dom/cjs/react-dom.development.js:19564:5)
      at scheduleWork (node_modules/react-dom/cjs/react-dom.development.js:19373:5)
      at scheduleRootUpdate (node_modules/react-dom/cjs/react-dom.development.js:20041:3)
      at updateContainerAtExpirationTime (node_modules/react-dom/cjs/react-dom.development.js:20069:10)
      at updateContainer (node_modules/react-dom/cjs/react-dom.development.js:20126:10)
      at ReactRoot.render (node_modules/react-dom/cjs/react-dom.development.js:20422:3)
      at /testbed/node_modules/react-dom/cjs/react-dom.development.js:20559:14
      at unbatchedUpdates (node_modules/react-dom/cjs/react-dom.development.js:19924:10)
      at legacyRenderSubtreeIntoContainer (node_modules/react-dom/cjs/react-dom.development.js:20555:5)
      at Object.render (node_modules/react-dom/cjs/react-dom.development.js:20624:12)
      at Object.render (node_modules/enzyme-adapter-react-16/build/ReactSixteenAdapter.js:367:114)
      at new ReactWrapper (node_modules/enzyme/build/ReactWrapper.js:134:16)
      at mount (node_modules/enzyme/build/mount.js:21:10)
      at mount (packages/material-ui/src/test-utils/createMount.js:14:12)
      at Context.mount (packages/material-ui/src/Tabs/Tabs.test.js:390:28)
      at processImmediate (node:internal/timers:466:21)
```

**thinking:**

```
The repro passes, and the four `<Tab />` test failures are expected since they test the `checkTextWrap`/`label`/`labelRef` behavior this change removes. I'll now check if the `<Tabs />` `performance.mark` failure pre-existed by running tests against the stashed original source.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; ../bin/envrun 'NODE_ENV=test timeout 500 ./node_modules/.bin/mocha --reporter spec packages/material-ui/src/Tab/repro.test.js packages/material-ui/src/Tab/Tab.test.js 2>&1 | head -40'; git stash -q -- packages/material-ui/src/Tab/Tab.js && ../bin/envrun 'NODE_ENV=test timeout 500 ./node_modules/.bin/mocha packages/material-ui/src/Tabs/Tabs.test.js 2>&1 | grep -E "passing|failing"'; git stash pop -q; git status --short
```

tool result:

```
Command did not complete within its 600s timeout and was moved to the background (ID: byxolpi4q). Output is being written to: /tmp/cell-scratch/claude-502/<actor-session-slug>/9af23c25-a392-46e7-a485-4f859ea3077f/tasks/byxolpi4q.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /work/mui__material-ui-14638/repo; directory changes made by the backgrounded command do not apply to subsequent commands.
```

**assistant:** That command bundles a stash and a stash-pop, so I'll wait for it to finish before touching any files.

**tool call: Bash**

```bash
sleep 280; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/9af23c25-a392-46e7-a485-4f859ea3077f/tasks/byxolpi4q.output
```

tool result:

```
Browserslist: caniuse-lite is outdated. Please run next command `yarn upgrade caniuse-lite browserslist`


  repro Tab wrapped
wrapped style {"fontSize":"0.75rem","lineHeight":1.5} root lineHeight 1.75
<button class="MuiButtonBase-root-11 MuiTab-root-1 MuiTab-textColorInherit-3 MuiTab-wrapped-9" tabindex="0" type="button" role="tab"><span class="MuiTab-wrapper-10">A very long label that spans two lines</span><span class="MuiTouchRipple-root-14"></span></button>
    ✓ styles + DOM (121ms)

  <Tab />
    ✓ should render with the root class
    1) should have a ref on label property
    prop: className
      ✓ should render with the user and root classes
    prop: selected
      ✓ should render with the selected and root classes
    prop: disabled
      ✓ should render with the disabled and root classes
    prop: onClick
      ✓ should be called when a click is triggered
    prop: label
      2) should render label with the label class
      3) should render with text wrapping
    prop: classes
Warning: Material-UI: the key `label` provided to the classes property is not implemented in Tab.
You can only override one of the following: root,labelIcon,textColorInherit,textColorPrimary,textColorSecondary,selected,disabled,fullWidth,wrapped,wrapper.
      4) should render label with a custom label class
    prop: icon
      ✓ should render icon element
    prop: textColor
      ✓ should support the inherit value
    prop: fullWidth
      ✓ should have the fullWidth class
    prop: style
      ✓ should be able to override everything


  10 passing (259ms)
  4 failing

  1) <Tab />
```

**tool call: Bash**

```bash
sleep 240; cat /tmp/cell-scratch/claude-502/<actor-session-slug>/9af23c25-a392-46e7-a485-4f859ea3077f/tasks/byxolpi4q.output | tail -5; cd /work/mui__material-ui-14638/repo; git stash list; git status --short
```

tool result:

```
?? Dockerfile
?? custom-reporter.js
?? packages/material-ui/src/Tab/repro.test.js

[exited with code 0]
 M docs/src/pages/premium-themes/instapaper/components/molecules/Tab.js
 M docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js
 M docs/src/pages/premium-themes/paperbase/Paperbase.js
 M docs/src/pages/premium-themes/tweeper/components/molecules/Tab.js
 M docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js
 M package.json
 M packages/material-ui/src/Tab/Tab.d.ts
 M packages/material-ui/src/Tab/Tab.js
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
?? packages/material-ui/src/Tab/repro.test.js
```

**assistant:** The stash was restored cleanly and all my changes are back. I'll check the Tabs baseline result from that run.

**tool call: Bash**

```bash
grep -nE "passing|failing|M docs" /tmp/cell-scratch/claude-502/<actor-session-slug>/9af23c25-a392-46e7-a485-4f859ea3077f/tasks/byxolpi4q.output
```

tool result:

```
37:  10 passing (259ms)
38:  4 failing
42:  33 passing (344ms)
43:  1 failing
45: M docs/src/pages/premium-themes/instapaper/components/molecules/Tab.js
46: M docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js
47: M docs/src/pages/premium-themes/paperbase/Paperbase.js
48: M docs/src/pages/premium-themes/tweeper/components/molecules/Tab.js
49: M docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js
```

**thinking:**

```
Confirmed the `performance.mark` failure in `<Tabs />` is a pre-existing environment issue, not related to this change (same result with original Tab.js). Now I'll remove the repro file and update the generated API page `pages/api/tab.md`.


```

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; rm packages/material-ui/src/Tab/repro.test.js; cat pages/api/tab.md
```

tool result:

````
---
filename: /packages/material-ui/src/Tab/Tab.js
---

<!--- This documentation is automatically generated, do not try to edit it. -->

# Tab API

<p class="description">The API documentation of the Tab React component. Learn more about the properties and the CSS customization points.</p>

```js
import Tab from '@material-ui/core/Tab';
```



## Props

| Name | Type | Default | Description |
|:-----|:-----|:--------|:------------|
| <span class="prop-name">children</span> | <span class="prop-type">unsupportedProp</span> |   | This property isn't supported. Use the `component` property if you need to change the children structure. |
| <span class="prop-name">classes</span> | <span class="prop-type">object</span> |   | Override or extend the styles applied to the component. See [CSS API](#css) below for more details. |
| <span class="prop-name">disabled</span> | <span class="prop-type">bool</span> | <span class="prop-default">false</span> | If `true`, the tab will be disabled. |
| <span class="prop-name">icon</span> | <span class="prop-type">node</span> |   | The icon element. |
| <span class="prop-name">label</span> | <span class="prop-type">node</span> |   | The label element. |
| <span class="prop-name">value</span> | <span class="prop-type">any</span> |   | You can provide your own value. Otherwise, we fallback to the child position index. |

Any other properties supplied will be spread to the root element ([ButtonBase](/api/button-base/)).

## CSS

You can override all the class names injected by Material-UI thanks to the `classes` property.
This property accepts the following keys:


| Name | Description |
|:-----|:------------|
| <span class="prop-name">root</span> | Styles applied to the root element.
| <span class="prop-name">labelIcon</span> | Styles applied to the root element if both `icon` and `label` are provided.
| <span class="prop-name">textColorInherit</span> | Styles applied to the root element if `textColor="inherit"`.
| <span class="prop-name">textColorPrimary</span> | Styles applied to the root element if `textColor="primary"`.
| <span class="prop-name">textColorSecondary</span> | Styles applied to the root element if `textColor="secondary"`.
| <span class="prop-name">selected</span> | Styles applied to the root element if `selected={true}` (controlled by the Tabs component).
| <span class="prop-name">disabled</span> | Styles applied to the root element if `disabled={true}` (controlled by the Tabs component).
| <span class="prop-name">fullWidth</span> | Styles applied to the root element if `fullWidth={true}` (controlled by the Tabs component).
| <span class="prop-name">wrapper</span> | Styles applied to the `icon` and `label`'s wrapper element.
| <span class="prop-name">labelContainer</span> | Styles applied to the label container element if `label` is provided.
| <span class="prop-name">label</span> | Styles applied to the label wrapper element if `label` is provided.
| <span class="prop-name">labelWrapped</span> | Deprecated, the styles will be removed in v4.

Have a look at [overriding with classes](/customization/overrides/#overriding-with-classes) section
and the [implementation of the component](https://github.com/mui-org/material-ui/blob/master/packages/material-ui/src/Tab/Tab.js)
for more detail.

If using the `overrides` [key of the theme](/customization/themes/#css),
you need to use the following style sheet name: `MuiTab`.

## Inheritance

The properties of the [ButtonBase](/api/button-base/) component are also available.
You can take advantage of this behavior to [target nested components](/guides/api/#spread).

## Demos

- [Tabs](/demos/tabs/)
````

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; python3 - <<'EOF'
p='pages/api/tab.md'
s=open(p).read()
pairs=[("""| <span class="prop-name">value</span> | <span class="prop-type">any</span> |   | You can provide your own value. Otherwise, we fallback to the child position index. |
""","""| <span class="prop-name">value</span> | <span class="prop-type">any</span> |   | You can provide your own value. Otherwise, we fallback to the child position index. |
| <span class="prop-name">wrapped</span> | <span class="prop-type">bool</span> | <span class="prop-default">false</span> | Tab labels appear in a single row. They can use a second line if needed. |
"""),("""| <span class="prop-name">wrapper</span> | Styles applied to the `icon` and `label`'s wrapper element.
| <span class="prop-name">labelContainer</span> | Styles applied to the label container element if `label` is provided.
| <span class="prop-name">label</span> | Styles applied to the label wrapper element if `label` is provided.
| <span class="prop-name">labelWrapped</span> | Deprecated, the styles will be removed in v4.
""","""| <span class="prop-name">wrapped</span> | Styles applied to the root element if `wrapped={true}`.
| <span class="prop-name">wrapper</span> | Styles applied to the `icon` and `label`'s wrapper element.
""")]
for a,b in pairs:
    assert a in s; s=s.replace(a,b,1)
open(p,'w').write(s)
EOF
../bin/envrun 'timeout 400 ./node_modules/.bin/eslint packages/material-ui/src/Tab docs/src/pages/premium-themes && ./node_modules/.bin/prettier --list-different packages/material-ui/src/Tab/*.js packages/material-ui/src/Tab/*.ts docs/src/pages/premium-themes/*/theme/*/components/tabs.js docs/src/pages/premium-themes/*/components/molecules/Tab.js docs/src/pages/premium-themes/paperbase/Paperbase.js; echo done $?'
```

tool result:

```
Traceback (most recent call last):
  File "<stdin>", line 14, in <module>
AssertionError
docs/src/pages/premium-themes/instapaper/components/molecules/Tab.js
done 1
```

**assistant:** Two small issues: my markdown pattern didn't match exactly, and prettier wants the instapaper `Tab.js` reformatted now that its line is shorter. I'll fix both.

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; grep -n "value\|wrapper" pages/api/tab.md | cat -A | cut -c1-200 | head; ../bin/envrun './node_modules/.bin/prettier --write docs/src/pages/premium-themes/instapaper/components/molecules/Tab.js' ; git diff docs/src/pages/premium-themes/instapaper/components/molecules/Tab.js
```

tool result:

```
cat: illegal option -- A
usage: cat [-belnstuv] [file ...]
docs/src/pages/premium-themes/instapaper/components/molecules/Tab.js 43ms

diff --git a/docs/src/pages/premium-themes/instapaper/components/molecules/Tab.js b/docs/src/pages/premium-themes/instapaper/components/molecules/Tab.js
index ba5932c60..a86bbf4c5 100644
--- a/docs/src/pages/premium-themes/instapaper/components/molecules/Tab.js
+++ b/docs/src/pages/premium-themes/instapaper/components/molecules/Tab.js
@@ -4,11 +4,7 @@ import MuiTab from '@material-ui/core/Tab';
 import { TAB } from '../../theme/core';
 
 const Tab = ({ className, inverted, ...props }) => (
-  <MuiTab
-    className={clsx(TAB.root, className)}
-    classes={{ label: TAB.label, selected: TAB.selected }}
-    {...props}
-  />
+  <MuiTab className={clsx(TAB.root, className)} classes={{ selected: TAB.selected }} {...props} />
 );
 
 export default Tab;
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; grep -n "prop-name\">value\|prop-name\">wrapper\|labelWrapped" pages/api/tab.md | sed -n l | cut -c1-250
```

tool result:

```
26:| <span class="prop-name">value</span> | <span class="pr\
op-type">any</span> |   | You can provide your own value. O\
therwise, we fallback to the child position index. |$
46:| <span class="prop-name">wrapper</span> | Styles applie\
d to the `icon` and `label`'s wrapper element.$
49:| <span class="prop-name">labelWrapped</span> | Deprecat\
ed, the styles will be removed in v4.$
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; python3 - <<'EOF'
p='pages/api/tab.md'
lines=open(p).read().split('\n')
out=[]
for l in lines:
    if 'prop-name">labelContainer' in l or 'prop-name">label</span> | Styles' in l or 'prop-name">labelWrapped' in l:
        continue
    if 'prop-name">wrapper</span>' in l:
        out.append('| <span class="prop-name">wrapped</span> | Styles applied to the root element if `wrapped={true}`.')
    out.append(l)
    if 'prop-name">value</span>' in l:
        out.append('| <span class="prop-name">wrapped</span> | <span class="prop-type">bool</span> | <span class="prop-default">false</span> | Tab labels appear in a single row. They can use a second line if needed. |')
open(p,'w').write('\n'.join(out))
EOF
git diff pages/api/tab.md
```

tool result:

```
diff --git a/pages/api/tab.md b/pages/api/tab.md
index bb7422d90..1ea696f96 100644
--- a/pages/api/tab.md
+++ b/pages/api/tab.md
@@ -24,6 +24,7 @@ import Tab from '@material-ui/core/Tab';
 | <span class="prop-name">icon</span> | <span class="prop-type">node</span> |   | The icon element. |
 | <span class="prop-name">label</span> | <span class="prop-type">node</span> |   | The label element. |
 | <span class="prop-name">value</span> | <span class="prop-type">any</span> |   | You can provide your own value. Otherwise, we fallback to the child position index. |
+| <span class="prop-name">wrapped</span> | <span class="prop-type">bool</span> | <span class="prop-default">false</span> | Tab labels appear in a single row. They can use a second line if needed. |
 
 Any other properties supplied will be spread to the root element ([ButtonBase](/api/button-base/)).
 
@@ -43,10 +44,8 @@ This property accepts the following keys:
 | <span class="prop-name">selected</span> | Styles applied to the root element if `selected={true}` (controlled by the Tabs component).
 | <span class="prop-name">disabled</span> | Styles applied to the root element if `disabled={true}` (controlled by the Tabs component).
 | <span class="prop-name">fullWidth</span> | Styles applied to the root element if `fullWidth={true}` (controlled by the Tabs component).
+| <span class="prop-name">wrapped</span> | Styles applied to the root element if `wrapped={true}`.
 | <span class="prop-name">wrapper</span> | Styles applied to the `icon` and `label`'s wrapper element.
-| <span class="prop-name">labelContainer</span> | Styles applied to the label container element if `label` is provided.
-| <span class="prop-name">label</span> | Styles applied to the label wrapper element if `label` is provided.
-| <span class="prop-name">labelWrapped</span> | Deprecated, the styles will be removed in v4.
 
 Have a look at [overriding with classes](/customization/overrides/#overriding-with-classes) section
 and the [implementation of the component](https://github.com/mui-org/material-ui/blob/master/packages/material-ui/src/Tab/Tab.js)
```

**tool call: Bash**

```bash
cd /work/mui__material-ui-14638/repo; git status --short; git diff packages/material-ui/src/Tab/Tab.js | head -80
```

tool result:

```
 M docs/src/pages/premium-themes/instapaper/components/molecules/Tab.js
 M docs/src/pages/premium-themes/instapaper/theme/instapaper/components/tabs.js
 M docs/src/pages/premium-themes/paperbase/Paperbase.js
 M docs/src/pages/premium-themes/tweeper/components/molecules/Tab.js
 M docs/src/pages/premium-themes/tweeper/theme/tweeper/components/tabs.js
 M package.json
 M packages/material-ui/src/Tab/Tab.d.ts
 M packages/material-ui/src/Tab/Tab.js
 M pages/api/tab.md
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
diff --git a/packages/material-ui/src/Tab/Tab.js b/packages/material-ui/src/Tab/Tab.js
index 225674eb5..3ac76f87e 100644
--- a/packages/material-ui/src/Tab/Tab.js
+++ b/packages/material-ui/src/Tab/Tab.js
@@ -16,13 +16,14 @@ export const styles = theme => ({
     minWidth: 72,
     position: 'relative',
     boxSizing: 'border-box',
-    padding: 0,
     minHeight: 48,
     flexShrink: 0,
+    padding: '6px 12px',
     overflow: 'hidden',
     whiteSpace: 'normal',
     textAlign: 'center',
     [theme.breakpoints.up('md')]: {
+      padding: '6px 24px',
       fontSize: theme.typography.pxToRem(13),
       minWidth: 160,
     },
@@ -30,13 +31,10 @@ export const styles = theme => ({
   /* Styles applied to the root element if both `icon` and `label` are provided. */
   labelIcon: {
     minHeight: 72,
-    // paddingTop supposed to be 12px
-    // - 3px from the paddingBottom
     paddingTop: 9,
-    // paddingBottom supposed to be 12px
-    // -3px for line-height of the label
-    // -6px for label padding
-    // = 3px
+    '& $wrapper > *:first-child': {
+      marginBottom: 6,
+    },
   },
   /* Styles applied to the root element if `textColor="inherit"`. */
   textColorInherit: {
@@ -79,6 +77,11 @@ export const styles = theme => ({
     flexGrow: 1,
     maxWidth: 'none',
   },
+  /* Styles applied to the root element if `wrapped={true}`. */
+  wrapped: {
+    fontSize: theme.typography.pxToRem(12),
+    lineHeight: 1.5,
+  },
   /* Styles applied to the `icon` and `label`'s wrapper element. */
   wrapper: {
     display: 'inline-flex',
@@ -87,41 +90,9 @@ export const styles = theme => ({
     width: '100%',
     flexDirection: 'column',
   },
-  /* Styles applied to the label container element if `label` is provided. */
-  labelContainer: {
-    width: '100%', // Fix an IE 11 issue
-    boxSizing: 'border-box',
-    padding: '6px 12px',
-    [theme.breakpoints.up('md')]: {
-      padding: '6px 24px',
-    },
-  },
-  /* Styles applied to the label wrapper element if `label` is provided. */
-  label: {},
-  /* Deprecated, the styles will be removed in v4. */
-  labelWrapped: {},
 });
 
 class Tab extends React.Component {
-  state = {
-    labelWrapped: false,
-  };
-
-  componentDidMount() {
-    this.checkTextWrap();
-  }
-
-  componentDidUpdate(prevProps, prevState) {
-    if (this.state.labelWrapped === prevState.labelWrapped) {
-      /**
```

**assistant:** I've fixed the two-line tab problem by adding a `wrapped` prop to `Tab`. When it's set, the tab uses the Material spec's two-line style (12px font, line height 1.5) instead of the 1.75 line height. **This is a breaking change:** it removes the `labelContainer`, `label` and `labelWrapped` style keys, and 4 tests in the existing `Tab.test.js` now fail.

**Why the change was needed.** The label sat inside two extra `<span>`s. On mount and every update, the component measured whether the text had wrapped and added a `labelWrapped` class, but that class had no styles, so wrapped text kept the 1.75 line height. The extra spans also made it awkward to change the label's spacing.

**What changed in `packages/material-ui/src/Tab/Tab.js`:**
- **Simpler markup:** a tab now renders the button, then `span.wrapper`, then the icon and label.
- **Padding:** the padding that was on the label container (`6px 12px`, or `6px 24px` on medium screens and up) is now on the tab itself.
- **Icon + label tabs:** the 6px gap is now a margin under the icon.
- **Measurement removed:** the state, the mount/update checks and `checkTextWrap` are gone.
- **New prop and class:** `wrapped` (default `false`) adds the `wrapped` class.

**Breaking change:** anyone overriding `labelContainer`, `label` or `labelWrapped` will need to move those styles to `root` or `wrapped`. Wrapping is no longer detected automatically; you set `wrapped` on tabs whose labels need two lines. I wrote this from memory of how this was handled for v4 upstream and couldn't confirm it offline.

**Other files:**
- `Tab.d.ts` and `pages/api/tab.md` are updated for the new prop and class keys. I edited the API page by hand rather than regenerating every page.
- The Instapaper, Tweeper and Paperbase example themes used the removed keys, so I moved their styles onto `root`. For Tweeper's icon-only tabs I reset the padding and hover background, because those styles used to sit on the label container, which icon-only tabs didn't have.

**Testing:**
- A throwaway check confirmed the new markup, that `wrapped` adds the class, and that the class gets `lineHeight: 1.5`. I deleted it afterwards.
- `Tab.test.js` as it stands: 10 pass, 4 fail. The failures are the tests for what was removed: `checkTextWrap`, `labelRef`, and the `label`/`labelWrapped` classes. I left the tests alone as you asked; if you expected the old tests to keep passing, tell me and I'll do a smaller fix that keeps the old markup.
- `Tabs.test.js`: 33 pass, 1 fails with `performance.mark is not a function`. It fails the same way with the original code, so it's an environment problem.
- ESLint and Prettier pass on the changed files.

`package.json` and `yarn.lock` (extra `@types` packages) and the untracked `Dockerfile` and `custom-reporter.js` were already there before I started. I didn't touch them.

_session end: success, turns 33, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.16 s: ps aux | grep -c mocha; ps aux | grep mocha | head -3
- `rc=143` 685.29 s: NODE_ENV=test npx mocha --require @babel/register packages/material-ui/src/Tab/repro.test.js packages/material-ui/src/Tab/Tab.test.js packages/material-ui/src/Tabs/Tabs.test.js 2>&1 | tail -60
- `rc=143` 0.13 s: pkill -f mocha; ps aux | grep -v grep | grep -c mocha; NODE_ENV=test timeout 500 ./node_modules/.bin/mocha packages/material-ui/src/Tab/repro.test.js packages/material-ui/src/Tab/Tab.test.js packages/material-ui/src/Tabs/Tabs.test.js 2>&1 | tail -60
- `rc=0` 500.13 s: NODE_ENV=test timeout 500 ./node_modules/.bin/mocha packages/material-ui/src/Tab/repro.test.js packages/material-ui/src/Tab/Tab.test.js packages/material-ui/src/Tabs/Tabs.test.js 2>&1 | tail -60
- `rc=0` 500.15 s: NODE_ENV=test timeout 500 ./node_modules/.bin/mocha --reporter spec packages/material-ui/src/Tab/repro.test.js packages/material-ui/src/Tab/Tab.test.js 2>&1 | head -40
- `rc=0` 500.13 s: NODE_ENV=test timeout 500 ./node_modules/.bin/mocha packages/material-ui/src/Tabs/Tabs.test.js 2>&1 | grep -E "passing|failing"
- `rc=0` 7.01 s: timeout 400 ./node_modules/.bin/eslint packages/material-ui/src/Tab docs/src/pages/premium-themes && ./node_modules/.bin/prettier --list-different packages/material-ui/src/Tab/*.js packages/material-ui/src/Tab/*.ts docs/src/pages/premium-themes/*/theme/*/components/tabs.js docs/src/pages/premium-themes/*/components/molecules/Tab.js docs/src/pages/premium-themes/paperbase/Paperbase.js; echo done $?
- `rc=0` 0.49 s: ./node_modules/.bin/prettier --write docs/src/pages/premium-themes/instapaper/components/molecules/Tab.js
