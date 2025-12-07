memory = {}


def explore(grid, r, c):
    global memory
    if (r, c) in memory:
        return memory[(r, c)]
    if r >= len(grid):
        return 1
    memory[(r, c)] = 0
    if grid[r][c] == '^':
        memory[(r, c)] += explore(grid, r, c - 1)
        memory[(r, c)] += explore(grid, r, c + 1)
    else:
        memory[(r, c)] += explore(grid, r + 1, c)
    return memory[(r, c)]


input = open(0).read().splitlines()
sr, sc = 0, input[0].index('S')
explore(input, sr, sc)
print(memory[(sr, sc)])
