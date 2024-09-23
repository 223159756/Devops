"""
This is a simple calculator script that supports basic operations.
"""

import os
from operator import add, sub, mul

def calc():
    """Perform calculation based on environment variables."""
    operation = os.getenv("OPERATOR", "+")  # Default to addition if no operator provided
    num1 = int(os.getenv("NUMBER1", "0"))
    num2 = int(os.getenv("NUMBER2", "0"))
    
    operators = {'+': add(num1, num2), '-': sub(num1, num2), '*': mul(num1, num2)}
    if operation in operators:
        print(f'{num1} {operation} {num2} = {operators[operation]}')
    else:
        print(f"Invalid operator: {operation}")

def menu():
    """Handles menu using environment variable."""
    choice = os.getenv("CHOICE", "1").lower()  # Default to option 1 (calculation)
    if choice == '1':
        calc()
    elif choice == 'q':
        return False
    else:
        print(f'Invalid choice: {choice}')

if __name__ == '__main__':
    menu()
