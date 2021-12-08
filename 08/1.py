if __name__ == '__main__':
    with open('input', 'r') as file:
        outputs = []
        for line in file.readlines():
            vals = line.split('|')
            outputs.extend(vals[1].split())
    print(len([x for x in outputs if len(x) in [2, 3, 4, 7]]))
