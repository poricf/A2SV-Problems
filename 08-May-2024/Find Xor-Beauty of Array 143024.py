# Problem: Find Xor-Beauty of Array - https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        def XOR(arr):
            x = 0
            for num in arr:
                x ^= num
            return x
        return XOR(nums)