# Erik Cooke
# Advent of code 2021-01 part 2

count = 0
count2 = 0
measurements = []

with open('code_input01.txt') as file:
	for line in file:
		measurements.append(int(line))

	previous_amt = measurements[0] + measurements[1] + measurements[2]
	for i in range(1, len(measurements) - 2):
		current_amt = measurements[i] + measurements[i + 1] + measurements[i + 2]
		print("current " + str(current_amt) + " previous " + str(previous_amt))
		if current_amt > previous_amt:
			count += 1

		previous_amt = current_amt

	print(count)
