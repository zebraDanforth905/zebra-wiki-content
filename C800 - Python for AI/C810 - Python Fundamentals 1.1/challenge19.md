---
title: "Challenge #19: Strings - Urgent Message"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 19
challenge_type: "regular"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #19: Strings - Urgent Message

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52679

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
