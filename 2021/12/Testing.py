from collections import defaultdict


def traverse(a, seen, can_twice):
    if a == 'end': return 1
    paths = 0
    for b in connections[a]:
        if b.islower():
            if b not in seen:
                paths += traverse(b, seen | {b}, can_twice)
            elif can_twice and b not in {'start', 'end'}:
                paths += traverse(b, seen | {b}, False)
        else:
            paths += traverse(b, seen, can_twice)
    return paths


connections = defaultdict(list)
with open('code_input12.txt') as file:
    for line in file:
        a, b = line.strip().split('-')
        connections[a].append(b)
        connections[b].append(a)
    print(connections)


print(traverse('start', {'start'}, False))
print(traverse('start', {'start'}, True))