sequences = []
all_sequences = set()


def step(n, nb_steps):
   step_sequences = {}
   previous_deltas = []
   previous_digit = int(str(n)[-1])
   for _ in  range(nb_steps):
      n = n ^ (n * 64)
      n = n % 16777216
      n = n ^ (n // 32)
      n = n % 16777216
      n = n ^ (n * 2048)
      n = n % 16777216

      digit = int(str(n)[-1])
      delta = digit - previous_digit
      previous_deltas.append(delta)
      if len(previous_deltas) > 4:
         previous_deltas.pop(0)
      if len(previous_deltas) == 4 and tuple(previous_deltas) not in step_sequences:
         step_sequences[tuple(previous_deltas)] = digit
         all_sequences.add(tuple(previous_deltas))
      previous_digit = digit
   sequences.append(step_sequences)


for line in open(0).read().splitlines():
   step(int(line), 2000)

max_bananas = -1
for seq in all_sequences:
   t = 0
   for step_seq in sequences:
      if seq in step_seq:
         t += step_seq[seq]
   max_bananas = max(max_bananas, t)
print(max_bananas)
