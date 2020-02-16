def sort_keys(d: dict) -> tuple:
    dict_str = {}
    dict_int = {}
    for key, value in d.items():
        if type(key) == int:
            dict_int[key] = value
        elif type(key) == str:
            dict_str[key] = value
    return dict_int, dict_str

d = {1: "totto", "Romain": 42, 42: 43, "new": "car"}
tuple_dict = sort_keys(d)
print(tuple_dict)
