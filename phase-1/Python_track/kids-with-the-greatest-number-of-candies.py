class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        maxcandy = max(candies)
        for kidcandy in candies:
            print (kidcandy +  extraCandies)
            answer.append(kidcandy + extraCandies >= maxcandy)
        
        return answer
