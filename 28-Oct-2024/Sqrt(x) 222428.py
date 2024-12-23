# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = (left + right) >> 1

            if mid * mid == x:
                return mid
            elif mid * mid < x:


                
                left = mid + 1
            else:
                right = mid - 1
            
        return left - 1