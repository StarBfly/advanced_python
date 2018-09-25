# homework 5 Output sum of prime numbers in the specified range [n, m).
import asyncio
from itertools import count
from itertools import islice
from math import sqrt


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


async def sum_of_prime(n, m):
    print("Counting sum...")
    x = 0
    for i in range(n, m):
        if is_prime(i):
            x += i
    await asyncio.sleep(1)
    return x


async def print_sum(n, m):
    result = await sum_of_prime(n, m)
    print("Sum of prime numbers in the range ({}, {}) is {}."
          .format(n, m, result))

loop = asyncio.get_event_loop()

# !!! The jupiter kernel itself runs on an event loop. !!!
if loop.is_running():
    loop.create_task(print_sum(1, 6))
else:
    loop.run_until_complete(print_sum(1, 6))
    loop.close()
