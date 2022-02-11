# Erik Cooke
# Advent of Code 2021 6 part 1

# Open input file
with open('code_input06.txt') as file:
    for line in file:
        x = line.strip().split(",")
        # print(x)
        x = [int(i) for i in x]
        # print(x)

for i in range(1, 257):
    new_fish = 0
    for j, fish in enumerate(x):
        if fish == 0:
            new_fish += 1
            x[j] = 6
        else:
            x[j] -= 1

    for add_fish in range(new_fish):
        x.append(8)

    # print("Day: ", i, " ", x)
print("Total # Fish: ", len(x))



