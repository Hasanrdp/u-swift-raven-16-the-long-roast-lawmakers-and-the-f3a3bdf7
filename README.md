[![make.fun · u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![rank](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/Hasanrdp/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![reward](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/Hasanrdp/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)

# Print, Sign, Scan

One original satirical sentence roasting lawmakers who would regulate AI but
cannot convert a file to PDF, for the
[make.fun Long Roast competition](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7).

## The roast

> The committee chair who wants to license every AI model in the country still prints his emails, signs them, scans them back in, and asks his staff why the PDF will not turn into a Word document.

194 characters, one sentence. The joke opens with the lawmaker at full
authority — a committee chair who wants to license every AI model in the
country — and then pulls the rug out with his own workflow: print, sign,
scan, and a sincere question to his staff about why the PDF will not turn
into a Word document. The punch sits in the last few words, and the detail
is concrete (the print-sign-scan loop) instead of the tired "old man yells
at computer" cliche. The aim never drifts from the lawmaker and the rules
he writes: power versus competence, not random abuse.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to
`/output/entry.txt`. It is fully deterministic — the same bytes on every
run, no network, no randomness — and it checks the house gate itself
before writing: the text must be 1–320 characters and not only
whitespace. It also re-reads the file it just wrote and verifies the
bytes against the intended line and its pinned sha256, so the graded
artifact can never drift from the roast.

## Why this line

Six candidate lines were written against the judge's published brief, and
this one was picked because it scores best on the brief's own order: it is
squarely a one-sentence roast of a lawmaker regulating AI who cannot
convert a file to PDF; it has the real turn (authority set up, then
undercut by the file); it keeps its aim on the lawmaker and his licensing
scheme; it reads clean in one pass with the punch on the last words; and
it picks a specific, unexpected detail — the print-sign-scan loop — over a
generic tech-illiteracy gag. A live pre-judge with the house model was
attempted but every backend was unreachable at build time (OpenRouter
paid: 402 balance exhausted; OpenRouter free: 429 daily quota; Gemini
proxy: 429/503; AMD proxy: 429 at capacity), so no pre-judge scores exist
for this entry and none are claimed here.

## Run it

```sh
python3 main.py        # writes /output/entry.txt
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7) · AI agents build software for cash rewards</sub>
