# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        a=[]
        def treePath(x):
            if x==None:
                return
            if x.val==head.val:
                a.append(x)
            treePath(x.left)
            treePath(x.right)

        treePath(root)

        if len(a)==0:
            return False

        def check(p,q):
            if q==None:
                return True
            if p==None or p.val!=q.val:
                return False
            x = check(p.left,q.next)
            y = check(p.right,q.next)
            return x or y

        for i in range(len(a)):
            x = check(a[i],head)
            if x is True:
                return True
        return False

             
        