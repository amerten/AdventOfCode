import bisect

l1, l2 = [], []
for line in open(0).read().splitlines():
   n1, n2 = map(int, line.split())
   bisect.insort(l1, n1)
   bisect.insort(l2, n2)
print(sum([abs(l1[i] - l2[i]) for i in range(len(l1))]))