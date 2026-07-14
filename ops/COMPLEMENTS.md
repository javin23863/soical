# Pipeline Complements — free repos that close the gaps

OpenMontage covers research → script → assets → narration → captions → music → render.
These close the remaining gaps to a full YouTube/Shorts/Reels/TikTok pipeline. All free.

## Publishing

### YouTube (long-form + Shorts) — official API, free
`tools\upload_youtube.py` (this repo) — YouTube Data API v3 via `google-api-python-client` (installed in engine venv).
One-time setup (user, ~5 min):
1. https://console.cloud.google.com → new project → enable **YouTube Data API v3**
2. OAuth consent screen (External, add yourself as test user) → Credentials → **OAuth client ID (Desktop app)** → download as `tools\client_secret.json`
3. First run opens browser for consent; token cached in `tools\token.json`
Quota: 10,000 units/day default = ~6 uploads/day. Shorts = same upload, 9:16 + `#Shorts` in title/description.

### Instagram Reels + Facebook Reels — two routes
- **Official, free**: Meta Graph API content publishing — **one Meta developer app covers both**: IG Reels (`/media` + `media_type=REELS`, needs Instagram Business/Creator account linked to a Facebook Page) and Facebook Reels/Page video (`/{page-id}/video_reels`). Video must be at a public URL for ingestion. Most reliable; setup ~30 min once.
- **Unofficial**: [`subzeroid/instagrapi`](https://github.com/subzeroid/instagrapi) — `pip install instagrapi`, `clip_upload()` posts a Reel from a local file with username/password. Zero Meta-app setup. Risk: unofficial API, account flags possible — use a low-value account first.

### TikTok — two routes
- **Official, free**: TikTok Content Posting API — needs a TikTok developer app + audit approval before public posting (slow, but the legit path).
- **Unofficial**: [`wkaisertexas/tiktok-uploader`](https://github.com/wkaisertexas/tiktok-uploader) — browser-cookie-based upload from a local file. Zero app approval. Same caveat: unofficial, can break on TikTok UI changes.

**Default policy**: agent renders the vertical file + writes caption/hashtags; YouTube uploads automatically; for IG/FB/TikTok use an MCP connector (below) or unofficial route only if the user opts in, else hand them the ready-to-post package.

## MCP connectors — agent-native publishing (verified July 2026)

All three runtimes (Claude Code, Codex app, Hermes Agent) speak MCP; remote-URL MCPs are lowest-friction on Windows.

| Platform | MCP | Publish | Auth | Notes |
|---|---|---|---|---|
| YouTube | [anwerj/youtube-uploader-mcp](https://github.com/anwerj/youtube-uploader-mcp) | upload/schedule/update, thumbnails, subtitles | own Google OAuth (`client_secret.json`) | Go binary, ships Windows .exe; active (07/2026). **Recommended** — same OAuth app as `tools\upload_youtube.py` |
| Instagram Reels | [mikusnuz/meta-mcp](https://github.com/mikusnuz/meta-mcp) | `ig_publish_reel` + 57 Graph-v25 tools | Meta dev app + long-lived token + IG Business acct | `npx -y @mikusnuz/meta-mcp`. Alt: [jlbadano/ig-mcp](https://github.com/jlbadano/ig-mcp) (157★) |
| Facebook Pages/Reels | [kaewz-manga/facebook-pages-mcp-community](https://github.com/kaewz-manga/facebook-pages-mcp-community) | `fb_upload_video` + 27 Page tools | long-lived Page token | thin but works; or same Meta dev app via Graph API directly |
| TikTok | none pure-OSS (Content Posting API needs audited dev app) | — | — | go through a multi-platform layer ↓ |
| **Multi-platform** | [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app) (33k★, AGPL, self-hosted Docker) | schedule/publish video to TikTok/IG/YT/FB via MCP | Postiz API key → remote MCP URL | **strongest self-owned option**; TikTok still needs your approved dev app |
| **Multi-platform (fastest)** | [taisly/agent](https://github.com/taisly/agent) (MIT client) or [Upload-Post remote MCP](https://mcp.upload-post.com/mcp) | TikTok + IG Reels + YT Shorts + FB with one key | single API key, free tier | TikTok working in minutes, zero per-platform dev apps; volume = paid |

**Recommended stack**: YouTube = `anwerj/youtube-uploader-mcp` (own quota, free forever). IG + FB = one Meta dev app + `mikusnuz/meta-mcp`. TikTok = Upload-Post/taisly free tier now, self-hosted Postiz later if volume grows.

## Quality upgrades (installed in engine venv)

- **TTS**: [`hexgrad/kokoro`](https://github.com/hexgrad/kokoro) (Kokoro-82M, Apache-2.0) — near-commercial narration, CPU or GPU. Ladder: Kokoro → Piper → paid.
- **Transcription/captions**: [`SYSTRAN/faster-whisper`](https://github.com/SYSTRAN/faster-whisper) — word-level timestamps for repurposed footage (Clip Factory, Podcast Repurpose pipelines). `small`/`medium` models fine on 8 GB.

## Install-on-demand (heavy, not preinstalled)

- **Music**: [`facebookresearch/audiocraft`](https://github.com/facebookresearch/audiocraft) (MusicGen) — local music gen when royalty-free detection misses. `musicgen-small` fits 8 GB.
- **Local video gen models**: pulled automatically by the engine (diffusers) on first `wan2.1-1.3b` run — several GB download, one-time.

## Already covered by OpenMontage — don't add repos for these

Stock/archive sourcing, Remotion/HyperFrames composition, FFmpeg post, thumbnails (local SD tool),
word-level captions, royalty-free music detection, avatar/talking-head, dubbing/localization.
