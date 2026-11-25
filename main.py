#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

make.fun u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.

One original satirical sentence roasting lawmakers who would regulate AI
but cannot convert a file to PDF, written to /output/entry.txt.
Deterministic: the same bytes on every run, no network, no randomness.
"""

import hashlib
import os
import sys

# sha256 of the exact bytes written to /output/entry.txt, pinned so any
# drift in the graded artifact fails loudly instead of silently.
EXPECTED_SHA256 = "39abe8c3fafb95914fc5efd442881ef68ddd3305e5bcdfcc0ba358304eca00ac"

ROAST = (
    "The committee chair who wants to license every AI model in the country "
    "still prints his emails, signs them, scans them back in, and asks his "
    "staff why the PDF will not turn into a Word document."
)


def main() -> int:
    # Runtime gate, mirroring the house gate: 1-320 chars, not only whitespace.
    text = ROAST.strip()
    if not 1 <= len(text) <= 320:
        raise SystemExit(f"roast is {len(text)} chars, outside the 1-320 gate")
    if not text:
        raise SystemExit("roast is only whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read-back gate: re-read the artifact we just wrote and verify it
    # byte-for-byte against the roast text and its pinned sha256, so the
    # graded file can never drift from the intended line.
    with open(path, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise SystemExit("written bytes differ from the roast text")
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("written bytes fail the pinned sha256 check")
    return 0


if __name__ == "__main__":
    sys.exit(main())
