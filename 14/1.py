from collections import defaultdict

if __name__ == '__main__':
    mappings = {}
    pairs_count = {}
    with open('input', 'r') as file:
        template = file.readline().strip()
        file.readline()  # empty separator
        line = file.readline().strip()
        while line != '':
            s = line.split(' -> ')
            mappings[s[0]] = s[1]
            line = file.readline().strip()
    pairs_count = {k: 0 for k, _ in mappings.items()}

    # change to 40 for part 2 solution =)
    steps = 10

    for a, b in zip(template[:-1], template[1:]):
        pairs_count[''.join([a, b])] += 1

    polymer_count = defaultdict(lambda: 0)

    current_pairs = {k: v for k, v in pairs_count.items() if v > 0}
    for ch in template:
        polymer_count[ch] += 1

    for i in range(steps):
        current_pairs = {k: v for k, v in pairs_count.items() if v > 0}
        for pair, count in current_pairs.items():
            pairs_count[pair] -= count
            a, b = pair
            insert = mappings[pair]
            polymer_count[insert] += count
            pairs_count[a + insert] += count
            pairs_count[insert + b] += count

    print(max(polymer_count.values()) - min(polymer_count.values()))
