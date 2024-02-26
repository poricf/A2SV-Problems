class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        maker = [weights[i] + weights[i+1] for i in range(n-1)]
        maker.sort(reverse = True)
        print(maker)
        return sum(maker[:k-1]) - sum(maker[n-k:])

        