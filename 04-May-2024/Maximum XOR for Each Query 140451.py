# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]: 
        n = len(nums)
        def toggle(x, i,z):
            for i in range(z):
                x = ((1 << i) ^ x)
            return x
        ans = 0
        result = []
        for num in nums:
            ans ^= num
        print(ans)
        
        for i in range(n-1,-1,-1):
            
            init = toggle(ans,i,maximumBit)
            result.append(init)
            ans ^= nums[i]
        
        return result
