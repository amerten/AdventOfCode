s = open(0).read().strip()
l = []
block, i_block = True, 0
for c in s:
   c = int(c)
   id = i_block if block else -1
   for _ in range(c):
      l.append(id)
   if block:
      i_block += 1
   block = not block
t = 0
i, j = 0, len(l) - 1
while i <= j:
   if l[i] == -1:
      while l[j] == -1 and j > i:
         j -= 1
      if j > i:
         t += (i * l[j])
         j -= 1
   else:
      t += (i * l[i])
   i += 1
print(t)
