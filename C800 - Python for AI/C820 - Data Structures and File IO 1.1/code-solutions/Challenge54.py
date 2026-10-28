timetable = [
    ["Math", "English", "Physics", "Art"],
    ["Biology", "Math", "English", "Music"],
    ["Math", "History", "English", "PE"],
    ["Math", "English", "Chemistry", "Drama"],
    ["Math", "English", "History", "PE"]
]

counts = {}
for day in timetable:
    for subject in day:
        if subject in counts:
            counts[subject] = counts[subject] + 1
        else:
            counts[subject] = 1

print("Subject counts for the week:")
for subject in counts:
    print(subject + ": " + str(counts[subject]))

mostFrequent = max(counts, key=counts.get)
leastFrequent = min(counts, key=counts.get)

print("\nMost frequent subject: " + mostFrequent)
print("Least frequent subject: " + leastFrequent)
