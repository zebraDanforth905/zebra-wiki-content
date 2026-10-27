sentence = input("Enter a sentence (lowercase letters and spaces only): ")

result = ""
for letter in sentence:
    if letter == " ":
        result = result + " "
    else:
        shifted = (ord(letter) - ord("a") + 1) % 26 + ord("a")
        result = result + chr(shifted)

print(result)
