# Homework 3: Lock

import threading


def odd_numbers_generator():
    for odd in range(1, 101, 2):
        yield odd


def even_numbers_generator():
    for even in range(2, 101, 2):
        yield even


class CountingThread(threading.Thread):
    def __init__(self, num_type, odd_lock, even_lock):
        super(CountingThread, self).__init__()
        self.num_type = num_type
        self.odd_thread_lock = odd_lock
        self.even_thread_lock = even_lock

    def run(self):
        if self.num_type == "odd":
            for i in odd_numbers_generator():
                self.odd_thread_lock.acquire()
                print("Odd thread number: {}".format(i))
                self.even_thread_lock.release()
        else:
            for i in even_numbers_generator():
                self.even_thread_lock.acquire()
                print("Even thread number: {}".format(i))
                self.odd_thread_lock.release()


odd_thread_lock = threading.Lock()
even_thread_lock = threading.Lock()

odd_thread = CountingThread(num_type="odd",
                            odd_lock=odd_thread_lock,
                            even_lock=even_thread_lock)

even_thread = CountingThread(num_type="even",
                             odd_lock=odd_thread_lock,
                             even_lock=even_thread_lock)


even_thread_lock.acquire()
odd_thread.start()
even_thread.start()

odd_thread.join()
even_thread.join()
