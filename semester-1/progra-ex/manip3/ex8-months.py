def nbdays_in_month(month, leap=False):
    month = month.lower()
    if month == "février":
        if leap:
            return 29
        else:
            return 28

    if month == "septembre" or month == "novembre" or month == "avril" or month == "juin":
        return 30
    else:
        return 31

print(nbdays_in_month("février", True))
