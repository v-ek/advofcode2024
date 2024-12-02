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

# Build counts for each value in the right 
counts = {}
for value in right_values:
    counts[value] = counts.get(value, 0) + value

similary_score = 0
for value in left_values:
    similary_score += counts.get(value, 0)
    
print(similary_score)
