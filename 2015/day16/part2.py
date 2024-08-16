mfcsam = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

for line in open(0).readlines():
    e = line.replace(':', '').replace(',', '').split()
    found = True
    for i in range(2, len(e) - 1, 2):
        n = int(e[i + 1])
        if e[i] in mfcsam:
            if e[i] in ["cats", "trees"]:
                found = n > mfcsam[e[i]]
            elif e[i] in ["pomeranians", "goldfish"]:
                found = n < mfcsam[e[i]]
            else:
                found = n == mfcsam[e[i]]
        if not found:
            break
    if found:
        print(e[1])
        break