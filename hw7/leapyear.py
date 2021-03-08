def checkLeapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False

year = input("Enter a year to see if it's a leap year or not: ")
if(checkLeapYear(year)):
    print(year,"is a leap year")

else:
    print(year, "is not a leap year")