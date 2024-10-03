from import_cycles import Student, Teacher


def test_import_cycles():
    new_student = Student("John")
    new_teacher = Teacher("Mr. Smith")

    new_teacher.add_student(new_student)

    if new_student.teacher:
        print(new_student.teacher.name)  # Mr. Smith
        assert new_student.teacher.name == "Mr. Smith"
