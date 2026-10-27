---
title: "Challenge #19: Strings - Urgent Message"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 19
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #19: Strings - Urgent Message

## Problem

A program is needed to check if the message sent is an urgent message.

• Get input from the user, which is a message.

• Print the length of the message.

• Remove all leading and trailing spaces from the message.

• Print the length of the message again, after the spaces are removed.

• Check if the message contains “911” and print out at which index it does; if not print -1.

## Solutions

```python
message = input("Enter your message: ")

print("Your message is " + str(len(message)) + " characters long.")

message = message.replace(" ", "")
print("Without spaces: " + message)

if "urgent" in message.lower():
    print("This is an urgent message!")
else:
    print("This is not an urgent message.")
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)
