from math import ceil, floor
from statistics import mean

if __name__ == '__main__':
    with open('input', 'r') as file:
        crabs = [int(i.strip()) for i in file.readline().split(',')]
    m = mean(crabs)
    m = floor(m)
    n = ceil(m)
    f = 0
    for c in crabs:
        d = abs(c - m)
        e = abs(c - n)
        f += max([((1 + d) / 2 * d), ((1 + e) / 2 * e)])
    print(round(f))
