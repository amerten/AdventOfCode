registers, p = {'a': 1, 'b': 0}, 0
instructions = open(0).read().splitlines()
while True:
    try:
        instruction = instructions[p].replace(',', '').split()
        if instruction[0] == "hlf":
            registers[instruction[1]] //= 2
            p += 1
        elif instruction[0] == "tpl":
            registers[instruction[1]] *= 3
            p += 1
        elif instruction[0] == "inc":
            registers[instruction[1]] += 1
            p += 1
        elif instruction[0] == "jmp":
            p += int(instruction[1])
        elif instruction[0] == "jie":
            if registers[instruction[1]] % 2 == 0:
                p += int(instruction[2])
            else:
                p += 1
        else:
            if registers[instruction[1]] == 1:
                p += int(instruction[2])
            else:
                p += 1
    except:
        break

print(registers["b"])