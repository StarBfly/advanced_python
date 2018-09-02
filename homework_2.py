# Program falls with segmentation error

import sys

# Getting default recursion limit
print(sys.getrecursionlimit())

# Setting a higher recursion depth by bitwise shift to cause C stack overflow
sys.setrecursionlimit(1 << 20)

print(sys.getrecursionlimit())


# Initializing recursion
def recurse_func(recurse_func):
    recurse_func(recurse_func)


if __name__ == "__main__":
    recurse_func(recurse_func)
