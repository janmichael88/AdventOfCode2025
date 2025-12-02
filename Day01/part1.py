from collections import defaultdict

'''
dial starts at 50
there are 99 numbers
can turn left or right
use mod 100
count number of times it hits zero
'''
lines = open("puzzle.txt","r")
count = 0
curr = 50
for l in lines:
    l = l.strip("\n")
    direction = l[0]
    num = int(l[1:])
    if direction == 'L':
        curr = (curr - num) % 100
    else:
        curr = (curr + num) % 100
    
    count += curr == 0

print(count)

