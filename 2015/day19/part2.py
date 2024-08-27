from random import shuffle

data = open(0).read().splitlines()
reps = []
for line in data[:-2]:
    reps.append(tuple(line.split(' => ')))
mol = data[-1]

target = mol
step = 0

while target != 'e':
    tmp = target
    for a, b in reps:
        if b not in target:
            continue

        target = target.replace(b, a, 1)
        step += 1

    if tmp == target:
        target = mol
        part2 = 0
        shuffle(reps)

print(step)