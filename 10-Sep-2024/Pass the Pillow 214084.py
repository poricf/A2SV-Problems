# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        a = time // (n - 1)
        b = time % (n - 1)
        return n - b if a & 1 else b + 1