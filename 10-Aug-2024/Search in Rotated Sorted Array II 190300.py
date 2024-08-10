# Problem: Search in Rotated Sorted Array II - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        low,high=0,n-1
        while low<=high:
            mid=low+(high-low)//2
            if target==nums[mid]:
                return True
            if (nums[mid]==nums[low]) and (nums[mid]==nums[high]):
                low+=1
                high-=1
            elif nums[mid]>=nums[low]:
                if target>=nums[low] and target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if target<=nums[high] and target>=nums[mid]:
                    low=mid+1
                else:
                    high=mid-1
        return False


            
            