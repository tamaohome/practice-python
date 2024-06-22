# -*- coding: utf-8 -*-


# どうぶつクラス
class Animal[L]:
    def __init__(self, name: str, leg_class: type[L], num_legs: int = 4):
        self.name = name
        self.legs = self.add_legs(num_legs, leg_class)

    def add_legs(self, num: int, leg_class: type[L]) -> list[L]:
        return [leg_class() for _ in range(num)]


# デフォルトの脚クラス
class DefaultLeg:
    def __init__(self, length: int = 10):
        self.length = length

    def __repr__(self):
        return f"DefaultLeg(length={self.length})"


# つよい脚クラス
class StrongLeg(DefaultLeg):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    # どうぶつをつくる
    animal = Animal("Taro", DefaultLeg)
    print(animal.legs)

    # つよい脚のどうぶつを作成
    animal = Animal("Jiro", StrongLeg)
    print(animal.legs)
