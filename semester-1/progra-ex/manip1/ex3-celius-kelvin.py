kelvin = int(input("Kelvin: "))
kelvin_to_fahrenheit = round((kelvin - 273.15) * (9 / 5) + 32, 2)
kelvin_to_celsius = round(kelvin - 273.15, 2)
print(f"{kelvin} K = {kelvin_to_fahrenheit} °F = {kelvin_to_celsius} °C")
