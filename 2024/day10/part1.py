def score(m, r, c, seen):
   h = m[r][c]
   if h == 9:
      ok = (r, c) not in seen
      seen.add((r, c))
      return ok
   s = 0
   for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
      if 0 <= r + dr < len(m) and 0 <= c + dc < len(m[r + dr]) and m[r + dr][c + dc] == h + 1:
         s += score(m, r + dr, c + dc, seen)
   return s


map = [list(map(int, list(l))) for l in open(0).read().splitlines()]
print(sum(score(map, r, c, set()) for r in range(len(map)) for c in range(len(map[r])) if map[r][c] == 0))
