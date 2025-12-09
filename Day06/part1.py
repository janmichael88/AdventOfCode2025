from collections import defaultdict
import math
'''
parsing problem
'''
lines = open("puzzle.txt","r")
data = [l.strip() for l in lines]
nums = [l.split() for l in data[:-1]]
ops = data[-1].split()
rows,cols = len(nums),len(nums[0])
ans = 0
for j in range(cols):
    curr_col = []
    for i in range(rows):
        curr_col.append(int(nums[i][j]))
    
    if ops[j] == '+':
        ans += sum(curr_col)
    else:
        ans += math.prod(curr_col)

print(ans)
