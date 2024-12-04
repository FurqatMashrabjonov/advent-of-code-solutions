with open("input.txt", "r") as file:
    lines = file.readlines()

left_locations  = []
right_locations = []

for line in lines: 
    numbers = line.split()
    left_locations.append(int(numbers[0]))
    right_locations.append(int(numbers[1]))

left_locations = sorted(left_locations)
right_locations = sorted(right_locations)

distance = 0

for l, r in zip(left_locations, right_locations):
    distance += abs(l - r)

print(distance)