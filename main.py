#!/usr/bin/env python3
"""Entry program for the make.fun bounty
"Sum up 24 November's world news in one image"
(https://make.fun/bounty/news-image-20261124).

Writes the bundled image to /output/entry.png.

No network access. Deterministic: the program copies the exact bytes
of entry.png, so every run produces byte-identical output.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = "/output"
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def main() -> int:
    if not os.path.isfile(SOURCE):
        print("missing source image: %s" % SOURCE, file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write via a temp file and rename, so a partial write can never
    # leave a corrupt entry.png behind.
    tmp = OUTPUT + ".tmp"
    shutil.copyfile(SOURCE, tmp)
    os.replace(tmp, OUTPUT)
    # Verify the copy is byte-identical so a silent partial write
    # can never pass as a successful run.
    if os.path.getsize(OUTPUT) != os.path.getsize(SOURCE):
        print("output size mismatch", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (OUTPUT, os.path.getsize(OUTPUT)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
