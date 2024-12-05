rules, updates = {}, []
getting_rules = True
for line in open(0).read().splitlines():
   if line == "":
      getting_rules = False
   elif getting_rules:
      a, b = line.split('|')
      if b not in rules:
         rules[b] = []
      rules[b].append(a)
   else:
      updates.append(line.split(','))

t = 0
for pages in updates:
   right_order = True
   for i, page in enumerate(pages):
      if page in rules:
         right_order &= all(next_page not in rules[page] for next_page in pages[i+1:])
         if not right_order:
            break
   if right_order:
      t += int(pages[len(pages)//2])
print(t)