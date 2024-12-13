t = 0
ax, ay, bx, by, X, Y = 0, 0, 0, 0, 0, 0
for line in open(0).read().splitlines():
   if line.startswith('Button'):
      _, b, raw_x, raw_y = line.replace(',', '').split()
      if b.startswith('A'):
         ax, ay = int(raw_x.split('+')[1]), int(raw_y.split('+')[1])
      else:
         bx, by = int(raw_x.split('+')[1]), int(raw_y.split('+')[1])
   elif line.startswith('Prize'):
      raw_x, raw_y = line.split(', ')
      x, y = int(raw_x.split('=')[1]), int(raw_y.split('=')[1])
   else:
      d = by * ax - ay * bx
      if d == 0:
         continue
      nb = (ax * y - ay * x) / d
      if int(nb) != nb or nb < 0 or nb > 100:
         continue
      na = (x - bx * nb) / ax
      if int(na) != na or na < 0 or na > 100:
         continue
      t += int(na * 3 + nb)
print(t)