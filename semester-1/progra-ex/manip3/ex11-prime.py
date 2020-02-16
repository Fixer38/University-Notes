import math

def is_prime(nb):

    if nb <= 1:
        return False

    last_divisor = math.floor(math.sqrt(nb))
    for x in range(2, 1+last_divisor):
        if nb % x == 0:
            return False
    return True

print(is_prime(10))
