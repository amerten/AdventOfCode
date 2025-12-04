grid = open(0).read().splitlines()
t = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] != '@':
            continue
        neighbors = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                neighbors += grid[nr][nc] == '@'
        t += neighbors < 4
print(t)