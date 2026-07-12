#!/usr/bin/env python3
"""Render all 12 video-01 visuals: 11 seekable HUD cards + 1 live gauntlet screencast.

Durations come from productions/video-01/build/sections.json (VO stage output),
each visual padded +GAP so assemble never loops awkwardly.

Run (any python3; rendering shells out to node + studio-kit renderer):
  python render_visuals.py [--only NN]
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
HUB = HERE.parent.parent
PROD = HUB / "productions" / "video-01"
VIS = PROD / "visuals"
RENDERER = HUB / "studio-kit" / "pipeline" / "generators" / "html3d-render.cjs"
COMP = HUB / "studio-kit" / "pipeline" / "generators" / "compositions" / "tc-card.html"
PAD_S = 1.0

# 3D background per section: bulb = raymarched mandelbulb, corridor = ring tunnel, net = particle web
BGS = {"01": "net", "02": "corridor", "03": "bulb", "04": "corridor", "05": "bulb", "06": "net",
       "08": "net", "09": "corridor", "10": "bulb", "11": "net", "12": "corridor"}

# All numbers verified — SCRIPT-VIDEO-01.md honesty checklist applies here too.
CARDS = {
 "01": {"kicker": "this week, inside one machine", "title": "",
        "counter": {"from": 349914, "to": 0, "label": "strategies validated so far — on purpose"},
        "lines": ["<b>349,914</b> strategies bred", "<b>111,966</b> admitted to the start line",
                  "validated: <span class='bad'>ZERO</span> — until the gauntlet says otherwise"]},
 "02": {"kicker": "the machine", "title": "One job:\nprove strategies **don't work**. And fail.",
        "lines": ["12-phase robustness gauntlet", "paper-only by design — order routing hard-blocked",
                  "survival after 12 rounds = the only compliment it pays"]},
 "03": {"kicker": "config file — unedited", "title": "Deliberately absent:\nWyckoff · Elliott · Order Blocks · **ICT**",
        "lines": ["\"structural concepts <b>NOT expressible</b> in this vocabulary\"",
                  "\"approximating them and keeping the famous name", "would be a <span class='warn'>mislabel</span>\""]},
 "04": {"kicker": "the chain", "title": "Can't be coded → can't be tested\n→ can't be **disproven**",
        "lines": ["when does a level count as \"swept\"?", "which candle closes the order block?",
                  "10 traders → 10 answers → <span class='bad'>0 falsifiable rules</span>"]},
 "05": {"kicker": "to be fair", "title": "Every \"ICT backtest\" tests a\n**private interpretation**",
        "lines": ["a different strategy — wearing the brand"]},
 "06": {"kicker": "what CAN be coded", "title": "10 textbook concepts.\nExact rules. **No vibes.**",
        "lines": ["Donchian breakout / breakdown · golden cross · EMA momentum",
                  "RSI mean-reversion / momentum · volatility squeeze",
                  "ATR expansion · inside bar · Bollinger reversion"]},
 # 07 = live gauntlet screencast (capture_gauntlet.cjs), not a card
 "08": {"kicker": "the label that matters", "title": "Admitted ≠ works.\nAdmitted = **worth torturing**.",
        "lines": ["every single one carries the same badge: <b>UNTESTED</b>",
                  "elsewhere: one green equity curve = \"profitable\""]},
 "09": {"kicker": "the gauntlet ahead", "title": "12 phases.\nEach exists because someone got **fooled** without it.",
        "lines": ["intake · out-of-sample · timing stress · <b>cost ×3</b>",
                  "MC parameter perturbation (200 sims) · <b>MC trade shuffle</b>",
                  "walk-forward (frozen params) · WFC gate · final OOS",
                  "governance: deflated Sharpe · PBO · CPCV"]},
 "10": {"kicker": "real receipt — real Dow data", "title": "A machine that can't say **no**\nis a marketing department",
        "lines": ["<span class='ok'>+129%</span> net, stable across subperiods → <b>ADOPTED</b>",
                  "<span class='warn'>+130%</span> headline, gains too concentrated → <b>REFUSED</b>",
                  "<span class='bad'>−41%</span> — grading made it worse. printed anyway."]},
 "11": {"kicker": "next on this channel", "title": "**111,966** strategies.\nThe battery runs on camera.",
        "lines": ["whatever survives, survives", "whatever dies, dies publicly",
                  "$997 course on the kill list? <span class='warn'>maybe wait a week</span>"]},
 "12": {"kicker": "run it yourself", "title": "The mini-gauntlet runs\nin **your browser**",
        "lines": ["link below — pick the strategy the internet sold you",
                  "research instrument · paper-only · no profit promised", "<b>subscribe for the executions</b>"]},
}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--only")
    args = p.parse_args()

    sections = {s["num"]: s for s in json.loads(
        (PROD / "build" / "sections.json").read_text(encoding="utf-8"))}
    VIS.mkdir(exist_ok=True)
    for num, card in CARDS.items():
        if args.only and num != args.only:
            continue
        out = VIS / f"{num}-card.mp4"
        if out.exists():
            print(f"[skip] {out.name}")
            continue
        dur = sections[num]["duration"] + PAD_S
        (COMP.parent / "cfg.json").write_text(json.dumps({**card, "bg": BGS.get(num, "net")}),
                                              encoding="utf-8")
        print(f"[render] {num} ({sections[num]['slug']}) {dur:.1f}s bg={BGS.get(num, 'net')}")
        r = subprocess.run(["node", str(RENDERER), "--html", str(COMP),
                            "--out", str(out), "--fps", "30", "--dur", f"{dur:.2f}",
                            "--w", "1920", "--h", "1080", "--nopost"], shell=True)
        if r.returncode:
            sys.exit(f"render failed on {num}")
    print("cards done. Section 07 = capture_gauntlet.cjs (live screencast).")


if __name__ == "__main__":
    main()
