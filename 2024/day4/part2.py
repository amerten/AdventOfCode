g = open(0).read().splitlines()
t, r, c = 0, 0, 0
for r in range(len(g) - 2):
   for c in range(len(g[r]) - 2):
      d1 = ''.join(g[r + i][c + i] for i in range(3)) in ["MAS", "SAM"]  # \  up-down
      d2 = ''.join(g[r + 2 - i][c + i] for i in range(3)) in ["MAS", "SAM"]  # / down-up
      t += (d1 and d2)
print(t)