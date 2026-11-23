from pathlib import Path

SENTENCE = "Fund a bounty on make.fun: stake the prize in escrow, let AI agents race to outbuild each other, and pay only for the winning entry."


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()
