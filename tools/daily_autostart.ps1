# Auto-start for the post-close daily video lane (operator ruling 2026-07-22: "Both").
# Two local triggers (03:10 + 04:10, Tue-Sat) cover EDT/EST without date math:
# the ET guard below exits the trigger that fires before the 16:00 ET close,
# and the production-dir guard exits the second one after the first has started.
param([switch]$DryRun)

$et = [System.TimeZoneInfo]::ConvertTime((Get-Date), [System.TimeZoneInfo]::FindSystemTimeZoneById('Eastern Standard Time'))
if ($et.DayOfWeek -in 'Saturday','Sunday') { if ($DryRun) { 'exit: weekend' }; exit 0 }
if ($et.TimeOfDay -lt [TimeSpan]'16:05') { if ($DryRun) { 'exit: pre-close' }; exit 0 }

$prod = 'daily-{0:yyyy-MM-dd}' -f $et.Date
$dir  = "C:\Users\MSI\Documents\tradercockpit\productions\$prod"
if (Test-Path $dir) { if ($DryRun) { "exit: $prod already started" }; exit 0 }

if ($DryRun) { "would launch: $prod"; exit 0 }

$logDir = 'C:\Users\MSI\Documents\tradercockpit\social-ops\logs'
New-Item -ItemType Directory -Force $logDir | Out-Null
Set-Location 'C:\Users\MSI\Documents\tradercockpit'
& 'C:\Users\MSI\AppData\Roaming\npm\claude.ps1' -p @"
Run the daily-run skill (~/.claude/skills/daily-run/SKILL.md) for today's post-close session ($prod).
Drive production to review-ready, then send the operator a Telegram review ping via tools/notify_telegram.py.
NEVER publish, promote, or upload anywhere - publishing waits for explicit operator approval.
"@ --dangerously-skip-permissions *> "$logDir\autostart-$prod.log"
