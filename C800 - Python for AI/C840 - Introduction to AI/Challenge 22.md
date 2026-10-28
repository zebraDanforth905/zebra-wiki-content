---
title: "Challenge #22: Enhance an Image"
stream: "Python developer"
stream_code: "c800"
course: "Python Fundamentals"
course_code: "c820"
version: "1.1"
challenge: 22
language: "python"
tags: [python]
author: "Your Name"
status: "draft"
challenge_type: "regular"
---

# Challenge #22: Enhance an Image

## Problem

In this challenge, you will learn how to open, modify, and save images using the Pillow library in Python. You will apply multiple image processing techniques and explain what happens at each step.

• Load an Image

• Import Image, ImageEnhance, and ImageFilter from the Pillow library

from PIL import Image, ImageEnhance, ImageFilter

•

• Open ANY image file and store it in a variable

• Display the original image

• Crop the Image

• Crop a specific region using coordinates (left, top, right, bottom)

• Display the cropped image

• Resize the Image

• Resize the image to a new width and height

• Display the resized image

• Rotate the Image

• Rotate the image by a positive angle

• Rotate the image by a negative angle

• Display both rotated versions

• Save Processed Images

• Save the cropped, resized, and rotated images with new file names

• Try saving in a different format such as .png

• Adjust Image Properties

• Create a brightness enhancer and increase brightness

• Create a contrast enhancer and increase contrast

• Create a color enhancer and increase saturation

• Display each enhanced image

• Adjust Transparency (Alpha)

• Convert the image to RGBA mode

• Access pixel data using .load()

• Loop through all pixels and reduce the alpha value

• Display the semi-transparent image

• Apply Filters

• Apply a blur filter and display the result

• Apply a contour filter and display the result

• Apply a sharpen filter and display the result

• Save at least one filtered image

One Final Task:

• Explain to your coach the following:

• Explain how cropping affects the image and whether the original image changes

• Observe and explain what happens if the aspect ratio is not maintained

• Explain the difference between clockwise and counterclockwise rotation

• Explain how the factor value changes the output

• Explain what alpha represents in an image

• Explain how filters modify the appearance without directly editing pixels

## Solutions

```python
# Add solution(s) here
```

You can include multiple approaches in this section if needed.

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)
