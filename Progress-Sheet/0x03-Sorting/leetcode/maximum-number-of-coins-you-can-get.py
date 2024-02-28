class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)

        ans = 0
        print(piles)
        i = 1
        m = len(piles)//3
        k = 0
        while i < len(piles) and k != m:
            ans += piles[i]
            i+=2
            k+=1
                
        return ans