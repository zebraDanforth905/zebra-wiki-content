bottles = 99

while bottles > 0:
    print(str(bottles) + " bottles of milk on the wall, " + str(bottles) + " bottles of milk.")
    print("Take one down and pass it around, " + str(bottles - 1) + " bottles of milk on the wall.")
    bottles = bottles - 1
