blocs = {
	"Air" :	{
			"id_num" : 0,  
			"id_text" : "minecraft:air",
			"variantes" : []
		}, 
	"Stone" :	{
			"id_num" : 1,
			"id_text" : "minecraft:stone",
			"variantes" : ["Granite", "Polished Granite", "Diorite", 						"Polished Diorite", "Andesite", "Polished Andesite"]
		},
	"Grass" :	{
			"id_num" : 2,  
			"id_text" : "minecraft:grass",
			"variantes" : []
		},
	"Dirt" :	{
			"id_num" : 3,  
			"id_text" : "minecraft:dirt",
			"variantes" : ["Coarse Dirt", "Podzol"]
		},
	"Cobblestone" : {
			"id_num" : 4,  
			"id_text" : "minecraft:cobblestone",
			"variantes" : []
		}, 
	"Oak Wood Plank" : {
			"id_num" : 5,
			"id_text" : "minecraft:planks",
			"variantes" : ["Spruce Wood Plank", "Birch Wood Plank", 
						"Jungle Wood Plank", "Acacia Wood Plank", 
						"Dark Oak Wood Plank"]
		}
}

#for key, attr in blocs.items():
#    print(attr["id_num"])
#    for variante in attr["variantes"]:
#        print(variante)

f:or key, attr in blocs.items():
    if len(attr["variantes"]) >= 1:
        print(key)

#def ask_info():
#    name = input("Entrez un nom: ")
#    id_num = input("Entrez un identifiant numérique: ")
#    id_text = input("Entrez un identifiant textuel: ")
#    return name, id_num, id_text
#
#block = ask_info()
#
#def add_block(block: tuple, blocs: dict):
#    blocs[block[0]] = {"id_num": block[1], "id_text": block[2]}
#    return blocs
#
#blocs = add_block(block, blocs)

def print_blocs(blocs: dict):
    for attr, block in blocs.items():
        print(f"{attr} :")
        for block_key, block_value in block.items():
            if block_value != []:
                print(f"- {block_key} : {block_value}")

def print_smallest_largest(nb_list: list):
    minimum = 999
    maximum = 0
    for nb in nb_list:
        if nb < minimum:
            minimum = nb
        elif nb > maximum:
            maximum = nb
    print(f"Minimum: {minimum}\nMaximum: {maximum}")

liste = [3, 10, 343, 278, 27, 998, 182, 391, 302, 401]
print_smallest_largest(liste)
