# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}  # Dictionary to store parent nodes
        def markParents(root):
            queue = deque([root])
            while queue:
                curr = queue.popleft()
                if curr.left:
                    parent[curr.left] = curr
                    queue.append(curr.left)
                if curr.right:
                    parent[curr.right] = curr
                    queue.append(curr.right)
        
        markParents(root)
        vis = {}  # Dictionary to track visited nodes
        q = deque([target])
        vis[target] = True
        curr = 0

        while q:
            size = len(q)
            if curr == k:
                break
            for _ in range(size):
                node = q.popleft()
                if node.left and node.left not in vis:
                    q.append(node.left)
                    vis[node.left] = True
                if node.right and node.right not in vis:
                    q.append(node.right)
                    vis[node.right] = True
                if node in parent and parent[node] not in vis:
                    q.append(parent[node])
                    vis[parent[node]] = True
            curr += 1

        return [node.val for node in q]

    