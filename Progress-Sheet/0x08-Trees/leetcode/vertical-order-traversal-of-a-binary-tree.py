# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []


        def dfs(node, col, row):
            if not node:
                return
            columns[col].append((row, node.val))
            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)

       
        columns = defaultdict(list)
        
        dfs(root, 0, 0)
        print(columns)

        result = []
        columnsS = sorted(columns)
        for col in columnsS:
            # print(columns[col])
            
            sorted_each = sorted(columns[col])

            result_col = [val for row, val in sorted_each]
            
            result.append(result_col)

        return result