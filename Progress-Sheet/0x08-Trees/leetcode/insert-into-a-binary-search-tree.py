# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

# Example usage
# Creating a binary search tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

# Creating an instance of the Solution class
solution = Solution()

# Inserting a new value into the binary search tree
new_val = 5
new_root = solution.insertIntoBST(root, new_val)

# Printing the new binary search tree
print("Inorder Traversal of the New BST:")
def inorder_traversal(node):
    if not node:
        return
    inorder_traversal(node.left)
    print(node.val, end=" ")
    inorder_traversal(node.right)

inorder_traversal(new_root)
