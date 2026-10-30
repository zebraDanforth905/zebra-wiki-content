---
title: "Challenge #46: Functions - Driver Speed Evaluation Simulation"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 46
challenge_type: "regular"   # regular | supplemental | discontinued
language: python
tags: [python]
author: "Your Name"
status: draft        # todo | draft | reviewed | final
---

# Challenge #46: Functions - Driver Speed Evaluation Simulation

## Challenge Brief

https://lms.zebrarobotics.com/courses/2576/assignments/52706

## Solutions

```python
import random


# Returns the demerit points for one drive: 1 point per full 10 km/h over the limit
def evaluate_drive(avg_speed, speed_limit):
    if avg_speed <= speed_limit:
        return 0
    return (avg_speed - speed_limit) // 10


def run_driver_simulation():
    print("===== Driver Speed Evaluation Simulation =====")

    speedLimits = [50, 60, 70, 80]
    totalPoints = 0

    drives = int(input("How many drives do you want to evaluate? "))

    for drive in range(drives):
        speedLimit = random.choice(speedLimits)
        driverSpeed = random.randint(speedLimit - 40, speedLimit + 40)
        points = evaluate_drive(driverSpeed, speedLimit)
        totalPoints = totalPoints + points

        print("\nDrive " + str(drive + 1))
        print("Speed limit: " + str(speedLimit))
        print("Driver speed: " + str(driverSpeed))
        print("Demerit points this drive: " + str(points))
        print("Total demerit points: " + str(totalPoints))

        if totalPoints >= 12:
            print("Immediate suspension triggered!")
            print("License suspended. You cannot continue driving.")
            break

    print("\nFinal demerit points: " + str(totalPoints))


run_driver_simulation()
```

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)
