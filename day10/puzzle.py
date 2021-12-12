SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

SCORES_COMPLETE = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

CHUNKS = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}


def puzzle_one():
    with open('input') as f:
        result = 0
        for line in f:
            stack = []
            for c in line.strip():
                if c in CHUNKS:
                    stack.append(c)
                else:
                    if CHUNKS[stack.pop()] != c:
                        result += SCORES[c]
                        break
    print(result)


def puzzle_two():
    with open('input') as f:
        scores = []
        for line in f:
            stack = []
            for c in line.strip():
                if c in CHUNKS:
                    stack.append(c)
                else:
                    if CHUNKS[stack.pop()] != c:
                        break
            else:
                if stack:
                    result = 0
                    for c in reversed(stack):
                        result *= 5
                        result += SCORES_COMPLETE[c]
                scores.append(result)
    print(sorted(scores)[len(scores) // 2])


if __name__ == '__main__':
    puzzle_one()
    puzzle_two()