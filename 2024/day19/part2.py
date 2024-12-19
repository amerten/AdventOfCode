memory = {}


def is_possible(target, towels):
   if target in memory:
      return memory[target]
   if target == "":
      return 1
   total = 0
   for tow in towels:
      if target.startswith(tow):
         total += is_possible(target[len(tow):], towels)
   memory[target] = total
   return total


towels = []
patterns = []
for line in open(0).read().splitlines():
   if ',' in line:
      towels = line.split(', ')
   elif line:
      patterns.append(line)
t = 0
for p in patterns:
   t += is_possible(p, towels)
print(t)