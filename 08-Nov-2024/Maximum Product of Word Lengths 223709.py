# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0

        def setbit(word):
            mask = 0
            for c in word:
                mask |= 1 << ord(c) - ord('a')
            return mask

        masks = [setbit(word) for word in words]

        for i in range(len(words)):
            for j in range(i):
                if not (masks[i] & masks[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans