from collections import defaultdict

'''
two inputs seperated by double linebreak
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

arr2 = []
for l in ids.split("\n"):
    arr2.append(int(l))

#check ranges
fresh = set()
for id in arr2:
    for l,r in arr1:
        if l <= id <= r:
            fresh.add(id)

print(len(fresh))