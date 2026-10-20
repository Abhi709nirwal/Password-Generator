"""Password Generator - a simple command-line tool.

Generates a strong random password using Python's `secrets` module,
which is designed for security-sensitive randomness.
"""
import secrets
import string


def ask_length() -> int:
    """Ask the user for a password length (minimum 8)."""
    while True:
        value = input("Password length (8-64): ").strip()
        if value.isdigit() and 8 <= int(value) <= 64:
            return int(value)
        print("Please enter a number between 8 and 64.")


def ask_yes_no(question: str) -> bool:
    """Ask a yes/no question. Returns True for yes."""
    while True:
        answer = input(f"{question} (y/n): ").strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("Please type y or n.")


def build_character_set(use_upper, use_digits, use_symbols) -> str:
    """Combine the allowed characters into one string."""
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()-_=+"
    return chars


def generate_password(length: int, chars: str) -> str:
    """Pick `length` random characters from `chars`."""
    return "".join(secrets.choice(chars) for _ in range(length))


def main() -> None:
    print("=== Password Generator ===")
    length = ask_length()
    use_upper = ask_yes_no("Include UPPERCASE letters?")
    use_digits = ask_yes_no("Include digits?")
    use_symbols = ask_yes_no("Include symbols?")

    chars = build_character_set(use_upper, use_digits, use_symbols)
    print("\nYour password:", generate_password(length, chars))


if __name__ == "__main__":
    main()
