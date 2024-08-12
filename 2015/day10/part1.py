n = open(0).read().strip()
nb_it = 40

for _ in range(nb_it):
    i = 0
    new_n = ""
    while i < len(n):
        c = n[i]
        j = 1
        while i + j < len(n) and n[i + j] == c:
            j += 1
        new_n += (str(j) + c)
        i += j
    n = new_n

print(len(n))