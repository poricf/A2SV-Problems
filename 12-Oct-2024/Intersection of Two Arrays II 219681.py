# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        co = Counter(nums1)
        co2 = Counter(nums2)
        k = set(nums1)&set(nums2)
        res = []
        for num in list(k):
            res.extend([num]*min(co[num],co2[num]))
        return res
        