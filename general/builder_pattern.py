# -*- coding: utf-8 -*-

from typing import Type


class Animal:
    def __init__(self, builder: "Builder", name: str):
        self.builder = builder
        self.name = name
        self.legs = []

    def add_legs(self, leg_class: Type["Leg"], leg_n: int):
        self.builder.add_legs(self, leg_class, leg_n)


class Leg:
    def __init__(self, length: int = 50):
        self.length = length

    def __repr__(self):
        return f"Leg({self.length}mm)"


class Builder:

    def add_legs(self, animal: Animal, leg_class: Type[Leg], leg_n: int):
        # from animal.default import Animal, Leg

        animal.legs = [leg_class() for _ in range(leg_n)]
        print(f"{animal.name}: {leg_n}本の足を追加しました。")


if __name__ == "__main__":
    builder = Builder()
    pochi = Animal(builder, "Pochi")
    pochi.add_legs(Leg, 4)

    print(pochi.legs)
