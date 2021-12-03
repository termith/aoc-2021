"""
P1. Starting with 0 horizontal position and 0 depth figure out multiplication of final horizontal pozition and depth
"""


def puzzle_one():
    position = 0
    depth = 0
    with open('input') as f:
        for command in f.readlines():
            direction, value = command.split()
            if direction == 'forward':
                position += int(value)
            elif direction == 'down':
                depth += int(value)
            else:
                depth -= int(value)
    print(f'position: {position}, depth: {depth}, result = {position * depth}')


def puzzle_two():
    position = 0
    depth = 0
    aim = 0
    with open('input') as f:
        for command in f.readlines():
            direction, value = command.split()
            if direction == 'forward':
                position += int(value)
                depth += int(value) * aim
            elif direction == 'down':
                aim += int(value)
            else:
                aim -= int(value)
    print(f'position: {position}, depth: {depth}, result = {position * depth}')


if __name__ == '__main__':
    puzzle_one()
    puzzle_two()