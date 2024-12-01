l1, l2 = [], []
for line in open(0).read().splitlines():
   n1, n2 = map(int, line.split())
   l1.append(n1)
   l2.append(n2)
print(sum([n * l2.count(n) for n in l1]))