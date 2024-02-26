class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Initializing the ans and stack 
        n = len(nums)
        result = [-1] * n
        st = []
        # Traversing through the array by 2n-1 as we are using an imaginary 
        # array of size n and as the array is circular we can traverse in reversibly also
        # It will not affect the ans
        for i in range(2*n-1,-1,-1):
            # Using while loop to remove the element which are less than the element 
            # we are traversing at in the stack
            # using index as that because this is a circular array
            while st and st[-1] <= nums[i%n]:
                st.pop()
            # When we are before the end of the nums if stack exist then add the 
            # top value of the stack to the result array as this will be the nge
            if (i <n):
                if st:
                    result[i] = st[-1]
            # else append the value in the stack as the stack is in increaing order
            # no element is smaller than the visiting element in the stack
            st.append(nums[i%n])
        return result

        