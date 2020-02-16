import math

def distance_on_earth(coord1: tuple, coord2: tuple) -> float:
    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])
    radius = 6378
    return radius * math.acos(math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2)*math.cos(abs(lon1-lon2)))

coord1 = (12.25, 3.12)
coord2 = (46.44, 23.12)
print(distance_on_earth(coord1, coord2))
