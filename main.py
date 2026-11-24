import os

TEXT = "Meet Snooze Insurance: for $4 a month, if your alarm fails, we send a man named Greg to your house to yell your name through the letterbox."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Self-check against the competition gate: UTF-8 text of 1 to 220
    # characters, not only whitespace, bytes exactly TEXT, no trailing newline.
    assert 1 <= len(TEXT) <= 220, "text must be 1-220 characters"
    assert TEXT.strip(), "text must not be only whitespace"
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == TEXT.encode("utf-8"), "written bytes must match TEXT exactly"
    assert not written.endswith(b"\n"), "no trailing newline"


if __name__ == "__main__":
    main()
