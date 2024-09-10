# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [[root,False]]
        heights = defaultdict(int)

        while stack:
            x , visited = stack.pop()

            if visited:
                leftheight = heights[x.left]
                rightheight = heights[x.right]

                if abs(rightheight - leftheight) > 1:
                    return False
                heights[x] = max(leftheight,rightheight) + 1

            else:
                stack.append([x,True])
                if x.right:
                    stack.append([x.right,False])
                if x.left:
                    stack.append([x.left,False])

        return True

        

        


        

            