class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ = defaultdict(int)
        n = len(s)
        for i in range(n):
            last_occ[s[i]] = i
        ans = []
        left = 0
        right = 0
        
        temp = 0
        while right < n and left < n:
            right = max(last_occ[s[left]],right)
            if left == right:
                ans.append(right - temp + 1) 
                temp = left + 1
            left += 1
            

        return ans
            
