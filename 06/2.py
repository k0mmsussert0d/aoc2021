"""
Both 1.py and 2.py serve the same solution,
although 2.py algorithm is more efficient
and solves part 2 of the exercise in reasonable
amount of time.
"""
from collections import deque

if __name__ == '__main__':
    with open('input', 'r') as file:
        fish = [int(i) for i in file.readline().split(',')]
    days = 256

    fish_stats = [0] * 9
    for f in fish:
        fish_stats[f] += 1

    Q = deque(fish_stats)

    for _ in range(days):
        spawn = Q.popleft()
        Q[6] += spawn
        Q.append(spawn)

    print(sum(Q))
