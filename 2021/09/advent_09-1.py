# Erik Cooke
# Advent of Code 2021 9 part 1
grid = []
risk_level = 0


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

            count = 0
            for (i, j) in zip(offset_x, offset_y):
                nx = x + i
                ny = y + j
                print("x = ", x, "y = ", y, "nx = ", nx, "ny = ", ny)
                if nx < 0 or nx >= (len(grid[0])) or ny < 0 or ny >= len(grid):
                    count += 1
                    continue
                else:
                    neighbor = grid[ny][nx]
                    if neighbor > grid[y][x]:
                        count += 1

            if count >= 4:
                risk_level += (grid[y][x] + 1)
                print("risk level = ", risk_level)



    print_grid()
    print(risk_level)
