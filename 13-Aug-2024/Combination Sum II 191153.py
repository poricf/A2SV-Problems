# Problem: Combination Sum II - https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        candidates.sort()


        def findexCombination(index: int, target: int):
            if target == 0:
                ans.append(ds[:])
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                ds.append(candidates[i])
                findexCombination(i + 1, target - candidates[i])
                ds.pop()


        findexCombination(0, target)
        return ans