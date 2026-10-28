fileObj = open("corrupted.txt", "r")
text = fileObj.read().strip()
fileObj.close()

# The real message is hidden in the odd-numbered letters
# (the 1st, 3rd, 5th... characters), which are the even indexes.
message = text[::2]
print(message)
