from collections import defaultdict

'''
given a grid, count (i,j) spots where its a '@'
check all eith adjacnet spots, which should be < 4 '@' in total
'''
lines = open("puzzle.txt","r")
grid = []
for l in lines:
    l = l.strip()
    grid.append(l)

rows,cols = len(grid),len(grid[0])
ans = 0

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '@':
            count = 0
            for di in [-1,0,1]:
                for dj in [-1,0,1]:
                    if (di,dj) != (0,0):
                        ii = i + di
                        jj = j + dj
                        if 0 <= ii < rows and 0 <= jj < cols:
                            count += grid[ii][jj] == '@'
            if count < 4:
                ans += 1
print(ans)

