# Erik Cooke
# Advent of Code 2021 14 part 1
from collections import defaultdict



def print_list(a):
    for row in a:
        for item in row:
            if item == 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print()






def main():
    # Open input file
    with open('code_input13.txt') as file:
        for line in file:



if __name__ == "__main__":
    main()
