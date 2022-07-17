# This is the starting template for a password generate that I will work on to add more features.

# Imports for program.
import random

# Lists to store possible values.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message and getting input from user.
print("Welcome to the PyPassword Generator!")


# Function to generate the password.
def generate_password(letters, numbers, symbols):
    nr_letters, nr_symbols, nr_numbers = validate_input()

    # Variable to store password.
    password = ""

    # Each for loop loops through the lists and randomly takes values from each list depending on amount entered by user.
    for letter in range(nr_letters):
        random_letter = random.choice(letters)
        password += random_letter

    for symbol in range(nr_symbols):
        random_symbol = random.choice(symbols)
        password += random_symbol

    for number in range(nr_numbers):
        random_number = random.choice(numbers)
        password += random_number
        
    return password


def validate_input():
    try:
        nr_letters = int(input("How many letters would you like in your password?\n")) 
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))
        
        return nr_letters,nr_symbols,nr_numbers
    except ValueError:
        print("Please only enter the number or letters, symbols or numbers you wish to generate, e.g. type '5' if you would like '5' letters in your password.")
        validate_input()
    
    return nr_letters,nr_symbols,nr_numbers


# Function that suffles the password into random order.
def shuffle_password(password):
    # Password is converted to a list then shuffled then joined back into a string.
    password_list = list(password)
    shuffled_password = random.shuffle(password_list)
    joined_password = "".join(password_list)

    return joined_password


# Prints off menu for the user to select and option from.
def menu():
    user_choice = input("""
    Please type the number associated with your selection.

    1. Generate password.
    2. Display unshuffled password.
    3. Display shuffled password.
    4. Exit program.
    Enter your choice: """)

    return user_choice

# While loop which will keep running until exited via the menu.
while(True):

    # Stores the users selected option.
    user_selection = menu()
    
    # Checks the users option then performs the option that has been selected by the user.
    if user_selection == "1":
        password = generate_password(letters, numbers, symbols)
    elif user_selection == "2":
        # Prints off password before it is shuffled.
        print(f"\n\tPassword before shuffle: {password}") 
    elif user_selection == "3":
        # Calls shuffle_password to shuffle the password then joins it back into a string version of the password.
        joined_password = shuffle_password(password)
        # Print off final password.
        print(f"\n\tPassword after shuffle: {joined_password}")
    elif user_selection == "4":
        print("Thank you for using the password generator.\nBrought to you by Namrods.")
        break
    else:
        print("Please only type options 1 - 4 as a number, e.g type '1' for option 1.")
