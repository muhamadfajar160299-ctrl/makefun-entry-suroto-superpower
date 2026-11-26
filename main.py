"""Write the competition entry to the output directory.

Reads the single-line entry shipped beside this script and copies its
exact bytes to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Standard library only; runs under ``python3 -S``.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(here, "entry.txt"), "rb") as f:
            data = f.read()
    except OSError as exc:
        print(f"cannot read entry.txt: {exc}", file=sys.stderr)
        raise SystemExit(1)
    if not data.strip():
        print("entry.txt is empty", file=sys.stderr)
        raise SystemExit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
            f.write(data)
    except OSError as exc:
        print(f"cannot write output: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
