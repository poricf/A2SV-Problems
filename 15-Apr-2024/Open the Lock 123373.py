# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def neighbour(lock):
            res = []
            for i in range(4):
                plus = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + plus + lock[i+1:])
                plus = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + plus + lock[i+1:])
            # print(res)
            return res
        visited = set(deadends)

        if "0000" in visited:
             return -1

        q = deque()
        q.append(("0000",0))

        while q:
            node , moves = q.popleft()

            if node == target:
                return moves
            
            for nb in neighbour(node):
                if nb not in visited:
                    q.append((nb,moves + 1))
                    visited.add(nb)
        
        return -1

