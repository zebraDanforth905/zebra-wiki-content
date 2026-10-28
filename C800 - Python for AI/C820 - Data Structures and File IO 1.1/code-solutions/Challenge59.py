# Caesar Cipher file encryptor. Reads a file, shifts every letter by a key,
# and writes the encrypted version to a new file.

shift = int(input("How many letters do you want to shift by (1-25)? "))

fileObj = open("secret.txt", "r")
text = fileObj.read()
fileObj.close()

encrypted = ""
for letter in text:
    if letter.isalpha():
        if letter.islower():
            start = ord("a")
        else:
            start = ord("A")
        encrypted = encrypted + chr((ord(letter) - start + shift) % 26 + start)
    else:
        encrypted = encrypted + letter

outObj = open("secret_encrypted.txt", "w")
outObj.write(encrypted)
outObj.close()

print("Encrypted file saved as secret_encrypted.txt")
print(encrypted)
