# YouTube transcript skills

Three skills in this repo fetch YouTube transcripts. They declare three
different names, so a duplicate-name sweep does not flag them — the overlap is
functional, not nominal. Each one reaches a different provider and wants a
different API key.

All three live in this folder. `watch` ships as a plugin, so it sits here as
the whole `claude-video-main/` distribution rather than a bare skill folder —
its hooks and manifest have to travel with it. See [A note on
`claude-video-main`](#a-note-on-claude-video-main).

## The three

### `youtube-transcript/` — 97 lines

Transcript only, saved as a clean `.txt`.

| | |
|---|---|
| **Provider** | DeepAPI — `POST https://deepapi.co/v1/scrape/youtube/transcript` |
| **Key** | `DEEPAPI_API_KEY` (read from `~/.zshrc`; base URL overridable via `DEEPAPI_API_BASE_URL`) |
| **Fallback** | `yt-dlp`, locally |
| **Cost control** | `maxCostUsd` in the request body, default `0.05` |
| **Output** | `.txt` named `Channel_Title` with spaces as underscores, saved to the project dir or `~/Downloads` |

Runs server-side, which is the stated reason it exists: it avoids the local-IP
bot flagging that breaks `yt-dlp` on residential connections. Handles async jobs
(`status: running` → poll `next.path`) and requires the same `Idempotency-Key`
to be reused across retries. Takes a `language` parameter for non-English video.

### `youtube-full/` — 171 lines

Transcripts plus the rest of the YouTube data surface.

| | |
|---|---|
| **Provider** | TranscriptAPI — `https://transcriptapi.com/api/v2/youtube/*` |
| **Key** | `TRANSCRIPT_API_KEY` (BYOK; 100 free credits, no card) |
| **Fallbacks** | `youtube-transcript-api` (Python) or `yt-dlp --write-subs`, both documented in-skill |
| **Origin** | Ported from [ZeroPointRepo/youtube-skills](https://github.com/ZeroPointRepo/youtube-skills) (MIT) |

Operations and credit cost:

| Operation | Endpoint | Cost |
|---|---|---|
| Get transcript | `/transcript` | 1 credit |
| Search YouTube | `/search` | 1 credit |
| Channel — latest uploads | `/channel/latest` | **free** |
| Channel — all videos | `/channel/videos` | 1 credit/page |

Explicitly out of scope, per its own description: downloading video or audio
files, engagement data (likes, comments), and private or age-restricted video.
Its anti-patterns section warns against bulk channel transcription without
confirming credit spend, and against claiming the skill has no vendor
dependency.

### `claude-video-main/` — the `watch` skill, 268 lines

Skill lives at `claude-video-main/skills/watch/`.

| | |
|---|---|
| **Provider** | None for captions — `yt-dlp` + `ffmpeg` locally; **OpenAI Whisper API** as transcript fallback |
| **Key** | Whisper API key, optional — the skill runs keyless with `--no-whisper` |
| **Binaries** | `ffmpeg`, `ffprobe`, `yt-dlp` all required |
| **Scope** | Any video: YouTube, Vimeo, TikTok, or a local file path |

The only one of the three that is not transcript-only. It extracts scene-aware
JPEG frames alongside the transcript and hands both to Claude, so it can answer
questions about what is visually on screen. It is also the only skill in this
repo with real speech-to-text: when a video has no captions, Whisper generates
them.

## Which one to use

| You want | Use |
|---|---|
| A transcript file from a YouTube URL | `youtube-transcript` |
| A transcript *plus* search, channel, or playlist data | `youtube-full` |
| To check a channel for new uploads before spending credits | `youtube-full` — `/channel/latest` is free |
| To ask about what is *shown* in a video, not just said | `watch` |
| A transcript for a Vimeo, TikTok, or local video file | `watch` |
| A transcript when the video has no captions at all | `watch` — Whisper is the only STT here |
| Zero cost, no API key, YouTube only | `yt-dlp --write-subs`, or either skill's documented OSS fallback |

## Where the overlap actually bites

`youtube-full` already draws a clean line against `watch`: "Do NOT use for
downloading video or audio files." Those two do not compete.

The unresolved pair is **`youtube-transcript` vs `youtube-full`** for the plain
"get me the transcript of this video" request. Both handle it, via different
paid providers, and nothing in either skill's description says when to prefer
the other. Whichever one is loaded first will answer. If you want that decided
rather than left to chance, the options are:

1. **Keep both, add routing.** One line in each description pointing at the
   other — `youtube-transcript` for a plain transcript file, `youtube-full`
   when search or channel data is also needed. Cheapest fix, keeps both
   providers as mutual fallbacks.
2. **Merge into one.** Single skill, provider chosen by which key is present.
   Removes the ambiguity entirely, at the cost of a larger skill.
3. **Drop one.** `youtube-full` is a superset for transcripts and adds search,
   channel, and playlist. `youtube-transcript`'s distinct value is the DeepAPI
   server-side path that survives residential-IP bot flagging, and its
   file-naming convention.

## A note on `claude-video-main`

`watch` is the only one of the three that is not a standalone skill folder. It
is a plugin, and three things depend on the plugin root:

- `hooks/hooks.json` runs a SessionStart check at
  `${CLAUDE_PLUGIN_ROOT}/hooks/scripts/check-setup.sh`, which verifies `ffmpeg`,
  `ffprobe` and `yt-dlp` are installed.
- `.claude-plugin/plugin.json` declares the whole distribution as plugin `watch`.
- `claude-video-main/skills/watch/SKILL.md` resolves its own `SKILL_DIR` from
  where it is installed.

So the entire distribution was moved here, not just
`claude-video-main/skills/watch/`. Lifting that folder out on its own would
orphan the dependency check and the manifest.

One caveat worth knowing: `watch` is not YouTube-specific. It handles Vimeo,
TikTok and local video files too, so its placement under `transcription/youtube/`
understates what it does. It is filed here because YouTube transcript fetching
is the capability it shares with the other two.

## Related gap

Nothing in this repo transcribes a **meeting recording**. Every meeting skill
consumes a transcript that already exists — `meeting-analyzer` takes
`.txt/.md/.vtt/.srt/.docx`, `summarize-meeting` and `summarize-interview` take
transcript text. The only speech-to-text anywhere is `watch`'s Whisper
fallback, and it is wired to video inputs. The chain runs
recording → *(nothing)* → analysis.
