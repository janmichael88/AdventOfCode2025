'''
same as part1, but we want to from svr to out
and we need to touch dac to fft
it could be
svr ... dac ... fft ... out
svr ... fft ... dac ... out

holy shit it worked! lmaoooo
'''
import collections
with open("puzzle.txt","r") as file:
    lines = file.read().splitlines()

graph = collections.defaultdict(list)
for l in lines:
    l = l.split(": ")
    u = l[0]
    for v in l[1].split(" "):
        graph[u].append(v)

def dp(curr,parent,graph,memo,seen,end):
    if curr == end:
        return 1
    if curr in memo:
        return memo[curr]
    ways = 0
    seen.add(curr)
    for neigh in graph[curr]:
        if neigh not in seen and neigh != parent:
            ways += dp(neigh,curr,graph,memo,seen,end)
    seen.remove(curr)
    memo[curr] = ways
    return ways

arr = [["svr","fft"],["fft","dac"],["dac","out"]]

ans = 1
for start,end in arr:
    seen = set()
    memo = {}
    ways = dp(start,-1,graph,memo,seen,end)
    ans *= ways

print(ans)