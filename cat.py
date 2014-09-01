from sys import argv

def cat(filename):
    with open(filename) as file:
        print(file.read())

if __name__ == '__main__':
    cat(argv[1])
