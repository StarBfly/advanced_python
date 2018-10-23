from __future__ import print_function


def fib(n):
    """Returns the Fibonacci number on position n."""
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    import time
    start_time = time.time()
    print(fib(45))
    end_time = time.time()
    print(end_time - start_time)
