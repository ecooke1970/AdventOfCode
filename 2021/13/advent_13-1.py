# Erik Cooke
# Advent of Code 2021 13 part 1
from collections import defaultdict

coordinates = []
flip = []


def print_list(a):
    for row in a:
        print(row)
    print()


def flip_page(flip_list, grid):
    print(flip_list)
    for i, j in flip_list:
        if i == 'y':
            print("Flip Y", j)
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] == 1 and y > j:
                        grid[y][x] = 0
                        diff = j - (y - j)
                        grid[diff][x] = 1
                        print(diff)
        else:
            print("Flip X", j)
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] == 1 and x > j:
                        grid[y][x] = 0
                        diff = j - (x - j)
                        grid[y][diff] = 1


def fill_grid(grid):
    for x, y in coordinates:
        grid[y][x] = 1


def count_grid(grid):
    num = 0
    for row in grid:
        num += row.count(1)
    return num


def main():
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
    # arr = [[0 for i in range(cols)] for j in range(rows)]
    fill_grid(grid)
    # print(high_x, high_y)
    print_list(grid)
    # print_list(coordinates)
    flip_page(flip, grid)
    print_list(grid)

    print(count_grid(grid))


if __name__ == "__main__":
    main()
