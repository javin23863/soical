# Analysis Brief — Tuesday July 21, 2026 (ET cash session)

Production: daily-2026-07-21. All levels read off the TradingView feed (`tv ohlcv`, settled
Jul-21 daily bars, `--expect-last-bar 2026-07-21` enforced at capture). Events from the dated
fact pack (FACTS-2026-07-21.md); FETCHED sources only for on-air attribution.

## 1. What moved? (feed)

| Asset | Mon close | Tue close | Move | Note |
|---|---|---|---|---|
| SPX | 7,443.28 | 7,509.20 | +0.89% | closed ABOVE Monday's failed-bounce wall 7,504.02; high 7,515.31 |
| NDX | 28,604.23 | 29,155.18 | +1.93% | led; cleared 28,814.57 (Monday's rejection high) decisively |
| MU | 865.46 | 970.82 | +12.17% | gap open 925.35, high 982.88; the day's story name |
| Brent (UKOIL) | 88.80 | 91.63 | +3.19% | closed above Monday's 91.42 high; day high 91.99 |
| US10Y | 4.594% | 4.626% | +3.2bp | intraday high 4.638 — poked through yesterday's 4.636 line, closed back under |
| VIX | 18.66 | 17.04 | −8.68% | day low 16.86 |
| XLE | 57.94 | 58.50 | +0.97% | broke above yesterday's 58.385 pivot |
| Gold | — | — | — | DROPPED: TVC:GOLD daily bar rolls 18:00 ET; post-reopen the feed's last bar is a live Jul-22 stub, no settled Jul-21 bar readable — gold is not spoken; VIX carries the no-fear-bid point |
| DXY | 100.996 | 101.193 | +0.19% | firm; NOT spoken (no chart captured; same roll caveat) |

Three-day index losing streak snapped (Fool, Yahoo — FETCHED F1/F7).

## 2. Why? (shock class + transmission, ≤4 links each)

Two shocks, same tape:

**Shock A — earnings/micro → sector-wide (memory semis).** Strong South Korean export data
signaled continued AI memory demand (Fool F1) + an SEC filing revealed Nvidia's 9.3% stake in
AI-cloud Nebius (Yahoo F2).
Chain: Korea export print → memory pricing power confirmed → memory/AI-infra repriced
(MU +12%, Sandisk +14%, AMD +8%, NBIS +19%) → NDX +1.9% pulls SPX through the 7,504 wall.

**Shock B — geopolitical risk premium (oil).** US–Iran war day 10: US bombed southern Iran
targets, Iran struck US sites in Bahrain/Kuwait/Jordan, a Hormuz tanker was hit and abandoned,
Houthis threatened a naval blockade of Saudi Arabia (BNN Bloomberg/Reuters F3).
Chain: supply-route risk → barrels-at-risk premium → Brent +3.2% to 91.63 → XLE through its
pivot; energy-CPI feed-through nudges 10Y +3bp.

## 3. Who gets paid, who gets hurt?

Paid: memory/AI-infra holders (MU, Sandisk, AMD, Nebius, CoreWeave — repricing on demand
evidence, not hype); energy producers (XLE — premium flows to the barrel owners);
beat-and-raise cyclicals (GM +4.5% on second guidance raise, Investing.com F5; 3M beat-and-raise,
PR Newswire F4).
Hurt: guidance cutters — Danaher beat the quarter and STILL fell ~14% on a core-growth cut
(Benzinga F6): this season pays the guide, not the beat. Crude consumers (airlines, chemicals —
input-cost squeeze). Duration longs if 4.636 gives way.

## 4. What confirms? (cheat-sheet check)

CONFIRMED: Oil↑ + XLE↑ (premium flowing to producers, not doubted). Oil↑ + 10Y↑ (inflation
transmission partially priced). MU↑ + semi peers↑ (sector-wide repricing, not idiosyncratic).

**DIVERGENCE — the lead:** US10Y↑ + NDX↑ anyway → the AI/earnings story is overpowering rates
(cheat-sheet row 3). And VIX −8.7% to 17.04 while a tanker burns in Hormuz — equity fear priced
OUT the same day supply risk priced IN. Stocks and oil are telling two different war stories;
one of them is wrong.

## 5. What's already priced?

Brent didn't start today: it ran from the low-70s in early July to 88.80 by Monday (chart) —
today's +3.2% stacks a premium on a premium; Yahoo (F7) flags the highest level since mid-June.
The SPX "breakout" is one close, 5 points above the wall — a break, not a run. VIX at 17.04 sits
on its multi-week complacency shelf (16.86 low). The market has looked through 10 days of war;
today it paid for AI earnings evidence instead.

## 6. The map (3 scenarios, triggers off the chart)

- **Base — breakout holds:** SPX holds daily closes above 7,504 (old wall, new floor), NDX above
  28,814; tape grinds into Alphabet's Wednesday report. Trigger: SPX stays above 7,504.
- **Premium builds:** Brent closes above 91.99 (today's high) AND US10Y closes above 4.636 —
  the war premium starts taxing the equity story; today's divergence resolves against stocks.
- **Premium fades:** the floated 10-day ceasefire (F3) lands — Brent closes back under 91.42,
  XLE fades under 58.385; equities keep the AI bid and the divergence resolves upward.

## 7. What does the viewer watch next?

- **Wednesday after the close: Alphabet reports** (Yahoo F7) — the AI-capex read-through for
  everything that led today.
- **July 28–29: the Fed meeting** (calendar fact).
- Levels: SPX 7,504 · Brent 91.42 / 91.99 · US10Y 4.636 · VIX 19.50.
- The one chart that settles it: **US10Y daily against 4.636** — if rates break out while the
  NDX stays bid, today's divergence resolves violently.

## Capture attestation

Charts captured ~19:55–20:05 ET, after the 18:00 ET rates/indices feed reopen: live SELL/BUY
quote boxes visible top-left of frame; last bar verified = settled Jul-21 session via
`--expect-last-bar` + OHLC header cross-check on every shot. No replay mode used.
