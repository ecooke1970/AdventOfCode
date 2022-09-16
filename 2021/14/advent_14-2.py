# Erik Cooke
# Advent of Code 2021 14 part 2

from collections import Counter, defaultdict


ITERATIONS = 40
insert_rules = {}
first_polymer = ""
polymer = defaultdict(int)
count_polymers = defaultdict(int)


def polymer_pairs():
    global first_polymer
    for i in range(len(first_polymer) - 1):
        polymer[first_polymer[i] + first_polymer[i+1]] += 1
        count_polymers[first_polymer[i]] += 1
    count_polymers[first_polymer[-1]] += 1


def process_polymer():
    global polymer
    for i in range(ITERATIONS):
        # print(f"start: {i}")
        temp_polymer = defaultdict(int)
        for item, value in polymer.items():
            # print("item:", item)
            # count_polymers[insert_rules[item]] += 1
            # print("count: ", count_polymers)
            temp_polymer[item[0] + insert_rules[item]] += value
            temp_polymer[insert_rules[item] + item[1]] += value
            count_polymers[insert_rules[item]] += value
        # print("End")
        polymer = temp_polymer
        # print(f"polymer: {polymer}")
        # print()


def print_count():
    for key, value in count_polymers.items():
        print(f"{key}: {value}")


def main():
    global first_polymer
    # Open input file
    with open('code_input14.txt') as file:
        first_polymer = file.readline().strip()
        file.readline()
        for line in file:
            x = line.strip().split(" -> ")
            insert_rules[x[0]] = x[1]

    polymer_pairs()
    process_polymer()
    print_count()
    totals = Counter(count_polymers).values()
    print(f"Answer: {max(totals) - min(totals)}")


if __name__ == "__main__":
    main()
