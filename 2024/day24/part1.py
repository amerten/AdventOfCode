wires = {}
gates = {}
bits = []
for line in open(0).read().splitlines():
   if ':' in line:
      w, v = line.split(': ')
      wires[w] = int(v)
   elif '->' in line:
      w1, g, w2, o = line.replace('->', '').split()
      if w1 not in wires:
         wires[w1] = None
      if w2 not in wires:
         wires[w2] = None
      if o not in wires:
         wires[o] = None
      if o[0] == 'z':
         bits.append(None)
      if (w1, g, w2) not in gates:
         gates[(w1, g, w2)] = []
      gates[(w1, g, w2)].append(o)

while any(v is None for v in bits):
   for w1, g, w2 in gates:
      for o in gates[(w1, g, w2)]:
         if wires[w1] is not None and wires[w2] is not None and wires[o] is None:
            if g == 'AND':
               wires[o] = wires[w1] and wires[w2]
            elif g == 'OR':
               wires[o] = wires[w1] or wires[w2]
            else:
               wires[o] = wires[w1] ^ wires[w2]
            if o[0] == 'z':
               bits[len(bits) - 1 - int(o[1:])] = wires[o]

print(int(''.join(map(str, bits)), 2))