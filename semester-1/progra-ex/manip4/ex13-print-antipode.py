def print_antipode(coord: tuple) -> None:
    if type(coord[0]) != float or type(coord[1]) != float:
        print("Erreur dans les données")
    else:
        latitude = str(coord[0] // 1)
        longitude = str(coord[1] // 1)
        if coord[0] > 0:
            latitude += "N"
        else:
            latitude += "S"
        if coord[1] > 0:
            longitude += "E"
        else:
            longitude += "O"
        print(latitude, longitude)

coord = (-3.22, -2.00)
print_antipode(coord)
