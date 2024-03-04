class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(curIndex,father):
            if len(s) == curIndex:
                return True
            for f in range(curIndex,len(s)):
                curVal = int(s[curIndex:f+1])

                if father - 1 == curVal and backtrack(f+1,curVal):
                    return True
            return False            

        for i in range(len(s)-1):
            sub = s[:i+1]
            val = int(sub)
            if backtrack(i+1,val):
                 return True

        return False