from sys import argv

def tail(fname):
    with open(fname) as file:
        lines = file.readlines()
    for line in lines[-10:]:
        print(line, end='')

if __name__ == '__main__':
    tail(argv[1])
