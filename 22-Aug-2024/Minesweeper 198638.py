# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

import collections
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return board
        
        m = len(board)
        n = len(board[0])

        changes = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        def count_mines(x, y):
            count = 0
            for change in changes:
                new_x, new_y = x + change[0], y + change[1]
                if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == "M":
                    count += 1
            
            return count
                    

        q = collections.deque()
        x, y = click[0], click[1]
        if board[x][y] == "M":
            board[x][y] = "X"
            return board
        else:
            mines_around = count_mines(x, y)
            print("Total mines %s" % mines_around)
            if mines_around > 0:
                board[x][y] = str(mines_around)
                return board
            else:
                board[x][y] = "B"
                q.append((x, y))
        
        while q:
            start = q.popleft()
            curr_x, curr_y = start[0], start[1]
            for change in changes:
                new_x, new_y = curr_x + change[0], curr_y + change[1]
                if 0 <= new_x < m and 0 <= new_y < n:
                    print("Checking adjacent: %s, %s" % (new_x, new_y))
                    if board[new_x][new_y].isnumeric() or board[new_x][new_y] == 'B':
                        continue
                    elif board[new_x][new_y] == 'E':
                        mines_around = count_mines(new_x, new_y)
                        if mines_around > 0:
                            board[new_x][new_y] = str(mines_around)
                        else:
                            board[new_x][new_y] = 'B'
                            q. append((new_x, new_y))
                else:
                    continue

        return board


        

        
        #####################