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


def main() -> None:
    p1 = Plant("rose", 30, 12)
    p2 = Plant("jose", 30, 45)
    p3 = Plant("maria", 23, 23)
    plants = [p1, p2, p3]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.show()


if __name__ == "__main__":
    main()
