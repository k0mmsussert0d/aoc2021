if __name__ == '__main__':
    with open('test_input', 'r') as file:
        hmap = [[int(y) for y in x.strip()] for x in file.readlines()]

    def surround(x, y):
        cords = [
            (x - 1, y),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y),
        ]
        return [hmap[i][j] for i, j in cords if 0 <= i <= len(hmap) - 1 and 0 <= j <= len(hmap[i]) - 1]

    def is_low_point(x, y):
        s = surround(x, y)
        if all([hmap[x][y] < i for i in s]):
            return hmap[x][y] + 1
        return None

    res = 0
    for i in range(len(hmap)):
        for j in range(len(hmap[i])):
            if l := is_low_point(i, j):
                res += l
    print(res)
