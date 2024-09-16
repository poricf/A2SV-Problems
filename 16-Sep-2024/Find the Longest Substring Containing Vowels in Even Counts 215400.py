# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

        for c in s:
            if c in 'aeiou':
                vowels[c] += 1

        for i in range(len(s), 0, -1):
            if n - i > 0 and s[i] in 'aeiou':
                vowels[s[i]] -= 1
            
            if all((value % 2 == 0 or value == 0) for value in vowels.values()):
                return i

            vowels_copy = vowels.copy()

            for j in range(1, len(s) - i + 1):
                if s[j - 1] in 'aeiou':
                    vowels_copy[s[j - 1]] -= 1
                if s[j + i - 1] in 'aeiou':
                    vowels_copy[s[j + i - 1]] += 1

                if all((value % 2 == 0 or value == 0) for value in vowels_copy.values()):
                    return i

        return 0