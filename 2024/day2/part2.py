def safe(l):
   if l != sorted(l) and l != sorted(l, reverse=True):
      return 0
   for i in range(len(l) - 1):
      d = abs(l[i] - l[i + 1])
      if d < 1 or d > 3:
         return 0
   return 1


def failsafe(r):
   l = list(map(int, r.split()))
   if safe(l):
      return 1
   for i in range(len(l)):
      cl = l.copy()
      cl.pop(i)
      if safe(cl):
         return 1
   return 0


print(sum(map(failsafe, open(0).read().splitlines())))