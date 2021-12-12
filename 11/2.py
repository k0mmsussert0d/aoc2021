if __name__ == '__main__':
    with open('input', 'r') as file:
        matrix = [[int(i) for i in list(line.strip())] for line in file.readlines()]

    flashes = 0

    def get_adjacent(x, y):
        cords = [
            (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
            (x - 1, y), (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
        ]
        return [(x0, y0) for x0, y0 in cords if 0 <= x0 <= len(matrix) - 1 and 0 <= y0 <= len(matrix[x]) - 1]


    def explode(x, y, ignore):
        global flashes
        if (x, y) in ignore:
            return
        if matrix[x][y] == 9:
            ignore.add((x, y))
            matrix[x][y] = 0
            flashes += 1
            adjacents = get_adjacent(x, y)
            for x0, y0 in adjacents:
                explode(x0, y0, ignore)
        else:
            matrix[x][y] += 1

    i = 0
    while True:
        i += 1
        ignore = set()
        for row, _ in enumerate(matrix):
            for col, octopus in enumerate(matrix[row]):
                explode(row, col, ignore)
        if all([x.count(0) == len(x) for x in matrix]):
            print(i)
            break
