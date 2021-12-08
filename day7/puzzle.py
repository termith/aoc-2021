import numpy as np


def puzzle_one():
    min_value = float('inf')
    positions = np.array(list(map(int, open('input').read().split(','))))
    size = positions.size
    for position in range(max(positions) + 1):
        pos_value = abs(((np.ones(size) * position) - positions)).sum()
        min_value = min(pos_value, min_value)
    print(min_value)


def puzzle_two():
    min_value = float('inf')
    positions = np.array(list(map(int, open('input').read().split(','))))
    size = positions.size
    foo = np.vectorize(lambda x: sum(range(int(x) + 1)))

    for position in range(max(positions) + 1):
        pos_value = foo(abs(((np.ones(size) * position) - positions))).sum()
        min_value = min(pos_value, min_value)
    print(min_value)


if __name__ == '__main__':
    puzzle_one()
    puzzle_two()
