# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution:
    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        def check(x):
            a = x - (x//divisor1) >= uniqueCnt1
            b = x - (x//divisor2) >= uniqueCnt2
            c = x - (x//lcm(divisor1,divisor2)) >= uniqueCnt1 + uniqueCnt2
            return a and b and c

        low, high = 1, 10**10 

        while low <= high:
            mid = (low+high)//2 

            if check(mid):
                high = mid-1 
            else:
                low = mid+1 

        return low 