# Erik Cooke
# Advent of Code 2021 12 part 2
from collections import defaultdict


caves = defaultdict(list)


def print_list(a):
    for row in a:
        print(row)
    print()


def print_caves():
    for i, value in caves.items():
        print(f'{i:>5} - {value}')


def find_paths(start, end, can_twice, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in caves:
        return []
    paths = []
    for node in caves[start]:
        if node.islower():
            if start not in path:
                new_paths = find_paths(node, end, can_twice, path)
                for new_path in new_paths:
                    paths.append(new_path)
            elif can_twice and node not in {'start', 'end'}:
                new_paths = find_paths(node, end, False, path)
                for new_path in new_paths:
                    paths.append(new_path)
        else:
            new_paths = find_paths(node, end, can_twice, path)
            for new_path in new_paths:
                paths.append(new_path)


# def find_paths(s, e, path=[]):
#     # global caves
#     path = path + [s]
#     if s == e:
#         return [path]
#     if s not in caves:
#         return []
#     paths = []
#     for node in caves[s]:
#         if node.isupper() or node not in path:
#             new_paths = find_paths(node, e, path)
#             for new_path in new_paths:
#                 paths.append(new_path)
#         elif not check_for_lower_dupes(path):
#             new_paths = find_paths(node, e, path)
#             for new_path in new_paths:
#                 paths.append(new_path)
#     return paths


def main():
    # Open input file
    with open('code_input12.txt') as file:
        for line in file:
            a, b = line.strip().split("-")
            caves[a].append(b)
            caves[b].append(a)

    print_caves()

    all_paths = find_paths('start', 'end', False)

    print(len(all_paths))

    # print_list(grid)
    # print()
    # create_graph()
    # print_caves()
    # print()
    # all_paths = find_paths('start', 'end')
    #
    # print_list(all_paths)
    # print(len(all_paths))


if __name__ == "__main__":
    main()
