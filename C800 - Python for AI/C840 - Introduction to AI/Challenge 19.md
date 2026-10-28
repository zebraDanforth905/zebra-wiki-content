---
title: "Challenge #19: Extracting Information Using Regular Expressions (Regex)"
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

# Challenge #19: Extracting Information Using Regular Expressions (Regex)

## Problem

You are given the following passage:

TECHZONE STORE recently launched several new products, including "SmartWatch Pro", "EcoBottle", "NoiseCancel Headphones", and "UltraLight Laptop", each available at different price points such as $49, $129, $299, $599, and $999. Customers can explore more details on websites like www.techzone.com, www.greenliving.com, www.soundhub.com, and www.laptopworld.com. For inquiries, they can contact support at +11234567890, +19876543210, +14165551234, or +16475559876, or send emails to info@techzone.com, support@greenliving.com, sales@soundhub.com, and help@laptopworld.com. Additional products like "Fitness Tracker", "Wireless Mouse", and "Gaming Keyboard" are also available at prices such as $25, $75, $150, and $220, giving customers a wide range of options to choose from.

New arrivals such as "4K Action Camera", "Bluetooth Speaker", and "Smart Home Hub" are now listed at $180, $60, and $210, and can be found on www.cameratech.com, www.audioworld.com, and www.smarthome.com. Customers may also reach out via +19051234567 and +14375550123 or email contact@cameratech.com and service@smarthome.com for further assistance.

Tasks

• Store the above text passage in a string called "corpus".

• Using Python and Regular Expressions (regex), write a program to extract the following:

• The company name (written in all uppercase at the beginning)

• All phone numbers (format: +1##########)

• All email addresses

• All website URLs (format: www.$$$$$.com)

• All product names (enclosed in double quotes)

• All prices (values starting with $)

• Create a dictionary that links each product to a price.

{
    "SmartWatch Pro": 49,
    "EcoBottle": 129
}

## Solutions

```python
# Add solution(s) here
```

You can include multiple approaches in this section if needed.

## Explanation

<!-- Explain in a few sentences why the solution works. -->

## Common Mistakes (optional)

## Additional Resources (optional)

- http://www.$$$$$.com/
