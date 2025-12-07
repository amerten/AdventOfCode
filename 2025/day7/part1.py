visited = set()


def explore(grid, r, c):
    global visited
    if r >= len(grid) or (r, c) in visited:
        return 0
    visited.add((r, c))
    split = 0
    if grid[r][c] == '^':
        split += 1
        split += explore(grid, r, c - 1)
        split += explore(grid, r, c + 1)
    else:
        split += explore(grid, r + 1, c)
    return split


input = open(0).read().splitlines()
print(explore(input, 0, input[0].index('S')))
