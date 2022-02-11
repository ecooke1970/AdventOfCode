# Erik Cooke
# Advent of Code 2021 5 part 2
import re

grid = {}
line_count = 0


def plot_line(x1, y1, x2, y2):
    # Check if x coordinates are the same
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for i in range(y1, y2 + 1):
            key = str(x1) + "," + str(i)
            if key in grid:
                grid[key] += 1
            else:
                grid[key] = 1

    elif y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for i in range(x1, x2 + 1):
            key = str(i) + "," + str(y1)
            if key in grid:
                grid[key] += 1
            else:
                grid[key] = 1
    else:
        if x1 > x2 and y1 > y2:
            start_x, stop_x, step_x = x1, x2 - 1, -1
            start_y, stop_y, step_y = y1, y2 - 1, -1
        elif x1 > x2:
            start_x, stop_x, step_x = x1, x2 - 1, -1
            start_y, stop_y, step_y = y1, y2 + 1, 1
        elif y1 > y2:
            start_x, stop_x, step_x = x1, x2 + 1, 1
            start_y, stop_y, step_y = y1, y2 - 1, -1
        else:
            start_x, stop_x, step_x = x1, x2 + 1, 1
            start_y, stop_y, step_y = y1, y2 + 1, 1

        for i, j in zip(range(start_x, stop_x, step_x), range(start_y, stop_y, step_y)):
            key = str(i) + "," + str(j)
            if key in grid:
                grid[key] += 1
            else:
                grid[key] = 1


# Open input file
with open('code_input05a.txt') as file:
    for line in file:
        line_count += 1
        temp = line.strip()
        x = []
        x = re.split(',| -> ', temp)
        # print(x)
        x = [int(i) for i in x]
        plot_line(x[0], x[1], x[2], x[3])

count = 0
grid_count = 0

for item in grid:
    grid_count += 1
    # print("item=", item, " value = ", grid[item])
    if int(grid[item]) >= 2:
        count += 1

print("grid size = ", len(grid))
print("grid count = ", grid_count)
print("line count = ", line_count)
print("count = ", count)


