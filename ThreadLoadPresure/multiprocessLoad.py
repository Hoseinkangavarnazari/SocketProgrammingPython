# importing the multiprocessing module
import multiprocessing
import time
from console_progressbar import ProgressBar

def print_square(num):
    while True:
        a = 12*9823874507209
        b = a * a



if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=print_square, args=(11, ))
    p2 = multiprocessing.Process(target=print_square, args=(12, ))
    p3 = multiprocessing.Process(target=print_square, args=(13, ))
    p4 = multiprocessing.Process(target=print_square, args=(14, ))

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    # starting process 3
    p3.start()
    # starting process 4
    p4.start()

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()
    # wait until process 3 is finished
    p3.join()
    # wait until process 4 is finished
    p4.join()

    # both processes finished
    print("Done!")
