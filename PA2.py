# Programmer: Peter Hope
# Course: CS701/GB-731, Dr. Rajeev
# Date: 10/6/21
# Programming Assignment: 2
# Program Inputs: Month number and year number
# Program Outputs: Days in the given month

print ("This program will determine how many days are in a given month of any year")

# create function for days with 31 days
def typeA (month):
    day = 31
    return day
# create function for days with 30 days
def typeB (month):
    day = 30
    return day

# ask for inputs and assign to int
month = int(input("Input the number of the month: "))
year = int(input("Input the number of the year: "))

# call for appropriate month type function
# for months with 31 days and print days
if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month ==12):
    days = typeA(month)
    print ("Number of days:", days)
# for months with 30 days and print days
elif (month == 4 or month == 6 or month == 9 or month == 11):
    days = typeB(month)
    print ("Number of days:", days)
# for february and print days
elif (month == 2):
    # determine if it is a leap year or not
    if (year%100 == 0):
        if (year%400 == 0):
            days = 29
        else:
            days = 28
    else:
        if (year%4 == 0):
            days = 29
        else:
            days = 28
    print ("Number of days:", days)
# catch if not a valid month number
else:
    print ("Please input a month number from 1-12")
