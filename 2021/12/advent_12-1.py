# Erik Cooke
# Advent of Code 2021 12 part 1
grid = []


def print_grid():
    for row in grid:
        print(row)
    print()


if __name__ == "__main__":
    # Open input file
    with open('code_input12.txt') as file:
        for line in file:
            x = line.strip().split("-")
            grid.append(x)

    print_grid()








