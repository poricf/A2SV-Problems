# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        current = head

        while current and current.next:

            next_distinct = current.next

            while next_distinct and current.val == next_distinct.val:
                next_distinct = next_distinct.next

            current.next = next_distinct

            current = next_distinct
        

        return head