from collections import defaultdict


def puzzle_one():
    points = defaultdict(int)
    with open('input') as f:
        for line in f:
            x1, y1, x2, y2 = tuple(map(int, line.replace(' -> ',  ',').split(',')))
            if x1 == x2:
                if y1 < y2:
                    y2, y1 = y1, y2
                while y1 >= y2:
                    points[(x1, y1)] += 1
                    y1 -= 1
            elif y1 == y2:
                if x1 < x2:
                    x2, x1 = x1, x2
                while x1 >= x2:
                    points[(x1, y1)] += 1
                    x1 -= 1
    print(len(list(filter(lambda x: x > 1, points.values()))))


def puzzle_two():
    points = defaultdict(int)
    with open('input') as f:
        for line in f:
            x1, y1, x2, y2 = tuple(map(int, line.replace(' -> ',  ',').split(',')))
            print(x1, y1, x2, y2)
            if x1 == x2:
                if y1 < y2:
                    y2, y1 = y1, y2
                while y1 >= y2:
                    points[(x1, y1)] += 1
                    y1 -= 1
            elif y1 == y2:
                if x1 < x2:
                    x2, x1 = x1, x2
                while x1 >= x2:
                    points[(x1, y1)] += 1
                    x1 -= 1
            else:
                if x1 > x2:
                    if y1 > y2:
                        while x1 >= x2 and y1 >= y2:
                            points[(x1, y1)] += 1
                            x1 -= 1
                            y1 -= 1
                    else:
                        while x1 >= x2 and y1 <= y2:
                            points[(x1, y1)] += 1
                            x1 -= 1
                            y1 += 1
                else:
                    if y1 > y2:
                        while x1 <= x2 and y1 >= y2:
                            points[(x1, y1)] += 1
                            x1 += 1
                            y1 -= 1
                    else:
                        while x1 <= x2 and y1 <= y2:
                            points[(x1, y1)] += 1
                            x1 += 1
                            y1 += 1
    print(len(list(filter(lambda x: x > 1, points.values()))))


if __name__ == '__main__':
    puzzle_one()
    puzzle_two()