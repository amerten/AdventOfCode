paths = {}


def explore(current):
    global paths
    if current == 'out':
        return 1
    return sum([explore(x) for x in paths[current]])


for line in open(0).read().splitlines():
    i, o = line.split(': ')
    paths[i] = o.split()
print(explore('you'))
