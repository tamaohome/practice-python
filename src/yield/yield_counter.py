# -*- coding: utf-8 -*-


def counter():
    i = 0
    while True:
        yield i
        i += 1


if __name__ == "__main__":
    for i in range(10):
        print(i, end=" ")
