# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1
        m = n // 3
        rem = n % 3
        if n == 3:
            return 2
        if rem == 0:
            return 3 ** (m)
        elif rem == 1:
            res = 3 ** (m - 1)
            sub = 3 * (m-1)
        else:
            res = 3 ** (m)
            sub = 3 * (m)
        print(n)
        n -= sub
        print(rem,m,res,n)
        
        return res * n
        