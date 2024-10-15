# -*- coding: utf-8 -*-

# from collections.abc import ItemsView, ValuesView
from typing import Tuple
from collections import UserDict

CoordinateType = Tuple[int | str, int | str]


class ConfigItem(UserDict):
    name: str = ""


class Position(ConfigItem):
    name = "Window Position"

    def __init__(self, position: CoordinateType = (0, 0)):
        super().__init__()
        x, y = position
        self.data = {"x": int(x), "y": int(y)}
    
    def update(self, position: CoordinateType):
        x, y = position
        self.data["x"] = int(x)
        self.data["y"] = int(y)

    # @property
    # def x(self):
    #     return self.data["x"]

    # @property
    # def y(self):
    #     return self.data["y"]


class Size(ConfigItem):
    name = "Window Size"

    def __init__(self, size: CoordinateType = (0, 0)):
        super().__init__()
        width, height = size
        self.data = {"width": int(width), "height": int(height)}
    
    def update(self, size: CoordinateType):
        width, height = size
        self.data["width"] = int(width)
        self.data["height"] = int(height)

    # @property
    # def width(self):
    #     return self.data["width"]

    # @property
    # def height(self):
    #     return self.data["height"]
