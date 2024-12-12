regions = []


def neighbors(p1, p2):
   return (abs(p1[0] - p2[0]) == 1 and p1[1] == p2[1]) or (abs(p1[1] - p2[1]) == 1 and p1[0] == p2[0])


def parse_regions(m, r, c, new=False):
   global regions
   if new:
      regions.append({(r, c)})
   else:
      regions[len(regions) - 1].add((r, c))
   for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nr, nc = r + dr, c + dc
      if (nr, nc) in regions[len(regions) - 1]:
         continue
      if 0 <= nr < len(m) and 0 <= nc < len(m[nr]) and m[nr][nc] == m[r][c]:
         parse_regions(m, nr, nc)


map = open(0).read().splitlines()
for r in range(len(map)):
   for c in range(len(map[r])):
      if all((r, c) not in x for x in regions):
         parse_regions(map, r, c, True)
t = 0
for region in regions:
   borders = {}
   for r, c in region:
      for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
         nr, nc = r + dr, c + dc
         if nr < 0 or nr >= len(map) or nc < 0 or nc >= len(map[0]) or map[nr][nc] != map[r][c]:
            if abs(dr) > 0:
               border = (r, 0, dr, 0)
            else:
               border = (0, c, 0, dc)
            if border not in borders:
               borders[border] = []
            borders[border].append((r, c))
   nb_borders = 0
   for border in borders:
      i, neighb = 0, [set()]
      seen = set()
      while True:
         found = False
         for b in borders[border]:
            if b in seen:
               continue
            if len(neighb[i]) == 0:
               neighb[i].add(b)
               seen.add(b)
               continue
            for ob in neighb[i]:
               if neighbors(b, ob):
                  neighb[i].add(b)
                  seen.add(b)
                  found = True
                  break
         if not found:
            if len(seen) != len(borders[border]):
               neighb.append(set())
               i += 1
            else:
               break
      nb_borders += len(neighb)
   t += (nb_borders * len(region))
print(t)