class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curSum = sum(nums[:k])
        left = 0
        right = k
        maxSum = curSum
        # print(curSum)
        while(right < n):

            curSum += nums[right]
            curSum -= nums[left]
            left += 1
            right += 1

            maxSum = max(maxSum,curSum)
            # print(maxSum)
        return maxSum/k

