# -*- coding: utf-8 -*-

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import Student


class Subject:
    """授業科目クラス"""

    def __init__(self, name: str, credits: int):
        self._name = name
        self._credits = credits
        self._students: list["Student"] = []

    def add_student(self, student: "Student"):
        self._students.append(student)
        student.subjects.append(self)
