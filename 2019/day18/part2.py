import networkx as nx
from heapq import heappush, heappop

data = [list(l.strip()) for l in open(0).read().splitlines()]

# INIT GRID

middle = (len(data) // 2, len(data[0]) // 2)

data[middle[0] - 1][middle[1]] = '#'
data[middle[0] + 1][middle[1]] = '#'
data[middle[0]][middle[1] - 1] = '#'
data[middle[0]][middle[1] + 1] = '#'
data[middle[0]][middle[1]] = '#'

data[middle[0] - 1][middle[1] - 1] = '1'
data[middle[0] - 1][middle[1] + 1] = '2'
data[middle[0] + 1][middle[1] + 1] = '3'
data[middle[0] + 1][middle[1] - 1] = '4'

# INIT GRAPH

positions = {}
G = nx.Graph()
keys = set()
for r, row in enumerate(data):
    for c, cell in enumerate(row):
        if cell != '#':
            if data[r][c + 1] != '#':
                G.add_edge((r, c), (r, c + 1))
            if data[r + 1][c] != '#':
                G.add_edge((r, c), (r + 1, c))
            if cell != '.' and ((97 <= ord(cell) <= 122) or cell.isdigit()):
                positions[cell] = (r, c)
                if 97 <= ord(cell) <= 122:
                    keys.add(cell)


# INIT PATHS

paths = {}
for start in positions:
    for end in positions:
        if start != end:
            try:
                path = nx.astar_path(G, positions[start], positions[end])
                doors = []
                for pos in path[1:-1]:
                    if 65 <= ord(data[pos[0]][pos[1]]) <= 90:
                        doors.append(data[pos[0]][pos[1]])
                paths[start + end] = (len(path) - 1, doors)
            except:
                continue

# ALGO


def can_go(keys_found, doors):
    return len(set([chr(ord(d) + 32) for d in doors]) - keys_found) == 0


seen = set()
q = [(0, '1', '2', '3', '4', frozenset())]

while q:
    node = heappop(q)
    if len(node[5]) == len(keys):
        print(node[0])
        break
    sn = (node[1], node[2], node[3], node[4], node[5])
    if sn in seen:
        continue
    seen.add(sn)
    keys_left = keys - node[5]
    for i in range(4):
        start = node[i + 1]
        for k in keys_left:
            if (start + k) in paths and can_go(node[5], paths[start + k][1]):
                new_keys = node[5] | frozenset(k)
                new_node = [node[0] + paths[start + k][0], node[1], node[2], node[3], node[4], new_keys]
                new_node[i + 1] = k
                heappush(q, tuple(new_node))

