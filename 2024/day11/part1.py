NB_BLINK = 25
l = list(map(int, open(0).read().split()))
for _ in range(NB_BLINK):
   i = 0
   while True:
      s = str(l[i])
      if len(s) % 2 == 0:
         l[i] = int(s[:len(s) // 2])
         l.insert(i + 1, int(s[len(s) // 2:]))
         i += 2
      else:
         l[i] = 1 if l[i] == 0 else l[i] * 2024
         i += 1
      if i >= len(l):
         break
print(len(l))