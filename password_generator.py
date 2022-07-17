# This is the starting template for a password generate that I will work on to add more features.

# Imports for program.
import random

# Lists to store possible values.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message and getting input from user.
print("Welcome to the PyPassword Generator!")

while(True):
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

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

    # Prints off password before it is shuffled.
    print(f"Password before shuffle: {password}")

    # Password is converted to a list then shuffled then joined back into a string.
    password_list = list(password)
    shuffled_password = random.shuffle(password_list)
    joined_password = "".join(password_list)

    # Print off final password.
    print(f"Password after shuffle: {joined_password}")

    generate_new_password = input("Do you wish to generator a new password, type 'y' for yes or 'n' for no.").lower()

    if generate_new_password == "n":
        print("Thank you for using the password generator.\nbrought to you by Namrods.")
        break
