class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        a=[max(i) for i in grid]
        b=[]
        l=len(grid)
        for i in range(l):
          
            c=max([j[i] for j in grid])
            b.append(c)
        ans=0
        for i in range(l):
            for j in range(l):
        
                ans+=min(a[i],b[j])-grid[i][j]
        return ans