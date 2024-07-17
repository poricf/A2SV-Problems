# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = set()

        right = 0
        left = 0
        ans = 0
        while right < len(s):
            if s[right] in dic:
                while s[right] in dic:
                    dic.remove(s[left])
                    left += 1
            
            ans = max(ans, right - left + 1)
            dic.add(s[right])
            right += 1
                
        return ans
        