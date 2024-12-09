s = open(0).read().strip()
l = []
block, i_block = True, 0
for size in s:
   size = int(size)
   id = i_block if block else -1
   l.append((size, id))
   if block:
      i_block += 1
   block = not block
while id > 0:
   j = len(l) - 1
   while j >= 0 and l[j][1] != id:
      j -= 1
   if j < 0:
      break
   i = 0
   while i < j:
      while l[i][1] != -1:
         i += 1
      if i >= j:
         break
      i_size, i_id = l[i]
      j_size, j_id = l[j]
      if i_size >= j_size:
         l.insert(i, l[j])
         l[j + 1] = (j_size, -1)
         if i_size == j_size:
            l.pop(i + 1)
         else:
            l[i + 1] = (i_size - j_size, -1)
         break
      i += 1
   id -= 1
t, i = 0, 0
for size, id in l:
   if id == -1:
      i += size
      continue
   for _ in range(size):
      t += (i * id)
      i += 1
print(t)