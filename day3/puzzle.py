"""
P1. Calculate "gamma rate" and "epsilon rate" from input
Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers
P2. Calculate "oxygen generator rating" and "CO2 scrubber rating" filter numbers by bit crtirerias
To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position.
To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position.
If 0 and 1 are equally common, keep values with a 0 in the position being considered.
"""


def puzzle_one():
    with open('input') as f:
        diagnostics = f.readlines()
        bits = [0] * len(diagnostics[0].strip())
        for d in diagnostics:
            for idx, bit in enumerate(d):
                if bit.strip() == '1':
                    bits[idx] += 1
        gamma_rate = int(''.join(['0' if len(diagnostics) - bits[i] > bits[i] else '1' for i in range(len(bits))]), 2)
        epsilon_rate = (2 ** len(bits) - 1) ^ gamma_rate
        print(f'epsilon_rate = {epsilon_rate}, gamma_rate = {gamma_rate}. Result = {epsilon_rate * gamma_rate}')


def count_ones_in_pos(l, p):
    cnt = 0
    for i in l:
        if i[p] == '1':
           cnt += 1
    return cnt


def puzzle_two():
    with open('input') as f:
        pos = 0
        diagnostics = list(map(lambda x: x.strip(), f.readlines()))
        while len(diagnostics) > 1:
            target_bit = '0' if count_ones_in_pos(diagnostics, pos) < len(diagnostics) // 2 else '1'
            diagnostics = list(filter(lambda d: d[pos] == target_bit, diagnostics))
            pos += 1
        ox_rate = int(diagnostics[0], 2)

    with open('input') as f:
        pos = 0
        diagnostics = list(map(lambda x: x.strip(), f.readlines()))
        while len(diagnostics) > 1:
            target_bit = '0' if count_ones_in_pos(diagnostics, pos) >= len(diagnostics) // 2 else '1'
            diagnostics = list(filter(lambda d: d[pos] == target_bit, diagnostics))
            pos += 1
        co2_rate = int(diagnostics[0], 2)

    print(f'oxygen rate = {ox_rate}, co2 rate = {co2_rate}. Result = {ox_rate * co2_rate}')


if __name__ == '__main__':
    puzzle_one()
    puzzle_two()

