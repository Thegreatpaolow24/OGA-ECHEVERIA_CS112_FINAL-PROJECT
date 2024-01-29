# Welcome to the Para sa gwapo Calculator
# This program performs basic arithmetic operations

class Calculator:
    # Class for basic arithmetic operations

    def add(self, num1, num2):
        # Method to perform addition
        return int(num1 + num2)

    def subtract(self, num1, num2):
        # Method to perform subtraction
        return int(num1 - num2)

    def multiply(self, num1, num2):
        # Method to perform multiplication
        return int(num1 * num2)

    def divide(self, num1, num2):
        # Method to perform division
        if num2 == 0:
            raise ValueError("Error: Division by zero is not allowed.")
        return int(num1 / num2)

    def exponentiate(self, num1, num2):
        # Method to perform exponentiation
        return int(num1 ** num2)


def get_user_input():
    # Function to get user input for the desired operation
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'exponent' for exponentiation")
    print("Enter 'quit' to end the program")

    return input(": ")


def get_user_numbers():
    # Function to get user input for two numbers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return num1, num2


def main():
    # Main program execution
    calculator = Calculator()

    while True:
        # Welcome message and user prompt
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'exponent' for exponentiation")
        print("Enter 'quit' to end the program")

        # Get user's choice of operation
        user_input = get_user_input()

        if user_input == "quit":
            # Quit the program
            print("Thank you for using the Para sa gwapo Calculator. mwa!")
            break
        elif user_input in ["add", "subtract", "multiply", "divide", "exponent"]:
            # Get user's numbers
            num1, num2 = get_user_numbers()

            if user_input == "add":
                # Perform addition
                result = calculator.add(num1, num2)
            elif user_input == "subtract":
                # Perform subtraction
                result = calculator.subtract(num1, num2)
            elif user_input == "multiply":
                # Perform multiplication
                result = calculator.multiply(num1, num2)
            elif user_input == "divide":
                try:
                    # Perform division
                    result = calculator.divide(num1, num2)
                except ValueError as e:
                    print(e)
                    continue
            elif user_input == "exponent":
                # Perform exponentiation
                result = calculator.exponentiate(num1, num2)

            # Display the result
            print(f"Result: {num1} {user_input} {num2} = {result}")
        else:
            # Handle invalid input
            print("Invalid input. Please enter a valid option.")

    # End of the program


if __name__ == "__main__":
    # Run the main program
    main()
