# Erik Cooke
# Advent of Code 2021 6 part 2

DAYS = 256
lantern_fish = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}


def process_fish():
    global lantern_fish
    for i in range(1, DAYS + 1):
        print("Day: ", i)
        new_fish = lantern_fish['0']
        for fish in (range(8)):
            lantern_fish[str(fish)] = lantern_fish[str(fish + 1)]
        lantern_fish['8'] = new_fish
        lantern_fish['6'] += new_fish
        print(lantern_fish)


def add_up_fish():
    total_fish = 0
    for i in lantern_fish:
        total_fish += lantern_fish[str(i)]

    return total_fish


# Open input file
with open('code_input06.txt') as file:
    for line in file:
        x = line.strip().split(",")
        # print(x)
        for j in x:
            lantern_fish[str(j)] += 1

print("Starting fish: ", lantern_fish)
process_fish()
print("Total Fish: ", add_up_fish())
