from sys import argv

def cat(filename):
    with open(filename) as file:
        print(file.read(), end='')

if __name__ == '__main__':
    for a in argv[1:]:
        cat(a)
