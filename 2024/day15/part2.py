def print_g(g):
   for y in range(len(g)):
      for x in range(len(g[y])):
         print(end=g[y][x])
      print()


def move_boxes(g, x, y, dx, dy):
   if abs(dx) == 1:
      if g[y][x + 2 * dx] == '.':
         g[y][x + dx] = '[' if dx > 0 else ']'
         g[y][x + 2 * dx] = ']' if dx > 0 else '['
         g[y][x] = '.'
      else:
         move_boxes(g, x + 2 * dx, y, dx, dy)
         move_boxes(g, x, y, dx, dy)
   else:
      if g[y][x] == '.':
         return
      dbx = 1 if g[y][x] == '[' else -1
      if g[y + dy][x] == '.' and g[y + dy][x + dbx] == '.':
         g[y + dy][x] = g[y][x]
         g[y + dy][x + dbx] = g[y][x + dbx]
         g[y][x] = '.'
         g[y][x + dbx] = '.'
      else:
         move_boxes(g, x, y + dy, dx, dy)
         move_boxes(g, x + dbx, y + dy, dx, dy)
         move_boxes(g, x, y, dx, dy)

def can_move_boxes(g, x, y, dx, dy):
   if abs(dx) == 1:
      i = 1
      while 1 <= x + dx * i < len(g[y]) - 1:
         if g[y][x + dx * i] == '#':
            return False
         if g[y][x + dx * i] == '.':
            return True
         i += 1
      return False
   else:
      if g[y][x] == '#':
         return False
      if g[y][x] == '.':
         return True
      if g[y][x] == '[':
         return True and can_move_boxes(g, x, y + dy, dx, dy) and can_move_boxes(g, x + 1, y + dy, dx, dy)
      return True and can_move_boxes(g, x, y + dy, dx, dy) and can_move_boxes(g, x - 1, y + dy, dx, dy)


def move_if_possible(g, x, y, dx, dy):
   nx, ny = x + dx, y + dy
   if g[ny][nx] == '#':
      return x, y
   if g[ny][nx] == '.':
      g[ny][nx] = '@'
      g[y][x] = '.'
      return nx, ny
   if can_move_boxes(g, nx, ny, dx, dy):
      move_boxes(g, nx, ny, dx, dy)
      g[ny][nx] = '@'
      g[y][x] = '.'
      return nx, ny
   return x, y


# --------------------------------------------------------------------


directions = {'>': (1, 0), '^': (0, -1), '<': (-1, 0), 'v': (0, 1)}
x, y = 0, 0
grid = []
moves = ""
for r, line in enumerate(open(0).read().splitlines()):
   if line.startswith('#'):
      l = []
      for c, tile in enumerate(line):
         if tile == '#':
            l.append('#')
            l.append('#')
         elif tile == 'O':
            l.append('[')
            l.append(']')
         elif tile == '.':
            l.append('.')
            l.append('.')
         else:
            l.append('@')
            l.append('.')
            x, y = 2 * c, r
      grid.append(l)
   elif line:
      moves += line
for m in moves:
   dx, dy = directions[m]
   x, y = move_if_possible(grid, x, y, dx, dy)
t = 0
for y in range(len(grid)):
   for x in range(len(grid[y])):
      if grid[y][x] == '[':
         t += (100 * y + x)
print(t)
