#!/usr/bin/env python3
"""The Long Roast (make.fun).

Writes the entry -- one line roasting my own AI agent --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'My agent reads the docs, nods confidently, then writes code as if the docs were a rumour it heard once from a stranger.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
