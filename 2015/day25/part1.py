input = open(0).read()
row, column = int(input.replace(',', '').split()[15]), int(input.replace('.', '').split()[17])
code, r, c = 20151125, 1, 1
while r != row or c != column:
    r -= 1
    c += 1
    if r == 0:
        r = c
        c = 1
    code *= 252533
    code %= 33554393
print(code)
