# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        lst = []
        cost = 0
        MOD = 10 ** 9 + 7
        for i, instruction in enumerate(instructions):
            right = bisect.bisect(lst, instruction)
            left = bisect.bisect_left(lst, instruction)
            cost += min(i - right, left)
            lst.insert(right, instruction)
        return cost % MOD 

        