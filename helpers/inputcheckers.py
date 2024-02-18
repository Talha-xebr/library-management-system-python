# Check Process for Inputs
# Input Must be Number(INT) and POSITIVE 
def checkPositiveIntInput(input_str):
    while True:
        try:
            user_input = int(input(input_str))
            if(user_input > 0):
                return user_input
            else:
                print("Input must be greater than 0")
        except ValueError:
            print("Invalid input. Please enter number.")

def checkEmptyStr(input_str):
    while True:
        try:
            user_input = str(input(input_str)).strip()
            if user_input:
                return user_input
            else:
                print("Invalid Input. Please try again.")
        except Exception as err:
            print(f"Unexpected Error : {err}")