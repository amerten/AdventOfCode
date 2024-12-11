NB_BLINK = 75
memory = {}


def blink(n, bl):
   if (n, bl) in memory:
      return memory[n, bl]
   if bl == NB_BLINK:
      return 1
   t = 0
   s = str(n)
   if len(s) % 2 == 0:
      t += blink(int(s[:len(s)//2]), bl + 1)
      t += blink(int(s[len(s)//2:]), bl + 1)
   else:
      t += blink(1 if n == 0 else n * 2024, bl + 1)
   memory[(n, bl)] = t
   return t


print(sum(blink(x, 0) for x in list(map(int, open(0).read().split()))))