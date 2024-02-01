class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        dic = {}
        notin = []
        res = []

        for i in arr1 :
            if i not in arr2 :
                notin.append(i)
            elif i in dic :
                dic[i] += 1
            else :
                dic[i] = 1

        for j in arr2 :
            res = res + [j]*dic[j]
            
        return res + sorted(notin)
		
		