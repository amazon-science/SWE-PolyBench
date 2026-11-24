# Instance: yt-dlp__yt-dlp-9862

- Final resolved (evaluator, logs/yt-dlp__yt-dlp-9862_result.json): True
- Run state: DONE
- One attempt. Duration 48.2 s, turns 9, actor cost $0.2254398, container commands 4
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/yt-dlp__yt-dlp-9862/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/yt-dlp__yt-dlp-9862/repo. Consider the following issue description:

<issue_description>
`--simulate` doesn't accurately simulate downloading under certain conditions
### DO NOT REMOVE OR SKIP THE ISSUE TEMPLATE

- [X] I understand that I will be **blocked** if I *intentionally* remove or skip any mandatory\* field

### Checklist

- [X] I'm reporting a bug unrelated to a specific site
- [X] I've verified that I have **updated yt-dlp to nightly or master** ([update instructions](https://github.com/yt-dlp/yt-dlp#update-channels))
- [X] I've checked that all provided URLs are playable in a browser with the same IP and same login details
- [X] I've checked that all URLs and arguments with special characters are [properly quoted or escaped](https://github.com/yt-dlp/yt-dlp/wiki/FAQ#video-url-contains-an-ampersand--and-im-getting-some-strange-output-1-2839-or-v-is-not-recognized-as-an-internal-or-external-command)
- [X] I've searched [known issues](https://github.com/yt-dlp/yt-dlp/issues/3766) and the [bugtracker](https://github.com/yt-dlp/yt-dlp/issues?q=) for similar issues **including closed ones**. DO NOT post duplicates
- [X] I've read the [guidelines for opening an issue](https://github.com/yt-dlp/yt-dlp/blob/master/CONTRIBUTING.md#opening-an-issue)

### Provide a description that is worded well enough to be understood

When running a yt-dlp command with `--simulate` (and without an `-f` arg), the default format selection differs from an unsimulated run under any of these conditions:
- ffmpeg is not available
- the outtmpl is `-`
- the URL is for a livestream (and `--live-from-start` was not passed)

A dry-run/simulate option should actually simulate the behaviour that will occur when downloading.
This behaviour is currently undocumented. Either the behaviour should be changed or at the very least be documented.

---

*Copying initial discussion: https://github.com/yt-dlp/yt-dlp/pull/9805#discussion_r1588171627*

It looks like we can trace this logic back to https://github.com/ytdl-org/youtube-dl/commit/0017d9ad6de831384e74db14a821e4c94020c9ac

Back then, upstream's default format spec was only `best` if ffmpeg was not available. So a simulated run would result in a "requested formats not available" error if ffmpeg was not available and there was no combined video+audio format available. This `simulate` check seems to be added so that you could print json without having to manually pass `-f bv+ba` or `-f bv` etc in this scenario -- see the linked upstream PR



### Provide verbose output that clearly demonstrates the problem

- [X] Run **your** yt-dlp command with **-vU** flag added (`yt-dlp -vU <your command line>`)
- [ ] If using API, add `'verbose': True` to `YoutubeDL` params instead
- [X] Copy the WHOLE output (starting with `[debug] Command-line config`) and insert it below

### Complete Verbose Output

