grid = open(0).read().splitlines()
t = 0
removed = set()
while True:
    l = len(removed)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] != '@' or (r, c) in removed:
                continue
            neighbors = 0
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                    neighbors += (grid[nr][nc] == '@' and (nr, nc) not in removed)
            to_remove = neighbors < 4
            t += to_remove
            if to_remove:
                removed.add((r, c))
    if l == len(removed):
        break
print(t)