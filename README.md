# Password Generator

A simple command-line tool that generates strong, random passwords.

## Features
- Choose password length (8-64 characters)
- Optional uppercase letters, digits and symbols
- Uses Python's `secrets` module (secure randomness, not `random`)
- Input validation for all prompts

## Tech Used
Python 3 (standard library only)

## How to Run
```bash
git clone https://github.com/Abhi709nirwal/password-generator.git
cd password-generator
python main.py
```

## Example
```
=== Password Generator ===
Password length (8-64): 12
Include UPPERCASE letters? (y/n): y
Include digits? (y/n): y
Include symbols? (y/n): y

Your password: k#7Qm-pZ2@vL
```

## What I Learned
- Functions and input validation
- Why `secrets` is safer than `random` for passwords

## Future Improvements
- Copy password to clipboard
- Generate multiple passwords at once
