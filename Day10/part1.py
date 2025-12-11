'''
first parse data,
lights, buttons,joltages
im thinking dp on subsets press or don't press
the problem is it worth repeating a button multiple times?

say we have this:
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
final state is 
[0,1,1,0]

we can use 
[0,0,0,1] 3
[0,1,0,1] 1,3
[0,0,1,0] 2
[0,0,1,1] 2,3
[1,0,1,0] 0,2
[1,1,0,0] 0,1

reframe as use subarrays to get final state starting from the zeros array
'''
import re
from collections import deque
with open("puzzle.txt","r") as file:
    lines = file.read().splitlines()

def parse_lights(lights):
    lights = list(lights[0])
    lights = [0 if ch == '.' else 1 for ch in lights]
    return lights

def parse_buttons(buttons):
    buttons = [ch.split(",") for ch in buttons]
    buttons = [list(map(int,b)) for b in buttons]
    return buttons

def parse_jolts(jolts):
    jolts = [ch.split(",") for ch in jolts]
    jolts = [list(map(int,b)) for b in jolts]
    return jolts[0]

brackets = r"\[(.*?)\]"
parens = r"\((.*?)\)"
curls = r"\{(.*?)\}"
lights = []
buttons = []
joltages = []
for l in lines:
    lights.append(parse_lights(re.findall(brackets,l)))
    buttons.append(parse_buttons(re.findall(parens,l)))
    joltages.append(parse_jolts(re.findall(curls,l)))


def dp(curr,i,end,n,memo,buttons):
    if i >= n:
        if curr == end:
            return 0
        return float('inf')
    key = (tuple(curr),i)
    if key in memo:
        return memo[key]
    skip = dp(curr,i+1,end,n,memo,buttons)
    next_mask = list(curr)
    bs = buttons[i]
    for b in bs:
        next_mask[b] = 1 - next_mask[b]
    no_skip = 1 + dp(next_mask,i+1,end,n,memo,buttons)
    ans = min(skip,no_skip)
    memo[key] = ans
    return ans

#we can just use bfs, and just use xor after converting to ints

def bfs(lights,buttons):
    k = len(lights)
    curr = [0]*k
    seen = set()
    seen.add(tuple(curr))
    q = deque([curr])
    ans = 0
    while q:
        n = len(q)
        next_q = deque([])
        for _ in range(n):
            curr = q.popleft()
            if curr == lights:
                return ans
            for b in buttons:
                next_mask = curr[:]
                for num in b:
                    next_mask[num] = 1 - next_mask[num]
                if tuple(next_mask) not in seen:
                    seen.add(tuple(next_mask))
                    next_q.append(next_mask)
        ans += 1
        q = next_q
    return ans

temp = 0
for l,b,j in zip(lights,buttons,joltages):
    ans = bfs(l,b)
    temp += ans

print(temp)