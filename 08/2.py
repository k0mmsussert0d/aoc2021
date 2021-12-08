from functools import reduce

if __name__ == '__main__':
    def get_with_len(len_, lst):
        return [i for i in lst if len(i) == len_]

    def common_of_digits(digits):
        return reduce(lambda x, y: x & y, [set(x) for x in digits])

    with open('input', 'r') as file:
        signals = []
        outputs = []
        for line in file.readlines():
            vals = line.split('|')
            signals.append(vals[0].split())
            outputs.append(vals[1].split())

    sum = 0
    for s, o in zip(signals, outputs):
        _1 = get_with_len(2, s)[0]
        _4 = get_with_len(4, s)[0]
        _7 = get_with_len(3, s)[0]
        _8 = get_with_len(7, s)[0]

        a = set(_7) - set(_1)
        _6 = [x for x in get_with_len(6, s) if len(set(_1) & set(x)) == 1][0]
        f = set(_6) & set(_1)
        c = set(_1) - f
        b = set(_4) - c - f - common_of_digits(get_with_len(5, s))
        d = set(_4) - c - f - b
        g = common_of_digits(get_with_len(5, s)) - a - d
        e = set(_8) - a - b - c - d - f - g

        _2 = list(a | c | d | e | g)
        _3 = list(a | c | d | f | g)
        _5 = list(a | b | d | f | g)
        _9 = list(a | b | c | d | f | g)
        _0 = list(a | b | c | e | f | g)

        nums = [_0, _1, _2, _3, _4, _5, _6, _7, _8, _9]
        output = 0
        for idx, out in enumerate(reversed(o)):
            digit = nums.index([x for x in nums if set(x) == set(out)][0])
            output += digit * 10 ** idx
        sum += output
    print(sum)
