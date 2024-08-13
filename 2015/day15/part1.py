import numpy as np


def mixtures(n, total):
    start = total if n == 1 else 0
    for i in range(start, total + 1):
        left = total - i
        if n - 1:
            for y in mixtures(n - 1, left):
                yield [i] + y
        else:
            yield [i]


def score(mixture):
    return np.prod([max(0, sum(ingredients[i][j] * mixture[i] for i in range(len(ingredients)))) for j in range(4)])


ingredients = []
for line in open(0).readlines():
    e = line.replace(',', '').split()
    ingredients.append([int(e[i]) for i in range(2, 11, 2)])
recipes = mixtures(len(ingredients), 100)
print(max(map(score, recipes)))
