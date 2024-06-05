# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        res = []
    
        for let in alpha:
            ans = float("inf")
            cnt = 0
            for word in words:
                if let in word:
                    cnt += 1
                    ans = min(ans,word.count(let))
            if cnt == len(words):
                res += [let for i in range(ans)]
        
        return res


