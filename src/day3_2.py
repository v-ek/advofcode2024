import re

with open("inputs/day3_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

pattern = re.compile(r"^ul\((\d+),(\d+)\)")

sum_of_prods = 0
enabled = True
for line in lines:
    idx = 0
    length = len(line)
    while idx < length:
        if line[idx] == "d":
            if line[idx+1:idx+4] == "o()":
                enabled = True
                idx += 4
                continue
            elif line[idx+1:idx+7] == "on't()":
                enabled = False
                idx += 7
                continue
        elif line[idx] == "m" and enabled:
            if match := pattern.match(line[idx+1:]):
                sum_of_prods += int(match.group(1)) * int(match.group(2))
                idx += 1 + match.end(0)
                continue
        idx += 1
print(sum_of_prods)
