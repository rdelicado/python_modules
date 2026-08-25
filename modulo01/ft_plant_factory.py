#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self.height = height
        self.days = days

    def show(self):
        print(
            f"{self.name.capitalize()}: "
            f"{self.height}cm, "
            f"{self.days} days old"
        )

    def grow(self, rate: float):
        self.height = round(self.height + rate, 1)

    def age(self):
        self.days += 1


def main():
    p1 = Plant("rose", 25.0, 30)
    p2 = Plant("oak", 200.0, 365)
    p3 = Plant("cactus", 5.0, 90)
    p4 = Plant("sunflower", 80.0, 45)
    p5 = Plant("fern", 15.0, 120)
    plants = [p1, p2, p3, p4, p5]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
