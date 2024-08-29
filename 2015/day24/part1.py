from itertools import combinations
from numpy import prod
import sys

packages = set(map(int, open(0).read().splitlines()))
total_weight = sum(packages)
weight = total_weight // 3

quantum_entanglement = sys.maxsize

for i_size in range(1, len(packages) - 1):
    found_size = False
    for i_c in combinations(packages, i_size):
        i_s = set(i_c)
        if sum(i_s) != weight:
            continue
        j_remaining = packages - i_s
        for j_size in range(1, len(j_remaining)):
            found_comb = False
            for j_c in combinations(j_remaining, j_size):
                j_s = set(j_c)
                if sum(i_s) != weight:
                    continue
                found_size, found_comb = True, True
                quantum_entanglement = min(quantum_entanglement, prod(list(i_s)))
                break
            if found_comb:
                break
    if found_size:
        break

print(quantum_entanglement)
