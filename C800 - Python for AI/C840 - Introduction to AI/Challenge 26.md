---
title: "Challenge #26: Detecting and Counting Colored Objects (Lego Image)"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 26
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #26: Detecting and Counting Colored Objects (Lego Image)

## Problem

1. Load the Image

•
Use cv2.imread() to open Lego_image.png.

2. Convert to HSV

•
Change the image from BGR to HSV using cv2.cvtColor().

•
HSV helps us find colors more easily.

3. Detect a Color (Example: Red)

•
Define the HSV range for red.

•
Use cv2.inRange() to create a mask

→ Red objects = white, background = black.

4. Clean the Mask

•
Use MORPH_OPEN with cv2.morphologyEx()

→ Removes small white dots (noise).

5. Find Objects (Contours)

•
Use cv2.findContours() to find shapes in the mask.

6. Filter and Count

•
Use cv2.contourArea() to remove very small shapes.

•
Count only the real objects.

7. Show Results

•
Draw circles or outlines on each object.

•
Display the total number of objects.

## Solutions

```python
# Add solution(s) here
```

You can include multiple approaches in this section if needed.

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

- https://dp4rp4tcpuoo1.cloudfront.net/C800/Introduction%20to%20AI/Class%207/8.13%20lego_count.png
