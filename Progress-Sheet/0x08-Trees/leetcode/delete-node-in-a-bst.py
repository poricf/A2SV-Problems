# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def deleteNode(self, root, key):
        
        def MinNode(node):
            while node.left:
                node = node.left
            return node

        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                minNode = MinNode(root.right)
                root.val = minNode.val

                root.right = self.deleteNode(root.right,minNode.val)
               

        return root