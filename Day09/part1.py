'''
given list of x,y points, make the largest rectangle
brute force all corners
'''

with open("puzzle.txt","r") as file:
    lines = file.read().splitlines()

data = [list(map(int,l.split(","))) for l in lines]
ans = 0
n = len(data)

for i in range(n):
    for j in range(i+1,n):
        p1,p2 = data[i],data[j]
        x1,y1 = p1
        x2,y2 = p2
        smallest_x = min(x1,x2)
        largest_x = max(x1,x2)
        smallest_y = min(y1,y2)
        largest_y = max(y1,y2)
        area = (largest_x - smallest_x + 1)*(largest_y - smallest_y + 1)
        ans = max(ans,area)
print(ans)