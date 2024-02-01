# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        cur = head

        while cur:
            next_node = cur.next
            cur.next = new_list
            new_list = cur
            cur = next_node
        
        return new_list