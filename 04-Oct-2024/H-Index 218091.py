# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        def check(h):
            ind = bisect_left(citations,h)
            return (n-ind) >=h 
        
        l = 0
        r = n
        ans = float("-inf")
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans=max(ans,mid)
                l = mid +  1
            else:
                r = mid - 1
        
        return ans

             
            