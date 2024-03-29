class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        '''
        idea of the problem:
        3,1,2,4
        subarrays are size 1) 3,1,2,4   minimums = 3+1+2+4
                      size 2) 3,1} 1,2} 2,4} minimum = 1 + 1 + 2
                      size 3}  3,1,4}  1,2,4} minumum = 1 + 1
                      size 4} 3,1,2,4}  minumum = 1
                      total = 3+1+2+4+1+1+2+1+1+1 = 17
        
        BruteForce - conisder all subbaraays using nested loop take the minimum and add them in a variable called sm this is the intutitive approach to solve the problem but it takes O(n^2)  this not the efficent way to solve this problem ... then what is the efficent way to solve
         3 is minimum for 1 window
         1 is minimum for  5 windows
         2 is minumum for 2 windows
         4 is minumum for 1 window
         
    from the above demonestration we can say the solution to the problem is to
    find sum(A[i] * f(i)), where f(i) is the number of subarrays in which A[i] is the minimum.
    
    But the Big question is how to find f(i) 
       In order to find f[i], we need to find out 2 things : 
        left[i], the length of strictly larger numbers on the left of A[i], 
        right[i], the length of larger numbers on the right of A[i].
        including it self
        
        FOR Example for 1 in the above (from left)  there is 1,3 and from right there are 
        1,2,4  so left[1] = 2 ... right[1] = 3  so total of 1 taht it ll be minimum is 
        3 * 2 = 6
        
        to se the solution we will use monotonically decreasing stack to keep track of the elements greater than a[i] in the array by holfing pair value of (value,cnt)
        lets simulate the idea in step by step for the first testcaase
        
        [3,1,2,4]
        **********************************************************************
        step 1:
        build left array means number of elements greater on the left including itself
        iterate from start to end on arr
        left = [0,0,0,0]
        s1 = []
        
        ----------------------------(3)
        left = [1,0,0,0]
        s1 = [(3,1)]
        -----------------------------(1) it is less that means pop the stack and count 
                                     the number of count element at the top o fthe stack has
        left = [1,2,0,0]
        s1 = [(1,1)]
        -----------------------------(2) it is greater just push
        left = [1,2,1,0]
        s1 = [(1,1), (2,1)]
        -------------------------------(4) it is greater just push
        left = [1,2,1,1]
        s1 = [(1,1), (2,1)]
        
        *****************************************************************************
        step2 2:
        build right array number of elements from the right that are greater
        
        right = [0,0,0,0]
        s2 = []
        
        ----------------------------------4
        right = [0,0,0,1]
        s2 = [(4,1)]
        ---------------------------------2
        right = [0,0,2,1]
        s2 = [(2,2)]
        --------------------------------- 1
        right = [0,3,2,1]
        s2 = [(1,3)]
        ----------------------------------3 
        right = [1,3,2,1]
        s2 = [(1,3) and (3,1)]
        
        
        *********************************************************************************
        
        step 3 now whe have built left and right so now we shoud multiply and add
        right = [1,3,2,1]
        left = [1,2,1,1]
        nums = [3,1,2,4]
        
        ans = 1*1*3 + 3*2*1 + 2*1*2 + 1*1*4  = 3 + 6 + 4 + 4 = 17
        
        '''
        
        #initialize left and right array
        n = len(arr)
        left , right = [0] * n, [0] * n
        s1 , s2 = [],[]
        
        # build left array using MD.stack
        i = 0
        for elem in arr:
            cnt = 1
            while s1 and elem < s1[-1][0]:
                cnt +=  s1[-1][1]
                s1.pop()
            s1.append([elem, cnt])
            left[i] = cnt
            i+=1

        
        # build right array using MD.stack
        j = n-1
        for elem in (reversed(arr)):
            cnt = 1
            while s2 and elem <= s2[-1][0]:
                cnt +=  s2[-1][1]
                s2.pop()
            s2.append([elem, cnt])
            right[j] = cnt 
            j -= 1
            
        #calculate the result A[i](f[i])  f = l*r
        ans = 0  
        for k in range(len(arr)):
            ans += (left[k]*right[k]*arr[k])
        return ans % MOD
            
        
        
        