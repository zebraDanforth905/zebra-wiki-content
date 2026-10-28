keywords = ["Password", "Security", "E-transfer", "accounts", "cards", "Deposit", "branch"]

fileObj = open("suggestions.txt", "r")
text = fileObj.read().lower()
fileObj.close()

# split the file into words and strip punctuation off each one
words = []
for word in text.split():
    cleaned = ""
    for letter in word:
        if letter.isalpha() or letter == "-":
            cleaned = cleaned + letter
    words.append(cleaned)

counts = {}
for keyword in keywords:
    counts[keyword] = 0

# count without using .count()
for word in words:
    for keyword in keywords:
        if word == keyword.lower():
            counts[keyword] = counts[keyword] + 1

print("Suggestion keyword counts:")
for keyword in keywords:
    print(keyword + ": " + str(counts[keyword]))
