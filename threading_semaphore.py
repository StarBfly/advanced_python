# Homework 3: Semaphore

import threading
import time


def odd_numbers_generator():
    for odd in range(1, 101, 2):
        yield odd


def even_numbers_generator():
    for even in range(2, 101, 2):
        yield even


ODD_PRINTED = False


class CountingThread(threading.Thread):
    def __init__(self, num_type, c_semaphore):
        super(CountingThread, self).__init__()
        self.num_type = num_type
        self.sem = c_semaphore

    def run(self):
        global ODD_PRINTED
        if self.num_type == "odd":
            for i in odd_numbers_generator():
                while ODD_PRINTED:
                    time.sleep(0.001)
                with self.sem:
                    print("Odd thread number: {}".format(i))
                    ODD_PRINTED = True
        else:
            for i in even_numbers_generator():
                while not ODD_PRINTED:
                    time.sleep(0.001)
                with self.sem:
                    print("Even thread number: {}".format(i))
                    ODD_PRINTED = False


semaphore = threading.Semaphore()

odd_thread = CountingThread(num_type="odd",
                            c_semaphore=semaphore)

even_thread = CountingThread(num_type="even",
                             c_semaphore=semaphore)


odd_thread.start()
even_thread.start()


odd_thread.join()
even_thread.join()
