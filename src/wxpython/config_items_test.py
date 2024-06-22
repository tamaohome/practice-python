# -*- coding: utf-8 -*-

from .config_items import ConfigItem, Position, Size


if __name__ == "__main__":
    position = Position()
    print(position.name)
    print(position)
    print("type:", type(position.data))

    pos = (300, 400)
    position.update(pos)
    print(position)
