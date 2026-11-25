import os

ENTRY_TEXT = "I asked my agent for one sharp roast and it spent a whole hour researching roasts, then submitted a compliment and asked if I was okay."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