```shell
[debug] Command-line config: ['-vU', '--simulate', 'https://www.youtube.com/watch?v=2yJgwwDcgV8']
[debug] Encodings: locale cp1252, fs utf-8, pref cp1252, out utf-8, error utf-8, screen utf-8
[debug] yt-dlp version master@2024.04.28.221944 from yt-dlp/yt-dlp-master-builds [ac817bc83] (win_exe)
[debug] Python 3.8.10 (CPython AMD64 64bit) - Windows-10-10.0.22631-SP0 (OpenSSL 1.1.1k  25 Mar 2021)
[debug] exe versions: none
[debug] Optional libraries: Cryptodome-3.20.0, brotli-1.1.0, certifi-2024.02.02, curl_cffi-0.5.10, mutagen-1.47.0, requests-2.31.0, sqlite3-3.35.5, urllib3-2.2.1, websockets-12.0
[debug] Proxy map: {}
[debug] Request Handlers: urllib, requests, websockets, curl_cffi
[debug] Loaded 1810 extractors
[debug] Fetching release info: https://api.github.com/repos/yt-dlp/yt-dlp-master-builds/releases/latest
Latest version: master@2024.04.28.221944 from yt-dlp/yt-dlp-master-builds
yt-dlp is up to date (master@2024.04.28.221944 from yt-dlp/yt-dlp-master-builds)
[youtube] Extracting URL: https://www.youtube.com/watch?v=2yJgwwDcgV8
[youtube] 2yJgwwDcgV8: Downloading webpage
[youtube] 2yJgwwDcgV8: Downloading ios player API JSON
[youtube] 2yJgwwDcgV8: Downloading android player API JSON
WARNING: [youtube] Skipping player responses from android clients (got player responses for video "aQvGIIdgFDM" instead of "2yJgwwDcgV8")
[debug] Loading youtube-nsig.7d1f7724 from cache
[debug] [youtube] Decrypted nsig ZyUwo2vdMccktm7tN0 => ZvGvrjLHlKzcbw
[debug] Loading youtube-nsig.7d1f7724 from cache
[debug] [youtube] Decrypted nsig vYdxycJ0vBBgWEBA_9 => Etq9qDUH370hPg
[youtube] 2yJgwwDcgV8: Downloading m3u8 information
[debug] Sort order given by extractor: quality, res, fps, hdr:12, source, vcodec:vp9.2, channels, acodec, lang, proto
[debug] Formats sorted by: hasvid, ie_pref, quality, res, fps, hdr:12(7), source, vcodec:vp9.2(10), channels, acodec, lang, proto, size, br, asr, vext, aext, hasaud, id
[debug] Default format spec: bestvideo*+bestaudio/best
[info] 2yJgwwDcgV8: Downloading 1 format(s): 244+251
```


</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/yt-dlp__yt-dlp-9862/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/yt-dlp__yt-dlp-9862/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/yt-dlp__yt-dlp-9862/bin/envrun 'git status --short && ls'
Edits you make under /work/yt-dlp__yt-dlp-9862/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
grep -n "_default_format_spec" -r yt_dlp test | head; grep -n "def _default_format_spec" -A25 yt_dlp/YoutubeDL.py
```

tool result:

```
yt_dlp/YoutubeDL.py:2193:    def _default_format_spec(self, info_dict, download=True):
yt_dlp/YoutubeDL.py:2962:                req_format = self._default_format_spec(info_dict, download=download)
test/test_YoutubeDL.py:523:    def test_default_format_spec(self):
test/test_YoutubeDL.py:525:        self.assertEqual(ydl._default_format_spec({}), 'bestvideo*+bestaudio/best')
test/test_YoutubeDL.py:528:        self.assertEqual(ydl._default_format_spec({'is_live': True}), 'best/bestvideo+bestaudio')
test/test_YoutubeDL.py:531:        self.assertEqual(ydl._default_format_spec({'is_live': True}), 'bestvideo*+bestaudio/best')
test/test_YoutubeDL.py:534:        self.assertEqual(ydl._default_format_spec({}), 'best/bestvideo+bestaudio')
test/test_YoutubeDL.py:537:        self.assertEqual(ydl._default_format_spec({}, download=False), 'bestvideo*+bestaudio/best')
test/test_YoutubeDL.py:538:        self.assertEqual(ydl._default_format_spec({'is_live': True}), 'best/bestvideo+bestaudio')
2193:    def _default_format_spec(self, info_dict, download=True):
2194-        download = download and not self.params.get('simulate')
2195-        prefer_best = download and (
2196-            self.params['outtmpl']['default'] == '-'
2197-            or info_dict.get('is_live') and not self.params.get('live_from_start'))
2198-
2199-        def can_merge():
2200-            merger = FFmpegMergerPP(self)
2201-            return merger.available and merger.can_merge()
2202-
2203-        if not prefer_best and download and not can_merge():
2204-            prefer_best = True
2205-            formats = self._get_formats(info_dict)
2206-            evaluate_formats = lambda spec: self._select_formats(formats, self.build_format_selector(spec))
2207-            if evaluate_formats('b/bv+ba') != evaluate_formats('bv*+ba/b'):
2208-                self.report_warning('ffmpeg not found. The downloaded format may not be the best available. '
2209-                                    'Installing ffmpeg is strongly recommended: https://github.com/yt-dlp/yt-dlp#dependencies')
2210-
2211-        compat = (self.params.get('allow_multiple_audio_streams')
2212-                  or 'format-spec' in self.params['compat_opts'])
2213-
2214-        return ('best/bestvideo+bestaudio' if prefer_best
2215-                else 'bestvideo+bestaudio/best' if compat
2216-                else 'bestvideo*+bestaudio/best')
2217-
2218-    def build_format_selector(self, format_spec):
```

**tool call: Bash**

```bash
sed -n 515,545p test/test_YoutubeDL.py; sed -n 2950,2970p yt_dlp/YoutubeDL.py; git log --oneline -1
```

tool result:

```
        downloaded_ids = [info['format_id'] for info in ydl.downloaded_info_dicts]
        self.assertEqual(downloaded_ids, ['D', 'C', 'B'])

        ydl = YDL({'format': 'best[height<40]'})
        with contextlib.suppress(ExtractorError):
            ydl.process_ie_result(info_dict)
        self.assertEqual(ydl.downloaded_info_dicts, [])

    def test_default_format_spec(self):
        ydl = YDL({'simulate': True})
        self.assertEqual(ydl._default_format_spec({}), 'bestvideo*+bestaudio/best')

        ydl = YDL({})
        self.assertEqual(ydl._default_format_spec({'is_live': True}), 'best/bestvideo+bestaudio')

        ydl = YDL({'simulate': True})
        self.assertEqual(ydl._default_format_spec({'is_live': True}), 'bestvideo*+bestaudio/best')

        ydl = YDL({'outtmpl': '-'})
        self.assertEqual(ydl._default_format_spec({}), 'best/bestvideo+bestaudio')

        ydl = YDL({})
        self.assertEqual(ydl._default_format_spec({}, download=False), 'bestvideo*+bestaudio/best')
        self.assertEqual(ydl._default_format_spec({'is_live': True}), 'best/bestvideo+bestaudio')


