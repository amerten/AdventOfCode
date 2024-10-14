grid = []
for _ in range(6):
   grid.append([" "] * 50)

for line in open(0).read().splitlines():
   d = line.split()
   if d[0] == 'rect':
      x, y = map(int, d[1].split('x'))
      for r in range(y):
         for c in range(x):
            grid[r][c] = '#'
   else:
      if d[1] == "column":
         x, p = int(d[2].split('=')[1]), int(d[4])
         old = [grid[y][x] for y in range(6)]
         for y in range(6):
            grid[y][x] = old[(y - p) % 6]
      else:
         y, p = int(d[2].split('=')[1]), int(d[4])
         old = grid[y].copy()
         for x in range(50):
            grid[y][x] = old[(x - p) % 50]
t = 0
for r in range(len(grid)):
   for c in range(len(grid[r])):
      t += grid[r][c] == '#'
print(t)

