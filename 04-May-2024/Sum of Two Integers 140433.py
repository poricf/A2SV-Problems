# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def subtract(self,x, y):
        diff =  x ^ y
        borrow = (~x & y) << 1
        if (y == 0):
            return x
        return self.subtract(diff,borrow)
        
    def add(self,a, b):
        if b == 0:
            return a
        else:
            s = a ^ b
            carry = (a & b) << 1
            return self.add(s, carry)

    def getSum(self, a: int, b: int) -> int:

        if (a >= 0 and b >= 0 ) | (a < 0 and b < 0) | (a < 0 and -a > b) | (b < 0 and -b > a) :
            return self.add(a,b)
        else:
            if a < 0:
                return self.subtract(b,-a)
            else:
                return self.subtract(a,-b)
