def check_byte_for_ip(byte):
    return True if byte > 0 and byte <= 255 else False

def check_ip(byte1, byte2, byte3, byte4):
    if check_byte_for_ip(byte1) and check_byte_for_ip(byte2) and check_byte_for_ip(byte3) and check_byte_for_ip(byte4):
        print(byte1, byte2, byte3, byte4, sep='.')
    else:
        print("Ce n'est pas une addresse valide")

check_ip(144, 155, 212, 1)
