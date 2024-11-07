# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M = len(nums2)
        ans = 0
        if N % 2:
            for num in nums2:
                ans ^= num
        
        if M % 2:
            for num in nums1:
                ans ^= num
        
        return ans