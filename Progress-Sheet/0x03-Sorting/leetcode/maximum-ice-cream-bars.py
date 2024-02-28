class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return sum(1 for icecream in sorted(costs) if (coins:= coins-icecream) >= 0)