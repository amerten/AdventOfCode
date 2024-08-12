def distance(speed, duration, rest, time):
    cycle = duration + rest
    nb_cycles = time // cycle
    time_remaining = time % cycle
    return speed * (duration * nb_cycles + min(time_remaining, duration))


time = 2503
d = 0
for line in open(0).read().splitlines():
    e = line.split()
    d = max(d, distance(int(e[3]), int(e[6]), int(e[13]), time))
print(d)
