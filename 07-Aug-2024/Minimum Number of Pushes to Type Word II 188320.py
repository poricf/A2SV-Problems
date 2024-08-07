# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        cc = Counter(word)

        sor_char = sorted(cc.items(), key=lambda x: x[1], reverse=True)
        new_word = [sor_char[i][0] for i in range(len(sor_char))]
        # print(new_word)
        ans = 0
        for i in range(1,len(new_word)+1):
            ans += (ceil(i/8) * cc[new_word[i-1]])
        
        return ans
        
