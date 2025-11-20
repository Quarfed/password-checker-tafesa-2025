"""
Michael Kosteriadis 001244342
Date: 4/11/2025
Assignment PasswordChecker2
"""

import datetime

def main():
    # declaring minimum and maximum password length
    MIN_PASSWORD_LENGTH = 6
    MAX_PASSWORD_LENGTH = 10

    print("PasswordChecker2 developed by: Michael Kosteriadis")

    # asking user to input password
    password = input("\nEnter a password Must contain a minimum of 6 characters and a maximum of 10 characters:\npassword:")

    # checking the length if the password
    password_length = len(password)



    # Check if the condition of minimum and maximum length is met if not ask for another input until it is
    while password_length < MIN_PASSWORD_LENGTH or password_length > MAX_PASSWORD_LENGTH:
        print("\n## password need to be longer than minimum of 6 characters and a maximum of 10 characters ##\n")
        password = input(
            "Enter a password Must contain a minimum of 6 characters and a maximum of 10 characters:\npassword:")

        # creating a way for the exact date and time to be recorded at the exact second an incorrect input is given
        current_date_and_time = str(datetime.datetime.today())

        #checking why the password is incorrect seeing if it is too long or too short
        if password_length < MIN_PASSWORD_LENGTH:
            reason_password_invalid = str("password < 6")
        else:
            reason_password_invalid = str("password > 10")

        # creating and opening a file with the correct naming convention required to record incorrect password attempts
        output_file = open("password_log_Michael_Kosteriadis.txt", "a")
        #this command below is outputting the date and time the output was given and also including the reason for it being rejected and then also writing a new line for new attempts
        output_file.write(current_date_and_time + ", " + reason_password_invalid + '\n')
        #closing the output file
        output_file.close()
        #calculating password length
        password_length = len(password)

    # checking if the password only contains numbers
    if password.isdigit():
        message = "password weak - contains only numbers"

    # checking if password only contains letters
    elif password.isalpha():
        message = "password weak - contains only letters"

    # If the password contains a mix of numbers and letters tell user password is strong
    else:
        message = "password strong!"

    #printing password length and password strength
    print("password length is: {}\n{}".format(password_length, message))

    #printing all lines of the .txt file with all attempts and displaying them in order
    output_file = open("password_log_Michael_Kosteriadis.txt", "r")
    for line in output_file:
        print(line, end='')
    output_file.close()

main()

