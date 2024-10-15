# -*- coding: utf-8 -*-

# UserDictを継承したクラスのサンプル

from collections import UserDict


class MyDict(UserDict):
    def __init__(self):
        super().__init__()

    def add_item(self, key, value):
        self.data[key] = value

    def remove_item(self, key):
        del self.data[key]


if __name__ == "__main__":
    my_dict = MyDict()
    my_dict.add_item("food", "ice cream")
    my_dict.add_item("drink", "coffee")

    print(my_dict.data)
    print("要素数:", len(my_dict))
    
