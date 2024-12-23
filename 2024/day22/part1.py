def step(n, nb_steps):
   for _ in  range(nb_steps):
      n = n ^ (n * 64)
      n = n % 16777216
      n = n ^ (n // 32)
      n = n % 16777216
      n = n ^ (n * 2048)
      n = n % 16777216
   return n


print(sum(map(lambda x: step(int(x), 2000), [x for x in open(0).read().splitlines()])))
