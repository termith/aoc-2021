def has_winner(boards):
    result = []
    for i, board in enumerate(boards):
        for column in board['columns']:
            if all(map(lambda x: x is None, column)):
                result.append(boards.pop(i))
                break
        else:
            for row in board['rows']:
                if all(map(lambda x: x is None, row)):
                    result.append(boards.pop(i))
                    break
    return result


def read_boards():
    with open('input') as f:
        numbers = list(map(int, f.readline().split(',')))
        f.readline()
        boards = []
        end = False
        while not end:
            board = {'rows': [], 'columns': [[], [], [], [], []]}
            while (line := f.readline()) != '\n':
                if not line:
                    end = True
                    break
                row = list(map(int, line.split()))
                for idx, n in enumerate(row):
                    board['columns'][idx].append(n)
                board['rows'].append(row)
            boards.append(board)
        return numbers, boards


def step(boards, number):
    for board in boards:
        for column in board['columns']:
            for i, n in enumerate(column):
                if n == number:
                    column[i] = None
        for row in board['rows']:
            for i, n in enumerate(row):
                if n == number:
                    row[i] = None
    return boards


def puzzle_one():
    numbers, boards = read_boards()
    master = iter(numbers)
    while not (winner := has_winner(boards)):
        number = next(master)
        boards = step(boards, number)
    result = 0
    for row in winner[-1]['rows']:
        result += sum(filter(lambda x: x is not None, row))
    print(result * number)


def puzzle_two():
    numbers, boards = read_boards()
    for number in numbers:
        boards = step(boards, number)
        winner = has_winner(boards)
        if winner:
            result = 0
            for row in winner[-1]['rows']:
                result += sum(filter(lambda x: x is not None, row))
            print(result * number)


if __name__ == '__main__':
    puzzle_one()
    puzzle_two()
