def number_system_calculator():
    """
    Handles number system conversions, addition, and subtraction.
    Supports Binary (2), Decimal (10), Octal (8), and Hexadecimal (16).
    """

    print("Choose an operation:")
    print("1. Convert between number systems")
    print("2. Addition")
    print("3. Subtraction")

    choice = input("Enter choice (1/2/3): ")

    bases = {
        "binary": 2,
        "decimal": 10,
        "octal": 8,
        "hexadecimal": 16
    }

    if choice == "1":
        num = input("Enter the number: ")
        base_from_name = input("Enter the base of the number (binary/decimal/octal/hexadecimal): ").lower()
        base_to_name = input("Enter the base to convert to (binary/decimal/octal/hexadecimal): ").lower()

        if base_from_name in bases and base_to_name in bases:
            try:
                decimal_value = int(num, bases[base_from_name])
            except ValueError:
                print("Error: Invalid number for the chosen base.")
                return

            if base_to_name == "binary":
                print("Converted:", bin(decimal_value)[2:])
            elif base_to_name == "decimal":
                print("Converted:", decimal_value)
            elif base_to_name == "octal":
                print("Converted:", oct(decimal_value)[2:])
            elif base_to_name == "hexadecimal":
                print("Converted:", hex(decimal_value)[2:].upper())
        else:
            print("Unsupported base!")

    elif choice in ["2", "3"]:
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        base_name = input("Enter the base of the numbers (binary/decimal/octal/hexadecimal): ").lower()
        output_base_name = input("Enter the base for the result (binary/decimal/octal/hexadecimal): ").lower()

        if base_name in bases and output_base_name in bases:
            try:
                val1 = int(num1, bases[base_name])
                val2 = int(num2, bases[base_name])
            except ValueError:
                print("Error: Invalid number for the chosen base.")
                return

            result = val1 + val2 if choice == "2" else val1 - val2

            if output_base_name == "binary":
                formatted_result = bin(result)[2:]
            elif output_base_name == "decimal":
                formatted_result = str(result)
            elif output_base_name == "octal":
                formatted_result = oct(result)[2:]
            elif output_base_name == "hexadecimal":
                formatted_result = hex(result)[2:].upper()

            print(f"Result in {output_base_name}: {formatted_result}")
        else:
            print("Unsupported base!")

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    number_system_calculator()
