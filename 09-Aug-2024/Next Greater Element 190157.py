# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * (10 ** 4 + 1)
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                res[stack.pop()] =  num
                
            stack.append(num)
        
        ans = []
        for num in nums1:
            ans.append(res[num])
        
        return ans