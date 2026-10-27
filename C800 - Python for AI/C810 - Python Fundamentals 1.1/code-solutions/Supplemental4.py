howMany = int(input("How many grades do you have? "))

total = 0
for i in range(howMany):
    grade = float(input("Enter a grade: "))
    total = total + grade

average = total / howMany
print("Your average grade is " + str(average))
