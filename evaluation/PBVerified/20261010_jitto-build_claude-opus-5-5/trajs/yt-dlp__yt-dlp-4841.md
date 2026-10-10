# Instance: yt-dlp__yt-dlp-4841

- Final resolved (evaluator, logs/yt-dlp__yt-dlp-4841_result.json): True
- Run state: DONE
- One attempt. Duration 40.6 s, turns 5, actor cost $0.22289520000000002, container commands 3
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

````
<uploaded_files>
/work/yt-dlp__yt-dlp-4841/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/yt-dlp__yt-dlp-4841/repo. Consider the following issue description:

<issue_description>
DiscoveryPlusItaly error 403: Forbidden
### Checklist

- [X] I'm reporting a broken site
- [X] I've verified that I'm running yt-dlp version **2022.06.22.1** ([update instructions](https://github.com/yt-dlp/yt-dlp#update)) or later (specify commit)
- [X] I've checked that all provided URLs are playable in a browser with the same IP and same login details
- [X] I've checked that all URLs and arguments with special characters are [properly quoted or escaped](https://github.com/ytdl-org/youtube-dl#video-url-contains-an-ampersand-and-im-getting-some-strange-output-1-2839-or-v-is-not-recognized-as-an-internal-or-external-command)
- [X] I've searched the [bugtracker](https://github.com/yt-dlp/yt-dlp/issues?q=) for similar issues including closed ones. DO NOT post duplicates
- [X] I've read the [guidelines for opening an issue](https://github.com/yt-dlp/yt-dlp/blob/master/CONTRIBUTING.md#opening-an-issue)
- [X] I've read about [sharing account credentials](https://github.com/yt-dlp/yt-dlp/blob/master/CONTRIBUTING.md#are-you-willing-to-share-account-details-if-needed) and I'm willing to share it if required

### Region

Italy

### Description

Hi, for first thanks for your work.

With DiscoveryPlusItaly there is some problem.
With the same link https://www.discoveryplus.com/it/video/killer-of-the-cosmos/stagione-1-collisione i obtain url with domain dplus-it-cloudfront.prod-vod.h264.io (an the error 403 forbidden) another time with another file i obtain url domain  dplus-it-prod-vod.akamaized.net (with download ok).
Yesterday night i get same error with similar url and google cloud domain...

Anyone can help me?
Thanks

### Verbose log

```shell
F:\>yt-dlp.exe -Uv --no-geo-bypass --cookies-from-browser firefox https://www.discoveryplus.com/it/video/killer-of-the-cosmos/stagione-1-collisione
[debug] Command-line config: ['-Uv', '--no-geo-bypass', '--cookies-from-browser', 'firefox', 'https://www.discoveryplus.com/it/video/killer-of-the-cosmos/stagione-1-collisione']
[debug] Encodings: locale cp1252, fs utf-8, pref cp1252, out utf-8, error utf-8, screen utf-8
[debug] yt-dlp version 2022.06.22.1 [a86e01e] (win32_exe)
[debug] Python version 3.8.10 (CPython 64bit) - Windows-10-10.0.22621-SP0
[debug] Checking exe version: ffmpeg -bsfs
[debug] Checking exe version: ffprobe -bsfs
[debug] Checking exe version: avprobe -bsfs
[debug] exe versions: ffmpeg 5.0.1-full_build-www.gyan.dev (setts)
[debug] Optional libraries: Cryptodome-3.14.1, brotli-1.0.9, certifi-2022.06.15, mutagen-1.45.1, sqlite3-2.6.0, websockets-10.3
[Cookies] Extracting cookies from firefox
[debug] Extracting cookies from: "C:\Users\Lepitrust\AppData\Roaming\Mozilla\Firefox\Profiles\bwd4mkhg.default-release\cookies.sqlite"
[Cookies] Extracted 44 cookies from firefox
[debug] Proxy map: {}
[debug] Fetching release info: https://api.github.com/repos/yt-dlp/yt-dlp/releases/latest
Latest version: 2022.06.22.1, Current version: 2022.06.22.1
yt-dlp is up to date (2022.06.22.1)
[debug] [DiscoveryPlusItaly] Extracting URL: https://www.discoveryplus.com/it/video/killer-of-the-cosmos/stagione-1-collisione
[DiscoveryPlusItaly] killer-of-the-cosmos/stagione-1-collisione: Downloading JSON metadata
[DiscoveryPlusItaly] 564088: Downloading JSON metadata
[DiscoveryPlusItaly] killer-of-the-cosmos/stagione-1-collisione: Downloading MPD manifest
[debug] Formats sorted by: hasvid, ie_pref, lang, quality, res, fps, hdr:12(7), vcodec:vp9.2(10), acodec, filesize, fs_approx, tbr, vbr, abr, asr, proto, vext, aext, hasaud, source, id
[debug] Default format spec: bestvideo*+bestaudio/best
[info] 564088: Downloading 1 format(s): dash-video=6369520+dash-audio_eng=160000
[debug] Invoking dashsegments downloader on "https://dplus-it-cloudfront.prod-vod.h264.io/90902a8f-ca80-4385-9c88-e8d81407253e/dbcb9fcb-ba71-4f73-b959-976b88227cb6/dash_clear_fmp4/x-discovery-token=Expires=1656240923&KeyName=primary&Signature=iida0AdPfjG2eZmWfIjPZ0SqU3U/master.mpd"
[dashsegments] Total fragments: 1324
[download] Destination: Collisione [564088].fdash-video=6369520.mp4
[debug] File locking is not supported. Proceeding without locking
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 1 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 2 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 3 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 4 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 5 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 6 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 7 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 8 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 9 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 10 of 10) ...
ERROR: Giving up after 10 fragment retries
  File "yt_dlp\__main__.py", line 16, in <module>
  File "yt_dlp\__init__.py", line 919, in main
  File "yt_dlp\__init__.py", line 911, in _real_main
  File "yt_dlp\YoutubeDL.py", line 3247, in download
  File "yt_dlp\YoutubeDL.py", line 3223, in wrapper
  File "yt_dlp\YoutubeDL.py", line 1418, in extract_info
  File "yt_dlp\YoutubeDL.py", line 1427, in wrapper
  File "yt_dlp\YoutubeDL.py", line 1511, in __extract_info
  File "yt_dlp\YoutubeDL.py", line 1568, in process_ie_result
  File "yt_dlp\YoutubeDL.py", line 2628, in process_video_result
  File "yt_dlp\YoutubeDL.py", line 3109, in process_info
  File "yt_dlp\YoutubeDL.py", line 2827, in dl
  File "yt_dlp\downloader\common.py", line 444, in download
  File "yt_dlp\downloader\dash.py", line 54, in real_download
  File "yt_dlp\downloader\fragment.py", line 370, in download_and_append_fragments_multiple
  File "yt_dlp\downloader\fragment.py", line 522, in download_and_append_fragments
  File "yt_dlp\downloader\fragment.py", line 478, in download_fragment
  File "yt_dlp\YoutubeDL.py", line 969, in report_error
  File "yt_dlp\YoutubeDL.py", line 901, in trouble

ERROR: fragment 1 not found, unable to continue
  File "yt_dlp\__main__.py", line 16, in <module>
  File "yt_dlp\__init__.py", line 919, in main
  File "yt_dlp\__init__.py", line 911, in _real_main
  File "yt_dlp\YoutubeDL.py", line 3247, in download
  File "yt_dlp\YoutubeDL.py", line 3223, in wrapper
  File "yt_dlp\YoutubeDL.py", line 1418, in extract_info
  File "yt_dlp\YoutubeDL.py", line 1427, in wrapper
  File "yt_dlp\YoutubeDL.py", line 1511, in __extract_info
  File "yt_dlp\YoutubeDL.py", line 1568, in process_ie_result
  File "yt_dlp\YoutubeDL.py", line 2628, in process_video_result
  File "yt_dlp\YoutubeDL.py", line 3109, in process_info
  File "yt_dlp\YoutubeDL.py", line 2827, in dl
  File "yt_dlp\downloader\common.py", line 444, in download
  File "yt_dlp\downloader\dash.py", line 54, in real_download
  File "yt_dlp\downloader\fragment.py", line 370, in download_and_append_fragments_multiple
  File "yt_dlp\downloader\fragment.py", line 523, in download_and_append_fragments
  File "yt_dlp\downloader\fragment.py", line 487, in append_fragment
  File "yt_dlp\YoutubeDL.py", line 969, in report_error
  File "yt_dlp\YoutubeDL.py", line 901, in trouble


[debug] Invoking dashsegments downloader on "https://dplus-it-cloudfront.prod-vod.h264.io/90902a8f-ca80-4385-9c88-e8d81407253e/dbcb9fcb-ba71-4f73-b959-976b88227cb6/dash_clear_fmp4/x-discovery-token=Expires=1656240923&KeyName=primary&Signature=iida0AdPfjG2eZmWfIjPZ0SqU3U/master.mpd"
[dashsegments] Total fragments: 1324
[download] Destination: Collisione [564088].fdash-audio_eng=160000.m4a
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 1 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 2 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 3 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 4 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 5 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 6 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 7 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 8 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 9 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 10 of 10) ...
ERROR: Giving up after 10 fragment retries
  File "yt_dlp\__main__.py", line 16, in <module>
  File "yt_dlp\__init__.py", line 919, in main
  File "yt_dlp\__init__.py", line 911, in _real_main
  File "yt_dlp\YoutubeDL.py", line 3247, in download
  File "yt_dlp\YoutubeDL.py", line 3223, in wrapper
  File "yt_dlp\YoutubeDL.py", line 1418, in extract_info
  File "yt_dlp\YoutubeDL.py", line 1427, in wrapper
  File "yt_dlp\YoutubeDL.py", line 1511, in __extract_info
  File "yt_dlp\YoutubeDL.py", line 1568, in process_ie_result
  File "yt_dlp\YoutubeDL.py", line 2628, in process_video_result
  File "yt_dlp\YoutubeDL.py", line 3109, in process_info
  File "yt_dlp\YoutubeDL.py", line 2827, in dl
  File "yt_dlp\downloader\common.py", line 444, in download
  File "yt_dlp\downloader\dash.py", line 54, in real_download
  File "yt_dlp\downloader\fragment.py", line 370, in download_and_append_fragments_multiple
  File "yt_dlp\downloader\fragment.py", line 522, in download_and_append_fragments
  File "yt_dlp\downloader\fragment.py", line 478, in download_fragment
  File "yt_dlp\YoutubeDL.py", line 969, in report_error
  File "yt_dlp\YoutubeDL.py", line 901, in trouble

ERROR: fragment 1 not found, unable to continue
  File "yt_dlp\__main__.py", line 16, in <module>
  File "yt_dlp\__init__.py", line 919, in main
  File "yt_dlp\__init__.py", line 911, in _real_main
  File "yt_dlp\YoutubeDL.py", line 3247, in download
  File "yt_dlp\YoutubeDL.py", line 3223, in wrapper
  File "yt_dlp\YoutubeDL.py", line 1418, in extract_info
  File "yt_dlp\YoutubeDL.py", line 1427, in wrapper
  File "yt_dlp\YoutubeDL.py", line 1511, in __extract_info
  File "yt_dlp\YoutubeDL.py", line 1568, in process_ie_result
  File "yt_dlp\YoutubeDL.py", line 2628, in process_video_result
  File "yt_dlp\YoutubeDL.py", line 3109, in process_info
  File "yt_dlp\YoutubeDL.py", line 2827, in dl
  File "yt_dlp\downloader\common.py", line 444, in download
  File "yt_dlp\downloader\dash.py", line 54, in real_download
  File "yt_dlp\downloader\fragment.py", line 370, in download_and_append_fragments_multiple
  File "yt_dlp\downloader\fragment.py", line 523, in download_and_append_fragments
  File "yt_dlp\downloader\fragment.py", line 487, in append_fragment
  File "yt_dlp\YoutubeDL.py", line 969, in report_error
  File "yt_dlp\YoutubeDL.py", line 901, in trouble
```

TRY without --no-geo-bypass: getting same error with google cloud url
```shell
F:\>yt-dlp.exe -Uv --cookies-from-browser firefox https://www.discoveryplus.com/it/video/killer-of-the-cosmos/stagione-1-collisione
[debug] Command-line config: ['-Uv', '--cookies-from-browser', 'firefox', 'https://www.discoveryplus.com/it/video/killer-of-the-cosmos/stagione-1-collisione']
[debug] Encodings: locale cp1252, fs utf-8, pref cp1252, out utf-8, error utf-8, screen utf-8
[debug] yt-dlp version 2022.06.22.1 [a86e01e] (win32_exe)
[debug] Python version 3.8.10 (CPython 64bit) - Windows-10-10.0.22621-SP0
[debug] Checking exe version: ffmpeg -bsfs
[debug] Checking exe version: ffprobe -bsfs
[debug] Checking exe version: avprobe -bsfs
[debug] exe versions: ffmpeg 5.0.1-full_build-www.gyan.dev (setts)
[debug] Optional libraries: Cryptodome-3.14.1, brotli-1.0.9, certifi-2022.06.15, mutagen-1.45.1, sqlite3-2.6.0, websockets-10.3
[Cookies] Extracting cookies from firefox
[debug] Extracting cookies from: "C:\Users\Lepitrust\AppData\Roaming\Mozilla\Firefox\Profiles\bwd4mkhg.default-release\cookies.sqlite"
[Cookies] Extracted 45 cookies from firefox
[debug] Proxy map: {}
[debug] Fetching release info: https://api.github.com/repos/yt-dlp/yt-dlp/releases/latest
Latest version: 2022.06.22.1, Current version: 2022.06.22.1
yt-dlp is up to date (2022.06.22.1)
[debug] [DiscoveryPlusItaly] Extracting URL: https://www.discoveryplus.com/it/video/killer-of-the-cosmos/stagione-1-collisione
[debug] Using fake IP 79.48.22.233 (IT) as X-Forwarded-For
[DiscoveryPlusItaly] killer-of-the-cosmos/stagione-1-collisione: Downloading JSON metadata
[DiscoveryPlusItaly] 564088: Downloading JSON metadata
[DiscoveryPlusItaly] killer-of-the-cosmos/stagione-1-collisione: Downloading MPD manifest
[debug] Formats sorted by: hasvid, ie_pref, lang, quality, res, fps, hdr:12(7), vcodec:vp9.2(10), acodec, filesize, fs_approx, tbr, vbr, abr, asr, proto, vext, aext, hasaud, source, id
[debug] Default format spec: bestvideo*+bestaudio/best
[info] 564088: Downloading 1 format(s): dash-video=6369520+dash-audio_eng=160000
[debug] Invoking dashsegments downloader on "https://dplus-it-google-v2.prod-vod.h264.io/90902a8f-ca80-4385-9c88-e8d81407253e/dbcb9fcb-ba71-4f73-b959-976b88227cb6/dash_clear_fmp4/x-goog-token=Expires=1656241208&KeyName=prod-sign-url-key-eu&Signature=h6ET8IWbm5cz_jq0YZLRbtegYLo/master.mpd"
[dashsegments] Total fragments: 1324
[download] Destination: Collisione [564088].fdash-video=6369520.mp4
[debug] File locking is not supported. Proceeding without locking
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 1 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 2 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 3 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 4 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 5 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 6 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 7 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 8 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 9 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 10 of 10) ...
ERROR: Giving up after 10 fragment retries
  File "yt_dlp\__main__.py", line 16, in <module>
  File "yt_dlp\__init__.py", line 919, in main
  File "yt_dlp\__init__.py", line 911, in _real_main
  File "yt_dlp\YoutubeDL.py", line 3247, in download
  File "yt_dlp\YoutubeDL.py", line 3223, in wrapper
  File "yt_dlp\YoutubeDL.py", line 1418, in extract_info
  File "yt_dlp\YoutubeDL.py", line 1427, in wrapper
  File "yt_dlp\YoutubeDL.py", line 1511, in __extract_info
  File "yt_dlp\YoutubeDL.py", line 1568, in process_ie_result
  File "yt_dlp\YoutubeDL.py", line 2628, in process_video_result
  File "yt_dlp\YoutubeDL.py", line 3109, in process_info
  File "yt_dlp\YoutubeDL.py", line 2827, in dl
  File "yt_dlp\downloader\common.py", line 444, in download
  File "yt_dlp\downloader\dash.py", line 54, in real_download
  File "yt_dlp\downloader\fragment.py", line 370, in download_and_append_fragments_multiple
  File "yt_dlp\downloader\fragment.py", line 522, in download_and_append_fragments
  File "yt_dlp\downloader\fragment.py", line 478, in download_fragment
  File "yt_dlp\YoutubeDL.py", line 969, in report_error
  File "yt_dlp\YoutubeDL.py", line 901, in trouble

ERROR: fragment 1 not found, unable to continue
  File "yt_dlp\__main__.py", line 16, in <module>
  File "yt_dlp\__init__.py", line 919, in main
  File "yt_dlp\__init__.py", line 911, in _real_main
  File "yt_dlp\YoutubeDL.py", line 3247, in download
  File "yt_dlp\YoutubeDL.py", line 3223, in wrapper
  File "yt_dlp\YoutubeDL.py", line 1418, in extract_info
  File "yt_dlp\YoutubeDL.py", line 1427, in wrapper
  File "yt_dlp\YoutubeDL.py", line 1511, in __extract_info
  File "yt_dlp\YoutubeDL.py", line 1568, in process_ie_result
  File "yt_dlp\YoutubeDL.py", line 2628, in process_video_result
  File "yt_dlp\YoutubeDL.py", line 3109, in process_info
  File "yt_dlp\YoutubeDL.py", line 2827, in dl
  File "yt_dlp\downloader\common.py", line 444, in download
  File "yt_dlp\downloader\dash.py", line 54, in real_download
  File "yt_dlp\downloader\fragment.py", line 370, in download_and_append_fragments_multiple
  File "yt_dlp\downloader\fragment.py", line 523, in download_and_append_fragments
  File "yt_dlp\downloader\fragment.py", line 487, in append_fragment
  File "yt_dlp\YoutubeDL.py", line 969, in report_error
  File "yt_dlp\YoutubeDL.py", line 901, in trouble


[debug] Invoking dashsegments downloader on "https://dplus-it-google-v2.prod-vod.h264.io/90902a8f-ca80-4385-9c88-e8d81407253e/dbcb9fcb-ba71-4f73-b959-976b88227cb6/dash_clear_fmp4/x-goog-token=Expires=1656241208&KeyName=prod-sign-url-key-eu&Signature=h6ET8IWbm5cz_jq0YZLRbtegYLo/master.mpd"
[dashsegments] Total fragments: 1324
[download] Destination: Collisione [564088].fdash-audio_eng=160000.m4a
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 1 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 2 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 3 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 4 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 5 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 6 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 7 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 8 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 9 of 10) ...
[download] Got server HTTP error: HTTP Error 403: Forbidden. Retrying fragment 1 (attempt 10 of 10) ...
ERROR: Giving up after 10 fragment retries
  File "yt_dlp\__main__.py", line 16, in <module>
  File "yt_dlp\__init__.py", line 919, in main
  File "yt_dlp\__init__.py", line 911, in _real_main
  File "yt_dlp\YoutubeDL.py", line 3247, in download
  File "yt_dlp\YoutubeDL.py", line 3223, in wrapper
  File "yt_dlp\YoutubeDL.py", line 1418, in extract_info
  File "yt_dlp\YoutubeDL.py", line 1427, in wrapper
  File "yt_dlp\YoutubeDL.py", line 1511, in __extract_info
  File "yt_dlp\YoutubeDL.py", line 1568, in process_ie_result
  File "yt_dlp\YoutubeDL.py", line 2628, in process_video_result
  File "yt_dlp\YoutubeDL.py", line 3109, in process_info
  File "yt_dlp\YoutubeDL.py", line 2827, in dl
  File "yt_dlp\downloader\common.py", line 444, in download
  File "yt_dlp\downloader\dash.py", line 54, in real_download
  File "yt_dlp\downloader\fragment.py", line 370, in download_and_append_fragments_multiple
  File "yt_dlp\downloader\fragment.py", line 522, in download_and_append_fragments
  File "yt_dlp\downloader\fragment.py", line 478, in download_fragment
  File "yt_dlp\YoutubeDL.py", line 969, in report_error
  File "yt_dlp\YoutubeDL.py", line 901, in trouble

ERROR: fragment 1 not found, unable to continue
  File "yt_dlp\__main__.py", line 16, in <module>
  File "yt_dlp\__init__.py", line 919, in main
  File "yt_dlp\__init__.py", line 911, in _real_main
  File "yt_dlp\YoutubeDL.py", line 3247, in download
  File "yt_dlp\YoutubeDL.py", line 3223, in wrapper
  File "yt_dlp\YoutubeDL.py", line 1418, in extract_info
  File "yt_dlp\YoutubeDL.py", line 1427, in wrapper
  File "yt_dlp\YoutubeDL.py", line 1511, in __extract_info
  File "yt_dlp\YoutubeDL.py", line 1568, in process_ie_result
  File "yt_dlp\YoutubeDL.py", line 2628, in process_video_result
  File "yt_dlp\YoutubeDL.py", line 3109, in process_info
  File "yt_dlp\YoutubeDL.py", line 2827, in dl
  File "yt_dlp\downloader\common.py", line 444, in download
  File "yt_dlp\downloader\dash.py", line 54, in real_download
  File "yt_dlp\downloader\fragment.py", line 370, in download_and_append_fragments_multiple
  File "yt_dlp\downloader\fragment.py", line 523, in download_and_append_fragments
  File "yt_dlp\downloader\fragment.py", line 487, in append_fragment
  File "yt_dlp\YoutubeDL.py", line 969, in report_error
  File "yt_dlp\YoutubeDL.py", line 901, in trouble
```

AKAMAIZED is OK!
```shell
F:\>yt-dlp.exe -Uv --no-geo-bypass --cookies-from-browser firefox https://www.discoveryplus.com/it/video/killer-of-the-cosmos/stagione-1-collisione
[debug] Command-line config: ['-Uv', '--no-geo-bypass', '--cookies-from-browser', 'firefox', 'https://www.discoveryplus.com/it/video/killer-of-the-cosmos/stagione-1-collisione']
[debug] Encodings: locale cp1252, fs utf-8, pref cp1252, out utf-8, error utf-8, screen utf-8
[debug] yt-dlp version 2022.06.22.1 [a86e01e] (win32_exe)
[debug] Python version 3.8.10 (CPython 64bit) - Windows-10-10.0.22621-SP0
[debug] Checking exe version: ffmpeg -bsfs
[debug] Checking exe version: ffprobe -bsfs
[debug] Checking exe version: avprobe -bsfs
[debug] exe versions: ffmpeg 5.0.1-full_build-www.gyan.dev (setts)
[debug] Optional libraries: Cryptodome-3.14.1, brotli-1.0.9, certifi-2022.06.15, mutagen-1.45.1, sqlite3-2.6.0, websockets-10.3
[Cookies] Extracting cookies from firefox
[debug] Extracting cookies from: "C:\Users\Lepitrust\AppData\Roaming\Mozilla\Firefox\Profiles\bwd4mkhg.default-release\cookies.sqlite"
[Cookies] Extracted 45 cookies from firefox
[debug] Proxy map: {}
[debug] Fetching release info: https://api.github.com/repos/yt-dlp/yt-dlp/releases/latest
Latest version: 2022.06.22.1, Current version: 2022.06.22.1
yt-dlp is up to date (2022.06.22.1)
[debug] [DiscoveryPlusItaly] Extracting URL: https://www.discoveryplus.com/it/video/killer-of-the-cosmos/stagione-1-collisione
[DiscoveryPlusItaly] killer-of-the-cosmos/stagione-1-collisione: Downloading JSON metadata
[DiscoveryPlusItaly] 564088: Downloading JSON metadata
[DiscoveryPlusItaly] killer-of-the-cosmos/stagione-1-collisione: Downloading MPD manifest
[debug] Formats sorted by: hasvid, ie_pref, lang, quality, res, fps, hdr:12(7), vcodec:vp9.2(10), acodec, filesize, fs_approx, tbr, vbr, abr, asr, proto, vext, aext, hasaud, source, id
[debug] Default format spec: bestvideo*+bestaudio/best
[info] 564088: Downloading 1 format(s): dash-video=6369520+dash-audio_eng=160000
[debug] Invoking dashsegments downloader on "https://dplus-it-prod-vod.akamaized.net/90902a8f-ca80-4385-9c88-e8d81407253e/dbcb9fcb-ba71-4f73-b959-976b88227cb6/dash_clear_fmp4/hdntl=exp=1656241315~acl=/90902a8f-ca80-4385-9c88-e8d81407253e/dbcb9fcb-ba71-4f73-b959-976b88227cb6/dash_clear_fmp4/*~data=hdntl~hmac=ab864b1d7baf327ba03d13c89c296efd0c7c20c963a4c6a7e4c9ef09d5043739/master.mpd"
[dashsegments] Total fragments: 1324
[download] Destination: Collisione [564088].fdash-video=6369520.mp4
[debug] File locking is not supported. Proceeding without locking
[download]   2.2% of ~1.87GiB at    3.13MiB/s ETA 08:22 (frag 29/1324)
.......
```

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/yt-dlp__yt-dlp-4841/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/yt-dlp__yt-dlp-4841/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/yt-dlp__yt-dlp-4841/bin/envrun 'git status --short && ls'
Edits you make under /work/yt-dlp__yt-dlp-4841/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

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
grep -n -A6 "^def base_url" yt_dlp/utils.py; grep -n -A8 "def test_base_url" test/test_utils.py
```

tool result:

```
2481:def base_url(url):
2482-    return re.match(r'https?://[^?#&]+/', url).group()
2483-
2484-
2485-def urljoin(base, path):
2486-    if isinstance(path, bytes):
2487-        path = path.decode()
563:    def test_base_url(self):
564-        self.assertEqual(base_url('http://foo.de/'), 'http://foo.de/')
565-        self.assertEqual(base_url('http://foo.de/bar'), 'http://foo.de/')
566-        self.assertEqual(base_url('http://foo.de/bar/'), 'http://foo.de/bar/')
567-        self.assertEqual(base_url('http://foo.de/bar/baz'), 'http://foo.de/bar/')
568-        self.assertEqual(base_url('http://foo.de/bar/baz?x=z/x/c'), 'http://foo.de/bar/')
569-
570-    def test_urljoin(self):
571-        self.assertEqual(urljoin('http://foo.de/', '/a/b/c.txt'), 'http://foo.de/a/b/c.txt')
```

**thinking:**

```
Found it: `base_url`'s regex in `yt_dlp/utils.py` excludes `&`, so for MPD URLs with token segments containing `&` it truncates the path and drops the signed token, causing 403s on fragment requests (Akamai URLs work since their tokens lack `&`). Now reproducing the issue.


```

**tool call: Bash**

```bash
cd /work/yt-dlp__yt-dlp-4841; bin/envrun "python -c \"from yt_dlp.utils import base_url; print(base_url('https://dplus-it-google-v2.prod-vod.h264.io/90902a8f/dbcb9fcb/dash_clear_fmp4/x-goog-token=Expires=1656241208&KeyName=prod-sign-url-key-eu&Signature=h6ET8IWbm5cz_jq0YZLRbtegYLo/master.mpd'))\""
```

tool result:

```
https://dplus-it-google-v2.prod-vod.h264.io/90902a8f/dbcb9fcb/dash_clear_fmp4/
Shell cwd was reset to /work/yt-dlp__yt-dlp-4841/repo
```

**assistant:** That confirms the bug: the token segment is gone. The fix is to allow `&` in the path:

**tool call: Bash**

```bash
sed -i '' "s|re.match(r'https?://\[^?#&\]+/', url)|re.match(r'https?://[^?#]+/', url)|" yt_dlp/utils.py && sed -n 2481,2483p yt_dlp/utils.py
cd ..; bin/envrun "python -c \"from yt_dlp.utils import base_url; print(base_url('https://dplus-it-google-v2.prod-vod.h264.io/90902a8f/dbcb9fcb/dash_clear_fmp4/x-goog-token=Expires=1656241208&KeyName=prod-sign-url-key-eu&Signature=h6ET8IWbm5cz_jq0YZLRbtegYLo/master.mpd')); print(base_url('http://foo.de/bar/baz?x=z/x/c&a=b/c'))\" && python -m pytest -q test/test_utils.py 2>&1 | tail -3"
```

tool result:

```
def base_url(url):
    return re.match(r'https?://[^?#]+/', url).group()

https://dplus-it-google-v2.prod-vod.h264.io/90902a8f/dbcb9fcb/dash_clear_fmp4/x-goog-token=Expires=1656241208&KeyName=prod-sign-url-key-eu&Signature=h6ET8IWbm5cz_jq0YZLRbtegYLo/
http://foo.de/bar/
=========================== short test summary info ============================
FAILED test/test_utils.py::TestUtil::test_locked_file - AssertionError: True ...
================== 1 failed, 104 passed, 83 warnings in 0.27s ==================
Shell cwd was reset to /work/yt-dlp__yt-dlp-4841/repo
```

**assistant:** One test failed, so I'll check whether it fails without my change too:

**tool call: Bash**

```bash
git stash -q && ../bin/envrun "python -m pytest -q test/test_utils.py -k locked_file 2>&1 | tail -1"; git stash pop -q && git diff --stat
```

tool result:

```
====================== 1 failed, 104 deselected in 0.24s =======================

 yt_dlp/utils.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**assistant:** I fixed the bug with a one-line change in `yt_dlp/utils.py`, in `base_url`.

**Cause:** When yt-dlp downloads a DASH stream, it takes the manifest (`master.mpd`) URL, strips it back to a "base URL" with `base_url`, and builds each fragment URL from that. The regex there was `r'https?://[^?#&]+/'`, so it treated `&` as the end of the path. The CloudFront and Google CDN URLs carry their signed token as a path segment that contains `&`:

```
.../dash_clear_fmp4/x-goog-token=Expires=...&KeyName=...&Signature=.../master.mpd
```

So the base URL was cut off at `.../dash_clear_fmp4/`, the token was lost, and every fragment request got a 403. The Akamai URLs worked only because their token (`hdntl=exp=...~acl=...`) has no `&` in it. That's why the same video sometimes downloaded and sometimes didn't: it depended on which CDN the server picked.

**Fix:** I changed the regex to `r'https?://[^?#]+/'`. An `&` is a legal character in a URL path; the query string still begins at `?`, so it is still excluded.

**Checks:**
- Before the fix, the issue's Google CDN URL gave `.../dash_clear_fmp4/`. After it, the result is `.../dash_clear_fmp4/x-goog-token=...&Signature=.../`, with the token kept.
- A query containing `&` and `/` (`http://foo.de/bar/baz?x=z/x/c&a=b/c`) still gives `http://foo.de/bar/`.
- `test/test_utils.py`: 104 passed, 1 failed. The failure is `test_locked_file`, and it fails the same way without my change, so the fix didn't cause it.

I didn't download anything from Discovery+ itself, since the container has no network access. I didn't create any extra files, so the diff is only that one line.

_session end: success, turns 5, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 0.61 s: python -c "from yt_dlp.utils import base_url; print(base_url('https://dplus-it-google-v2.prod-vod.h264.io/90902a8f/dbcb9fcb/dash_clear_fmp4/x-goog-token=Expires=1656241208&KeyName=prod-sign-url-key-eu&Signature=h6ET8IWbm5cz_jq0YZLRbtegYLo/master.mpd'))"
- `rc=0` 1.0 s: python -c "from yt_dlp.utils import base_url; print(base_url('https://dplus-it-google-v2.prod-vod.h264.io/90902a8f/dbcb9fcb/dash_clear_fmp4/x-goog-token=Expires=1656241208&KeyName=prod-sign-url-key-eu&Signature=h6ET8IWbm5cz_jq0YZLRbtegYLo/master.mpd')); print(base_url('http://foo.de/bar/baz?x=z/x/c&a=b/c'))" && python -m pytest -q test/test_utils.py 2>&1 | tail -3
- `rc=0` 0.64 s: python -m pytest -q test/test_utils.py -k locked_file 2>&1 | tail -1
