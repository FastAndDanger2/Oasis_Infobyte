import random
import string

def generatePassword(length, use_uppercase, use_digits, use_special_chars):
    characters = string.ascii_lowercase  # Start with lowercase letters

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator_cli():
    print("Simple Password Generator")

    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generatePassword(length, use_uppercase, use_digits, use_special_chars)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    password_generator_cli()
