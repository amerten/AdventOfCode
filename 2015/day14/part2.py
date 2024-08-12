def distance(h, time):
    cycle = h[1] + h[2]
    nb_cycles = time // cycle
    time_remaining = time % cycle
    return h[0] * (h[1] * nb_cycles + min(time_remaining, h[1]))


horses = []
for line in open(0).read().splitlines():
    e = line.split()
    horses.append([0, int(e[3]), int(e[6]), int(e[13])])

time = 2503
for t in range(1, time + 1):
    distances = []
    for i, h in enumerate(horses):
        distances.append(distance(h[1:], t))
    for i, d in enumerate(distances):
        if d == max(distances):
            horses[i][0] += 1
print(max(h[0] for h in horses))

