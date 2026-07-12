# OpenMontage-Skill — universal AI video production hub

One skill, any LLM runtime: turn a natural-language brief into finished YouTube videos, Shorts, Instagram Reels, and TikToks — free-first (archive/stock footage, local TTS, local GPU generation), paid APIs only as opt-in.

Engine: [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) (AGPLv3) — cloned into `OpenMontage/` (gitignored; re-clone with the setup below).

```
openmontage/SKILL.md    the universal skill (agentskills.io format — works in Claude Code & Hermes Agent)
RUNTIMES/               per-runtime install + capability notes (Claude Code, Codex app, Hermes Agent)
COMPLEMENTS.md          free repos closing the gaps: YouTube/IG/TikTok publishing, Kokoro TTS, faster-whisper, MusicGen
tools/upload_youtube.py YouTube Data API v3 uploader (free)
```

## Setup (new machine)

```powershell
git clone https://github.com/calesthio/OpenMontage.git
cd OpenMontage
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\pip install -r requirements-gpu.txt diffusers transformers accelerate   # GPU box only
.venv\Scripts\pip install piper-tts kokoro soundfile faster-whisper google-api-python-client google-auth-oauthlib
cd remotion-composer && npm install && cd ..
copy .env.example .env    # set VIDEO_GEN_LOCAL_ENABLED=true, VIDEO_GEN_LOCAL_MODEL per your VRAM
```

Then install the skill for your runtime — see `RUNTIMES/`.

GPU sizing: 8 GB VRAM → `wan2.1-1.3b` only. 16 GB+ → `wan2.1-14b` / `ltx2-local`. 24 GB+ → `hunyuan-1.5`.
