i_d, directions = 0, [(0, -1), (1, 0), (0, 1), (-1, 0)]
x, y = 0, 0
g = []
for r, line in enumerate(open(0).read().splitlines()):
   if '^' in line:
      x, y = line.index('^'), r
   g.append(line)
visited = {(x, y)}
while True:
   nx, ny = x + directions[i_d][0], y + directions[i_d][1]
   if 0 <= ny < len(g) and 0 <= nx < len(g[ny]):
      if g[ny][nx] == '#':
         i_d = (i_d + 1) % len(directions)
      else:
         x, y = nx, ny
         visited.add((x, y))
   else:
      print(len(visited))
      break