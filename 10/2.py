from statistics import median

if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    chunks = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }
    points = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }

    scores = []
    for line in lines:
        stack = []
        correct = True
        for c in line:
            match c:
                case '(' | '[' | '{' | '<':
                    stack.append(c)
                case ')' | ']' | '}' | '>':
                    pop = stack.pop()
                    if chunks[c] != pop:
                        correct = False
                        break
        if correct and len(stack) != 0:
            p = 0
            while len(stack) != 0:
                c = stack.pop()
                p *= 5
                p += points[c]
            scores.append(p)
    print(median(scores))
