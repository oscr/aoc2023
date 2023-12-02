import re


def get_minimum_cubes(counts):
    return max([int(n) for n in counts])

lines = open('../input.txt', 'r').read().split('\n')

sum = 0
for game, line in enumerate(lines, start=1):
    red = get_minimum_cubes(re.findall(r"(?=(\d+) red)", line))
    green = get_minimum_cubes(re.findall(r"(?=(\d+) green)", line))
    blue = get_minimum_cubes(re.findall(r"(?=(\d+) blue)", line))
    sum += red * green * blue

print(sum)