numbers = [3, 6, 9, 12, 15]

# Approach A - a lambda inside a list comprehension
transform = lambda n: n * 2 if n % 2 == 0 else n
resultA = [transform(n) for n in numbers]

# Approach B - a list comprehension with a conditional expression (no lambda)
resultB = [n * 2 if n % 2 == 0 else n for n in numbers]

print("Original:    " + str(numbers))
print("Approach A:  " + str(resultA))
print("Approach B:  " + str(resultB))
