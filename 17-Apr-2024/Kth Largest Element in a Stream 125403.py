# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapify(nums)

        while len(nums) > self.k:
            heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heappush(self.nums,val)
        
        else:
            if self.nums[0] < val:
                heapreplace(self.nums,val)
        
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)