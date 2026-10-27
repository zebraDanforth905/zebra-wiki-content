---
title: "Challenge #46: Functions - Driver Speed Evaluation Simulation"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 46
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #46: Functions - Driver Speed Evaluation Simulation

## Problem

In this challenge, you will build a program that simulates multiple driving events and calculates demerit points based on how fast a driver travels compared to a randomly selected speed limit.

Your solution will include two functions:

Function 1 (helper function): evaluate_drive(avg_speed, speed_limit)

Purpose

Evaluates a driver’s average speed against a given speed limit, and returns the number of demerit points earned.

Rules

• If the driver’s speed is within or below the speed limit, return 0 points.

• If the driver exceeds the speed limit:

• Award 1 demerit point for every 10 km/h over the speed limit
(e.g., 15 km/h over → 1 point; 25 km/h over → 2 points)

Return Value

•
An integer representing the number of demerit points.

Function 2 (primary function): run_driver_simluation()

Purpose

Runs a full simulation of multiple driving events, using evaluate_drive() to determine the demerit points for each drive.

Steps

• Display a simulation header.

• Create a list of possible speed limits:[50, 60, 70, 80]

• Ask the user how many drives they want to evaluate.

• For each simulated drive:

•

• Randomly choose a speed limit from the list using random.choice().

• Randomly generate the driver’s speed (within ±40 km/h of the speed limit).

• Pass both values to evaluate_drive() and get the demerit points.

• Add the returned demerit points to a running total.

• Print:

• Speed limit

• Driver speed

• Demerit points from the drive

• Total accumulated demerit points

• If total demerit points reach 12 or more, stop the simulation immediately and print:

•

• "Immediate suspension triggered!"

• "License suspended. You cannot continue driving."

• After all drives finish (or an early stop), print the final result.

Program Execution

At the end of the file, call:

run_driver_simluation()

to start the simulation.

Hints

random.choice()

random.choice(sequence) selects one random element from a list (or any sequence).

Example:

speed_limits = [50, 60, 70, 80]
speed_limit = random.choice(speed_limits)

This will randomly assign one of the values (50, 60, 70, or 80) to speed_limit each time it is called.

This allows every simulated drive to have a different speed limit.

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
