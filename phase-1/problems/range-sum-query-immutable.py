class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = nums 
        n = len(nums)-1
        for i in range(n):
            self.preSum[i+1] += self.preSum[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0: 
            return self.preSum[right]
        return self.preSum[right] - self.preSum[left-1]