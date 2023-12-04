import math


def parse_line(line):
    winning, numbers = line.split(":")[1].split("|")
    winning = list(filter(None, winning.split(" ")))
    numbers = list(filter(None, numbers.split(" ")))
    return winning, numbers


def to_points(count):
    if count == 0:
        return 0
    else:
        return math.pow(2, count-1)


def solve_part1(filename='../input_example.txt'):
    lines = open(filename, 'r').read().split('\n')

    result = 0
    for i, line in enumerate(lines, start=1):
        winning, numbers = parse_line(line)
        winning_count = 0
        for n in numbers:
            if n in winning:
                winning_count += 1
        result += to_points(winning_count)
    return result


def solve_part2(filename='../input_example.txt'):
    lines = open(filename, 'r').read().split('\n')

    result = 0
    cards = [1 for i in range(len(lines))]
    for i, line in enumerate(lines, start=0):
        result += cards[i]
        winning, numbers = parse_line(line)
        winning_count = 0
        for n in numbers:
            if n in winning:
                winning_count += 1
        for w in range(1, winning_count+1):
            cards[i+w] += cards[i]
    return result


if __name__ == "__main__":
    assert solve_part1('../input_example.txt') == 13
    assert solve_part2('../input_example.txt') == 30
    print(solve_part1('../input.txt'))
    print(solve_part2('../input.txt'))