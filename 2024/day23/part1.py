connections = {}
for line in open(0).read().splitlines():
   c1, c2 = line.split('-')
   if c1 not in connections:
      connections[c1] = set()
   if c2 not in connections:
      connections[c2] = set()
   connections[c1].add(c2)
   connections[c2].add(c1)


visited = set()
t = 0
for c1 in connections:
   for c2 in connections[c1]:
      if frozenset([c1, c2]) in visited:
         continue
      for c3 in connections[c2]:
         if frozenset([c1, c2, c3]) in visited:
            continue
         if c3 in connections[c1] and (c1[0]=='t'or c2[0]=='t' or c3[0]=='t'):
            t += 1
         visited.add(frozenset([c1, c2, c3]))
      visited.add(frozenset([c1, c2]))
print(t)