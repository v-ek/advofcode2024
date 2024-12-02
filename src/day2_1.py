with open("inputs/day2_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

safe_reports = 0
for line in lines:
    values = [int(value) for value in line.split(" ")]
    prev_value = values[0]
    prev_sign = None
    sign = None
    for value in values[1:]:
        diff = value - prev_value
        abs_diff = abs(diff)
        if diff == abs_diff:
            sign = "+"
        else:
            sign = "-"
        if not (abs_diff >= 1 and abs_diff <= 3 and (sign == prev_sign or prev_sign is None)):
            break
        prev_sign = sign
        prev_value = value
    else:
        safe_reports += 1

print(safe_reports)
