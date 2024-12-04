with open("input.txt", "r") as file:
    lines = file.readlines()

left_locations  = []
right_appears = {}

for line in lines: 
    numbers = line.split()
    left_locations.append(int(numbers[0]))
    
    right_appears[numbers[1]] = 1 + right_appears.get(str(numbers[1]), 0)

result = 0

for num in left_locations:
    result += num * right_appears.get(str(num), 0)

print(result)

