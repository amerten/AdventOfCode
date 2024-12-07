def can_be_true(r, n, t):
   if len(n) == 0:
      return t == r
   k = n.pop(0)
   return can_be_true(r, n.copy(), t + k) or can_be_true(r, n.copy(), t * k) or can_be_true(r, n.copy(), int(str(t) + str(k)))


t = 0
for line in open(0).read().splitlines():
   r, n = line.split(': ')
   l = list(map(int, n.split()))
   t += int(r) if can_be_true(int(r), l[1:], l[0]) else 0
print(t)
