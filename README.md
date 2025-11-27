# Password-Checker-tafesa-2025
- This project is current as of November 2025 for ICTPRG302 Intro to programing with Python
- I DO NOT condone cheating and this work should not be used in a copy paste scenario
- USE AT YOUR OWN RISK
# STATUS
## PASSWORD_CHECKER_PART1: Pass 100% :heavy_check_mark:

## PASSWORD_CHECKER_PART2: Pass 100% :heavy_check_mark:

## PASSWORD_CHECKER_PART3: Pass 100% :heavy_check_mark:

# Learning outcomes
## Password checker 1
### While loops:
    - Loops while a condition is true untill it is false then the loop will break
### IF statments:
    - Loops until a condition is true or false
### INPUT:
    - Takes a users input and creates a variable
### LEN()
    - Will calculate the length of a given string or list withing the ()
### .ISALPHA()
    - Will check if a string contains ONLY letters and will return a bool output (true, false)
      - "HELLO" will return 'true'
      - "hello1" will return 'false' (contains number)
      - "hello world" will also return false (contains a space)
### .ISDIGIT()
    - will check if a string contains ONLY numbers and return a bool output (true, false)
      - "123456789" Will return 'true'
      -  "1234a" will return 'false'
  
## Password Checker 2
### File Handling
    - In Part 2 of password checker you will genrate outputs to a file using Python File handling:
    - (filename) = open("filename", "actions that will be conducted with the file")
      -with the open command you will in this project be creating a new .txt file
      -the within the second set of brackets you will input your desired name followed by a comma and
        then one of the following options
        - a: to append to a file (will not overwrite data)
        - w: to write to a file (will overwrite anything inside the file)
        - r: to read from an existing file
    - (filename).Write(what ever text you are wanting to write to the file)
    - (filename).close()- will close the file that you're writing too, why this needs
        to happen is outside scope of what is required however just make sure its done! (you can google it if you'd like)

## Password checker 3
### Lists (arrays)
    - Lists are basically arrays think of them as row in excel
    - The first position in a list is identified as (0) and all information will be identified in order
        they were appended to the list
    - (name of list) = [] will create an empty list that can be called given its name 
    - (name of list) = []*(number) will create a list with a set capacity 
    - (listname).append will add elements to the list into the next available slot
