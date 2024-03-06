# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: If the list is empty, simply return the head
        if not head:
            return head

        current = head

        while current and current.next:

            # Find the next distinct element by skipping duplicates
            next_distinct = current.next

            while next_distinct and current.val == next_distinct.val:
                next_distinct = next_distinct.next

            # Link the current node to the next distinct node
            current.next = next_distinct

            # Move to the next node in the list
            current = next_distinct
        

        return head