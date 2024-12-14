width, height = 101, 103
seconds = 100
nb_robots = [0, 0, 0, 0]  # top-left, top-right, bott-right, bott-left
for line in open(0).read().splitlines():
   a, b = line.split()
   x, y = map(int, a.split('=')[1].split(','))
   dx, dy = map(int, b.split('=')[1].split(','))
   x = (x + dx * seconds) % width
   y = (y + dy * seconds) % height
   top = 0 <= y < height // 2
   bottom = height // 2 + 1 <= y < height
   left = 0 <= x < width // 2
   right = width // 2 + 1 <= x < width
   if top:
      if left:
         nb_robots[0] += 1
      elif right:
         nb_robots[1] += 1
   elif bottom:
      if left:
         nb_robots[3] += 1
      elif right:
         nb_robots[2] += 1
t = 1
for n in nb_robots:
   t *= n
print(t)
