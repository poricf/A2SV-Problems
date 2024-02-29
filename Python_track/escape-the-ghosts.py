class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        players_move = (abs(target[0])) + abs(target[1]) 

        for ghost in ghosts:
            ghostmove = (abs(target[0] - ghost[0])) + (abs(target[1] - ghost[1])) 
            if ghostmove <= players_move  :
                return False
            
        return True
