import timeit
import time

code_to_test = """
def print_tic_tac(secondes):
    while secondes != 0:
        print("tic")
        time.sleep(1)
        secondes -=1

        if secondes != 0:
            print("tac")
            time.sleep(1)
            secondes -= 1
print_tic_tac(11)
"""
elapsed_time = timeit.timeit(code_to_test, number=1)/1
print(elapsed_time)
