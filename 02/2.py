from functools import reduce


if __name__ == '__main__':
    def func(res, line):
        match line.split(' '):
            case ['forward', value]:
                res[0] += int(value)
                res[1] += res[2] * int(value)
            case ['up', value]:
                res[2] -= int(value)
            case ['down', value]:
                res[2] += int(value)
        return res

    with open('input', 'r') as f:
        cords = reduce(func, f.readlines(), [0, 0, 0])
        print(cords[0] * cords[1])

