# Each student ID maps to:
#   a tuple for the birthdate (year, month, day) -> never changes
#   a set for the subjects taken -> no duplicates
#   a list for the books read -> order matters and duplicates are allowed
classroom = {
    "S001": {
        "birthdate": ("2005", "08", "15"),
        "subjects": {"Math", "Science"},
        "books": ["Holes", "Hatchet", "Holes"]
    },
    "S002": {
        "birthdate": ("2006", "01", "30"),
        "subjects": {"English", "Art", "Math"},
        "books": ["Wonder", "Matilda"]
    }
}

for studentId in classroom:
    student = classroom[studentId]
    print("ID: " + studentId +
          ", Birthdate: " + str(student["birthdate"]) +
          ", Subjects: " + str(student["subjects"]) +
          ", Books Read: " + str(student["books"]))
