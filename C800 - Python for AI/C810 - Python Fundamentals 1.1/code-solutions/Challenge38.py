shift = int(input("How many positions do you want to shift (1-25)? "))
sentence = input("Enter a sentence (lowercase letters and spaces only): ")

result = ""
for letter in sentence:
    if letter == " ":
        result = result + " "
    else:
        shifted = (ord(letter) - ord("a") + shift) % 26 + ord("a")
        result = result + chr(shifted)

print(result)
