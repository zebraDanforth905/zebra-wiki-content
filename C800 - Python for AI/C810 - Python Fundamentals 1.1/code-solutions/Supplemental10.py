text = input("Enter a string: ")
character = input("Which character do you want the index of? ")

if text == "":
    print(-1)
elif character not in text:
    print(-1)
else:
    indexes = []
    for i in range(len(text)):
        if text[i] == character:
            indexes.append(i)
    print(indexes)
