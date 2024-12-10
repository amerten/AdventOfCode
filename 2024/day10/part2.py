def rating(m, r, c, trail, trails):
   h = m[r][c]
   trail += str(r) + str(c)
   if h == 9:
      ok = trail not in trails
      trails.add(trail)
      return ok
   s = 0
   for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
      if 0 <= r + dr < len(m) and 0 <= c + dc < len(m[r + dr]) and m[r + dr][c + dc] == h + 1:
         s += rating(m, r + dr, c + dc, trail, trails)
   return s


map = [list(map(int, list(l))) for l in open(0).read().splitlines()]
print(sum(rating(map, r, c, "", set()) for r in range(len(map)) for c in range(len(map[r])) if map[r][c] == 0))
