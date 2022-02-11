# Erik Cooke
# Advent of Code 2021 8 part 1


# Open input file
with open('code_input08.txt') as file:
    total = 0
    for line in file:
        x = line.strip().split(" | ")
        x = x[1].split()

        for i in x:
            j = len(i)
            if j == 2 or j == 3 or j == 4 or j == 7:
                print(len(i), " ", i)
                total += 1

print(total)
