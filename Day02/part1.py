from collections import defaultdict

'''
need to look for invalid ids
invalid ids are just numbers concatcted with the same number twice
for each number in the range, check if left half == right  half
'''
lines = open("puzzle.txt","r")
data = list(l.split(",") for l in lines)
data = data[0]
ans = 0
for r in data:
    start,end = r.split("-")
    start,end = int(start),int(end)
    for num in range(start,end+1):
        str_num = str(num)
        if len(str_num) % 2 == 0:
            mid = len(str_num) // 2
            left = str_num[:mid]
            right = str_num[mid:]
            if left == right:
                ans += int(num)
print(ans)