g = open(0).read().splitlines()
t = 0
for r in range(len(g)):
   for c in range(len(g[r])):
      up, down, left, right = r >= 3, r <= len(g) - 4, c >= 3, c <= len(g[r]) - 4
      t += (right and ''.join(g[r][c + i] for i in range(4)) == "XMAS")
      t += (left and ''.join(g[r][c - i] for i in range(4)) == "XMAS")
      t += (up and ''.join(g[r - i][c] for i in range(4)) == "XMAS")
      t += (down and ''.join(g[r + i][c] for i in range(4)) == "XMAS")
      t += (up and right and ''.join(g[r - i][c + i] for i in range(4)) == "XMAS")
      t += (up and left and ''.join(g[r - i][c - i] for i in range(4)) == "XMAS")
      t += (down and right and ''.join(g[r + i][c + i] for i in range(4)) == "XMAS")
      t += (down and left and ''.join(g[r + i][c - i] for i in range(4)) == "XMAS")
print(t)