# -*- coding: utf-8 -*-

from import_cycles import Student, Subject


def test_import_cycles():
    math = Subject("Math", 2)

    yoshida = Student("Yoshida")
    yoshida.add_subject(math)

    assert yoshida.subjects[0] == math
