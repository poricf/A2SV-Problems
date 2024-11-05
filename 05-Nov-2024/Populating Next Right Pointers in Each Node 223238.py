# Problem: Populating Next Right Pointers in Each Node - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque()
        queue.append(root)

        while queue:
            q = len(queue)
            for i in range(q):
                node = queue.popleft()
                if i != q - 1:
                    node.next = queue[0]
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        
        return root
