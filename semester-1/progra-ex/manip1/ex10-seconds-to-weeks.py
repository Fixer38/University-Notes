sec = int(input("Secondes : "))
week = sec // ((3600*24)*7) # 24 for nb of hours and 7 for number of days in a week
day = (sec%3600*24*7) // (3600 * 24)
hour = (sec%3600 * 24) // 3600
minut = (sec%3600) // 60
print(f"{sec} secondes = {week} semaines {day} jours {hour} heures {minut} minutes {sec%60} secondes")
