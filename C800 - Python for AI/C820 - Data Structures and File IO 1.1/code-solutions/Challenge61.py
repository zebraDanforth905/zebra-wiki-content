fileObj = open("student_marks.txt", "r")
lines = fileObj.readlines()
fileObj.close()

results = []
for line in lines:
    parts = line.split()
    name = parts[0].replace("-", " ")
    marks = []
    for mark in parts[1:]:
        marks.append(int(mark))

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    results.append({
        "name": name,
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest
    })

outObj = open("student_summary.txt", "w")
for student in results:
    line = (student["name"] +
            " | Total: " + str(student["total"]) +
            " | Average: " + str(round(student["average"], 1)) +
            " | Highest: " + str(student["highest"]) +
            " | Lowest: " + str(student["lowest"]))
    print(line)
    outObj.write(line + "\n")
outObj.close()

print("\nSummary written to student_summary.txt")
