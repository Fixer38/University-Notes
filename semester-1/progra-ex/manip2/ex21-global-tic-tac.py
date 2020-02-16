sec = int(input("Entrez un nombre de secondes: "))
i = 0

def tic():
    global i

    if i < sec:
        print("tic")

    i += 1

    if i < sec:
        tac()


def tac():
    global i

    if i < sec:
        print("tac")

    i += 1

    if i < sec:
        tic()

tic()
