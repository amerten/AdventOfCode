import re

t = 0
do = True
for m in re.finditer('mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)', open(0).read()):
   if m[0].startswith('mul') and do:
      t += int(m[1]) * int(m[2])
   else:
      do = m[0] == 'do()'
print(t)
