def square_feet(gift):
    d = sorted(list(map(int, gift.split('x'))))
    return 2 * (d[0] + d[1]) + d[0] * d[1] * d[2]


print(sum(map(square_feet, open(0).read().splitlines())))
