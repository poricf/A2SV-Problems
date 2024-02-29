class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        words = ''.join(word1)
        wordss = ''.join(word2)
        
        return words == wordss
