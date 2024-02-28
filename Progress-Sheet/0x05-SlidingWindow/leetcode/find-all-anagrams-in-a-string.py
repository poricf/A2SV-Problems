class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        ans = []
        window = [0]*128
        sample = [0]*128

        for i in p:
            sample[ord(i)] += 1
        
        right = 0
        left = 0
        while(right < len(s)):
            window[ord(s[right])] += 1
            if(right - left+ 1 == k):
                if(window == sample):
                    ans.append(left)
                window[ord(s[left])]-=1
                left+=1
            right+=1
        return ans
            
        

