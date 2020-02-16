def common_pairs(d1: dict, d2: dict) -> list:
    common_pair = []
    for value in d1.items():
        print(value)
        if value in d2.items():
            common_pair.append(value)
    return common_pair

liste = common_pairs({1: "totto", 32: "rom", 2: "haha"}, {1: "totto", 2: "haha", "hello": "hello"})
print(liste)
