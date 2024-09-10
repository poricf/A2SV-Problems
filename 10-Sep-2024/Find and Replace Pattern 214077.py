# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        dic = {}
        matched = set()
        
        for word in words:
            isValid = True

            for i in range(len(pattern)):
                w, p = word[i], pattern[i]

                if w in dic:
                    if dic[w] != p:
                        isValid = False
                        break
                elif p in matched:
                    isValid = False
                    break
                else: 
                    dic[w] = p
                    matched.add(p)

            if isValid: ans.append(word)
            
            dic.clear()
            matched.clear()

        return ans