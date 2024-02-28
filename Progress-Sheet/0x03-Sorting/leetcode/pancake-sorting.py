class Solution:
    def __init__(self):
        self.result = []
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return self.result
        max_index = arr.index(max(arr))
        left = arr[:max_index+1]
        left.reverse()
        self.result.append(max_index+1)

        arr[:max_index+1] = left
        arr.reverse()
        self.result.append(len(arr))
        
        self.pancakeSort(arr[:-1])

        return self.result
        