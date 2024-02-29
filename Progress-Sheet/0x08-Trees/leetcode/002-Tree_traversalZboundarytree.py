# A binary tree node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# A simple function to print leaf nodes of a Binary Tree
def printLeaves(root):
    if root:
        printLeaves(root.left)
        if root.left is None and root.right is None:
            print(root.data)
        printLeaves(root.right)

# A function to print all left boundary nodes, except a leaf node.
# Print the nodes in top-down manner
def printBoundaryLeft(root):
    if root:
        if root.left:
            print(root.data)
            printBoundaryLeft(root.left)
        elif root.right:
            print(root.data)
            printBoundaryLeft(root.right)

# A function to print all right boundary nodes, except a leaf node.
# Print the nodes in bottom-up manner
def printBoundaryRight(root):
    if root:
        if root.right:
            printBoundaryRight(root.right)
            print(root.data)
        elif root.left:
            printBoundaryRight(root.left)
            print(root.data)

# A function to do boundary traversal of a given binary tree
def printBoundary(root):
    if root:
        print(root.data)
        printBoundaryLeft(root.left)
        printLeaves(root.left)
        printLeaves(root.right)
        printBoundaryRight(root.right)

# Driver program to test the code
root = TreeNode(20)
root.left = TreeNode(8)
root.left.left = TreeNode(4)
root.left.right = TreeNode(12)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)
root.right = TreeNode(22)
root.right.right = TreeNode(25)

printBoundary(root)