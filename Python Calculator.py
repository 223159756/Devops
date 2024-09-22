import os
from operator import add, sub, mul

def calc():
    # Get the operator, number 1, and number 2 from environment variables
    op = os.getenv("OPERATOR", "+")  # Default to '+'
    n1 = int(os.getenv("NUMBER1", 0))  # Default to 0
    n2 = int(os.getenv("NUMBER2", 0))  # Default to 0

    operators = {'+': add(n1, n2), '-': sub(n1, n2), '*': mul(n1, n2)}
    if op in operators:
        print('{} {} {} = {}'.format(n1, op, n2, operators[op]))
    else:
        print("Invalid operator: ", op)

def menu():
    # Get the choice from environment variables (defaults to '1' to calculate)
    choice = os.getenv("CHOICE", "1").lower()
    if choice == '1':
        calc()
    elif choice == 'q':
        print("Quitting...")
        return False
    else:
        print('Not a correct choice: <{}>, try again'.format(choice))

if __name__ == '__main__':
    menu()
