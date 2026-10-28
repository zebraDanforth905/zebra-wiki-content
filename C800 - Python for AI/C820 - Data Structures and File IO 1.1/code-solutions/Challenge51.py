import random

palette = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]

canvas = [[random.choice(palette) for _ in range(3)] for _ in range(3)]
for row in canvas:
    print(row)

counts = {}
for row in canvas:
    for color in row:
        if color in counts:
            counts[color] = counts[color] + 1
        else:
            counts[color] = 1

print()
for color in counts:
    print(color + " -> " + str(counts[color]))
