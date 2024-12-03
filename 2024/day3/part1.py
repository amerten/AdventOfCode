import re

t = 0
for m in re.finditer('mul\((\d{1,3}),(\d{1,3})\)', open(0).read()):
   t += int(m[1]) * int(m[2])
print(t)