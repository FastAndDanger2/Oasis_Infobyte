import random
import string
import math

def generatePassword(length, use_uppercase, use_digits, use_special_chars):
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

def calculate_complexity(password):
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += len(string.punctuation)

    entropy = len(password) * math.log2(charset_size) if charset_size else 0
    brute_force_time_seconds = (2 ** entropy) / 1e9

    if entropy < 28:
        strength = "Very Weak"
    elif entropy < 36:
        strength = "Weak"
    elif entropy < 60:
        strength = "Moderate"
    elif entropy < 128:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, brute_force_time_seconds

def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds / 60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds / 3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds / 86400:.2f} days"
    else:
        return f"{seconds / 31536000:.2f} years"

def password_generator_cli():
    print("Simple Password Generator")

    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generatePassword(length, use_uppercase, use_digits, use_special_chars)
    print(f"\nGenerated Password: {password}")

    strength, brute_force_time_seconds = calculate_complexity(password)
    print(f"Password Strength: {strength}")
    print(f"Estimated Time to Crack (Brute Force): {format_time(brute_force_time_seconds)}")

if __name__ == "__main__":
    password_generator_cli()
