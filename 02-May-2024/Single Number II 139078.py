# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        def setith(x,i):
            x = (1 << i) | x

            return x
        def checkset(x,i):
            if (1 <<  i) & x:
                return True
            return False
        
        def clearith(x,i):
            x =(~(1 << i)) & x
            return x
        def toggleith(x,i):
            x = (1 << i) ^ x
            return x
        ans = 0
        for bitind in range(32):
            cnt = 0
            for num in nums:
                if checkset(num,bitind):
                    cnt += 1
            
            if cnt % 3 == 1:
                ans = setith(ans,bitind)
        
        if ans & (1 << 31):
            ans = ans - (1 << 32)
        
        return ans

