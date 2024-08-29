# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        i = 1
        while i <= n:
            if n % i == 0:
                count += 1
            if count == k:
                return i
            i += 1
        
        return -1
