# Erik Cooke
# Advent of Code 2021 11 part 1

STEPS = 2
grid = []


def print_grid():
    for row in grid:
        print(row)
    print()


if __name__ == "__main__":
    # Open input file
    with open('code_input11.txt') as file:
        for line in file:
            x = line.strip()
            x = [int(i) for i in x]
            grid.append(x)

    print_grid()

    for step in range(STEPS):
        # Advance each octopus by 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                grid[row][col] += 1
        print_grid()

        # process grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                 






