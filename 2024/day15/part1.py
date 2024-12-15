def print_g(g):
   for y in range(len(g)):
      for x in range(len(g[y])):
         print(end=g[y][x])
      print()


directions = {'>': (1, 0), '^': (0, -1), '<': (-1, 0), 'v': (0, 1)}
x, y = 0, 0
grid = []
moves = ""
for r, line in enumerate(open(0).read().splitlines()):
   if line.startswith('#'):
      grid.append(list(line))
      if '@' in line:
         x, y = line.index('@'), r
   elif line:
      moves += line
for m in moves:
   dx, dy = directions[m]
   nx, ny = x + dx, y + dy
   if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]):
      if grid[ny][nx] == '.':
         grid[y][x] = '.'
         grid[ny][nx] = '@'
         x, y = nx, ny
      elif grid[ny][nx] == 'O':
         bx, by = nx + dx, ny + dy
         can_move = False
         while 0 <= by < len(grid) and 0 <= bx < len(grid[by]):
            if grid[by][bx] == '#':
               break
            elif grid[by][bx] == '.':
               can_move = True
               break
            bx, by = bx + dx, by + dy
         if can_move:
            grid[y][x] = '.'
            grid[ny][nx] = '@'
            for i in range(2, abs(by - y) + abs(bx - x) + 1):
               grid[y + i * dy][x + i * dx] = 'O'
            x, y = nx, ny
t = 0
for y in range(len(grid)):
   for x in range(len(grid[y])):
      if grid[y][x] == 'O':
         t += (100 * y + x)
print(t)
