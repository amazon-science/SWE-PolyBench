# Instance: mui__material-ui-38247

- Final resolved (evaluator, logs/mui__material-ui-38247_result.json): False
- Run state: DONE
- One attempt. Duration 530.1 s, turns 14, actor cost $0.36840439999999997, container commands 3
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/mui__material-ui-38247/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/mui__material-ui-38247/repo. Consider the following issue description:

<issue_description>
[docs] The documentation for <Icon/> doesn't render an icon for the SandBox
### Duplicates

- [X] I have searched the existing issues

### Related page

https://mui.com/material-ui/icons/

### Kind of issue

Broken demonstration

### Issue description

cmd + f for "add_cicle"

and click on the codesandbox for the example for `<Icon baseClassName="material-icons-two-tone">add_circle</Icon>`:

![Screenshot 2023-06-26 at 3 48 31 PM](https://github.com/mui/material-ui/assets/17265085/cb81d9ca-92e0-4ac8-8e5e-10c0b59a5da2)

See that the icon doesn't render, instead it renders "ad":
![Screenshot 2023-06-26 at 3 49 14 PM](https://github.com/mui/material-ui/assets/17265085/2d1da3db-4895-464c-bb60-2f9b34a75b2e)


### Context 🔦

In general, I think it's odd that every MUI icon has its own react component. ie: `<SendIcon/>`, `<StorageIcon/>`

I want to use a single generic icon component like `<Icon/>` and then pass in the icon I want with a string. It seems like the only way of accomplishing that is with `<Icon>icon_name</Icon>` but apparently thats not working. 

As an aside, why is the icon string passed in as a child and not something more robust and type-safe like a prop called `icon`.

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/mui__material-ui-38247/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/mui__material-ui-38247/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/mui__material-ui-38247/bin/envrun 'git status --short && ls'
Edits you make under /work/mui__material-ui-38247/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
ls docs/src/modules/sandbox && cat docs/src/modules/sandbox/CreateReactApp.ts && grep -rn "getHtml\|fonts.googleapis" docs/src/modules/sandbox | head -30
```

tool result:

```
CodeSandbox.test.js
CodeSandbox.ts
CreateReactApp.ts
Dependencies.test.js
Dependencies.ts
FileExtension.ts
StackBlitz.test.js
StackBlitz.ts
types.ts
import { DemoData } from 'docs/src/modules/sandbox/types';

export const getHtml = ({
  title,
  language,
  codeStyling,
}: {
  title: string;
  language: string;
  codeStyling?: 'Tailwind' | 'MUI System';
}) => {
  return `<!DOCTYPE html>
<html lang="${language}">
  <head>
    <title>${title}</title>
    <!-- Fonts to support Material Design -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap"
    />
    <!-- Icons to support Material Design -->
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/icon?family=Material+Icons"
    />${
      codeStyling === 'Tailwind'
        ? `
    <!-- Check the Tailwind CSS's installation guide for setting up tailwind: https://tailwindcss.com/docs/installation -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
      tailwind.config = {
        theme: {
          extend: {
            animation: {
              appear: 'in-right 200ms',
            },
            border: {
              3: '3px',
            },
            boxShadow: {
              'outline-purple': '0 0 0 4px rgba(192, 132, 252, 0.25)',
              'outline-purple-light': '0 0 0 4px rgba(245, 208, 254, 0.25)',
              'outline-purple-xs': '0 0 0 1px rgba(192, 132, 252, 0.25)',
              'outline-switch': '0 0 1px 8px rgba(168, 85, 247, 0.35)',
            },
            cursor: {
              inherit: 'inherit',
            },
            keyframes: {
              'in-right': {
                from: { transform: 'translateX(100%)' },
                to: { transform: 'translateX(0)' },
              },
            },
            lineHeight: {
              '5.5': '1.375rem',
            },
            maxWidth: {
              snackbar: '560px',
            },
            minHeight: {
              badge: '22px',
            },
            minWidth: {
              badge: '22px',
              listbox: '200px',
              snackbar: '300px',
              'tabs-list': '400px',
            },
          },
        },
      }
    </script>`
        : ''
    }
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>`;
};

export function getRootIndex(demoData: DemoData) {
  // document.querySelector returns 'Element | null' but createRoot expects 'Element | DocumentFragment'.
  const type = demoData.codeVariant === 'TS' ? '!' : '';

  if (demoData.productId === 'joy-ui') {
    return `import * as React from 'react';
import * as ReactDOM from 'react-dom/client';
import { StyledEngineProvider, CssVarsProvider } from '@mui/joy/styles';
import Demo from './Demo';

ReactDOM.createRoot(document.querySelector("#root")${type}).render(
  <React.StrictMode>
    <StyledEngineProvider injectFirst>
      <CssVarsProvider>
        <Demo />
      </CssVarsProvider>
    </StyledEngineProvider>
  </React.StrictMode>
);`;
  }
  if (demoData.productId === 'base-ui') {
    return `import * as React from 'react';
import * as ReactDOM from 'react-dom/client';
import Demo from './Demo';

ReactDOM.createRoot(document.querySelector("#root")${type}).render(
  <React.StrictMode>
    <Demo />
  </React.StrictMode>
);`;
  }
  return `import * as React from 'react';
import * as ReactDOM from 'react-dom/client';
import { StyledEngineProvider } from '@mui/material/styles';
import Demo from './Demo';

ReactDOM.createRoot(document.querySelector("#root")${type}).render(
  <React.StrictMode>
    <StyledEngineProvider injectFirst>
      <Demo />
    </StyledEngineProvider>
  </React.StrictMode>
);`;
}

export const getTsconfig = () => `{
  "compilerOptions": {
    "target": "es5",
    "lib": [
      "dom",
      "dom.iterable",
      "esnext"
    ],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react"
  },
  "include": [
    "src"
  ]
}
`;
docs/src/modules/sandbox/CodeSandbox.test.js:52:    <link rel="preconnect" href="https://fonts.googleapis.com" />
docs/src/modules/sandbox/CodeSandbox.test.js:56:      href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap"
docs/src/modules/sandbox/CodeSandbox.test.js:61:      href="https://fonts.googleapis.com/icon?family=Material+Icons"
docs/src/modules/sandbox/CodeSandbox.test.js:141:    <link rel="preconnect" href="https://fonts.googleapis.com" />
docs/src/modules/sandbox/CodeSandbox.test.js:145:      href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap"
docs/src/modules/sandbox/CodeSandbox.test.js:150:      href="https://fonts.googleapis.com/icon?family=Material+Icons"
docs/src/modules/sandbox/CreateReactApp.ts:3:export const getHtml = ({
docs/src/modules/sandbox/CreateReactApp.ts:17:    <link rel="preconnect" href="https://fonts.googleapis.com" />
docs/src/modules/sandbox/CreateReactApp.ts:21:      href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap"
docs/src/modules/sandbox/CreateReactApp.ts:26:      href="https://fonts.googleapis.com/icon?family=Material+Icons"
docs/src/modules/sandbox/CodeSandbox.ts:42:      content: CRA.getHtml(demoData),
docs/src/modules/sandbox/CodeSandbox.ts:106:      content: CRA.getHtml({
docs/src/modules/sandbox/StackBlitz.ts:13:    'index.html': CRA.getHtml(demoData),
docs/src/modules/sandbox/StackBlitz.test.js:39:    <link rel="preconnect" href="https://fonts.googleapis.com" />
docs/src/modules/sandbox/StackBlitz.test.js:43:      
[... 586 more characters not shown]
```

**assistant:** Let me check what the (already-updated) tests expect.

**tool call: Bash**

```bash
sed -n 1,170p docs/src/modules/sandbox/CodeSandbox.test.js; git log --oneline -1 -- docs/src/modules/sandbox; grep -rn "Material+Icons" docs --include=*.js --include=*.ts --include=*.tsx | grep -v sandbox/ | head
```

tool result:

```
import { expect } from 'chai';
import CodeSandbox from './CodeSandbox';

const testCase = `import * as React from 'react';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';

export default function BasicButtons() {
  return (
    <Stack spacing={2} direction="row">
      <Button variant="text">Text</Button>
      <Button variant="contained">Contained</Button>
      <Button variant="outlined">Outlined</Button>
    </Stack>
  );
}
`;

describe('CodeSandbox', () => {
  it('generate the correct JavaScript result', () => {
    const result = CodeSandbox.createReactApp({
      title: 'BasicButtons Material Demo',
      githubLocation:
        'https://github.com/mui/material-ui/blob/v5.7.0/docs/data/material/components/buttons/BasicButtons.js',
      codeVariant: 'JS',
      language: 'en',
      raw: testCase,
    });
    expect(result.files).to.deep.equal({
      'package.json': {
        content: {
          description:
            'https://github.com/mui/material-ui/blob/v5.7.0/docs/data/material/components/buttons/BasicButtons.js',
          dependencies: {
            react: 'latest',
            '@mui/material': 'latest',
            'react-dom': 'latest',
            '@emotion/react': 'latest',
            '@emotion/styled': 'latest',
          },
          devDependencies: {
            'react-scripts': 'latest',
          },
        },
      },
      'public/index.html': {
        content: `<!DOCTYPE html>
<html lang="en">
  <head>
    <title>BasicButtons Material Demo</title>
    <!-- Fonts to support Material Design -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap"
    />
    <!-- Icons to support Material Design -->
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/icon?family=Material+Icons"
    />
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>`,
      },
      'Demo.js': {
        content: `import * as React from 'react';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';

export default function BasicButtons() {
  return (
    <Stack spacing={2} direction="row">
      <Button variant="text">Text</Button>
      <Button variant="contained">Contained</Button>
      <Button variant="outlined">Outlined</Button>
    </Stack>
  );
}
`,
      },
      'index.js': {
        content: `import * as React from 'react';
import * as ReactDOM from 'react-dom/client';
import { StyledEngineProvider } from '@mui/material/styles';
import Demo from './Demo';

ReactDOM.createRoot(document.querySelector("#root")).render(
  <React.StrictMode>
    <StyledEngineProvider injectFirst>
      <Demo />
    </StyledEngineProvider>
  </React.StrictMode>
);`,
      },
    });
  });

  it('generate the correct TypeScript result', () => {
    const result = CodeSandbox.createReactApp({
      title: 'BasicButtons Material Demo',
      githubLocation:
        'https://github.com/mui/material-ui/blob/v5.7.0/docs/data/material/components/buttons/BasicButtons.tsx',
      codeVariant: 'TS',
      language: 'en',
      raw: testCase,
    });
    expect(result.files).to.deep.equal({
      'package.json': {
        content: {
          description:
            'https://github.com/mui/material-ui/blob/v5.7.0/docs/data/material/components/buttons/BasicButtons.tsx',
          dependencies: {
            react: 'latest',
            '@mui/material': 'latest',
            'react-dom': 'latest',
            '@emotion/react': 'latest',
            '@emotion/styled': 'latest',
            '@types/react': 'latest',
            '@types/react-dom': 'latest',
            typescript: 'latest',
          },
          devDependencies: {
            'react-scripts': 'latest',
          },
          main: 'index.tsx',
          scripts: {
            start: 'react-scripts start',
          },
        },
      },
      'public/index.html': {
        content: `<!DOCTYPE html>
<html lang="en">
  <head>
    <title>BasicButtons Material Demo</title>
    <!-- Fonts to support Material Design -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap"
    />
    <!-- Icons to support Material Design -->
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/icon?family=Material+Icons"
    />
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>`,
      },
      'Demo.tsx': {
        content: `import * as React from 'react';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';

export default function BasicButtons() {
  return (
    <Stack spacing={2} direction="row">
      <Button variant="text">Text</Button>
      <Button variant="contained">Contained</Button>
      <Button variant="outlined">Outlined</Button>
    </Stack>
  );
ddf840bf3c [docs] Use IBM Plex Sans in Tailwind CSS demos (#38464)
(eval):1: no matches found: --include=*.js
```

**tool call: Bash**

```bash
ls docs/data/material/components/icons/; cat docs/data/material/components/icons/TwoToneIcons.js docs/data/material/components/icons/Icons.js; grep -rn "two-tone\|Material+Icons" docs/data/material/components/icons/*.md docs/pages/_document.js docs/src -r | head -20
```

tool result:

```
CreateSvgIcon.js
CreateSvgIcon.tsx
CreateSvgIcon.tsx.preview
FontAwesomeIcon.js
FontAwesomeIcon.tsx
FontAwesomeIcon.tsx.preview
FontAwesomeIconSize.js
FontAwesomeIconSize.tsx
FontAwesomeIconSize.tsx.preview
FontAwesomeSvgIconDemo.js
FontAwesomeSvgIconDemo.tsx
FontAwesomeSvgIconDemo.tsx.preview
Icons.js
Icons.tsx
Icons.tsx.preview
SvgIconChildren.js
SvgIconChildren.tsx
SvgIconChildren.tsx.preview
SvgIconsColor.js
SvgIconsColor.tsx
SvgIconsColor.tsx.preview
SvgIconsSize.js
SvgIconsSize.tsx
SvgIconsSize.tsx.preview
SvgMaterialIcons.js
SvgMaterialIcons.tsx
TwoToneIcons.js
TwoToneIcons.tsx
TwoToneIcons.tsx.preview
icons.md
import * as React from 'react';
import Icon from '@mui/material/Icon';

export default function TwoToneIcons() {
  return <Icon baseClassName="material-icons-two-tone">add_circle</Icon>;
}
import * as React from 'react';
import Box from '@mui/material/Box';
import { green } from '@mui/material/colors';
import Icon from '@mui/material/Icon';

export default function Icons() {
  return (
    <Box
      sx={{
        '& > :not(style)': {
          m: 2,
        },
      }}
    >
      <Icon>add_circle</Icon>
      <Icon color="primary">add_circle</Icon>
      <Icon sx={{ color: green[500] }}>add_circle</Icon>
      <Icon fontSize="small">add_circle</Icon>
      <Icon sx={{ fontSize: 30 }}>add_circle</Icon>
    </Box>
  );
}
docs/data/material/components/icons/icons.md:218:  href="https://fonts.googleapis.com/icon?family=Material+Icons"
docs/data/material/components/icons/icons.md:227:For instance, you can display two-tone icons with Material Design:
docs/data/material/components/icons/icons.md:234:  href="https://fonts.googleapis.com/css?family=Material+Icons+Two+Tone"
docs/data/material/components/icons/icons.md:252:        baseClassName: 'material-icons-two-tone',
docs/data/material/components/icons/icons.md:259:Then, you can use the two-tone font directly:
docs/src/modules/sandbox/CodeSandbox.test.js:61:      href="https://fonts.googleapis.com/icon?family=Material+Icons"
docs/src/modules/sandbox/CodeSandbox.test.js:150:      href="https://fonts.googleapis.com/icon?family=Material+Icons"
docs/src/modules/sandbox/CreateReactApp.ts:26:      href="https://fonts.googleapis.com/icon?family=Material+Icons"
docs/src/modules/sandbox/StackBlitz.test.js:48:      href="https://fonts.googleapis.com/icon?family=Material+Icons"
docs/src/modules/sandbox/StackBlitz.test.js:123:      href="https://fonts.googleapis.com/icon?family=Material+Icons"
```

**tool call: Bash**

```bash
cat packages/mui-material/src/Icon/Icon.test.js | head -80; sed -n 200,275p docs/data/material/components/icons/icons.md
```

tool result:

````
import * as React from 'react';
import { expect } from 'chai';
import { createRenderer, describeConformance } from 'test/utils';
import Icon, { iconClasses as classes } from '@mui/material/Icon';

describe('<Icon />', () => {
  const { render } = createRenderer();

  describeConformance(<Icon>account_circle</Icon>, () => ({
    classes,
    inheritComponent: 'span',
    render,
    muiName: 'MuiIcon',
    refInstanceof: window.HTMLSpanElement,
    testComponentPropWith: 'div',
    skip: ['themeVariants', 'componentsProp'],
  }));

  it('renders children by default', () => {
    const { getByTestId } = render(<Icon data-testid="root">account_circle</Icon>);

    expect(getByTestId('root')).to.have.text('account_circle');
  });

  describe('optional classes', () => {
    it('should render with the secondary color', () => {
      const { getByTestId } = render(
        <Icon data-testid="root" color="secondary">
          account_circle
        </Icon>,
      );

      expect(getByTestId('root')).to.have.class(classes.colorSecondary);
    });

    it('should render with the action color', () => {
      const { getByTestId } = render(
        <Icon data-testid="root" color="action">
          account_circle
        </Icon>,
      );

      expect(getByTestId('root')).to.have.class(classes.colorAction);
    });

    it('should render with the error color', () => {
      const { getByTestId } = render(
        <Icon data-testid="root" color="error">
          account_circle
        </Icon>,
      );

      expect(getByTestId('root')).to.have.class(classes.colorError);
    });

    it('should render with the primary class', () => {
      const { getByTestId } = render(
        <Icon data-testid="root" color="primary">
          account_circle
        </Icon>,
      );

      expect(getByTestId('root')).to.have.class(classes.colorPrimary);
    });

    it('should render without the default class', () => {
      const { getByTestId } = render(
        <Icon data-testid="root" baseClassName="material-icons-round">
          account_circle
        </Icon>,
      );

      expect(getByTestId('root')).not.to.have.class('material-icons');
    });

    it('should render with the supplied base class', () => {
      const { getByTestId } = render(
        <Icon data-testid="root" baseClassName="material-icons-round">
          account_circle
        </Icon>,

```jsx
import Icon from '@mui/material/Icon';

<Icon>star</Icon>;
```

By default, an Icon will inherit the current text color.
Optionally, you can set the icon color using one of the theme color properties: `primary`, `secondary`, `action`, `error` & `disabled`.

### Font Material Icons

`Icon` will by default set the correct base class name for the Material Icons font (filled variant).
All you need to do is load the font, for instance, via Google Web Fonts:

```html
<link
  rel="stylesheet"
  href="https://fonts.googleapis.com/icon?family=Material+Icons"
/>
```

{{"demo": "Icons.js"}}

### Custom font

For other fonts, you can customize the baseline class name using the `baseClassName` prop.
For instance, you can display two-tone icons with Material Design:

```jsx
import Icon from '@mui/material/Icon';

<link
  rel="stylesheet"
  href="https://fonts.googleapis.com/css?family=Material+Icons+Two+Tone"
  // Import the two tones MD variant                           ^^^^^^^^
/>;
```

{{"demo": "TwoToneIcons.js"}}

#### Global base class name

Modifying the `baseClassName` prop for each component usage is repetitive.
You can change the default prop globally with the theme

```js
const theme = createTheme({
  components: {
    MuiIcon: {
      defaultProps: {
        // Replace the `material-icons` default value.
        baseClassName: 'material-icons-two-tone',
      },
    },
  },
});
```

Then, you can use the two-tone font directly:

```jsx
<Icon>add_circle</Icon>
```

### Font Awesome

[Font Awesome](https://fontawesome.com/icons) can be used with the `Icon` component as follows:

{{"demo": "FontAwesomeIcon.js"}}

Note that the Font Awesome icons weren't designed like the Material Icons (compare the two previous demos).
The fa icons are cropped to use all the space available. You can adjust for this with a global override:

```js
const theme = createTheme({
````

**tool call: Bash**

```bash
cat docs/data/material/components/icons/FontAwesomeIcon.js docs/data/material/components/icons/TwoToneIcons.tsx docs/data/material/components/icons/TwoToneIcons.tsx.preview; grep -rn "Two+Tone\|Material+Icons" docs/pages docs/src --include=*.js | head
```

tool result:

```
import * as React from 'react';
import { loadCSS } from 'fg-loadcss';
import Box from '@mui/material/Box';
import { green } from '@mui/material/colors';
import Icon from '@mui/material/Icon';

export default function FontAwesomeIcon() {
  React.useEffect(() => {
    const node = loadCSS(
      'https://use.fontawesome.com/releases/v5.14.0/css/all.css',
      // Inject before JSS
      document.querySelector('#font-awesome-css') || document.head.firstChild,
    );

    return () => {
      node.parentNode.removeChild(node);
    };
  }, []);

  return (
    <Box
      sx={{
        '& > :not(style)': {
          m: 2,
        },
      }}
    >
      <Icon baseClassName="fas" className="fa-plus-circle" />
      <Icon baseClassName="fas" className="fa-plus-circle" color="primary" />
      <Icon
        baseClassName="fas"
        className="fa-plus-circle"
        sx={{ color: green[500] }}
      />
      <Icon baseClassName="fas" className="fa-plus-circle" fontSize="small" />
      <Icon baseClassName="fas" className="fa-plus-circle" sx={{ fontSize: 30 }} />
    </Box>
  );
}
import * as React from 'react';
import Icon from '@mui/material/Icon';

export default function TwoToneIcons() {
  return <Icon baseClassName="material-icons-two-tone">add_circle</Icon>;
}
<Icon baseClassName="material-icons-two-tone">add_circle</Icon>(eval):1: no matches found: --include=*.js
```

**tool call: Bash**

```bash
grep -rn "Two+Tone\|Material+Icons" docs/pages docs/src | grep -v test.js | head; grep -n "fg-loadcss" docs/package.json
```

tool result:

```
docs/pages/_app.js:116:    'https://fonts.googleapis.com/icon?family=Material+Icons|Material+Icons+Two+Tone',
docs/src/modules/sandbox/CreateReactApp.ts:26:      href="https://fonts.googleapis.com/icon?family=Material+Icons"
83:    "fg-loadcss": "^3.1.0",
```

**tool call: Bash**

```bash
sed -n 105,125p docs/pages/_app.js; cat docs/data/material/components/icons/FontAwesomeIcon.tsx | head -20
```

tool result:

```
let dependenciesLoaded = false;

function loadDependencies() {
  if (dependenciesLoaded) {
    return;
  }

  dependenciesLoaded = true;

  loadCSS(
    'https://fonts.googleapis.com/icon?family=Material+Icons|Material+Icons+Two+Tone',
    document.querySelector('#material-icon-font'),
  );
}

if (typeof window !== 'undefined' && process.env.NODE_ENV === 'production') {
  // eslint-disable-next-line no-console
  console.log(
    `%c

import * as React from 'react';
import { loadCSS } from 'fg-loadcss';
import Box from '@mui/material/Box';
import { green } from '@mui/material/colors';
import Icon from '@mui/material/Icon';

export default function FontAwesomeIcon() {
  React.useEffect(() => {
    const node = loadCSS(
      'https://use.fontawesome.com/releases/v5.14.0/css/all.css',
      // Inject before JSS
      document.querySelector('#font-awesome-css') || document.head.firstChild,
    );

    return () => {
      node.parentNode!.removeChild(node);
    };
  }, []);

  return (
```

**thinking:**

```
Found the cause: the sandbox HTML only loads `Material+Icons`, missing `Material+Icons+Two+Tone` that the docs site loads globally, so two-tone icons render as clipped raw text. I'll fix this by having the demo load its own font, mirroring how the neighboring Font Awesome demo does it.


```

**tool call: Bash**

```bash
cd docs/data/material/components/icons && for ext in js tsx; do
if [ $ext = tsx ]; then BANG='!'; else BANG=''; fi
cat > TwoToneIcons.$ext <<EOF
import * as React from 'react';
import { loadCSS } from 'fg-loadcss';
import Icon from '@mui/material/Icon';

export default function TwoToneIcons() {
  React.useEffect(() => {
    const node = loadCSS(
      'https://fonts.googleapis.com/icon?family=Material+Icons+Two+Tone',
      // Inject before JSS
      document.querySelector('#material-icon-font') || document.head.firstChild,
    );

    return () => {
      node.parentNode${BANG}.removeChild(node);
    };
  }, []);

  return <Icon baseClassName="material-icons-two-tone">add_circle</Icon>;
}
EOF
done; cd -; git diff
```

tool result:

```
<persisted-output>
Output too large (1.5MB). Full output saved to: <actor-session-dir>

Preview (first 2KB):
diff --git a/docs/data/material/components/icons/TwoToneIcons.js b/docs/data/material/components/icons/TwoToneIcons.js
index 125785fdc2..f878f93533 100644
--- a/docs/data/material/components/icons/TwoToneIcons.js
+++ b/docs/data/material/components/icons/TwoToneIcons.js
@@ -1,6 +1,19 @@
 import * as React from 'react';
+import { loadCSS } from 'fg-loadcss';
 import Icon from '@mui/material/Icon';
 
 export default function TwoToneIcons() {
+  React.useEffect(() => {
+    const node = loadCSS(
+      'https://fonts.googleapis.com/icon?family=Material+Icons+Two+Tone',
+      // Inject before JSS
+      document.querySelector('#material-icon-font') || document.head.firstChild,
+    );
+
+    return () => {
+      node.parentNode.removeChild(node);
+    };
+  }, []);
+
   return <Icon baseClassName="material-icons-two-tone">add_circle</Icon>;
 }
diff --git a/docs/data/material/components/icons/TwoToneIcons.tsx b/docs/data/material/components/icons/TwoToneIcons.tsx
index 125785fdc2..03c4b9bc44 100644
--- a/docs/data/material/components/icons/TwoToneIcons.tsx
+++ b/docs/data/material/components/icons/TwoToneIcons.tsx
@@ -1,6 +1,19 @@
 import * as React from 'react';
+import { loadCSS } from 'fg-loadcss';
 import Icon from '@mui/material/Icon';
 
 export default function TwoToneIcons() {
+  React.useEffect(() => {
+    const node = loadCSS(
+      'https://fonts.googleapis.com/icon?family=Material+Icons+Two+Tone',
+      // Inject before JSS
+      document.querySelector('#material-icon-font') || document.head.firstChild,
+    );
+
+    return () => {
+      node.parentNode!.removeChild(node);
+    };
+  }, []);
+
   return <Icon baseClassName="material-icons-two-tone">add_circle</Icon>;
 }
diff --git a/package.json b/package.json
index bf7b63102f..2581ad3fac 100644
--- a/package.json
+++ b/package.json
@@ -98,21 +98,24 @@
     "@testing-library/dom": "^9.3.1",
     "@testing-library/react": "^14.0.0",
     "@testing-library/user-event": "^14.4.3",
...
</persisted-output>
```

**assistant:** The diff also shows changes to `package.json` that I didn't make. I'll look at those before going further.

**tool call: Bash**

```bash
git status --short; git diff --stat
```

tool result:

```
 M docs/data/material/components/icons/TwoToneIcons.js
 M docs/data/material/components/icons/TwoToneIcons.tsx
 M package.json
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
 .../data/material/components/icons/TwoToneIcons.js |    13 +
 .../material/components/icons/TwoToneIcons.tsx     |    13 +
 package.json                                       |    11 +-
 yarn.lock                                          | 30490 ++++++++++---------
 4 files changed, 16057 insertions(+), 14470 deletions(-)
```

**thinking:**

```
I'll leave the package.json/yarn.lock/Dockerfile/custom-reporter.js changes untouched since those came from environment setup, not my edits. Next I'll verify the sandbox picks up fg-loadcss as a dependency, then run lint, type check, TS→JS sync, and sandbox tests.


```

**tool call: Bash**

```bash
/work/mui__material-ui-38247/bin/envrun 'cat > /tmp/repro.test.js <<EOF
const fs = require("fs");
const { expect } = require("chai");
const CodeSandbox = require("/testbed/docs/src/modules/sandbox/CodeSandbox").default;
it("two tone sandbox", () => {
  const r = CodeSandbox.createReactApp({ title: "t", githubLocation: "x", codeVariant: "JS", language: "en", raw: fs.readFileSync("/testbed/docs/data/material/components/icons/TwoToneIcons.js", "utf8") });
  console.log(r.files["package.json"].content.dependencies);
  expect(r.files["Demo.js"].content).to.include("Material+Icons+Two+Tone");
});
EOF
cp /tmp/repro.test.js docs/src/modules/sandbox/zzrepro.test.js
yarn -s cross-env NODE_ENV=test mocha docs/src/modules/sandbox/*.test.js 2>&1 | tail -20; rm docs/src/modules/sandbox/zzrepro.test.js
yarn -s eslint docs/data/material/components/icons/TwoToneIcons.* && yarn -s prettier --check docs/data/material/components/icons/TwoToneIcons.* && yarn -s tsc -p docs/tsconfig.json --noEmit 2>&1 | grep -i twotone; yarn -s docs:typescript:formatted >/dev/null 2>&1; git status --short docs'
```

tool result:

```
warning You don't appear to have an internet connection. Try the --offline flag to use the cache for registry queries.
Browserslist: caniuse-lite is outdated. Please run:
  npx update-browserslist-db@latest
  Why you should do it regularly: https://github.com/browserslist/update-db#readme
including inaccessible elements by default

{
  react: 'latest',
  'fg-loadcss': 'latest',
  '@mui/material': 'latest',
  'react-dom': 'latest',
  '@emotion/react': 'latest',
  '@emotion/styled': 'latest'
}

  ...................

  19 passing (39ms)

warning You don't appear to have an internet connection. Try the --offline flag to use the cache for registry queries.

/testbed/custom-reporter.js
   1:1   error  Unexpected var, use let or const instead                                       no-var
   2:1   error  Unexpected var, use let or const instead                                       no-var
   2:1   error  Expected 1 empty line after require statement not followed by another require  import/newline-after-import
   2:12  error  `path` import should occur before import of `mocha`                            import/order
   5:3   error  All 'var' declarations must be at the top of the function scope                vars-on-top
   5:3   error  Unexpected var, use let or const instead                                       no-var
   6:3   error  All 'var' declarations must be at the top of the function scope                vars-on-top
   6:3   error  Unexpected var, use let or const instead                                       no-var
   7:25  error  Unexpected unnamed function                                                    func-names
   7:25  error  Unexpected function expression                                                 prefer-arrow-callback
   8:5   error  Unexpected var, use let or const instead                                       no-var
   9:5   error  Unexpected var, use let or const instead                                       no-var
  10:5   error  Unexpected var, use let or const instead                                       no-var
  14:7   error  Expected property shorthand                                                    object-shorthand
  30:20  error  Unexpected unnamed function                                                    func-names
  30:20  error  Unexpected function expression                                                 prefer-arrow-callback
  31:5   error  Unexpected console statement                                                   no-console
  33:7   error  Expected property shorthand                                                    object-shorthand
  34:7   error  Expected property shorthand                                                    object-shorthand
  39:1   error  The '__proto__' property is deprecated                                         no-proto

/testbed/docs/data/material/components/icons/TwoToneIcons.tsx.preview
  1:1  error  'React' must be in scope when using JSX             react/react-in-jsx-scope
  1:1  error  JSX not allowed in files with extension '.preview'  react/jsx-filename-extension
  1:2  error  'Icon' is not defined                               react/jsx-no-undef
  1:2  error  'Icon' is not defined                               no-undef

✖ 24 problems (24 errors, 0 warnings)
  14 errors and 0 warnings potentially fixable with the `--fix` option.

 M docs/data/base/components/autocomplete/AutocompleteIntroduction/css/index.js
 M docs/data/base/components/autocomplete/AutocompleteIntroduction/system/index.js
 M docs/data/base/components/autocomplete/AutocompleteIntroduction/tailwind/index.js
 M docs/data/base/components/focus-trap/PortalFocusTrap.js
 M docs/data/joy/components/autocomplete/FreeSoloCreateOption.js
 M docs/data/joy/components/checkbox/ExampleChoiceChipCheckbox.js
 M docs/data/joy/components/input/InputSubscription.js
 M docs/data/material/components/app-bar/BottomAppBar.js
 M docs/data/material/components/icons/TwoToneIcons.js
 M docs/data/material/components/icons/TwoToneIcons.tsx
 M docs/data/material/components/skeleton/Facebook.js
 M docs/data/material/components/skeleton/YouTube.js
 M docs/data/material/components/steppers/HorizontalLinearStepper.js
 M docs/data/material/components/table/EnhancedTable.js
 M docs/data/material/getting-started/templates/checkout/Checkout.js
 M docs/src/pages/premium-themes/onepirate/modules/views/ProductValues.js
 M docs/src/pages/premium-themes/paperbase/Paperbase.js
```

**thinking:**

```
Fg-loadcss is now a sandbox dependency and all 19 tests pass, including my repro. The lint errors aren't real issues (just environment/glob noise), but the formatter unexpectedly rewrote unrelated demos—I'll revert those and keep only my two files.


```

**tool call: Bash**

```bash
git diff docs/data/material/components/icons/TwoToneIcons.js | head -30; git status --short docs | grep -v TwoToneIcons | awk '{print $2}' | xargs git checkout -- ; git status --short
```

**tool call: Bash**

```bash
/work/mui__material-ui-38247/bin/envrun 'yarn -s eslint docs/data/material/components/icons/TwoToneIcons.js docs/data/material/components/icons/TwoToneIcons.tsx && yarn -s prettier --check docs/data/material/components/icons/TwoToneIcons.js docs/data/material/components/icons/TwoToneIcons.tsx && echo LINT_OK; yarn -s tsc -p docs/tsconfig.json --noEmit 2>&1 | grep -ic twotone'
```

tool result:

```
diff --git a/docs/data/material/components/icons/TwoToneIcons.js b/docs/data/material/components/icons/TwoToneIcons.js
index 125785fdc2..f878f93533 100644
--- a/docs/data/material/components/icons/TwoToneIcons.js
+++ b/docs/data/material/components/icons/TwoToneIcons.js
@@ -1,6 +1,19 @@
 import * as React from 'react';
+import { loadCSS } from 'fg-loadcss';
 import Icon from '@mui/material/Icon';
 
 export default function TwoToneIcons() {
+  React.useEffect(() => {
+    const node = loadCSS(
+      'https://fonts.googleapis.com/icon?family=Material+Icons+Two+Tone',
+      // Inject before JSS
+      document.querySelector('#material-icon-font') || document.head.firstChild,
+    );
+
+    return () => {
+      node.parentNode.removeChild(node);
+    };
+  }, []);
+
   return <Icon baseClassName="material-icons-two-tone">add_circle</Icon>;
 }
 M docs/data/material/components/icons/TwoToneIcons.js
 M docs/data/material/components/icons/TwoToneIcons.tsx
 M package.json
 M yarn.lock
?? Dockerfile
?? custom-reporter.js
```

tool result:

```
Exit code 1
warning You don't appear to have an internet connection. Try the --offline flag to use the cache for registry queries.

/testbed/custom-reporter.js
   1:1   error  Unexpected var, use let or const instead                                       no-var
   2:1   error  Unexpected var, use let or const instead                                       no-var
   2:1   error  Expected 1 empty line after require statement not followed by another require  import/newline-after-import
   2:12  error  `path` import should occur before import of `mocha`                            import/order
   5:3   error  All 'var' declarations must be at the top of the function scope                vars-on-top
   5:3   error  Unexpected var, use let or const instead                                       no-var
   6:3   error  All 'var' declarations must be at the top of the function scope                vars-on-top
   6:3   error  Unexpected var, use let or const instead                                       no-var
   7:25  error  Unexpected unnamed function                                                    func-names
   7:25  error  Unexpected function expression                                                 prefer-arrow-callback
   8:5   error  Unexpected var, use let or const instead                                       no-var
   9:5   error  Unexpected var, use let or const instead                                       no-var
  10:5   error  Unexpected var, use let or const instead                                       no-var
  14:7   error  Expected property shorthand                                                    object-shorthand
  30:20  error  Unexpected unnamed function                                                    func-names
  30:20  error  Unexpected function expression                                                 prefer-arrow-callback
  31:5   error  Unexpected console statement                                                   no-console
  33:7   error  Expected property shorthand                                                    object-shorthand
  34:7   error  Expected property shorthand                                                    object-shorthand
  39:1   error  The '__proto__' property is deprecated                                         no-proto

✖ 20 problems (20 errors, 0 warnings)
  14 errors and 0 warnings potentially fixable with the `--fix` option.

0
```

**assistant:** `yarn eslint` runs the repo's own lint script, which lints the whole tree and stops on `custom-reporter.js`. I'll call eslint directly on just the two demo files.

**tool call: Bash**

```bash
/work/mui__material-ui-38247/bin/envrun 'node_modules/.bin/eslint docs/data/material/components/icons/TwoToneIcons.js docs/data/material/components/icons/TwoToneIcons.tsx && node_modules/.bin/prettier --check docs/data/material/components/icons/TwoToneIcons.js docs/data/material/components/icons/TwoToneIcons.tsx && echo LINT_OK'
```

tool result:

```
Checking formatting...
All matched files use Prettier code style!
LINT_OK
```

**assistant:** The two-tone `<Icon>` demo should now show the icon in CodeSandbox and StackBlitz instead of the clipped text "ad". I haven't opened a real sandbox to watch it render, since the container has no network.

**Cause:** the docs site loads both the Material Icons and Material Icons Two Tone fonts globally (`docs/pages/_app.js:116`). The page that sandboxes are built from (`docs/src/modules/sandbox/CreateReactApp.ts`) only loads the base Material Icons font. So in a sandbox, `baseClassName="material-icons-two-tone"` has no font behind it, and the literal text "add_circle" shows, cut off to "ad".

**Fix:** `TwoToneIcons.js` and `TwoToneIcons.tsx` in `docs/data/material/components/icons/` now load the Two Tone font themselves when the demo mounts and remove it when it unmounts. This is the same approach the Font Awesome demo on that page already uses. The sandbox generator sees the new import and adds `fg-loadcss` (the small CSS-loading library both demos use) to the sandbox's dependencies. I did this rather than adding the font to every sandbox page because the existing sandbox tests check that page's HTML exactly.

**Checks:**
- A temporary test built the sandbox from the updated demo: it includes the Two Tone font and lists `fg-loadcss` as a dependency. All 19 sandbox tests pass with it, and I've deleted it.
- eslint, prettier and the docs TypeScript check all pass on the two changed files.
- The script that regenerates the JS demos from the TS ones produced no changes to these files, so they're in sync. It did reformat about a dozen unrelated demos, probably because the container has different tool versions, and I reverted those.

The only changes are the two demo files. `package.json`, `yarn.lock`, `Dockerfile` and `custom-reporter.js` were already modified or present from the environment setup, and I left them as they were.

The issue also asks why the icon name is passed as a child rather than a typed `icon` prop. That's an API design question, and I didn't change anything for it.

_session end: success, turns 14, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 319.0 s: cat > /tmp/repro.test.js <<EOF const fs = require("fs"); const { expect } = require("chai"); const CodeSandbox = require("/testbed/docs/src/modules/sandbox/CodeSandbox").default; it("two tone sandbox", () => {   const r = CodeSandbox.createReactApp({ title: "t", githubLocation: "x", codeVariant: "JS", language: "en", raw: fs.readFileSync("/testbed/docs/data/material/components/icons/TwoToneIcons.js", "utf8") });   console.log(r.files["package.json"].content.dependencies);   expect(r.files["Demo.js"].content).to.include("Material+Icons+Two+Tone"); }); EOF cp /tmp/repro.test.js docs/src/modules/
- `rc=1` 138.77 s: yarn -s eslint docs/data/material/components/icons/TwoToneIcons.js docs/data/material/components/icons/TwoToneIcons.tsx && yarn -s prettier --check docs/data/material/components/icons/TwoToneIcons.js docs/data/material/components/icons/TwoToneIcons.tsx && echo LINT_OK; yarn -s tsc -p docs/tsconfig.json --noEmit 2>&1 | grep -ic twotone
- `rc=0` 3.9 s: node_modules/.bin/eslint docs/data/material/components/icons/TwoToneIcons.js docs/data/material/components/icons/TwoToneIcons.tsx && node_modules/.bin/prettier --check docs/data/material/components/icons/TwoToneIcons.js docs/data/material/components/icons/TwoToneIcons.tsx && echo LINT_OK
