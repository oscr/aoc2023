def parse_input(lines):
    seeds = [int(i) for i in filter(None, lines[0].split(": ")[1].split(" "))]

    maps = []
    for line in lines[1:]:
        conversions = []
        for row in line.split("\n")[1:]:
            destination, source, length = [int(i) for i in row.split()]
            conversions.append((destination, source, length))

        conversions.sort()
        maps.insert(0, conversions)  # Reverse the maps order

    return seeds, maps


def get_seed_ranges(seeds):
    ranges = []
    for i, seed in enumerate(seeds):
        if i % 2 == 0:
            ranges.append([seed, seed + seeds[i+1]])
    return ranges


def is_valid_seed(i, seed_ranges):
    return any(start <= i <= end for start, end in seed_ranges)


def location_to_seed(location, maps):
    for step in maps:
        for destination, source, length in step:
            if destination <= location < destination+length:
                location = location - destination + source
                break
    return location


def solve_part1(filename='../input_example.txt'):
    lines = open(filename, 'r').read().split('\n\n')
    seeds, almanac = parse_input(lines)
    current = 0
    while True:
        seed = location_to_seed(current, almanac)
        if seed in seeds:
            return current
        current += 1


def solve_part2(filename='../input_example.txt'):
    lines = open(filename, 'r').read().split('\n\n')
    seeds, almanac = parse_input(lines)
    seed_ranges = get_seed_ranges(seeds)
    current = 0
    while True:
        seed = location_to_seed(current, almanac)
        if is_valid_seed(seed, seed_ranges):
            return current
        current += 1


if __name__ == "__main__":
    assert solve_part1('../input_example.txt') == 35
    assert solve_part2('../input_example.txt') == 46
    assert solve_part1('../input.txt') == 51580674
    assert solve_part2('../input.txt') == 99751240