class TestYoutubeDL(unittest.TestCase):
    def test_subtitles(self):
        def s_formats(lang, autocaption=False):
            return [{
                'ext': ext,
        while True:
            if interactive_format_selection:
                req_format = input(self._format_screen('\nEnter format selector ', self.Styles.EMPHASIS)
                                   + '(Press ENTER for default, or Ctrl+C to quit)'
                                   + self._format_screen(': ', self.Styles.EMPHASIS))
                try:
                    format_selector = self.build_format_selector(req_format) if req_format else None
                except SyntaxError as err:
                    self.report_error(err, tb=False, is_error=False)
                    continue

            if format_selector is None:
                req_format = self._default_format_spec(info_dict, download=download)
                self.write_debug(f'Default format spec: {req_format}')
                format_selector = self.build_format_selector(req_format)

            formats_to_download = self._select_formats(formats, format_selector)
            if interactive_format_selection and not formats_to_download:
                self.report_error('Requested format is not available', tb=False, is_error=False)
                continue
            break
39bc699d2 Release 2024.07.07
```

**tool call: Bash**

```bash
grep -n "can_merge\|FFmpeg" test/test_YoutubeDL.py | head; grep -n "_default_format_spec\|download=download" -r yt_dlp | head; grep -n -i "simulat" README.md | head -30
```

tool result:

```
yt_dlp/YoutubeDL.py:1837:            ie_result = self.process_video_result(ie_result, download=download)
yt_dlp/YoutubeDL.py:1891:                new_result, download=download, extra_info=extra_info)
yt_dlp/YoutubeDL.py:2087:            entry, download=download, extra_info=extra_info)
yt_dlp/YoutubeDL.py:2193:    def _default_format_spec(self, info_dict, download=True):
yt_dlp/YoutubeDL.py:2962:                req_format = self._default_format_spec(info_dict, download=download)
40:    * [Verbosity and Simulation Options](#verbosity-and-simulation-options)
364:    --mark-watched                  Mark videos watched (even with --simulate)
695:                                    Simulate unless --no-simulate is used
706:## Verbosity and Simulation Options:
711:    -s, --simulate                  Do not download the video and do not write
713:    --no-simulate                   Download the video even if printing/listing
728:                                    Implies --quiet. Implies --simulate unless
729:                                    --no-simulate or later stages of WHEN are
738:                                    video. Simulate unless --no-simulate is
742:                                    url or infojson passed. Simulate unless
743:                                    --no-simulate is used. If the URL refers to
748:                                    another simulation option is used (Alias:
829:                                    Simulate unless --no-simulate is used
843:                                    Simulate unless --no-simulate is used
2284:    --print-json                     -j --no-simulate
```

**assistant:** Reproducing the current behaviour first:

**tool call: Bash**

```bash
cat > /work/yt-dlp__yt-dlp-9862/repo/repro.py <<'EOF'
from test.helper import FakeYDL
for p, info, kw in [({'simulate': True}, {'is_live': True}, {}), ({'simulate': True, 'outtmpl': '-'}, {}, {}),
                    ({}, {'is_live': True}, {'download': False}) ]:
    print(p, info, kw, FakeYDL(p)._default_format_spec(info, **kw) if kw else FakeYDL(p)._default_format_spec(info))
EOF
/work/yt-dlp__yt-dlp-9862/bin/envrun 'python repro.py'
```

tool result:

```
{'simulate': True} {'is_live': True} {} bestvideo*+bestaudio/best
{'simulate': True, 'outtmpl': '-'} {} {} bestvideo*+bestaudio/best
{} {'is_live': True} {'download': False} bestvideo*+bestaudio/best
```

**assistant:** Confirmed: simulated runs pick a different format spec. Now the fix — make the default spec independent of `simulate`/`download`:

**tool call: Bash**

```bash
python3 - <<'EOF'
p='yt_dlp/YoutubeDL.py'
s=open(p).read()
s=s.replace("""    def _default_format_spec(self, info_dict, download=True):
        download = download and not self.params.get('simulate')
        prefer_best = download and (
            self.params['outtmpl']['default'] == '-'
            or info_dict.get('is_live') and not self.params.get('live_from_start'))
""","""    def _default_format_spec(self, info_dict):
        prefer_best = (
            self.params['outtmpl']['default'] == '-'
            or info_dict.get('is_live') and not self.params.get('live_from_start'))
""")
s=s.replace("if not prefer_best and download and not can_merge():","if not prefer_best and not can_merge():")
s=s.replace("req_format = self._default_format_spec(info_dict, download=download)","req_format = self._default_format_spec(info_dict)")
open(p,'w').write(s)
EOF
git diff --stat
sed -i '' 's/, \*\*kw) if kw else FakeYDL(p)._default_format_spec(info))/))/' repro.py
/work/yt-dlp__yt-dlp-9862/bin/envrun 'python repro.py'
```

tool result:

```
 yt_dlp/YoutubeDL.py | 9 ++++-----
 1 file changed, 4 insertions(+), 5 deletions(-)
{'simulate': True} {'is_live': True} {} best/bestvideo+bestaudio
{'simulate': True, 'outtmpl': '-'} {} {} best/bestvideo+bestaudio
{} {'is_live': True} {'download': False} best/bestvideo+bestaudio
```

**assistant:** Simulated runs now get the same spec as real downloads. Next I'll check for other callers and docs that mention the old behaviour, then run the tests:

**tool call: Bash**

```bash
rm repro.py; grep -rn "_default_format_spec" --include=*.py . ; grep -n -i "simulat\|dry" README.md | sed -n '/format/Ip'; /work/yt-dlp__yt-dlp-9862/bin/envrun 'python -m pytest -q test/test_YoutubeDL.py 2>&1 | tail -15'
```

tool result:

```
(eval):1: no matches found: --include=*.py
self = <test.test_YoutubeDL.TestFormatSelection testMethod=test_default_format_spec>

    def test_default_format_spec(self):
        ydl = YDL({'simulate': True})
>       self.assertEqual(ydl._default_format_spec({}), 'bestvideo*+bestaudio/best')
E       AssertionError: 'best/bestvideo+bestaudio' != 'bestvideo*+bestaudio/best'
E       - best/bestvideo+bestaudio
E       ? -----
E       + bestvideo*+bestaudio/best
E       ?          +          +++++

test/test_YoutubeDL.py:525: AssertionError
=========================== short test summary info ============================
FAILED test/test_YoutubeDL.py::TestFormatSelection::test_default_format_spec
========================= 1 failed, 24 passed in 3.27s =========================
```

**thinking:**

```
That one failure is expected since the container lacks ffmpeg and the test targets old `simulate` behavior. Next I'll verify the logic with `FFmpegMergerPP` patched both ways and re-run the caller grep that zsh had broken.


```

**tool call: Bash**

```bash
grep -rn "_default_format_spec" yt_dlp devscripts test; /work/yt-dlp__yt-dlp-9862/bin/envrun 'python - <<EOF
from unittest.mock import patch
from test.helper import FakeYDL as Y
with patch("yt_dlp.postprocessor.ffmpeg.FFmpegMergerPP.available", False):
    print("no ffmpeg:", Y({})._default_format_spec({}), "|", Y({"simulate": True})._default_format_spec({}))
with patch("yt_dlp.postprocessor.ffmpeg.FFmpegMergerPP.available", True), patch("yt_dlp.postprocessor.ffmpeg.FFmpegMergerPP.can_merge", lambda _: True):
    for p, i in [({}, {}), ({"simulate": True}, {}), ({"simulate": True}, {"is_live": True}), ({"live_from_start": True}, {"is_live": True}), ({"outtmpl": "-"}, {}), ({"allow_multiple_audio_streams": True}, {})]:
        print("ffmpeg:", p, i, Y(p)._default_format_spec(i))
EOF'
```

tool result:

```
Binary file yt_dlp/__pycache__/YoutubeDL.cpython-312.pyc matches
yt_dlp/YoutubeDL.py:2193:    def _default_format_spec(self, info_dict):
yt_dlp/YoutubeDL.py:2961:                req_format = self._default_format_spec(info_dict)
Binary file test/__pycache__/test_YoutubeDL.cpython-312-pytest-8.4.1.pyc matches
test/test_YoutubeDL.py:523:    def test_default_format_spec(self):
test/test_YoutubeDL.py:525:        self.assertEqual(ydl._default_format_spec({}), 'bestvideo*+bestaudio/best')
test/test_YoutubeDL.py:528:        self.assertEqual(ydl._default_format_spec({'is_live': True}), 'best/bestvideo+bestaudio')
test/test_YoutubeDL.py:531:        self.assertEqual(ydl._default_format_spec({'is_live': True}), 'bestvideo*+bestaudio/best')
test/test_YoutubeDL.py:534:        self.assertEqual(ydl._default_format_spec({}), 'best/bestvideo+bestaudio')
test/test_YoutubeDL.py:537:        self.assertEqual(ydl._default_format_spec({}, download=False), 'bestvideo*+bestaudio/best')
test/test_YoutubeDL.py:538:        self.assertEqual(ydl._default_format_spec({'is_live': True}), 'best/bestvideo+bestaudio')
no ffmpeg: best/bestvideo+bestaudio | best/bestvideo+bestaudio
ffmpeg: {} {} bestvideo*+bestaudio/best
ffmpeg: {'simulate': True} {} bestvideo*+bestaudio/best
ffmpeg: {'simulate': True} {'is_live': True} best/bestvideo+bestaudio
ffmpeg: {'live_from_start': True} {'is_live': True} bestvideo*+bestaudio/best
ffmpeg: {'outtmpl': '-'} {} best/bestvideo+bestaudio
ffmpeg: {'allow_multiple_audio_streams': True} {} bestvideo+bestaudio/best
```

**tool call: Bash**

```bash
git status --short; git diff
```

tool result:

```
 M yt_dlp/YoutubeDL.py
?? Dockerfile
diff --git a/yt_dlp/YoutubeDL.py b/yt_dlp/YoutubeDL.py
index e56c3ed3c..fd5aa0118 100644
--- a/yt_dlp/YoutubeDL.py
+++ b/yt_dlp/YoutubeDL.py
@@ -2190,9 +2190,8 @@ def _select_formats(self, formats, selector):
                                    or all(f.get('acodec') == 'none' for f in formats)),  # OR, No formats with audio
         }))
 
