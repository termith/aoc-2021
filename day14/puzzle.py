from collections import Counter


def read_data():
    transforms = {}
    with open('input') as f:
        start = f.readline().strip()
        f.readline()
        while line := f.readline():
            k, v = line.strip().split(' -> ')
            transforms[k] = v
    return start, transforms


def puzzle_one():
    polymer, transforms = read_data()
    for _ in range(10):
        new_polymer = ''
        i = 0
        while i != len(polymer) - 1:
            new_polymer += polymer[i]
            if polymer[i:i+2] in transforms:
                new_polymer += transforms[polymer[i:i+2]]
            i += 1
        new_polymer += polymer[-1]
        polymer = new_polymer
    c = Counter(polymer)

    print(max(c.values()) - min(c.values()))


def puzzle_two():
    polymer, transforms = read_data()
    pairs = Counter()
    letters = Counter()
    i = 0
    while i != len(polymer) - 1:
        pairs[polymer[i:i+2]] += 1
        letters[polymer[i]] += 1
        i += 1
    letters[polymer[-1]] += 1
    for _ in range(40):
        decrement = []
        increment = []
        for pair in pairs:
            if pair in transforms:
                value = pairs[pair]
                if value:
                    decrement.append((pair, value))
                    letter = transforms[pair]
                    increment.append((f'{pair[0]}{letter}', value))
                    increment.append((f'{letter}{pair[1]}', value))
                    letters[letter] += value
        for d_p in decrement:
            pairs[d_p[0]] -= d_p[1]
        for i_p in increment:
            pairs[i_p[0]] += i_p[1]
    print(max(letters.values()) - min(letters.values()))


if __name__ == '__main__':
    puzzle_one()
    puzzle_two()