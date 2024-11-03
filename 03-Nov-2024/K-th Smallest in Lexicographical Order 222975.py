# Problem: K-th Smallest in Lexicographical Order - https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(prefix, n):
            steps = 0
            first = prefix
            last = prefix + 1
            while first <= n:
                steps += min(last, n + 1) - first
                first *= 10
                last *= 10
            return steps

        current = 1
        k -= 1
        while k > 0:
            steps = count_steps(current, n)
            if steps <= k:
                current += 1
                k -= steps
            else:
                current *= 10
                k -= 1
        
        return current

