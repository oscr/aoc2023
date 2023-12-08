import re
import math


def steps_to_end(instructions, nodes, current):
    steps = 0
    while not current.endswith("Z"):
        current = nodes[instructions[steps % len(instructions)]][current]
        steps += 1
    return steps


def solve_part1(instructions, nodes):
    return steps_to_end(instructions, nodes, 'AAA')


def solve_part2(instructions, nodes, start_nodes):
    steps = 1
    for node in start_nodes:
        steps = math.lcm(steps, steps_to_end(instructions, nodes, node))
    return steps


def parse_input_part2(filename):
    file = open(filename, 'r').read()
    start_nodes = re.findall(r"(\w{2}A) =", file)
    return *parse_input(filename), start_nodes


def parse_input(filename):
    lines = open(filename, 'r').read().splitlines()

    instructions = [*lines[0]]
    nodes_left = {}
    nodes_right = {}
    for line in lines[2:]:
        node, left, right = re.findall(r"\w{3}", line)
        nodes_left[node] = left
        nodes_right[node] = right
    nodes = {"L": nodes_left, "R": nodes_right}
    return instructions, nodes


if __name__ == "__main__":
    assert solve_part1(*parse_input('../input_example_1.txt')) == 2
    assert solve_part1(*parse_input('../input_example_2.txt')) == 6
    assert solve_part1(*parse_input('../input.txt')) == 17287
    assert solve_part2(*parse_input_part2('../input_example_3.txt')) == 6
    assert solve_part2(*parse_input_part2('../input.txt')) == 18625484023687