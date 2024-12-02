def safe(r):
   l = list(map(int, r.split()))
   if l != sorted(l) and l != sorted(l, reverse=True):
      return 0
   for i in range(len(l) - 1):
      d = abs(l[i] - l[i + 1])
      if d < 1 or d > 3:
         return 0
   return 1


print(sum(map(safe, open(0).read().splitlines())))