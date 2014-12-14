from functools import reduce
from sys import argv

def fold_factorial(n):
    """(int) -> int"""

    def multiply(x, y):
        return x * y

    return reduce(multiply, range(2, n + 1), 1)

if __name__ == '__main__':
    print(fold_factorial(int(argv[1])))
