if __name__ == '__main__':
    with open('input', 'r') as file:
        input_ = [[j for j in list(i.strip())] for i in file.readlines()]
        columns = list(map(list, zip(*input_)))
        l = len(columns[0])
        gamma = ['1' if c.count('1') > l / 2 else '0' for c in columns]
        epsilon = list(map({'1': '0', '0': '1'}.get, gamma))
        print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))

