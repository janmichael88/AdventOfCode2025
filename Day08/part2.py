'''
generatting distant matrix should work
union find
need to make k connection
validate the components

for part two keep going until we have one comonents
then chech the last two junctino boxes
'''

from collections import Counter
with open("puzzle.txt", "r") as file:
    lines = file.read().splitlines()

data = [list(map(int,l.split(","))) for l in lines]
nodes = len(data)

def dist(p1,p2):
    d_sq = 0
    for u,v in zip(p1,p2):
        d_sq += (u-v)**2
    return d_sq**.5

all_dists = []
n = len(data)
for i in range(n):
    for j in range(i+1,n):
        p1,p2 = data[i],data[j]
        d = dist(p1,p2)
        all_dists.append((d,i,j))

all_dists.sort(key = lambda x: x[0])

class DSU:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
        self.components = n          # initially every node is its own component
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_par = self.find(x)
        y_par = self.find(y)
        if x_par == y_par:
            return False
        
        # union by rank / size
        if self.rank[x_par] > self.rank[y_par]:
            self.rank[x_par] += self.rank[y_par]
            self.rank[y_par] = 0
            self.parent[y_par] = x_par
        else:
            self.rank[y_par] += self.rank[x_par]
            self.rank[x_par] = 0
            self.parent[x_par] = y_par
        
        self.components -= 1          # merged → component count decreases
        return True

    def count(self):
        return self.components
    
dsu = DSU(nodes)
for weight,u,v in all_dists:
    dsu.union(u,v)
    if dsu.count() == 1:
        p1,p2 = data[u],data[v]
        print(p1[0]*p2[0])
        break
