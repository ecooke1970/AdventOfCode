# Author: Erik Cooke
# Advent of Code 2021 15 part 1
import heapq

grid = []
start = '0, 0'


def dijkstra(adj, start, end):
    d = {start: 0}
    parent = {start: None}
    pq = [(0, start)]
    visited = set()
    while pq:
        du, u = heapq.heappop(pq)
        if u in visited: continue
        if u == end:
            break
        visited.add(u)
        for v, weight in adj[u]:
            if v not in d or d[v] > du + weight:
                d[v] = du + weight
                parent[v] = u
                heapq.heappush(pq, (d[v], v))

    return parent, d


def main():
    with open('code_input15.txt') as file:
        for line in file:
            x = line.strip()
            temp = []
            for num in x:
                temp.append(num)
            grid.append(temp)

    end = (len(grid) - 1, len(grid[0]) - 1)

    adj = {}
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            # print(f"{x}{y} col: {col}")
            adj['str(x), str(y)'] = col

    print(f"start = {start}, end = {end}")

    print(dijkstra(adj, start, end))



if __name__ == "__main__":
    main()

