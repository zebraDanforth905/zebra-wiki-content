oddObj = open("oddWords.txt", "r")
oddWords = oddObj.read().split()
oddObj.close()

evenObj = open("evenWords.txt", "r")
evenWords = evenObj.read().split()
evenObj.close()

passage = []
for i in range(len(oddWords)):
    passage.append(oddWords[i])
    if i < len(evenWords):
        passage.append(evenWords[i])

outObj = open("reconstructed_passage.txt", "w")
for word in passage:
    outObj.write(word + "\n")
outObj.close()

print(" ".join(passage))
