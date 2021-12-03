if __name__ == '__main__':
    def transpose(l):
        return list(map(list, zip(*l)))


    def freq_reduce(lst, func, pos=0):
        return int(''.join(lst[0]), 2) if len(lst) == 1 else freq_reduce(list(filter(lambda x: x[pos] == func(transpose(lst), pos), lst)), func, pos + 1)


    def oxygen(lst):
        return freq_reduce(lst, lambda x, p: '1' if x[p].count('1') >= len(x[p]) / 2 else '0')


    def co2(lst):
        return freq_reduce(lst, lambda x, p: '0' if x[p].count('0') <= len(x[p]) / 2 else '1')


    with open('input', 'r') as file:
        input_ = [[j for j in list(i.strip())] for i in file.readlines()]
        print(oxygen(input_.copy()) * co2(input_.copy()))
