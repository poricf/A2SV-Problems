from collections import deque   
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def morrisTraversal(root):
    if root is None:
        return []

    result = []
    current = root

    while current:
        if current.left is None:
            result.append(current.val)
            current = current.right
        else:
            predecessor = current.left

            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                result.append(current.val)
                current = current.right

    return result

def diagonalTraversal(root):
    if root is None:
        return []

    result = []
    queue = deque([(root, 0)])

    while queue:
        node, level = queue.popleft()

        # Add the node value to the result list
        result.append(node.val)

        # Traverse the right child if it exists
        if node.right:
            queue.append((node.right, level))

        # Traverse the left child if it exists
        if node.left:
            queue.append((node.left, level + 1))

    return result


# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Performing diagonal traversal
result = diagonalTraversal(root)

# Printing the result
print("Diagonal Traversal:", result)
# Performing Morris traversal
result = morrisTraversal(root)

# Printing the result
print("Morris Traversal:", result)

