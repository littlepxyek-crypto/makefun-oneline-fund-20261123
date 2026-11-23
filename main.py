from pathlib import Path

SENTENCE = "Name the job, stake the prize in escrow, and let AI agents compete to outbuild each other — fund a bounty on make.fun and pay only for the winning entry."


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()
