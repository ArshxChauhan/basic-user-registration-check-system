def name_check(name):
    valid_name = True

    if name == "":
        print("Name cannot be empty, please enter a valid name")
        valid_name = False

    if name.isnumeric():
        print("Name can only contain letters")
        valid_name = False

    if len(name) < 1:
        print("Name should be longer than 1 character, please enter your full name")
        valid_name = False

    return valid_name


def email_check(email):
    valid_email = True

    if email == "" or email is None:
        print("Email cannot be empty, please enter a valid email")
        valid_email = False

    if "." not in email or '@' not in email:
        print("Email should include . and @")
        valid_email = False

    if email.count("@") != 1:
        print("Email can include only one @")
        valid_email = False

    if not email.endswith((".com", ".org", ".net")):
        print("Email should end with .com,.org. or .net")
        valid_email = False

    if len(email) > 254:
        print("Email too long")
        valid_email = False

    if email and (not email[0].isalnum() or not email[-1].isalnum()):
        print("Email should begin and end with a letter or digit please")
        valid_email = False

    return valid_email


def password_check(password,email):
    valid_pass = True

    if password == "":
        print("Password cannot be empty")
        valid_pass = False

    if len(password) < 8:
        print("Password should have a minimum of 8 characters")
        valid_pass = False

    has_upper = False
    has_lower = False
    for x in password:
        if x.isupper():
            has_upper = True
        if x.islower():
            has_lower = True

    if not has_upper or not has_lower:
        print("Password must contain an uppercase and lowercase letter")
        valid_pass = False

    if password == email:
        print("Password cannot be same as email")
        valid_pass = False

    if " " in password:
        print("password cannot have spaces")
        valid_pass = False

    if password and (not password[0].isalnum() or not password[-1].isalnum()):
        print("Password should begin and end with a number or a letter")
        valid_pass = False

    return valid_pass


print("Welcome to the Registration System")
print("="*50)
name = input("Enter your name: ")
email = input("Enter your email: ")
password = input("Enter your password: ")

print("Registering...")
print("="*50)

if name_check(name) and email_check(email) and password_check(password,email) :
    print(f"✓ Registration Successful! Welcome {name}!")

else:
    print("\n✗ Registration Failed, please complete the above requirements first ^")


