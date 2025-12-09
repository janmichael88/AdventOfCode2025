'''
need to count the number of times it hits as ^
count the indicies in hashset
dfs and mark the indices for splitters
'''

from collections import deque

with open("puzzle.txt","r") as f:
    lines = f.read().splitlines()

rows,cols = len(lines),len(lines[0])
curr_row,curr_col = 0,-1
for i,ch in enumerate(lines[0]):
    if ch == 'S':
        curr_col = i
        break


seen = set()
splitters = set()
q = deque([(curr_row,curr_col)])

while q:
    i,j = q.popleft()
    if (i,j) in seen:
        continue
    seen.add((i,j))
    #go down
    ii,jj = i+1,j
    if 0 <= ii < rows and 0 <= jj < cols:
        if lines[ii][jj] == '.':
            q.append((ii,jj))
        if lines[ii][jj] == '^':
            splitters.add((ii,jj))
            left = j-1
            right = j+1
            if 0 <= left < cols and 0 <= right < cols:
                q.append((ii,left))
                q.append((ii,right))

print(len(splitters))



