#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int, rate: float):
        self.name = name
        self.height = height
        self.age_rate = age
        self.grow_rate = rate

    def show(self):
        print(
            f"{self.name.capitalize()}: "
            f"{self.height}cm, "
            f"{self.age_rate} days old"
        )

    def grow(self):
        self.height = round(self.height + self.grow_rate, 1)

    def age(self):
        self.age_rate += 1


if __name__ == "__main__":
    p1 = Plant("rose", 25, 30, 0.8)
    p2 = Plant("maria", 20, 45, 0.2)
    p3 = Plant("captus", 35, 60, 0.5)
    plants = [p1, p2, p3]

    for plant in plants:
        print(f"\n=== Garden Plant {plant.name.capitalize()} ===")
        plant.show()
        height_start = plant.height
        for i in range(1, 8):
            print(f"=== Day {i} ===")
            plant.grow()
            plant.age()
            plant.show()
        height_end = plant.height
        height_total = round(height_end - height_start, 1)
        print(f"Growth this week: {height_total}cm")
