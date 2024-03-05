from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preOrder(root):
    ans = []
    if root:
        ans.append(root.val)
        ans.extend(preOrder(root.left))
        ans.extend(preOrder(root.right))
    return ans

def inOrder(root):
    ans = []
    if root:
        ans.extend(inOrder(root.left))
        ans.append(root.val)
        ans.extend(inOrder(root.right))
    return ans

def postOrder(root):
    ans = []
    if root:
        ans.extend(postOrder(root.left))
        ans.extend(postOrder(root.right))
        ans.append(root.val)
    return ans




def bfs_recursive(queue):
    if not queue:
        return []

    node = queue.popleft()
    result.append(node.val)

    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)

    bfs_recursive(queue)

    return result

def dfs_recursive(node):
    result = []
    
    def traverse(node):
        if node:
            result.append(node.val)  # First, add the data of the node
            traverse(node.left)      # Then, recur on the left child
            traverse(node.right)     # Finally, recur on the right child
    
    traverse(node)
    return result



# Example usage
# Creating a binary tree
root = TreeNode(1) 
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Performing traversals
print("Preorder Traversal:", preOrder(root))
print("Inorder Traversal:", inOrder(root))
print("Postorder Traversal:", postOrder(root))
print("DFS Traversal (Recursive):", dfs_recursive(root))


queue = deque([root])
result = []

# Performing BFS traversal recursively
print("BFS Traversal (Recursive):", bfs_recursive(queue))

