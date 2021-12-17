import re

if __name__ == '__main__':
    cords = []
    folds = []
    with open('input', 'r') as file:
        line = file.readline().strip()
        while line != '':
            s = [int(x) for x in line.split(',')]
            cords.append((s[0], s[1]))
            line = file.readline().strip()
        line = file.readline().strip()
        while line != '':
            folds.append(re.compile(r'fold along ([xy])=(\d+)').match(line).groups())
            line = file.readline().strip()

    width = max([x for x, _ in cords]) + 1
    height = max([x for _, x in cords]) + 1

    hv = folds[0][0]
    axis = int(folds[0][1])
    t = height if hv == 'y' else width
    new_cords = []
    for x, y in cords:
        if hv == 'y' and y > axis:
            d = y - axis
            y0 = axis - d
            new_cords.append((x, y0))
        elif hv == 'x' and x > axis:
            d = x - axis
            x0 = axis - d
            new_cords.append((x0, y))
        else:
            new_cords.append((x, y))

    matrix = [['.' for i in range(width)] for j in range(height)]
    for x, y in new_cords:
        matrix[y][x] = '#'

    print(sum([sum([x == '#' for x in row]) for row in matrix]))
