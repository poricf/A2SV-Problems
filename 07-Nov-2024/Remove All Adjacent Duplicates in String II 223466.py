# Problem: Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        last = defaultdict(list)
        st = []
        for c in s:
            if st and st[-1] == c and last[c] and len(st) - last[c][-1] == k - 1:
                last[c].pop()
                while st and st[-1] == c:
                    st.pop()
            
            else:
                if not st or st[-1] != c:
                    last[c].append(len(st))
            
                st.append(c)
        
        return "".join(st)