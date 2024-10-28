def decompress(line):
   try:
      i = line.index('(')
   except:
      i = -1
   if i == -1:
      return len(line)
   if i > 0:
      return i + decompress(line[i:])
   j = line.index(')')
   n, m = map(int, line[i + 1:j].split('x'))
   return m * decompress(line[j+1:j+1+n]) + decompress(line[j+n+1:])


print(sum(map(decompress, open(0).read().splitlines())))