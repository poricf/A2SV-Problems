class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        '''
        s = ( ( ( ) ) ( ) )

        for this 
        s = (3) = 6
        A = B + C = (()) + () =  2 + 1 = 3
        B = (D) = 2
        D = ()
------------------------------------------------------------------
     
        stack = [0,0,0]
            ** when close parenthesis comes then [0,0] score = 0 we will add 1 at the top 
                [0,1]
            ** stack = [0]  score = 1 so 2 * 1 will be added to top
            
                [2]
                [2,0]
                [2] score = 0
                [3]
                [] score = 3
                [6]
we will return 6

        '''
        st = [0] #initialize with 0

        for c in s:
            if c == '(':
                st.append(0)
            else:
                score = st.pop()

                if score == 0:
                    st[-1] += 1
                else:
                    st[-1] += (score*2)
        
        return st[0]

        '''
        TimeC & spaceC = O(n)
        '''