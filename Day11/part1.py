'''
parse graph and count paths from you to out
its director for part1
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

memo = {}
seen = set()

def dp(curr,parent,graph,memo):
    if curr == 'out':
        return 1
    if curr in memo:
        return memo[curr]
    ways = 0
    seen.add(curr)
    for neigh in graph[curr]:
        if neigh not in seen and neigh != parent:
            ways += dp(neigh,curr,graph,memo)
    seen.remove(curr)
    memo[curr] = ways
    return ways

print(dp('you',-1,graph,memo))