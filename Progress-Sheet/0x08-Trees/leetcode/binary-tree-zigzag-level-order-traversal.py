from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result

        q = []
        q.append(root)
        leftToRight = True

        while len(q) > 0:
            size = len(q)
            row = [0] * size
            for i in range(size):
                node = q.pop(0)

                # find position to fill node's value
                index = i if leftToRight else (size - 1 - i)

                row[index] = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # after this level
            leftToRight = not leftToRight
            result.append(row)

        return result

# def main():
#     root = TreeNode(3)
#     root.left = TreeNode(9)
#     root.right = TreeNode(20)
#     root.right.left = TreeNode(15)
#     root.right.right = TreeNode(7)

#     solution = Solution()
#     ans = solution.zigzagLevelOrder(root)

#     print("Zig Zag Traversal of Binary Tree")
#     for row in    