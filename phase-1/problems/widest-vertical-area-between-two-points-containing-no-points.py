class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        num_sets = set()
        for i in range(len(points)):
            num_sets.add(points[i][0])
        lists = list(num_sets)
        lists.sort()
        ans = 0
        for i in range(1,len(lists)):
            ans = max(ans,lists[i]-lists[i-1])
        return ans