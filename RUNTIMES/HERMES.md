# OpenMontage on Hermes Agent (Nous Research)

**Install:** Hermes uses the agentskills.io SKILL.md standard — same format as this skill:

```
npx skills add C:\Users\MSI\Desktop\OpenMontage-Skill\openmontage
```

(If a local path isn't accepted by your `skills` CLI version, copy the `openmontage\` folder into Hermes' skills directory.)

## Play to Hermes' strengths

- **HyperFrames is native to Hermes** (`npx skills add heygen-com/hyperframes`) — the same HTML+CSS+GSAP+FFmpeg composition engine OpenMontage supports as a Remotion alternative. For motion-graphics videos Hermes can go brief → HTML scenes → GSAP timing → MP4/WebM entirely with its own official skill, using OpenMontage's pipelines, script conventions, and quality gates as the production framework. Node ≥22 + FFmpeg required (this box: Node 24, FFmpeg 8.1 ✓).
- **Free TTS built in**: Hermes ships Edge TTS (free) — usable for narration drafts; final narration via Kokoro/Piper in the engine venv for word-level timing.
- **Browser automation** (Browser Use / local Chrome): source archive + stock footage where no API exists.
- **Vision**: paste extracted frames (`ffmpeg -vf fps=1/2`) for render QC.
- **Voice channels**: drive a production hands-free from Discord voice.

Same GPU pins apply (8 GB → `wan2.1-1.3b`); GPU tools run through the engine venv at `OpenMontage\.venv`.
