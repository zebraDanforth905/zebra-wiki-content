---
title: "Challenge #27: Detecting Trained Objects"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 27
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #27: Detecting Trained Objects

## Problem

• Set Up the Environment

• Import OpenCV (cv2)

• Load pre-trained Haar cascade classifiers for face, smile, and car detection

• Use appropriate XML files such as frontal face, smile, and car classifiers

• Detect Faces

• Load an image (e.g., "people.jpg")

• Convert the image to grayscale

• Use detectMultiScale() to detect faces

• Draw rectangles around detected faces

• Display the result

• Detect Smiles

• Use the detected face regions (ROI) to improve smile detection accuracy

• Apply the smile classifier only within each face region

• Draw rectangles around detected smiles

• Display the updated image

• Detect Cars

• Load a different image or video frame (e.g., "traffic.jpg")

• Convert it to grayscale

• Use the car classifier to detect vehicles

• Draw bounding boxes around detected cars

• Display the result

## Solutions

```python
# Add solution(s) here
```

You can include multiple approaches in this section if needed.

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)
