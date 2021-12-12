def find_neighbors(cave, i, j):
    n = set()
    if i != 0:
        n.add((i - 1, j))
        if j != 0:
            n.add((i - 1, j - 1))
        if j != len(cave[i]) - 1:
            n.add((i - 1, j + 1))
    if i != len(cave) - 1:
        n.add((i + 1, j))
        if j != 0:
            n.add((i + 1, j - 1))
        if j != len(cave[i]) - 1:
            n.add((i + 1, j + 1))
    if j != 0:
        n.add((i, j - 1))
    if j != len(cave[i]) - 1:
        n.add((i, j + 1))
    return n

def simulate(cave):
    flash_count = [0]
    for i in range(len(cave)):
        for j in range(len(cave[i])):
            cave[i][j] += 1
    flashed = set()

    def flash(i, j, first=True):
        # Find neighbors
        if (i, j) not in flashed:
            if not first:
                cave[i][j] += 1
            if cave[i][j] > 9:
                flash_count[0] += 1
                flashed.add((i, j))
                neighbors = find_neighbors(cave, i, j)
                for i_n, j_n in neighbors:
                    flash(i_n, j_n, False)

    for i in range(len(cave)):
        for j in range(len(cave[i])):
            flash(i, j)
            for i_f, j_f in flashed:
                cave[i_f][j_f] = 0
    return flash_count[0]


def puzzle_one():
    cave = []

    with open('input') as f:
        for line in f:
            cave.append(list(map(int, list(line.strip()))))
        flash_count = 0
        for _ in range(100):
           flash_count += simulate(cave)
    print(flash_count)


def puzzle_two():
    flash_count = 0
    step = 0
    cave = []
    with open('input') as f:
        for line in f:
            cave.append(list(map(int, list(line.strip()))))

    while flash_count != len(cave) * len(cave[0]):
        flash_count = simulate(cave)
        step += 1
    print(step)


if __name__ == '__main__':
    puzzle_one()
    puzzle_two()
