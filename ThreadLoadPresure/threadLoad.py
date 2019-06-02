#!/usr/bin/env python

import threading
import time
from console_progressbar import ProgressBar


class MyThread(threading.Thread):
    def run(self):

        while True:
            a = 12*9823874507209
            b = a * a


def main():
    counter = 1
    # Four times...
    for x in range(20):
            # ...Instantiate a thread and pass a unique ID to it
        print(counter)
        counter += 1
        mythread = MyThread(name="Thread-{}".format(x + 1))
        # ...Start the thread, invoke the run meth
        mythread.start()


if __name__ == '__main__':
    main()
