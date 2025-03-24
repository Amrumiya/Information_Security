import random
import string
import argparse

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("You must select at least one character type.")

    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Secure Password Generator")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password (default: 12)")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude special characters")

    args = parser.parse_args()

    password = generate_password(
        args.length,
        not args.no_upper,
        not args.no_lower,
        not args.no_digits,
        not args.no_symbols
    )

    print("Generated Password:", password)

