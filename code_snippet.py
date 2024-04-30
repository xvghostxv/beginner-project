''''
If you used naming like this ["python file.py"] again I will k!ll you 

'''
def get_user_input():
    while True:
        try:
            user_input = input("Enter a number: ")
            return float(user_input)
        except ValueError:
            print("Invalid input...please enter a numeric value")

def get_operation():
    while True:
        try:
            operation = input("Enter operation type (+, -, /, *): ")
            if operation in ("+", "-", "/", "*"):
                return operation
            else:
                raise ValueError
        except ValueError:
            print("Invalid operation type...please enter (+, -, /, *)")


def is_user_wants_to_continue():
    while True:
        try:
            user_input = input("Welcome to the math calculator, Do you want to continue? (y/n): ")
            if user_input in ("y", "n"):
                if user_input == "n":
                    print("Thank you for using the calculator!")
                    return False
                elif user_input == "y":
                    return True
            else:
                raise ValueError
        except ValueError:
            print("Invalid input...please enter (y, n)")

if __name__ == "__main__":
    while is_user_wants_to_continue():

        first_number = get_user_input()
        second_number = get_user_input()
        operation = get_operation()
        result = eval(f"{first_number} {operation} {second_number}")
        print("Result is:", result) if result is not None else print("Unexpected Error")

        
        
