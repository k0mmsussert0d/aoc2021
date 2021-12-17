import re

if __name__ == '__main__':
    def get_width(cords):
        return max([x for x, _ in cords]) + 1

    def get_height(cords):
        return max([x for _, x in cords]) + 1

    def write_matrix(cords):
        width = get_width(cords)
        height = get_height(cords)
        matrix = [['.' for _ in range(width)] for _ in range(height)]

        for x, y in cords:
            matrix[y][x] = '#'

        return matrix

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

    matrix = write_matrix(cords)
    width = get_width(cords)
    height = get_height(cords)

    for hv, axis in folds:
        axis = int(axis)
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

        cords = new_cords
        matrix = write_matrix(cords)

    for row in matrix:
        print(''.join(row))
