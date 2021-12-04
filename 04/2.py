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


    with open('input', 'r') as file:
        seq = [int(i) for i in file.readline().strip().split(',')]
        boards = []
        b_i = -1
        line = file.readline()
        while line:
            if line == '\n':
                b_i += 1
                boards.append(([], False))
            else:
                boards[b_i][0].append([(int(i), False) for i in line.strip().split()])
            line = file.readline()

    found = False
    for idx, s in enumerate(seq):
        for idx_board, (board, board_state) in enumerate(boards):
            if board_state is True:
                continue
            for row in board:
                for idx_row, (num, state) in enumerate(row):
                    if num == s:
                        row[idx_row] = num, True
            if idx >= 5 and check_win(board):
                boards[idx_board] = (board, True)
                last = sum(unmarked(board)) * s
    print(last)
