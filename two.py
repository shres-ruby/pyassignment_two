# 2. Write an if statement to determine whether a variable holding a year is a leap year.

year = 2000

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("Leap year")

else:
    print("Not leap year")