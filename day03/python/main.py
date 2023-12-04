import re


def is_valid(row, column):
    """Ensure we don't get indexes outside the 2d array"""
    return 0 <= row <= len(schematic) - 1 and 0 <= column <= len(schematic[0]) - 1


def is_numeric(row, column):
    return is_valid(row, column) and schematic[row][column].isnumeric()


def is_symbol(row, column):
    return is_valid(row, column) and schematic[row][column] != "."


def find_match(row, column):
    """Finds the part within at a certain coordinate"""
    return [m for m in matches if m["row"] == row and m["start"] <= column <= m["end"]]


def is_gear(row, column):
    """Looks for two parts around the gear "*" symbol"""
    values = []

    if is_numeric(row, column - 1): values.append(find_match(row, column - 1))
    if is_numeric(row, column + 1): values.append(find_match(row, column + 1))
    if is_numeric(row - 1, column):
        values.append(find_match(row - 1, column))
    else:
        if is_numeric(row - 1, column - 1): values.append(find_match(row - 1, column - 1))
        if is_numeric(row - 1, column + 1): values.append(find_match(row - 1, column + 1))
    if is_numeric(row + 1, column):
        values.append(find_match(row + 1, column))
    else:
        if is_numeric(row + 1, column - 1): values.append(find_match(row + 1, column - 1))
        if is_numeric(row + 1, column + 1): values.append(find_match(row + 1, column + 1))

    if len(values) == 2:
        return values[0][0]["value"] * values[1][0]["value"]
    else:
        return 0


def is_part(row, column, length):
    """A valid part has a symbol as beside it"""
    return is_symbol(row, column - 1) or \
        is_symbol(row, column + length) or \
        any([is_symbol(row-1, column+i) for i in range(-1, length + 1)]) or \
        any([is_symbol(row+1, column+i) for i in range(-1, length + 1)])


schematic = open('../input.txt', 'r').read().split('\n')

parts = re.compile(r"\d+")
gears = re.compile(r"\*")

solution_part1 = 0
solution_part2 = 0
matches = []
for row in range(len(schematic)):
    for match in parts.finditer(schematic[row]):
        if is_part(row, match.start(), len(match.group())):
            solution_part1 += int(match.group())
            matches.append({"row": row, "start": match.start(), "end": match.end(), "value": int(match.group())})

for row in range(len(schematic)):
    for match in gears.finditer(schematic[row]):
        solution_part2 += is_gear(row, match.start())


assert solution_part1 == 536576
assert solution_part2 == 467835

print("part 1: ", solution_part1)
print("part 2: ", solution_part2)