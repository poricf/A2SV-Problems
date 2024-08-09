# Problem: Sum of Subarray minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        left = [0] * n
        right = [0] * n

        stack = []
        for i in range(n):
            cnt = 1
            while stack and arr[i] < stack[-1][0]:
                a , j = stack.pop()
                cnt += j

            stack.append((arr[i],cnt))
            left[i] = cnt

        stack = []
        for i in range(n-1,-1,-1):
            cnt = 1
            while stack and arr[i] <= stack[-1][0]:
                a , j = stack.pop()
                cnt += j

            stack.append((arr[i],cnt))
            right[i] = cnt
        ans = 0
        for i in range(n):
            ans += left[i] * right[i] * arr[i]

        return ans % mod