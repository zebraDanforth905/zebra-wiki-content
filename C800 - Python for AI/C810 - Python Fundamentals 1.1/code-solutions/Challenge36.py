import random

words = ["python", "turtle", "dragon", "guitar", "planet",
         "rocket", "garden", "pencil", "wizard", "yellow"]

word = random.choice(words)
print("The word has " + str(len(word)) + " letters.")

for attempt in range(5):
    letter = input("Guess a letter: ")
    if letter in word:
        print("Yes! '" + letter + "' is in the word.")
    else:
        print("Sorry, '" + letter + "' is not in the word.")

finalGuess = input("Now guess the whole word: ")
if finalGuess == word:
    print("You win! The word was " + word + ".")
else:
    print("You lose! The word was " + word + ".")
