regions = []


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
   perimeter = 0
   for r, c in region:
      for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
         nr, nc = r + dr, c + dc
         perimeter += (nr < 0 or nr >= len(map) or nc < 0 or nc >= len(map[0]) or map[nr][nc] != map[r][c])
   t += (perimeter * len(region))
print(t)