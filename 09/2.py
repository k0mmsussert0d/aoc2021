if __name__ == '__main__':
    with open('input', 'r') as file:
        hmap = [[int(y) for y in x.strip()] for x in file.readlines()]

    def surround_cords(x, y):
        cords = [
            (x - 1, y),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y),
        ]
        return [(x, y) for x, y in cords if 0 <= x <= len(hmap) - 1 and 0 <= y <= len(hmap[i]) - 1]

    def surround_values(x, y):
        return [hmap[i][j] for i, j in surround_cords(x, y)]

    def is_low_point(x, y):
        s = surround_values(x, y)
        if all([hmap[x][y] < i for i in s]):
            return hmap[x][y] + 1
        return None

    def traverse(x, y, ignore=None):
        if ignore is None:
            ignore = set()
        if hmap[x][y] != 9 and (x, y) not in ignore:
            ignore.add((x, y))
            for x0, y0 in surround_cords(x, y):
                traverse(x0, y0, ignore)
        return len(ignore)

    res = []
    for i in range(len(hmap)):
        for j in range(len(hmap[i])):
            if l := is_low_point(i, j):
                res.append(traverse(i, j))
    res.sort(reverse=True)
    print(res[0] * res[1] * res[2])
