# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.totalPairs = 0

        def dfs(tree):
            # leaf node
            if not tree.left and not tree.right:
                return [1]
            
            possible = []
            if tree.left:
                left = dfs(tree.left)
                possible+=left
            if tree.right:
                right = dfs(tree.right)
                for length in possible:
                    for length2 in right:
                        if length+length2 <= distance:
                            self.totalPairs+=1
                possible+=right
            
            return [1+length for length in possible]

        dfs(root)
        return self.totalPairs
        ################