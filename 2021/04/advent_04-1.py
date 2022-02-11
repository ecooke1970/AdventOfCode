# Erik Cooke
# Advent of Code 2021 4 part 1

numbers = []
boards = [[]]

# Open input file
with open('code_input04.txt') as file:
    # Read first line for the numbers called
    line = file.readline()
    # Add called numbers to the numbers list
    numbers = line.strip().split(",")
    # Read in blank line
    file.readline()

    for line in file:
        if len(line.strip()) == 0:
            boards.append([])
        else:
            boards[-1].append(line.strip().split())


print("numbers = ", numbers)
print("boards = ", boards)


def print_boards():
    global boards
    for board in boards:
        for row in board:
            for num in row:
                print(f'{num:>4}', end="")
            print()
        print()


def winner(i):
    # print("board = ", i)
    count = 0
    for row in boards[i]:
        for num in row:
            if int(num) < 100:
                count += int(num)
    return count


def find_winning_card():
    for number in numbers:
        # print("number = ", number)
        for i, board in enumerate(boards):
            for j, row in enumerate(board):
                for k, num in enumerate(row):
                    if num == number:
                        boards[i][j][k] = int(num) + 100

        # print_boards()

        for l, board in enumerate(boards):
            for row in board:
                count = 0
                for num in row:
                    if int(num) > 99:
                        count += 1
                        # print("num = ", num, " count = ", count)
                if count >= 5:
                    total = winner(l)
                    print("Total = ", total, "Number = ", number)
                    return int(total) * int(number)


print(find_winning_card())

