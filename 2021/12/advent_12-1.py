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
        print("Part 1 ", cave[0], " ", cave[1])
        if cave[0] == 'end' or cave[1] == 'start':
            continue
        elif cave[0] in caves:
            caves[cave[0]].append(cave[1])
        else:
            caves[cave[0]] = []
            caves[cave[0]].append(cave[1])

        print(caves)

        print("Part 2 ", cave[0], " ", cave[1])
        if cave[1] == 'end' or cave[0] == 'start':
            continue
        elif cave[1] in caves:
            caves[cave[1]].append(cave[0])
        else:
            caves[cave[1]] = []
            caves[cave[1]].append(cave[0])

        print(caves)
        print()


if __name__ == "__main__":
    # Open input file
    with open('code_input12.txt') as file:
        for line in file:
            x = line.strip().split("-")
            grid.append(x)

    # print_grid()
    create_graph()








