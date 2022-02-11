# Erik Cooke
# Advent of Code 2021 8 part 2


# Open input file
with open('code_input08.txt') as file:
    total = 0
    for line in file:
        numbers = {}
        x = line.strip().split(" | ")
        segments = x[0].split()
        segments = ["".join(sorted(x)) for x in segments]
        segments.sort(key=len)
        output = x[1].split()
        output = ["".join(sorted(x)) for x in output]

        for x in segments:
            if len(x) == 2:
                numbers[1] = x
            elif len(x) == 4:
                numbers[4] = x
            elif len(x) == 3:
                numbers[7] = x
            elif len(x) == 7:
                numbers[8] = x
            elif len(x) == 5:
                if numbers[7][0] in x and numbers[7][1] in x and numbers[7][2] in x:
                    numbers[3] = x
                else:
                    matches = 0
                    for i in numbers[4]:
                        if i in x:
                            matches += 1
                    if matches == 3:
                        numbers[5] = x
                    elif matches == 2:
                        numbers[2] = x
            else:
                matches = 0
                for i in numbers[7]:
                    if i in x:
                        matches += 1
                if matches == 2:
                    numbers[6] = x
                else:
                    matches = 0
                    for i in numbers[4]:
                        if i in x:
                            matches += 1
                    if matches == 3:
                        numbers[0] = x
                    else:
                        numbers[9] = x
        num = ""
        for x in output:
            for i, j in numbers.items():
                # print(i, " ", j, " ", x)
                if j == x:
                    num += str(i)
                    continue
                    # print("num = ", num )

        total += int(num)

        # print("segments = ", segments)
        # print("output = ", output)
        # print("numbers = ", numbers)
        # print("number = ", num)
        # print()

print("Total = ", total)


