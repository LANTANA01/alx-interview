
# 0x04-utf8_validation

This project focuses on validating UTF-8 encoded data. The goal is to determine whether a given data set represents a valid UTF-8 encoding. Here are the key points you'll need to cover in your README:

## Project Overview

The `0x04-utf8_validation` project aims to implement a method that checks whether a provided data set adheres to the UTF-8 encoding rules. Specifically, we'll be working with the following requirements:

1. A character in UTF-8 can be 1 to 4 bytes long.
2. The data set can contain multiple characters.
3. The data will be represented by a list of integers, where each integer represents 1 byte of data (so we only need to handle the 8 least significant bits of each integer).

## Prerequisites

Before diving into the project, make sure you're familiar with the following concepts:

- **Bitwise Operations in Python**: Understand how to manipulate bits using operations like AND (&), OR (|), XOR (^), NOT (~), and shifts (<<, >>).
- **UTF-8 Encoding Scheme**: Know the rules for encoding characters into one or more bytes in UTF-8. You'll need to recognize patterns that represent valid UTF-8 encoded characters.
- **Data Representation**: Be comfortable working with data at the byte level.
- **List Manipulation in Python**: Understand how to iterate through lists, access list elements, and use list comprehensions.
- **Boolean Logic**: Apply logical operations to make decisions within your program.

## Project Structure

- Your code should adhere to the PEP 8 style (version 1.7.x).
- All files must be executable.
- A `README.md` file at the root of the project folder is mandatory.

## Usage

To test your implementation, you can use the provided `0-main.py` script. It imports the `validUTF8` function from your code and demonstrates its usage:

```python
#!/usr/bin/python3

from validate_utf8 import validUTF8

data = [65]  # Example data set (you can replace this with your own)
print(validUTF8(data))  # Should print True or False.
