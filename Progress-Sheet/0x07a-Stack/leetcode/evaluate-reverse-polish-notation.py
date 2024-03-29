class Solution:
    def isoperator(self,s):
        return s in ["+","-","/","*"]
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for c in tokens:
            if self.isoperator(c):
                x = st.pop()
                y = st.pop()

                if c == '+':
                    st.append(x+y)
                elif c == '-':
                    st.append(y-x)
                elif c == '/':
                    st.append(int(y/x))
                else:
                    st.append(y*x)
            else:
                st.append(int(c))
    
        return st[-1]