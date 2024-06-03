import csv
from sys import argv, exit
from tabulate import tabulate

def main():
    if len(argv) < 2:
        exit('Too few command-line arguments')
    elif len(argv) > 2:
        exit('Too many command-line arguments')
    else:
        if not argv[1].endswith('csv'):
            exit('Not a CSV file')




if __name__ == '__main__':
    main()