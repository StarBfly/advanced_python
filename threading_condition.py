# Homework 3: Condition

import threading


def odd_numbers_generator():
    for odd in range(1, 101, 2):
        yield odd


def even_numbers_generator():
    for even in range(2, 101, 2):
        yield even


FIRST_ODD_PRINTED = False


class CountingThread(threading.Thread):
    def __init__(self, num_type, cond):
        super(CountingThread, self).__init__()
        self.num_type = num_type
        self.cv = cond

    def run(self):
        global FIRST_ODD_PRINTED
        if self.num_type == "odd":
            for i in odd_numbers_generator():
                with self.cv:
                    print("Odd thread number: {}".format(i))
                    FIRST_ODD_PRINTED = True
                    self.cv.notify()
                    self.cv.wait()

        else:
            for i in even_numbers_generator():
                with self.cv:
                    while not FIRST_ODD_PRINTED:
                        self.cv.wait()
                    print("Even thread number: {}".format(i))
                    self.cv.notify()
                    self.cv.wait()


condition = threading.Condition()

odd_thread = CountingThread(num_type="odd", cond=condition)

even_thread = CountingThread(num_type="even", cond=condition)

odd_thread.start()
even_thread.start()


odd_thread.join()
even_thread.join()
