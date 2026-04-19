# User Registration System

A terminal-based user registration system built in Python that validates name, email, and password before registering a user.

## Features
- Name validation (non-empty, letters only, minimum length)
- Email validation (format, single @, valid ending, length, alphanumeric start/end)
- Password validation (length, uppercase, lowercase, no spaces, not same as email)
- Specific error messages for each failed validation

## How it works
The program prompts the user to enter their name, email and password. Each field is validated through its own dedicated function. If all three pass, the user is registered. If any fail, specific error messages are displayed.

## Built with
Python 3.12 — functions, string methods, loops, conditionals
