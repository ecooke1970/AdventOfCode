# Erik Cooke
# Advent of Code 2021 12 part 1a
grid = []
caves = {}


def print_list(a):
    for row in a:
        print(row)
    print()


def print_caves():
    for i, value in caves.items():
        print(f'{i:>5} - {value}')


def create_graph():
    for cave in grid:
        if cave[0] == 'end' or cave[1] == 'start':
            continue
        elif cave[0] in caves:
            caves[cave[0]].append(cave[1])
        else:
            caves[cave[0]] = []
            caves[cave[0]].append(cave[1])

        # print("Part 2 ", cave[0], " ", cave[1])
        if cave[1] == 'end' or cave[0] == 'start':
            continue
        elif cave[1] in caves:
            caves[cave[1]].append(cave[0])
        else:
            caves[cave[1]] = []
            caves[cave[1]].append(cave[0])

    # def find_all_paths(graph, start, end, path=[]):
    #     path = path + [start]
    #     if start == end:
    #         return [path]
    #     if not graph.has_key(start):
    #         return []
    #     paths = []
    #     for node in graph[start]:
    #         if node not in path:
    #             newpaths = find_all_paths(graph, node, end, path)
    #             for newpath in newpaths:
    #                 paths.append(newpath)
    #     return paths


def find_paths(s, e, path=[]):
    # global caves
    path = path + [s]
    if s == e:
        return [path]
    if s not in caves:
        return []
    paths = []
    for node in caves[s]:

        if node.isupper() or node not in path:
            new_paths = find_paths(node, e, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


def main():
    # Open input file
    with open('code_input12.txt') as file:
        for line in file:
            x = line.strip().split("-")
            if x[1] == 'start' or x[0] == 'end':
                x[0], x[1] = x[1], x[0]
            grid.append(x)

    print_list(grid)
    print()
    create_graph()
    print_caves()
    print()
    all_paths = find_paths('start', 'end')

    print_list(all_paths)
    print(len(all_paths))


if __name__ == "__main__":
    main()
