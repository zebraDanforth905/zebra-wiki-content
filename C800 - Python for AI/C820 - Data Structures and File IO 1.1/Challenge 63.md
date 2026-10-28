---
title: "Challenge #63: OOP - Student Marks Portal"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 63
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #63: OOP - Student Marks Portal

## Problem

You will build a Python program called markBook.py that manages student information using:

• A Student class

• A menu-driven console application

• A proper main() entry point

• A marks.txt file that preloads students into the system

This system will serve as a small student-information management portal for school staff.

marks.txt File

Your program must read the initial list of students from a text file named:

marks.txt

The file will contain one student per line, using the format:

first_name, last_name, mark, date_of_birth, student_number, grade, class_number, classes_attended
John, Parker, 85, 2007-04-12, S1001, 10, 10A, 42
Emily, Chen, 92, 2006-11-23, S1002, 11, 11B, 48
Liam, Thompson, 76, 2008-02-05, S1003, 9, 9C, 38
Sophia, Reyes, 88, 2007-09-17, S1004, 10, 10C, 45
Noah, Patel, 67, 2008-06-29, S1005, 9, 9A, 33
Olivia, Martins, 94, 2006-03-14, S1006, 11, 11A, 52

Student Class Requirements

Create a class named Student with the following attributes:

• first_name

• last_name

• mark

• date_of_birth

• student_number

• grade

• class_number

• classes_attended

Also include:

• A constructor (__init__)

• A __str__ or __repr__ method (Ask the coach)

Program Requirements

Your program must:

• Read and parse the marks.txt file

• Store each student as a Student object in a list.

• Display the menu:

===== MarkBook Student Management =====
1) View all students
2) Add a student
3) Update student marks and grade
4) Update attendance count
5) Update any student field
6) Exit

• Use a main() function and include:

if __name__ == "__main__":
    main()

• Allow staff to:

• View all students

• Add a new student

• Update marks + grade

• Update attendance

• Update any field

• Exit the system

Parsing the marks.txt File

Students must:

• Open the file

• Read line by line

• Split values into respective fields.

• Create Student objects once the newline character is reached

## Solutions

```python
# Challenge 63: Student Marks Portal (the assignment calls this file markBook.py)

class Student:
    def __init__(self, first_name, last_name, mark, date_of_birth,
                 student_number, grade, class_number, classes_attended):
        self.first_name = first_name
        self.last_name = last_name
        self.mark = mark
        self.date_of_birth = date_of_birth
        self.student_number = student_number
        self.grade = grade
        self.class_number = class_number
        self.classes_attended = classes_attended

    def __str__(self):
        return (self.first_name + " " + self.last_name +
                " | Mark: " + str(self.mark) +
                " | DOB: " + self.date_of_birth +
                " | Student #: " + self.student_number +
                " | Grade: " + str(self.grade) +
                " | Class: " + self.class_number +
                " | Attendance: " + str(self.classes_attended))


def load_students(fileName):
    students = []
    fileObj = open(fileName, "r")
    for line in fileObj:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(",")
        student = Student(parts[0].strip(), parts[1].strip(), int(parts[2]),
                          parts[3].strip(), parts[4].strip(), int(parts[5]),
                          parts[6].strip(), int(parts[7]))
        students.append(student)
    fileObj.close()
    return students


def find_student(students, number):
    for student in students:
        if student.student_number == number:
            return student
    return None


def main():
    students = load_students("marks.txt")

    option = 0
    while option != 6:
        print("\n      MarkBook Student Management      ")
        print("1) View all students")
        print("2) Add a student")
        print("3) Update student marks and grade")
        print("4) Update attendance count")
        print("5) Update any student field")
        print("6) Exit")
        option = int(input("Choose an option: "))

        if option == 1:
            for student in students:
                print(student)
        elif option == 2:
            student = Student(
                input("First name: "), input("Last name: "), int(input("Mark: ")),
                input("Date of birth: "), input("Student number: "), int(input("Grade: ")),
                input("Class number: "), int(input("Classes attended: ")))
            students.append(student)
        elif option == 3:
            student = find_student(students, input("Student number: "))
            if student is not None:
                student.mark = int(input("New mark: "))
                student.grade = int(input("New grade: "))
            else:
                print("Student not found.")
        elif option == 4:
            student = find_student(students, input("Student number: "))
            if student is not None:
                student.classes_attended = int(input("New attendance count: "))
            else:
                print("Student not found.")
        elif option == 5:
            student = find_student(students, input("Student number: "))
            if student is not None:
                field = input("Which field? ")
                value = input("New value: ")
                setattr(student, field, value)
            else:
                print("Student not found.")
        elif option == 6:
            print("Goodbye!")
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)
