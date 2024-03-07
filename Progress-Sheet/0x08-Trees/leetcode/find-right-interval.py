from typing import List
from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = []
        startToIndex = {}

        for i, interval in enumerate(intervals):
            startToIndex[interval[0]] = i

        for interval in intervals:
            ind = bisect_left(sorted(startToIndex.keys()), interval[1])
            if ind == len(startToIndex):
                ans.append(-1)
            else:
                ans.append(startToIndex[sorted(startToIndex.keys())[ind]])

        return ans