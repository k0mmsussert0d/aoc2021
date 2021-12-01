if __name__ == '__main__':
    a = b = x = 0
    with open('./input', 'r') as file:
        a = int(file.readline())
        for line in file:
            b = int(line)
            if b> a:
                x += 1
            a = b
    print(x)

