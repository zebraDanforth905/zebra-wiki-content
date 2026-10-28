# Challenge 48: Explain the difference between a global and a local variable.
#
# A global variable is created outside of any function. It can be read from
# anywhere in the program.
#
# A local variable is created inside a function. It only exists while that
# function is running and cannot be used outside of it.

score = 0          # global variable

def play():
    bonus = 10     # local variable, only exists inside play()
    print("Bonus this round:", bonus)
    print("Total score so far:", score)

play()
print("Score is still global:", score)
