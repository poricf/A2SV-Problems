# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def Symmetric(a,b):
            if type(a) == TreeNode and type(b) == TreeNode:
                if a.val == b.val:
                    one = Symmetric(a.left,b.right)
                    two = Symmetric(a.right,b.left)
                    return one and two
            else:
                return a==b

        
        return Symmetric(root.left,root.right)