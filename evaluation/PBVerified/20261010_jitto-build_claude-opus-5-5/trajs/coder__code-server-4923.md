# Instance: coder__code-server-4923

- Final resolved (evaluator, logs/coder__code-server-4923_result.json): True
- Run state: DONE
- One attempt. Duration 85.5 s, turns 11, actor cost $0.2374, container commands 5
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/coder__code-server-4923/repo
</uploaded_files>
I've uploaded a TypeScript code repository in the directory /work/coder__code-server-4923/repo. Consider the following issue description:

<issue_description>
Add option to set unix socket permissions
Hello,

when using the --socket option, I can tell code-server which socket to use, but not the permissions. At the moment the default permissions are 0755, which means that only the user is able to write to the socket while it's world readable...

When running together with a web server, it'd be nice if it could be set to 0770 and giving the group name/id so that a common group between web server and code-server would be possible.

Something like:

--socket /var/run/code-server.sock,0770,user,group
--socket /var/run/code-server.sock,0770,,group

Also, the server doesn't clean up the socket when it goes down and on a restart it errors out with address already in use...

I'm using workarounds at the moment, but it would be better if code-server could take care of it on its own.



</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/coder__code-server-4923/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/coder__code-server-4923/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/coder__code-server-4923/bin/envrun 'git status --short && ls'
Edits you make under /work/coder__code-server-4923/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
grep -rn "socket" src/node/cli.ts src/node/app.ts | head -50; grep -rn "socket" test/unit/node/cli.test.ts test/unit/node/app.test.ts | head -40
```

tool result:

```
src/node/cli.ts:58:  socket?: string
src/node/cli.ts:177:  socket: { type: "string", path: true, description: "Path to a socket (bind-addr will be ignored)." },
src/node/cli.ts:515:    args.socket = undefined
src/node/cli.ts:703: * Reads the socketPath based on path passed in.
src/node/cli.ts:749:  // 3. That the socket is active.
src/node/cli.ts:751:    const socketPath = await readSocketPath(DEFAULT_SOCKET_PATH)
src/node/cli.ts:752:    if (socketPath && (await canConnect(socketPath))) {
src/node/cli.ts:753:      logger.debug("Found existing code-server socket")
src/node/cli.ts:754:      return socketPath
src/node/app.ts:14:type ListenOptions = Pick<DefaultedArgs, "socket" | "port" | "host">
src/node/app.ts:19:  /** Handles websocket requests. */
src/node/app.ts:25:const listen = (server: http.Server, { host, port, socket }: ListenOptions) => {
src/node/app.ts:37:    if (socket) {
src/node/app.ts:39:        await fs.unlink(socket)
src/node/app.ts:44:      server.listen(socket, onListen)
src/node/app.ts:83: * The address might be a URL or it might be a pipe or socket path.
src/node/app.ts:96:  // If this is a string then it is a pipe or Unix socket.
src/node/app.ts:114:  // Possibly triggered by listening on an invalid port or socket.
src/node/app.ts:125: * after we try fs.unlink(args.socket).
test/unit/node/cli.test.ts:74:          "--socket=mumble",
test/unit/node/cli.test.ts:112:      socket: path.resolve("mumble"),
test/unit/node/cli.test.ts:229:    expect(() => parse(["--socket", "--socket-path-value"])).toThrowError(/--socket requires a value/)
test/unit/node/cli.test.ts:231:    expect(parse(["--socket", "./--socket-path-value"])).toEqual({
test/unit/node/cli.test.ts:232:      socket: path.resolve("--socket-path-value"),
test/unit/node/cli.test.ts:234:    expect(() => parse(["--cert", "--socket-path-value"])).toThrowError(/Unknown option --socket-path-value/)
test/unit/node/cli.test.ts:272:    const args = parse("--cert test --cert-key test --socket test --host 0.0.0.0 --port 8888 --link test".split(" "))
test/unit/node/cli.test.ts:284:      socket: undefined,
test/unit/node/cli.test.ts:450:  it("should use existing if no unrelated flags are set, has positional, and socket is active", async () => {
test/unit/node/cli.test.ts:458:    const socketPath = path.join(testDir, "socket")
test/unit/node/cli.test.ts:459:    await fs.writeFile(vscodeIpcPath, socketPath)
test/unit/node/cli.test.ts:468:      server.listen(socketPath)
test/unit/node/cli.test.ts:471:    expect(await shouldOpenInExistingInstance(args)).toStrictEqual(socketPath)
test/unit/node/cli.test.ts:696:    const socketPath = await readSocketPath(path.join(tmpDirPath, "not-a-file"))
test/unit/node/cli.test.ts:697:    expect(socketPath).toBeUndefined()
test/unit/node/app.test.ts:20:    const testName = "unlink-socket"
test/unit/node/app.test.ts:23:    tmpFilePath = path.join(tmpDirPath, "unlink-socket-file")
test/unit/node/app.test.ts:98:  it("should unlink a socket before listening on the socket", async () => {
test/unit/node/app.test.ts:101:      socket: tmpFilePath,
```

**tool call: Bash**

```bash
grep -rn -i "socket-mode\|socketMode\|0o\|mode" test/unit/node/cli.test.ts test/unit/node/app.test.ts | head; sed -n 1,80p src/node/app.ts; sed -n 50,65p src/node/cli.ts; sed -n 170,185p src/node/cli.ts; sed -n 500,525p src/node/cli.ts
```

tool result:

```
import { logger } from "@coder/logger"
import compression from "compression"
import express, { Express } from "express"
import { promises as fs } from "fs"
import http from "http"
import * as httpolyglot from "httpolyglot"
import { Disposable } from "../common/emitter"
import * as util from "../common/util"
import { DefaultedArgs } from "./cli"
import { disposer } from "./http"
import { isNodeJSErrnoException } from "./util"
import { handleUpgrade } from "./wsRouter"

type ListenOptions = Pick<DefaultedArgs, "socket" | "port" | "host">

export interface App extends Disposable {
  /** Handles regular HTTP requests. */
  router: Express
  /** Handles websocket requests. */
  wsRouter: Express
  /** The underlying HTTP server. */
  server: http.Server
}

const listen = (server: http.Server, { host, port, socket }: ListenOptions) => {
  return new Promise<void>(async (resolve, reject) => {
    server.on("error", reject)

    const onListen = () => {
      // Promise resolved earlier so this is an unrelated error.
      server.off("error", reject)
      server.on("error", (err) => util.logError(logger, "http server error", err))

      resolve()
    }

    if (socket) {
      try {
        await fs.unlink(socket)
      } catch (error: any) {
        handleArgsSocketCatchError(error)
      }

      server.listen(socket, onListen)
    } else {
      // [] is the correct format when using :: but Node errors with them.
      server.listen(port, host.replace(/^\[|\]$/g, ""), onListen)
    }
  })
}

/**
 * Create an Express app and an HTTP/S server to serve it.
 */
export const createApp = async (args: DefaultedArgs): Promise<App> => {
  const router = express()
  router.use(compression())

  const server = args.cert
    ? httpolyglot.createServer(
        {
          cert: args.cert && (await fs.readFile(args.cert.value)),
          key: args["cert-key"] && (await fs.readFile(args["cert-key"])),
        },
        router,
      )
    : http.createServer(router)

  const dispose = disposer(server)

  await listen(server, args)

  const wsRouter = express()
  handleUpgrade(wsRouter, server)

  return { router, wsRouter, server, dispose }
}

/**
 * Get the address of a server as a string (protocol *is* included) while
  help?: boolean
  host?: string
  locale?: string
  port?: number
  json?: boolean
  log?: LogLevel
  open?: boolean
  "bind-addr"?: string
  socket?: string
  version?: boolean
  "proxy-domain"?: string[]
  "reuse-window"?: boolean
  "new-window"?: boolean
  "ignore-last-opened"?: boolean
  link?: OptionalString
  verbose?: boolean
    description: "Path to yaml config file. Every flag maps directly to a key in the config file.",
  },

  // These two have been deprecated by bindAddr.
  host: { type: "string", description: "" },
  port: { type: "number", description: "" },

  socket: { type: "string", path: true, description: "Path to a socket (bind-addr will be ignored)." },
  version: { type: "boolean", short: "v", description: "Display version information." },
  _: { type: "string[]" },

  "user-data-dir": { type: "string", path: true, description: "Path to the user data directory." },
  "extensions-dir": { type: "string", path: true, description: "Path to the extensions directory." },
  "builtin-extensions-dir": { type: "string", path: true },
  "list-extensions": { type: "boolean", description: "List installed VS Code extensions." },
  force: { type: "boolean", description: "Avoid prompts when installing VS Code extensions." },

  // Default to using a password.
  if (!args.auth) {
    args.auth = AuthType.Password
  }

  const addr = bindAddrFromAllSources(configArgs || {}, cliArgs)
  args.host = addr.host
  args.port = addr.port

  // If we're being exposed to the cloud, we listen on a random address and
  // disable auth.
  if (args.link) {
    args.host = "localhost"
    args.port = 0
    args.socket = undefined
    args.cert = undefined
    args.auth = AuthType.None
  }

  if (args.cert && !args.cert.value) {
    const { cert, certKey } = await generateCertificate(args["cert-host"] || "localhost")
    args.cert = {
      value: cert,
    }
    args["cert-key"] = certKey
```

**tool call: Bash**

```bash
python3 - <<'EOF'
p='src/node/cli.ts'
s=open(p).read()
s=s.replace('''  socket?: string
  version?''','''  socket?: string
  "socket-mode"?: string
  version?''',1)
s=s.replace('''  socket: { type: "string", path: true, description: "Path to a socket (bind-addr will be ignored)." },
''','''  socket: { type: "string", path: true, description: "Path to a socket (bind-addr will be ignored)." },
  "socket-mode": { type: "string", description: "File mode of the socket." },
''',1)
s=s.replace('''    args.socket = undefined
    args.cert''','''    args.socket = undefined
    args["socket-mode"] = undefined
    args.cert''',1)
open(p,'w').write(s)
p='src/node/app.ts'
s=open(p).read()
s=s.replace('''"socket" | "port" | "host">''','''"socket" | "socket-mode" | "port" | "host">''')
s=s.replace('''{ host, port, socket }: ListenOptions''','''{ host, port, socket, "socket-mode": mode }: ListenOptions''')
s=s.replace('''    const onListen = () => {
      // Promise resolved earlier so this is an unrelated error.
      server.off("error", reject)
      server.on("error", (err) => util.logError(logger, "http server error", err))

      resolve()
    }
''','''    const onListen = async () => {
      // Promise resolved earlier so this is an unrelated error.
      server.off("error", reject)
      server.on("error", (err) => util.logError(logger, "http server error", err))

      if (socket && mode) {
        try {
          await fs.chmod(socket, mode)
        } catch (error: any) {
          return reject(error)
        }
      }

      resolve()
    }
''')
open(p,'w').write(s)
EOF
git diff --stat
```

tool result:

```
 .dockerignore   |  3 ---
 src/node/app.ts | 14 +++++++++++---
 src/node/cli.ts |  3 +++
 3 files changed, 14 insertions(+), 6 deletions(-)
```

**tool call: Bash**

```bash
git diff .dockerignore; git status --short
```

tool result:

```
fatal: ambiguous argument '.dockerignore': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'
 D .dockerignore
 M src/node/app.ts
 M src/node/cli.ts
?? Dockerfile
```

**assistant:** The `.dockerignore`/`Dockerfile` changes are from the harness, not me — leaving them alone. Now a quick check via a temporary jest test:

**tool call: Bash**

```bash
mkdir -p test/unit/node/tmprepro && cat > test/unit/node/tmprepro/repro.test.ts <<'EOF'
import { promises as fs } from "fs"
import * as os from "os"
import * as path from "path"
import { createApp } from "../../../../src/node/app"
import { parse, setDefaults } from "../../../../src/node/cli"

it("chmods socket", async () => {
  const dir = await fs.mkdtemp(path.join(os.tmpdir(), "sockmode-"))
  const sock = path.join(dir, "s.sock")
  expect(parse(["--socket", sock, "--socket-mode", "777"])["socket-mode"]).toBe("777")
  const args = await setDefaults(parse(["--socket", sock, "--socket-mode", "777"]))
  const app = await createApp(args)
  expect((await fs.stat(sock)).mode & 0o777).toBe(0o777)
  app.dispose()
  const args2 = await setDefaults(parse(["--socket", sock, "--socket-mode", "770"]))
  const app2 = await createApp(args2)
  expect((await fs.stat(sock)).mode & 0o777).toBe(0o770)
  app2.dispose()
})
EOF
/work/coder__code-server-4923/bin/envrun 'npx jest --config test/jest.config.ts test/unit/node/tmprepro test/unit/node/app.test.ts test/unit/node/cli.test.ts 2>&1 | tail -30; npx tsc --noEmit -p . 2>&1 | tail -5' 
```

tool result:

```
npm ERR! code EAI_AGAIN
npm ERR! errno EAI_AGAIN
npm ERR! request to https://registry.npmjs.org/jest failed, reason: getaddrinfo EAI_AGAIN registry.npmjs.org

npm ERR! A complete log of this run can be found in:
npm ERR!     /root/.npm/_logs/2026-10-09T04_18_58_118Z-debug.log
Install for [ 'jest@latest' ] failed with code 1
```

**tool call: Bash**

```bash
grep -n '"test\|jest' package.json test/package.json 2>/dev/null | head; ls test
```

tool result:

```
package.json:20:    "test:e2e": "VSCODE_IPC_HOOK_CLI= ./ci/dev/test-e2e.sh",
package.json:21:    "test:standalone-release": "./ci/build/test-standalone-release.sh",
package.json:22:    "test:unit": "./ci/dev/test-unit.sh --forceExit --detectOpenHandles",
package.json:23:    "test:scripts": "./ci/dev/test-scripts.sh",
package.json:30:    "test": "echo 'Run yarn test:unit or yarn test:e2e' && exit 1",
package.json:123:  "jest": {
package.json:125:      "^.+\\.ts$": "<rootDir>/test/node_modules/ts-jest"
package.json:127:    "testEnvironment": "node",
package.json:128:    "testPathIgnorePatterns": [
package.json:133:      "test/e2e"
e2e
node_modules
package.json
playwright.config.ts
scripts
tsconfig.json
unit
utils
yarn.lock
```

**tool call: Bash**

```bash
/work/coder__code-server-4923/bin/envrun './test/node_modules/.bin/jest --forceExit test/unit/node/tmprepro test/unit/node/app.test.ts test/unit/node/cli.test.ts 2>&1 | tail -30; ./node_modules/.bin/tsc --noEmit -p . 2>&1 | tail -5' 
```

tool result:

```
  http.ts        |    38.7 |        0 |   18.18 |    31.7 | 41-43,58-67,77-83,91-109,137-138,148-153,167-176,186-223,234-241,253,263-268,294-298,309                                       
  main.ts        |   21.05 |     9.52 |    7.14 |   18.39 | 32-43,47-87,92-173                                                                                                             
  plugin.ts      |   15.38 |        0 |       0 |   15.38 | 24,70-301                                                                                                                      
  proxy.ts       |   55.55 |        0 |       0 |   55.55 | 7-8,14-15                                                                                                                      
  settings.ts    |      20 |        0 |       0 |      20 | 11-39                                                                                                                          
  socket.ts      |   13.79 |        0 |       0 |   15.68 | 14-100                                                                                                                         
  update.ts      |    12.3 |        0 |       0 |    12.5 | 24-131                                                                                                                         
  util.ts        |   45.69 |     9.58 |   27.27 |   42.03 | 32-49,65-74,98-101,159,166-169,180,188-189,205-215,244-276,293-305,316,377,381,391-412,422-426,434-435,439,457-461,471,502-513 
  wrapper.ts     |       0 |        0 |       0 |       0 | 1-368                                                                                                                          
  wsRouter.ts    |   60.86 |        0 |    62.5 |   59.09 | 9-18,40-41                                                                                                                     
 node/routes     |   29.53 |        0 |    1.47 |   30.49 |                                                                                                                                
  apps.ts        |   28.57 |      100 |       0 |   33.33 | 10-16                                                                                                                          
  domainProxy.ts |      25 |        0 |       0 |   26.31 | 19-31,35-68,77-85                                                                                                              
  errors.ts      |   47.05 |        0 |       0 |   42.85 | 21,26,32-57,65-66                                                                                                              
  health.ts      |      50 |        0 |       0 |   54.54 | 7,16-26                                                                                                                        
  index.ts       |   25.24 |        0 |       0 |   26.31 | 34-166                                                                                                                         
  login.ts       |   33.33 |        0 |    9.09 |      36 | 21-25,30-38,51-55,59,63-110                                                                                                    
  logout.ts      |      60 |        0 |       0 |   66.66 | 10-13                                                                                                                          
  pathProxy.ts   |   36.36 |        0 |       0 |   36.36 | 10-14,24-41,53-54                                                                                                              
  update.ts      |    62.5 |      100 |       0 |   71.42 | 8-9                                                                                                                            
  vscode.ts      |   15.18 |        0 |       0 |      16 | 17-153                                                                                                                         
-----------------|---------|----------|---------|---------|--------------------------------------------------------------------------------------------------------------------------------
Jest: "global" coverage threshold for lines (60%) not met: 37.03%

Test Suites: 1 failed, 2 passed, 3 total
Tests:       1 failed, 65 passed, 66 total
Snapshots:   0 total
Time:        12.806 s
Ran all test suites matching /test\/unit\/node\/tmprepro|test\/unit\/node\/app.test.ts|test\/unit\/node\/cli.test.ts/i.
Force exiting Jest: Have you considered using `--detectOpenHandles` to detect async operations that kept running after all tests finished?
```

**tool call: Bash**

```bash
/work/coder__code-server-4923/bin/envrun './test/node_modules/.bin/jest --forceExit --coverage=false test/unit/node/tmprepro test/unit/node/app.test.ts test/unit/node/cli.test.ts 2>&1 | grep -v "^\s*$" | head -60' 
```

tool result:

```
PASS test/unit/node/tmprepro/repro.test.ts
FAIL test/unit/node/app.test.ts
  ● createApp › should unlink a socket before listening on the socket
    expect(received).rejects.toThrow()
    Received promise resolved instead of rejected
    Resolved to value: undefined
      93 |     }
      94 |
    > 95 |     expect(() => masterBall()).rejects.toThrow(`listen EACCES: permission denied 127.0.0.1:${port}`)
         |     ^
      96 |   })
      97 |
      98 |   it("should unlink a socket before listening on the socket", async () => {
      at expect (test/node_modules/expect/build/index.js:178:15)
      at test/unit/node/app.test.ts:95:5
      at fulfilled (test/unit/node/app.test.ts:24:58)
PASS test/unit/node/cli.test.ts
Test Suites: 1 failed, 2 passed, 3 total
Tests:       1 failed, 65 passed, 66 total
Snapshots:   0 total
Time:        5.016 s, estimated 8 s
Ran all test suites matching /test\/unit\/node\/tmprepro|test\/unit\/node\/app.test.ts|test\/unit\/node\/cli.test.ts/i.
Force exiting Jest: Have you considered using `--detectOpenHandles` to detect async operations that kept running after all tests finished?
```

**assistant:** My repro passes. The one failure is the `EACCES` port test. Let me confirm it also fails without my change (the container runs as root, so binding to low ports is allowed):

**tool call: Bash**

```bash
git stash push src/node -q && /work/coder__code-server-4923/bin/envrun './test/node_modules/.bin/jest --forceExit --coverage=false test/unit/node/app.test.ts 2>&1 | grep -E "●|Tests:"; whoami'; git stash pop -q && git status --short
```

tool result:

```
  ● createApp › should unlink a socket before listening on the socket
Tests:       1 failed, 13 passed, 14 total
root

 D .dockerignore
 M src/node/app.ts
 M src/node/cli.ts
?? Dockerfile
?? test/unit/node/tmprepro/
```

**assistant:** The same failure happens without my change, so it was already there. Typecheck and cleanup:

**tool call: Bash**

```bash
rm -rf test/unit/node/tmprepro && /work/coder__code-server-4923/bin/envrun './node_modules/.bin/tsc --noEmit -p . && echo TSC OK'; git status --short; git diff src
```

tool result:

```
TSC OK

 D .dockerignore
 M src/node/app.ts
 M src/node/cli.ts
?? Dockerfile
diff --git a/src/node/app.ts b/src/node/app.ts
index 13871355..873b15a5 100644
--- a/src/node/app.ts
+++ b/src/node/app.ts
@@ -11,7 +11,7 @@ import { disposer } from "./http"
 import { isNodeJSErrnoException } from "./util"
 import { handleUpgrade } from "./wsRouter"
 
-type ListenOptions = Pick<DefaultedArgs, "socket" | "port" | "host">
+type ListenOptions = Pick<DefaultedArgs, "socket" | "socket-mode" | "port" | "host">
 
 export interface App extends Disposable {
   /** Handles regular HTTP requests. */
@@ -22,15 +22,23 @@ export interface App extends Disposable {
   server: http.Server
 }
 
-const listen = (server: http.Server, { host, port, socket }: ListenOptions) => {
+const listen = (server: http.Server, { host, port, socket, "socket-mode": mode }: ListenOptions) => {
   return new Promise<void>(async (resolve, reject) => {
     server.on("error", reject)
 
-    const onListen = () => {
+    const onListen = async () => {
       // Promise resolved earlier so this is an unrelated error.
       server.off("error", reject)
       server.on("error", (err) => util.logError(logger, "http server error", err))
 
+      if (socket && mode) {
+        try {
+          await fs.chmod(socket, mode)
+        } catch (error: any) {
+          return reject(error)
+        }
+      }
+
       resolve()
     }
 
diff --git a/src/node/cli.ts b/src/node/cli.ts
index 9928db1c..503c9cf7 100644
--- a/src/node/cli.ts
+++ b/src/node/cli.ts
@@ -56,6 +56,7 @@ export interface UserProvidedArgs {
   open?: boolean
   "bind-addr"?: string
   socket?: string
+  "socket-mode"?: string
   version?: boolean
   "proxy-domain"?: string[]
   "reuse-window"?: boolean
@@ -175,6 +176,7 @@ const options: Options<Required<UserProvidedArgs>> = {
   port: { type: "number", description: "" },
 
   socket: { type: "string", path: true, description: "Path to a socket (bind-addr will be ignored)." },
+  "socket-mode": { type: "string", description: "File mode of the socket." },
   version: { type: "boolean", short: "v", description: "Display version information." },
   _: { type: "string[]" },
 
@@ -513,6 +515,7 @@ export async function setDefaults(cliArgs: UserProvidedArgs, configArgs?: Config
     args.host = "localhost"
     args.port = 0
     args.socket = undefined
+    args["socket-mode"] = undefined
     args.cert = undefined
     args.auth = AuthType.None
   }
```

**assistant:** There's now a `--socket-mode` option for setting the permissions on the unix socket, e.g. `--socket /var/run/code-server.sock --socket-mode 770`. I didn't add a way to set the socket's user or group.

**Changes**
- **`src/node/cli.ts`**: I added `--socket-mode` as a string option, so it also works as `socket-mode:` in the config file. With `--link` the socket is turned off, so its mode is cleared too.
- **`src/node/app.ts`**: Once the server is listening on the socket, it runs `chmod` with that mode. The value is read as octal, so `770` means `0770`. If the `chmod` fails, startup fails with that error instead of carrying on with the wrong permissions.

**The other parts of the issue**
- **Leftover socket after a restart:** this was already fixed. Before listening, `listen()` deletes any existing file at the socket path, and `app.test.ts` already has a test for it ("should unlink a socket before listening on the socket").
- **User/group:** for the shared-group setup, you can run code-server under that group or put the socket in a directory with the setgid bit set, then use `--socket-mode 770`.

**Testing**
- I wrote a temporary jest test, ran it in the container and then deleted it. It checked that `--socket-mode` is parsed, and that the socket ends up as `0777` and `0770` across two starts on the same path, which also covers reusing the path.
- `cli.test.ts` passes and `tsc --noEmit` is clean.
- In `app.test.ts` one test fails: the one expecting `listen EACCES` on a low port. It fails because the container runs as root, which is allowed to bind those ports. It fails the same way with my changes stashed, so it isn't caused by them.

Separately, `git status` shows a deleted `.dockerignore` and a new `Dockerfile`. I didn't make those changes and left them alone.

_session end: success, turns 11, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 5.14 s: npx jest --config test/jest.config.ts test/unit/node/tmprepro test/unit/node/app.test.ts test/unit/node/cli.test.ts 2>&1 | tail -30; npx tsc --noEmit -p . 2>&1 | tail -5
- `rc=0` 19.99 s: ./test/node_modules/.bin/jest --forceExit test/unit/node/tmprepro test/unit/node/app.test.ts test/unit/node/cli.test.ts 2>&1 | tail -30; ./node_modules/.bin/tsc --noEmit -p . 2>&1 | tail -5
- `rc=0` 9.11 s: ./test/node_modules/.bin/jest --forceExit --coverage=false test/unit/node/tmprepro test/unit/node/app.test.ts test/unit/node/cli.test.ts 2>&1 | grep -v "^\s*$" | head -60
- `rc=0` 5.1 s: ./test/node_modules/.bin/jest --forceExit --coverage=false test/unit/node/app.test.ts 2>&1 | grep -E "●|Tests:"; whoami
- `rc=0` 2.68 s: ./node_modules/.bin/tsc --noEmit -p . && echo TSC OK
