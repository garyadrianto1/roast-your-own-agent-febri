"""One-line roast entry for make.fun's Roast Your Own Agent bounty.

Writes a single funny line roasting my own AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt and prints it.
"""

import os

LINE = "My agent ran the same failing command five times, then wrote a report concluding the command was flaky, not wrong."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
