def decompress(s):
   r = ""
   i = 0
   while i < len(s):
      if s[i] == "(":
         marker = s[i + 1:s.index(')', i + 1)]
         a, b = map(int, marker.split('x'))
         for _ in range(b):
            r += s[i + len(marker) + 2: i + len(marker) + 2 + a]
         i += (len(marker) + 1 + a)
      else:
         r += s[i]
      i += 1
   return r


print(sum(len(decompress(line)) for line in open(0).read().splitlines()))
