class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        BruteForce = search for next greater element for each num on 
        nums2 in a mapping ds since all are unique
        then for each value that apears in num1 then go search in result map for 
        the mapped value of the element our result map will be {n2elem,nextgreater}s
        it is not optimized 
        t(n) - O(n^2)
        s(n) - O(n)
       
        OptimizedSolution = Monotonic Decreasing Stack
        idea = use monotonically decreasing stack 

        step 1 - iterate over nums2
        stack = []
        mapping = {{1,-1}, (3,-1), (4,-1), (2,-1)}
        result = []
        ----------------------1(0)
        stack = [1]
        ----------------------3(2)
        stack = [3]
        mapping = {(1,3).....}
        -----------------------4(3)
        stack = [4] 
        mapping = {(1,3), (3,4)...}
        -------------------------2(1)
        stack = [4,2]
        mapping = {(1,3), (3,4)...}



        '''

        mapping = {elem: -1 for elem in nums2}
        result = []
        stack = []

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:       
                mapping[stack[-1]] = nums2[i]           
                stack.pop()                             
            stack.append(nums2[i])                   
       
        
        for i in range(len(nums1)):
            result.append(mapping[nums1[i]])
        return result


            