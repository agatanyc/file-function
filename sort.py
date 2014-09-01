from sys import argv

def sort(fname):
    with open(fname) as file:
        ss = file.readlines()
        ss.sort()
        for line in ss:
            print(line, end='')

if __name__ == '__main__':
    sort(argv[1])
