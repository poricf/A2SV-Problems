class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        '''
        Author - Fahmi Dinsefa 
        Date - 1/26/2024
        Time C - O(n)
        space C - O(1)
        Concept - Prefix Sum
        '''
        currS = 0

        n = len(s)
        arr = [0]*(n+1)
        for shift in shifts:
            start,end,direction = shift
            if direction == 0:
                arr[start] -= 1   
                arr[end + 1] += 1
            else:
                arr[start] += 1   
                arr[end + 1] -= 1                
            
        pref = list(accumulate(arr))
        ans = []
        print(pref)
        for i, c in enumerate(s):
            curS = pref[i]
            now = (ord(s[i]) + curS)
            now -=  97
            now %= 26
            now += 97
            print(now)
            ans.append(chr(now))

        return "".join(ans)



