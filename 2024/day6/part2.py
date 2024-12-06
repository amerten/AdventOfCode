def loop(g):
   i_d, directions = 0, [(0, -1), (1, 0), (0, 1), (-1, 0)]
   x, y = 0, 0
   for r, line in enumerate(g):
      if '^' in line:
         x, y = line.index('^'), r
         break
   visited = {(x, y)}
   walls = set()
   while True:
      dir = directions[i_d]
      nx, ny = x + dir[0], y + dir[1]
      if 0 <= ny < len(g) and 0 <= nx < len(g[ny]):
         if g[ny][nx] == '#':
            if ((nx, ny) + dir) in walls:
               return visited, True
            walls.add((nx, ny) + dir)
            i_d = (i_d + 1) % len(directions)
         else:
            x, y = nx, ny
            visited.add((x, y))
      else:
         return visited, False


grid = list(map(list, open(0).read().splitlines()))
visited, _ = loop(grid)
t = 0
for px, py in visited:
   if grid[py][px] != '^':
      grid[py][px] = '#'
      _, is_loop = loop(grid)
      t += is_loop
      grid[py][px] = '.'
print(t)
