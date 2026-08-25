#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.height}cm, "
            f"{self.days} days old"
        )

    def grow(self, rate: float) -> None:
        self.height = round(self.height + rate, 1)

    def age(self) -> None:
        self.days += 1


def main() -> None:
    p1 = Plant("rose", 25.0, 30)

    print("=== Garden Plant Growth ===")
    p1.show()
    height_start = p1.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        p1.grow(0.8)
        p1.age()
        p1.show()
    height_end = p1.height
    height_total = round(height_end - height_start, 1)
    print(f"Growth this week: {height_total}cm")


if __name__ == "__main__":
    main()
