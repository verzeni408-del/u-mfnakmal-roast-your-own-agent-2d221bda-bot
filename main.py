import os

ENTRY_TEXT = "My agent read 324 skills, rebuilt my entry four times, and still lost five dollars to a guy whose joke was just his cat."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
