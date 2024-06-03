import csv
from sys import argv, exit
from tabulate import tabulate


def main():
    if len(argv) < 2:
        exit("Too few command-line arguments")
    elif len(argv) > 2:
        exit("Too many command-line arguments")
    else:
        if not argv[1].lower().endswith("csv"):
            exit("Not a CSV file")
        else:
            try:
                table = tabular(argv[1])
                print(table)
            except FileNotFoundError:
                exit("File does not exist")


def tabular(file):
    with open(file) as f:
        reader = csv.reader(f)
        table = tabulate(reader, headers="firstrow", tablefmt="grid")
        return table


if __name__ == "__main__":
    main()
