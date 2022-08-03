import random
import itertools
#
# def randoms(min, max, n):
#     return [random.randint(min, max) for _ in range(n)]
#
# for r in randoms(10, 30, 5):
#     print(r)

# varinat 2


def randoms(min, max, n):
    for i in range(n):
        yield random.randint(min, max)


for r in randoms(10, 30, 5):
    print(r)

rand_sequence = randoms(1, 10, 10)
five_sequence = list(itertools.islice(rand_sequence, 5))

print(five_sequence)
