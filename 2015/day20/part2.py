import collections
import itertools


def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1
    if n > 1:
        yield n


def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result


def get_divisors(n):
    pf = prime_factors(n)

    pf_with_multiplicity = collections.Counter(pf)

    powers = [
        [factor ** i for i in range(count + 1)]
        for factor, count in pf_with_multiplicity.items()
    ]

    for prime_power_combo in itertools.product(*powers):
        yield prod(prime_power_combo)


input = int(input())

i = 1
while True:
    t = 0
    for d in sorted(list(get_divisors(i)), reverse=True):
        if i // d > 50:
            break
        t += (d * 11)
    if t >= input:
        print(i)
        break
    i += 1
