from collections import deque

def puzzle_one():
    floor_map = []
    min_heights = []
    coords = []
    with open('input') as f:
        for line in f:
            floor_map.append([int(h) for h in line.strip()])
    for i in range(len(floor_map)):
        for j in range(len(floor_map[i])):
            current_height = floor_map[i][j]
            up = 10 if i == 0 else floor_map[i - 1][j]
            down = 10 if i == len(floor_map) - 1 else floor_map[i + 1][j]
            left = 10 if j == 0 else floor_map[i][j - 1]
            right = 10 if j == len(floor_map[0]) - 1 else floor_map[i][j + 1]
            if current_height < up and current_height < down and current_height < left and current_height < right:
                min_heights.append(current_height)
                coords.append((i, j))
    print(sum(min_heights) + len(min_heights))
    return coords


def calc_basin(point, floor_map):
    todo = deque()
    checked = set()
    todo.append(point)
    while todo:
        p = todo.popleft()
        checked.add(p)
        i, j = p
        if i > 0:
            if floor_map[i-1][j] != 9 and (i-1, j) not in checked:
                todo.append((i-1, j))
        if i < len(floor_map) - 1:
            if floor_map[i+1][j] != 9 and (i+1, j) not in checked:
                todo.append((i+1, j))
        if j > 0:
            if floor_map[i][j-1] != 9 and (i, j-1) not in checked:
                todo.append((i, j-1))
        if j < len(floor_map[0]) - 1:
            if floor_map[i][j+1] != 9 and (i, j+1) not in checked:
                todo.append((i, j+1))

    return len(checked)


def puzzle_two(min_heights):
    floor_map = []
    basin_lengths = []
    with open('input') as f:
        for line in f:
            floor_map.append([int(h) for h in line.strip()])
    for point in min_heights:
        basin_lengths.append(calc_basin(point, floor_map))
    basin_lengths.sort(reverse=True)
    result = 1
    for l in basin_lengths[:3]:
        result *= l
    print(result)


if __name__ == '__main__':
    min_heights = puzzle_one()
    puzzle_two(min_heights)
