#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(
            f"{self.name.capitalize()}: "
            f"{self.height}cm, "
            f"{self.age} days old"
        )


if __name__ == "__main__":
    p1 = Plant("rose", 30, 12)
    p2 = Plant("jose", 30, 45)
    p3 = Plant("maria", 23, 23)
    plants = [p1, p2, p3]

    for plant in plants:
        plant.show()
