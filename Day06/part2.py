from collections import defaultdict
import math
'''
now traverse right to left and do on columns
right pad with zeros, then traverse the column again
i need to split along each column somehow -__-
walk the grid....
'''
lines = open("sample.txt","r")
data = [l.rstrip("\n") for l in lines]
rows,cols = len(data), max([len(r) for r in data])

ans = 0
i,j = rows-1,0
while j < cols:
    #find next problem
    next_j = j+1
    while next_j < cols and next_j == " ":
        next_j += 1
    print(j,next_j + 1,data[i][j])
    #j to next_j + 1 are the boundaies
    curr_op = data[i][j]
    nums = []
    for col in range(j,next_j+2):
        if col >= cols:
            continue
        curr_num = ""
        for row in range(rows-1):
            curr_num += data[row][col]
        curr_num = curr_num.strip()
        if len(curr_num) > 0:
            nums.append(int(curr_num))
        print(curr_num)
    if curr_op == '+':
        ans += sum(nums)
    else:
        ans += math.prod(nums)
    j = next_j + 3

    
print(ans)

from math import prod
from itertools import zip_longest

with open("puzzle.txt", "r") as f:
    lines = f.read().splitlines()

key = [line.split() for line in lines]
ops = list(zip(*key))

grand_total = 0
for p in ops:
    if p[-1] == '*':
        grand_total += prod([int(t) for t in p[:-1]])
    else:
        grand_total += sum([int(t) for t in p[:-1]])

# part 1
print(grand_total)

with open("puzzle.txt") as f:
    rows = f.read().splitlines()

cols = list(zip_longest(*rows, fillvalue=' '))

grand_total = 0
idx = 0
while idx < len(cols):
    row = cols[idx]

    # operator is always last element of the tuple
    op = row[-1]

    operands = []

    # read operand rows until a blank tuple
    while idx < len(cols) and any(c != ' ' for c in cols[idx]):
        tup = cols[idx]

        # everything except the last column is a potential digit
        digit_part = ''.join(c for c in tup[:-1] if c.isdigit())

        if digit_part:
            operands.append(int(digit_part))

        idx += 1

    # Now we’re on the blank separator row — skip it
    idx += 1

    # Apply the operation
    if op == '+':
        grand_total += sum(operands)
    else:
        grand_total += prod(operands)

print(grand_total)