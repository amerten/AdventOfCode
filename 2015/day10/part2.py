from itertools import groupby

n = open(0).read()
nb_it = 50
for i in range(nb_it):
    n = ''.join([str(len(list(g))) + str(k) for k, g in groupby(n)])
print(len(n))


