import heapq


def shortest_path(maze, start, end):
   visited = set()
   to_visit = [(0, start[0], start[1], [])]
   while True:
      d, x, y, path = heapq.heappop(to_visit)
      if (d, x, y) in visited:
         continue
      visited.add((d, x, y))
      p = path.copy()
      p.append((x, y))
      if (x, y) == end:
         return p
      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
         nx, ny = x + dx, y + dy
         if maze[ny][nx] != '#' and (nx, ny) not in p:
            heapq.heappush(to_visit, (d + 1, nx, ny, p))
   return None


start, end = None, None
maze = []
for y, line in enumerate(open(0).read().splitlines()):
   if 'S' in line:
      start = (line.index('S'), y)
   if 'E' in line:
      end = (line.index('E'), y)
   maze.append(line)
path = shortest_path(maze, start, end)
t = 0
for i in range(len(path) - 4):
   for j in range(i + 4, len(path)):
      p1, p2 = path[i], path[j]
      delta_path = j - i
      man_dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
      t += man_dist < delta_path and man_dist <= 20 and delta_path - man_dist >= 100
print(t)