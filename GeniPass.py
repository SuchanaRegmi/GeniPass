""" In our daily lives, we frequently rely on passwords to protect our most sensitive information, like email and bank
account details. The use of secure passwords is necessary in shielding us from unauthorized access and potential
fraudulent activities that could jeopardize our security. A weak password is one that can be easily guessed due to its
simplicity. Such passwords often consist of common words, basic phrases, or predictable sequences such as "password,"
"123456," and lack a diverse mix of characters.

Recognizing the need for stronger password security, we have envisioned Geni-Pass, a secure password generator. This
program is designed to allow users with the ability to tailor their passwords' length and strength according to their
wants and needs. Geni-Pass offers the option to include a mix of uppercase and lowercase letters, numbers, and special
characters. These elements are randomly combined to ensure the generation of a strong password. For instance, if you
require a password incorporating uppercase letters, numbers, and special characters, Geni-Pass will integrate these
elements, producing a strong and reliable password. Moreover, Geni-Pass caters to those who prefer a personal touch in
their password. It allows users to incorporate a specific word of their choice into the password, while still ensuring
the inclusion of a random selection of user-specified characters, maintaining the strength of the password. Our goal
with Geni-Pass is to make the creation of secure passwords straightforward and reliable.
"""
# Importing random module
import random

# Function to validate the length of the password
def validating_length(length_of_pass):
    """ This function checks if the inputted length of the password is valid. It repeatedly prompts the user to input
    a password length until the input they have entered is an integer, and it is at least 8, which is what we have set
    as the minimum length of a strong password.

    Args:
         length_of_pass (str): The desired length of the password gievn by the user.

    Returns:
        int: The validated length of the password.
    """

    while int(length_of_pass) < 8 or not length_of_pass.isdigit():
        print("Password length is too short. Not a strong password length. ")
        length_of_pass = input("How long would you like your password to be? ")

    return int(length_of_pass)


# Function to validate the number of passwords
def validating_num_of_pass(number_of_pass):
    """
    This functipn checks if the inputted number of passwords is valid. This function repeatedly prompts the user until
    the number of passwords entered is an integer and the integer is greater than 0. This ensures that the program will
    generate at least one password.

    Args:
    number_of_passwords (str): The number of passwords the user wants the program to create.

    Returns:
    int: The validated number of passwords to be generated.
    """
    while int(number_of_pass) <= 0 or not number_of_pass.isdigit():
        print("Invalid Input. Try Again.")
        number_of_pass = input("How many passwords would you like? ")

    return int(number_of_pass)

