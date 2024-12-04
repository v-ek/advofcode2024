import re

with open("inputs/day3_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

pattern = re.compile(r"mul\((\d+),(\d+)\)")
sum_of_prods = 0
for line in lines:
    matches = pattern.findall(line)
    if matches:
        sum_of_prods += sum((int(entry[0])*int(entry[1]) for entry in matches))

print(sum_of_prods)
