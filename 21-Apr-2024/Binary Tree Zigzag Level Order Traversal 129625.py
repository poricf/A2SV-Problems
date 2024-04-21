# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()

        q.append(root)
        ans = []
        cnt = 0
        while q:
            Clevel = []
            for i in range(len(q)):
                node = q.popleft()
                if node: 
                    Clevel.append(node.val)
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
            
            cnt += 1
            if cnt%2:
                if Clevel: ans.append(Clevel)
            else:
                if Clevel: ans.append(reversed(Clevel))
        return ans

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