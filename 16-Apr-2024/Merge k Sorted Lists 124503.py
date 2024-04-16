# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, x: self.val < x.val
        
        merged_head = merged_tail = ListNode()
        
        heap = [ll for ll in lists if ll is not None]
        heapify(heap)

        while heap:
            node = heappop(heap)
            if node.next:
                heappush(heap ,node.next)

            merged_tail.next = ListNode(node.val)
            merged_tail = merged_tail.next
        
        return merged_head.next
            



    
