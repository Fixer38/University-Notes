def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 != 0):
        print("année bissextile")
    else:
        print("année non bissextile")

is_leap_year(2000)
