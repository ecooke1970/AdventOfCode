# Erik Cooke
# Advent of Code 2021 3 part 2

input_data = []
input_data_co2 = []
temp_data = []

with open('code_input03.txt') as file:
    for line in file:
        input_data.append(line.strip())
        input_data_co2.append(line.strip())

for i in range(len(input_data[0])):
    count = 0
    if len(input_data) == 1:
        break
    else:
        for entry in input_data:
            count += int(entry[i])

        if count >= len(input_data) / 2:
            for entry in input_data:
                if int(entry[i]) == 1:
                    temp_data.append(entry)
        else:
            for entry in input_data:
                if int(entry[i]) == 0:
                    temp_data.append(entry)

    input_data = temp_data
    temp_data = []

for i in range(len(input_data_co2[0])):
    count = 0
    if len(input_data_co2) == 1:
        break
    else:
        for entry in input_data_co2:
            count += int(entry[i])

        if count >= len(input_data_co2) / 2:
            for entry in input_data_co2:
                if int(entry[i]) == 0:
                    temp_data.append(entry)
        else:
            for entry in input_data_co2:
                if int(entry[i]) == 1:
                    temp_data.append(entry)

    input_data_co2 = temp_data
    temp_data = []

print()
print("Oxygen Generator Rating binary = " + str(input_data))
print("Oxygen Generator Rating decimal = ", int(input_data[0], 2))
print()
print("CO2 Scrubber Rating binary = " + str(input_data_co2))
print("CO2 Scrubber Rating decimal = ", int(input_data_co2[0], 2))
print()
print("Life support rating = ", int(input_data[0], 2) * int(input_data_co2[0], 2))