# Generates password
def generate_password():
    """
    This function generates and prints a set of passwords based on user specifications.

    The function prompts the user for three key inputs:
    1. Desired length of the password: Ensures it meets a minimum strength requirement.
    2. Number of passwords to generate: Allows generation of multiple passwords.
    3. Types of characters to include (uppercase, lowercase, numbers, symbols): 
       User can specify a combination of character types for the password.

    The function then iterates to create the specified number of passwords. For each password, it 
    iterates over its length, filling each position with a randomly chosen character from the 
    specified types. The process includes validation of inputs and handling of invalid selections.

    Outputs:
    Each generated password is printed out once it is created.
    """
        
    # Prompts user for desired length of password
    length_of_password = input("How long would you like your password to be? ")
    # Sends the input to the validating_length function
    length_of_password = validating_length(length_of_password)

    # Prompts user for desired number of passwords
    number_of_passwords = input("How many passwords would you like? ")
    # Sends the input to the validating_num_of_pass function
    number_of_passwords = validating_num_of_pass(number_of_passwords)

    # Prompts the user the combination of characters they would like in their password (uppercase characters, lowercase
    # characters, numbers and/or symbols)
    choice_of_chars = input(
        "What would you like in your password? \n Please choose atleast 3 options: uppercase, lowercase, numbers, "
        "symbols (split by commas). ")

    # Converts the input string to lowercase and then splits it into a list of elements, each separated by a comma and space
    choice_of_chars = choice_of_chars.lower().split(", ")

    # Initializing counter and password
    counter = 0
    password = []

    # Initializes the password list with underscores, setting each underscore as a placeholder for a character in the
    # password
    for i in range(int(length_of_password)):
        password += "_"

    # A while loop that iterates until the desired number of passwords have been generated, incrementing the counter each
    # time
    while counter != int(number_of_passwords):
        counter += 1

        # Iterate over the length of the password to replace each _ placeholder with a character
        for i in range(len(password)):

            # Lists representing different character type combinations that the user can select for password composition
            uln_word = ["uppercase", "lowercase", "numbers"]
            uls_word = ["uppercase", "lowercase", "symbols"]
            uns_word = ["uppercase", "numbers", "symbols"]
            lns_word = ["lowercase", "numbers", "symbols"]
            all_word = ["uppercase", "lowercase", "numbers", "symbols"]

            # Checks if the user's choice includes uppercase, lowercase, and numbers. If so, selects a random character from
            # the list of uppercase letters, lowercase letters, and numbers and replaces the _ in the current position in
            # the password.
            if uln_word[0] in choice_of_chars and uln_word[1] in choice_of_chars and uln_word[2] in choice_of_chars:
                password[i] = random.choice(upper_lower_num)
                string = ''.join(password)

            # Checks if the user's choice includes uppercase, lowercase, and symbols. If so, selects a random character from
            # the combined list of uppercase letters, lowercase letters, and special characters and replaces the _ in the
            # current position in the password.
            elif uls_word[0] in choice_of_chars and uls_word[1] in choice_of_chars and uls_word[2] in choice_of_chars:
                password[i] = random.choice(upper_lower_symbols)
                string = ''.join(password)

            # Checks if the user's choice includes uppercase, numbers, and symbols. If so, selects a random character from
            # the combined list of uppercase letters, numbers, and special characters and replaces the _ in the current
            # position in the password.
            elif uns_word[0] in choice_of_chars and uns_word[1] in choice_of_chars and uns_word[2] in choice_of_chars:
                password[i] = random.choice(upper_num_symbols)
                final_password = ''.join(password)

            # Checks if the user's choice includes lowercase, numbers, and symbols. If so, selects a random character from
            # the combined list of lowercase letters, numbers, and special characters and replaces the _ in the current
            # position in the password.
            elif lns_word[0] in choice_of_chars and lns_word[1] in choice_of_chars and lns_word[2] in choice_of_chars:
                password[i] = random.choice(lower_num_symbols)
                final_password = ''.join(password)

            # Checks if the user's choice includes all character types or explicitly chooses 'all'. If so, selects a random
            # character from the combined list of all character types and replaces the _ in the current position in the password.
            elif all_word[0] in choice_of_chars and all_word[1] in choice_of_chars and all_word[2] in choice_of_chars and all_word[3] in choice_of_chars or choice_of_chars == "all":
                password[i] = random.choice(all_choices)
                final_password = ''.join(password)

            # If none of the above conditions are met, the input is considered invalid and the user is prompted to make a
            # valid selection.
            else:
                print("\nInvalid input. Please choose a minimum of 3 from the options provided. ")
                choice_of_chars = input(
                    "What would you like in your password? \n Please choose at least 3 options: uppercase, lowercase, "
                    "numbers, symbols (split by commas). ")
            
        # Concatenates all elements in the 'password' list to form the final password 
        final_password = ''.join(password)
        
        # Outputting the final generated password
        print("Your new generated password is: " + final_password)

# Setting up for program output
print("--- Welcome to GeniPass --- \nLet's help you generate a strong password or multiple if you desire.\n")

# Defining the list of characters to generate randomized passwords
upper_case_alpa = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                   "U", "V", "W", "X", "Y", "Z"]
lower_case_alpa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] * 3
special_characters = ["-", "_", ".", "!", "@", "#", "$", "^", "*"] * 3

# Combines uppercase, lowercase letters, and numbers
upper_lower_num = upper_case_alpa + lower_case_alpa + numbers  
# Combines uppercase letters, numbers, and special characters
upper_num_symbols = upper_case_alpa + numbers + special_characters  
# Combines uppercase and lowercase letters with special characters
upper_lower_symbols = upper_case_alpa + lower_case_alpa + special_characters  
# Combines lowercase letters, numbers, and special characters
lower_num_symbols = lower_case_alpa + numbers + special_characters  
# Combines all character types: uppercase, lowercase, numbers, and special characters
all_choices = upper_case_alpa + lower_case_alpa + numbers + special_characters  

# Randomizes the positioning of the characters in the combined list of uppercase, lowercase letters, and numbers
random.shuffle(upper_lower_num)  
# Randomizes the positioning of the characters in the combined list of uppercase letters, numbers, and special characters
random.shuffle(upper_num_symbols)  
# Randomizes the positioning of the characters in the combined list of uppercase, lowercase letters, and special characters
random.shuffle(upper_lower_symbols)
# Randomizes the positioning of the characters in the combined list of lowercase letters, numbers, and special characters
random.shuffle(lower_num_symbols) 
# Randomizes the positioning of the characters in the combined list of all character types
random.shuffle(all_choices)  

# Runs the program
generate_password()