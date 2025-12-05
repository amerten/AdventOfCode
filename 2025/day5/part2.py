def merge(ranges, range):
    r1_min, r1_max = range
    merged = False
    for r2_min, r2_max in ranges:
        if (r1_min <= r2_max and r1_max >= r2_min) or (r2_min <= r1_max and r2_max >= r1_min):
            ranges.remove((r2_min, r2_max))
            merged = True
            merge(ranges, (min(r1_min, r2_min), max(r1_max, r2_max)))
    if not merged:
        ranges.append((r1_min, r1_max))


ranges = []
for range in open(0).read().split('\n\n')[0].split():
    merge(ranges, map(int, range.split('-')))
t = 0
for r_min, r_max in ranges:
    t += (r_max - r_min + 1)
print(t)