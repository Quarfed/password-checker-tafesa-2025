"""
Michael Kosteriadis 001244342
Date:
PasswordChecker3
"""

# DEF MAIN()
#   list_data = [] empty list
#   input_file= OPEN ITworks_password_log.txt "R"
#   FOR line IN input_file
#       list.data.append line_data
#   input_file CLOSE
#   count_pw_too_large = [] empty list
#   count_pw_too_small = [] empty list
#   pw_too_short = password < 6
#   FOR data IN list_data
#       IF pw_too_short IN data:
#           count_pw_too_short.APPEND data
#       ELSE:
#           count_pw_too_long.APPEND data
#   FOR line in list_data
#       PRINT line
#   PRINT "Number of passwords too short: {} \n Number of passwords too long: {}".FORMAT LEN count pw too short, LEN count pw too long

def main():

    print("\nWelcome to Password Checker3 Created by: Michael Kosteriadis 001244342\n")

# creating an empty list called list data
    list_data=[]

# opening input file to read password outcomes
    input_file=open("ITWorks_password_log.txt", "r")

# reading through the lines in the input file and appending them to the list we created
    for line in input_file:
        list_data.append(line)

# closing file
    input_file.close()

# creating empty lists to store the password outcomes
    count_pw_too_large = []
    count_pw_too_short = []
# creating a target string to search the strings in the list and help sort them into the separate lists
    pw_too_short = "password < 6"

# iterating though data in the list
    for data in list_data:

#if the target string is found in the data it will append that to the pw too short
        if pw_too_short in data:
            count_pw_too_short.append(data)

# if the target string isn't found then the data will append to pw too long
        else:
            count_pw_too_large.append(data)

# print all data in list
    for line in list_data:
        print(line)

# printing the amount of strings that are then sorted into the  pw too short and pw too long showing the amount of passwords that were too long and too short
    print("Number of passwords too short:{}\n \nNumber of passwords too long:{}".format(len(count_pw_too_short), len(count_pw_too_large)))

main()
