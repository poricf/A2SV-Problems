# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time Complexity :  O(n)
# Space Complexity : O(1)
class Solution(object):
    def middleNode(self, head):
      
        temp = head
        while temp and temp.next:
          
            head = head.next
            temp = temp.next.next
        
        return head