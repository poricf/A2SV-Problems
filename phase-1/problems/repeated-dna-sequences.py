class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        answer = set()
        k = 10
        count = defaultdict(int)
        left = 0
        for right in range(len(s)):
            if right - left + 1 == k:
                count[s[left:right+1]]+= 1
                if count[s[left:right+1]] > 1:
                    answer.add(s[left:right+1])
                left += 1
        return list(answer)
        

