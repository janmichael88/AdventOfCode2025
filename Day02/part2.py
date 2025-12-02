from collections import defaultdict

'''
for part 2, invalid ids, can be made of sequences where there are at least 2 reptitions
say we have number like
1234
we need to check

'''
def check(num):
    n = len(num)

    # Try every prefix length k (block size)
    for k in range(1, n):  # block must be at least length 1
        if n % k != 0:
            continue  # block size must divide total length

        block = num[:k]
        times = n // k

        if block * times == num:  # repeated pattern
            return True

    return False

        

lines = open("puzzle.txt","r")
data = list(l.split(",") for l in lines)
data = data[0]
ans = 0
for r in data:
    start,end = r.split("-")
    start,end = int(start),int(end)
    for num in range(start,end+1):
        str_num = str(num)
        if check(str_num):
            ans += num

print(ans)
