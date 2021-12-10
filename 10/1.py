if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = file.readlines()

    chunks = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    p = 0
    for line in lines:
        stack = []
        for c in line:
            match c:
                case '(' | '[' | '{' | '<':
                    stack.append(c)
                case ')' | ']' | '}' | '>':
                    pop = stack.pop()
                    if chunks[c] != pop:
                        p += points[c]
                        break
    print(p)
