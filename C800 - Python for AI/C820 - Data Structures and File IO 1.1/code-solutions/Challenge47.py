# Challenge 47: Explain the difference between a parameter and an argument.
#
# A parameter is the name listed in a function's definition. It is a
# placeholder for the value the function will receive.
#
# An argument is the actual value you pass to the function when you call it.
#
# In the example below, "name" is the parameter and "Sam" is the argument.

def greet(name):       # name is the PARAMETER
    print("Hello, " + name)

greet("Sam")           # "Sam" is the ARGUMENT
