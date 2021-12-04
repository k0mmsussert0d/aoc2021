from functools import reduce

if __name__ == '__main__':
    def check_win(board):
        def cond(row):
            for _, state in row:
                if state is False:
                    return False
            return True
        for row in board:
            if cond(row):
                return True
        for col in list(map(list, zip(*board))):
            if cond(col):
                return True
        return False


    def unmarked(board):
        res = []
        for row in board:
            for v, state in row:
                if state is False:
                    res.append(v)
        return res


    with open('test_input', 'r') as file:
        seq = [int(i) for i in file.readline().strip().split(',')]
        boards = []
        b_i = -1
        line = file.readline()
        while line:
            if line == '\n':
                b_i += 1
                boards.append([])
            else:
                boards[b_i].append([(int(i), False) for i in line.strip().split()])
            line = file.readline()

    found = False
    for idx, s in enumerate(seq):
        for board in boards:
            for row in board:
                for idx_row, (num, state) in enumerate(row):
                    if num == s:
                        row[idx_row] = num, True
            if idx >= 5 and check_win(board):
                print(sum(unmarked(board)) * s)
                exit()
