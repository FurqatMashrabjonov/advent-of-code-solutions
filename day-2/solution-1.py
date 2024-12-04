with open("input.txt", "r") as file:
    lines = file.readlines()

reports  = []

for line in lines: 
    numbers = line.split()
    levels = []
    for num in numbers:
        levels.append(int(num))
    reports.append(levels)


def non_decreasing(L):
    return all(x<=y for x, y in zip(L, L[1:]))
def non_increasing(L):
    return all(x>=y for x, y in zip(L, L[1:]))
def monotonic(L):
    return non_decreasing(L) or non_increasing(L)

def is_safe(level):
    if (not monotonic(level)):
        return False
    
    for i in range(1, len(level)):
        dis = abs(level[i] - level[i - 1])
        if (dis < 1 or dis > 3):
            return False
    
    return True
    
res = 0
for level in reports:
    if (is_safe(level)):
        res += 1

print(res)