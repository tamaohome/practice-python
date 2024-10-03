# -*- coding: utf-8 -*-

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import Subject


class Student:
    def __init__(self, name):
        self._name = name
        self.subjects: list["Subject"] = []

    def add_subject(self, subject: "Subject"):
        subject.add_student(self)

    @property
    def name(self) -> str:
        return self._name
