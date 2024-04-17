# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []
        for num in arr:
            diff = abs(num - x)

            if len(max_heap) < k:
                heappush(max_heap,(-diff,num))
            
            else:
                if -max_heap[0][0] <= diff :
                    if num > max_heap[0][1]:
                        continue

                heapreplace(max_heap,(-diff,num))

        
        result= []
        for d,val in max_heap:
            result.append(val) 
                        
        return sorted(result)

            

