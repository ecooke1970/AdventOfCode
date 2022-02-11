# Erik Cooke
# Advent of Code 2021 4 part 2

numbers = []
boards = [[]]
winners = []

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

    print("boards length = ", len(boards))


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

        print_boards()
        # Check rows for a winning card
        for l, board in enumerate(boards):
            if l in winners:
                continue

            for row in board:
                count = 0
                for num in row:
                    if int(num) > 99:
                        count += 1
                        # print("num = ", num, " count = ", count)
                if count >= 5:
                    winners.append(l)

        if len(winners) == len(boards):
            total = winner(winners[-1])
            print("Total = ", total, "Number = ", number)
            return int(total) * int(number)

        # Check columns for a winning card
        for l, board in enumerate(boards):
            if l in winners:
                continue

            for i in range(len(boards[l][0])):
                count = 0
                for j in range(len(boards[l])):
                    if int(boards[l][j][i]) > 99:
                        count += 1

                if count >= 5:
                    winners.append(l)

        if len(winners) == len(boards):
            total = winner(winners[-1])
            print("Total = ", total, "Number = ", number)
            return int(total) * int(number)


print(find_winning_card())

