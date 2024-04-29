with open(0) as f:
    data = [line.strip() for line in f.readlines()]


for r in range(len(data)):
    for c in range(len(data)):
        if data[r][c] == 'S':
            start = (r, c)
            break
    else:
        continue
    break


def are_connected(p1, p2):
    c1, c2 = data[p1[0]][p1[1]], data[p2[0]][p2[1]]
    if c1 == '.' or c2 == '.' or p1 == p2:
        return False
    connected_right = p2 == (p1[0], p1[1] + 1) and c2 in '-7JS'
    connected_left = p2 == (p1[0], p1[1] - 1) and c2 in 'FL-S'
    connected_bottom = p2 == (p1[0] + 1, p1[1]) and c2 in '|LJS'
    connected_top = p2 == (p1[0] - 1, p1[1]) and c2 in 'F|7S'
    if c1 == 'F': return connected_bottom or connected_right
    if c1 == '-': return connected_left or connected_right
    if c1 == '7': return connected_left or connected_bottom
    if c1 == '|': return connected_top or connected_bottom
    if c1 == 'L': return connected_top or connected_right
    if c1 == 'J': return connected_top or connected_left
    return connected_top or connected_bottom or connected_right or connected_left


distances = {}
previous_position, current_position = None, start

distance = 0
while True:
    for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        r, c = current_position[0] + d[0], current_position[1] + d[1]
        if r < 0 or r >= len(data) or c < 0 or c >= len(data[r]):
            continue
        if are_connected(current_position, (r, c)) and (r, c) != previous_position:
            distance += 1
            distances[(r, c)] = distance
            previous_position = current_position
            current_position = (r, c)
            break
    if current_position == start:
        break

for p in distances:
    distances[p] = min(distances[p], len(distances) - distances[p])

print(max(distances.values()))
