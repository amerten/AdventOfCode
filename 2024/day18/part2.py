import heapq


memory = set()
for i, line in enumerate(open(0).read().splitlines()):
   c, r = map(int, line.split(','))
   memory.add((c, r))
   visited = set()
   to_visit = [(0, 0, 0)]
   end = (70, 70)
   found = False
   while to_visit:
      d, x, y = heapq.heappop(to_visit)
      if (x, y) == end:
         found = True
         break
      if (x, y) in visited:
         continue
      visited.add((x, y))
      for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
         nx, ny = x + dx, y + dy
         if (nx, ny) not in memory and 0 <= nx <= end[0] and 0 <= ny <= end[1]:
            heapq.heappush(to_visit, (d + 1, nx, ny))
   if not found:
      print(str(c) + "," + str(r))
      break