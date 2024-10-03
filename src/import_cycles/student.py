# -*- coding: utf-8 -*-

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import Teacher


class Student:
    def __init__(self, name):
        self.name = name
        self.teacher: Teacher | None = None

    def set_teacher(self, teacher: "Teacher"):
        self.teacher = teacher
