'''
dp, count paths
'''

with open("puzzle.txt","r") as f:
    lines = f.read().splitlines()

rows,cols = len(lines),len(lines[0])
curr_row,curr_col = 0,-1
for i,ch in enumerate(lines[0]):
    if ch == 'S':
        curr_col = i
        break

memo = {}
def dp(i,j):
    #valid count
    if i == rows - 1:
        return 1
    if (i,j) in memo:
        return memo[(i,j)]
    #go down
    ii,jj = i+1,j
    ways = 0
    if 0 <= ii < rows and 0 <= jj < cols:
        if lines[ii][jj] == '.':
            ways += dp(ii,jj)
        if lines[ii][jj] == '^':
            left = j-1
            right = j+1
            if 0 <= left < cols and 0 <= right < cols:
                ways += dp(ii,left)
                ways += dp(ii,right)
    memo[(i,j)] = ways
    return ways

print(dp(curr_row,curr_col))