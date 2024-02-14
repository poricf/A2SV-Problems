class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt = 0
        vowels = "aeiou"
        ans = 0
        l = 0
        for r in range(len(s)):
            if s[r] in vowels: cnt += 1  

            if r - l + 1 > k:
                if s[l] in vowels: cnt -= 1 
                l += 1
            
            ans = max(cnt, ans)
        return ans            
            
