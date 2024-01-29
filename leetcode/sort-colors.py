class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)

        count = Counter(nums)
        cur = min(nums)
        for holder in range(n):
            seeker = holder
            while(seeker < n and nums[seeker] != cur):
                seeker += 1
            if seeker < n:
                nums[holder],nums[seeker] = nums[seeker],nums[holder]
            if holder + 1 - count[nums[holder]]  == 0 and  holder < count[0]:
                cur += 1



        """
        Do not return anything, modify nums in-place instead.
        """
        