-    def _default_format_spec(self, info_dict, download=True):
-        download = download and not self.params.get('simulate')
-        prefer_best = download and (
+    def _default_format_spec(self, info_dict):
+        prefer_best = (
             self.params['outtmpl']['default'] == '-'
             or info_dict.get('is_live') and not self.params.get('live_from_start'))
 
@@ -2200,7 +2199,7 @@ def can_merge():
             merger = FFmpegMergerPP(self)
             return merger.available and merger.can_merge()
 
-        if not prefer_best and download and not can_merge():
+        if not prefer_best and not can_merge():
             prefer_best = True
             formats = self._get_formats(info_dict)
             evaluate_formats = lambda spec: self._select_formats(formats, self.build_format_selector(spec))
@@ -2959,7 +2958,7 @@ def is_wellformed(f):
                     continue
 
             if format_selector is None:
-                req_format = self._default_format_spec(info_dict, download=download)
+                req_format = self._default_format_spec(info_dict)
                 self.write_debug(f'Default format spec: {req_format}')
                 format_selector = self.build_format_selector(req_format)
```

**assistant:** `--simulate` (and other runs that don't download, like `-j`) now picks the same default format as a real download. One existing test fails as a result, `test_default_format_spec` in `test/test_YoutubeDL.py`, because it was written for the old behaviour; details below.

**Cause:** `_default_format_spec` in `yt_dlp/YoutubeDL.py` treated a simulated or non-downloading run differently. That turned off all three rules that fall back to `best/bestvideo+bestaudio`: output to `-`, a livestream without `--live-from-start`, and ffmpeg not being able to merge. This was left over from an old youtube-dl workaround that's no longer needed, since the default spec already falls back to video+audio.

**Fix:** I removed the `download` parameter and the `simulate` check, so those three rules always apply. I also updated the one place that calls the function. The "ffmpeg not found" warning now shows on simulated runs too, which matches what a real run would do.

**Checks:**
- Before the fix, I reproduced the bug: with `simulate`, a livestream and `outtmpl: '-'` both gave `bestvideo*+bestaudio/best`. After the fix, both give `best/bestvideo+bestaudio`.
- With ffmpeg patched as available, I checked the other cases (plain, simulate, live, live with `--live-from-start`, `outtmpl '-'`, `allow_multiple_audio_streams`). Each gave the expected spec, and simulated and real runs now match.
- With ffmpeg patched as unavailable, both runs give `best/bestvideo+bestaudio`.
- `test/test_YoutubeDL.py`: 24 passed, 1 failed. The failure is `test_default_format_spec`. The container has no ffmpeg, and the test still expects `YDL({'simulate': True})._default_format_spec({})` to skip the ffmpeg check and return `bestvideo*+bestaudio/best`. It also passes the `download=False` argument, which no longer exists. Since you said the tests are already handled, I left it unchanged; it will need updating to match the new behaviour if that hasn't been done.

I deleted my reproduction script. The untracked `Dockerfile` in the repo wasn't created by me, so I didn't touch it.

_session end: success, turns 9, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.69 s: python repro.py
- `rc=0` 0.44 s: python repro.py
- `rc=0` 3.88 s: python -m pytest -q test/test_YoutubeDL.py 2>&1 | tail -15
- `rc=0` 0.62 s: python - <<EOF from unittest.mock import patch from test.helper import FakeYDL as Y with patch("yt_dlp.postprocessor.ffmpeg.FFmpegMergerPP.available", False):     print("no ffmpeg:", Y({})._default_format_spec({}), "|", Y({"simulate": True})._default_format_spec({})) with patch("yt_dlp.postprocessor.ffmpeg.FFmpegMergerPP.available", True), patch("yt_dlp.postprocessor.ffmpeg.FFmpegMergerPP.can_merge", lambda _: True):     for p, i in [({}, {}), ({"simulate": True}, {}), ({"simulate": True}, {"is_live": True}), ({"live_from_start": True}, {"is_live": True}), ({"outtmpl": "-"}, {}), ({"allow_mult
