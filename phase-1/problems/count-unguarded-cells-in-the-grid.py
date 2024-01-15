class Solution:
    vis = 0
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        visited = [[(0,0)] * (n+2) for _ in range(m+2)]
        for row, col in walls:
            visited[row+1][col+1] = (-1,-1)
        for row, col in guards:
            visited[row+1][col+1] = (1,1)

        for row in range(1,m+1):
            for col in range(1,n+1):
                if visited[row][col] == (-1,-1):
                    continue
                else:
                    if visited[row-1][col][0] == 1:
                        visited[row][col] = (1,visited[row][col][1])
                    if visited[row][col-1][1] == 1:
                        visited[row][col] = (visited[row][col][0],1)
        _sum = 0
        for row in range(m,0,-1):
            for col in range(n,0,-1):
                # print(row,col)
                if visited[row][col] == (-1,-1):
                    continue
                else:
                    if visited[row+1][col][0] == 1:
                        visited[row][col] = (1,visited[row][col][1])
                    if visited[row][col+1][1] == 1:
                        visited[row][col] = (visited[row][col][0], 1)
                if sum(visited[row][col]) == 0:
                    _sum += 1
        return _sum