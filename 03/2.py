if __name__ == '__main__':
    def transpose(l):
        return list(map(list, zip(*l)))


    def freq_reduce(lst, func):
        pos = 0
        while len(lst) != 1:
            cols = transpose(lst)
            f = func(cols, pos)
            lst = list(filter(lambda x: x[pos] == f, lst))
            pos += 1
        return lst[0]


    def oxygen(lst):
        return freq_reduce(lst, lambda x, p: '1' if x[p].count('1') >= len(x[p]) / 2 else '0')


    def co2(lst):
        return freq_reduce(lst, lambda x, p: '0' if x[p].count('0') <= len(x[p]) / 2 else '1')


    with open('input', 'r') as file:
        input_ = [[j for j in list(i.strip())] for i in file.readlines()]
        print(int(''.join(oxygen(input_.copy())), 2) * int(''.join(co2(input_.copy())), 2))
