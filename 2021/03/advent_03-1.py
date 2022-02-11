# Erik Cooke
# Advent of Code 2021 3 part 1

gamma = ""
epsilon = ""
diag_report = []

with open('code_input03.txt') as file:
    for line in file:
        diag_report.append(line.strip())
    print(diag_report)

for i in range(len(diag_report[0])):
    count = 0
    for entry in diag_report:
        print("entry " + entry)
        count += int(entry[i])

    if count > len(diag_report) / 2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print()
print("gamma = " + gamma)
print("epsilon = " + epsilon)
print("gamma in decimal = ", int(gamma, 2))
print("epsilon in decimal = ", int(epsilon, 2))
print()
print("Power Consumption = ", int(gamma, 2) * int(epsilon, 2))

