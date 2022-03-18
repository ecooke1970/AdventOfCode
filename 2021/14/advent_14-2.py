# Erik Cooke
# Advent of Code 2021 14 part 2

from collections import Counter, defaultdict


ITERATIONS = 10
insert_rules = {}
first_polymer = ""
polymer = defaultdict(int)
count_polymers = defaultdict(int)


def polymer_pairs():
    global first_polymer, count_polymers
    for i in range(len(first_polymer) - 1):
        polymer[first_polymer[i] + first_polymer[i+1]]
        count_polymers[first_polymer[i]] += 1
    count_polymers[first_polymer[-1]] += 1
    # print(polymer)
    # print("Count: ", count_polymers)


def process_polymer():
    global polymer, count_polymers
    for i in range(ITERATIONS):
        temp_polymer = defaultdict(int)
        for item in polymer:
            print("item:", item)
            count_polymers[insert_rules[item]] += 1
            print("count: ", count_polymers)

            temp_polymer[item[0] + insert_rules[item]] += polymer[item] + 1
            temp_polymer[insert_rules[item] + item[1]] += polymer[item] + 1
        print("End")
        polymer = temp_polymer
        print("polymer:", polymer)
    print(count_polymers)


# def count_letters():
#     global polymer
#     count = defaultdict(int)
#     for item in polymer:
#         count[item[0]] += polymer.get(item)
#         count[item[1]] += polymer.get(item)
#     print(count)


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
    # count_letters()
    # z = Counter(new_polymer)
    # print(z)
    # values = z.values()
    # print(values)
    # print(max(values) - min(values))


if __name__ == "__main__":
    main()
