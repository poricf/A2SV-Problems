# Problem: Minimum Size Subarray in Infinite Array - https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums += nums
        pref = [0] * (2*n + 1)
        for i in range(1,2*n+1):
            pref[i] = nums[i-1] + pref[i-1]
        
        tar = target % pref[n]
        val = target // pref[n]

        mp = defaultdict(int)

        for i in range(1,2*n+1):
            mp[pref[i]] = i
        ans = float("inf")
        for right in range(1,2*n+1):
            cur = pref[right]
            need = pref[right] - tar
            if need in mp:
                left = mp[need]
                ans = min(ans,right - left)
        if ans == float("inf"):
            return -1
        res = ans + (val * n)

        return res