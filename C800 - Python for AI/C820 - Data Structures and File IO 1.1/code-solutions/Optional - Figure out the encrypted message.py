# The first line of the file is the shift value. Every letter after that has
# been shifted forward by that amount, so we shift each letter back to decode.

fileObj = open("encrypted_message.txt", "r")
lines = fileObj.readlines()
fileObj.close()

shift = int(lines[0].strip())
encrypted = lines[1].rstrip("\n")

message = ""
for letter in encrypted:
    if letter.isalpha():
        message = message + chr((ord(letter) - ord("a") - shift) % 26 + ord("a"))
    else:
        message = message + letter

print(message)
