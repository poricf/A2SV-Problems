class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
                          []
     
        /              |         |         \
       [1]           [2]         [3]       [4]
    /      \       /     \     /     \
 [1,2]    [1,3]  [1,4]  [2,3] [2,4]  [3,4]
   |         |       |     |        |
 [1,2,3]   [1,2,4] [1,3,4]  [2,3,4]..... 
                                   

        '''
        res = []

        def backtrack(start,combination):
            if len(combination) == k:
                res.append(combination[:])
                return
            
            for i in range(start, n + 1):
                combination.append(i)
                backtrack(i + 1,combination)
                combination.pop()
                # backtrack(i + 1,combination)
        backtrack(1,[])

        return res