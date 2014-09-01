from sys import argv
import cat
import echo
import head
import sort
import tail

if argv[1] == '-c':
    cat.cat(argv[2])
elif argv[1] == '-e':
    echo.echo(argv[2])
elif argv[1] == '-h':
    head.head(argv[2])
elif argv[1] == '-s':
    sort.sort(argv[2])
elif argv[1] == '-t':
    tail.tail(argv[2])
