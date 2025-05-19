import random
import string

def generate_password(length=12, use_letters=True, use_digits=True, use_symbols=True):
    characters = ''
    
    if use_letters:
        characters += string.ascii_letters  # a-z + A-Z
    if use_digits:
        characters += string.digits         # 0-9
    if use_symbols:
        characters += string.punctuation    # Special symbols

    if not characters:
        return "Error: No character types selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# --- User Input Example ---
if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        pwd = generate_password(length, use_letters, use_digits, use_symbols)
        print(f"\nGenerated Password: {pwd}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")



