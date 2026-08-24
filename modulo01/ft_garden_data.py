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
            f"{self.age} days old")


if __name__ == "__main__":
    p1 = Plant("rose", 30, 12)
    p2 = Plant("jose", 30, 45)
    p3 = Plant("maria", 23, 23)

    p1.show()
    p2.show()
    p3.show()
