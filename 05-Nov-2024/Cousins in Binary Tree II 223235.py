# Problem: Cousins in Binary Tree II - https://leetcode.com/problems/cousins-in-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        q = deque()
        q.append((root,0))
        while q:
            n = len(q)
            level_sum = 0
            levels = []
            for _ in range(n):
                node , brother = q.popleft()
                level_sum += node.val
                levels.append((node , brother + node.val))
                lv , rv = 0 , 0
                if node.left:
                    if node.right:
                        rv = node.right.val
                    q.append((node.left,rv))
                if node.right:
                    if node.left:
                        lv = node.left.val
                    q.append((node.right,lv))
                
            
            for node , sibling_sum in levels:
                node.val = level_sum - (sibling_sum) 

        return root
            

                

            
            