# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        def rightmostset(n):
            return (n & n - 1) ^ n
        xor = 0
        for num in nums: 
            xor ^= num

        x = rightmostset(xor)
        b1 , b2 = 0 , 0
        for num in nums:
            if num & x:
                b1 ^= num
            else:
                b2 ^= num
        
        return [b1,b2]
            