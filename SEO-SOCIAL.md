# Instagram + TikTok — connection & profile SEO

## Connect Instagram (pipeline leg already built — needs 3 values from you)

Prereq: IG account switched to **Professional (Creator/Business)** and linked to a
Facebook Page (IG app → Settings → Account type; then Accounts Center → link Page).

1. developers.facebook.com → Create App (type: Business) → note **App ID + App Secret**.
2. Graph API Explorer → your app → generate **User Token** with these 6 permissions:
   `pages_show_list, pages_read_engagement, pages_manage_posts, publish_video,
   instagram_basic, instagram_content_publish`.
3. Paste all 3 here — I run `tools/meta_setup.py` and the IG + FB Reels legs go live
   in `publish.py` (B2 staging already verified).

## Connect TikTok (two routes, no free direct one)

- **Route A — Postiz (recommended, already vendored `postiz/`):**
  1. developers.tiktok.com → register app → add **Login Kit + Content Posting API**
     → note Client Key + Secret (TikTok reviews the app; sandbox posts = private
     until audit passes, ~days).
  2. Blocked locally until Docker exists (install needs a reboot — after batv3).
     Then: `postiz/.env` ← TIKTOK_CLIENT_ID/SECRET, `docker compose up -d`,
     connect the account at localhost:4007, publish/schedule from there.
- **Route B — manual (works today):** produce.py shorts land in
  `studio-kit/clipper/output/` → post from phone. Caption files sit next to clips.

## Profile SEO — Instagram (@handle: get `tradercockpit`; fallback `thetradercockpit`)

- **Name field** (searchable, ≠ handle): `TraderCockpit | Trading Strategy Tester`
  — "trading strategy" in the name field is the biggest IG-search lever.
- **Bio:**
  > I execute trading strategies. 12 phases of statistical torture.
  > ICT couldn't even enter. ⚙️ 0 validated — on purpose.
  > 🧪 Run the gauntlet ⬇
- **Link:** https://javin23863.github.io/soical/
- Category: Science, Technology & Engineering. Reels-first; covers = HUD frames
  with 3–4-word hooks; pin the 3 best-performing Reels.
- Hashtag mix per Reel (5–8): #trading #quanttrading #backtesting #ict
  #smartmoneyconcepts #algotrading + 1–2 video-specific.

## Profile SEO — TikTok (@handle: `tradercockpit`)

- **Name:** `TraderCockpit — Strategy Executioner`
- **Bio (80 chars):** `I test trading strategies to death. 12 phases. 0 mercy. Gauntlet ⬇`
- Link in bio (needs 1k followers for clickable — put URL as text + in comments until then).
- TikTok SEO = SPOKEN + on-screen + caption keywords ("ICT strategy tested",
  "backtest") — the machine VO already says them; captions burned by produce.py
  cover on-screen. Caption: hook line + 3–4 hashtags (#ict #trading #backtesting #ai).
- Post the SAME 9:16 renders as YT Shorts/IG Reels (one render, 4 platforms).

## Cross-platform rules

- Handle consistency: tradercockpit everywhere (or thetradercockpit everywhere).
- Every profile links the landing page; landing page JSON-LD `sameAs` lists all
  profiles (YouTube already in; add IG/TikTok URLs once created).
- First 5–8 posts: the shorts cut from video #1 (cold open / horoscope line /
  refused-receipt) — same starving-audience hooks, per-platform captions.
