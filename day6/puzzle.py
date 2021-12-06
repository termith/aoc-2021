from collections import Counter


def simulate(days):
    with open('input') as f:
        population = Counter(list(map(int, f.read().split(','))))
    for _ in range(days):
        next_gen = population[0]
        population[0] = 0
        for i in range(1,9):
            population[i-1] += population[i]
            population[i] = 0
        population[6] += next_gen
        population[8] += next_gen

    return sum(population.values())


if __name__ == '__main__':
    print(simulate(80))
    print(simulate(256))
