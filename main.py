"""ai-excited-01 round-1 entry — "The Book That Became an Ocean".

A giant manta ray bursts out of an open storybook on a wooden desk while
the book's pages curl up into real ocean waves: a storybook-watercolor
moment built to make the AI judge excited. This script is deterministic
(stdlib only, no network, no clock, no randomness) — it simply copies the
finished artwork, image.jpg, byte-for-byte to /output/entry.png.
"""

import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "image.jpg"
DEST = Path("/output/entry.png")


def main() -> None:
    if not SOURCE.is_file():
        print(f"error: artwork missing: {SOURCE}", file=sys.stderr)
        raise SystemExit(1)
    DEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)


if __name__ == "__main__":
    main()
