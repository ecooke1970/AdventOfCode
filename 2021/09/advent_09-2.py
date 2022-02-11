# Erik Cooke
# Advent of Code 2021 9 part 2
grid = []
risk_level = 0
basin_set = set()
basins = []


def find_basin(x, y):
    if str(x) + "," + str(y) in basin_set:
        return 0
    basin_set.add(str(x) + "," + str(y))
    if grid[y][x] == 9:
        return 0
    # print("x:",x, " ", "y:", y)
    count = 1
    # Search up
    if not y - 1 < 0:
        count += find_basin(x, y - 1)
    # Search right
    if not x + 1 > len(grid[0]) - 1:
        count += find_basin(x + 1, y)
    # Search down
    if not y + 1 > len(grid) - 1:
        count += find_basin(x, y + 1)
    # Search left
    if not x - 1 < 0:
        count += find_basin(x - 1, y)

    # print("count: ", count)
    return count


def print_grid():
    for row in grid:
        print(row)


if __name__ == "__main__":
    # Open input file
    with open('code_input09.txt') as file:
        total = 0
        for line in file:
            x = line.strip()
            x = [int(i) for i in x]
            grid.append(x)

    offset_x = [0, 1, 0, -1]
    offset_y = [-1, 0, 1, 0]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            basin_size = 0
            count = 0
            for (i, j) in zip(offset_x, offset_y):
                nx = x + i
                ny = y + j
                # print("x = ", x, "y = ", y, "nx = ", nx, "ny = ", ny)
                if nx < 0 or nx >= (len(grid[0])) or ny < 0 or ny >= len(grid):
                    count += 1
                    continue
                else:
                    neighbor = grid[ny][nx]
                    if neighbor > grid[y][x]:
                        count += 1

            if count >= 4:
                basin_size = find_basin(x, y)
                risk_level += (grid[y][x] + 1)
                basins.append(basin_size)
                # print("risk level = ", risk_level)
                # print("basin size for ", x, ",", y, " = ", basin_size)

    basins.sort()
    answer = basins[-1] * basins[-2] * basins[-3]
    print("Answer = ", answer)
    # print_grid()
    # print(risk_level)
    print(basins)
    # print("basin set = ", basin_set)
    print(len(basin_set))
