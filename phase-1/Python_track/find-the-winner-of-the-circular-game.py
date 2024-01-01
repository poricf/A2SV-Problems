class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        index = 0
        arr = [0]*n
        for i in range(1,n+1):
            arr[i-1] = i 

        print(arr)

        while(len(arr) > 1):
            index += (k - 1)
            index = index % len(arr)
            
            arr.pop(index % len(arr))
        
        return arr[0]

        


