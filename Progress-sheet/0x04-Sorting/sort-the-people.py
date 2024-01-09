class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names) 
        for i in range(n):
            mx = heights[i]
            mxindex = i
            for j in range(i,n):
                if mx < heights[j]:
                    mx = heights[j]
                    mxindex = j
            
            heights[i],heights[mxindex] = heights[mxindex],heights[i]
            names[i],names[mxindex] = names[mxindex],names[i]

        return names