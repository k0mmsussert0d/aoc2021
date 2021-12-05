import re

if __name__ == '__main__':
    with open('input', 'r') as file:
        vents = [tuple([int(i) for i in re.compile(r'(\d+),(\d+) -> (\d+),(\d+)').match(line).groups()]) for line in file.readlines()]
    matrix = []
    for _ in range(1000):
        matrix.append([0] * 1000)
    for ax, ay, bx, by in vents:
        if ay == by:
            if ax < bx:
                start = ax
                end = bx
            else:
                start = bx
                end = ax
            for zx in range(start, end + 1):
                matrix[by][zx] += 1
        elif ax == bx:
            if ay < by:
                start = ay
                end = by
            else:
                start = by
                end = ay
            for zy in range(start, end + 1):
                matrix[zy][bx] += 1
    print(sum([len(list(filter(lambda x: x > 1, i))) for i in matrix]))
