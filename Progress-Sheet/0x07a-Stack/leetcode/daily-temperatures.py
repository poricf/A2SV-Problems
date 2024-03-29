class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
       # BruteForce = searching for NextGreater Element in the array for each              element 
        t(n) = O(n)
        O(n) = O(1)
        
        # Optimized Solution = Monotonicaly decreasing stack 
        [73, 74,75,71,69,72,76,73]
        
        stack condition in each iteration
        ------------------------73(0)
        [73]           --->   [0]
        [0,0,0,0,0,0,0,0]
        -------------------74(1)
        [74]                  [1]
        [1,0,0,0,0,0,0,0]
        ---------------------75(2)
        [75] ---[2]
        [1,1,0,0,0,0,0,0]
        ----------------------71(3)
        [75,71]-----[2,3]               
        [1,1,0,0,0,0,0,0]
        ----------------------------69(4)
        [75,71,69]----[2,3,4]
        [1,1,0,0,0,0,0,0]
        ----------------------------72(5)
        [75,72]------[2,5]
        [1,1,0,2,1,0,0,0]
        ----------------------------- 76(6)
        [76]---------[6]
        [1,1,4,1,1,1,0,0]
        ----------------------------- 73(7)
        [76,73] ---[6,7]
        [1,1,4,1,1,1,0,0]
        ---------------------------------------------------end
        
        
        
        
        
        
        
        
        
        '''
        n = len(temperatures)
        
        res = [0] * n
        stack = [] #index of the temprature
        
        for index in range(len(temperatures)):
            while stack and temperatures[index] > temperatures[stack[-1]]:
                stack_ind = stack.pop()
                res[stack_ind] = index - stack_ind
            stack.append(index)
        return res
            