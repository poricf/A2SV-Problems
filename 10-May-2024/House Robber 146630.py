# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        store = Counter()
        def fn(i):
            if i == n - 1:
                return nums[i]
            if i >= n:
                return 0
            
            res = float("-inf")

            for j in range(2,4):
                if i + j not in store:
                    store[i+j] = fn(i+j)
                
                res = max(store[i+j],res)

            return res + nums[i]        

    

        return max(fn(0),fn(1)) if n > 1 else fn(0)