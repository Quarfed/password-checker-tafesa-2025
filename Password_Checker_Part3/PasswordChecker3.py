"""
Michael Kosteriadis 001244342
Date:
PasswordChecker3
"""

# DEF MAIN()
#   list_data = [] empty list
#   count_pw_too_short = 0
#   count_pw_too_large = 0
#   input_file= OPEN ITworks_password_log.txt "R"
#   FOR line IN input_file
#       list.data.append line_data
#   input_file CLOSE
#   pw_too_short = password < 6
#   FOR data IN list_data
#       IF pw_too_short IN data:
#           count_pw_too_short + 1
#       ELSE:
#           count_pw_too_long + 1
#   FOR line in list_data
#       PRINT line
#   PRINT "Number of passwords too short: {} \n Number of passwords too long: {}".FORMAT count_pw_too_small, count_pw_too_large

def main():

    print("\nWelcome to Password Checker3 Created by: Michael Kosteriadis 001244342\n")

# creating an empty list called list data and the Password too long and short counts
    list_data=[]
    count_pw_too_short = 0
    count_pw_too_large = 0

# opening input file to read password outcomes
    input_file=open("ITWorks_password_log.txt", "r")

# reading through the lines in the input file and appending them to the list we created
    for line in input_file:
        list_data.append(line)

# closing file
    input_file.close()

# creating a target string to search the strings in the list and help sort them into the separate lists
    pw_too_short = "password < 6"

# iterating though data in the list
    for data in list_data:

#if the target string is found in the data it will
        if pw_too_short in data:
            count_pw_too_short += 1

# if the target string isn't found then the data will append to pw too long
        else:
            count_pw_too_large += 1
# print all data in list
    for line in list_data:
        print(line, end= '')

# printing the amount of strings that are then sorted into the  pw too short and pw too long showing the amount of passwords that were too long and too short
    print("\n Number of passwords too short:{}\n \nNumber of passwords too long:{}".format(count_pw_too_short, count_pw_too_large))

main()
