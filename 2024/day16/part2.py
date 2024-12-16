import heapq


start, end = (0, 0), (0, 0)
maze = []
for r, row in enumerate(open(0).read().splitlines()):
   line = []
   for c, tile in enumerate(row):
      if tile == 'S':
         start = (r, c)
      elif tile == 'E':
         end = (r, c)
      line.append(tile)
   maze.append(line)

visited = set()
to_visit = [(0, start[0], start[1], 0, 1, {start})]
best_score = None
paths = []
while to_visit:
   score, r, c, dr, dc, path = heapq.heappop(to_visit)
   if (r, c) == end:
      if best_score:
         if best_score == score:
            paths.append(path)
         else:
            break
      else:
         best_score = score
         paths.append(path)
   visited.add((r, c, dr, dc))
   for ori in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      nr, nc = r + ori[0], c + ori[1]
      if (nr, nc) not in path and (nr, nc, ori[0], ori[1]) not in visited and maze[nr][nc] != '#':
         s = score + 1
         if ori != (dr, dc):
            s += 1000
         p = path.copy()
         p.add((nr, nc))
         heapq.heappush(to_visit, (s, nr, nc, ori[0], ori[1], p))

best_positions = set()
for path in paths:
   best_positions = best_positions | set(path)
print(len(best_positions))