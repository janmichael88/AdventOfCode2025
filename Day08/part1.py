'''
generatting distant matrix should work
union find
need to make k connection
validate the components
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
    def __init__(self,n):
        #no pointers and no size initially
        self.rank = [1]*n
        self.parent = [i for i in range(n)]
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        x_par = self.find(x)
        y_par = self.find(y)
        if x_par == y_par:
            return False
        #try doing union
        if self.rank[x_par] > self.rank[y_par]:
            self.rank[x_par] += self.rank[y_par]
            self.rank[y_par] = 0
            self.parent[y_par] = x_par
        else:
            self.rank[y_par] += self.rank[x_par]
            self.rank[x_par] = 0
            self.parent[x_par] = y_par
        return True 
    
dsu = DSU(nodes)
for weight,u,v in all_dists[:1000]:
    dsu.union(u,v)

temp = sorted(dsu.rank)
print(sorted(dsu.rank))
print(temp[-1]*temp[-2]*temp[-3])