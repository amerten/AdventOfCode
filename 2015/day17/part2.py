combinations = []
def search(remaining, used):
    for i in range(len(remaining)):
        r, u = remaining[i+1:], used + [remaining[i]]
        s = sum(u)
        if s == 150:
            combinations.append(u)
        elif s < 150:
            search(r, u)


containers = list(map(int, open(0).readlines()))
search(containers, [])
print(len([l for l in combinations if len(l) == min(len(x) for x in combinations)]))