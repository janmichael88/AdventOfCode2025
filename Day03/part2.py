from collections import defaultdict

'''
need to reframe problem is picking numbers from array in order, such that we get the largest number possible
jesus dp already, pick or dont pick
'''

lines = open("sample.txt","r")

def dp(i,arr,memo,k):
    n = len(arr)
    if i >= n:
        if k == 0:
            return 0
        return float('-inf')
    if (i,k) in memo:
        return memo[(i,k)]

    if k < 0:
        return float('-inf')
    take = dp(i+1,arr,memo,k-1)*10 + arr[i]
    no_take = dp(i+1,arr,memo,k)
    ans = max(take,no_take)
    memo[(i,k)] = ans
    return ans

memo = {}
test =  [8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1]
test = test[::-1]

lines = open("puzzle.txt","r")
ans = 0
for l in lines:
    l = l.rstrip()
    nums = [int(n) for n in l]
    nums = nums[::-1]
    memo = {}
    largest = dp(0,nums,memo,12) 
    ans += largest

print(ans)


