# Problem: Longest Increasing Subsequence II - https://leetcode.com/problems/longest-increasing-subsequence-ii/description/

class SegmentTree:
    def __init__(self, data, default=0, func=max):
        self.default = default
        self.func = func
        self.n = len(data)
        
        # Build the segment tree with an appropriate size (2*n for a complete tree)
        self.tree = [default] * (4 * self.n)
        
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        
        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = func(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index, value):
        """Update the element at index to value and update the segment tree accordingly."""
        index += self.n
        self.tree[index] = value
        
        # Update parents
        while index > 1:
            index //= 2
            self.tree[index] = self.func(self.tree[2 * index], self.tree[2 * index + 1])

    def query(self, left, right):
        """Query the function (e.g., sum or max) over the interval [left, right)."""
        left += self.n
        right += self.n
        
        res = self.default
        while left < right:
            if left % 2 == 1:
                res = self.func(res, self.tree[left])
                left += 1
            if right % 2 == 1:
                right -= 1
                res = self.func(res, self.tree[right])
            left //= 2
            right //= 2
        
        return res

    def __getitem__(self, index):
        """Retrieve element at index."""
        return self.tree[self.n + index]

    def __setitem__(self, index, value):
        """Set element at index to a new value."""
        self.update(index, value)

    def __delitem__(self, index):
        """Delete element at index (set to default)."""
        self.update(index, self.default)

    def __repr__(self):
        return f"SegmentTree({self.tree[self.n:]})"


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        n = len(nums)
        tree = SegmentTree([0] * (mx + k) , default=0 , func= max)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1 , -1):
            val = nums[i]
            l = val + 1
            r = val + k
            res = tree.query(l,r+1)
            dp[i] = res + 1
            tree.update(val,res+1)
        
        return max(dp)
