import random
import time

riddles = [
    ["What has to be broken before you can use it?", "An egg"],
    ["I'm tall when I'm young and short when I'm old. What am I?", "A candle"],
    ["What has hands but cannot clap?", "A clock"],
    ["What has a head and a tail but no body?", "A coin"]
]

riddle = random.choice(riddles)
print(riddle[0])

time.sleep(3)

print("The answer is: " + riddle[1])
