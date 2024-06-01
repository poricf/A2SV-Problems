# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        visited = set()
        visited.add(root)
        ans = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                for nb in node.children:
                    if nb not in visited:
                        q.append(nb)
                        visited.add(nb)
            ans += 1
        
        return ans
                
