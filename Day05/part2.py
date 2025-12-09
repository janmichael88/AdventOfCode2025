from collections import defaultdict

'''
two inputs seperated by double linebreak
for part 2, we need the unique ranges, and then merge them, we don't the second input
'''
with open("puzzle.txt", "r", encoding="utf-8") as f:
    text = f.read()

blocks = text.split("\n\n")
ranges = blocks[0]
ids = blocks[1]

arr1 = []
for l in ranges.split("\n"):
    l = l.split("-")
    left,right = int(l[0]),int(l[1])
    arr1.append([left,right])

arr1.sort(key = lambda x: (x[0],x[1]))
curr = [arr1[0]]

for l,r in arr1[1:]:
    #merge
    if curr[-1][0] <= l <= curr[-1][1]:
        curr[-1][0] = min(curr[-1][0],l)
        curr[-1][1] = max(curr[-1][1],r)
    #add
    else:
        curr.append([l,r])

fresh = 0
for l,r in curr:
    fresh += r - l + 1

print(fresh)
