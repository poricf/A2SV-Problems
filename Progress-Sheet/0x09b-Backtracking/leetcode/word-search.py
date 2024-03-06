class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    ROWS = len(board)
    COLS = len(board[0])
    path = set()
    def dfs(r, c, i):
      if r < 0 or  r== ROWS or c < 0 or c == COLS:
        return False
      if board[r][c] != word[i] or (r,c) in path:
        return False
      if i == len(word)-1:
        return True

      
      path.add((r,c))
      isExist = \
          dfs(r + 1, c, i + 1) or \
          dfs(r - 1, c, i + 1) or \
          dfs(r, c + 1, i + 1) or \
          dfs(r, c - 1, i + 1)
      path.remove((r,c))

      return isExist

    return any(dfs(i, j, 0) for i in range(ROWS) for j in range(COLS))