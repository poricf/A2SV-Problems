class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed = list(zip(*matrix))
        return transposed