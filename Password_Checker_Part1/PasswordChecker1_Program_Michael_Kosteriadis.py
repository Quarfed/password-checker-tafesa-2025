"""
Michael Kosteriadis
Date: 31/10/2025
Assignment PasswordChecker1
"""
# MINIMUM_PASSWORD_LENGTH = 6
# MAX_PASSWORD_LENGTH = 10
#
# INPUT password
# CALCULATE password Length
# WHILE password < 6 or > 10
#   PRINT password requirements
#   INPUT password
#   CALCULATE password length
#
# IF password .ISDIGIT
#   OUTPUT = password weak only contains numbers
# ELIF password .ISNUMBER
#   OUTPUT = password weak only contains letters
# ELSE
#   OUTPUT = password strong!
# PRINT password length and password strength



# declaring minimum and maximum password length
MIN_PASSWORD_LENGTH = 6
MAX_PASSWORD_LENGTH = 10

print("\n PasswordChecker1 program developed by: Michael Kosteriadis\n")

# asking user to input password
password=input("\nEnter a password Must contain a minimum of 6 characters and a maximum of 10 characters:\npassword:")

# checking the length if the password
password_length = len(password)

# Check if the condition of minimum and maximum length is met if not ask for another input until it is
while password_length < MIN_PASSWORD_LENGTH or password_length > MAX_PASSWORD_LENGTH:
    print("\n## password need to be longer than minimum of 6 characters and a maximum of 10 characters ##\n")
    password = input("Enter a password Must contain a minimum of 6 characters and a maximum of 10 characters:\npassword:")
    password_length = len(password)

# checking if the password only contains numbers
if password.isdigit():
        comment = "password weak - contains only numbers"

# checking if password only contains letters
elif password.isalpha():
        comment = "password weak - contains only letters"

# If the password contains a mix of numbers and letters tell user password is strong
else:
    comment = "password strong!"

# Print password length and password strength
print("password length is: {}\n{}".format(password_length, comment))




