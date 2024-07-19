<<<<<<< Updated upstream
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
=======
from typing import TypeVar, Generic, List, Optional
from enum import Enum

CellType = int | str | float | bool | None


# class Table[R: DefaultRow[DefaultCell], C: DefaultCell]:
#     def __init__(self, rows = []):
#         self.rows: list[R] = rows
#         self.max_rows = 0
#         self.max_cols = 0
    
#     # 空の行、列を追加する
#     def add_empty_row(self):
#         row = DefaultRow()
#         self.add_row(row)
    
#     def add_row(self, row: DefaultRow[DefaultCell]):
#         self.rows.append(row)
#         self.max_rows += 1
#         self.max_cols = max(self.max_cols, len(self.rows))


class DefaultRow[C: DefaultCell]:
    def __init__(self, cells: List[C]=[]):
        self.cells = cells
    
    def add_empty_cell(self):
        cell = DefaultCell()
        self.add_cell(cell)
    
    def add_cell(self, cell: C):
        self.cells.append(cell)

class DefaultCell:
    def __init__(self, value: CellType=None):
        self.value = value



>>>>>>> Stashed changes
