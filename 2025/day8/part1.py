import math

boxes = []
distances = {}
circuits = []
for line in open(0).read().splitlines():
    boxes.append(tuple(map(int, line.split(","))))
for i in range(len(boxes) - 1):
    for j in range(i + 1, len(boxes)):
        b1, b2 = boxes[i], boxes[j]
        distances[((b1[0] - b2[0])**2 + (b1[1] - b2[1])**2 + (b1[2] - b2[2])**2) ** 0.5] = (b1, b2)
counter = 1000
for _, boxes in sorted(distances.items(), key=lambda item: item[0]):
    b1, b2 = boxes
    s_b1_in, s_b2_in = None, None
    for circuit in circuits:
        if b1 in circuit:
            s_b1_in = circuit
        if b2 in circuit:
            s_b2_in = circuit
        if s_b1_in and s_b2_in:
            break
    if s_b1_in and s_b2_in and s_b1_in != s_b2_in:
        circuits.remove(s_b1_in)
        circuits.remove(s_b2_in)
        circuits.append(s_b1_in.union(s_b2_in))
    elif s_b1_in and s_b1_in != s_b2_in:
        s_b1_in.add(b2)
    elif s_b2_in and s_b1_in != s_b2_in:
        s_b2_in.add(b1)
    elif not s_b1_in and not s_b2_in:
        circuits.append({b1, b2})
    counter -= 1
    if counter == 0:
        break
sizes = list(map(lambda x: len(x), sorted(circuits, key=lambda x: len(x), reverse=True)))
print(math.prod(sizes[:3]))