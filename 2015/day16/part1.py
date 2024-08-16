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
    for i in range(2, len(e) - 1):
        if e[i] in mfcsam and mfcsam[e[i]] != int(e[i + 1]):
            found = False
            break
    if found:
        print(e[1])
        break