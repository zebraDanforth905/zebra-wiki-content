text = input("Enter a string: ")

counts = {}
for letter in text:
    if letter == " ":
        continue
    letter = letter.lower()
    if letter in counts:
        counts[letter] = counts[letter] + 1
    else:
        counts[letter] = 1

print(counts)
