# Erik Cooke
# Advent of Code 2021 12 part 1
grid = []
caves = {}


def print_grid():
    for row in grid:
        print(row)
    print()


def create_graph():
    for cave in grid:
        caves[cave[0]] = [cave[1]]

    print(caves)


if __name__ == "__main__":
    # Open input file
    with open('code_input12.txt') as file:
        for line in file:
            x = line.strip().split("-")
            grid.append(x)

    print_grid()
    create_graph()








