from heapq import heappush, heappop


maze = open(0).read().splitlines()
portals = {}
max_c = 0


def is_outer(pos):
    return pos[0] == 2 or pos[1] == 2 or pos[0] == len(maze) - 3 or pos[1] == len(maze[0]) - 3


for r in range(len(maze)):
    for c in range(len(maze[r])):
        if maze[r][c].isupper():
            name, pos = None, None
            if r > 0 and maze[r - 1][c] == '.':
                name = maze[r][c] + maze[r + 1][c]
                pos = (r - 1, c)
            elif r < len(maze) - 1 and maze[r + 1][c] == '.':
                name = maze[r - 1][c] + maze[r][c]
                pos = (r + 1, c)
            elif c > 0 and maze[r][c - 1] == '.':
                name = maze[r][c] + maze[r][c + 1]
                pos = (r, c - 1)
                max_c = max(max_c, c - 1)
            elif c < len(maze[r]) - 1 and maze[r][c + 1] == '.':
                name = maze[r][c - 1] + maze[r][c]
                pos = (r, c + 1)

            if name and pos:
                if name in ['ZZ', 'AA']:
                    portals[name] = pos
                elif name not in portals:
                    portals[name] = [pos]
                else:
                    portals[name].append(pos)

paths = {}
for portal in portals:
    if portal not in ['AA', 'ZZ']:
        paths[portals[portal][0]] = portals[portal][1]
        paths[portals[portal][1]] = portals[portal][0]


q = [(0, 0, portals['AA'])]
seen = set()

while q:
    d, l, p = heappop(q)
    if l == 0 and p == portals['ZZ']:
        print(d)
        break
    if (l, p) in seen:
        continue
    seen.add((l, p))
    for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        np = (p[0] + dir[0], p[1] + dir[1])
        delta = 0
        if maze[np[0]][np[1]].isupper() and p in paths:
            if l == 0 and is_outer(p):
                continue
            np = paths[p]
            delta = -1 if is_outer(p) else 1
        elif maze[np[0]][np[1]] != '.':
            continue
        heappush(q, (d + 1, l + delta, np))
