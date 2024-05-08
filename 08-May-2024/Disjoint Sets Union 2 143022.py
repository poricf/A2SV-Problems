# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

class UnionFind:
  def __init__(self, size):
    self.root = [i for i in range(size)]
    self.size = [1] * size
    self._min = [i for i in range(size)]
    self._max = [i for i in range(size)]

  def find(self, x):
    while x != self.root[x]:
      x = self.root[x]
    return x
    
  def union(self, x, y):
    rootX = self.find(x)
    rootY = self.find(y)
    if rootX != rootY:
      if self.size[rootX] > self.size[rootY]:
        self.root[rootY] = rootX
        self.size[rootX] += self.size[rootY]
        self._min[rootX] = min(self._min[rootY], self._min[rootX])
        self._max[rootX] = max(self._max[rootY], self._max[rootX])
      else:
        self.root[rootX] = rootY
        self.size[rootY] += self.size[rootX]
        self._min[rootY] = min(self._min[rootY], self._min[rootX])
        self._max[rootY] = max(self._max[rootY], self._max[rootX])


n, m = map(int, input().split())
uf = UnionFind(n+1)


for i in range(m):
  s = input().split()
  if len(s) == 3:
    q, x, y = s[0], int(s[1]), int(s[2])
    uf.union(x, y)
  else:
    q, x =  s[0], int(s[1])
    p = uf.find(x)
    print(uf._min[p], uf._max[p], uf.size[p])

