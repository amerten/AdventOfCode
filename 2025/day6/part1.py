input = open(0).read().splitlines()
operators = input[-1].split()
t = 0
for i in range(len(operators)):
    s = ""
    for j in range(len(input) - 1):
        s += input[j].split()[i]
        if j < len(input) - 2:
            s += " " + operators[i] + " "
    t += eval(s)
print(t)