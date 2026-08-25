#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days


def main() -> None:
    p = Plant("Rose", 30, 12)
    print(
        "== Welcome to My Garden ==\n"
        f"Plant: {p.name.capitalize()}\n"
        f"Height: {p.height}cm "
        f"Age: {p.days} days\n"
        "== End of Program =="
    )


if __name__ == "__main__":
    main()
