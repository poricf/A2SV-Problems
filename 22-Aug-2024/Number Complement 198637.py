# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        k = num.bit_length()
        ans = num ^ (2**k - 1)
        
        return ans