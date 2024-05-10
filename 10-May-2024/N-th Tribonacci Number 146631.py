# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

cache = {0: 0, 1: 1 , 2 : 1}
class Solution:
    
    def tribonacci(self, n: int) -> int:
        if n in cache:
            return cache[n]
        cache[n] = self.tribonacci(n-2) + self.tribonacci(n-3) + self.tribonacci(n-1)     

        return cache[n]