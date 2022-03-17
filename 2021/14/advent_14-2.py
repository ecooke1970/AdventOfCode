# Erik Cooke
# Advent of Code 2021 14 part 2

from collections import Counter

ITERATIONS = 40
insert_rules = {}
polymer = ""


def polymer_pairs():
    global polymer
    new_polymer =

def process_polymer():
    global polymer
    for i in range(ITERATIONS):
        print(i, "BEGIN")
        new_code = polymer[0]
        for j in range(len(polymer) - 1):
            code = polymer[j:j+2]
            x = insert_rules[code]
            new_code += x + code[1]
        polymer = new_code
        print(i, "END")
        # print(polymer)


def main():
    global polymer
    # Open input file
    with open('code_input14.txt') as file:
        polymer = file.readline().strip()
        file.readline()
        for line in file:
            x = line.strip().split(" -> ")
            insert_rules[x[0]] = x[1]

    polymer_pairs()
    process_polymer()
    z = Counter(polymer)
    # print(z)
    values = z.values()
    # print(values)
    print(max(values) - min(values))


if __name__ == "__main__":
    main()
