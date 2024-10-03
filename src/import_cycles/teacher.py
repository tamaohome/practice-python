# -*- coding: utf-8 -*-

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import Student


class Teacher:
    def __init__(self, name):
        self.name = name
        self.students: list[Student] = []

    def add_student(self, student: "Student"):
        self.students.append(student)
        student.teacher = self
