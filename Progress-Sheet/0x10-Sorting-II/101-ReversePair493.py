from bisect import bisect_right

class Solution:
    def reversePairs(self, nums):
        self.ans = 0
        sorted_nums = self.mergeSort(nums)
        return self.ans

    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        sorted_left = self.mergeSort(left)
        sorted_right = self.mergeSort(right)

        return self.merge(sorted_left, sorted_right)

    def merge(self, left, right):
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                ind = bisect_right(left, right[j] * 2)
                if ind < len(left):
                    self.ans += len(left) - ind
                j += 1

        merged.extend(left[i:])

        while j < len(right):
            ind = bisect_right(left, right[j] * 2)
            if ind < len(left):
                self.ans += len(left) - ind
            merged.append(right[j])
            j += 1

        return merged


def main():
    nums = [int(x) for x in input().split()]
    solution = Solution()
    ans = solution.reversePairs(nums)
    print(ans)

t = int(input())
for i in range(t):
    main()