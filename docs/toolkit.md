Python Number System Calculator
A minimal CLI program built using Python to perform number system conversions, addition, and subtraction across binary, decimal, octal, and hexadecimal.

Features
Convert numbers between binary, decimal, octal, and hexadecimal.

Perform addition and subtraction in any chosen base.

Output results in a user‑selected base.

Menu‑driven interface with error handling for invalid inputs.

Built with Python’s simplicity and readability for beginners.

Requirements
Python 3.10+ (Ubuntu: install via sudo apt install python3)

pip (comes with Python)

Editor: VS Code + Python extension

Setup Instructions
bash
# Clone this repository
git clone https://github.com/<your-username>/number_system_calculator
cd number_system_calculator

# Run the app
python3 NumberCalc.py
Program runs interactively in the terminal.

Usage Flow
Choose an operation:

Convert between number systems

Addition

Subtraction

Enter numbers and specify their base (binary/decimal/octal/hexadecimal).

Choose the output base for the result.

View the converted or calculated output.

Example:

Input: 1011 and 110 in binary, operation = addition, output base = hexadecimal.

Output: 11.

Common Issues
Error	Solution
python: not found	Use python3 instead of python.
IndentationError	Ensure consistent spaces; Python enforces indentation strictly.
ValueError: invalid literal	Input must match the chosen base (e.g., binary only allows 0/1).
Unsupported base	Only binary, decimal, octal, or hexadecimal are supported.
References
Python Docs

Learn Python (learnpython.org)

Real Python Tutorials

GeeksforGeeks: Number System Conversion in Python

Author
Built by Jacob Sihul for the Moringa AI Capstone Project using GenAI for setup, debugging, and documentation.