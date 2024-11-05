# Problem: Greatest Common Divisor of Strings - https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        n = len(str1)
        m = len(str2)
        G = gcd(n , m)
        return str1[:G]