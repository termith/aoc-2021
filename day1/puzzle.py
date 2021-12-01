"""
P1. Count the number of times a depth measurement increases from the previous measurement.

P2. Count the number of times the sum of measurements in this sliding window (size=3) increases from the previous sum
"""


def puzzle_one():
    counter = -1  # this is for first measure which is hasn't to be count
    prev = 0
    with open('input') as f:
        for measure in f.readlines():
            if prev < int(measure):
                counter += 1
            prev = int(measure)
    print(counter)


def puzzle_two():
    measurements = list(map(int, open('input').readlines()))
    position = 1
    counter = 0
    prev_sum = sum(measurements[:3])
    while position <= len(measurements) - 3:
        next_sum = sum(measurements[position:position+3])
        if next_sum > prev_sum:
            counter += 1
        prev_sum = next_sum
        position += 1
    print(counter)


if __name__ == '__main__':
    puzzle_one()
    puzzle_two()