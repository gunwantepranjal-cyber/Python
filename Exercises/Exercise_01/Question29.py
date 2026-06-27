year = 2024
if year %4 == 0:
    if year % 100 == 0:
        if year % 400  == 0:
            print("leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("not a leap year")
print("Year processed:",year)
