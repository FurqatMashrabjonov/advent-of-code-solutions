import re

with open("input.txt", "r") as file:
    text = file.read()

matches = re.findall(r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)', text)

res = 0
for nums in matches:
    res += int(nums[0]) * int(nums[1])

print(res)