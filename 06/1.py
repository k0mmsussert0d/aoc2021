"""
Both 1.py and 2.py serve the same solution,
although 2.py algorithm is more efficient
and solves part 2 of the exercise in reasonable
amount of time.
"""
if __name__ == '__main__':
    with open('input', 'r') as file:
        fish = [int(i) for i in file.readline().split(',')]
    days = 80
    for _ in range(days):
        new = 0
        for idx, f in enumerate(fish):
            if f > 0:
                fish[idx] = f - 1
            else:
                fish[idx] = 6
                new += 1
        if new > 0:
            fish.extend([8] * new)
    print(len(fish))
