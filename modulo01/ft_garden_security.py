#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        self._height = height
        self._days = days

    def show(self) -> None:
        print(
            f"{self._name.capitalize()}: "
            f"{self._height}cm, "
            f"{self._days} days old"
        )

    def grow(self, rate: float) -> None:
        self._height = round(self._height + rate, 1)

    def age(self) -> None:
        self._days += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def set_height(self, height: float) -> None:
        if height < 0:
            print(
                f"{self._name.capitalize()}: "
                "Error, height can't be negative\n"
                "Height update rejected"
            )
            return
        self._height = height

    def set_age(self, days: int) -> None:
        if days < 0:
            print(
                f"{self._name.capitalize()}: "
                "Error, age can't be negative\n"
                "Age update rejected"
            )
            return
        self._days = days


def main() -> None:
    p1 = Plant("Rose", 15.0, 10)
    print(
        "=== Garden Security System ===\n"
        "Plant created: ", end=""
    )
    p1.show()
    p1.set_height(25)
    p1.set_age(30)
    print(
        f"\nHeight updated: {p1.get_height()}cm\n"
        f"Age updated: {p1.get_age()} days\n"
    )
    p1.set_height(-12)
    p1.set_age(-34)
    print("\nCurrent state: ", end="")
    p1.show()


if __name__ == "__main__":
    main()
