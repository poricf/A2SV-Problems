# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def prime_factors(n):
            factors = defaultdict(int)
            while n % 2 == 0:
                factors[2] += 1
                n //= 2
            sqrt_n = math.isqrt(n)
            for i in range(3, sqrt_n + 1, 2):
                while n % i == 0:
                    factors[i] += 1
                    n //= i
            if n > 2:
                factors[n] += 1
            return factors
        ans = set()
        for num in nums:
            fac = prime_factors(num)
            # print(fac)
            for a in fac.keys():
                ans.add(a)
        # print(ans)
        return len(ans)
