# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        visible = {}
        def dfs(root, level):
            if not root:
                return
            dfs(root.left, level+1)
            visible[level] = root.val
            dfs(root.right, level+1)
    
# this function will run the dfs function

        dfs(root, 0)
        view = []
        for i in sorted(visible.keys()):
            view.append(visible[i])
        
        return view