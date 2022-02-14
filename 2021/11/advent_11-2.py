# Erik Cooke
# Advent of Code 2021 11 part 2

STEPS = 500
grid = []
flash_count = 0
offset_x = [-1,  0,  1, 1, 1, 0, -1, -1]
offset_y = [-1, -1, -1, 0, 1, 1,  1,  0]


def print_grid():
    for row in grid:
        print(row)
    print()


def process_step():
    # Advance each octopus by 1
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            grid[row][col] += 1


def process_flashes():
    global flash_count
    count = 1
    while count > 0:
        flash_count = 0
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    flash_count += 1
                    continue
                elif grid[y][x] > 9:
                    for (i, j) in zip(offset_x, offset_y):
                        nx = x + i
                        ny = y + j
                        if nx < 0 or nx >= (len(grid[0])) or ny < 0 or ny >= len(grid):
                            continue
                        elif grid[ny][nx] > 0:
                            grid[ny][nx] += 1
                    grid[y][x] = 0
                    count += 1
    print_grid()


if __name__ == "__main__":
    # Open input file
    with open('code_input11.txt') as file:
        for line in file:
            x = line.strip()
            x = [int(i) for i in x]
            grid.append(x)

    print_grid()
    for step in range(1, STEPS + 1):
        # Advance each octopus by 1
        process_step()
        # process grid
        process_flashes()
        if flash_count == len(grid[0]) * len(grid):
            print("Step# = ", step)
            break

    print(flash_count)








