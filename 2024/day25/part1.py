locks, keys = [], []
is_lock, is_key = False, False
for line in open(0).read().splitlines():
   if line == "":
      if is_lock:
         locks.append(nbs)
      else:
         keys.append(nbs)
      is_lock, is_key = False, False
   else:
      if not is_lock and not is_key:
         nbs = [0] * len(line)
         is_lock, is_key = not '.' in line, '.' in line
      for i, c in enumerate(line):
         nbs[i] += c == '#'
if is_lock:
   locks.append(nbs)
else:
   keys.append(nbs)

t = 0
for k in keys:
   for l in locks:
      t += all(k[i] + l[i] <= 7 for i in range(5))
print(t)