sec = int(input("Secondes : "))
hour = sec // 3600
minut = (sec%3600) // 60
print(f"{sec} secondes = {hour} Heures {minut} minutes {sec%60} secondes")
