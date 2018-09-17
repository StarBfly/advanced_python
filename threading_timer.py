# Homework 3: Timer

from threading import Timer
import time


def odd_numbers_counter():
    for odd in range(1, 101, 2):
        print("Odd thread number: {}".format(odd))
        time.sleep(0.4)


def even_number_counter():
    for even in range(2, 101, 2):
        print("Even thread number: {}".format(even))
        time.sleep(0.4)


odd_thread = Timer(0.2, odd_numbers_counter)
even_thread = Timer(0.4, even_number_counter)

odd_thread.start()
even_thread.start()

odd_thread.join()
even_thread.join()
