# Python Number System Calculator

A lightweight command-line tool built in Python for converting numbers across bases and performing arithmetic operations (addition and subtraction) in binary, decimal, octal, and hexadecimal formats.

## Features

* Convert values between binary, decimal, octal, and hexadecimal
* Add or subtract numbers defined in any supported base
* Display results in a user-selected output base
* Menu-driven interface for intuitive navigation
* Robust input validation and exception handling
* Designed with clarity and readability to support learners transitioning into Python

## Requirements

* Python 3.10 or newer
* Ubuntu installation: `sudo apt install python3`
* pip (bundled with Python installations)
* Recommended editor: Visual Studio Code with the Python extension

## Setup Instructions

```bash
# Clone the repository


# Run the program
python3 NumberCalc.py
The calculator will start interactively in your terminal.

Usage Overview
Select an operation from the menu:

Convert a number between bases

Addition

Subtraction

Enter the numeric values and the base they belong to
(binary, decimal, octal, or hexadecimal)

Select the base in which the result should be displayed

Review the calculated or converted output

Example
Input: 1011 and 110 (binary), operation: addition, output base: hexadecimal
Output: 11

Common Issues and Solutions
Issue	Explanation / Resolution
python: command not found	Use python3 instead of python.
IndentationError	Ensure that all indentation uses spaces consistently.
ValueError: invalid literal	Input must be valid for the specified base (e.g., binary must use only 0 and 1).
Unsupported base	Only binary, decimal, octal, and hexadecimal are implemented.
References
Official Python Documentation

Learn Python (learnpython.org)

Real Python Tutorials

GeeksforGeeks: Number System Conversion Resources

Author
Developed by Jacob Sihul for the Moringa AI Capstone Project with assistance from GenAI for debugging, documentation, and workflow guidance.
