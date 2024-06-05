# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        nums = []
        while cur:
            nums.append(cur.val)
            cur = cur.next
        
        i = 0
        j = len(nums) - 1
        ans = 0
        while i < j:
            ans = max(ans,nums[i] + nums[j])
            i += 1
            j -= 1
        
        return ans
            