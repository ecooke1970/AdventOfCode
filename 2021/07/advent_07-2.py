# Erik Cooke
# Advent of Code 2021 7 part 2
lowest_fuel = 999999999
position = None

# Open input file
with open('code_input07.txt') as file:
    total = 0
    for line in file:
        x = line.strip().split(",")
        x = [int(i) for i in x]
        x.sort()
        print(x)

for i in range(x[0], x[-1] + 1):
    counter = 0
    for j in x:
        # counter += sum(range(1, abs(j - i) + 1))
        counter += int((abs(j - i) + 1) * (abs(j - i) / 2))
        # (x + 1) * (x / 2)

    if lowest_fuel > counter:
        lowest_fuel = counter
        position = i

print("Best position is: ", position)
print("Lowest Fuel Position: ", lowest_fuel)
