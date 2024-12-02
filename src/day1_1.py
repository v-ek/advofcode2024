with open("inputs/day1_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

left_values = []
right_values = []
for line in lines:
    left, right = line.split("  ")
    left_values.append(int(left))
    right_values.append(int(right))

left_values.sort()
right_values.sort()
    
print(sum((abs(left - right) for left, right in zip(left_values, right_values))))