# OpenMontage on Codex (OpenAI Codex app)

**Install:** add this block to `~/.codex/AGENTS.md` (or the project `AGENTS.md`):

```markdown
## Video production
For any video creation request, use the OpenMontage engine at
C:\Users\MSI\Desktop\OpenMontage-Skill\OpenMontage — read its CODEX.md and AGENT_GUIDE.md first.
Machine pins + free-first policy: C:\Users\MSI\Desktop\OpenMontage-Skill\openmontage\SKILL.md
```

The engine ships its own `CODEX.md` and `.codex/` config — Codex is a first-class supported runtime.

## Play to the Codex app's strengths

- **Image input**: Codex can't watch video natively (per 2026 changelog), but it reviews renders well — extract frames with `ffmpeg -i out.mp4 -vf fps=1/2 frames/f_%03d.png` and inspect them for QC before presenting.
- **In-app browser**: open the backlot dashboard (`python -m backlot open`) inside Codex to watch the production live.
- **Image generation**: native — use it for thumbnails, storyboards, and style frames before committing GPU time.
- **Computer use**: source assets from archive/stock sites when an API route is missing.
- **Multiple terminals**: one for the pipeline driver, one for the GPU render, one for the dashboard.

Same GPU pins apply (8 GB → `wan2.1-1.3b`).
