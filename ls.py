import sys
import os

def ls():
    for x in os.listdir():
        if not x.startswith('.'):
            print(x)

def ls_a():
    for x in os.listdir():
        print(x)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        ls()
    elif sys.argv[1] == '-a':
        ls_a()
    else:
        print('usage: ls.py [-a]', file=sys.stderr)
        sys.exit(1)
