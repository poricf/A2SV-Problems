class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        1)It initializes an empty list called "res", which will be used to store all 
        the valid elements in the board.

        2)It loops through each cell in the board using two nested "for" loops.
        For each cell, it retrieves the value of the element in that cell and stores 
        it in a variable called "element".

        3)If the element is not a dot ('.'), which means it's a valid number, 
        the method adds three tuples to the "res" list:

        The first tuple contains the row index (i) and the element itself.
        The second tuple contains the element itself and the column index (j).
        The third tuple contains the floor division of the row index by 3 (i // 3), the floor division of the column index by 3 (j // 3), and the element itself. This tuple represents the 3x3 sub-grid that the current cell belongs to.
        
        4)After processing all the cells, the method checks if the length of "res" is 
        equal to the length of the set of "res".
        
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    target = board[i][j]
                    target_i,target_j = i,j
                else:
                    continue
            
                for k in range(9):
                    if target_j == k:
                        continue
                    else:
                        if target == board[i][k]:
                            print("j")
                            return False
                
                for l in range(9):
                    if target_i == l:
                        continue
                    else:
                        if target == board[l][j]:
                            return False
                
                for n in range(9):
                    for m in range(9):
                        if n == target_i and m == target_j:
                            continue
                        
                        if n//3 == target_i//3 and m//3 == target_j//3:
                            if target == board[n][m]:
                                return False
        return True

        '''
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))