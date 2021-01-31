try:

    Year = int(input("Enter a year to see if it's a leap year or not: "))

    leapTrue = Year%4 == 0
    leapTrue = Year%100 == 0
    leapTrue = Year%400 == 0

    if leapTrue:

        print  ("This is a leap year")

    else:

        print  ("This is not a leap year")
except ValueError:

    print  ("Error, Only digits are allowed")
