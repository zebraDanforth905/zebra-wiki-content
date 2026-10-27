totalSlices = int(input("How many pizza slices are there? "))
people = int(input("How many people are sharing? "))

each = totalSlices // people
leftOver = totalSlices % people

print("Each person gets " + str(each) + " slices.")
print("There are " + str(leftOver) + " slices left over.")
