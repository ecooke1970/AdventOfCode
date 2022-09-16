# Author: Erik Cooke
# Advent of Code 2021 15 part 1
grid = []


def main():
    with open('code_input15.txt') as file:
        for line in file:
            x = line.strip()
            temp = []
            for num in x:
                temp.append(int(num))
            grid.append(temp)


if __name__ == "__main__":
    main()

