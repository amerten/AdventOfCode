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
to_visit = [(0, start[0], start[1], 0, 1)]
while to_visit:
   score, r, c, dr, dc = heapq.heappop(to_visit)
   if (r, c) == end:
      print(score)
      break
   visited.add((r, c, dr, dc))
   for ori in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      if ori != (dr, dc):
         state = (r, c, ori[0], ori[1])
         if state in visited:
            continue
         heapq.heappush(to_visit, (score + 1000, r, c, ori[0], ori[1]))
   if (r + dr, c + dc, dr, dc) not in visited and maze[r + dr][c + dc] != '#':
      heapq.heappush(to_visit, (score + 1, r + dr, c + dc, dr, dc))