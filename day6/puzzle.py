
def simulate(days):
    with open('input') as f:
        lanternfishes = list(map(int, f.read().split(',')))
        for _ in range(days):
            next_generation = []
            for i in range(len(lanternfishes)):
                if lanternfishes[i] == 0:
                    next_generation.append(8)
                    lanternfishes[i] = 6
                else:
                    lanternfishes[i] -= 1
            lanternfishes.extend(next_generation)
    return len(lanternfishes)


if __name__ == '__main__':
    print(simulate(80))
    print(simulate(256))
