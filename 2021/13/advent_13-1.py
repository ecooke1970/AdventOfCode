# Erik Cooke
# Advent of Code 2021 13 part 1
from collections import defaultdict

coordinates = []
flip = []
grid = []


def print_list(a):
    for row in a:
        for item in row:
            if item == 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print()


def flip_page(flip_list):
    global grid
    # flip_count = 0
    for i, j in flip_list:
        if i == 'y':
            # print("Flip Y", j)
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] == 1 and y > j:
                        diff = j - (y - j)
                        grid[diff][x] = 1
            grid = grid[:-j]
        elif i == 'x':
            # print("Flip X", j)
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] == 1 and x > j:
                        diff = j - (x - j)
                        grid[y][diff] = 1
            for k, row in enumerate(grid):
                grid[k] = row[:j]
        # flip_count += 1
        # if flip_count >= 1:
        #     break


def fill_grid():
    for x, y in coordinates:
        grid[y][x] = 1


def count_grid():
    num = 0
    for row in grid:
        num += row.count(1)
    return num


def main():
    global grid
    # Open input file
    high_x, high_y = 0, 0
    with open('code_input13.txt') as file:
        for line in file:
            if ',' in line:
                x, y = line.strip().split(',')
                x, y = int(x), int(y)
                high_x = x if x > high_x else high_x
                high_y = y if y > high_y else high_y
                coordinates.append([x, y])
            elif 'fold' in line:
                x = line.strip().split('=')
                i = [x[0][-1], int(x[1])]
                flip.append(i)

    grid = [[0 for i in range(high_x + 1)] for j in range(high_y + 1)]

    fill_grid()

    flip_page(flip)

    print_list(grid)
    # print(count_grid())


if __name__ == "__main__":
    main()
