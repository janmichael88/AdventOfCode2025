'''
first parse data,
lights, buttons,joltages
same as part1, excepy that we the buttons are counters, to each index
and we must have the joltages
need to use linear programming
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

def bfs(joltages,buttons):
    k = len(joltages)
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
            if curr == joltages:
                return ans
            for b in buttons:
                next_mask = curr[:]
                for num in b:
                    next_mask[num] += 1
                if tuple(next_mask) not in seen:
                    seen.add(tuple(next_mask))
                    next_q.append(next_mask)
        ans += 1
        q = next_q
    return ans

temp = 0
i = 0
for l,b,j in zip(lights,buttons,joltages):
    ans = bfs(j,b)
    print(i)
    temp += ans
    i += 1

print(temp)