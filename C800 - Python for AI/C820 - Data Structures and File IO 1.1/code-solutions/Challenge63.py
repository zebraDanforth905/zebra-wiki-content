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
