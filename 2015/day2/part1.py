def square_feet(gift):
    l, w, h = map(int, gift.split('x'))
    dimensions = [l * w, l * h, w * h]
    return min(dimensions) + 2 * sum(dimensions)


print(sum(map(square_feet, open(0).read().splitlines())))
