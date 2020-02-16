def print_ipv4(octet1, octet2, octet3, octet4):
    if octet1 <= 255 and octet2 <= 255 and octet3 <= 255 and octet4 <= 255:
        print(octet1, octet2, octet3, octet4, sep=".")
    else:
        print("Ce n'est pas une addresse valide")

print_ipv4(150, 25, 18, 32)
