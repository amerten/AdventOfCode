input = open(0).read().splitlines()
operators = input[-1].split()
numbers = []
ns = []
for c in range(len(input[0]) - 1, -1, -1):
    o = ""
    for r in range(len(input) - 1):
        if input[r][c] != " ":
            o += input[r][c]
    if len(o) > 0:
        ns.append(o)
    else:
        operation = (" " + operators[len(operators) - 1 - len(numbers)] + " ").join(ns)
        numbers.append(eval(operation))
        ns = []
operation = (" " + operators[len(operators) - 1 - len(numbers)] + " ").join(ns)
numbers.append(eval(operation))
print(sum(numbers))