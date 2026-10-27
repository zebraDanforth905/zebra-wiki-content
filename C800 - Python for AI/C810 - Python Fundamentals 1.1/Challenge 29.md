---
title: "Challenge #29: Loops - Bottles of Milk"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 29
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #29: Loops - Bottles of Milk

## Problem

Write a Python program that prints the lyrics of the famous “99 Bottles of Milk” song. Your program should:

• Start with 99 bottles of milk on the wall.

• Repeat the verses, counting down by one bottle each time.

• Handle the singular form correctly when there is 1 bottle.

• End with the verse for no more bottles and suggest going to the store to buy more.

Example Output

99 bottles of milk on the wall, 99 bottles of milk.
Take one down and pass it along, 98 bottles of milk on the wall.

...

2 bottles of milk on the wall, 2 bottles of milk.
Take one down and pass it along, 1 bottle of milk on the wall.

1 bottle of milk on the wall, 1 bottle of milk.
Take one down and pass it along, no more bottles of milk on the wall.

No more bottles of milk on the wall, no more bottles of milk.
Go to the store and buy some more, 99 bottles of milk on the wall.

Hints

• Use a loop to count down from 99 to 1.

• Use conditional statements to handle singular vs. plural: "bottle" vs. "bottles".

• Print the final verse after the loop.

## Solutions

```python
bottles = 99

while bottles > 0:
    print(str(bottles) + " bottles of milk on the wall, " + str(bottles) + " bottles of milk.")
    print("Take one down and pass it around, " + str(bottles - 1) + " bottles of milk on the wall.")
    bottles = bottles - 1
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)
