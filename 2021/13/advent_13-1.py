# Erik Cooke
# Advent of Code 2021 13 part 1
from collections import defaultdict


caves = defaultdict(list)


def print_list(a):
    for row in a:
        print(row)
    print()


def print_caves():
    for i, value in caves.items():
        print(f'{i:>5} - {value}')


def main():
    # Open input file
    with open('code_input13.txt') as file:
        for line in file:
            pass


if __name__ == "__main__":
    main()
