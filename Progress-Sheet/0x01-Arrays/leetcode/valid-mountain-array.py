class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if sorted(arr) == arr:
            return False
        if sorted(arr,reverse = True) == arr:
            return False
        i = 0
        j = len(arr) - 1
        n = len(arr) 
        while i  < n - 1 and arr[i] < arr[i + 1]: 
            i += 1
        while j > 0 and arr[j - 1] > arr[j]: 
            j -= 1
        return i == j