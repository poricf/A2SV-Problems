'''
Apprach 1 swapping
'''
class Solution:
    ans = []
    def recurPermute(self, index: int, nums: List[int], ans: List[List[int]]):
        if index == len(nums):
            ans.append(nums[:])
            return
        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            self.recurPermute(index + 1, nums, ans)
            nums[index], nums[i] = nums[i], nums[index]


    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.recurPermute(0, nums, self.ans)
        return self.ans
'''
Pproach 2 using map
class Solution:
    
    ans = []
    ds = []

    def permute(self, nums: List[int]) -> List[List[int]]:

        self.ans = []
        self.ds = []
        freq = [0] * len(nums)
        self.recurPermute(nums, freq)
        return self.ans


    def recurPermute(self, nums: List[int], freq: List[int]):
        if len(self.ds) == len(nums):
            self.ans.append(self.ds.copy())
            return
        for i in range(len(nums)):
            if not freq[i]:
                self.ds.append(nums[i])
                freq[i] = 1
                self.recurPermute(nums, freq)
                freq[i] = 0
                self.ds.pop()


        
'''