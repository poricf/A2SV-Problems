class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        cnt = 0
       
        
        ans = float("inf")
        for r in range(len(blocks)):
            if blocks[r] == 'W': cnt += 1
            if r - l + 1 == k:
                ans = min(ans , cnt)
                if blocks[l] == 'W': cnt -= 1
                l += 1
        return ans
            
