class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(mid):
            calculated_sum = 0
            for num in nums:
                # print(mid,(math.ceil(num/mid)))
                calculated_sum += math.ceil(num/mid)
            # print(calculated_sum)
            if calculated_sum <= threshold:
                return True
            return False

        left = 1
        right = max(nums)

        while left <  right:
            mid = (left + right ) >> 1

            if check(mid):
                right = mid
            else:
                left = mid + 1
            
        return left