class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        n = len(citations)
        right = n - 1

        while left <= right:
            mid = (left + right ) >> 1

            if citations[mid] == n - mid :
                return n - mid
            elif citations[mid] < n - mid:
                left = mid + 1
            else:
                right = mid - 1
        
        return n -  left