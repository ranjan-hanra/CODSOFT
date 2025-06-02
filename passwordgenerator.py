import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_specials=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    if not characters:
        return "You must select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
try:
    length = int(input("Enter the desired password length: "))
    use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_specials = input("Include special characters? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, use_letters, use_digits, use_specials)
    print("Generated password:", password)
except ValueError:
    print("Invalid input. Please enter a valid number for length.")
