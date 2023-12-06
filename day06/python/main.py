import re
import math


def solve_part1(filename='../input_example.txt'):
    races = parse_input_part1(filename)
    return calculate_records(races)


def solve_part2(filename='../input_example.txt'):
    races = parse_input_part2(filename)
    return calculate_records(races)


def calculate_records(races):
    records = []
    for time, distance in races:
        i = 0
        for t in range(time):
            if t * (time - t) > distance:
                i += 1
        records.append(i)
    return math.prod(records)


def parse_input_part2(filename):
    time, distance = open(filename, 'r').read().splitlines()
    times = int(time.split(":")[1].replace(" ", ""))
    distances = int(distance.split(":")[1].replace(" ", ""))
    return [(times, distances)]


def parse_input_part1(filename):
    time, distance = open(filename, 'r').read().splitlines()
    times = [int(i) for i in re.findall(r"\d+", time)]
    distances = [int(i) for i in re.findall(r"\d+", distance)]
    return zip(times, distances)


if __name__ == "__main__":
    assert solve_part1('../input_example.txt') == 288
    assert solve_part2('../input_example.txt') == 71503
    assert solve_part1('../input.txt') == 3316275
    assert solve_part2('../input.txt') == 27102791