#!/usr/bin/env node
// Screencast the real landing-page gauntlet run -> visuals/07-gauntlet.mp4
// Usage: node capture_gauntlet.cjs [--dur 22]
const puppeteer = require(require("path").join(__dirname, "..", "..", "studio-kit",
  "pipeline", "generators", "node_modules", "puppeteer"));
const path = require("path");
const { spawnSync } = require("child_process");
const fs = require("fs");

const DUR = +(process.argv.includes("--dur") ? process.argv[process.argv.indexOf("--dur") + 1] : 22);
const HUB = path.join(__dirname, "..", "..");
const PAGE = "file:///" + path.join(HUB, "docs", "index.html").replace(/\\/g, "/");
const OUT = path.join(HUB, "productions", "video-01", "visuals", "07-gauntlet.mp4");
const TMP = OUT.replace(/\.mp4$/, ".webm");

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    args: ["--no-sandbox", "--window-size=1920,1080", "--hide-scrollbars", "--force-color-profile=srgb"],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080 });
  await page.goto(PAGE, { waitUntil: "load" });
  await page.click("#boot").catch(() => {});           // skip boot for the capture
  await page.evaluate(() => document.getElementById("chamber").scrollIntoView({ block: "center" }));
  const recorder = await page.screencast({ path: TMP });
  await page.click(".chip");                            // first strategy chip (ICT / Smart Money)
  await new Promise(r => setTimeout(r, 600));
  await page.click("#initiate");
  await new Promise(r => setTimeout(r, DUR * 1000));    // 12 phases x 560ms + verdict dwell
  await recorder.stop();
  await browser.close();
  const r = spawnSync("ffmpeg", ["-y", "-i", TMP, "-vf", "fps=30,scale=1920:1080,format=yuv420p",
    "-c:v", "libx264", "-preset", "medium", "-crf", "19", OUT], { stdio: "inherit" });
  fs.rmSync(TMP, { force: true });
  if (r.status !== 0) process.exit(1);
  console.log("out ->", OUT);
})().catch(e => { console.error(e); process.exit(1); });
