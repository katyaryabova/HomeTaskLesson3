year = int(input("Enter year for get information if the year is leap: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year is: ", year)
else:
    print("Normal Year is: ", year)
