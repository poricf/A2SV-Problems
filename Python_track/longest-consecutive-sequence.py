class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        srt = sorted(list(set(nums)))
        out = 1
        mx = 1
        for i in range(1,len(srt)):
            if srt[i]-srt[i-1]==1 :
                mx+=1
                if mx>out:
                    out=mx
            else:
                mx = 1
        return out if nums else 0