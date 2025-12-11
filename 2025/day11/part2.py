paths = {}
memory = {}


def explore(current, target):
    if (current, target) in memory:
        return memory[(current, target)]
    if current == target:
        return 1
    if current == 'out':
        return 0
    memory[(current, target)] = sum([explore(x, target) for x in paths[current]])
    return memory[(current, target)]


for line in open(0).read().splitlines():
    i, o = line.split(': ')
    paths[i] = o.split()

sToF = explore('svr', 'fft')
dToF = explore('dac', 'fft')
sToD = explore('svr', 'dac')
fToD = explore('fft', 'dac')
fToO = explore('fft', 'out')
dToO = explore('dac', 'out')

print(sToF * fToD * dToO + sToD * dToF * fToO)
