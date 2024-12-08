antennas = {}
for r, line in enumerate(open(0).read().splitlines()):
    for c, spot in enumerate(line):
        if spot != '.':
            if spot not in antennas:
                antennas[spot] = []
            antennas[spot].append((r, c))
antinodes = set()
for antenna in antennas:
    for i in range(len(antennas[antenna]) - 1):
        for j in range(i + 1, len(antennas[antenna])):
            a1, a2 = antennas[antenna][i], antennas[antenna][j]
            dr, dc = a1[0] - a2[0], a1[1] - a2[1]
            k = 0
            while 0 <= a1[0] + dr * k <= r and 0 <= a1[1] + dc * k <= c:
                antinodes.add((a1[0] + dr * k, a1[1] + dc * k))
                k += 1
            k = 0
            while 0 <= a2[0] - dr * k <= r and 0 <= a2[1] - dc * k <= c:
                antinodes.add((a2[0] - dr * k, a2[1] - dc * k))
                k += 1
print(len(antinodes))
