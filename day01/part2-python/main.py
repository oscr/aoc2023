import re

toDigits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

lines = open('input.txt', 'r').read().split('\n')
digitsAndWords = [ re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line) for line in lines]
digits = [[d if d not in toDigits else toDigits[d] for d in line] for line in digitsAndWords]
calibratedValues = [int("{}{}".format(line[0], line[-1])) for line in digits if line != []]

print(sum(calibratedValues))