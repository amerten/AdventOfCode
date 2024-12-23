connections = {}
for line in open(0).read().splitlines():
   c1, c2 = line.split('-')
   if c1 not in connections:
      connections[c1] = set()
   if c2 not in connections:
      connections[c2] = set()
   connections[c1].add(c2)
   connections[c2].add(c1)

largest_lan = []
for c1 in connections:
   lan = [c1]
   for c2 in connections:
      if all(c2 in connections[c] for c in lan):
         lan.append(c2)
   if len(lan) > len(largest_lan):
      largest_lan = lan
print(','.join(sorted(largest_lan)))
