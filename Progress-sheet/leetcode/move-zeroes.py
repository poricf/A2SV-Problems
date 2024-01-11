class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        i = 0 # place_holder
        j = 0 #seeker
        while (j < n):

            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                
            j+=1



            