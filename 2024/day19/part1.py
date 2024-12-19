memory = {}


def is_possible(target, towels):
   if target in memory:
      return memory[target]
   found = False
   for tow in towels:
      if target.startswith(tow):
         found |= is_possible(target[len(tow):], towels)
         memory[target] = found
         if found:
            break
   return found


towels = []
patterns = []
for line in open(0).read().splitlines():
   if ',' in line:
      for tow in line.split(', '):
         towels.append(tow)
         memory[tow] = True
   elif line:
      patterns.append(line)
t = 0
for p in patterns:
   t += is_possible(p, towels)
print(t)