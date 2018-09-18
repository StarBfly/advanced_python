# Counting factorial in different processes and get time of calculating
from functools import wraps
import multiprocessing
from multiprocessing import cpu_count
from time import time


def execution_time_printer(func):
    """Calculate time of execution"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        begin = time()
        func(*args, **kwargs)
        end = time()
        print('Execution time: {}'.format(end - begin))
    return wrapper


@execution_time_printer
def factorial(n):
    """Factorial calculation"""
    x = 1
    for i in range(1, n + 1):
        x = x * i
    return x


@execution_time_printer
def multiprocessing_calculation():
    """Launch factorial calculating in different processes"""
    processes = []
    for i in range(cpu_count() + 1):
        p = multiprocessing.Process(target=factorial, args=(50000,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()


if __name__ == '__main__':
    multiprocessing_calculation()
