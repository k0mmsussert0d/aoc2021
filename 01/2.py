if __name__ == '__main__':
    with open('./input', 'r') as file:
        lines = file.readlines()
    i, x  = 1, 0
    a = [int(y) for y in lines[0:3]]
    while i < len(lines) - 2:
        b = [int(y) for y in lines[i:i+3]]
        if sum(b) > sum(a):
            x += 1
        a = b.copy()
        i += 1
    print(x)
