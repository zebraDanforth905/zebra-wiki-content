fileObj = open("questions.txt", "r")
lines = fileObj.readlines()
fileObj.close()

score = 0
for line in lines:
    line = line.strip()
    question = line[:line.index(":")]
    answer = line[line.index(":") + 1:]

    guess = input(question + " ")
    if guess.lower() == answer.lower():
        print("Correct!")
        score = score + 1
    else:
        print("Wrong. The answer was " + answer + ".")

print("You scored " + str(score) + " out of " + str(len(lines)) + ".")
