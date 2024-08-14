# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        
        head = head.next
        
        cs = 0
        
        while head is not None:
            if head.val == 0:
                if cs > 0:
                    current.next = ListNode(cs)
                    current = current.next
                cs = 0
            else:
                cs += head.val
            
            head = head.next
        
        return dummy.next
 