import re


def is_possible_count(counts, limit):
    return all([int(count) <= limit for count in counts])

lines = open('../input.txt', 'r').read().split('\n')

sum = 0
for game, line in enumerate(lines, start=1):
    red = is_possible_count(re.findall(r"(?=(\d+) red)", line), 12)
    green = is_possible_count(re.findall(r"(?=(\d+) green)", line), 13)
    blue = is_possible_count(re.findall(r"(?=(\d+) blue)",  line), 14)
    if all([red, green, blue]):
        sum += game

print(sum)