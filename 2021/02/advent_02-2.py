# Erik Cooke
# Advent of Code 2021 2 part 2

direction_list = []
h_position = 0
depth = 0
aim = 0

with open('code_input02.txt') as file:
    for line in file:
        direction_list.append(line.split())

for direction in direction_list:
    if direction[0] == "forward":
        h_position += int(direction[1])
        depth += aim * int(direction[1])
    elif direction[0] == "down":
        aim += int(direction[1])
    elif direction[0] == "up":
        aim -= int(direction[1])

print("Horizontal Position= " + str(h_position))
print("Depth= " + str(depth))
print("Final Value: " + str(h_position * depth))
