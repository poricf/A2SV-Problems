class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic=Counter(s)
        ans=0
        oddValue=0
        for k,v in dic.items():
            if v %2 ==0:
                ans+=v
            else:
                ans+=v-1
                oddValue=1
        return (ans+oddValue)