# Erik Cooke

count = 0
count2 = 0

with open('code_input01.txt') as file:
	previous_line = file.readline()
	line = file.readline()
	print(previous_line, "N/A")
	while line:
		if int(line) > int(previous_line):
			print(line, "Increased")
			count += 1
		else:
			print(line, "Decreased")
			count2 += 1
		previous_line = line
		line = file.readline()

print()
print("Increase: ", count)
print("Decrease: ", count2)
print(count + count2)