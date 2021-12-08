from collections import Counter

unique_numbers = [2, 4, 3, 7]


def puzzle_one():
    counter = 0
    with open('input') as f:
        for line in f:
            for signal in line.split('|')[1].split():
                if len(set(signal)) in unique_numbers:
                    counter += 1
    print(counter)


DIGITS = {
    'abcefg' : 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}


def decipher(signals):
    code = {}
    count = Counter(''.join(signals))
    for l, value in count.items():
        if l in code:
            continue
        if value == 6:
            code[l] = 'b'
        elif value == 4:
            code[l] = 'e'
        elif value == 9:
            code[l] = 'f'
        elif value == 8:
            for s in signals:
                if len(s) == 2 and l in s:
                    code[l] = 'c'
            if not code.get(l):
                code[l] = 'a'
        elif value == 7:
            for s in signals:
                if len(s) == 4 and l in s:
                    code[l] = 'd'
            if not code.get(l):
                code[l] = 'g'
    return code


def puzzle_two():
    with open('input') as f:
        result = 0
        for line in f:
            signals = line.split('|')[0].split()
            code = decipher(signals)
            output = line.split('|')[1].split()
            d = []
            for c in output:
                d.append(str(DIGITS[''.join(sorted([code[l] for l in c]))]))
            result += int(''.join(d))
        print(result)


if __name__ == '__main__':
    puzzle_one()
    puzzle_two()
