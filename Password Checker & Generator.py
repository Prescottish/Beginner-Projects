# Step 0 Set up imported packages
import requests
# Replace 'raw_github_url' with the raw URL of your wordlist on GitHub
raw_wordlist_url = 'https://raw.githubusercontent.com/ignis-sec/Pwdb-Public/master/wordlists/ignis-100K.txt'

# Make a GET request to the raw URL
response = requests.get(raw_wordlist_url)
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the content of the wordlist
    wordlist_content = response.text
    # Now 'wordlist_content' contains the content of the wordlist
    # You can split it into a list of words if needed
    wordlist = wordlist_content.split('\n')

# Step 1 Generate title and authorship
print("Password Checker & Generator \n Created by Preston Cotton")

# Step 2 Prompt user to choose check password strength or generate password
userChoice = str(input("Enter \"c\" to check a current password or \"g\" to generate a new password: "))

# Step 3 Create a condition if user inputs c
import re


def passwrdchkr(checkedPassword, wordlist):
    # Check if password is not in the wordlist
    if checkedPassword in wordlist:
        return "The password has been found in data leaks, it is not secure."

    # Check if password is the correct length
    if not 8 <= len(checkedPassword) <= 64:
        return "The password length is not secure, it must be between 8 and 20 characters long."
    if not re.search(r'\d', checkedPassword):
        return "Password is not secure, it must contain at least one digit."

    # Print statement for secure password
    return "Password is secure"


if userChoice.lower() == 'c' or userChoice.upper() == 'c':
    checkedPassword = str(input("Enter your password: "))

    # Call the function and print the result
    result = passwrdchkr(checkedPassword, wordlist)
    print(result)

# Create condition if user enter g
import random
import string


def passwrdgenratr(min_length, include_numbers=True, include_special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Actual creation of password
    characters = letters
    if include_numbers:
        characters += digits
    if include_special_characters:
        characters += special

    # Prior to generated password, forces condition to become true
    generatrdpasswrd = ''
    criteria_met = False
    has_number = False
    has_special = False

    while not criteria_met or len(generatrdpasswrd) < min_length:
        new_char = random.choice(characters)
        generatrdpasswrd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        # Update meets_criteria using logical AND
        criteria_met = True
        if include_numbers:
            criteria_met = has_number
        if include_special_characters:
            criteria_met = criteria_met and has_special

    return generatrdpasswrd

if userChoice.lower() == 'g' or userChoice.upper() == 'g':
    # Function to generate password and the source of characters


    min_length = int(input("Enter minimum length: "))
    include_special_characters = input("Do you want special characters (y/n): ").lower() == 'y'
    generated_password = passwrdgenratr(min_length, include_numbers=True, include_special_characters=include_special_characters)
    print(generated_password)

# Boolean in case of invalid input
elif userChoice !=  'c' or userChoice.upper() != 'c' or userChoice.lower() != 'g' or userChoice.upper() != 'g':
    print(userChoice,"is an invalid input, either enter \"c\" to check a current password or \"g\" to generate a new password")




