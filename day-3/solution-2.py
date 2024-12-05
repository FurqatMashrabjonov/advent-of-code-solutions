import re

with open("input.txt", "r") as file:
    text = file.read()

instructions = re.findall(r"(don't\(\)|do\(\)|mul\(\d+\s*,\s*\d+\))", text)

res = 0
enabled = True
for instruction in instructions:
    if (instruction == "don't()"):
        enabled = False
    elif (instruction == 'do()'):
        enabled = True
    else:
        if enabled:
            numbers = re.findall(r'\d+', instruction)
            res += int(numbers[0]) * int(numbers[1])


print(res)