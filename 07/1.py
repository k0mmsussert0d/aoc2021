from statistics import median

if __name__ == '__main__':
    with open('input', 'r') as file:
        crabs = [int(i.strip()) for i in file.readline().split(',')]
    med = round(median(crabs))
    print(sum([abs(x - med) for x in crabs]))
