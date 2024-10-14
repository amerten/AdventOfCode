t = 0
for line in open(0).read().splitlines():
   in_brackets = False
   supports_tls = False
   for i, c in enumerate(line):
      if c == '[':
         in_brackets = True
      elif c == ']':
         in_brackets = False
      else:
         if i < len(line) - 3:
            if line[i] != line[i+1] and line[i] == line[i+3] and line[i+1] == line[i+2]:
               if in_brackets:
                  supports_tls = False
                  break
               supports_tls = True
   t += supports_tls
print(t)