# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        visited = set([''])
        ans = ''
        for i in range(len(words)):
            wrdd = words[i][:-1]
            word = words[i]
            if wrdd in visited:
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word 
                visited.add(word)
        return ans