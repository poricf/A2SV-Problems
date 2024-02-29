from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return []
        
        result = []
        stack = []
        current = root
        
        while current or stack:
            while current:
                result.append(current.val)  # Preorder: append node value before traversing children
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            current = current.right
        
        return result
    
    def inorderTraversal(self, root):
        if root is None:
            return []
        
        result = []
        stack = []
        current = root
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.val)  # Inorder: append node value after traversing left subtree
            current = current.right
        
        return result
    
    def postorderTraversal(self, root):
        if root is None:
            return []
        
        result = []
        stack = []
        current = root
        last_visited = None
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack[-1]
            
            if current.right is None or current.right == last_visited:
                result.append(current.val)  # Postorder: append node value after traversing both subtrees
                stack.pop()
                last_visited = current
                current = None
            else:
                current = current.right
        
        return result
    
    def dfs(self, root):
        if root is None:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    def bfs(self, root):
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result


# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Creating an instance of the Solution class
solution = Solution()

# Performing traversals
preorder_result = solution.preorderTraversal(root)
inorder_result = solution.inorderTraversal(root)
postorder_result = solution.postorderTraversal(root)
dfs_result = solution.dfs(root)
bfs_result = solution.bfs(root)

# Printing the results
print("Preorder Traversal:", preorder_result)
print("Inorder Traversal:", inorder_result)
print("Postorder Traversal:", postorder_result)
print("DFS Traversal:", dfs_result)
print("BFS Traversal:", bfs_result)
