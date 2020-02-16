from time import sleep


def tic_tac(sec):
    sec_ecouler = 0
    while sec_ecouler < sec:
        if sec_ecouler % 2 == 0:
            print("tic")
        else:
            print("tac")
        sec_ecouler += 1
        sleep(1)

tic_tac(11)
