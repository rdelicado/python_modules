#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self._height = height
        self._days = days

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
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
                f"{self.name.capitalize()}: "
                "Error, height can't be negative\n"
                "Height update rejected"
            )
            return
        self._height = height

    def set_age(self, days: int) -> None:
        if days < 0:
            print(
                f"{self.name.capitalize()}: "
                "Error, age can't be negative\n"
                "Age update rejected"
            )
            return
        self._days = days


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            color: str,
    ) -> None:
        super().__init__(name, height, days)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed is True:
            print(" Rose is blooming beautifully!")
        else:
            print(" Rose has not bloomed yet")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            diameter: float
    ) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter = diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name.capitalize()} now produces a shade "
            f"of {round(self._height, 1)}cm long and "
            f"{round(self.trunk_diameter, 1)}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(
            " Trunk diameter: "
            f"{round(self.trunk_diameter, 1)}cm"
        )


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            harvest_season: str,
    ) -> None:
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, rate: float) -> None:
        super().grow(rate)

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    # Flower
    f1 = Flower("rose", 15.0, 10, "red")
    print(f"=== {type(f1).__name__}")
    f1.show()
    print("[asking the rose bloom]")
    f1.bloom()
    f1.show()
    print()

    # Tree
    f2 = Tree("oak", 200.0, 365, 5.0)
    print(f"=== {type(f2).__name__}")
    f2.show()
    print("[asking the oak to produce shade]")
    f2.produce_shade()
    print()

    # Vegetable
    f3 = Vegetable("tomato", 5.0, 10, "April")
    print(f"=== {type(f3).__name__}")
    f3.show()
    print(f"[make {f3.name} grow and age for 20 days]")
    for i in range(20):
        f3.grow(2.1)
        f3.age()
    f3.show()


if __name__ == "__main__":
    main()
