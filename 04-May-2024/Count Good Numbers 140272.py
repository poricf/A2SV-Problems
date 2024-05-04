# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        '''Intution: 
        --------------------------------------------------------------------------
        lets say  n = 3
        then there are 3 digits right 2 of them are even indices(0&2) and 1 of it is odd(1th indice):
        - in the even indices there has to be only even number  and the same fot the odd
            we have 5 choices for even (2,4,6,8,0)
            we have 4 choices for odd (1,3,5,7)
        so in 0th and 2th indices we have 5 choices which is 5^2 = 25
        in the 1th index we have 4 choice which is 4^1 = 4

        total 25*4 = 100
        ----------------------------------------------------------
        eg 2
        n = 4;
        even  5^2 = 25
        odd 4^2 = 16
        total  = 25*16= 400

        two cases are there then 
        if n is even then the answer is 
        5^(n/2)  *  4^(n/2)
        if n is odd 
        5^(n/2) * 5  * 4^(n/2)
        '''
        def mypow(base, exponent):
            result = 1
            base = base % MOD

            while exponent > 0:
                if exponent % 2 == 1:
                    result = (result * base) % MOD
                exponent = exponent // 2
                base = (base * base) % MOD

            return result
        if n % 2:
            ans = mypow(5,n//2) * 5 * mypow(4,n//2)
        else:  
            ans = mypow(5,n//2) * mypow(4,n//2)

        return ans % MOD
