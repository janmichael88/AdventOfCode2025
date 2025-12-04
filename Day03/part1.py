from collections import defaultdict

'''
sort each line and get the two largest batteries
need to maintain order
'''

lines = open("puzzle.txt","r")
ans = 0
for l in lines:
    l = l.rstrip()
    nums = [int(n) for n in l]
    n = len(nums)
    largest = 0
    for i in range(n):
        for j in range(i+1,n):
            curr = nums[i]*10 + nums[j]
            largest = max(largest,curr)
    ans += largest

print(ans)