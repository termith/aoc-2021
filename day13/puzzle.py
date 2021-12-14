


def read_data():
    points = []
    with open('input') as f:
        while (line := f.readline()) != '\n':
            points.append(tuple(map(int, line.strip().split(','))))
        transforms = []
        while line := f.readline():
            splitted = line.rsplit(maxsplit=1)[1].split('=')
            transforms.append((splitted[0], int(splitted[1])))
    return points, transforms


def fold(points, axis):
    new_points = set()
    if axis[0] == 'y':
        for point in points:
            if point[1] < axis[1]:
                new_points.add(point)
            else:
                new_points.add((point[0], 2 * axis[1] - point[1]))
    else:
        for point in points:
            if point[0] < axis[1]:
                new_points.add(point)
            else:
                new_points.add((2 * axis[1] - point[0], point[1]))
    return new_points


def puzzle_one():
    points, transforms = read_data()
    print(len(fold(points, transforms[0])))


def puzzle_two():
    points, transforms = read_data()
    for t in transforms:
        points = fold(points, t)
    for i in range(max([p[1] for p in points]) + 1):
        for j in range(max([p[0] for p in points]) + 1):
            print(' ' if (j, i) not in points else '#', end='')
        print('\n', end='')


if __name__ == '__main__':
    puzzle_one()
    puzzle_two()
