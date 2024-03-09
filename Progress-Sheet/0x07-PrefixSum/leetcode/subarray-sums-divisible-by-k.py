
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainders = Counter(map(lambda x: x % k, accumulate(nums)))        
        ans = 0
        for r in remainders:
            # combinations of prefixes have same remainer mod k
            ans += remainders[r] * (remainders[r]-1) // 2
        ans += remainders[0]
        return ans