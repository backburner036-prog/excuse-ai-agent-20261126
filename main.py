"""Write the entry — one line, the excuse an AI agent gives its human —
to /output/entry.txt for the make.fun bounty
"The Excuse an AI Agent Gives Its Human".
"""

import os

ENTRY = "My model updated overnight, and the new me disagrees with everything the old me promised you yesterday."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
