class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        N,M = len(matrix),len(matrix[0])
        p_sum = [[0 for _ in range(M+1)] for _ in range(N+1)]
        for r in range(N):
            for cl in range(M):
                above = p_sum[r][cl+1]
                behind = p_sum[r+1][cl]
                top_right = p_sum[r][cl]
                p_sum[r+1][cl+1] += above + behind - top_right + matrix[r][cl]
        ans  =0 
        for r1 in range(1,N+1):
            for r2 in range(r1,N+1):
                freq = defaultdict(int)
                freq[0] += 1
                for cl in range(1,M+1):
                    current = p_sum[r2][cl] - p_sum[r1-1][cl]-target
                    ans += freq[current]
                    freq[p_sum[r2][cl] - p_sum[r1-1][cl]] += 1
        return ans