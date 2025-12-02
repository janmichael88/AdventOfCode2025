from collections import defaultdict

'''
for part 2, we need to count the number of times a dial hits a zero
just calculate distance to zero before incrementing
brute force works fine
'''
lines = open("puzzle.txt", "r")
count = 0
curr = 50
n = 100

for l in lines:
    l = l.strip()
    direction = 1 if l[0] == 'R' else -1
    #we can brute force in babysteps
    num = int(l[1:])
    for step in range(num):
        curr = curr + 1*direction
        curr = curr % n
        if curr == 0:
            count += 1


print(count)

with open('puzzle.txt') as f:
    turns = [line.strip() for line in f]

moves = [(t[0], int(t[1:])) for t in turns]

# PART 2
position = 50
zeros = 0
for direction, num in moves:
    if direction == "L":
        if (position - num) < 0:
            zeros += abs((100 + position - num) // 100)
            if position != 0:
                zeros += 1
        position = (position - num) % 100
        if position == 0:
            zeros += 1
    elif direction == "R":
        zeros += (position + num) // 100
        position = (position + num) % 100
result2 = zeros
print("Result 2:", result2)