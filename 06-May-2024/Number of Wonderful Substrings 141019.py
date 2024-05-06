# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        lst = [ord(i) - ord('a') for i in word]
        freq = defaultdict(int)
        freq[0] = 1
        ans = 0
        pref = 0
        for num in lst: 
            pref ^= (1 <<num)
            ans += freq[pref]

            for i in range(10):
                target = 1 << i
                ans += freq[pref ^ target]
                
            freq[pref] += 1
            
        return ans 