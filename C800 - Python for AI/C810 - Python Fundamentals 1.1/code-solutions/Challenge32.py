word = input("Please enter a word: ")

result = ""
for letter in word:
    result = result + letter + "-"

# remove the extra dash on the end
print(result[:-1])
