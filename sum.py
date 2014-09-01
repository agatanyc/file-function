def sum(n):
    r = 0
    for i in range(0, n + 1):
        r += i
    return r

from sys import argv

print(sum(int(argv[1])))
