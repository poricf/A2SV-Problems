class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        hash_t = Counter(t)
        hash_s = defaultdict(int)

        left,start_ind,minLen = 0,0,float('inf')
        count = 0

        for right,c in enumerate(s):
            hash_s[c] += 1

            if hash_s[c] <= hash_t[c]:
                count += 1

            if count == len(t):
                #minimize the window by removing trfochun and 
                #yelelutn
                while hash_s[s[left]] > hash_t[s[left]] or hash_t[s[left]] == 0:
                    if hash_s[s[left]] > hash_t[s[left]]:
                        hash_s[s[left]] -= 1
                    left += 1
                
                window_len = right - left + 1
                if minLen > window_len:
                    minLen = window_len
                    start_ind = left
        
        if start_ind == -1 or  minLen == float("inf"):
            return ""
        print(start_ind,minLen)
        
        return s[start_ind:start_ind + minLen]

        