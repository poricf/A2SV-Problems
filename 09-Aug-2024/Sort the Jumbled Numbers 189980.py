# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d = {}
        
        for i in nums:
            b = str(i)
            c = "".join(str(mapping[int(digit)]) for digit in b)
            t = int(c)
            if t in d:
                d[t].append(i)
            else:
                d[t] = [i]
        
        d = dict(sorted(d.items(), key=lambda x: x[0]))
        
        m = []
        for i in d.values():
            m.extend(i)
        
        print(m)
        return m