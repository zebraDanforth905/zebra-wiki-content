sentence = input("Enter a sentence: ")

result = ""
i = 0
while i < len(sentence):
    if sentence[i] not in "aeiou":
        result = result + sentence[i]
    i = i + 1

print(result)
