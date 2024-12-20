import heapq


start, end = None, None
maze = []
for y, line in enumerate(open(0).read().splitlines()):
   if 'S' in line:
      start = (line.index('S'), y)
   if 'E' in line:
      end = (line.index('E'), y)
   maze.append(line)

shortcuts = []
best_path = None
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
      best_path = p
      break
   for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nx, ny = x + dx, y + dy
      if maze[ny][nx] == '#':
         nx, ny = nx + dx, ny + dy
         if 0 <= ny < len(maze) and 0 <= nx < len(maze[ny]) and maze[ny][nx] != '#':
            shortcuts.append((x, y, nx, ny))
   for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nx, ny = x + dx, y + dy
      if maze[ny][nx] != '#' and (nx, ny) not in p:
         heapq.heappush(to_visit, (d + 1, nx, ny, p))
t = 0
for x, y, nx, ny in shortcuts:
   if (x, y) in best_path and (nx, ny) in best_path:
      pico_saved = best_path.index((nx, ny)) - best_path.index((x, y)) - 2
      t += (pico_saved >= 100)
print(t)