def modify_production(tile: dict, resource: str, amount: int) -> None:
    tile["production"][resource] += amount
    if tile[resource] < 0:
        tile[resource] = 0

def new_tile(terrain: str) -> dict:
    production = {"food": 0, "materials": 0, "gold": 0}
    tile = {"terrain": terrain, "production": production}
    if terrain == "water":
        modify_production(tile, "food", 1)
    elif terrain == "plain":
        modify_production(tile, "food", 2)
    elif terrain == "forest":
        modify_production(tile, "food", 1)
        modify_production(tile, "materials", 1)
    else:
        modify_production(tile, "materials", 2)
    return tile

def has_owner(tile: dict, name: str = None) -> bool:
    if name == None:
        return "owner" in tile and tile["owner"] != None
    else:
        return tile["owner"] == name


def has_city(tile: dict) -> bool:
    return 'city' in tile

def has_tradepost(tile: dict) -> bool:
    return 'tradepost' in tile

def can_build_city(tile: dict) -> bool:
    return tile["terrain"] == "plain" and has_owner(tile) and not has_tradepost(tile)

def can_build_tradepost(tile: dict) -> bool:
    return tile["terrain"] != "water" and has_owner(tile) and not has_city(tile) and not has_tradepost(tile)

def build_tradepost(tile: dict) -> None:
    if can_build_tradepost(tile):
        tile["tradepost"] = True
        modify_production(tile, "gold", 1)
    else:
        print("Impossible de construire le tradepost")

def build_city(tile: dict, name: str) -> None:
    if can_build_city(tile):
        tile["city"] = name
        modify_production(tile, "gold", 3)
        if has_tradepost(tile):
            del tile["tradepost"]
            modify_production(tile, "gold", -1)
    else:
        print("Impossible de construire une ville")

def cut_forest(tile: dict) -> None:
    if tile["terrain"] == "forest":
        tile["terrain"] = "plain"
        modify_production(tile, "food", 1)
        modify_production(tile, "materials", -1)
    else:
        print("Pas de forêt")

def change_owner(tile: dict, name: str = None) -> str:
    previous_owner = None
    if has_owner(tile):
        previous_owner = tile["owner"]
        if name == None:
            del tile["owner"]
    if name != None:
        tile["owner"] = name
    return previous_owner

def raze_building(tile: dict) -> bool:
    razed = False
    if has_city(tile):
        del tile["city"]
        modify_production(tile, "gold", -3)
        razed = True
    if has_tradepost(tile):
        tile["tradepost"] = None
        modify_production(tile, "gold", -1)
        razed = True
    return razed


def count_cities(tiles: list, name: str) -> int:
    nb_cities = 0
    for tile in tiles:
        if tile["owner"] == name:
            nb_cities += 1
    return nb_cities

def count_total_productions(tiles: list, name: str) -> dict:
    nbfood = 0
    nbmaterial = 0
    nbgold = 0
    for tile in tiles:
        if tile["owner"] == name:
            for prod in tile["production"]:
                if prod["food"]:
                    nbfood += 1
                elif prod["materials"]:
                    nbmaterial += 1
                else:
                    nbgold += 1
    return {"gold": nbgold, "material": nbmaterial, "food": nbfood}

ressource = {"food": 0, "materials": 0, "gold": 0}
tile = {"terrain" : "plain",
        "production": ressource
        }
