t = 0
for line in open(0).read().splitlines():
   in_brackets = False
   aba, bab = set(), set()
   for i, c in enumerate(line):
      if i >= len(line) - 2:
         break
      if c == '[':
         in_brackets = True
      elif c == ']':
         in_brackets = False
      else:
         if line[i] == line[i+2] and line[i] != line[i+1]:
            if in_brackets:
               bab.add(line[i+1] + line[i] + line[i+1])
            else:
               aba.add(line[i:i+3])
   if len(aba.intersection(bab)) > 0:
      t += 1
print(t)